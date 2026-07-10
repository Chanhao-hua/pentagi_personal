# `backend/cmd/installer` 文件清单

本组共 `113` 个文件。

## `backend/cmd/installer/checker/checker.go`

- 文件类型：`.go`
- 大小：`26838` 字节
- 文本行数：`691`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`checker`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`CheckResult, CheckHandler, GatherAllInfo, GatherDockerInfo, GatherWorkerInfo, GatherPentagiInfo, GatherGraphitiInfo, GatherLangfuseInfo, GatherObservabilityInfo, GatherSystemInfo, GatherUpdatesInfo, IsReadyToContinue`
- 直接依赖：`backend/cmd/installer/state`, `backend/pkg/version`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/hardening/hardening.go`, `backend/cmd/installer/hardening/hardening_test.go`, `backend/cmd/installer/main.go`, `backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/processor/logic_test.go`, `backend/cmd/installer/processor/mock_test.go`, `backend/cmd/installer/processor/model.go`, `backend/cmd/installer/processor/processor.go`, `backend/cmd/installer/processor/update.go`, `backend/cmd/installer/wizard/app.go` 等 14 项

## `backend/cmd/installer/checker/helpers.go`

- 文件类型：`.go`
- 大小：`29718` 字节
- 文本行数：`1025`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`checker`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`DockerVersion, ImageInfo, CheckUpdatesRequest, CheckUpdatesResponse, DockerErrorType`
- 直接依赖：`backend/cmd/installer/state`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/hardening/hardening.go`, `backend/cmd/installer/hardening/hardening_test.go`, `backend/cmd/installer/main.go`, `backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/processor/logic_test.go`, `backend/cmd/installer/processor/mock_test.go`, `backend/cmd/installer/processor/model.go`, `backend/cmd/installer/processor/processor.go`, `backend/cmd/installer/processor/update.go`, `backend/cmd/installer/wizard/app.go` 等 14 项
- 备注：长文件（1025 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/cmd/installer/checker/helpers_test.go`

- 文件类型：`.go`
- 大小：`25593` 字节
- 文本行数：`840`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`checker`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`GetVar, GetVars, GetEnvPath, Exists, Reset, Commit, IsDirty, GetEulaConsent, SetEulaConsent, SetStack, GetStack, SetVar`
- 直接依赖：`backend/cmd/installer/loader`, `backend/cmd/installer/state`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/hardening/hardening.go`, `backend/cmd/installer/hardening/hardening_test.go`, `backend/cmd/installer/main.go`, `backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/processor/logic_test.go`, `backend/cmd/installer/processor/mock_test.go`, `backend/cmd/installer/processor/model.go`, `backend/cmd/installer/processor/processor.go`, `backend/cmd/installer/processor/update.go`, `backend/cmd/installer/wizard/app.go` 等 14 项
- 备注：测试文件，用于验证对应模块行为。；长文件（840 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/cmd/installer/files/.gitignore`

- 文件类型：`<none>`
- 大小：`24` 字节
- 文本行数：`4`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`未识别`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/cmd/installer/files/files.go`

- 文件类型：`.go`
- 大小：`11276` 字节
- 文本行数：`402`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`files`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`FileStatus, Files, EmbeddedProvider, NewFiles, GetContent, Exists, ExistsInFS, Stat, Copy, Check, List`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/hardening/migrations.go`, `backend/cmd/installer/main.go`, `backend/cmd/installer/processor/fs.go`, `backend/cmd/installer/processor/fs_test.go`, `backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/processor/logic_test.go`, `backend/cmd/installer/processor/mock_test.go`, `backend/cmd/installer/processor/model.go`, `backend/cmd/installer/processor/processor.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/controller/controller.go`, `backend/cmd/installer/wizard/models/apply_changes.go` 等 14 项

## `backend/cmd/installer/files/files_test.go`

- 文件类型：`.go`
- 大小：`16479` 字节
- 文本行数：`610`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`files`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`TestNewFiles, TestGetContent_FromFS, TestExistsInFS, TestStat_FromFS, TestCopy_File, TestCopy_PreservesExecutable_FromFS, TestCheck_DetectsPermissionMismatch_FromFS, TestCopy_Directory, TestCopy_WithoutRewrite, TestCopy_WithRewrite, TestExists_WithoutEmbedded, TestCopy_FromEmbedded`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/hardening/migrations.go`, `backend/cmd/installer/main.go`, `backend/cmd/installer/processor/fs.go`, `backend/cmd/installer/processor/fs_test.go`, `backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/processor/logic_test.go`, `backend/cmd/installer/processor/mock_test.go`, `backend/cmd/installer/processor/model.go`, `backend/cmd/installer/processor/processor.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/controller/controller.go`, `backend/cmd/installer/wizard/models/apply_changes.go` 等 14 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/cmd/installer/files/generate.go`

- 文件类型：`.go`
- 大小：`22689` 字节
- 文本行数：`828`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`main`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`FileMetadata, MetadataFile, FileMetadata, MetadataFile, GetContent, Exists, Stat, Copy, List, CheckHash, ExpectedMode, TestToEmbedPath`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/hardening/migrations.go`, `backend/cmd/installer/main.go`, `backend/cmd/installer/processor/fs.go`, `backend/cmd/installer/processor/fs_test.go`, `backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/processor/logic_test.go`, `backend/cmd/installer/processor/mock_test.go`, `backend/cmd/installer/processor/model.go`, `backend/cmd/installer/processor/processor.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/controller/controller.go`, `backend/cmd/installer/wizard/models/apply_changes.go` 等 14 项
- 备注：长文件（828 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/cmd/installer/files/links/.env`

- 文件类型：`<none>`
- 大小：`27` 字节
- 文本行数：`1`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`未识别`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/cmd/installer/files/links/EULA.md`

- 文件类型：`.md`
- 大小：`22` 字节
- 文本行数：`1`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`未识别`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/cmd/installer/files/links/docker-compose-graphiti.yml`

- 文件类型：`.yml`
- 大小：`42` 字节
- 文本行数：`1`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`未识别`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/cmd/installer/files/links/docker-compose-langfuse.yml`

- 文件类型：`.yml`
- 大小：`42` 字节
- 文本行数：`1`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`未识别`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/cmd/installer/files/links/docker-compose-observability.yml`

- 文件类型：`.yml`
- 大小：`47` 字节
- 文本行数：`1`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`未识别`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/cmd/installer/files/links/docker-compose.yml`

