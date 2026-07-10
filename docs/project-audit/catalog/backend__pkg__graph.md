# `backend/pkg/graph` 文件清单

本组共 `11` 个文件。

## `backend/pkg/graph/context.go`

- 文件类型：`.go`
- 大小：`4635` 字节
- 文本行数：`184`
- 所属分组：`backend/pkg/graph`
- 所属包/模块：`graph`
- 推断作用：GraphQL 相关文件，包含 schema、resolver、订阅和生成代码边界。
- 生成文件：`否`
- 关键导出/符号：`GqlContextKey, GetUserID, SetUserID, GetUserType, SetUserType, GetUserPermissions, SetUserPermissions`
- 直接依赖：`backend/pkg/database`, `backend/pkg/flowfiles`, `backend/pkg/graph/model`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/services/graphql.go`

## `backend/pkg/graph/context_test.go`

- 文件类型：`.go`
- 大小：`9622` 字节
- 文本行数：`389`
- 所属分组：`backend/pkg/graph`
- 所属包/模块：`graph`
- 推断作用：GraphQL 相关文件，包含 schema、resolver、订阅和生成代码边界。
- 生成文件：`否`
- 关键导出/符号：`TestGetUserID_Found, TestGetUserID_Missing, TestGetUserID_WrongType, TestSetUserID_Roundtrip, TestGetUserType_Found, TestGetUserType_Missing, TestGetUserType_WrongType, TestSetUserType_Roundtrip, TestGetUserPermissions_Found, TestGetUserPermissions_Missing, TestGetUserPermissions_WrongType, TestSetUserPermissions_Roundtrip`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/services/graphql.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/graph/generate.go`

- 文件类型：`.go`
- 大小：`289` 字节
- 文本行数：`12`
- 所属分组：`backend/pkg/graph`
- 所属包/模块：`graph`
- 推断作用：GraphQL 相关文件，包含 schema、resolver、订阅和生成代码边界。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/services/graphql.go`

## `backend/pkg/graph/generated.go`

- 文件类型：`.go`
- 大小：`1466160` 字节
- 文本行数：`45737`
- 所属分组：`backend/pkg/graph`
- 所属包/模块：`graph`
- 推断作用：GraphQL 相关文件，包含 schema、resolver、订阅和生成代码边界。
- 生成文件：`是`
- 关键导出/符号：`NewExecutableSchema, Config, ResolverRoot, DirectiveRoot, ComplexityRoot, MutationResolver, QueryResolver, SubscriptionResolver, Schema, Complexity, Exec`
- 直接依赖：`backend/pkg/graph/model`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/services/graphql.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（45737 行），属于复杂度热点，阅读时建议先看对外导出和测试。；包含 TODO，后续维护时可重点留意未完成事项。

## `backend/pkg/graph/model/models_gen.go`

- 文件类型：`.go`
- 大小：`49404` 字节
- 文本行数：`1610`
- 所属分组：`backend/pkg/graph`
- 所属包/模块：`model`
- 推断作用：GraphQL 相关文件，包含 schema、resolver、订阅和生成代码边界。
- 生成文件：`是`
- 关键导出/符号：`APIToken, APITokenWithSecret, AgentConfig, AgentLog, AgentPrompt, AgentPrompts, AgentTestResult, AgentTypeUsageStats, AgentsConfig, AgentsPrompts, Assistant, AssistantLog`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/mocks/logs.go`, `backend/pkg/controller/flow.go`, `backend/pkg/database/converter/analytics.go`, `backend/pkg/database/converter/converter.go`, `backend/pkg/database/knowledge/knowledge.go`, `backend/pkg/database/knowledge/knowledge_test.go`, `backend/pkg/graph/context.go`, `backend/pkg/graph/generated.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/graph/subscriptions/controller.go`, `backend/pkg/graph/subscriptions/publisher.go`, `backend/pkg/graph/subscriptions/subscriber.go` 等 22 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（1610 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/graph/resolver.go`

- 文件类型：`.go`
- 大小：`910` 字节
- 文本行数：`33`
- 所属分组：`backend/pkg/graph`
- 所属包/模块：`graph`
- 推断作用：GraphQL 相关文件，包含 schema、resolver、订阅和生成代码边界。
- 生成文件：`否`
- 关键导出/符号：`Resolver`
- 直接依赖：`backend/pkg/config`, `backend/pkg/controller`, `backend/pkg/database`, `backend/pkg/database/knowledge`, `backend/pkg/graph/subscriptions`, `backend/pkg/providers`, `backend/pkg/server/auth`, `backend/pkg/templates`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/services/graphql.go`

