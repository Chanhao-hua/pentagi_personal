# `backend/pkg/schema` 文件清单

本组共 `2` 个文件。

## `backend/pkg/schema/schema.go`

- 文件类型：`.go`
- 大小：`8503` 字节
- 文本行数：`230`
- 所属分组：`backend/pkg/schema`
- 所属包/模块：`schema`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/schema` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`IValid, Schema, GetValidator, ValidateString, ValidateBytes, ValidateGo, Valid, Value, Scan, Definitions, Type, MarshalJSON`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/providers/handlers.go`, `backend/pkg/tools/executor.go`, `backend/pkg/tools/tools.go`

## `backend/pkg/schema/schema_test.go`

- 文件类型：`.go`
- 大小：`13138` 字节
- 文本行数：`530`
- 所属分组：`backend/pkg/schema`
- 所属包/模块：`schema`
- 推断作用：文本文件，当前未命中特定规则，建议结合所在目录 `backend/pkg/schema` 的上下文阅读。
- 生成文件：`否`
- 关键导出/符号：`TestSchemaValid, TestSchemaGetValidator, TestSchemaValidateString, TestSchemaValidateBytes, TestSchemaValidateGo, TestSchemaValueScan, TestTypeMarshalJSON, TestTypeUnmarshalJSON, TestSchemaValidateObjectWithEnum, TestSchemaValidateWithPattern, TestSchemaValidateArray, TestScanFromJSON`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/pkg/providers/handlers.go`, `backend/pkg/tools/executor.go`, `backend/pkg/tools/tools.go`
- 备注：测试文件，用于验证对应模块行为。
