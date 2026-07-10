# `backend/pkg/providers` 文件清单

本组共 `76` 个文件。

## `backend/pkg/providers/anthropic/anthropic.go`

- 文件类型：`.go`
- 大小：`5123` 字节
- 文本行数：`194`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`anthropic`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`AnthropicAgentModel, AnthropicToolCallIDTemplate, BuildProviderConfig, DefaultProviderConfig, DefaultModels, New, Type, Name, GetRawConfig, GetProviderConfig, GetPriceInfo, GetModels`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`, `backend/pkg/system`, `backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/providers.go`

## `backend/pkg/providers/anthropic/anthropic_test.go`

- 文件类型：`.go`
- 大小：`2683` 字节
- 文本行数：`107`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`anthropic`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestConfigLoading, TestProviderType, TestModelsLoading`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/providers.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/providers/anthropic/config.yml`

- 文件类型：`.yml`
- 大小：`2673` 字节
- 文本行数：`164`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`未识别`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/providers/anthropic/models.yml`

- 文件类型：`.yml`
- 大小：`4545` 字节
- 文本行数：`93`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`未识别`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/providers/assistant.go`

- 文件类型：`.go`
- 大小：`23350` 字节
- 文本行数：`713`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`providers`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`AssistantProvider, FlowWorker, Type, Model, Title, Language, ToolCallIDTemplate, Embedder, SetMsgChainID, SetAgentLogProvider, SetMsgLogProvider, SetFlowWorker`
- 直接依赖：`backend/pkg/cast`, `backend/pkg/csum`, `backend/pkg/database`, `backend/pkg/docker`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/providers/embeddings`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`, `backend/pkg/templates`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/subtask.go`, `backend/pkg/controller/task.go`, `backend/pkg/graph/resolver.go` 等 18 项

## `backend/pkg/providers/bedrock/bedrock.go`

- 文件类型：`.go`
- 大小：`13778` 字节
- 文本行数：`467`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`bedrock`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`BedrockAgentModel, BedrockToolCallIDTemplate, BuildProviderConfig, DefaultProviderConfig, DefaultModels, New, Type, Name, GetRawConfig, GetProviderConfig, GetPriceInfo, GetModels`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`, `backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/providers.go`

## `backend/pkg/providers/bedrock/bedrock_test.go`

- 文件类型：`.go`
- 大小：`34047` 字节
- 文本行数：`1225`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`bedrock`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestConfigLoading, TestProviderType, TestModelsLoading, TestBedrockSpecificFeatures, TestGetUsage, TestInferPropertyType, TestInferSchemaFromArguments, TestCollectToolUsageFromChain, TestRestoreMissedToolsFromChain, TestExtractToolsFromOptions, TestAuthenticationStrategies, TestAuthenticationErrors`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/providers.go`
- 备注：测试文件，用于验证对应模块行为。；长文件（1225 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/providers/bedrock/config.yml`

- 文件类型：`.yml`
- 大小：`3679` 字节
- 文本行数：`176`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`未识别`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/providers/bedrock/models.yml`

- 文件类型：`.yml`
- 大小：`7833` 字节
- 文本行数：`201`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`未识别`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/providers/custom/custom.go`

- 文件类型：`.go`
- 大小：`5252` 字节
- 文本行数：`198`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`custom`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`BuildProviderConfig, DefaultProviderConfig, New, Type, Name, GetRawConfig, GetProviderConfig, GetPriceInfo, GetModels, Model, ModelWithPrefix, Call`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`, `backend/pkg/system`, `backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/providers/providers.go`

## `backend/pkg/providers/custom/custom_test.go`

- 文件类型：`.go`
- 大小：`7170` 字节
- 文本行数：`269`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`custom`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestConfigLoading, TestProviderType, TestBuildProviderConfig, TestProviderModelsIntegration`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/providers/providers.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/providers/custom/example_test.go`

- 文件类型：`.go`
- 大小：`5069` 字节
- 文本行数：`197`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`custom`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestCustomProviderUsageModes, TestCustomProviderConfigValidation`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/providers/providers.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/providers/deepseek/config.yml`

- 文件类型：`.yml`
- 大小：`3666` 字节
- 文本行数：`198`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`未识别`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/providers/deepseek/deepseek.go`

