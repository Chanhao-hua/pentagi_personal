# `backend/pkg/database` 文件清单

本组共 `35` 个文件。

## `backend/pkg/database/agentlogs.sql.go`

- 文件类型：`.go`
- 大小：`6328` 字节
- 文本行数：`269`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateAgentLogParams, CreateAgentLog, GetFlowAgentLogParams, GetFlowAgentLog, GetFlowAgentLogs, GetSubtaskAgentLogs, GetTaskAgentLogs, GetUserFlowAgentLogsParams, GetUserFlowAgentLogs`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/analytics.sql.go`

- 文件类型：`.go`
- 大小：`9145` 字节
- 文本行数：`333`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`GetAssistantsCountForFlow, GetFlowsForPeriodLast3MonthsRow, GetFlowsForPeriodLast3Months, GetFlowsForPeriodLastMonthRow, GetFlowsForPeriodLastMonth, GetFlowsForPeriodLastWeekRow, GetFlowsForPeriodLastWeek, GetMsgchainsForFlowRow, GetMsgchainsForFlow, GetSubtasksForTasksRow, GetSubtasksForTasks, GetTasksForFlowRow`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/api_token_with_secret.go`

- 文件类型：`.go`
- 大小：`98` 字节
- 文本行数：`7`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`否`
- 关键导出/符号：`APITokenWithSecret`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项

## `backend/pkg/database/api_tokens.sql.go`

- 文件类型：`.go`
- 大小：`9634` 字节
- 文本行数：`410`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateAPITokenParams, CreateAPIToken, DeleteAPIToken, DeleteUserAPITokenParams, DeleteUserAPIToken, DeleteUserAPITokenByTokenIDParams, DeleteUserAPITokenByTokenID, GetAPIToken, GetAPITokenByTokenID, GetAPITokens, GetUserAPITokenParams, GetUserAPIToken`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/assistantlogs.sql.go`

- 文件类型：`.go`
- 大小：`9096` 字节
- 文本行数：`348`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateAssistantLogParams, CreateAssistantLog, CreateResultAssistantLogParams, CreateResultAssistantLog, DeleteFlowAssistantLog, GetFlowAssistantLog, GetFlowAssistantLogsParams, GetFlowAssistantLogs, GetUserFlowAssistantLogsParams, GetUserFlowAssistantLogs, UpdateAssistantLogParams, UpdateAssistantLog`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/assistants.sql.go`

- 文件类型：`.go`
- 大小：`16521` 字节
- 文本行数：`592`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateAssistantParams, CreateAssistant, DeleteAssistant, GetAssistant, GetAssistantUseAgents, GetFlowAssistantParams, GetFlowAssistant, GetFlowAssistants, GetUserFlowAssistantParams, GetUserFlowAssistant, GetUserFlowAssistantsParams, GetUserFlowAssistants`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/containers.sql.go`

- 文件类型：`.go`
- 大小：`9724` 字节
- 文本行数：`407`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateContainerParams, CreateContainer, GetContainers, GetFlowContainers, GetFlowPrimaryContainer, GetRunningContainers, GetUserContainers, GetUserFlowContainersParams, GetUserFlowContainers, UpdateContainerImageParams, UpdateContainerImage, UpdateContainerStatusParams`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/converter/analytics.go`

- 文件类型：`.go`
- 大小：`13826` 字节
- 文本行数：`408`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`converter`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`否`
- 关键导出/符号：`CalculateSubtaskDuration, SubtaskDurationInfo, CalculateSubtasksWithOverlapCompensation, CalculateTaskDuration, CalculateFlowDuration, CountFinishedToolcalls, CountFinishedToolcallsForSubtask, CountFinishedToolcallsForTask, BuildFlowExecutionStats`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/model`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/schema.resolvers.go`, `backend/pkg/graph/subscriptions/publisher.go`

## `backend/pkg/database/converter/analytics_test.go`

- 文件类型：`.go`
- 大小：`28926` 字节
- 文本行数：`843`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`converter`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`否`
- 关键导出/符号：`TestCalculateSubtaskDuration_CreatedStatus, TestCalculateSubtaskDuration_WaitingStatus, TestCalculateSubtaskDuration_FinishedStatus, TestCalculateSubtaskDuration_WithMsgchainValidation, TestCalculateSubtasksWithOverlapCompensation_NoOverlap, TestCalculateSubtasksWithOverlapCompensation_WithOverlap, TestCalculateSubtasksWithOverlapCompensation_IgnoresCreated, TestCalculateTaskDuration_OnlySubtasks, TestCalculateTaskDuration_WithGenerator, TestCalculateTaskDuration_WithRefiner, TestCountFinishedToolcalls, TestCountFinishedToolcallsForSubtask`
- 直接依赖：`backend/pkg/database`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/schema.resolvers.go`, `backend/pkg/graph/subscriptions/publisher.go`
- 备注：测试文件，用于验证对应模块行为。；长文件（843 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/database/converter/converter.go`

- 文件类型：`.go`
- 大小：`41131` 字节
- 文本行数：`1252`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`converter`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`否`
- 关键导出/符号：`ConvertFlows, ConvertFlow, ConvertContainers, ConvertContainer, ConvertTasks, ConvertSubtasks, ConvertTask, ConvertSubtask, ConvertFlowAssistant, ConvertAssistants, ConvertAssistant, ConvertScreenshots`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/model`, `backend/pkg/providers/pconfig`, `backend/pkg/providers/tester`, `backend/pkg/providers/tester/testdata`, `backend/pkg/templates`, `backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/schema.resolvers.go`, `backend/pkg/graph/subscriptions/publisher.go`
- 备注：长文件（1252 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/database/converter/converter_test.go`

- 文件类型：`.go`
- 大小：`1922` 字节
- 文本行数：`59`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`converter`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`否`
- 关键导出/符号：`TestIsAgentTool`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/schema.resolvers.go`, `backend/pkg/graph/subscriptions/publisher.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/database/database.go`

