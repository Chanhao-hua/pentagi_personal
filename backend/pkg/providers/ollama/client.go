package ollama

import (
	"bufio"
	"bytes"
	"context"
	"encoding/hex"
	"encoding/json"
	"errors"
	"fmt"
	"hash/crc32"
	"io"
	"net/http"
	"net/url"
	"os"
	"strconv"
	"strings"

	"github.com/vxcontrol/langchaingo/llms"
	"github.com/vxcontrol/langchaingo/llms/reasoning"
	"github.com/vxcontrol/langchaingo/llms/streaming"
)

const defaultServerURL = "http://localhost:11434"

var (
	errEmptyResponse       = errors.New("no response")
	errIncompleteEmbedding = errors.New("not all input got embedded")
)

type statusError struct {
	statusCode int
	body       string
}

func (e *statusError) Error() string {
	if e.body == "" {
		return fmt.Sprintf("ollama api returned status %d", e.statusCode)
	}
	return fmt.Sprintf("ollama api returned status %d: %s", e.statusCode, e.body)
}

type Client struct {
	baseURL    *url.URL
	httpClient *http.Client
	apiKey     string
	model      string
}

func NewClient(serverURL string, httpClient *http.Client, apiKey string, model string) (*Client, error) {
	if serverURL == "" {
		serverURL = defaultServerURL
	}
	if httpClient == nil {
		httpClient = http.DefaultClient
	}
	if apiKey == "" {
		apiKey = os.Getenv("OLLAMA_API_KEY")
	}

	parsedURL, err := url.Parse(serverURL)
	if err != nil {
		return nil, fmt.Errorf("failed to parse Ollama server URL: %w", err)
	}

	return &Client{
		baseURL:    parsedURL,
		httpClient: httpClient,
		apiKey:     apiKey,
		model:      model,
	}, nil
}

func (c *Client) Call(ctx context.Context, prompt string, options ...llms.CallOption) (string, error) {
	return llms.GenerateFromSinglePrompt(ctx, c, prompt, options...)
}

func (c *Client) GenerateContent(
	ctx context.Context,
	messages []llms.MessageContent,
	options ...llms.CallOption,
) (*llms.ContentResponse, error) {
	opts := llms.CallOptions{}
	for _, opt := range options {
		opt(&opts)
	}

	model := opts.GetModel()
	if model == "" {
		model = c.model
	}

	chatMessages, err := convertMessages(messages)
	if err != nil {
		return nil, err
	}

	req, err := newChatRequest(model, chatMessages, opts)
	if err != nil {
		return nil, err
	}

	resp, err := c.chat(ctx, req, opts.StreamingFunc)
	if err != nil {
		return nil, err
	}

	return contentResponseFromChat(resp), nil
}

func (c *Client) CreateEmbedding(ctx context.Context, inputTexts []string) ([][]float32, error) {
	embeddings := make([][]float32, 0, len(inputTexts))

	for _, input := range inputTexts {
		resp := struct {
			Embedding []float64 `json:"embedding"`
		}{}
		if err := c.doJSON(ctx, http.MethodPost, "/api/embeddings", embeddingRequest{
			Model:  c.model,
			Prompt: input,
		}, &resp); err != nil {
			return nil, err
		}
		if len(resp.Embedding) == 0 {
			return nil, errEmptyResponse
		}

		embedding := make([]float32, len(resp.Embedding))
		for i, val := range resp.Embedding {
			embedding[i] = float32(val)
		}
		embeddings = append(embeddings, embedding)
	}

	if len(inputTexts) != len(embeddings) {
		return embeddings, errIncompleteEmbedding
	}
	return embeddings, nil
}

func (c *Client) List(ctx context.Context) ([]string, error) {
	resp := struct {
		Models []struct {
			Name string `json:"name"`
		} `json:"models"`
	}{}
	if err := c.doJSON(ctx, http.MethodGet, "/api/tags", nil, &resp); err != nil {
		return nil, err
	}

	models := make([]string, 0, len(resp.Models))
	for _, model := range resp.Models {
		models = append(models, model.Name)
	}
	return models, nil
}