- 文件类型：`.go`
- 大小：`5424` 字节
- 文本行数：`198`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`deepseek`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`DeepSeekAgentModel, DeepSeekToolCallIDTemplate, BuildProviderConfig, DefaultProviderConfig, DefaultModels, New, Type, Name, GetRawConfig, GetProviderConfig, GetPriceInfo, GetModels`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`, `backend/pkg/system`, `backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/providers.go`

## `backend/pkg/providers/deepseek/deepseek_test.go`

- 文件类型：`.go`
- 大小：`5335` 字节
- 文本行数：`203`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`deepseek`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestConfigLoading, TestProviderType, TestModelsLoading, TestModelWithPrefix, TestModelWithoutPrefix, TestMissingAPIKey, TestGetUsage`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/providers.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/providers/deepseek/models.yml`

- 文件类型：`.yml`
- 大小：`956` 字节
- 文本行数：`16`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`未识别`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/providers/embeddings/embedder.go`

- 文件类型：`.go`
- 大小：`9975` 字节
- 文本行数：`380`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`embeddings`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`Embedder, IsAvailable, New`
- 直接依赖：`backend/pkg/config`, `backend/pkg/observability/langfuse`, `backend/pkg/providers/ollama`, `backend/pkg/system`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/etester/main.go`, `backend/cmd/etester/tester.go`, `backend/cmd/ftester/worker/executor.go`, `backend/pkg/database/knowledge/knowledge.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/provider.go`, `backend/pkg/providers/providers.go`, `backend/pkg/tools/code.go`, `backend/pkg/tools/guide.go`, `backend/pkg/tools/search.go`, `backend/pkg/tools/tools.go`, `backend/pkg/tools/vecstore_helper.go`

## `backend/pkg/providers/embeddings/embedder_test.go`

- 文件类型：`.go`
- 大小：`8729` 字节
- 文本行数：`413`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`embeddings`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestNew_AllProviders, TestNew_UnsupportedProvider, TestNew_OpenAI_DefaultModel, TestNew_OpenAI_CustomURL, TestNew_OpenAI_FallbackToOpenAIServerURL, TestNew_OpenAI_KeyPriority, TestNew_Jina_DefaultModel, TestNew_Huggingface_DefaultModel, TestNew_GoogleAI_DefaultModel, TestNew_VoyageAI_DefaultModel, TestNew_WithBatchSizeAndStripNewLines, TestNew_HTTPClientError`
- 直接依赖：`backend/pkg/config`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/etester/main.go`, `backend/cmd/etester/tester.go`, `backend/cmd/ftester/worker/executor.go`, `backend/pkg/database/knowledge/knowledge.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/provider.go`, `backend/pkg/providers/providers.go`, `backend/pkg/tools/code.go`, `backend/pkg/tools/guide.go`, `backend/pkg/tools/search.go`, `backend/pkg/tools/tools.go`, `backend/pkg/tools/vecstore_helper.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/providers/embeddings/wrapper.go`

- 文件类型：`.go`
- 大小：`2993` 字节
- 文本行数：`113`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`embeddings`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`EmbedDocuments, EmbedQuery`
- 直接依赖：`backend/pkg/observability`, `backend/pkg/observability/langfuse`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/etester/main.go`, `backend/cmd/etester/tester.go`, `backend/cmd/ftester/worker/executor.go`, `backend/pkg/database/knowledge/knowledge.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/provider.go`, `backend/pkg/providers/providers.go`, `backend/pkg/tools/code.go`, `backend/pkg/tools/guide.go`, `backend/pkg/tools/search.go`, `backend/pkg/tools/tools.go`, `backend/pkg/tools/vecstore_helper.go`

## `backend/pkg/providers/gemini/config.yml`

- 文件类型：`.yml`
- 大小：`2525` 字节
- 文本行数：`160`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`未识别`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/providers/gemini/gemini.go`

- 文件类型：`.go`
- 大小：`5297` 字节
- 文本行数：`203`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`gemini`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`GeminiAgentModel, GeminiToolCallIDTemplate, BuildProviderConfig, DefaultProviderConfig, DefaultModels, New, Type, Name, GetRawConfig, GetProviderConfig, GetPriceInfo, GetModels`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`, `backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/providers.go`

## `backend/pkg/providers/gemini/gemini_test.go`

