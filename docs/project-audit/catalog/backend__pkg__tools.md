# `backend/pkg/tools` 文件清单

本组共 `47` 个文件。

## `backend/pkg/tools/args.go`

- 文件类型：`.go`
- 大小：`40670` 字节
- 文本行数：`403`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`FileOp, FileAction, BrowserAction, Browser, SubtaskInfo, SubtaskList, SubtaskOperationType, SubtaskOperation, SubtaskInfoPatch, SubtaskPatch, TaskResult, AskUser`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/args_test.go`

- 文件类型：`.go`
- 大小：`15499` 字节
- 文本行数：`595`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`TestBoolUnmarshalJSON, TestBoolMarshalJSON, TestBoolBool, TestBoolString, TestInt64UnmarshalJSON, TestInt64MarshalJSON, TestInt64Int, TestInt64Int64Method, TestInt64PtrInt64, TestInt64String, TestBoolJSONRoundTrip, TestInt64JSONRoundTrip`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/tools/browser.go`

- 文件类型：`.go`
- 大小：`13823` 字节
- 文本行数：`521`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`NewBrowserTool, Handle, ContentMD, ContentHTML, Links, IsAvailable`
- 直接依赖：`backend/pkg/observability`, `backend/pkg/observability/langfuse`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/browser_test.go`

- 文件类型：`.go`
- 大小：`17638` 字节
- 文本行数：`616`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`PutScreenshot, TestBrowserResolveUrl, TestBrowserIsAvailable, TestContentMD_ScreenshotFailure_ReturnsContent, TestContentHTML_ScreenshotFailure_ReturnsContent, TestLinks_ScreenshotFailure_ReturnsContent, TestContentMD_ScreenshotSmall_ReturnsContent, TestContentMD_BothSucceed_ReturnsContentAndScreenshot, TestGetHTML_SmallContent_ReturnsWarning, TestGetHTML_EmptyContent_ReturnsError, TestGetHTML_BinaryURL_ReturnsError, TestGetMD_SmallContent_ReturnsWarning`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/tools/code.go`

- 文件类型：`.go`
- 大小：`12961` 字节
- 文本行数：`418`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`NewCodeTool, Handle, IsAvailable`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/model`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/providers/embeddings`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/context.go`

- 文件类型：`.go`
- 大小：`846` 字节
- 文本行数：`35`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`AgentContextKey, GetAgentContext, PutAgentContext`
- 直接依赖：`backend/pkg/database`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/context_test.go`

- 文件类型：`.go`
- 大小：`4110` 字节
- 文本行数：`147`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`TestGetAgentContextEmpty, TestPutAgentContextFirst, TestPutAgentContextChaining, TestPutAgentContextTripleChaining, TestPutAgentContextIsolation, TestPutAgentContextDoesNotMutatePreviousDerivedContext, TestGetAgentContextIgnoresOtherContextValues`
- 直接依赖：`backend/pkg/database`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/tools/duckduckgo.go`

- 文件类型：`.go`
- 大小：`15883` 字节
- 文本行数：`565`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`NewDuckDuckGoTool, Handle, IsAvailable`
- 直接依赖：`backend/pkg/config`, `backend/pkg/database`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/system`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/duckduckgo_test.go`

- 文件类型：`.go`
- 大小：`19193` 字节
- 文本行数：`667`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`TestDuckDuckGoHandle, TestDuckDuckGoIsAvailable, TestDuckDuckGoHandle_ValidationAndSwallowedError, TestDuckDuckGoHandle_StatusCodeErrors, TestDuckDuckGoParseHTMLStructured, TestDuckDuckGoParseHTMLRegex, TestDuckDuckGoParseHTMLRegex_BlockBoundaries, TestDuckDuckGoCleanText, TestDuckDuckGoFormatResults, TestDuckDuckGoMaxResultsClamp, TestDuckDuckGoSafeSearchMapping, TestDuckDuckGoRegionDefault`
- 直接依赖：`backend/pkg/config`, `backend/pkg/database`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/tools/executor.go`

- 文件类型：`.go`
- 大小：`17754` 字节
- 文本行数：`621`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`DefaultResultSizeLimit, Tools, Execute, IsBarrierFunction, IsFunctionExists, GetBarrierToolNames, GetBarrierTools, GetToolSchema`
- 直接依赖：`backend/pkg/database`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/schema`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/executor_test.go`