func (c *Client) Show(ctx context.Context, model string) error {
	return c.doJSON(ctx, http.MethodPost, "/api/show", showRequest{Model: model}, nil)
}

func (c *Client) Pull(ctx context.Context, model string) error {
	stream := false
	return c.doJSON(ctx, http.MethodPost, "/api/pull", pullRequest{
		Model:  model,
		Stream: &stream,
	}, nil)
}

func (c *Client) chat(ctx context.Context, request chatRequest, streamingFunc streaming.Callback) (chatResponse, error) {
	resp, err := c.do(ctx, http.MethodPost, "/api/chat", request)
	if err != nil {
		return chatResponse{}, err
	}
	defer resp.Body.Close()

	if request.Stream != nil && *request.Stream {
		return c.readStreamingChat(ctx, resp.Body, streamingFunc)
	}

	var chatResp chatResponse
	if err := json.NewDecoder(resp.Body).Decode(&chatResp); err != nil {
		return chatResponse{}, err
	}
	return chatResp, nil
}

func (c *Client) readStreamingChat(
	ctx context.Context,
	body io.Reader,
	streamingFunc streaming.Callback,
) (chatResponse, error) {
	defer streaming.CallWithDone(ctx, streamingFunc) //nolint:errcheck

	var (
		finalResp         chatResponse
		streamedResponse  string
		streamedToolCalls []toolCall
	)
	splitter := reasoning.NewChunkContentSplitter()
	scanner := bufio.NewScanner(body)
	scanner.Buffer(make([]byte, 0, 64*1024), 10*1024*1024)
	for scanner.Scan() {
		line := bytes.TrimSpace(scanner.Bytes())
		if len(line) == 0 {
			continue
		}

		var chunk chatResponse
		if err := json.Unmarshal(line, &chunk); err != nil {
			return chatResponse{}, err
		}

		textContent, reasoningContent := splitter.Split(chunk.Message.Content)
		if err := streaming.CallWithReasoning(ctx, streamingFunc, &reasoning.ContentReasoning{
			Content: reasoningContent,
		}); err != nil {
			return chatResponse{}, fmt.Errorf("error calling streaming reasoning: %w", err)
		}
		if err := streaming.CallWithText(ctx, streamingFunc, textContent); err != nil {
			return chatResponse{}, fmt.Errorf("error calling streaming text: %w", err)
		}

		for _, tc := range chunk.Message.ToolCalls {
			toolCallID := makeToolCallID(tc.Function.Index, tc.Function.Name)
			toolCallArgs, err := tc.Function.Arguments.String()
			if err != nil {
				return chatResponse{}, fmt.Errorf("error marshalling tool call '%s' arguments: %w", toolCallID, err)
			}
			toolCall := streaming.NewToolCall(toolCallID, tc.Function.Name, toolCallArgs)
			if err := streaming.CallWithToolCall(ctx, streamingFunc, toolCall); err != nil {
				return chatResponse{}, fmt.Errorf("error calling streaming tool call '%s': %w", toolCallID, err)
			}
		}

		streamedResponse += chunk.Message.Content
		streamedToolCalls = append(streamedToolCalls, chunk.Message.ToolCalls...)
		finalResp = chunk
		if chunk.Done {
			break
		}
	}
	if err := scanner.Err(); err != nil {
		return chatResponse{}, err
	}

	finalResp.Message = message{
		Role:      "assistant",
		Content:   streamedResponse,
		ToolCalls: streamedToolCalls,
	}
	return finalResp, nil
}

func (c *Client) doJSON(ctx context.Context, method string, path string, payload any, dst any) error {
	resp, err := c.do(ctx, method, path, payload)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	if dst == nil {
		_, err = io.Copy(io.Discard, resp.Body)
		return err
	}
	return json.NewDecoder(resp.Body).Decode(dst)
}

