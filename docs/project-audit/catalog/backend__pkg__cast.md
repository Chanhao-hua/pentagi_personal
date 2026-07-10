# `backend/pkg/cast` 文件清单

本组共 `3` 个文件。

## `backend/pkg/cast/chain_ast.go`

- 文件类型：`.go`
- 大小：`37294` 字节
- 文本行数：`1200`
- 所属分组：`backend/pkg/cast`
- 所属包/模块：`cast`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/cast` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`BodyPairType, ChainAST, ChainSection, Header, BodyPair, ToolCallPair, ToolCallsInfo, NewChainAST, Messages, Messages, Messages, Messages`
- 直接依赖：`backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/controller/assistant.go`, `backend/pkg/controller/flow.go`, `backend/pkg/csum/chain_summary.go`, `backend/pkg/csum/chain_summary_e2e_test.go`, `backend/pkg/csum/chain_summary_reasoning_test.go`, `backend/pkg/csum/chain_summary_split_test.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/helpers_test.go`, `backend/pkg/providers/performer.go`, `backend/pkg/providers/performers.go` 等 14 项
- 备注：长文件（1200 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/cast/chain_ast_test.go`

- 文件类型：`.go`
- 大小：`101321` 字节
- 文本行数：`3216`
- 所属分组：`backend/pkg/cast`
- 所属包/模块：`cast`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/cast` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`TestNewChainAST_EmptyChain, TestNewChainAST_BasicChains, TestNewChainAST_ToolCallChains, TestNewChainAST_MultipleHumanMessages, TestNewChainAST_ConsecutiveHumans, TestNewChainAST_UnexpectedTool, TestAddToolResponse, TestAppendHumanMessage, TestGeneratedChains, TestComplexGeneratedChains, TestMessages, TestConstructors`
- 直接依赖：`backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/controller/assistant.go`, `backend/pkg/controller/flow.go`, `backend/pkg/csum/chain_summary.go`, `backend/pkg/csum/chain_summary_e2e_test.go`, `backend/pkg/csum/chain_summary_reasoning_test.go`, `backend/pkg/csum/chain_summary_split_test.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/helpers_test.go`, `backend/pkg/providers/performer.go`, `backend/pkg/providers/performers.go` 等 14 项
- 备注：测试文件，用于验证对应模块行为。；长文件（3216 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/cast/chain_data_test.go`

- 文件类型：`.go`
- 大小：`18144` 字节
- 文本行数：`643`
- 所属分组：`backend/pkg/cast`
- 所属包/模块：`cast`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/cast` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`ChainConfig, DefaultChainConfig, GenerateChain, GenerateComplexChain, DumpChainStructure`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/controller/assistant.go`, `backend/pkg/controller/flow.go`, `backend/pkg/csum/chain_summary.go`, `backend/pkg/csum/chain_summary_e2e_test.go`, `backend/pkg/csum/chain_summary_reasoning_test.go`, `backend/pkg/csum/chain_summary_split_test.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/helpers_test.go`, `backend/pkg/providers/performer.go`, `backend/pkg/providers/performers.go` 等 14 项
- 备注：测试文件，用于验证对应模块行为。