- 文件类型：`.yml`
- 大小：`33` 字节
- 文本行数：`1`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`未识别`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/cmd/installer/files/links/example.custom.provider.yml`

- 文件类型：`.yml`
- 大小：`58` 字节
- 文本行数：`1`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`未识别`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/cmd/installer/files/links/example.ollama.provider.yml`

- 文件类型：`.yml`
- 大小：`70` 字节
- 文本行数：`1`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`未识别`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/cmd/installer/files/links/observability`

- 文件类型：`<none>`
- 大小：`28` 字节
- 文本行数：`1`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`未识别`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/cmd/installer/files/links/providers-configs`

- 文件类型：`<none>`
- 大小：`31` 字节
- 文本行数：`1`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`未识别`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用：`当前未发现`

## `backend/cmd/installer/hardening/hardening.go`

- 文件类型：`.go`
- 大小：`12688` 字节
- 文本行数：`367`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`hardening`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`HardeningArea, HardeningPolicyType, HardeningPolicy, DoHardening`
- 直接依赖：`backend/cmd/installer/checker`, `backend/cmd/installer/loader`, `backend/cmd/installer/state`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/main.go`

## `backend/cmd/installer/hardening/hardening_test.go`

- 文件类型：`.go`
- 大小：`50265` 字节
- 文本行数：`1582`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`hardening`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`GetVar, GetVars, GetEnvPath, Exists, Reset, IsDirty, GetEulaConsent, SetEulaConsent, SetStack, GetStack, ResetVar, ResetVars`
- 直接依赖：`backend/cmd/installer/checker`, `backend/cmd/installer/loader`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/main.go`
- 备注：测试文件，用于验证对应模块行为。；长文件（1582 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/cmd/installer/hardening/migrations.go`

- 文件类型：`.go`
- 大小：`2872` 字节
- 文本行数：`89`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`hardening`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`DoMigrateSettings`
- 直接依赖：`backend/cmd/installer/files`, `backend/cmd/installer/state`, `backend/cmd/installer/wizard/controller`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/main.go`

## `backend/cmd/installer/hardening/migrations_test.go`

- 文件类型：`.go`
- 大小：`28857` 字节
- 文本行数：`930`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`hardening`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`TestDoMigrateSettings_SuccessfulMigrations, TestDoMigrateSettings_VariableNotSet, TestDoMigrateSettings_EmptyVariable, TestDoMigrateSettings_PathNotExist, TestDoMigrateSettings_AlreadyDefaultValue, TestDoMigrateSettings_EmbeddedConfigs, TestDoMigrateSettings_WrongPathType, TestDoMigrateSettings_ErrorHandling, TestDoMigrateSettings_CombinedMigrations, TestCheckPathInHostFS`
- 直接依赖：`backend/cmd/installer/loader`, `backend/cmd/installer/wizard/controller`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/main.go`
- 备注：测试文件，用于验证对应模块行为。；长文件（930 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/cmd/installer/hardening/network.go`

- 文件类型：`.go`
- 大小：`2012` 字节
- 文本行数：`66`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`hardening`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`DoSyncNetworkSettings`
- 直接依赖：`backend/cmd/installer/state`, `backend/cmd/installer/wizard/controller`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/main.go`

## `backend/cmd/installer/hardening/network_test.go`

- 文件类型：`.go`
- 大小：`32215` 字节
- 文本行数：`1052`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`hardening`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`GetVar, GetVars, SetVar, SetVars, GetEnvPath, Exists, Reset, Commit, IsDirty, GetEulaConsent, SetEulaConsent, SetStack`
- 直接依赖：`backend/cmd/installer/loader`, `backend/cmd/installer/wizard/controller`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/main.go`
- 备注：测试文件，用于验证对应模块行为。；长文件（1052 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/cmd/installer/loader/example_test.go`

- 文件类型：`.go`
- 大小：`1966` 字节
- 文本行数：`74`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`loader`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`ExampleEnvFile_workflow`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/checker/helpers_test.go`, `backend/cmd/installer/hardening/hardening.go`, `backend/cmd/installer/hardening/hardening_test.go`, `backend/cmd/installer/hardening/migrations_test.go`, `backend/cmd/installer/hardening/network_test.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/processor/mock_test.go`, `backend/cmd/installer/state/state.go`, `backend/cmd/installer/wizard/controller/controller.go`, `backend/cmd/installer/wizard/models/ai_agents_settings_form.go`, `backend/cmd/installer/wizard/models/base_controls.go`, `backend/cmd/installer/wizard/models/docker_form.go` 等 19 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/cmd/installer/loader/file.go`

- 文件类型：`.go`
- 大小：`5434` 字节
- 文本行数：`244`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`loader`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`EnvVar, IsDefault, IsPresent, EnvFile, Del, Set, Get, GetAll, SetAll, Save, Clone`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/checker/helpers_test.go`, `backend/cmd/installer/hardening/hardening.go`, `backend/cmd/installer/hardening/hardening_test.go`, `backend/cmd/installer/hardening/migrations_test.go`, `backend/cmd/installer/hardening/network_test.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/processor/mock_test.go`, `backend/cmd/installer/state/state.go`, `backend/cmd/installer/wizard/controller/controller.go`, `backend/cmd/installer/wizard/models/ai_agents_settings_form.go`, `backend/cmd/installer/wizard/models/base_controls.go`, `backend/cmd/installer/wizard/models/docker_form.go` 等 19 项

## `backend/cmd/installer/loader/loader.go`

