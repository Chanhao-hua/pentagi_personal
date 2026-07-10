# `backend/pkg/docker` 文件清单

本组共 `1` 个文件。

## `backend/pkg/docker/client.go`

- 文件类型：`.go`
- 大小：`26073` 字节
- 文本行数：`865`
- 所属分组：`backend/pkg/docker`
- 所属包/模块：`docker`
- 推断作用：Docker 沙箱执行层文件，负责容器生命周期与命令执行隔离。
- 生成文件：`否`
- 关键导出/符号：`WorkFolderPathInContainer, BaseContainerPortsNumber, DockerClient, GetPrimaryContainerPorts, NewDockerClient, RunContainer, StopContainer, RemoveContainer, Cleanup, IsContainerRunning, GetDefaultImage, ContainerExecCreate`
- 直接依赖：`backend/pkg/config`, `backend/pkg/database`, `backend/pkg/queue`
- 被这些文件直接引用（按 Go 包级 import 统计）：`backend/cmd/ftester/main.go`, `backend/cmd/ftester/worker/executor.go`, `backend/cmd/ftester/worker/tester.go`, `backend/cmd/pentagi/main.go`, `backend/pkg/controller/flow.go`, `backend/pkg/controller/flows.go`, `backend/pkg/flowfiles/files.go`, `backend/pkg/providers/assistant.go`, `backend/pkg/providers/handlers.go`, `backend/pkg/providers/helpers.go`, `backend/pkg/providers/provider.go`, `backend/pkg/providers/providers.go` 等 18 项
- 备注：长文件（865 行），属于复杂度热点，阅读时建议先看对外导出和测试。；包含 TODO，后续维护时可重点留意未完成事项。