- 文件类型：`.go`
- 大小：`13653` 字节
- 文本行数：`479`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`gemini`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestConfigLoading, TestProviderType, TestModelsLoading, TestGeminiSpecificFeatures, TestGetUsage, TestAPIKeyTransportRoundTrip, RoundTrip, TestAPIKeyTransportWithMockServer, TestGeminiProviderWithProxyConfiguration`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/providers.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/providers/gemini/models.yml`

- 文件类型：`.yml`
- 大小：`4645` 字节
- 文本行数：`83`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`未识别`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/providers/glm/config.yml`

- 文件类型：`.yml`
- 大小：`4485` 字节
- 文本行数：`223`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`未识别`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/providers/glm/glm.go`

- 文件类型：`.go`
- 大小：`5760` 字节
- 文本行数：`202`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`glm`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`GLMAgentModel, GLMToolCallIDTemplate, BuildProviderConfig, DefaultProviderConfig, DefaultModels, New, Type, Name, GetRawConfig, GetProviderConfig, GetPriceInfo, GetModels`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`, `backend/pkg/system`, `backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/providers.go`

## `backend/pkg/providers/glm/glm_test.go`

- 文件类型：`.go`
- 大小：`5256` 字节
- 文本行数：`203`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`glm`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestConfigLoading, TestProviderType, TestModelsLoading, TestModelWithPrefix, TestModelWithoutPrefix, TestMissingAPIKey, TestGetUsage`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/providers.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/providers/glm/models.yml`

- 文件类型：`.yml`
- 大小：`3881` 字节
- 文本行数：`108`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`未识别`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/providers/handlers.go`

- 文件类型：`.go`
- 大小：`37910` 字节
- 文本行数：`993`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`providers`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`GetAskAdviceHandler, GetCoderHandler, GetInstallerHandler, GetMemoristHandler, GetPentesterHandler, GetSubtaskSearcherHandler, GetTaskSearcherHandler, GetSummarizeResultHandler`
- 直接依赖：`backend/pkg/cast`, `backend/pkg/csum`, `backend/pkg/database`, `backend/pkg/docker`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/providers/pconfig`, `backend/pkg/schema`, `backend/pkg/templates`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/subtask.go`, `backend/pkg/controller/task.go`, `backend/pkg/graph/resolver.go` 等 18 项
- 备注：长文件（993 行），属于复杂度热点，阅读时建议先看对外导出和测试。；包含 TODO，后续维护时可重点留意未完成事项。

## `backend/pkg/providers/helpers.go`

- 文件类型：`.go`
- 大小：`37080` 字节
- 文本行数：`1185`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`providers`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`backend/pkg/cast`, `backend/pkg/csum`, `backend/pkg/database`, `backend/pkg/docker`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/providers/pconfig`, `backend/pkg/templates`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/subtask.go`, `backend/pkg/controller/task.go`, `backend/pkg/graph/resolver.go` 等 18 项
- 备注：长文件（1185 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/providers/helpers_test.go`

- 文件类型：`.go`
- 大小：`37262` 字节
- 文本行数：`1276`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`providers`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestUpdateMsgChainResult, TestFindUnrespondedToolCalls, TestEnsureChainConsistency, TestRepeatingDetector, TestRepeatingDetectorEscalationThreshold, TestClearCallArguments, TestExecutionMonitorDetector_ShouldInvokeAdviser, TestExecutionMonitorDetector_Reset, TestExecutionMonitorDetector_SameToolSequence, TestExecutionMonitorDetector_TotalCallsSequence, TestWrapToolCallIDTemplateError`
- 直接依赖：`backend/pkg/cast`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/subtask.go`, `backend/pkg/controller/task.go`, `backend/pkg/graph/resolver.go` 等 18 项
- 备注：测试文件，用于验证对应模块行为。；长文件（1276 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/providers/kimi/config.yml`

- 文件类型：`.yml`
- 大小：`4382` 字节
- 文本行数：`225`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`未识别`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/providers/kimi/kimi.go`

- 文件类型：`.go`
- 大小：`5825` 字节
- 文本行数：`204`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`kimi`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`KimiAgentModel, KimiToolCallIDTemplate, BuildProviderConfig, DefaultProviderConfig, DefaultModels, New, Type, Name, GetRawConfig, GetProviderConfig, GetPriceInfo, GetModels`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`, `backend/pkg/system`, `backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/providers.go`