- 文件类型：`.go`
- 大小：`2756` 字节
- 文本行数：`132`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`loader`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`LoadEnvFile`
- 直接依赖：`backend/pkg/config`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/checker/helpers_test.go`, `backend/cmd/installer/hardening/hardening.go`, `backend/cmd/installer/hardening/hardening_test.go`, `backend/cmd/installer/hardening/migrations_test.go`, `backend/cmd/installer/hardening/network_test.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/processor/mock_test.go`, `backend/cmd/installer/state/state.go`, `backend/cmd/installer/wizard/controller/controller.go`, `backend/cmd/installer/wizard/models/ai_agents_settings_form.go`, `backend/cmd/installer/wizard/models/base_controls.go`, `backend/cmd/installer/wizard/models/docker_form.go` 等 19 项

## `backend/cmd/installer/loader/loader_test.go`

- 文件类型：`.go`
- 大小：`18056` 字节
- 文本行数：`699`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`loader`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`TestLoadEnvFile, TestLoadEnvFileErrors, TestEnvVarMethods, TestEnvFileSetGet, TestEnvFileSave, TestEnvFileSaveNewFile, TestEnvFileSaveErrors, TestEnvFileClone, TestLoadVarsEdgeCases, TestPatchRaw, TestEnvFileDelInSave, TestSetDefaultVarsNilURL`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/checker/helpers_test.go`, `backend/cmd/installer/hardening/hardening.go`, `backend/cmd/installer/hardening/hardening_test.go`, `backend/cmd/installer/hardening/migrations_test.go`, `backend/cmd/installer/hardening/network_test.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/processor/mock_test.go`, `backend/cmd/installer/state/state.go`, `backend/cmd/installer/wizard/controller/controller.go`, `backend/cmd/installer/wizard/models/ai_agents_settings_form.go`, `backend/cmd/installer/wizard/models/base_controls.go`, `backend/cmd/installer/wizard/models/docker_form.go` 等 19 项
- 备注：测试文件，用于验证对应模块行为。

## `backend/cmd/installer/main.go`

- 文件类型：`.go`
- 大小：`5740` 字节
- 文本行数：`206`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`main`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`Config`
- 直接依赖：`backend/cmd/installer/checker`, `backend/cmd/installer/files`, `backend/cmd/installer/hardening`, `backend/cmd/installer/state`, `backend/cmd/installer/wizard`, `backend/pkg/version`
- 被这些文件直接引用：`当前未发现`

## `backend/cmd/installer/main_test.go`

- 文件类型：`.go`
- 大小：`4492` 字节
- 文本行数：`190`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`main`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`TestParseFlags, TestValidateEnvPath, TestCreateEmptyEnvFile, TestInitializeState`
- 直接依赖：`backend/pkg/version`
- 被这些文件直接引用：`当前未发现`
- 备注：测试文件，用于验证对应模块行为。

## `backend/cmd/installer/navigator/navigator.go`

- 文件类型：`.go`
- 大小：`2271` 字节
- 文本行数：`100`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`navigator`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`Navigator, NavigatorStack, Strings, String, NewNavigator, Push, Pop, Current, CanGoBack, GetStack, String`
- 直接依赖：`backend/cmd/installer/checker`, `backend/cmd/installer/state`, `backend/cmd/installer/wizard/logger`, `backend/cmd/installer/wizard/models`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`

## `backend/cmd/installer/navigator/navigator_test.go`

- 文件类型：`.go`
- 大小：`9029` 字节
- 文本行数：`322`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`navigator`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`Exists, Reset, Commit, IsDirty, GetEulaConsent, SetEulaConsent, GetStack, SetStack, GetVar, SetVar, ResetVar, GetVars`
- 直接依赖：`backend/cmd/installer/checker`, `backend/cmd/installer/loader`, `backend/cmd/installer/wizard/models`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/cmd/installer/processor/compose.go`

- 文件类型：`.go`
- 大小：`8685` 字节
- 文本行数：`221`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`processor`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/processor/docker.go`

- 文件类型：`.go`
- 大小：`15219` 字节
- 文本行数：`433`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`processor`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`backend/pkg/tools`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/processor/fs.go`

- 文件类型：`.go`
- 大小：`15198` 字节
- 文本行数：`428`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`processor`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`backend/cmd/installer/files`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/processor/fs_test.go`

- 文件类型：`.go`
- 大小：`23490` 字节
- 文本行数：`713`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`processor`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`TestFileSystemOperationsImpl_EnsureStackIntegrity, TestFileSystemOperationsImpl_VerifyStackIntegrity, TestFileSystemOperationsImpl_CleanupStackFiles, TestFileSystemOperationsImpl_EnsureFileFromEmbed, TestFileSystemOperationsImpl_VerifyDirectoryContentIntegrity, TestFileSystemOperationsImpl_ExcludedFilesHandling, TestFileSystemOperationsImpl_FileExists, TestFileSystemOperationsImpl_DirectoryExists, TestFileSystemOperationsImpl_ValidateYamlFile, TestCheckStackIntegrity, TestCheckStackIntegrity_RealFiles, TestFileSystemOperations_IntegrityWithForceMode`
- 直接依赖：`backend/cmd/installer/files`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/cmd/installer/wizard/registry/registry.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/cmd/installer/processor/locale.go`

- 文件类型：`.go`
- 大小：`5909` 字节
- 文本行数：`131`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`processor`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`Subsystem, SubsystemOperationMessage, SubsystemOperationMessages`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/processor/logic.go`

- 文件类型：`.go`
- 大小：`28751` 字节
- 文本行数：`905`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`processor`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`backend/cmd/installer/checker`, `backend/cmd/installer/files`, `backend/cmd/installer/wizard/logger`, `backend/pkg/server/models`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/cmd/installer/wizard/registry/registry.go`
- 备注：长文件（905 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/cmd/installer/processor/logic_test.go`

- 文件类型：`.go`
- 大小：`42604` 字节
- 文本行数：`1236`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`processor`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`TestStart, TestStop, TestRestart, TestUpdate, TestRemove, TestApplyChanges_ErrorPropagation_FromEnsureNetworks, TestPurge_StrictAndDockerCleanup, TestApplyChanges_Embedded_AllStacksUpdated, TestApplyChanges_Disabled_RemovesInstalled, TestDownload_ComposeStacks, TestDownload_AllStacks, TestDownload_WorkerStack`
- 直接依赖：`backend/cmd/installer/checker`, `backend/cmd/installer/files`, `backend/pkg/version`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/cmd/installer/wizard/registry/registry.go`
- 备注：测试文件，用于验证对应模块行为。；长文件（1236 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/cmd/installer/processor/mock_test.go`

- 文件类型：`.go`
- 大小：`63343` 字节
- 文本行数：`2177`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`processor`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`Exists, Reset, Commit, IsDirty, GetEulaConsent, SetEulaConsent, SetStack, GetStack, GetVar, SetVar, ResetVar, GetVars`
- 直接依赖：`backend/cmd/installer/checker`, `backend/cmd/installer/files`, `backend/cmd/installer/loader`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/cmd/installer/wizard/registry/registry.go`
- 备注：测试文件，用于验证对应模块行为。；长文件（2177 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/cmd/installer/processor/model.go`

- 文件类型：`.go`
- 大小：`8118` 字节
- 文本行数：`231`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`processor`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`ProcessorModel, NewProcessorModel, ApplyChanges, CheckFiles, FactoryReset, Install, Update, Download, Remove, Purge, Start, Stop`
- 直接依赖：`backend/cmd/installer/checker`, `backend/cmd/installer/files`, `backend/cmd/installer/state`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/processor/pg.go`

