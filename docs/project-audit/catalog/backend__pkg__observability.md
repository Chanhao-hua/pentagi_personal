# `backend/pkg/observability` 文件清单

本组共 `136` 个文件。

## `backend/pkg/observability/collector.go`

- 文件类型：`.go`
- 大小：`6128` 字节
- 文本行数：`183`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`observability`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/subtask.go`, `backend/pkg/controller/task.go`, `backend/pkg/database/database.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go` 等 34 项

## `backend/pkg/observability/langfuse/agent.go`

- 文件类型：`.go`
- 大小：`6274` 字节
- 文本行数：`242`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`Agent, AgentOption, WithAgentID, WithAgentName, WithAgentMetadata, WithAgentInput, WithAgentOutput, WithAgentStartTime, WithAgentEndTime, WithAgentLevel, WithAgentStatus, WithAgentVersion`
- 直接依赖：`backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/api/.fern/metadata.json`

- 文件类型：`.json`
- 大小：`289` 字节
- 文本行数：`11`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`未识别`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/pkg/observability/langfuse/api/README.md`

- 文件类型：`.md`
- 大小：`6562` 字节
- 文本行数：`202`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`未识别`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`
- 备注：包含 TODO，后续维护时可重点留意未完成事项。

## `backend/pkg/observability/langfuse/api/annotationqueues.go`

- 文件类型：`.go`
- 大小：`47627` 字节
- 文本行数：`1458`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`CreateAnnotationQueueRequest, SetName, SetDescription, SetScoreConfigIDs, UnmarshalJSON, MarshalJSON, AnnotationQueuesCreateQueueAssignmentRequest, SetQueueID, UnmarshalJSON, MarshalJSON, CreateAnnotationQueueItemRequest, SetQueueID`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（1458 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/observability/langfuse/api/annotationqueues/client.go`

- 文件类型：`.go`
- 大小：`5280` 字节
- 文本行数：`206`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`annotationqueues`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Listqueues, Createqueue, Getqueue, Listqueueitems, Createqueueitem, Getqueueitem, Deletequeueitem, Updatequeueitem, Createqueueassignment, Deletequeueassignment`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`

- 文件类型：`.go`
- 大小：`15336` 字节
- 文本行数：`495`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`annotationqueues`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Listqueues, Createqueue, Getqueue, Listqueueitems, Createqueueitem, Getqueueitem, Deletequeueitem, Updatequeueitem, Createqueueassignment, Deletequeueassignment`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/blobstorageintegrations.go`

- 文件类型：`.go`
- 大小：`31904` 字节
- 文本行数：`842`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`BlobStorageIntegrationsDeleteBlobStorageIntegrationRequest, SetID, BlobStorageExportFrequency, NewBlobStorageExportFrequencyFromString, Ptr, BlobStorageExportMode, NewBlobStorageExportModeFromString, Ptr, BlobStorageIntegrationDeletionResponse, GetMessage, GetExtraProperties, SetMessage`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（842 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`

- 文件类型：`.go`
- 大小：`2498` 字节
- 文本行数：`85`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`blobstorageintegrations`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Getblobstorageintegrations, Upsertblobstorageintegration, Deleteblobstorageintegration`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/option`, `backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`

- 文件类型：`.go`
- 大小：`4992` 字节
- 文本行数：`161`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`blobstorageintegrations`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Getblobstorageintegrations, Upsertblobstorageintegration, Deleteblobstorageintegration`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/option`, `backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/client/client.go`

- 文件类型：`.go`
- 大小：`4791` 字节
- 文本行数：`111`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`client`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient`
- 直接依赖：`backend/pkg/observability/langfuse/api/annotationqueues`, `backend/pkg/observability/langfuse/api/blobstorageintegrations`, `backend/pkg/observability/langfuse/api/comments`, `backend/pkg/observability/langfuse/api/datasetitems`, `backend/pkg/observability/langfuse/api/datasetrunitems`, `backend/pkg/observability/langfuse/api/datasets`, `backend/pkg/observability/langfuse/api/health`, `backend/pkg/observability/langfuse/api/ingestion`, `backend/pkg/observability/langfuse/api/llmconnections`, `backend/pkg/observability/langfuse/api/media`, `backend/pkg/observability/langfuse/api/metricsv2`, `backend/pkg/observability/langfuse/api/metrics` 等 29 项
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/client/client_test.go`

- 文件类型：`.go`
- 大小：`1003` 字节
- 文本行数：`46`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`client`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`TestNewClient`
- 直接依赖：`backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；测试文件，用于验证对应模块行为。

## `backend/pkg/observability/langfuse/api/comments.go`