func (c *Client) do(ctx context.Context, method string, path string, payload any) (*http.Response, error) {
	var body io.Reader
	if payload != nil {
		data, err := json.Marshal(payload)
		if err != nil {
			return nil, err
		}
		body = bytes.NewReader(data)
	}

	endpoint := c.baseURL.ResolveReference(&url.URL{Path: path})
	req, err := http.NewRequestWithContext(ctx, method, endpoint.String(), body)
	if err != nil {
		return nil, err
	}
	req.Header.Set("Accept", "application/json")
	if payload != nil {
		req.Header.Set("Content-Type", "application/json")
	}
	if c.apiKey != "" {
		req.Header.Set("Authorization", "Bearer "+c.apiKey)
	}

	resp, err := c.httpClient.Do(req)
	if err != nil {
		return nil, err
	}
	if resp.StatusCode >= 200 && resp.StatusCode < 300 {
		return resp, nil
	}
	defer resp.Body.Close()

	data, _ := io.ReadAll(io.LimitReader(resp.Body, 4096))
	return nil, &statusError{
		statusCode: resp.StatusCode,
		body:       strings.TrimSpace(string(data)),
	}
}

type showRequest struct {
	Model string `json:"model"`
}

type pullRequest struct {
	Model  string `json:"model"`
	Stream *bool  `json:"stream,omitempty"`
}

type embeddingRequest struct {
	Model  string `json:"model"`
	Prompt string `json:"prompt"`
}

type chatRequest struct {
	Model    string         `json:"model"`
	Format   any            `json:"format,omitempty"`
	Messages []message      `json:"messages"`
	Options  map[string]any `json:"options,omitempty"`
	Stream   *bool          `json:"stream,omitempty"`
	Tools    []llms.Tool    `json:"tools,omitempty"`
}

type chatResponse struct {
	Message         message `json:"message"`
	Done            bool    `json:"done"`
	DoneReason      string  `json:"done_reason"`
	EvalCount       int     `json:"eval_count"`
	PromptEvalCount int     `json:"prompt_eval_count"`
}

type message struct {
	Role      string     `json:"role"`
	Content   string     `json:"content"`
	Images    [][]byte   `json:"images,omitempty"`
	ToolCalls []toolCall `json:"tool_calls,omitempty"`
}

type toolCall struct {
	Function toolCallFunction `json:"function"`
}

type toolCallFunction struct {
	Name      string        `json:"name"`
	Arguments toolArguments `json:"arguments"`
	Index     int           `json:"index,omitempty"`
}

type toolArguments json.RawMessage

func (a *toolArguments) UnmarshalJSON(data []byte) error {
	if len(bytes.TrimSpace(data)) == 0 || bytes.Equal(bytes.TrimSpace(data), []byte("null")) {
		*a = toolArguments([]byte("{}"))
		return nil
	}
	*a = append((*a)[0:0], data...)
	return nil
}

func (a toolArguments) MarshalJSON() ([]byte, error) {
	if len(a) == 0 {
		return []byte("{}"), nil
	}
	return a, nil
}