- 文件类型：`.go`
- 大小：`2886` 字节
- 文本行数：`94`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`processor`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/processor/processor.go`

- 文件类型：`.go`
- 大小：`9942` 字节
- 文本行数：`254`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`processor`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`ProductStack, ProcessorOperation, ProductDockerNetwork, FilesCheckResult, Processor, WithForce, WithTerminal, WithPasswordValue, NewProcessor, ApplyChanges, CheckFiles, FactoryReset`
- 直接依赖：`backend/cmd/installer/checker`, `backend/cmd/installer/files`, `backend/cmd/installer/state`, `backend/cmd/installer/wizard/terminal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/processor/state.go`

- 文件类型：`.go`
- 大小：`4657` 字节
- 文本行数：`194`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`processor`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`ProcessorOutputMsg, ProcessorCompletionMsg, ProcessorStartedMsg, ProcessorWaitMsg, ProcessorFilesCheckMsg, OperationOption`
- 直接依赖：`backend/cmd/installer/wizard/terminal`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/processor/update.go`

- 文件类型：`.go`
- 大小：`7888` 字节
- 文本行数：`279`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`processor`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`backend/cmd/installer/checker`, `backend/pkg/version`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`, `backend/cmd/installer/wizard/models/reset_password.go`, `backend/cmd/installer/wizard/registry/registry.go`
- 备注：包含 TODO，后续维护时可重点留意未完成事项。

## `backend/cmd/installer/state/example_test.go`

- 文件类型：`.go`
- 大小：`6947` 字节
- 文本行数：`226`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`state`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`ExampleState_transactionWorkflow, ExampleState_rollbackWorkflow, ExampleState_persistenceWorkflow`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/checker/checker.go`, `backend/cmd/installer/checker/helpers.go`, `backend/cmd/installer/checker/helpers_test.go`, `backend/cmd/installer/hardening/hardening.go`, `backend/cmd/installer/hardening/migrations.go`, `backend/cmd/installer/hardening/network.go`, `backend/cmd/installer/main.go`, `backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/processor/model.go`, `backend/cmd/installer/processor/processor.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/controller/controller.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/cmd/installer/state/state.go`

- 文件类型：`.go`
- 大小：`6393` 字节
- 文本行数：`311`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`state`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`EULAConsentFile, State, NewState, Exists, Reset, Commit, IsDirty, GetEulaConsent, SetEulaConsent, SetStack, GetStack, GetVar`
- 直接依赖：`backend/cmd/installer/loader`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/checker/checker.go`, `backend/cmd/installer/checker/helpers.go`, `backend/cmd/installer/checker/helpers_test.go`, `backend/cmd/installer/hardening/hardening.go`, `backend/cmd/installer/hardening/migrations.go`, `backend/cmd/installer/hardening/network.go`, `backend/cmd/installer/main.go`, `backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/processor/model.go`, `backend/cmd/installer/processor/processor.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/controller/controller.go`

## `backend/cmd/installer/state/state_test.go`

- 文件类型：`.go`
- 大小：`18953` 字节
- 文本行数：`702`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`state`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`TestNewState, TestStateExists, TestStateStepManagement, TestStateVariableManagement, TestStateCommit, TestStateReset, TestStatePersistence, TestStateErrors`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/checker/checker.go`, `backend/cmd/installer/checker/helpers.go`, `backend/cmd/installer/checker/helpers_test.go`, `backend/cmd/installer/hardening/hardening.go`, `backend/cmd/installer/hardening/migrations.go`, `backend/cmd/installer/hardening/network.go`, `backend/cmd/installer/main.go`, `backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/processor/model.go`, `backend/cmd/installer/processor/processor.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/controller/controller.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/cmd/installer/wizard/app.go`

- 文件类型：`.go`
- 大小：`7399` 字节
- 文本行数：`260`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`wizard`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`App, NewApp, Init, Update, View, Run`
- 直接依赖：`backend/cmd/installer/checker`, `backend/cmd/installer/files`, `backend/cmd/installer/navigator`, `backend/cmd/installer/processor`, `backend/cmd/installer/state`, `backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/logger`, `backend/cmd/installer/wizard/models`, `backend/cmd/installer/wizard/registry`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/main.go`

## `backend/cmd/installer/wizard/controller/controller.go`

- 文件类型：`.go`
- 大小：`98242` 字节
- 文本行数：`2572`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`controller`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`Controller, LLMProviderConfigController, LangfuseConfigController, GraphitiConfigController, ObservabilityConfigController, SummarizerConfigController, EmbedderConfigController, AIAgentsConfigController, ScraperConfigController, SearchEnginesConfigController, DockerConfigController, ChangesConfigController`
- 直接依赖：`backend/cmd/installer/checker`, `backend/cmd/installer/files`, `backend/cmd/installer/loader`, `backend/cmd/installer/state`, `backend/cmd/installer/wizard/locale`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/hardening/migrations.go`, `backend/cmd/installer/hardening/migrations_test.go`, `backend/cmd/installer/hardening/network.go`, `backend/cmd/installer/hardening/network_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/models/ai_agents_settings_form.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/base_screen.go`, `backend/cmd/installer/wizard/models/docker_form.go`, `backend/cmd/installer/wizard/models/embedder_form.go`, `backend/cmd/installer/wizard/models/eula.go`, `backend/cmd/installer/wizard/models/graphiti_form.go` 等 31 项
- 备注：长文件（2572 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/cmd/installer/wizard/locale/locale.go`

- 文件类型：`.go`
- 大小：`122576` 字节
- 文本行数：`2396`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`locale`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/controller/controller.go`, `backend/cmd/installer/wizard/models/ai_agents_settings_form.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/base_screen.go`, `backend/cmd/installer/wizard/models/docker_form.go`, `backend/cmd/installer/wizard/models/embedder_form.go`, `backend/cmd/installer/wizard/models/eula.go`, `backend/cmd/installer/wizard/models/graphiti_form.go`, `backend/cmd/installer/wizard/models/langfuse_form.go`, `backend/cmd/installer/wizard/models/list_screen.go`, `backend/cmd/installer/wizard/models/llm_provider_form.go` 等 28 项
- 备注：长文件（2396 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/cmd/installer/wizard/logger/logger.go`

- 文件类型：`.go`
- 大小：`2155` 字节
- 文本行数：`128`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`logger`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`Log, Errorf, Debugf, Warnf, Fatalf, Panicf, GetLevel, SetLevel, SetOutput`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/processor/logic.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/models/ai_agents_settings_form.go`, `backend/cmd/installer/wizard/models/base_screen.go`, `backend/cmd/installer/wizard/models/docker_form.go`, `backend/cmd/installer/wizard/models/embedder_form.go`, `backend/cmd/installer/wizard/models/eula.go`, `backend/cmd/installer/wizard/models/graphiti_form.go`, `backend/cmd/installer/wizard/models/langfuse_form.go`, `backend/cmd/installer/wizard/models/llm_provider_form.go`, `backend/cmd/installer/wizard/models/observability_form.go` 等 18 项

