# `backend/pkg/csum` 文件清单

本组共 `4` 个文件。

## `backend/pkg/csum/chain_summary.go`

- 文件类型：`.go`
- 大小：`34922` 字节
- 文本行数：`1013`
- 所属分组：`backend/pkg/csum`
- 所属包/模块：`csum`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/csum` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`SummarizerConfig, Summarizer, NewSummarizer, SummarizeChain, GenerateSummary`
- 直接依赖：`backend/pkg/cast`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/models/helpers/calc_context.go`, `backend/cmd/installer/wizard/models/helpers/calc_context_test.go`, `backend/cmd/installer/wizard/models/summarizer_form.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go`, `backend/pkg/providers/provider.go`, `backend/pkg/providers/providers.go`, `backend/pkg/templates/validator/testdata.go`
- 备注：长文件（1013 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/csum/chain_summary_e2e_test.go`

- 文件类型：`.go`
- 大小：`52094` 字节
- 文本行数：`1422`
- 所属分组：`backend/pkg/csum`
- 所属包/模块：`csum`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/csum` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`TestSummarizeChain, TestSummarizationIdempotence, TestLastBodyPairPreservation, TestLastQASectionExceedsMaxQABytes`
- 直接依赖：`backend/pkg/cast`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/models/helpers/calc_context.go`, `backend/cmd/installer/wizard/models/helpers/calc_context_test.go`, `backend/cmd/installer/wizard/models/summarizer_form.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go`, `backend/pkg/providers/provider.go`, `backend/pkg/providers/providers.go`, `backend/pkg/templates/validator/testdata.go`
- 备注：测试文件，用于验证对应模块行为。；长文件（1422 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/csum/chain_summary_reasoning_test.go`

- 文件类型：`.go`
- 大小：`20564` 字节
- 文本行数：`588`
- 所属分组：`backend/pkg/csum`
- 所属包/模块：`csum`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/csum` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`TestSummarizeOversizedBodyPairs_WithReasoning, TestSummarizeOversizedBodyPairs_WithoutReasoning, TestSummarizeSections_WithReasoning, TestSummarizeLastSection_WithReasoning, TestSummarizeOversizedBodyPairs_WithReasoningMessage, TestSummarizeOversizedBodyPairs_KimiPattern`
- 直接依赖：`backend/pkg/cast`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/models/helpers/calc_context.go`, `backend/cmd/installer/wizard/models/helpers/calc_context_test.go`, `backend/cmd/installer/wizard/models/summarizer_form.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go`, `backend/pkg/providers/provider.go`, `backend/pkg/providers/providers.go`, `backend/pkg/templates/validator/testdata.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/csum/chain_summary_split_test.go`

- 文件类型：`.go`
- 大小：`79893` 字节
- 文本行数：`2131`
- 所属分组：`backend/pkg/csum`
- 所属包/模块：`csum`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/csum` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`SummarizerChecks, Summarize, ValidateChecks, SummarizerHandler, TestSummarizeSections, TestSummarizeLastSection, TestSummarizeQAPairs, TestLastBodyPairNeverSummarized, TestLastBodyPairWithReasoning, TestLastBodyPairWithLargeResponse_MultiPair`
- 直接依赖：`backend/pkg/cast`, `backend/pkg/templates`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/models/helpers/calc_context.go`, `backend/cmd/installer/wizard/models/helpers/calc_context_test.go`, `backend/cmd/installer/wizard/models/summarizer_form.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go`, `backend/pkg/providers/provider.go`, `backend/pkg/providers/providers.go`, `backend/pkg/templates/validator/testdata.go`
- 备注：测试文件，用于验证对应模块行为。；长文件（2131 行），属于复杂度热点，阅读时建议先看对外导出和测试。