## `backend/pkg/graph/schema.graphqls`

- 文件类型：`.graphqls`
- 大小：`24731` 字节
- 文本行数：`1115`
- 所属分组：`backend/pkg/graph`
- 所属包/模块：`未识别`
- 推断作用：GraphQL 相关文件，包含 schema、resolver、订阅和生成代码边界。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`
- 备注：长文件（1115 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/graph/schema.resolvers.go`

- 文件类型：`.go`
- 大小：`89147` 字节
- 文本行数：`2977`
- 所属分组：`backend/pkg/graph`
- 所属包/模块：`graph`
- 推断作用：GraphQL 相关文件，包含 schema、resolver、订阅和生成代码边界。
- 生成文件：`是`
- 关键导出/符号：`CreateFlow, PutUserInput, StopFlow, FinishFlow, DeleteFlow, RenameFlow, CreateAssistant, CallAssistant, StopAssistant, DeleteAssistant, TestAgent, TestProvider`
- 直接依赖：`backend/pkg/controller`, `backend/pkg/database`, `backend/pkg/database/converter`, `backend/pkg/flowfiles`, `backend/pkg/graph/model`, `backend/pkg/providers/anthropic`, `backend/pkg/providers/bedrock`, `backend/pkg/providers/deepseek`, `backend/pkg/providers/gemini`, `backend/pkg/providers/glm`, `backend/pkg/providers/kimi`, `backend/pkg/providers/openai` 等 20 项
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/server/services/graphql.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（2977 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/graph/subscriptions/controller.go`

- 文件类型：`.go`
- 大小：`17940` 字节
- 文本行数：`465`
- 所属分组：`backend/pkg/graph`
- 所属包/模块：`subscriptions`
- 推断作用：GraphQL 相关文件，包含 schema、resolver、订阅和生成代码边界。
- 生成文件：`否`
- 关键导出/符号：`SubscriptionsController, UserContext, FlowContext, FlowSubscriber, ProviderSubscriber, APITokenSubscriber, SettingsSubscriber, FlowTemplateSubscriber, ResourceSubscriber, FlowPublisher, KnowledgeSubscriber, KnowledgePublisher`
- 直接依赖：`backend/pkg/database`, `backend/pkg/graph/model`, `backend/pkg/providers/pconfig`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/msglog.go`, `backend/pkg/controller/msglogs.go`, `backend/pkg/controller/screenshot.go` 等 33 项

## `backend/pkg/graph/subscriptions/publisher.go`

- 文件类型：`.go`
- 大小：`10348` 字节
- 文本行数：`286`
- 所属分组：`backend/pkg/graph`
- 所属包/模块：`subscriptions`
- 推断作用：GraphQL 相关文件，包含 schema、resolver、订阅和生成代码边界。
- 生成文件：`否`
- 关键导出/符号：`GetFlowID, SetFlowID, GetUserID, SetUserID, FlowCreated, FlowDeleted, FlowUpdated, TaskCreated, TaskUpdated, AssistantCreated, AssistantUpdated, AssistantDeleted`
- 直接依赖：`backend/pkg/database`, `backend/pkg/database/converter`, `backend/pkg/graph/model`, `backend/pkg/providers/pconfig`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/msglog.go`, `backend/pkg/controller/msglogs.go`, `backend/pkg/controller/screenshot.go` 等 33 项

## `backend/pkg/graph/subscriptions/subscriber.go`

- 文件类型：`.go`
- 大小：`10399` 字节
- 文本行数：`302`
- 所属分组：`backend/pkg/graph`
- 所属包/模块：`subscriptions`
- 推断作用：GraphQL 相关文件，包含 schema、resolver、订阅和生成代码边界。
- 生成文件：`否`
- 关键导出/符号：`GetFlowID, SetFlowID, GetUserID, SetUserID, FlowCreatedAdmin, FlowCreated, FlowDeletedAdmin, FlowDeleted, FlowUpdatedAdmin, FlowUpdated, TaskCreated, TaskUpdated`
- 直接依赖：`backend/pkg/graph/model`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`, `backend/pkg/controller/alog.go`, `backend/pkg/controller/alogs.go`, `backend/pkg/controller/aslog.go`, `backend/pkg/controller/aslogs.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/controller/msglog.go`, `backend/pkg/controller/msglogs.go`, `backend/pkg/controller/screenshot.go` 等 33 项
