# `backend/pkg/controller` 文件清单

本组共 `26` 个文件。

## `backend/pkg/controller/alog.go`

- 文件类型：`.go`
- 大小：`1867` 字节
- 文本行数：`82`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`FlowAgentLogWorker, NewFlowAgentLogWorker, PutLog, GetLog`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/subscriptions`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/alogs.go`

- 文件类型：`.go`
- 大小：`1626` 字节
- 文本行数：`72`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`AgentLogController, NewAgentLogController, NewFlowAgentLog, ListFlowsAgentLog, GetFlowAgentLog`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/subscriptions`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/aslog.go`

- 文件类型：`.go`
- 大小：`12281` 字节
- 文本行数：`429`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`FlowAssistantLogWorker, NewFlowAssistantLogWorker, PutMsg, PutFlowAssistantMsg, PutFlowAssistantMsgResult, StreamFlowAssistantMsg, UpdateMsgResult`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/subscriptions`, `backend/pkg/providers`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/aslogs.go`

- 文件类型：`.go`
- 大小：`2191` 字节
- 文本行数：`85`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`AssistantLogController, NewAssistantLogController, NewFlowAssistantLog, ListFlowsAssistantLog, GetFlowAssistantLog`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/subscriptions`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/assistant.go`

- 文件类型：`.go`
- 大小：`20034` 字节
- 文本行数：`615`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`AssistantWorker, NewAssistantWorker, LoadAssistantWorker, GetAssistantID, GetUserID, GetFlowID, GetTitle, GetStatus, SetStatus, PutInput, Finish, Stop`
- 直接依赖：`backend/pkg/cast`, `backend/pkg/database`, `backend/pkg/graph/subscriptions`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/providers`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider`, `backend/pkg/templates`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/context.go`

- 文件类型：`.go`
- 大小：`1205` 字节
- 文本行数：`61`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`ErrNothingToLoad, FlowContext, TaskContext, SubtaskContext`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/subscriptions`, `backend/pkg/observability/langfuse`, `backend/pkg/providers`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/flow.go`

- 文件类型：`.go`
- 大小：`36802` 字节
- 文本行数：`1203`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`FlowWorker, NewFlowWorker, LoadFlowWorker, GetFlowID, GetUserID, GetTitle, GetContext, GetStatus, SetStatus, AddAssistant, GetAssistant, DeleteAssistant`
- 直接依赖：`backend/pkg/cast`, `backend/pkg/config`, `backend/pkg/database`, `backend/pkg/docker`, `backend/pkg/flowfiles`, `backend/pkg/graph/model`, `backend/pkg/graph/subscriptions`, `backend/pkg/observability`, `backend/pkg/observability/langfuse`, `backend/pkg/providers`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/provider` 等 14 项
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`
- 备注：长文件（1203 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/controller/flows.go`

- 文件类型：`.go`
- 大小：`9011` 字节
- 文本行数：`392`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`FlowController, NewFlowController, LoadFlows, CreateFlow, CreateAssistant, ListFlows, GetFlow, StopFlow, FinishFlow, RenameFlow`
- 直接依赖：`backend/pkg/config`, `backend/pkg/database`, `backend/pkg/docker`, `backend/pkg/graph/subscriptions`, `backend/pkg/providers`, `backend/pkg/providers/provider`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/msglog.go`

- 文件类型：`.go`
- 大小：`6024` 字节
- 文本行数：`244`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`FlowMsgLogWorker, NewFlowMsgLogWorker, PutMsg, PutFlowMsg, PutFlowMsgResult, PutTaskMsg, PutTaskMsgResult, PutSubtaskMsg, PutSubtaskMsgResult, UpdateMsgResult`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/subscriptions`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/msglogs.go`

- 文件类型：`.go`
- 大小：`1570` 字节
- 文本行数：`69`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`MsgLogController, NewMsgLogController, NewFlowMsgLog, ListFlowsMsgLog, GetFlowMsgLog`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/subscriptions`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/prompter.go`

- 文件类型：`.go`
- 大小：`1931` 字节
- 文本行数：`51`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`backend/pkg/database`, `backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/prompter_test.go`

- 文件类型：`.go`
- 大小：`6457` 字节
- 文本行数：`210`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`GetUserPrompts, TestBuildUserPrompter_NoUserPrompts, TestBuildUserPrompter_SingleOverride, TestBuildUserPrompter_PartialOverridesPreserveDefaults, TestBuildUserPrompter_EmptyBodyIsIgnored, TestNewUserPrompter_HappyPath, TestNewUserPrompter_DBErrorPropagates`
- 直接依赖：`backend/pkg/database`, `backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/controller/screenshot.go`

- 文件类型：`.go`
- 大小：`1782` 字节
- 文本行数：`63`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`FlowScreenshotWorker, NewFlowScreenshotWorker, PutScreenshot, GetScreenshot`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/subscriptions`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/screenshots.go`

- 文件类型：`.go`
- 大小：`1652` 字节
- 文本行数：`69`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`ScreenshotController, NewScreenshotController, NewFlowScreenshot, ListFlowsScreenshot, GetFlowScreenshot`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/subscriptions`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/slog.go`

- 文件类型：`.go`
- 大小：`2029` 字节
- 文本行数：`86`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`FlowSearchLogWorker, NewFlowSearchLogWorker, PutLog, GetLog`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/subscriptions`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/slogs.go`

- 文件类型：`.go`
- 大小：`1650` 字节
- 文本行数：`72`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`SearchLogController, NewSearchLogController, NewFlowSearchLog, ListFlowsSearchLog, GetFlowSearchLog`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/subscriptions`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/subtask.go`

- 文件类型：`.go`
- 大小：`10677` 字节
- 文本行数：`372`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`TaskUpdater, SubtaskWorker, NewSubtaskWorker, LoadSubtaskWorker, GetMsgChainID, GetSubtaskID, GetTaskID, GetFlowID, GetUserID, GetTitle, GetDescription, IsCompleted`
- 直接依赖：`backend/pkg/database`, `backend/pkg/observability`, `backend/pkg/providers`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/subtasks.go`