## `backend/pkg/providers/kimi/kimi_test.go`

- 文件类型：`.go`
- 大小：`5263` 字节
- 文本行数：`203`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`kimi`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestConfigLoading, TestProviderType, TestModelsLoading, TestModelWithPrefix, TestModelWithoutPrefix, TestMissingAPIKey, TestGetUsage`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/providers.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/providers/kimi/models.yml`

- 文件类型：`.yml`
- 大小：`2342` 字节
- 文本行数：`62`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`未识别`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/providers/ollama/client.go`

- 文件类型：`.go`
- 大小：`13783` 字节
- 文本行数：`544`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`ollama`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`Error, Client, NewClient, Call, GenerateContent, CreateEmbedding, List, Show, Pull, UnmarshalJSON, MarshalJSON, String`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/providers.go`

## `backend/pkg/providers/ollama/config.yml`

- 文件类型：`.yml`
- 大小：`1008` 字节
- 文本行数：`79`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`未识别`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/providers/ollama/ollama.go`

- 文件类型：`.go`
- 大小：`6677` 字节
- 文本行数：`279`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`ollama`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`BuildProviderConfig, DefaultProviderConfig, New, Type, Name, GetRawConfig, GetProviderConfig, GetPriceInfo, GetModels, Model, ModelWithPrefix, Call`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`, `backend/pkg/system`, `backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/providers.go`

## `backend/pkg/providers/ollama/ollama_test.go`

- 文件类型：`.go`
- 大小：`5215` 字节
- 文本行数：`188`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`ollama`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestBuildProviderConfig, TestDefaultProviderConfig, TestNew, TestOllamaProviderWithProxy, TestOllamaProviderWithCustomConfig, TestOllamaProviderPricing, TestGetUsageEdgeCases`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/providers.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/providers/openai/config.yml`

- 文件类型：`.yml`
- 大小：`2072` 字节
- 文本行数：`144`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`未识别`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/providers/openai/models.yml`

- 文件类型：`.yml`
- 大小：`12758` 字节
- 文本行数：`246`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`未识别`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/providers/openai/openai.go`

- 文件类型：`.go`
- 大小：`4723` 字节
- 文本行数：`186`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`openai`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`OpenAIAgentModel, OpenAIToolCallIDTemplate, BuildProviderConfig, DefaultProviderConfig, DefaultModels, New, Type, Name, GetRawConfig, GetProviderConfig, GetPriceInfo, GetModels`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`, `backend/pkg/system`, `backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/providers.go`

## `backend/pkg/providers/openai/openai_test.go`

- 文件类型：`.go`
- 大小：`2656` 字节
- 文本行数：`107`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`openai`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestConfigLoading, TestProviderType, TestModelsLoading`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/providers.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/providers/pconfig/config.go`

- 文件类型：`.go`
- 大小：`25313` 字节
- 文本行数：`894`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`pconfig`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`CallUsage, NewCallUsage, Fill, Merge, UpdateCost, IsZero, String, ProviderOptionsType, AllAgentTypes, ModelConfig, ModelsConfig, PriceInfo`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/flow.go`, `backend/pkg/database/converter/converter.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/graph/subscriptions/controller.go`, `backend/pkg/graph/subscriptions/publisher.go`, `backend/pkg/providers/anthropic/anthropic.go`, `backend/pkg/providers/anthropic/anthropic_test.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/bedrock/bedrock.go`, `backend/pkg/providers/bedrock/bedrock_test.go` 等 46 项
- 备注：长文件（894 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/providers/pconfig/config_test.go`

- 文件类型：`.go`
- 大小：`45473` 字节
- 文本行数：`1869`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`pconfig`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestReasoningConfig_UnmarshalJSON, TestReasoningConfig_UnmarshalYAML, TestLoadConfig, TestLoadConfig_BackwardCompatibility, TestLoadConfigData_BackwardCompatibility, TestAgentConfig_UnmarshalJSON, TestAgentConfig_UnmarshalYAML, TestAgentConfig_BuildOptions, TestProvidersConfig_GetOptionsForType, TestAgentConfig_MarshalJSON, TestAgentConfig_MarshalYAML, TestLoadConfig_WithDefaultOptions`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/flow.go`, `backend/pkg/database/converter/converter.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/graph/subscriptions/controller.go`, `backend/pkg/graph/subscriptions/publisher.go`, `backend/pkg/providers/anthropic/anthropic.go`, `backend/pkg/providers/anthropic/anthropic_test.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/bedrock/bedrock.go`, `backend/pkg/providers/bedrock/bedrock_test.go` 等 46 项
- 备注：测试文件，用于验证对应模块行为。；长文件（1869 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/providers/performer.go`