- 文件类型：`.go`
- 大小：`18642` 字节
- 文本行数：`595`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`CreateCommentRequest, SetProjectID, SetObjectType, SetObjectID, SetContent, SetAuthorUserID, UnmarshalJSON, MarshalJSON, CommentsGetRequest, SetPage, SetLimit, SetObjectType`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/comments/client.go`

- 文件类型：`.go`
- 大小：`2095` 字节
- 文本行数：`87`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`comments`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Get, Create, GetByID`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/comments/raw_client.go`

- 文件类型：`.go`
- 大小：`4893` 字节
- 文本行数：`169`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`comments`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Get, Create, GetByID`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/core/api_error.go`

- 文件类型：`.go`
- 大小：`1055` 字节
- 文本行数：`48`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`core`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`APIError, NewAPIError, Unwrap, Error`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 61 项

## `backend/pkg/observability/langfuse/api/core/http.go`

- 文件类型：`.go`
- 大小：`325` 字节
- 文本行数：`16`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`core`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`HTTPClient`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 61 项

## `backend/pkg/observability/langfuse/api/core/request_option.go`

- 文件类型：`.go`
- 大小：`3399` 字节
- 文本行数：`125`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`core`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RequestOption, RequestOptions, NewRequestOptions, ToHeader, BaseURLOption, HTTPClientOption, HTTPHeaderOption, BodyPropertiesOption, QueryParametersOption, MaxAttemptsOption, BasicAuthOption`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 61 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/datasetitems.go`

- 文件类型：`.go`
- 大小：`22541` 字节
- 文本行数：`683`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`CreateDatasetItemRequest, SetDatasetName, SetInput, SetExpectedOutput, SetMetadata, SetSourceTraceID, SetSourceObservationID, SetID, SetStatus, UnmarshalJSON, MarshalJSON, DatasetItemsDeleteRequest`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/datasetitems/client.go`

- 文件类型：`.go`
- 大小：`2460` 字节
- 文本行数：`104`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`datasetitems`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, List, Create, Get, Delete`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`

- 文件类型：`.go`
- 大小：`6241` 字节
- 文本行数：`213`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`datasetitems`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, List, Create, Get, Delete`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/datasetrunitems.go`

- 文件类型：`.go`
- 大小：`8981` 字节
- 文本行数：`253`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`CreateDatasetRunItemRequest, SetRunName, SetRunDescription, SetMetadata, SetDatasetItemID, SetObservationID, SetTraceID, UnmarshalJSON, MarshalJSON, DatasetRunItemsListRequest, SetDatasetID, SetRunName`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`

- 文件类型：`.go`
- 大小：`1666` 字节
- 文本行数：`70`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`datasetrunitems`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, List, Create`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`

- 文件类型：`.go`
- 大小：`3643` 字节
- 文本行数：`125`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`datasetrunitems`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, List, Create`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/datasets.go`

- 文件类型：`.go`
- 大小：`37229` 字节
- 文本行数：`1191`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`CreateDatasetRequest, SetName, SetDescription, SetMetadata, SetInputSchema, SetExpectedOutputSchema, UnmarshalJSON, MarshalJSON, DatasetsDeleteRunRequest, SetDatasetName, SetRunName, DatasetsGetRequest`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（1191 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/observability/langfuse/api/datasets/client.go`

- 文件类型：`.go`
- 大小：`3205` 字节
- 文本行数：`138`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`datasets`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, List, Create, Get, Getrun, Deleterun, Getruns`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/datasets/raw_client.go`

- 文件类型：`.go`
- 大小：`9112` 字节
- 文本行数：`310`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`datasets`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, List, Create, Get, Getrun, Deleterun, Getruns`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/error_codes.go`

- 文件类型：`.go`
- 大小：`1070` 字节
- 文本行数：`44`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`无或未解析`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/errors.go`

- 文件类型：`.go`
- 大小：`2881` 字节
- 文本行数：`147`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`BadRequestError, UnmarshalJSON, MarshalJSON, Unwrap, ForbiddenError, UnmarshalJSON, MarshalJSON, Unwrap, MethodNotAllowedError, UnmarshalJSON, MarshalJSON, Unwrap`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/file_param.go`

- 文件类型：`.go`
- 大小：`1172` 字节
- 文本行数：`42`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`FileParam, FileParamOption, NewFileParam, Name, ContentType`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项

## `backend/pkg/observability/langfuse/api/health.go`

- 文件类型：`.go`
- 大小：`2696` 字节
- 文本行数：`106`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`HealthResponse, GetVersion, GetStatus, GetExtraProperties, SetVersion, SetStatus, UnmarshalJSON, MarshalJSON, String`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/health/client.go`

- 文件类型：`.go`
- 大小：`1206` 字节
- 文本行数：`51`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`health`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Health`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/option`, `backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/health/raw_client.go`

- 文件类型：`.go`
- 大小：`2016` 字节
- 文本行数：`74`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`health`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Health`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/option`, `backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/ingestion.go`

- 文件类型：`.go`
- 大小：`308783` 字节
- 文本行数：`9706`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`IngestionBatchRequest, SetBatch, SetMetadata, UnmarshalJSON, MarshalJSON, BaseEvent, GetID, GetTimestamp, GetMetadata, GetExtraProperties, SetID, SetTimestamp`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（9706 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/observability/langfuse/api/ingestion/client.go`

- 文件类型：`.go`
- 大小：`2447` 字节
- 文本行数：`67`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`ingestion`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Batch`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/ingestion/raw_client.go`

- 文件类型：`.go`
- 大小：`2156` 字节
- 文本行数：`77`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`ingestion`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Batch`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/internal/caller.go`