- 文件类型：`.go`
- 大小：`3250` 字节
- 文本行数：`139`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`否`
- 关键导出/符号：`NullStringToPtrString, PtrStringToNullString, StringToNullString, Int64ToNullInt64, Uint64ToNullInt64, NullInt64ToInt64, TimeToNullTime, PtrTimeToNullTime, SanitizeUTF8, GormLogger, Print, NewGorm`
- 直接依赖：`backend/pkg/observability`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：包含 TODO，后续维护时可重点留意未完成事项。

## `backend/pkg/database/db.go`

- 文件类型：`.go`
- 大小：`632` 字节
- 文本行数：`32`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`DBTX, New, Queries, WithTx`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/flow_templates.sql.go`

- 文件类型：`.go`
- 大小：`3492` 字节
- 文本行数：`154`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateFlowTemplateParams, CreateFlowTemplate, DeleteFlowTemplateParams, DeleteFlowTemplate, GetFlowTemplateParams, GetFlowTemplate, GetFlowTemplatesByUserID, UpdateFlowTemplateParams, UpdateFlowTemplate`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/flows.sql.go`

- 文件类型：`.go`
- 大小：`20429` 字节
- 文本行数：`703`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateFlowParams, CreateFlow, DeleteFlow, GetFlow, GetFlowStatsRow, GetFlowStats, GetFlows, GetFlowsStatsByDayLast3MonthsRow, GetFlowsStatsByDayLast3Months, GetFlowsStatsByDayLastMonthRow, GetFlowsStatsByDayLastMonth, GetFlowsStatsByDayLastWeekRow`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/knowledge.sql.go`

- 文件类型：`.go`
- 大小：`15728` 字节
- 文本行数：`456`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`DeleteFlowMemoryDocuments, DeleteKnowledgeDocument, DeleteUserKnowledgeDocumentParams, DeleteUserKnowledgeDocument, GetKnowledgeDocumentRow, GetKnowledgeDocument, GetUserKnowledgeDocumentParams, GetUserKnowledgeDocumentRow, GetUserKnowledgeDocument, InsertKnowledgeDocumentParams, InsertKnowledgeDocument, ListAllKnowledgeDocumentsRow`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/knowledge/knowledge.go`

