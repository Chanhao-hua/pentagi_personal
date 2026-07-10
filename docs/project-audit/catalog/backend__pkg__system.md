# `backend/pkg/system` 文件清单

本组共 `6` 个文件。

## `backend/pkg/system/host_id.go`

- 文件类型：`.go`
- 大小：`371` 字节
- 文本行数：`17`
- 所属分组：`backend/pkg/system`
- 所属包/模块：`system`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/system` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`GetHostID`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/lfclient.go`, `backend/pkg/providers/anthropic/anthropic.go`, `backend/pkg/providers/custom/custom.go`, `backend/pkg/providers/deepseek/deepseek.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/glm/glm.go`, `backend/pkg/providers/kimi/kimi.go`, `backend/pkg/providers/ollama/ollama.go`, `backend/pkg/providers/openai/openai.go`, `backend/pkg/providers/qwen/qwen.go`, `backend/pkg/tools/duckduckgo.go`, `backend/pkg/tools/google.go` 等 17 项

## `backend/pkg/system/utils.go`

- 文件类型：`.go`
- 大小：`2499` 字节
- 文本行数：`117`
- 所属分组：`backend/pkg/system`
- 所属包/模块：`system`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/system` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`GetSystemCertPool, GetHTTPClient`
- 直接依赖：`backend/pkg/config`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/lfclient.go`, `backend/pkg/providers/anthropic/anthropic.go`, `backend/pkg/providers/custom/custom.go`, `backend/pkg/providers/deepseek/deepseek.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/glm/glm.go`, `backend/pkg/providers/kimi/kimi.go`, `backend/pkg/providers/ollama/ollama.go`, `backend/pkg/providers/openai/openai.go`, `backend/pkg/providers/qwen/qwen.go`, `backend/pkg/tools/duckduckgo.go`, `backend/pkg/tools/google.go` 等 17 项

## `backend/pkg/system/utils_darwin.go`

- 文件类型：`.go`
- 大小：`1231` 字节
- 文本行数：`59`
- 所属分组：`backend/pkg/system`
- 所属包/模块：`system`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/system` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/lfclient.go`, `backend/pkg/providers/anthropic/anthropic.go`, `backend/pkg/providers/custom/custom.go`, `backend/pkg/providers/deepseek/deepseek.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/glm/glm.go`, `backend/pkg/providers/kimi/kimi.go`, `backend/pkg/providers/ollama/ollama.go`, `backend/pkg/providers/openai/openai.go`, `backend/pkg/providers/qwen/qwen.go`, `backend/pkg/tools/duckduckgo.go`, `backend/pkg/tools/google.go` 等 17 项

## `backend/pkg/system/utils_linux.go`

- 文件类型：`.go`
- 大小：`4126` 字节
- 文本行数：`152`
- 所属分组：`backend/pkg/system`
- 所属包/模块：`system`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/system` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`Feature`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/lfclient.go`, `backend/pkg/providers/anthropic/anthropic.go`, `backend/pkg/providers/custom/custom.go`, `backend/pkg/providers/deepseek/deepseek.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/glm/glm.go`, `backend/pkg/providers/kimi/kimi.go`, `backend/pkg/providers/ollama/ollama.go`, `backend/pkg/providers/openai/openai.go`, `backend/pkg/providers/qwen/qwen.go`, `backend/pkg/tools/duckduckgo.go`, `backend/pkg/tools/google.go` 等 17 项

## `backend/pkg/system/utils_test.go`

- 文件类型：`.go`
- 大小：`21057` 字节
- 文本行数：`777`
- 所属分组：`backend/pkg/system`
- 所属包/模块：`system`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/system` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`TestGetSystemCertPool_EmptyPath, TestGetSystemCertPool_NonExistentFile, TestGetSystemCertPool_InvalidPEM, TestGetSystemCertPool_SingleRootCA, TestGetSystemCertPool_MultipleRootCAs, TestGetSystemCertPool_WithIntermediateCerts, TestGetHTTPClient_NoProxy, TestGetHTTPClient_WithProxy, TestGetHTTPClient_InsecureSkipVerify, TestHTTPClient_RealConnection_WithIntermediateInChain, TestHTTPClient_RealConnection_WithoutIntermediateInChain, TestHTTPClient_RealConnection_WithIntermediateInRootPool`
- 直接依赖：`backend/pkg/config`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/lfclient.go`, `backend/pkg/providers/anthropic/anthropic.go`, `backend/pkg/providers/custom/custom.go`, `backend/pkg/providers/deepseek/deepseek.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/glm/glm.go`, `backend/pkg/providers/kimi/kimi.go`, `backend/pkg/providers/ollama/ollama.go`, `backend/pkg/providers/openai/openai.go`, `backend/pkg/providers/qwen/qwen.go`, `backend/pkg/tools/duckduckgo.go`, `backend/pkg/tools/google.go` 等 17 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/system/utils_windows.go`

- 文件类型：`.go`
- 大小：`3539` 字节
- 文本行数：`127`
- 所属分组：`backend/pkg/system`
- 所属包/模块：`system`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/system` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/lfclient.go`, `backend/pkg/providers/anthropic/anthropic.go`, `backend/pkg/providers/custom/custom.go`, `backend/pkg/providers/deepseek/deepseek.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/glm/glm.go`, `backend/pkg/providers/kimi/kimi.go`, `backend/pkg/providers/ollama/ollama.go`, `backend/pkg/providers/openai/openai.go`, `backend/pkg/providers/qwen/qwen.go`, `backend/pkg/tools/duckduckgo.go`, `backend/pkg/tools/google.go` 等 17 项