- 文件类型：`.go`
- 大小：`9160` 字节
- 文本行数：`323`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`internal`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`Caller, CallerParams, NewCaller, CallParams, CallResponse, Call`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/comments.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go` 等 81 项

## `backend/pkg/observability/langfuse/api/internal/caller_test.go`

- 文件类型：`.go`
- 大小：`20242` 字节
- 文本行数：`707`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`internal`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`InternalTestCase, InternalTestRequest, InternalTestResponse, InternalTestNotFoundError, TestCall, TestMergeHeaders, TestIsNil, FormURLEncodedTestRequest, TestNewFormURLEncodedBody, TestNewFormURLEncodedRequestBody, TestNewRequestBodyFormURLEncoded`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/comments.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go` 等 81 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/observability/langfuse/api/internal/error_decoder.go`

- 文件类型：`.go`
- 大小：`1925` 字节
- 文本行数：`65`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`internal`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`ErrorCodes, ErrorDecoder, NewErrorDecoder`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/comments.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go` 等 81 项

## `backend/pkg/observability/langfuse/api/internal/error_decoder_test.go`

- 文件类型：`.go`
- 大小：`1755` 字节
- 文本行数：`60`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`internal`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`TestErrorDecoder`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/comments.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go` 等 81 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/observability/langfuse/api/internal/explicit_fields.go`

- 文件类型：`.go`
- 大小：`3282` 字节
- 文本行数：`117`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`internal`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`HandleExplicitFields`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/comments.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go` 等 81 项

## `backend/pkg/observability/langfuse/api/internal/explicit_fields_test.go`

- 文件类型：`.go`
- 大小：`13690` 字节
- 文本行数：`498`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`internal`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`SetName, SetCode, SetCount, SetEnabled, SetTags, MarshalJSON, TestHandleExplicitFields, TestHandleExplicitFieldsCustomMarshaler, TestHandleExplicitFieldsPointerHandling, TestHandleExplicitFieldsEmbeddedStruct, TestHandleExplicitFieldsTagHandling, SetNestedName`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/comments.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go` 等 81 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/observability/langfuse/api/internal/extra_properties.go`

- 文件类型：`.go`
- 大小：`4230` 字节
- 文本行数：`142`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`internal`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`MarshalJSONWithExtraProperty, MarshalJSONWithExtraProperties, ExtractExtraProperties`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/comments.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go` 等 81 项

## `backend/pkg/observability/langfuse/api/internal/extra_properties_test.go`

- 文件类型：`.go`
- 大小：`7433` 字节
- 文本行数：`229`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`internal`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`MarshalJSON, TestMarshalJSONWithExtraProperties, TestExtractExtraProperties`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/comments.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go` 等 81 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/observability/langfuse/api/internal/http.go`

- 文件类型：`.go`
- 大小：`1823` 字节
- 文本行数：`72`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`internal`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`HTTPClient, ResolveBaseURL, EncodeURL, MergeHeaders`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/comments.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go` 等 81 项

## `backend/pkg/observability/langfuse/api/internal/query.go`

- 文件类型：`.go`
- 大小：`9082` 字节
- 文本行数：`354`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`internal`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`QueryEncoder, QueryValues, QueryValuesWithDefaults, Contains`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/comments.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go` 等 81 项

## `backend/pkg/observability/langfuse/api/internal/query_test.go`

- 文件类型：`.go`
- 大小：`10691` 字节
- 文本行数：`396`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`internal`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`TestQueryValues, TestQueryValuesWithDefaults`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/comments.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go` 等 81 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/observability/langfuse/api/internal/retrier.go`

- 文件类型：`.go`
- 大小：`6581` 字节
- 文本行数：`240`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`internal`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`RetryOption, RetryFunc, WithMaxAttempts, Retrier, NewRetrier, Run`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/comments.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go` 等 81 项

## `backend/pkg/observability/langfuse/api/internal/retrier_test.go`

- 文件类型：`.go`
- 大小：`10146` 字节
- 文本行数：`353`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`internal`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`RetryTestCase, TestRetrier, TestRetryWithRequestBody, TestRetryDelayTiming`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/comments.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go` 等 81 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/observability/langfuse/api/internal/stringer.go`

- 文件类型：`.go`
- 大小：`312` 字节
- 文本行数：`14`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`internal`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`StringifyJSON`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/comments.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go` 等 81 项

## `backend/pkg/observability/langfuse/api/internal/time.go`

- 文件类型：`.go`
- 大小：`2978` 字节
- 文本行数：`138`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`internal`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`Date, NewDate, NewOptionalDate, Time, TimePtr, MarshalJSON, UnmarshalJSON, DateTime, NewDateTime, NewOptionalDateTime, Time, TimePtr`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/comments.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go` 等 81 项

## `backend/pkg/observability/langfuse/api/llmconnections.go`

- 文件类型：`.go`
- 大小：`18941` 字节
- 文本行数：`552`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`LlmConnectionsListRequest, SetPage, SetLimit, LlmAdapter, NewLlmAdapterFromString, Ptr, LlmConnection, GetID, GetProvider, GetAdapter, GetDisplaySecretKey, GetBaseURL`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/llmconnections/client.go`