- 文件类型：`.go`
- 大小：`24545` 字节
- 文本行数：`727`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`knowledge`
- 推断作用：知识库数据访问层文件，连接数据库记录、向量索引和订阅更新。
- 生成文件：`否`
- 关键导出/符号：`PublisherFactory, KnowledgeStore, NewKnowledgeStore, ListDocuments, ListUserDocuments, GetDocument, GetUserDocument, SearchDocuments, SearchUserDocuments, CreateDocument, UpdateDocument, UpdateUserDocument`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/model`, `backend/pkg/graph/subscriptions`, `backend/pkg/providers/embeddings`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/resolver.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/graphql.go`, `backend/pkg/server/services/knowledge.go`

## `backend/pkg/database/knowledge/knowledge_test.go`

- 文件类型：`.go`
- 大小：`79114` 字节
- 文本行数：`2261`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`knowledge`
- 推断作用：知识库数据访问层文件，连接数据库记录、向量索引和订阅更新。
- 生成文件：`否`
- 关键导出/符号：`InsertKnowledgeDocument, GetKnowledgeDocument, GetUserKnowledgeDocument, ListAllKnowledgeDocuments, ListFlowKnowledgeDocuments, ListUserKnowledgeDocuments, UpdateKnowledgeDocument, DeleteKnowledgeDocument, DeleteUserKnowledgeDocument, SearchKnowledgeDocuments, SearchUserKnowledgeDocuments, SimilaritySearch`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/model`, `backend/pkg/graph/subscriptions`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/graph/resolver.go`, `backend/pkg/server/router.go`, `backend/pkg/server/services/graphql.go`, `backend/pkg/server/services/knowledge.go`
- 备注：测试文件，用于验证对应模块行为。；长文件（2261 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/database/models.go`

- 文件类型：`.go`
- 大小：`35349` 字节
- 文本行数：`1158`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`AssistantStatus, Scan, NullAssistantStatus, Scan, Value, ContainerStatus, Scan, NullContainerStatus, Scan, Value, ContainerType, Scan`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（1158 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/database/msgchains.sql.go`

- 文件类型：`.go`
- 大小：`44397` 字节
- 文本行数：`1415`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateMsgChainParams, CreateMsgChain, GetAllFlowsUsageStatsRow, GetAllFlowsUsageStats, GetFlowMsgChains, GetFlowTaskTypeLastMsgChainParams, GetFlowTaskTypeLastMsgChain, GetFlowTypeMsgChainsParams, GetFlowTypeMsgChains, GetFlowUsageStatsRow, GetFlowUsageStats, GetMsgChain`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（1415 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/database/msglogs.sql.go`

- 文件类型：`.go`
- 大小：`7760` 字节
- 文本行数：`328`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateMsgLogParams, CreateMsgLog, CreateResultMsgLogParams, CreateResultMsgLog, GetFlowMsgLogs, GetSubtaskMsgLogs, GetTaskMsgLogs, GetUserFlowMsgLogsParams, GetUserFlowMsgLogs, UpdateMsgLogResultParams, UpdateMsgLogResult`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/prompts.sql.go`

- 文件类型：`.go`
- 大小：`6322` 字节
- 文本行数：`278`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateUserPromptParams, CreateUserPrompt, DeletePrompt, DeleteUserPromptParams, DeleteUserPrompt, GetPrompts, GetUserPromptParams, GetUserPrompt, GetUserPromptByTypeParams, GetUserPromptByType, GetUserPrompts, UpdatePromptParams`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/providers.sql.go`

- 文件类型：`.go`
- 大小：`9578` 字节
- 文本行数：`415`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateProviderParams, CreateProvider, DeleteProvider, DeleteUserProviderParams, DeleteUserProvider, GetProvider, GetProviders, GetProvidersByType, GetUserProviderParams, GetUserProvider, GetUserProviderByNameParams, GetUserProviderByName`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/querier.go`

- 文件类型：`.go`
- 大小：`25597` 字节
- 文本行数：`320`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`Querier`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/resources.sql.go`

- 文件类型：`.go`
- 大小：`9901` 字节
- 文本行数：`428`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`GetAllResourcesAll, GetAllResourcesInDirParams, GetAllResourcesInDir, GetAllResourcesRecursiveParams, GetAllResourcesRecursive, GetAllResourcesRoot, GetUserResourceByID, GetUserResourcesAll, GetUserResourcesByIDs, GetUserResourcesInDirParams, GetUserResourcesInDir, GetUserResourcesRecursiveParams`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/roles.sql.go`

