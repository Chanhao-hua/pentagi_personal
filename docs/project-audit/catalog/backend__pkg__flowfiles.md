# `backend/pkg/flowfiles` 文件清单

本组共 `2` 个文件。

## `backend/pkg/flowfiles/files.go`

- 文件类型：`.go`
- 大小：`28609` 字节
- 文本行数：`990`
- 所属分组：`backend/pkg/flowfiles`
- 所属包/模块：`flowfiles`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/flowfiles` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`File, Files, TarEntry, List, FlowDataDir, FlowUploadsDir, FlowContainerDir, FlowResourcesDir, ResolveCachedPath, SanitizeFileName, SanitizeContainerCachePath, NewFile`
- 直接依赖：`backend/pkg/docker`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/controller/flow.go`, `backend/pkg/graph/context.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/provider.go`, `backend/pkg/server/services/flow_files.go`, `backend/pkg/server/services/flow_files_test.go`, `backend/pkg/tools/terminal_test.go`, `backend/pkg/tools/tools.go`
- 备注：长文件（990 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/pkg/flowfiles/files_test.go`

- 文件类型：`.go`
- 大小：`35630` 字节
- 文本行数：`1002`
- 所属分组：`backend/pkg/flowfiles`
- 所属包/模块：`flowfiles`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/flowfiles` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`TestFlowDirs, TestSanitizeFileName, TestSanitizeContainerCachePath, TestResolveCachedPath, TestListDirEntries, TestListDirEntriesMissingDir, TestListDirEntriesRecursivePreservesNestedPaths, TestListBothSources, TestLocalEntryExistsAndRegularFileInfo, TestSaveUploadedFileToTemp, TestIsWithinDir, TestResolvePulledStagedTarget`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/controller/flow.go`, `backend/pkg/graph/context.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/providers/provider.go`, `backend/pkg/server/services/flow_files.go`, `backend/pkg/server/services/flow_files_test.go`, `backend/pkg/tools/terminal_test.go`, `backend/pkg/tools/tools.go`
- 备注：测试文件，用于验证对应模块行为。；长文件（1002 行），属于复杂度热点，阅读时建议先看对外导出和测试。
