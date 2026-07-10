# `backend/pkg/config` 文件清单

本组共 `2` 个文件。

## `backend/pkg/config/config.go`

- 文件类型：`.go`
- 大小：`15170` 字节
- 文本行数：`356`
- 所属分组：`backend/pkg/config`
- 所属包/模块：`config`
- 推断作用：后端配置加载与环境变量解析文件。
- 生成文件：`否`
- 关键导出/符号：`Config, NewConfig, GetSecretPatterns`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/cmd/etester/main.go`, `backend/cmd/etester/tester.go`, `backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/loader/loader.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/docker/client.go`, `backend/pkg/graph/resolver.go` 等 58 项

## `backend/pkg/config/config_test.go`

- 文件类型：`.go`
- 大小：`19379` 字节
- 文本行数：`612`
- 所属分组：`backend/pkg/config`
- 所属包/模块：`config`
- 推断作用：后端配置加载与环境变量解析文件。
- 生成文件：`否`
- 关键导出/符号：`TestGetSecretPatterns_Empty, TestGetSecretPatterns_WithSecrets, TestGetSecretPatterns_TrimsWhitespace, TestGetSecretPatterns_SkipsEmptyStrings, TestGetSecretPatterns_PatternCompilation, TestGetSecretPatterns_AllFields, TestNewConfig_Defaults, TestNewConfig_EnvOverride, TestNewConfig_ProviderDefaults, TestNewConfig_StaticURL, TestNewConfig_StaticURL_Empty, TestNewConfig_SummarizerDefaults`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ctester/main.go`, `backend/cmd/etester/main.go`, `backend/cmd/etester/tester.go`, `backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/installer/loader/loader.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/docker/client.go`, `backend/pkg/graph/resolver.go` 等 58 项
- 备注：测试文件，用于验证对应模块行为。