- 文件类型：`.go`
- 大小：`1725` 字节
- 文本行数：`70`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`llmconnections`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, List, Upsert`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/llmconnections/raw_client.go`

- 文件类型：`.go`
- 大小：`3629` 字节
- 文本行数：`125`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`llmconnections`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, List, Upsert`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/media.go`

- 文件类型：`.go`
- 大小：`27271` 字节
- 文本行数：`664`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`MediaGetRequest, SetMediaID, GetMediaUploadURLRequest, SetTraceID, SetObservationID, SetContentType, SetContentLength, SetSha256Hash, SetField, UnmarshalJSON, MarshalJSON, PatchMediaBody`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/media/client.go`

- 文件类型：`.go`
- 大小：`1992` 字节
- 文本行数：`87`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`media`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Get, Patch, Getuploadurl`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/media/raw_client.go`

- 文件类型：`.go`
- 大小：`4746` 字节
- 文本行数：`165`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`media`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Get, Patch, Getuploadurl`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/metrics.go`

- 文件类型：`.go`
- 大小：`5216` 字节
- 文本行数：`160`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`MetricsMetricsRequest, SetQuery, MetricsResponse, GetData, GetExtraProperties, SetData, UnmarshalJSON, MarshalJSON, String`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/metrics/client.go`

- 文件类型：`.go`
- 大小：`1546` 字节
- 文本行数：`57`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`metrics`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Metrics`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/metrics/raw_client.go`

- 文件类型：`.go`
- 大小：`2260` 字节
- 文本行数：`82`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`metrics`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Metrics`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/metricsv2.go`

- 文件类型：`.go`
- 大小：`6142` 字节
- 文本行数：`168`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`MetricsV2MetricsRequest, SetQuery, MetricsV2Response, GetData, GetExtraProperties, SetData, UnmarshalJSON, MarshalJSON, String`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/metricsv2/client.go`

- 文件类型：`.go`
- 大小：`5920` 字节
- 文本行数：`153`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`metricsv2`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Metrics`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/metricsv2/raw_client.go`

- 文件类型：`.go`
- 大小：`2273` 字节
- 文本行数：`82`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`metricsv2`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Metrics`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/models.go`

- 文件类型：`.go`
- 大小：`47496` 字节
- 文本行数：`1364`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`CreateModelRequest, SetModelName, SetMatchPattern, SetStartDate, SetUnit, SetInputPrice, SetOutputPrice, SetTotalPrice, SetPricingTiers, SetTokenizerID, SetTokenizerConfig, UnmarshalJSON`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（1364 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/observability/langfuse/api/models/client.go`

- 文件类型：`.go`
- 大小：`2412` 字节
- 文本行数：`104`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`models`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, List, Create, Get, Delete`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/models/raw_client.go`

- 文件类型：`.go`
- 大小：`5987` 字节
- 文本行数：`211`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`models`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, List, Create, Get, Delete`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/observations.go`

- 文件类型：`.go`
- 大小：`14609` 字节
- 文本行数：`369`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`ObservationsGetRequest, SetObservationID, ObservationsGetManyRequest, SetPage, SetLimit, SetName, SetUserID, SetType, SetTraceID, SetLevel, SetParentObservationID, SetEnvironment`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/observations/client.go`

- 文件类型：`.go`
- 大小：`1820` 字节
- 文本行数：`72`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`observations`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Get, Getmany`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/observations/raw_client.go`

- 文件类型：`.go`
- 大小：`3597` 字节
- 文本行数：`126`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`observations`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Get, Getmany`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/observationsv2.go`

- 文件类型：`.go`
- 大小：`18732` 字节
- 文本行数：`467`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`ObservationsV2GetManyRequest, SetFields, SetExpandMetadata, SetLimit, SetCursor, SetParseIoAsJSON, SetName, SetUserID, SetType, SetTraceID, SetLevel, SetParentObservationID`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/observationsv2/client.go`

- 文件类型：`.go`
- 大小：`2626` 字节
- 文本行数：`76`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`observationsv2`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Getmany`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/observationsv2/raw_client.go`

- 文件类型：`.go`
- 大小：`2303` 字节
- 文本行数：`82`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`observationsv2`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Getmany`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/opentelemetry.go`

- 文件类型：`.go`
- 大小：`27545` 字节
- 文本行数：`950`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`OpentelemetryExportTracesRequest, SetResourceSpans, UnmarshalJSON, MarshalJSON, OtelAttribute, GetKey, GetValue, GetExtraProperties, SetKey, SetValue, UnmarshalJSON, MarshalJSON`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（950 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/observability/langfuse/api/opentelemetry/client.go`

- 文件类型：`.go`
- 大小：`2050` 字节
- 文本行数：`68`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`opentelemetry`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Exporttraces`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/opentelemetry/raw_client.go`

- 文件类型：`.go`
- 大小：`2183` 字节
- 文本行数：`77`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`opentelemetry`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Exporttraces`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/option/request_option.go`

- 文件类型：`.go`
- 大小：`2203` 字节
- 文本行数：`73`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`option`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RequestOption, WithBaseURL, WithHTTPClient, WithHTTPHeader, WithBodyProperties, WithQueryParameters, WithMaxAttempts, WithBasicAuth`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/client/client.go`, `backend/pkg/observability/langfuse/api/client/client_test.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go` 等 55 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/organizations.go`