- 文件类型：`.go`
- 大小：`36485` 字节
- 文本行数：`1140`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`providers`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`backend/pkg/cast`, `backend/pkg/csum`, `backend/pkg/database`, `backend/pkg/graphiti`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/providers/pconfig`, `backend/pkg/templates`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/subtask.go`, `backend/pkg/controller/task.go`, `backend/pkg/graph/resolver.go` 等 18 项
- 备注：长文件（1140 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/providers/performers.go`

- 文件类型：`.go`
- 大小：`32942` 字节
- 文本行数：`1049`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`providers`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`backend/pkg/cast`, `backend/pkg/database`, `backend/pkg/observability`, `backend/pkg/providers/pconfig`, `backend/pkg/templates`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/subtask.go`, `backend/pkg/controller/task.go`, `backend/pkg/graph/resolver.go` 等 18 项
- 备注：长文件（1049 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/providers/provider.go`

- 文件类型：`.go`
- 大小：`33267` 字节
- 文本行数：`979`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`providers`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`ToolPlaceholder, TasksNumberLimit, PerformResult, StreamMessageChunkType, StreamMessageChunk, StreamMessageHandler, FlowProvider, FlowProviderHandlers, SetAgentLogProvider, SetMsgLogProvider, SetProvider, ID`
- 直接依赖：`backend/pkg/cast`, `backend/pkg/csum`, `backend/pkg/database`, `backend/pkg/docker`, `backend/pkg/flowfiles`, `backend/pkg/graphiti`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/providers/embeddings`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`, `backend/pkg/templates` 等 13 项
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/subtask.go`, `backend/pkg/controller/task.go`, `backend/pkg/graph/resolver.go` 等 18 项
- 备注：长文件（979 行），属于复杂度热点，阅读时建议先看对外导出和测试。；包含 TODO，后续维护时可重点留意未完成事项。

## `backend/pkg/providers/provider/agents.go`

- 文件类型：`.go`
- 大小：`18530` 字节
- 文本行数：`708`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`provider`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`DetermineToolCallIDTemplate`
- 直接依赖：`backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/providers/pconfig`, `backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/anthropic/anthropic.go`, `backend/pkg/providers/anthropic/anthropic_test.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/bedrock/bedrock.go`, `backend/pkg/providers/bedrock/bedrock_test.go` 等 38 项

## `backend/pkg/providers/provider/agents_test.go`

- 文件类型：`.go`
- 大小：`5183` 字节
- 文本行数：`222`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`provider`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestFallbackHeuristicDetection, TestDetermineMinimalCharset, TestDetermineCommonCharset`
- 直接依赖：`backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/anthropic/anthropic.go`, `backend/pkg/providers/anthropic/anthropic_test.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/bedrock/bedrock.go`, `backend/pkg/providers/bedrock/bedrock_test.go` 等 38 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/providers/provider/litellm.go`

- 文件类型：`.go`
- 大小：`6301` 字节
- 文本行数：`209`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`provider`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`ApplyModelPrefix, RemoveModelPrefix, LoadModelsFromHTTP`
- 直接依赖：`backend/pkg/providers/pconfig`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/anthropic/anthropic.go`, `backend/pkg/providers/anthropic/anthropic_test.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/bedrock/bedrock.go`, `backend/pkg/providers/bedrock/bedrock_test.go` 等 38 项

## `backend/pkg/providers/provider/litellm_test.go`

- 文件类型：`.go`
- 大小：`16134` 字节
- 文本行数：`579`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`provider`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestApplyModelPrefix, TestRemoveModelPrefix, TestLoadModelsFromYAML, TestLoadModelsFromHTTP_WithoutPrefix, TestLoadModelsFromHTTP_WithPrefix, TestLoadModelsFromHTTP_FallbackParsing, TestLoadModelsFromHTTP_SkipModelsWithoutTools, TestLoadModelsFromHTTP_Errors, TestEndToEndProviderSimulation`
- 直接依赖：`backend/pkg/providers/pconfig`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/anthropic/anthropic.go`, `backend/pkg/providers/anthropic/anthropic_test.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/bedrock/bedrock.go`, `backend/pkg/providers/bedrock/bedrock_test.go` 等 38 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/providers/provider/provider.go`

