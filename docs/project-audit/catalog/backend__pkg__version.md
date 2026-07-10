# `backend/pkg/version` 文件清单

本组共 `2` 个文件。

## `backend/pkg/version/version.go`

- 文件类型：`.go`
- 大小：`639` 字节
- 文本行数：`37`
- 所属分组：`backend/pkg/version`
- 所属包/模块：`version`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/version` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`GetBinaryVersion, IsDevelopMode, GetBinaryName`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/cmd/etester/main.go`, `backend/cmd/ftester/main.go`, `backend/cmd/installer/checker/checker.go`, `backend/cmd/installer/main.go`, `backend/cmd/installer/main_test.go`, `backend/cmd/installer/processor/logic_test.go`, `backend/cmd/installer/processor/update.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go` 等 17 项

## `backend/pkg/version/version_test.go`

- 文件类型：`.go`
- 大小：`1510` 字节
- 文本行数：`74`
- 所属分组：`backend/pkg/version`
- 所属包/模块：`version`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/version` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`TestGetBinaryVersion_Default, TestGetBinaryVersion_WithVersion, TestGetBinaryVersion_WithVersionAndRevision, TestGetBinaryVersion_WithRevisionOnly, TestIsDevelopMode_True, TestIsDevelopMode_False, TestGetBinaryName_Default, TestGetBinaryName_Custom`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/cmd/etester/main.go`, `backend/cmd/ftester/main.go`, `backend/cmd/installer/checker/checker.go`, `backend/cmd/installer/main.go`, `backend/cmd/installer/main_test.go`, `backend/cmd/installer/processor/logic_test.go`, `backend/cmd/installer/processor/update.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/graph/schema.resolvers.go`, `backend/pkg/observability/lfclient.go`, `backend/pkg/observability/obs.go` 等 17 项
- 备注：测试文件，用于验证对应模块行为。