- 文件类型：`.go`
- 大小：`32753` 字节
- 文本行数：`1113`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`OrganizationsDeleteProjectMembershipRequest, SetProjectID, UnmarshalJSON, MarshalJSON, OrganizationsGetProjectMembershipsRequest, SetProjectID, DeleteMembershipRequest, GetUserID, GetExtraProperties, SetUserID, UnmarshalJSON, MarshalJSON`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（1113 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/observability/langfuse/api/organizations/client.go`

- 文件类型：`.go`
- 大小：`4904` 字节
- 文本行数：`166`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`organizations`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Getorganizationmemberships, Updateorganizationmembership, Deleteorganizationmembership, Getprojectmemberships, Updateprojectmembership, Deleteprojectmembership, Getorganizationprojects, Getorganizationapikeys`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/option`, `backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/organizations/raw_client.go`

- 文件类型：`.go`
- 大小：`11564` 字节
- 文本行数：`374`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`organizations`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Getorganizationmemberships, Updateorganizationmembership, Deleteorganizationmembership, Getprojectmemberships, Updateprojectmembership, Deleteprojectmembership, Getorganizationprojects, Getorganizationapikeys`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/option`, `backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/pointer.go`

- 文件类型：`.go`
- 大小：`2877` 字节
- 文本行数：`138`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`Bool, Byte, Bytes, Complex64, Complex128, Float32, Float64, Int, Int8, Int16, Int32, Int64`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项

## `backend/pkg/observability/langfuse/api/projects.go`

- 文件类型：`.go`
- 大小：`37392` 字节
- 文本行数：`1245`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`ProjectsCreateRequest, SetName, SetMetadata, SetRetention, UnmarshalJSON, MarshalJSON, ProjectsCreateAPIKeyRequest, SetProjectID, SetNote, SetPublicKey, SetSecretKey, UnmarshalJSON`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（1245 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/observability/langfuse/api/projects/client.go`

- 文件类型：`.go`
- 大小：`3986` 字节
- 文本行数：`153`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`projects`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Get, Create, Update, Delete, Getapikeys, Createapikey, Deleteapikey`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/option`, `backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/projects/raw_client.go`

- 文件类型：`.go`
- 大小：`10098` 字节
- 文本行数：`342`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`projects`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Get, Create, Update, Delete, Getapikeys, Createapikey, Deleteapikey`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/option`, `backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/prompts.go`

- 文件类型：`.go`
- 大小：`40347` 字节
- 文本行数：`1263`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`PromptsDeleteRequest, SetPromptName, SetLabel, SetVersion, PromptsGetRequest, SetPromptName, SetVersion, SetLabel, PromptsListRequest, SetName, SetLabel, SetTag`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（1263 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/observability/langfuse/api/prompts/client.go`

- 文件类型：`.go`
- 大小：`2462` 字节
- 文本行数：`104`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`prompts`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Get, Delete, List, Create`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/prompts/raw_client.go`

- 文件类型：`.go`
- 大小：`6392` 字节
- 文本行数：`224`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`prompts`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Get, Delete, List, Create`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/promptversion.go`

- 文件类型：`.go`
- 大小：`2668` 字节
- 文本行数：`78`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`PromptVersionUpdateRequest, SetName, SetVersion, SetNewLabels, UnmarshalJSON, MarshalJSON`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/promptversion/client.go`

- 文件类型：`.go`
- 大小：`1280` 字节
- 文本行数：`53`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`promptversion`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Update`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/promptversion/raw_client.go`

- 文件类型：`.go`
- 大小：`2236` 字节
- 文本行数：`81`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`promptversion`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Update`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/reference.md`

- 文件类型：`.md`
- 大小：`116115` 字节
- 文本行数：`7502`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`未识别`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`
- 备注：长文件（7502 行），属于复杂度热点，阅读时建议先看对外导出和测试。；包含 TODO，后续维护时可重点留意未完成事项。

## `backend/pkg/observability/langfuse/api/scim.go`

- 文件类型：`.go`
- 大小：`65165` 字节
- 文本行数：`2238`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`SCIMCreateUserRequest, SetUserName, SetName, SetEmails, SetActive, SetPassword, UnmarshalJSON, MarshalJSON, SCIMDeleteUserRequest, SetUserID, SCIMGetUserRequest, SetUserID`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（2238 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/observability/langfuse/api/scim/client.go`

- 文件类型：`.go`
- 大小：`3889` 字节
- 文本行数：`149`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`scim`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Getserviceproviderconfig, Getresourcetypes, Getschemas, Listusers, Createuser, Getuser, Deleteuser`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/option`, `backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/scim/raw_client.go`

- 文件类型：`.go`
- 大小：`9872` 字节
- 文本行数：`333`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`scim`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Getserviceproviderconfig, Getresourcetypes, Getschemas, Listusers, Createuser, Getuser, Deleteuser`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/option`, `backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/score.go`