- 文件类型：`.go`
- 大小：`8753` 字节
- 文本行数：`350`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`TestGetMessage, TestArgsToMarkdown, TestIsBarrierFunction, TestGetBarrierToolNames, TestToolsReturnsDefinitions, TestExecuteEarlyReturns, TestGetToolSchemaFallbackAndUnknown, TestGetBarrierToolsSkipsUnknownBarriers, TestGetSummarizePromptTruncatesLongArgValues, TestConverToJSONSchemaErrorPath`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/tools/flow_manager.go`

- 文件类型：`.go`
- 大小：`31853` 字节
- 文本行数：`937`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`NewFlowStatusTool, Handle, NewWaitFlowCompletionTool, Handle, NewStopFlowTool, Handle, NewSubmitFlowInputTool, Handle, NewPatchFlowSubtasksTool, Handle`
- 直接依赖：`backend/pkg/database`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
- 备注：长文件（937 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/tools/flow_manager_test.go`

- 文件类型：`.go`
- 大小：`45435` 字节
- 文本行数：`1383`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`GetFlowTasks, GetFlowSubtasks, GetFlowTaskSubtasks, GetTaskPlannedSubtasks, GetSubtaskMsgLogs, TestInferFlowStatus, TestTruncateText, TestFlowStatusToolHandle, TestBuildSummary, TestBuildTasksList, TestBuildSubtasksList, TestBuildRunningInfo`
- 直接依赖：`backend/pkg/database`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
- 备注：测试文件，用于验证对应模块行为。；长文件（1383 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/tools/google.go`

- 文件类型：`.go`
- 大小：`4444` 字节
- 文本行数：`180`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`NewGoogleTool, Handle, IsAvailable`
- 直接依赖：`backend/pkg/config`, `backend/pkg/database`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/system`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/google_test.go`

- 文件类型：`.go`
- 大小：`9344` 字节
- 文本行数：`333`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`TestGoogleIsAvailable, TestGoogleFormatResults, TestGoogleNewSearchService, TestGoogleHandle_ValidationAndSwallowedError, TestGoogleHandle_WithAgentContext, TestGoogleMaxResultsClamp, TestGoogleConfigHelpers, TestGoogleConfigHelpers_NilConfig`
- 直接依赖：`backend/pkg/config`, `backend/pkg/database`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/tools/graphiti_search.go`

- 文件类型：`.go`
- 大小：`25603` 字节
- 文本行数：`792`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`GraphitiSearcher, NewGraphitiSearchTool, IsAvailable, Handle, FormatGraphitiTemporalResults, FormatGraphitiEntityRelationshipResults, FormatGraphitiDiverseResults, FormatGraphitiEpisodeContextResults, FormatGraphitiSuccessfulToolsResults, FormatGraphitiRecentContextResults, FormatGraphitiEntityByLabelResults`
- 直接依赖：`backend/pkg/graphiti`, `backend/pkg/observability`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/guide.go`

- 文件类型：`.go`
- 大小：`12533` 字节
- 文本行数：`402`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`NewGuideTool, Handle, IsAvailable`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/model`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/providers/embeddings`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/memory.go`

- 文件类型：`.go`
- 大小：`8203` 字节
- 文本行数：`260`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`NewMemoryTool, Handle, IsAvailable`
- 直接依赖：`backend/pkg/database`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/memory_utils.go`

- 文件类型：`.go`
- 大小：`1779` 字节
- 文本行数：`65`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`MergeAndDeduplicateDocs`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/memory_utils_test.go`

- 文件类型：`.go`
- 大小：`9760` 字节
- 文本行数：`298`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`TestMergeAndDeduplicateDocs_EmptyInput, TestMergeAndDeduplicateDocs_NoDuplicates, TestMergeAndDeduplicateDocs_WithDuplicates, TestMergeAndDeduplicateDocs_SortingByScore, TestMergeAndDeduplicateDocs_LimitEnforcement, TestMergeAndDeduplicateDocs_MetadataPreservation, TestHashContent_Consistency, TestMergeAndDeduplicateDocs_ZeroMaxDocs, TestMergeAndDeduplicateDocs_ComplexScenario`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/tools/perplexity.go`

- 文件类型：`.go`
- 大小：`12806` 字节
- 文本行数：`427`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`Message, CompletionRequest, CompletionResponse, Choice, Usage, NewPerplexityTool, Handle, IsAvailable`
- 直接依赖：`backend/pkg/config`, `backend/pkg/database`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/system`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/perplexity_test.go`

- 文件类型：`.go`
- 大小：`14977` 字节
- 文本行数：`508`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`TestPerplexityHandle, TestPerplexityIsAvailable, TestPerplexityHandleErrorResponse, TestPerplexityFormatResponse, TestPerplexityGetSummarizePrompt, TestPerplexityHandle_ValidationAndSwallowedError, TestPerplexityHandle_StatusCodeErrors, TestPerplexityDefaultValues, TestPerplexityCustomModel`
- 直接依赖：`backend/pkg/config`, `backend/pkg/database`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/tools/proxy_test.go`

