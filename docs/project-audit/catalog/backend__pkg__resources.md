# `backend/pkg/resources` 文件清单

本组共 `2` 个文件。

## `backend/pkg/resources/resources.go`

- 文件类型：`.go`
- 大小：`12978` 字节
- 文本行数：`436`
- 所属分组：`backend/pkg/resources`
- 所属包/模块：`resources`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/resources` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`ResourceEntry, ZipEntry, ResourcesDir, BlobPath, EnsureResourcesDir, ComputeFileMD5, IsValidBlobHash, BlobExists, DeleteBlob, SanitizeResourcePath, SanitizeResourceDir, SanitizeResourceFileName`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/controller/flow.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/services/flow_files.go`, `backend/pkg/server/services/flow_files_test.go`, `backend/pkg/server/services/resources.go`, `backend/pkg/server/services/resources_test.go`

## `backend/pkg/resources/resources_test.go`

- 文件类型：`.go`
- 大小：`8650` 字节
- 文本行数：`264`
- 所属分组：`backend/pkg/resources`
- 所属包/模块：`resources`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/resources` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`TestResourceDirsAndBlobPath, TestComputeFileMD5, TestIsValidBlobHash, TestBlobLifecycle, TestSanitizeResourcePath, TestSanitizeResourceDir, TestSanitizeResourceFileName, TestPathHelpers, TestEscapeLike, TestZipResources, TestZipResourcesSkipsNonRegularBlobs, TestZipDirectory`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/controller/flow.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/server/services/flow_files.go`, `backend/pkg/server/services/flow_files_test.go`, `backend/pkg/server/services/resources.go`, `backend/pkg/server/services/resources_test.go`
- 备注：测试文件，用于验证对应模块行为。