- 文件类型：`.go`
- 大小：`10221` 字节
- 文本行数：`275`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`CreateScoreRequest, SetID, SetTraceID, SetSessionID, SetObservationID, SetDatasetRunID, SetName, SetValue, SetComment, SetMetadata, SetEnvironment, SetQueueID`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/score/client.go`

- 文件类型：`.go`
- 大小：`1651` 字节
- 文本行数：`70`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`score`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Create, Delete`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/score/raw_client.go`

- 文件类型：`.go`
- 大小：`3344` 字节
- 文本行数：`119`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`score`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Create, Delete`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/scoreconfigs.go`

- 文件类型：`.go`
- 大小：`24878` 字节
- 文本行数：`745`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`CreateScoreConfigRequest, SetName, SetDataType, SetCategories, SetMinValue, SetMaxValue, SetDescription, UnmarshalJSON, MarshalJSON, ScoreConfigsGetRequest, SetPage, SetLimit`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/scoreconfigs/client.go`

- 文件类型：`.go`
- 大小：`2471` 字节
- 文本行数：`104`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`scoreconfigs`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Get, Create, GetByID, Update`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/scoreconfigs/raw_client.go`

- 文件类型：`.go`
- 大小：`6272` 字节
- 文本行数：`215`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`scoreconfigs`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Get, Create, GetByID, Update`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/scorev2.go`

- 文件类型：`.go`
- 大小：`253401` 字节
- 文本行数：`7374`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`ScoreV2GetRequest, SetPage, SetLimit, SetUserID, SetName, SetFromTimestamp, SetToTimestamp, SetEnvironment, SetSource, SetOperator, SetValue, SetScoreIDs`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（7374 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/observability/langfuse/api/scorev2/client.go`

- 文件类型：`.go`
- 大小：`1693` 字节
- 文本行数：`70`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`scorev2`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Get, GetByID`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/scorev2/raw_client.go`

- 文件类型：`.go`
- 大小：`3537` 字节
- 文本行数：`126`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`scorev2`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Get, GetByID`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/sessions.go`

- 文件类型：`.go`
- 大小：`14599` 字节
- 文本行数：`484`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`SessionsGetRequest, SetSessionID, SessionsListRequest, SetPage, SetLimit, SetFromTimestamp, SetToTimestamp, SetEnvironment, PaginatedSessions, GetData, GetMeta, GetExtraProperties`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/sessions/client.go`

- 文件类型：`.go`
- 大小：`1767` 字节
- 文本行数：`70`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`sessions`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, List, Get`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/sessions/raw_client.go`

- 文件类型：`.go`
- 大小：`3570` 字节
- 文本行数：`126`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`sessions`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, List, Get`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/trace.go`

- 文件类型：`.go`
- 大小：`124969` 字节
- 文本行数：`3810`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`TraceDeleteRequest, SetTraceID, TraceDeleteMultipleRequest, SetTraceIDs, UnmarshalJSON, MarshalJSON, TraceGetRequest, SetTraceID, TraceListRequest, SetPage, SetLimit, SetUserID`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（3810 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/observability/langfuse/api/trace/client.go`

- 文件类型：`.go`
- 大小：`2400` 字节
- 文本行数：`104`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`trace`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`Client, NewClient, Get, Delete, List, Deletemultiple`
- 直接依赖：`backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/trace/raw_client.go`

- 文件类型：`.go`
- 大小：`6195` 字节
- 文本行数：`213`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`trace`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`RawClient, NewRawClient, Get, Delete, List, Deletemultiple`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`, `backend/pkg/observability/langfuse/api/core`, `backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/api/client/client.go`
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。

## `backend/pkg/observability/langfuse/api/types.go`

- 文件类型：`.go`
- 大小：`115371` 字节
- 文本行数：`3745`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`api`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`是`
- 关键导出/符号：`BasePrompt, GetName, GetVersion, GetConfig, GetLabels, GetTags, GetCommitMessage, GetResolutionGraph, GetExtraProperties, SetName, SetVersion, SetConfig`
- 直接依赖：`backend/pkg/observability/langfuse/api/internal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/observability/langfuse/agent.go`, `backend/pkg/observability/langfuse/api/annotationqueues/client.go`, `backend/pkg/observability/langfuse/api/annotationqueues/raw_client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/client.go`, `backend/pkg/observability/langfuse/api/blobstorageintegrations/raw_client.go`, `backend/pkg/observability/langfuse/api/comments/client.go`, `backend/pkg/observability/langfuse/api/comments/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetitems/client.go`, `backend/pkg/observability/langfuse/api/datasetitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/client.go`, `backend/pkg/observability/langfuse/api/datasetrunitems/raw_client.go`, `backend/pkg/observability/langfuse/api/datasets/client.go` 等 70 项
- 备注：生成产物，优先修改上游 schema、注解或源码后再重新生成。；长文件（3745 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/observability/langfuse/chain.go`

- 文件类型：`.go`
- 大小：`5417` 字节
- 文本行数：`215`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`Chain, ChainOption, WithChainID, WithChainName, WithChainMetadata, WithChainInput, WithChainOutput, WithChainStartTime, WithChainEndTime, WithChainLevel, WithChainStatus, WithChainVersion`
- 直接依赖：`backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/client.go`

- 文件类型：`.go`
- 大小：`18110` 字节
- 文本行数：`369`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`InstrumentationVersion, AnnotationQueuesClient, BlobStorageIntegrationsClient, CommentsClient, DatasetitemsClient, DatasetrunitemsClient, DatasetsClient, HealthClient, IngestionClient, MediaClient, MetricsV2Client, MetricsClient`
- 直接依赖：`backend/pkg/observability/langfuse/api`, `backend/pkg/observability/langfuse/api/client`, `backend/pkg/observability/langfuse/api/option`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/context.go`