- 文件类型：`.go`
- 大小：`36787` 字节
- 文本行数：`1349`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`PutLog, URL, MockURL, CACertPEM, CACertPath, Close, TestNewTestProxy_InvalidInput, TestTestProxy_BasicHTTPInterception, TestTestProxy_HTTPSInterception, TestTestProxy_HTTPSWithCACertFile, TestTestProxy_RequestHeaders, TestTestProxy_RequestBody`
- 直接依赖：`backend/pkg/database`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
- 备注：测试文件，用于验证对应模块行为。；长文件（1349 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/tools/registry.go`

- 文件类型：`.go`
- 大小：`24000` 字节
- 文本行数：`492`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`ToolType, String, GetToolType, GetRegistryDefinitions, GetToolTypeMapping, GetToolsByType`
- 直接依赖：`backend/pkg/database`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/registry_test.go`

- 文件类型：`.go`
- 大小：`9337` 字节
- 文本行数：`290`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`TestToolTypeString, TestGetToolType, TestRegistryDefinitionsCompleteness, TestRegistryDefinitionsReturnsCopy, TestToolTypeMappingReturnsCopy, TestGetToolsByType, TestRegistryDefinitionNames, TestGetMessageType, TestGetMessageResultFormat, TestAllowedToolListsContainKnownUniqueTools`
- 直接依赖：`backend/pkg/database`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/tools/search.go`

- 文件类型：`.go`
- 大小：`12365` 字节
- 文本行数：`395`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`NewSearchTool, Handle, IsAvailable`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/model`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/providers/embeddings`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/searxng.go`

- 文件类型：`.go`
- 大小：`7420` 字节
- 文本行数：`289`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`NewSearxngTool, IsAvailable, Handle, SearxngResult, SearxngResponse, SearxngInfo`
- 直接依赖：`backend/pkg/config`, `backend/pkg/database`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/system`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/searxng_test.go`

- 文件类型：`.go`
- 大小：`12044` 字节
- 文本行数：`415`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`TestSearxngHandle, TestSearxngIsAvailable, TestSearxngParseHTTPResponse_StatusAndDecodeErrors, TestSearxngFormatResults_NoResults, TestSearxngFormatResults_WithResults, TestSearxngHandle_ValidationAndSwallowedError, TestSearxngHandle_DefaultLimit, TestSearxngHandle_TimeRange`
- 直接依赖：`backend/pkg/config`, `backend/pkg/database`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/tools/sploitus.go`

- 文件类型：`.go`
- 大小：`12491` 字节
- 文本行数：`388`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`NewSploitusTool, Handle, IsAvailable`
- 直接依赖：`backend/pkg/config`, `backend/pkg/database`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/system`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/sploitus_test.go`

- 文件类型：`.go`
- 大小：`16195` 字节
- 文本行数：`576`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`TestSploitusHandle, TestSploitusIsAvailable, TestSploitusHandle_ValidationAndSwallowedError, TestSploitusHandle_StatusCodeErrors, TestSploitusFormatResults, TestSploitusDefaultValues, TestSploitusSizeLimits, TestSploitusMaxResultsClamp`
- 直接依赖：`backend/pkg/config`, `backend/pkg/database`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/tools/tavily.go`

- 文件类型：`.go`
- 大小：`10318` 字节
- 文本行数：`323`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`NewTavilyTool, Handle, IsAvailable`
- 直接依赖：`backend/pkg/config`, `backend/pkg/database`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/system`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/tavily_test.go`