- 文件类型：`.go`
- 大小：`4440` 字节
- 文本行数：`155`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`provider`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`ProviderType, String, ProviderName, String, Provider, Contains, Contains, Get, ListNames, ListTypes`
- 直接依赖：`backend/pkg/providers/pconfig`, `backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/anthropic/anthropic.go`, `backend/pkg/providers/anthropic/anthropic_test.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/bedrock/bedrock.go`, `backend/pkg/providers/bedrock/bedrock_test.go` 等 38 项

## `backend/pkg/providers/provider/wrapper.go`

- 文件类型：`.go`
- 大小：`12070` 字节
- 文本行数：`403`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`provider`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`GenerateContentFunc, WrapGenerateFromSinglePrompt, WrapGenerateContent`
- 直接依赖：`backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/providers/pconfig`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/anthropic/anthropic.go`, `backend/pkg/providers/anthropic/anthropic_test.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/bedrock/bedrock.go`, `backend/pkg/providers/bedrock/bedrock_test.go` 等 38 项

## `backend/pkg/providers/providers.go`

- 文件类型：`.go`
- 大小：`37467` 字节
- 文本行数：`1200`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`providers`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`ProviderController, NewProviderController, NewFlowProvider, LoadFlowProvider, Embedder, GraphitiClient, NewAssistantProvider, LoadAssistantProvider, DefaultProviders, DefaultProvidersConfig, GetProvider, GetProviders`
- 直接依赖：`backend/pkg/config`, `backend/pkg/csum`, `backend/pkg/database`, `backend/pkg/docker`, `backend/pkg/graphiti`, `backend/pkg/observability`, `backend/pkg/providers/anthropic`, `backend/pkg/providers/bedrock`, `backend/pkg/providers/custom`, `backend/pkg/providers/deepseek`, `backend/pkg/providers/embeddings`, `backend/pkg/providers/gemini` 等 22 项
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/subtask.go`, `backend/pkg/controller/task.go`, `backend/pkg/graph/resolver.go` 等 18 项
- 备注：长文件（1200 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/providers/qwen/config.yml`

- 文件类型：`.yml`
- 大小：`4084` 字节
- 文本行数：`181`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`未识别`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/providers/qwen/models.yml`

- 文件类型：`.yml`
- 大小：`12219` 字节
- 文本行数：`273`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`未识别`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/providers/qwen/qwen.go`

- 文件类型：`.go`
- 大小：`5592` 字节
- 文本行数：`202`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`qwen`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`QwenAgentModel, QwenToolCallIDTemplate, BuildProviderConfig, DefaultProviderConfig, DefaultModels, New, Type, Name, GetRawConfig, GetProviderConfig, GetPriceInfo, GetModels`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`, `backend/pkg/system`, `backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/providers.go`

## `backend/pkg/providers/qwen/qwen_test.go`

- 文件类型：`.go`
- 大小：`5415` 字节
- 文本行数：`203`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`qwen`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestConfigLoading, TestProviderType, TestModelsLoading, TestModelWithPrefix, TestModelWithoutPrefix, TestMissingAPIKey, TestGetUsage`
- 直接依赖：`backend/pkg/config`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/providers.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/providers/subtask_patch.go`