- 文件类型：`.go`
- 大小：`585` 字节
- 文本行数：`22`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`ObservationContextKey`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/context_test.go`

- 文件类型：`.go`
- 大小：`1499` 字节
- 文本行数：`64`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`TestObservationContext_RoundTrip, TestGetObservationContext_NotFound, TestObservationContext_NestedOverride`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/observability/langfuse/converter.go`

- 文件类型：`.go`
- 大小：`12480` 字节
- 文本行数：`498`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/converter_test.go`

- 文件类型：`.go`
- 大小：`14903` 字节
- 文本行数：`563`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`TestConvertInput, TestConvertOutput, TestRoleMapping, TestToolContentParsing, TestThinkingExtraction, TestJoinTextParts, TestEdgeCases, BenchmarkConvertInput, TestRealWorldScenario`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/observability/langfuse/embedding.go`

- 文件类型：`.go`
- 大小：`5899` 字节
- 文本行数：`224`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`Embedding, EmbeddingOption, WithEmbeddingID, WithEmbeddingName, WithEmbeddingMetadata, WithEmbeddingInput, WithEmbeddingOutput, WithEmbeddingStartTime, WithEmbeddingEndTime, WithEmbeddingLevel, WithEmbeddingStatus, WithEmbeddingVersion`
- 直接依赖：`backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/evaluator.go`

- 文件类型：`.go`
- 大小：`6580` 字节
- 文本行数：`242`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`Evaluator, EvaluatorOption, WithEvaluatorID, WithEvaluatorName, WithEvaluatorMetadata, WithEvaluatorInput, WithEvaluatorOutput, WithEvaluatorStartTime, WithEvaluatorEndTime, WithEvaluatorLevel, WithEvaluatorStatus, WithEvaluatorVersion`
- 直接依赖：`backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/event.go`

- 文件类型：`.go`
- 大小：`4003` 字节
- 文本行数：`168`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`Event, EventOption, WithEventName, WithEventMetadata, WithEventInput, WithEventOutput, WithEventTime, WithEventLevel, WithEventStatus, WithEventVersion, String, MarshalJSON`
- 直接依赖：`backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/generation.go`

- 文件类型：`.go`
- 大小：`8164` 字节
- 文本行数：`284`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`Generation, GenerationOption, WithGenerationID, WithGenerationName, WithGenerationMetadata, WithGenerationInput, WithGenerationOutput, WithGenerationStartTime, WithGenerationEndTime, WithGenerationCompletionStartTime, WithGenerationLevel, WithGenerationStatus`
- 直接依赖：`backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/guardrail.go`

- 文件类型：`.go`
- 大小：`6578` 字节
- 文本行数：`242`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`Guardrail, GuardrailOption, WithGuardrailID, WithGuardrailName, WithGuardrailMetadata, WithGuardrailInput, WithGuardrailOutput, WithGuardrailStartTime, WithGuardrailEndTime, WithGuardrailLevel, WithGuardrailStatus, WithGuardrailVersion`
- 直接依赖：`backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/helpers.go`

- 文件类型：`.go`
- 大小：`8910` 字节
- 文本行数：`338`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`Metadata, ObservationLevel, ToLangfuse, GenerationUsageUnit, String, ToLangfuse, GenerationUsage, ToLangfuse, ModelParameters, ToLangfuse, GetLangchainModelParameters`
- 直接依赖：`backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/helpers_test.go`

- 文件类型：`.go`
- 大小：`14751` 字节
- 文本行数：`537`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`TestMergeMaps, TestMergeMaps_DoesNotMutateDst, TestObservationLevel_ToLangfuse, TestGenerationUsageUnit_String, TestGenerationUsageUnit_ToLangfuse, TestGenerationUsage_ToLangfuse, TestModelParameters_ToLangfuse, TestGetLangchainModelParameters, TestNewTraceID, TestNewSpanID, TestGetCurrentTime, TestGetCurrentTimeString`
- 直接依赖：`backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/observability/langfuse/noop.go`

- 文件类型：`.go`
- 大小：`1303` 字节
- 文本行数：`58`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`NewNoopObserver, NewObservation, Shutdown, ForceFlush`
- 直接依赖：`backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/noop_test.go`