## `backend/cmd/installer/wizard/models/ai_agents_settings_form.go`

- 文件类型：`.go`
- 大小：`13879` 字节
- 文本行数：`402`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`AIAgentsSettingsFormModel, NewAIAgentsSettingsFormModel, BuildForm, GetFormTitle, GetFormDescription, GetFormName, GetFormSummary, GetFormOverview, GetCurrentConfiguration, IsConfigured, GetHelpContent, HandleSave`
- 直接依赖：`backend/cmd/installer/loader`, `backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/logger`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/apply_changes.go`

- 文件类型：`.go`
- 大小：`14830` 字节
- 文本行数：`532`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`ApplyChangesFormModel, NewApplyChangesFormModel, BuildForm, GetFormTitle, GetFormDescription, GetFormName, GetFormSummary, GetFormOverview, GetCurrentConfiguration, IsConfigured, GetHelpContent, HandleSave`
- 直接依赖：`backend/cmd/installer/files`, `backend/cmd/installer/processor`, `backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/terminal`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/base_controls.go`

- 文件类型：`.go`
- 大小：`1033` 字节
- 文本行数：`44`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`NewBooleanInput, NewTextInput`
- 直接依赖：`backend/cmd/installer/loader`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/base_screen.go`

- 文件类型：`.go`
- 大小：`27478` 字节
- 文本行数：`979`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`BaseListOption, FilterValue, BaseListDelegate, NewBaseListDelegate, SetColors, SetWidth, Height, Spacing, Update, Render, BaseListHelper, CreateList`
- 直接依赖：`backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/logger`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`
- 备注：长文件（979 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/cmd/installer/wizard/models/docker_form.go`

- 文件类型：`.go`
- 大小：`14387` 字节
- 文本行数：`446`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`DockerFormModel, NewDockerFormModel, BuildForm, GetFormTitle, GetFormDescription, GetFormName, GetFormSummary, GetFormOverview, GetCurrentConfiguration, IsConfigured, GetHelpContent, HandleSave`
- 直接依赖：`backend/cmd/installer/loader`, `backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/logger`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/embedder_form.go`

- 文件类型：`.go`
- 大小：`21599` 字节
- 文本行数：`638`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`EmbeddingProviderInfo, EmbedderFormModel, NewEmbedderFormModel, BuildForm, GetFormTitle, GetFormDescription, GetFormName, GetFormSummary, GetFormOverview, GetCurrentConfiguration, IsConfigured, GetHelpContent`
- 直接依赖：`backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/logger`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/eula.go`

- 文件类型：`.go`
- 大小：`6957` 字节
- 文本行数：`272`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`EULAModel, NewEULAModel, Init, Update, View, GetScrollInfo, EULALoadedMsg, GetFormTitle, GetFormDescription, GetFormName, GetFormOverview, GetCurrentConfiguration`
- 直接依赖：`backend/cmd/installer/files`, `backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/logger`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/graphiti_form.go`

- 文件类型：`.go`
- 大小：`13683` 字节
- 文本行数：`402`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`GraphitiFormModel, NewGraphitiFormModel, BuildForm, GetFormTitle, GetFormDescription, GetFormName, GetFormSummary, GetFormOverview, GetCurrentConfiguration, IsConfigured, GetHelpContent, HandleSave`
- 直接依赖：`backend/cmd/installer/loader`, `backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/logger`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/helpers/calc_context.go`

- 文件类型：`.go`
- 大小：`12137` 字节
- 文本行数：`308`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`helpers`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`ContextEstimate, ConfigBoundaries, NewConfigBoundaries, CalculateContextEstimate`
- 直接依赖：`backend/pkg/csum`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/models/summarizer_form.go`

## `backend/cmd/installer/wizard/models/helpers/calc_context_test.go`

- 文件类型：`.go`
- 大小：`18337` 字节
- 文本行数：`508`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`helpers`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`TestConfigBoundaries, TestMonotonicBehavior, TestBooleanParametersLogic, TestBoundariesUsage, TestCalculateContextEstimate`
- 直接依赖：`backend/pkg/csum`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/models/summarizer_form.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/cmd/installer/wizard/models/langfuse_form.go`

- 文件类型：`.go`
- 大小：`16203` 字节
- 文本行数：`457`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`LangfuseFormModel, NewLangfuseFormModel, BuildForm, GetFormTitle, GetFormDescription, GetFormName, GetFormSummary, GetFormOverview, GetCurrentConfiguration, IsConfigured, GetHelpContent, HandleSave`
- 直接依赖：`backend/cmd/installer/loader`, `backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/logger`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/list_screen.go`

- 文件类型：`.go`
- 大小：`10453` 字节
- 文本行数：`370`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`ListScreenHandler, ListItem, ListScreen, NewListScreen, GetFormOverview, GetCurrentConfiguration, IsConfigured, GetFormHotKeys, Init, Update, View, GetScreen`
- 直接依赖：`backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/llm_provider_form.go`

