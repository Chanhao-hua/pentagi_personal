# `backend/pkg/graphiti` 文件清单

本组共 `2` 个文件。

## `backend/pkg/graphiti/client.go`

- 文件类型：`.go`
- 大小：`5130` 字节
- 文本行数：`146`
- 所属分组：`backend/pkg/graphiti`
- 所属包/模块：`graphiti`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/graphiti` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`Client, NewClient, IsEnabled, GetTimeout, AddMessages, TemporalWindowSearch, EntityRelationshipsSearch, DiverseResultsSearch, EpisodeContextSearch, SuccessfulToolsSearch, RecentContextSearch, EntityByLabelSearch`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/executor.go`, `backend/pkg/providers/performer.go`, `backend/pkg/providers/provider.go`, `backend/pkg/providers/providers.go`, `backend/pkg/tools/graphiti_search.go`, `backend/pkg/tools/tools.go`

## `backend/pkg/graphiti/client_test.go`

- 文件类型：`.go`
- 大小：`4163` 字节
- 文本行数：`151`
- 所属分组：`backend/pkg/graphiti`
- 所属包/模块：`graphiti`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/graphiti` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`TestNewClient_Disabled, TestIsEnabled, TestGetTimeout, TestAddMessages_Disabled, TestSearchMethods_Disabled`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/executor.go`, `backend/pkg/providers/performer.go`, `backend/pkg/providers/provider.go`, `backend/pkg/providers/providers.go`, `backend/pkg/tools/graphiti_search.go`, `backend/pkg/tools/tools.go`
- 备注：测试文件，用于验证对应模块行为。