- 文件类型：`.go`
- 大小：`10142` 字节
- 文本行数：`338`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`providers`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`backend/pkg/database`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/subtask.go`, `backend/pkg/controller/task.go`, `backend/pkg/graph/resolver.go` 等 18 项

## `backend/pkg/providers/subtask_patch_test.go`

- 文件类型：`.go`
- 大小：`40494` 字节
- 文本行数：`1242`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`providers`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestApplySubtaskOperations_EmptyPatch, TestApplySubtaskOperations_RemoveOperation, TestApplySubtaskOperations_RemoveMultiple, TestApplySubtaskOperations_RemoveNonExistent, TestApplySubtaskOperations_ModifyTitle, TestApplySubtaskOperations_ModifyDescription, TestApplySubtaskOperations_ModifyBoth, TestApplySubtaskOperations_AddAtBeginning, TestApplySubtaskOperations_AddAfterSpecific, TestApplySubtaskOperations_AddAfterNonExistent, TestApplySubtaskOperations_ReorderToBeginning, TestApplySubtaskOperations_ReorderAfterSpecific`
- 直接依赖：`backend/pkg/database`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/subtask.go`, `backend/pkg/controller/task.go`, `backend/pkg/graph/resolver.go` 等 18 项
- 备注：测试文件，用于验证对应模块行为。；长文件（1242 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/providers/tester/config.go`

- 文件类型：`.go`
- 大小：`2142` 字节
- 文本行数：`84`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`tester`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestOption, WithAgentTypes, WithGroups, WithStreamingMode, WithVerbose, WithParallelWorkers, WithCustomRegistry`
- 直接依赖：`backend/pkg/providers/pconfig`, `backend/pkg/providers/tester/testdata`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/database/converter/converter.go`, `backend/pkg/providers/providers.go`

## `backend/pkg/providers/tester/mock/provider.go`

- 文件类型：`.go`
- 大小：`8518` 字节
- 文本行数：`332`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`mock`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`Provider, ResponseConfig, NewProvider, SetResponses, SetDefaultResponse, SetStreamingDelay, Type, Name, Model, ModelWithPrefix, GetUsage, GetModels`
- 直接依赖：`backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`, `backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/providers/tester/runner_test.go`

## `backend/pkg/providers/tester/result.go`

- 文件类型：`.go`
- 大小：`815` 字节
- 文本行数：`24`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`tester`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`AgentTestResults, ProviderTestResults`
- 直接依赖：`backend/pkg/providers/tester/testdata`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/database/converter/converter.go`, `backend/pkg/providers/providers.go`

## `backend/pkg/providers/tester/runner.go`

- 文件类型：`.go`
- 大小：`7948` 字节
- 文本行数：`275`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`tester`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestProvider`
- 直接依赖：`backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`, `backend/pkg/providers/tester/testdata`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/database/converter/converter.go`, `backend/pkg/providers/providers.go`

## `backend/pkg/providers/tester/runner_test.go`

- 文件类型：`.go`
- 大小：`10965` 字节
- 文本行数：`376`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`tester`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestTestProvider, TestTestProviderWithOptions, TestTestProviderStreamingMode, TestTestProviderJSONTests, TestTestProviderToolTests, TestTestProviderErrorHandling, TestTestProviderGroups, TestApplyOptions`
- 直接依赖：`backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`, `backend/pkg/providers/tester/mock`, `backend/pkg/providers/tester/testdata`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/database/converter/converter.go`, `backend/pkg/providers/providers.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/providers/tester/testdata/completion.go`

- 文件类型：`.go`
- 大小：`8496` 字节
- 文本行数：`304`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`testdata`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`ID, Name, Type, Group, Streaming, Prompt, Messages, Tools, StreamingCallback, Execute`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/database/converter/converter.go`, `backend/pkg/providers/tester/config.go`, `backend/pkg/providers/tester/result.go`, `backend/pkg/providers/tester/runner.go`, `backend/pkg/providers/tester/runner_test.go`

## `backend/pkg/providers/tester/testdata/completion_test.go`

- 文件类型：`.go`
- 大小：`9820` 字节
- 文本行数：`290`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`testdata`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestCompletionTestCase, TestContainsString, TestStringModifiers, TestModifierCombinations`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/database/converter/converter.go`, `backend/pkg/providers/tester/config.go`, `backend/pkg/providers/tester/result.go`, `backend/pkg/providers/tester/runner.go`, `backend/pkg/providers/tester/runner_test.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/providers/tester/testdata/json.go`