- 文件类型：`.go`
- 大小：`27958` 字节
- 文本行数：`797`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`LLMProviderFormModel, NewLLMProviderFormModel, BuildForm, GetFormTitle, GetFormDescription, GetFormName, GetFormSummary, GetFormOverview, GetCurrentConfiguration, IsConfigured, GetHelpContent, HandleSave`
- 直接依赖：`backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/logger`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/llm_providers.go`

- 文件类型：`.go`
- 大小：`2855` 字节
- 文本行数：`104`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`LLMProvidersHandler, NewLLMProvidersHandler, LoadItems, HandleSelection, GetFormTitle, GetFormDescription, GetFormName, GetOverview, ShowConfiguredStatus, LLMProvidersModel, NewLLMProvidersModel`
- 直接依赖：`backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/main_menu.go`

- 文件类型：`.go`
- 大小：`4427` 字节
- 文本行数：`157`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`MainMenuHandler, NewMainMenuHandler, LoadItems, HandleSelection, GetOverview, ShowConfiguredStatus, GetFormTitle, GetFormDescription, GetFormName, MainMenuModel, NewMainMenuModel`
- 直接依赖：`backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/maintenance.go`

- 文件类型：`.go`
- 大小：`4892` 字节
- 文本行数：`182`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`MaintenanceHandler, NewMaintenanceHandler, LoadItems, HandleSelection, GetFormTitle, GetFormDescription, GetFormName, GetOverview, ShowConfiguredStatus, MaintenanceModel, NewMaintenanceModel`
- 直接依赖：`backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/mock_form.go`

- 文件类型：`.go`
- 大小：`4183` 字节
- 文本行数：`150`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`MockFormModel, NewMockFormModel, BuildForm, GetFormTitle, GetFormDescription, GetFormName, GetFormSummary, GetFormOverview, GetCurrentConfiguration, IsConfigured, GetHelpContent, HandleSave`
- 直接依赖：`backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/monitoring.go`

- 文件类型：`.go`
- 大小：`2546` 字节
- 文本行数：`96`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`MonitoringHandler, NewMonitoringHandler, LoadItems, HandleSelection, GetFormTitle, GetFormDescription, GetFormName, GetOverview, ShowConfiguredStatus, MonitoringModel, NewMonitoringModel`
- 直接依赖：`backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/observability_form.go`

- 文件类型：`.go`
- 大小：`14400` 字节
- 文本行数：`390`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`ObservabilityFormModel, NewObservabilityFormModel, BuildForm, GetFormTitle, GetFormDescription, GetFormName, GetFormSummary, GetFormOverview, GetCurrentConfiguration, IsConfigured, GetHelpContent, HandleSave`
- 直接依赖：`backend/cmd/installer/loader`, `backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/logger`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/processor_operation_form.go`

- 文件类型：`.go`
- 大小：`24015` 字节
- 文本行数：`680`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`ProcessorOperationFormModel, NewProcessorOperationFormModel, BuildForm, GetFormTitle, GetFormDescription, GetFormName, GetFormSummary, GetFormOverview, GetCurrentConfiguration, IsConfigured, GetHelpContent, HandleSave`
- 直接依赖：`backend/cmd/installer/processor`, `backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/terminal`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/reset_password.go`

- 文件类型：`.go`
- 大小：`9080` 字节
- 文本行数：`318`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`ResetPasswordHandler, NewResetPasswordHandler, BuildForm, GetFormSummary, GetHelpContent, HandleSave, HandleReset, OnFieldChanged, GetFormFields, SetFormFields, ResetPasswordModel, NewResetPasswordModel`
- 直接依赖：`backend/cmd/installer/loader`, `backend/cmd/installer/processor`, `backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`, `backend/pkg/server/models`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/scraper_form.go`

- 文件类型：`.go`
- 大小：`16181` 字节
- 文本行数：`502`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`ScraperFormModel, NewScraperFormModel, BuildForm, GetFormTitle, GetFormDescription, GetFormName, GetFormSummary, GetFormOverview, GetCurrentConfiguration, IsConfigured, GetHelpContent, HandleSave`
- 直接依赖：`backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/logger`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/search_engines_form.go`

- 文件类型：`.go`
- 大小：`16389` 字节
- 文本行数：`510`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`SearchEnginesFormModel, NewSearchEnginesFormModel, BuildForm, GetFormTitle, GetFormDescription, GetFormName, GetFormSummary, GetFormOverview, GetCurrentConfiguration, IsConfigured, GetHelpContent, HandleSave`
- 直接依赖：`backend/cmd/installer/loader`, `backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/logger`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/server_settings_form.go`

- 文件类型：`.go`
- 大小：`18852` 字节
- 文本行数：`517`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`ServerSettingsFormModel, NewServerSettingsFormModel, BuildForm, GetFormTitle, GetFormDescription, GetFormName, GetFormSummary, GetFormOverview, GetCurrentConfiguration, IsConfigured, GetHelpContent, HandleSave`
- 直接依赖：`backend/cmd/installer/loader`, `backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/logger`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/summarizer.go`

- 文件类型：`.go`
- 大小：`2527` 字节
- 文本行数：`96`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`SummarizerHandler, NewSummarizerHandler, LoadItems, HandleSelection, GetFormTitle, GetFormDescription, GetFormName, GetOverview, ShowConfiguredStatus, SummarizerModel, NewSummarizerModel`
- 直接依赖：`backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/summarizer_form.go`

- 文件类型：`.go`
- 大小：`17631` 字节
- 文本行数：`586`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`SummarizerFormModel, NewSummarizerFormModel, BuildForm, GetFormTitle, GetFormDescription, GetFormName, GetFormSummary, GetFormOverview, GetCurrentConfiguration, IsConfigured, GetHelpContent, HandleSave`
- 直接依赖：`backend/cmd/installer/loader`, `backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/logger`, `backend/cmd/installer/wizard/models/helpers`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`, `backend/pkg/csum`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/tools.go`

- 文件类型：`.go`
- 大小：`2430` 字节
- 文本行数：`99`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`ToolsHandler, NewToolsHandler, LoadItems, HandleSelection, GetFormTitle, GetFormDescription, GetFormName, GetOverview, ShowConfiguredStatus, ToolsModel, NewToolsModel`
- 直接依赖：`backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/types.go`

- 文件类型：`.go`
- 大小：`6356` 字节
- 文本行数：`201`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`Registry, RestoreModel, ScreenID, LLMProviderID, NavigationMsg, MenuState, MenuItem, StatusInfo, GetScreen, GetArgs, CreateScreenID`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/models/welcome.go`

- 文件类型：`.go`
- 大小：`16237` 字节
- 文本行数：`477`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`models`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`WelcomeModel, NewWelcomeModel, Init, Update, View, IsReadyToContinue, HasScrollableContent, GetFormTitle, GetFormDescription, GetFormName, GetFormOverview, GetCurrentConfiguration`
- 直接依赖：`backend/cmd/installer/checker`, `backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/navigator/navigator.go`, `backend/cmd/installer/navigator/navigator_test.go`, `backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/registry/registry.go`