- 文件类型：`.go`
- 大小：`2265` 字节
- 文本行数：`107`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`GetRoleRow, GetRole, GetRoleByNameRow, GetRoleByName, GetRolesRow, GetRoles`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/screenshots.sql.go`

- 文件类型：`.go`
- 大小：`5579` 字节
- 文本行数：`245`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateScreenshotParams, CreateScreenshot, GetFlowScreenshots, GetScreenshot, GetSubtaskScreenshots, GetTaskScreenshots, GetUserFlowScreenshotsParams, GetUserFlowScreenshots`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/searchlogs.sql.go`

- 文件类型：`.go`
- 大小：`6643` 字节
- 文本行数：`278`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateSearchLogParams, CreateSearchLog, GetFlowSearchLogParams, GetFlowSearchLog, GetFlowSearchLogs, GetSubtaskSearchLogs, GetTaskSearchLogs, GetUserFlowSearchLogsParams, GetUserFlowSearchLogs`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/subtasks.sql.go`

- 文件类型：`.go`
- 大小：`14401` 字节
- 文本行数：`593`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateSubtaskParams, CreateSubtask, DeleteSubtask, DeleteSubtasks, GetFlowSubtaskParams, GetFlowSubtask, GetFlowSubtasks, GetFlowTaskSubtasksParams, GetFlowTaskSubtasks, GetSubtask, GetTaskCompletedSubtasks, GetTaskPlannedSubtasks`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/tasks.sql.go`

- 文件类型：`.go`
- 大小：`7553` 字节
- 文本行数：`334`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateTaskParams, CreateTask, GetFlowTaskParams, GetFlowTask, GetFlowTasks, GetTask, GetUserFlowTaskParams, GetUserFlowTask, GetUserFlowTasksParams, GetUserFlowTasks, UpdateTaskFailedResultParams, UpdateTaskFailedResult`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/termlogs.sql.go`

- 文件类型：`.go`
- 大小：`6703` 字节
- 文本行数：`293`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateTermLogParams, CreateTermLog, GetContainerTermLogs, GetFlowTermLogs, GetSubtaskTermLogs, GetTaskTermLogs, GetTermLog, GetUserFlowTermLogsParams, GetUserFlowTermLogs`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/toolcalls.sql.go`

- 文件类型：`.go`
- 大小：`23182` 字节
- 文本行数：`707`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateToolcallParams, CreateToolcall, GetAllFlowsToolcallsStatsRow, GetAllFlowsToolcallsStats, GetCallToolcall, GetFlowToolcallParams, GetFlowToolcall, GetFlowToolcalls, GetFlowToolcallsStatsRow, GetFlowToolcallsStats, GetSubtaskToolcalls, GetSubtaskToolcallsStatsRow`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/user_preferences.sql.go`

- 文件类型：`.go`
- 大小：`5119` 字节
- 文本行数：`196`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`AddFavoriteFlowParams, AddFavoriteFlow, CreateUserPreferencesParams, CreateUserPreferences, DeleteFavoriteFlowParams, DeleteFavoriteFlow, DeleteUserPreferences, GetUserPreferencesByUserID, UpdateUserPreferencesParams, UpdateUserPreferences, UpsertUserPreferencesParams, UpsertUserPreferences`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/users.sql.go`

- 文件类型：`.go`
- 大小：`10517` 字节
- 文本行数：`401`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateUserParams, CreateUser, DeleteUser, GetUserRow, GetUser, GetUserByHashRow, GetUserByHash, GetUsersRow, GetUsers, UpdateUserNameParams, UpdateUserName, UpdateUserPasswordParams`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/database/vecstorelogs.sql.go`

- 文件类型：`.go`
- 大小：`7101` 字节
- 文本行数：`288`
- 所属分组：`backend/pkg/database`
- 所属包/模块：`database`
- 推断作用：数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。
- 生成文件：`是`
- 关键导出/符号：`CreateVectorStoreLogParams, CreateVectorStoreLog, GetFlowVectorStoreLogParams, GetFlowVectorStoreLog, GetFlowVectorStoreLogs, GetSubtaskVectorStoreLogs, GetTaskVectorStoreLogs, GetUserFlowVectorStoreLogsParams, GetUserFlowVectorStoreLogs`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/mocks/logs.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go` 等 87 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。