func (a toolArguments) String() (string, error) {
	if len(a) == 0 {
		return "{}", nil
	}
	data, err := json.Marshal(json.RawMessage(a))
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func convertMessages(messages []llms.MessageContent) ([]message, error) {
	chatMessages := make([]message, 0, len(messages))
	for _, mc := range messages {
		msg, err := convertMessageContent(mc)
		if err != nil {
			return nil, err
		}
		chatMessages = append(chatMessages, msg)
	}
	return chatMessages, nil
}

func convertMessageContent(mc llms.MessageContent) (message, error) {
	msg := message{Role: typeToRole(mc.Role)}

	var foundText bool
	for _, part := range mc.Parts {
		switch pt := part.(type) {
		case llms.TextContent:
			if foundText {
				msg.Content += "\n\nnext part of text\n\n" + pt.Text
			} else {
				foundText = true
				msg.Content = pt.Text
			}
		case llms.BinaryContent:
			msg.Images = append(msg.Images, pt.Data)
		case llms.ToolCall:
			tc, err := convertToolCall(pt)
			if err != nil {
				return message{}, err
			}
			msg.ToolCalls = append(msg.ToolCalls, tc)
		case llms.ToolCallResponse:
			msg.Content = pt.Content
		default:
			return message{}, fmt.Errorf("unsupported Ollama message part %T", part)
		}
	}

	return msg, nil
}

func convertToolCall(call llms.ToolCall) (toolCall, error) {
	tc := toolCall{
		Function: toolCallFunction{
			Name:  call.FunctionCall.Name,
			Index: parseToolCallID(call.ID),
		},
	}
	if err := json.Unmarshal([]byte(call.FunctionCall.Arguments), &tc.Function.Arguments); err != nil {
		return toolCall{}, fmt.Errorf("error unmarshalling tool call arguments: %w", err)
	}
	return tc, nil
}

func newChatRequest(model string, messages []message, opts llms.CallOptions) (chatRequest, error) {
	stream := opts.StreamingFunc != nil
	req := chatRequest{
		Model:    model,
		Messages: messages,
		Options:  makeOllamaOptions(opts),
		Stream:   &stream,
		Tools:    opts.Tools,
	}
	if opts.JSONMode {
		req.Format = "json"
	}
	return req, nil
}

func makeOllamaOptions(opts llms.CallOptions) map[string]any {
	return map[string]any{
		"num_predict":       opts.GetMaxTokens(),
		"temperature":       float32(opts.GetTemperature()),
		"stop":              opts.StopWords,
		"top_k":             opts.GetTopK(),
		"top_p":             float32(opts.GetTopP()),
		"min_p":             float32(opts.GetMinP()),
		"seed":              opts.GetSeed(),
		"repeat_penalty":    float32(opts.GetRepetitionPenalty()),
		"frequency_penalty": float32(opts.GetFrequencyPenalty()),
		"presence_penalty":  float32(opts.GetPresencePenalty()),
	}
}

func contentResponseFromChat(resp chatResponse) *llms.ContentResponse {
	responseReasoning, content := reasoning.SplitContentWithReasoning(resp.Message.Content)
	choice := &llms.ContentChoice{
		Content:    content,
		Reasoning:  responseReasoning,
		StopReason: resp.DoneReason,
		GenerationInfo: map[string]any{
			"CompletionTokens": resp.EvalCount,
			"PromptTokens":     resp.PromptEvalCount,
			"TotalTokens":      resp.EvalCount + resp.PromptEvalCount,
		},
	}

	for _, tc := range resp.Message.ToolCalls {
		args, err := tc.Function.Arguments.String()
		if err != nil {
			args = "{}"
		}
		choice.ToolCalls = append(choice.ToolCalls, llms.ToolCall{
			ID:   makeToolCallID(tc.Function.Index, tc.Function.Name),
			Type: "function",
			FunctionCall: &llms.FunctionCall{
				Name:      tc.Function.Name,
				Arguments: args,
			},
		})
	}

	return &llms.ContentResponse{Choices: []*llms.ContentChoice{choice}}
}

func typeToRole(typ llms.ChatMessageType) string {
	switch typ {
	case llms.ChatMessageTypeSystem:
		return "system"
	case llms.ChatMessageTypeAI:
		return "assistant"
	case llms.ChatMessageTypeHuman, llms.ChatMessageTypeGeneric:
		return "user"
	case llms.ChatMessageTypeFunction:
		return "function"
	case llms.ChatMessageTypeTool:
		return "tool"
	default:
		return ""
	}
}

func makeToolCallID(index int, name string) string { //nolint:gosec
	hash := crc32.NewIEEE().Sum([]byte(name))
	encHash := hex.EncodeToString(hash)
	return fmt.Sprintf("ollama-%s-%d", encHash, index)
}

func parseToolCallID(id string) int { //nolint:gosec
	fallback := func() int {
		hash := crc32.NewIEEE()
		hash.Write([]byte(id))
		return int(hash.Sum32())
	}

	parts := strings.Split(id, "-")
	if len(parts) != 3 {
		return fallback()
	}

	index, err := strconv.Atoi(parts[2])
	if err != nil {
		return fallback()
	}

	return index
}