## `backend/cmd/installer/wizard/registry/registry.go`

- 文件类型：`.go`
- 大小：`6831` 字节
- 文本行数：`166`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`registry`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`Registry, NewRegistry, GetScreen, HandleMsg`
- 直接依赖：`backend/cmd/installer/files`, `backend/cmd/installer/processor`, `backend/cmd/installer/wizard/controller`, `backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/models`, `backend/cmd/installer/wizard/styles`, `backend/cmd/installer/wizard/window`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`

## `backend/cmd/installer/wizard/styles/styles.go`

- 文件类型：`.go`
- 大小：`8709` 字节
- 文本行数：`330`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`styles`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`Styles, New, GetRenderer, RenderStatusIcon, RenderStatusText, RenderMenuItem, RenderASCIILogo, RenderFooter`
- 直接依赖：`backend/cmd/installer/wizard/locale`, `backend/cmd/installer/wizard/logger`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/models/ai_agents_settings_form.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/base_controls.go`, `backend/cmd/installer/wizard/models/base_screen.go`, `backend/cmd/installer/wizard/models/docker_form.go`, `backend/cmd/installer/wizard/models/embedder_form.go`, `backend/cmd/installer/wizard/models/eula.go`, `backend/cmd/installer/wizard/models/graphiti_form.go`, `backend/cmd/installer/wizard/models/langfuse_form.go`, `backend/cmd/installer/wizard/models/list_screen.go`, `backend/cmd/installer/wizard/models/llm_provider_form.go` 等 28 项

## `backend/cmd/installer/wizard/terminal/key2uv.go`

- 文件类型：`.go`
- 大小：`7621` 字节
- 文本行数：`215`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`terminal`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`backend/cmd/installer/wizard/terminal/vt`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/processor.go`, `backend/cmd/installer/processor/state.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`

## `backend/cmd/installer/wizard/terminal/pty_unix.go`

- 文件类型：`.go`
- 大小：`3413` 字节
- 文本行数：`159`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`terminal`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`backend/cmd/installer/wizard/terminal/vt`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/processor.go`, `backend/cmd/installer/processor/state.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`

## `backend/cmd/installer/wizard/terminal/pty_windows.go`

- 文件类型：`.go`
- 大小：`336` 字节
- 文本行数：`19`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`terminal`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/processor.go`, `backend/cmd/installer/processor/state.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`

## `backend/cmd/installer/wizard/terminal/teacmd.go`

- 文件类型：`.go`
- 大小：`1623` 字节
- 文本行数：`81`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`terminal`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/processor.go`, `backend/cmd/installer/processor/state.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`

## `backend/cmd/installer/wizard/terminal/teacmd_test.go`

- 文件类型：`.go`
- 大小：`8119` 字节
- 文本行数：`362`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`terminal`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`TestUpdateNotifierSingleSubscriber, TestUpdateNotifierOnlyOneAcquirer, TestUpdateNotifierNewAcquireAfterRelease, TestUpdateNotifierAfterClose, TestUpdateNotifierConcurrentAccess, TestUpdateNotifierReleaseWithoutAcquirer, TestUpdateNotifierContextReuse, TestUpdateNotifierStartsWithActiveChannel, TestWaitForTerminalUpdate, TestWaitForTerminalUpdateSingleWinner`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/processor.go`, `backend/cmd/installer/processor/state.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`
- 备注：测试文件，用于验证对应模块行为。

## `backend/cmd/installer/wizard/terminal/terminal.go`

- 文件类型：`.go`
- 大小：`12956` 字节
- 文本行数：`587`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`terminal`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`Printf, TerminalUpdateMsg, TerminalOption, WithAutoScroll, WithAutoPoll, WithStyle, WithCurrentEnv, WithNoStyled, WithNoPty, Terminal, NewTerminal, Execute`
- 直接依赖：`backend/cmd/installer/wizard/logger`, `backend/cmd/installer/wizard/terminal/vt`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/processor.go`, `backend/cmd/installer/processor/state.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`
- 备注：包含 TODO，后续维护时可重点留意未完成事项。

## `backend/cmd/installer/wizard/terminal/terminal_test.go`

- 文件类型：`.go`
- 大小：`25456` 字节
- 文本行数：`1065`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`terminal`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`TestNewTerminal, TestTerminalSetSize, TestTerminalAppend, TestTerminalClear, TestExecuteEcho, TestExecuteCat, TestExecuteGrep, TestExecuteInteractiveInput, TestExecuteMultipleCommands, TestRestoreModel, TestTeaKeyToUVKey, TestExecuteConcurrency`
- 直接依赖：`backend/cmd/installer/wizard/terminal/vt`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/processor/processor.go`, `backend/cmd/installer/processor/state.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/processor_operation_form.go`
- 备注：测试文件，用于验证对应模块行为。；长文件（1065 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/cmd/installer/wizard/terminal/vt/callbacks.go`

- 文件类型：`.go`
- 大小：`2145` 字节
- 文本行数：`64`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`Callbacks`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`

## `backend/cmd/installer/wizard/terminal/vt/cc.go`

- 文件类型：`.go`
- 大小：`1748` 字节
- 文本行数：`61`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`

## `backend/cmd/installer/wizard/terminal/vt/charset.go`

- 文件类型：`.go`
- 大小：`1045` 字节
- 文本行数：`46`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`CharSet`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`

## `backend/cmd/installer/wizard/terminal/vt/csi.go`

- 文件类型：`.go`
- 大小：`1195` 字节
- 文本行数：`56`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`

## `backend/cmd/installer/wizard/terminal/vt/csi_cursor.go`

- 文件类型：`.go`
- 大小：`3169` 字节
- 文本行数：`111`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`

## `backend/cmd/installer/wizard/terminal/vt/csi_mode.go`

- 文件类型：`.go`
- 大小：`2463` 字节
- 文本行数：`107`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`

## `backend/cmd/installer/wizard/terminal/vt/csi_screen.go`

- 文件类型：`.go`
- 大小：`450` 字节
- 文本行数：`19`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`

## `backend/cmd/installer/wizard/terminal/vt/csi_sgr.go`

- 文件类型：`.go`
- 大小：`318` 字节
- 文本行数：`13`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`