- 文件类型：`.go`
- 大小：`12198` 字节
- 文本行数：`437`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`TestTavilyHandle, TestTavilyIsAvailable, TestTavilyParseHTTPResponse_StatusAndDecodeErrors, TestTavilyBuildResult_WithSummarizer, TestTavilyHandle_ValidationAndSwallowedError`
- 直接依赖：`backend/pkg/config`, `backend/pkg/database`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/tools/terminal.go`

- 文件类型：`.go`
- 大小：`14450` 字节
- 文本行数：`462`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`PrimaryTerminalNamePrefix, NewTerminalTool, Handle, ExecCommand, ReadFile, WriteFile, PrimaryTerminalName, IsAvailable`
- 直接依赖：`backend/pkg/database`, `backend/pkg/docker`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/terminal_test.go`

- 文件类型：`.go`
- 大小：`17723` 字节
- 文本行数：`532`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`PutMsg, RunContainer, StopContainer, RemoveContainer, IsContainerRunning, ContainerExecCreate, ContainerExecAttach, ContainerStatPath, ListContainerDir, ContainerExecInspect, CopyToContainer, CopyFromContainer`
- 直接依赖：`backend/pkg/database`, `backend/pkg/docker`, `backend/pkg/flowfiles`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/tools/testdata/ddg_result_docker_security.html`

- 文件类型：`.html`
- 大小：`30671` 字节
- 文本行数：`638`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`未识别`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/tools/testdata/ddg_result_golang_http_client.html`

- 文件类型：`.html`
- 大小：`29144` 字节
- 文本行数：`636`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`未识别`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/tools/testdata/ddg_result_owasp_vulnerabilities.html`

- 文件类型：`.html`
- 大小：`32269` 字节
- 文本行数：`648`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`未识别`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/tools/testdata/ddg_result_site_github_golang.html`

- 文件类型：`.html`
- 大小：`28499` 字节
- 文本行数：`626`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`未识别`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/tools/testdata/ddg_result_sql_injection.html`

- 文件类型：`.html`
- 大小：`31255` 字节
- 文本行数：`640`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`未识别`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/tools/testdata/sploitus_result_cve_2026.json`

- 文件类型：`.json`
- 大小：`75223` 字节
- 文本行数：`105`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`未识别`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/tools/testdata/sploitus_result_metasploit.json`

- 文件类型：`.json`
- 大小：`3537` 字节
- 文本行数：`75`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`未识别`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/tools/testdata/sploitus_result_nginx.json`

- 文件类型：`.json`
- 大小：`126914` 字节
- 文本行数：`105`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`未识别`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/tools/testdata/sploitus_result_nmap.json`

- 文件类型：`.json`
- 大小：`3351` 字节
- 文本行数：`75`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`未识别`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/tools/tools.go`

- 文件类型：`.go`
- 大小：`54663` 字节
- 文本行数：`1945`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`ExecutorHandler, SummarizeHandler, Functions, Scan, DisableFunction, ExternalFunction, FunctionInfo, Tool, ScreenshotProvider, AgentLogProvider, MsgLogProvider, SearchLogProvider`
- 直接依赖：`backend/pkg/config`, `backend/pkg/database`, `backend/pkg/docker`, `backend/pkg/flowfiles`, `backend/pkg/graph/model`, `backend/pkg/graphiti`, `backend/pkg/providers/embeddings`, `backend/pkg/schema`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
- 备注：长文件（1945 行），属于复杂度热点，阅读时建议先看对外导出和测试。；包含 TODO，后续维护时可重点留意未完成事项。

## `backend/pkg/tools/traversaal.go`

- 文件类型：`.go`
- 大小：`4464` 字节
- 文本行数：`175`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`NewTraversaalTool, Handle, IsAvailable`
- 直接依赖：`backend/pkg/config`, `backend/pkg/database`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/system`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项

## `backend/pkg/tools/traversaal_test.go`

- 文件类型：`.go`
- 大小：`7271` 字节
- 文本行数：`246`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`TestTraversaalHandle, TestTraversaalIsAvailable, TestTraversaalParseHTTPResponse_StatusAndDecodeErrors, TestTraversaalHandle_ValidationAndSwallowedError`
- 直接依赖：`backend/pkg/config`, `backend/pkg/database`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/tools/vecstore_helper.go`

- 文件类型：`.go`
- 大小：`2437` 字节
- 文本行数：`79`
- 所属分组：`backend/pkg/tools`
- 所属包/模块：`tools`
- 推断作用：安全测试工具适配文件，封装外部工具的调用与结果转换。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`backend/pkg/database`, `backend/pkg/providers/embeddings`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/args.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/processor/docker.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/task.go`, `backend/pkg/csum/chain_summary.go` 等 28 项