- 文件类型：`.go`
- 大小：`5491` 字节
- 文本行数：`198`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`testdata`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`ID, Name, Type, Group, Streaming, Prompt, Messages, Tools, StreamingCallback, Execute`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/database/converter/converter.go`, `backend/pkg/providers/tester/config.go`, `backend/pkg/providers/tester/result.go`, `backend/pkg/providers/tester/runner.go`, `backend/pkg/providers/tester/runner_test.go`

## `backend/pkg/providers/tester/testdata/json_test.go`

- 文件类型：`.go`
- 大小：`3221` 字节
- 文本行数：`114`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`testdata`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestJSONTestCase, TestJSONValueValidation`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/database/converter/converter.go`, `backend/pkg/providers/tester/config.go`, `backend/pkg/providers/tester/result.go`, `backend/pkg/providers/tester/runner.go`, `backend/pkg/providers/tester/runner_test.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/providers/tester/testdata/models.go`

- 文件类型：`.go`
- 大小：`4427` 字节
- 文本行数：`166`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`testdata`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestType, TestGroup, MessagesData, ToMessageContent, TestDefinition, MessageData, ToolCallData, FunctionCallData, ToolData, ExpectedToolCall, TestCase, TestSuite`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/database/converter/converter.go`, `backend/pkg/providers/tester/config.go`, `backend/pkg/providers/tester/result.go`, `backend/pkg/providers/tester/runner.go`, `backend/pkg/providers/tester/runner_test.go`

## `backend/pkg/providers/tester/testdata/registry.go`

- 文件类型：`.go`
- 大小：`2589` 字节
- 文本行数：`96`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`testdata`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestRegistry, LoadBuiltinRegistry, LoadRegistryFromYAML, GetTestSuite, GetTestsByGroup, GetTestsByType, GetAllTests`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/database/converter/converter.go`, `backend/pkg/providers/tester/config.go`, `backend/pkg/providers/tester/result.go`, `backend/pkg/providers/tester/runner.go`, `backend/pkg/providers/tester/runner_test.go`

## `backend/pkg/providers/tester/testdata/registry_test.go`

- 文件类型：`.go`
- 大小：`11470` 字节
- 文本行数：`417`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`testdata`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestRegistryLoad, TestTestSuiteCreation, TestRegistryErrors, TestBuiltinRegistry, TestRegistryExtendedMessageTests`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/database/converter/converter.go`, `backend/pkg/providers/tester/config.go`, `backend/pkg/providers/tester/result.go`, `backend/pkg/providers/tester/runner.go`, `backend/pkg/providers/tester/runner_test.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/providers/tester/testdata/result.go`

- 文件类型：`.go`
- 大小：`506` 字节
- 文本行数：`17`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`testdata`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestResult`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/database/converter/converter.go`, `backend/pkg/providers/tester/config.go`, `backend/pkg/providers/tester/result.go`, `backend/pkg/providers/tester/runner.go`, `backend/pkg/providers/tester/runner_test.go`

## `backend/pkg/providers/tester/testdata/tests.yml`

- 文件类型：`.yml`
- 大小：`23737` 字节
- 文本行数：`731`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`未识别`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/providers/tester/testdata/tool.go`

- 文件类型：`.go`
- 大小：`13033` 字节
- 文本行数：`436`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`testdata`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`ID, Name, Type, Group, Streaming, Prompt, Messages, Tools, StreamingCallback, Execute`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/database/converter/converter.go`, `backend/pkg/providers/tester/config.go`, `backend/pkg/providers/tester/result.go`, `backend/pkg/providers/tester/runner.go`, `backend/pkg/providers/tester/runner_test.go`

## `backend/pkg/providers/tester/testdata/tool_test.go`

- 文件类型：`.go`
- 大小：`23249` 字节
- 文本行数：`841`
- 所属分组：`backend/pkg/providers`
- 所属包/模块：`testdata`
- 推断作用：LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。
- 生成文件：`否`
- 关键导出/符号：`TestToolTestCase, TestToolTestCaseMultipleFunctions, TestValidateArgumentValue, TestCompareNumeric, TestCompareFloat, TestCompareString, TestCompareBool, TestCompareSlice, TestCompareMap, TestToolCallEnhancedValidation`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/pkg/database/converter/converter.go`, `backend/pkg/providers/tester/config.go`, `backend/pkg/providers/tester/result.go`, `backend/pkg/providers/tester/runner.go`, `backend/pkg/providers/tester/runner_test.go`
- 备注：测试文件，用于验证对应模块行为。；长文件（841 行），属于复杂度热点，阅读时建议先看对外导出和测试。