## `backend/cmd/installer/wizard/terminal/vt/cursor.go`

- 文件类型：`.go`
- 大小：`414` 字节
- 文本行数：`26`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`CursorStyle, Cursor`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`

## `backend/cmd/installer/wizard/terminal/vt/dcs.go`

- 文件类型：`.go`
- 大小：`1173` 字节
- 文本行数：`36`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`

## `backend/cmd/installer/wizard/terminal/vt/esc.go`

- 文件类型：`.go`
- 大小：`765` 字节
- 文本行数：`34`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`

## `backend/cmd/installer/wizard/terminal/vt/focus.go`

- 文件类型：`.go`
- 大小：`632` 字节
- 文本行数：`30`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`Focus, Blur`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`

## `backend/cmd/installer/wizard/terminal/vt/handlers.go`

- 文件类型：`.go`
- 大小：`24657` 字节
- 文本行数：`920`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`DcsHandler, CsiHandler, OscHandler, ApcHandler, SosHandler, PmHandler, EscHandler, CcHandler, RegisterDcsHandler, RegisterCsiHandler, RegisterOscHandler, RegisterApcHandler`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`
- 备注：长文件（920 行），属于复杂度热点，阅读时建议先看对外导出和测试。；包含 TODO，后续维护时可重点留意未完成事项。

## `backend/cmd/installer/wizard/terminal/vt/key.go`

- 文件类型：`.go`
- 大小：`12492` 字节
- 文本行数：`454`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`KeyMod, KeyPressEvent, SendKey`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`
- 备注：包含 TODO，后续维护时可重点留意未完成事项。

## `backend/cmd/installer/wizard/terminal/vt/mode.go`

- 文件类型：`.go`
- 大小：`1350` 字节
- 文本行数：`34`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`

## `backend/cmd/installer/wizard/terminal/vt/mouse.go`

- 文件类型：`.go`
- 大小：`3181` 字节
- 文本行数：`116`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`MouseButton, Mouse, MouseClick, MouseRelease, MouseWheel, MouseMotion, SendMouse`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`

## `backend/cmd/installer/wizard/terminal/vt/osc.go`

- 文件类型：`.go`
- 大小：`3222` 字节
- 文本行数：`137`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`

## `backend/cmd/installer/wizard/terminal/vt/screen.go`

- 文件类型：`.go`
- 大小：`22181` 字节
- 文本行数：`807`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`Screen, NewScreen, Reset, Bounds, Touched, CellAt, SetCell, Height, Resize, Width, Clear, ClearArea`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`
- 备注：长文件（807 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/cmd/installer/wizard/terminal/vt/terminal.go`

- 文件类型：`.go`
- 大小：`9787` 字节
- 文本行数：`393`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`Logger, Terminal, NewTerminal, SetLogger, SetCallbacks, Touched, Bounds, CellAt, SetCell, WidthMethod, Draw, Height`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`

## `backend/cmd/installer/wizard/terminal/vt/terminal_test.go`

- 文件类型：`.go`
- 大小：`35750` 字节
- 文本行数：`1754`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`Printf, TestTerminal`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`
- 备注：测试文件，用于验证对应模块行为。；长文件（1754 行），属于复杂度热点，阅读时建议先看对外导出和测试。

## `backend/cmd/installer/wizard/terminal/vt/utf8.go`

- 文件类型：`.go`
- 大小：`2878` 字节
- 文本行数：`119`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`
- 备注：包含 TODO，后续维护时可重点留意未完成事项。

## `backend/cmd/installer/wizard/terminal/vt/utils.go`

- 文件类型：`.go`
- 大小：`132` 字节
- 文本行数：`9`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`vt`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`无或未解析`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/terminal/key2uv.go`, `backend/cmd/installer/wizard/terminal/pty_unix.go`, `backend/cmd/installer/wizard/terminal/terminal.go`, `backend/cmd/installer/wizard/terminal/terminal_test.go`

## `backend/cmd/installer/wizard/window/window.go`

- 文件类型：`.go`
- 大小：`2513` 字节
- 文本行数：`105`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`window`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`MinContentHeight, Window, New, SetWindowSize, SetHeaderHeight, SetFooterHeight, SetLeftSideBarWidth, SetRightSideBarWidth, GetWindowSize, GetWindowWidth, GetWindowHeight, GetContentSize`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/models/ai_agents_settings_form.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/base_controls.go`, `backend/cmd/installer/wizard/models/base_screen.go`, `backend/cmd/installer/wizard/models/docker_form.go`, `backend/cmd/installer/wizard/models/embedder_form.go`, `backend/cmd/installer/wizard/models/eula.go`, `backend/cmd/installer/wizard/models/graphiti_form.go`, `backend/cmd/installer/wizard/models/langfuse_form.go`, `backend/cmd/installer/wizard/models/list_screen.go`, `backend/cmd/installer/wizard/models/llm_provider_form.go` 等 28 项

## `backend/cmd/installer/wizard/window/window_test.go`

- 文件类型：`.go`
- 大小：`9282` 字节
- 文本行数：`344`
- 所属分组：`backend/cmd/installer`
- 所属包/模块：`window`
- 推断作用：后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。
- 生成文件：`否`
- 关键导出/符号：`TestNew, TestSetWindowSize, TestSetHeaderHeight, TestSetFooterHeight, TestSetLeftSideBarWidth, TestSetRightSideBarWidth, TestGetContentSizeWithAllMargins, TestGetContentWidth, TestGetContentHeight, TestIsShowHeaderTrue, TestIsShowHeaderFalse, TestIsShowHeaderBoundary`
- 直接依赖：`无或未解析`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/installer/wizard/app.go`, `backend/cmd/installer/wizard/models/ai_agents_settings_form.go`, `backend/cmd/installer/wizard/models/apply_changes.go`, `backend/cmd/installer/wizard/models/base_controls.go`, `backend/cmd/installer/wizard/models/base_screen.go`, `backend/cmd/installer/wizard/models/docker_form.go`, `backend/cmd/installer/wizard/models/embedder_form.go`, `backend/cmd/installer/wizard/models/eula.go`, `backend/cmd/installer/wizard/models/graphiti_form.go`, `backend/cmd/installer/wizard/models/langfuse_form.go`, `backend/cmd/installer/wizard/models/list_screen.go`, `backend/cmd/installer/wizard/models/llm_provider_form.go` 等 28 项
- 备注：测试文件，用于验证对应模块行为。
