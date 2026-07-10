# `backend/pkg/terminal` 文件清单

本组共 `2` 个文件。

## `backend/pkg/terminal/output.go`

- 文件类型：`.go`
- 大小：`6957` 字节
- 文本行数：`258`
- 所属分组：`backend/pkg/terminal`
- 所属包/模块：`terminal`
- 推断作用：终端会话与命令交互文件，用于在容器或运行时中维护交互式会话。
- 生成文件：`否`
- 关键导出/符号：`Info, Success, Error, Warning, PrintInfo, PrintSuccess, PrintError, PrintWarning, PrintMock, PrintHeader, PrintKeyValue, PrintValueFormat`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/etester/flush.go`, `backend/cmd/etester/info.go`, `backend/cmd/etester/main.go`, `backend/cmd/etester/reindex.go`, `backend/cmd/etester/search.go`, `backend/cmd/etester/test.go`, `backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/interactive.go`, `backend/cmd/ftester/worker/tester.go`

## `backend/pkg/terminal/output_test.go`

- 文件类型：`.go`
- 大小：`8195` 字节
- 文本行数：`317`
- 所属分组：`backend/pkg/terminal`
- 所属包/模块：`terminal`
- 推断作用：终端会话与命令交互文件，用于在容器或运行时中维护交互式会话。
- 生成文件：`否`
- 关键导出/符号：`TestIsMarkdownContent_Headers, TestIsMarkdownContent_CodeBlocks, TestIsMarkdownContent_Bold, TestIsMarkdownContent_Links, TestIsMarkdownContent_Lists, TestIsMarkdownContent_PlainText, TestIsMarkdownContent_EdgeCases, TestInteractivePromptContext_ReadsInput, TestInteractivePromptContext_TrimsWhitespace, TestInteractivePromptContext_CancelledContext, TestGetYesNoInputContext_Yes, TestGetYesNoInputContext_No`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/etester/flush.go`, `backend/cmd/etester/info.go`, `backend/cmd/etester/main.go`, `backend/cmd/etester/reindex.go`, `backend/cmd/etester/search.go`, `backend/cmd/etester/test.go`, `backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/mocks/tools.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/interactive.go`, `backend/cmd/ftester/worker/tester.go`
- 备注：测试文件，用于验证对应模块行为。