- 文件类型：`.go`
- 大小：`5138` 字节
- 文本行数：`175`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`TestNewNoopObserver_ImplementsObserver, TestNoopObserver_NewObservation_NewTrace, TestNoopObserver_NewObservation_InheritsParentTrace, TestNoopObserver_NewObservation_ExplicitTraceID, TestNoopObserver_NewObservation_InheritsParentObservationID, TestNoopObserver_NewObservation_ExplicitObservationID, TestNoopObserver_NewObservation_ExplicitObsIDNoParent, TestNoopObserver_NewObservation_ExplicitTraceDoesNotInheritObsID, TestNoopObserver_Shutdown, TestNoopObserver_ForceFlush, TestNoopObserver_Enqueue_NoPanic`
- 直接依赖：`backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/pkg/observability/langfuse/observation.go`

- 文件类型：`.go`
- 大小：`5216` 字节
- 文本行数：`194`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`Observation, ID, TraceID, String, Log, Score, Event, Span, Generation, Agent, Tool, Chain`
- 直接依赖：`backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/observer.go`

- 文件类型：`.go`
- 大小：`5936` 字节
- 文本行数：`255`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`Observer, NewObserver, NewObservation, Shutdown, ForceFlush`
- 直接依赖：`backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/options.go`

- 文件类型：`.go`
- 大小：`655` 字节
- 文本行数：`36`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`ObserverOption, WithProject, WithRelease, WithSendInterval, WithSendTimeout, WithQueueSize`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/retriever.go`

- 文件类型：`.go`
- 大小：`6580` 字节
- 文本行数：`242`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`Retriever, RetrieverOption, WithRetrieverID, WithRetrieverName, WithRetrieverMetadata, WithRetrieverInput, WithRetrieverOutput, WithRetrieverStartTime, WithRetrieverEndTime, WithRetrieverLevel, WithRetrieverStatus, WithRetrieverVersion`
- 直接依赖：`backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/score.go`

- 文件类型：`.go`
- 大小：`3381` 字节
- 文本行数：`136`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`ScoreOption, WithScoreID, WithScoreName, WithScoreMetadata, WithScoreTime, WithScoreFloatValue, WithScoreStringValue, WithScoreComment, WithScoreConfigID, WithScoreQueueID`
- 直接依赖：`backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/span.go`

- 文件类型：`.go`
- 大小：`5316` 字节
- 文本行数：`215`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`Span, SpanOption, WithSpanID, WithSpanName, WithSpanMetadata, WithSpanInput, WithSpanOutput, WithSpanStartTime, WithSpanEndTime, WithSpanLevel, WithSpanStatus, WithSpanVersion`
- 直接依赖：`backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/tool.go`

- 文件类型：`.go`
- 大小：`5356` 字节
- 文本行数：`215`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`Tool, ToolOption, WithToolID, WithToolName, WithToolMetadata, WithToolInput, WithToolOutput, WithToolStartTime, WithToolEndTime, WithToolLevel, WithToolStatus, WithToolVersion`
- 直接依赖：`backend/pkg/observability/langfuse/api`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/langfuse/trace.go`

- 文件类型：`.go`
- 大小：`1874` 字节
- 文本行数：`79`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`langfuse`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`TraceContext, TraceContextOption, WithTraceTimestamp, WithTraceName, WithTraceUserID, WithTraceInput, WithTraceOutput, WithTraceSessionID, WithTraceVersion, WithTraceMetadata, WithTraceTags, WithTracePublic`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/worker/tester.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/context.go`, `backend/pkg/controller/flow.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/embedder.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/performer.go` 等 29 项

## `backend/pkg/observability/lfclient.go`

- 文件类型：`.go`
- 大小：`2858` 字节
- 文本行数：`113`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`observability`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`LangfuseClient, API, Observer, Shutdown, ForceFlush, NewLangfuseClient`
- 直接依赖：`backend/pkg/config`, `backend/pkg/observability/langfuse`, `backend/pkg/system`, `backend/pkg/version`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/subtask.go`, `backend/pkg/controller/task.go`, `backend/pkg/database/database.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go` 等 34 项

## `backend/pkg/observability/obs.go`

- 文件类型：`.go`
- 大小：`23136` 字节
- 文本行数：`735`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`observability`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`SpanContextKey, ErrNotConfigured, InstrumentationVersion, Observability, Langfuse, Tracer, Meter, Collector, Dumper, InitObserver, Flush, Shutdown`
- 直接依赖：`backend/pkg/observability/langfuse`, `backend/pkg/version`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/subtask.go`, `backend/pkg/controller/task.go`, `backend/pkg/database/database.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go` 等 34 项
- 备注：包含 TODO，后续维护时可重点留意未完成事项。

## `backend/pkg/observability/otelclient.go`

- 文件类型：`.go`
- 大小：`5305` 字节
- 文本行数：`187`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`observability`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`TelemetryClient, Logger, Tracer, Meter, Shutdown, ForceFlush, NewTelemetryClient`
- 直接依赖：`backend/pkg/config`, `backend/pkg/version`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/assistant.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/subtask.go`, `backend/pkg/controller/task.go`, `backend/pkg/database/database.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/embeddings/wrapper.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go` 等 34 项

## `backend/pkg/observability/profiling/profiling.go`

- 文件类型：`.go`
- 大小：`1194` 字节
- 文本行数：`32`
- 所属分组：`backend/pkg/observability`
- 所属包/模块：`profiling`
- 推断作用：可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。
- 生成文件：`否`
- 关键导出/符号：`Start`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/pentagi/main.go`
