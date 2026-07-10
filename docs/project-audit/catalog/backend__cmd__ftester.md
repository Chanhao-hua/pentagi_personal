# `backend/cmd/ftester` 文件清单

本组共 `7` 个文件。

## `backend/cmd/ftester/main.go`

- 文件类型：`.go`
- 大小：`4345` 字节
- 文本行数：`163`
- 所属分组：`backend/cmd/ftester`
- 所属包/模块：`main`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`backend/cmd/ftester/worker`, `backend/pkg/config`, `backend/pkg/database`, `backend/pkg/docker`, `backend/pkg/observability`, `backend/pkg/providers`, `backend/pkg/providers/provider`, `backend/pkg/terminal`, `backend/pkg/version`
- 被这些文件直接引用：`当前未发现`

## `backend/cmd/ftester/mocks/logs.go`

- 文件类型：`.go`
- 大小：`10958` 字节
- 文本行数：`353`
- 所属分组：`backend/cmd/ftester`
- 所属包/模块：`mocks`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`ProxyProviders, NewProxyProviders, GetScreenshotProvider, GetAgentLogProvider, GetMsgLogProvider, GetSearchLogProvider, GetTermLogProvider, GetVectorStoreLogProvider, GetToolCallLogProvider, GetKnowledgeProvider, PutScreenshot, PutLog`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/model`, `backend/pkg/terminal`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`

## `backend/cmd/ftester/mocks/tools.go`

- 文件类型：`.go`
- 大小：`39011` 字节
- 文本行数：`646`
- 所属分组：`backend/cmd/ftester`
- 所属包/模块：`mocks`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`MockResponse`
- 直接依赖：`backend/pkg/terminal`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`

## `backend/cmd/ftester/worker/args.go`

- 文件类型：`.go`
- 大小：`10291` 字节
- 文本行数：`352`
- 所属分组：`backend/cmd/ftester`
- 所属包/模块：`worker`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`FunctionInfo, ArgumentInfo, DescribeParams, GetAvailableFunctions, GetFunctionInfo, ParseFunctionArgs`
- 直接依赖：`backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`

## `backend/cmd/ftester/worker/executor.go`

- 文件类型：`.go`
- 大小：`13179` 字节
- 文本行数：`471`
- 所属分组：`backend/cmd/ftester`
- 所属包/模块：`worker`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`Handle, IsAvailable, GetTool, ExecuteFunctionWrapper, ExecuteRealFunction, ExecuteFunctionWithMode, GetSummarizer`
- 直接依赖：`backend/cmd/ftester/mocks`, `backend/pkg/config`, `backend/pkg/database`, `backend/pkg/docker`, `backend/pkg/graphiti`, `backend/pkg/providers`, `backend/pkg/providers/embeddings`, `backend/pkg/terminal`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`
- 备注：包含 TODO，后续维护时可重点留意未完成事项。

## `backend/cmd/ftester/worker/interactive.go`

- 文件类型：`.go`
- 大小：`4892` 字节
- 文本行数：`185`
- 所属分组：`backend/cmd/ftester`
- 所属包/模块：`worker`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`InteractiveFillArgs`
- 直接依赖：`backend/pkg/terminal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`

## `backend/cmd/ftester/worker/tester.go`

- 文件类型：`.go`
- 大小：`22395` 字节
- 文本行数：`686`
- 所属分组：`backend/cmd/ftester`
- 所属包/模块：`worker`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`Tester, NewTester, Execute`
- 直接依赖：`backend/cmd/ftester/mocks`, `backend/pkg/config`, `backend/pkg/database`, `backend/pkg/docker`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/providers`, `backend/pkg/providers/provider`, `backend/pkg/templates`, `backend/pkg/terminal`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`
- 备注：包含 TODO，后续维护时可重点留意未完成事项。