- 文件类型：`.go`
- 大小：`5257` 字节
- 文本行数：`194`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`NewSubtaskInfo, SubtaskController, NewSubtaskController, LoadSubtasks, GenerateSubtasks, RefineSubtasks, PopSubtask, ListSubtasks, GetSubtask`
- 直接依赖：`backend/pkg/database`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`
- 备注：包含 TODO，后续维护时可重点留意未完成事项。

## `backend/pkg/controller/task.go`

- 文件类型：`.go`
- 大小：`10341` 字节
- 文本行数：`400`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`FlowUpdater, TaskWorker, NewTaskWorker, LoadTaskWorker, GetTaskID, GetFlowID, GetUserID, GetTitle, IsCompleted, IsWaiting, GetStatus, SetStatus`
- 直接依赖：`backend/pkg/database`, `backend/pkg/observability`, `backend/pkg/providers`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/tasks.go`

- 文件类型：`.go`
- 大小：`2379` 字节
- 文本行数：`111`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`TaskController, NewTaskController, LoadTasks, CreateTask, ListTasks, GetTask`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/tclog.go`

- 文件类型：`.go`
- 大小：`2973` 字节
- 文本行数：`127`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`FlowToolCallLogWorker, NewFlowToolCallLogWorker, PutLog, UpdateLogSuccess, UpdateLogFailed, GetLog`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/subscriptions`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/tclogs.go`

- 文件类型：`.go`
- 大小：`1670` 字节
- 文本行数：`72`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`ToolCallLogController, NewToolCallLogController, NewFlowToolCallLog, ListFlowsToolCallLog, GetFlowToolCallLog`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/subscriptions`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/termlog.go`

- 文件类型：`.go`
- 大小：`2579` 字节
- 文本行数：`101`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`FlowTermLogWorker, NewFlowTermLogWorker, PutMsg, GetMsg, GetContainers`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/subscriptions`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/termlogs.go`

- 文件类型：`.go`
- 大小：`1966` 字节
- 文本行数：`82`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`TermLogController, NewTermLogController, NewFlowTermLog, ListFlowsTermLog, GetFlowTermLog, GetFlowContainers`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/subscriptions`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/vslog.go`

- 文件类型：`.go`
- 大小：`2223` 字节
- 文本行数：`94`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`FlowVectorStoreLogWorker, NewFlowVectorStoreLogWorker, PutLog, GetLog`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/subscriptions`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`

## `backend/pkg/controller/vslogs.go`

- 文件类型：`.go`
- 大小：`1779` 字节
- 文本行数：`72`
- 所属分组：`backend/pkg/controller`
- 所属包/模块：`controller`
- 推断作用：业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。
- 生成文件：`否`
- 关键导出/符号：`VectorStoreLogController, NewVectorStoreLogController, NewFlowVectorStoreLog, ListFlowsVectorStoreLog, GetFlowVectorStoreLog`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/subscriptions`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/graph/resolver.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/assistants.go`, `backend/pkg/server/services/flows.go`, `backend/pkg/server/services/graphql.go`
