# 项目审查与使用文档

## 说明

本目录由 `scripts/generate_project_audit.py` 根据当前工作区代码自动生成，用于快速理解 PentAGI 的整体设计、文件职责与依赖关系。

以下结论基于当前工作树，未覆盖运行时动态反射、数据库内容驱动逻辑或 Docker 容器内部的二次调用链。

## 仓库规模

- 文件总数：`1174`
- 文本文件：`1140`
- 生成产物：`121`

### 主要目录

- `backend/pkg/observability`：`136` 个文件
- `frontend/src/components`：`133` 个文件
- `backend/cmd/installer`：`113` 个文件
- `backend/pkg/server`：`92` 个文件
- `backend/pkg/providers`：`76` 个文件
- `frontend/src/features`：`64` 个文件
- `backend/pkg/tools`：`47` 个文件
- `backend/pkg/templates`：`46` 个文件
- `backend/docs`：`35` 个文件
- `backend/pkg/database`：`35` 个文件
- `backend/migrations`：`30` 个文件
- `frontend/src/lib`：`28` 个文件
- `frontend/public/fonts`：`27` 个文件
- `backend/pkg/controller`：`26` 个文件
- `backend/sqlc`：`25` 个文件
- `root`：`20` 个文件
- `examples/configs`：`19` 个文件
- `examples/tests`：`19` 个文件
- `frontend`：`19` 个文件
- `frontend/src/pages`：`19` 个文件

### 文件类型分布

- `.go`：`547`
- `.tsx`：`181`
- `.ts`：`104`
- `.md`：`81`
- `.yml`：`62`
- `.sql`：`53`
- `.tmpl`：`41`
- `<none>`：`21`
- `.json`：`21`
- `.woff2`：`16`
- `.html`：`6`
- `.ttf`：`6`
- `.png`：`4`
- `.yaml`：`3`
- `.exe`：`3`

## 整体设计思路

### 后端

后端以 `backend/cmd/pentagi/main.go` 为主入口：先加载环境配置，再初始化数据库连接、GORM、pgvector 连接池、迁移、Docker 客户端、Provider 控制器、Flow 控制器与订阅器，最后把这些依赖交给 `backend/pkg/server/router.go` 组装成 Gin HTTP 服务。

HTTP 层采用 REST + GraphQL 并存设计：REST 资源主要落在 `backend/pkg/server/services/`，GraphQL 入口由 `GraphqlService` 承接。路由层只负责鉴权、中间件与路径分发，业务编排继续下沉到 `backend/pkg/controller/`、`backend/pkg/providers/`、`backend/pkg/docker/` 与 `backend/pkg/database/`。

AI Agent 运行路径的核心思想是把长生命周期的渗透测试 Flow 抽象成可恢复的后台编排对象：Flow 控制器管理执行状态，Provider 统一封装模型能力，Docker 层隔离工具执行，数据库与订阅层分别承担持久化和实时推送。

### 前端

前端以 `frontend/src/main.tsx` 挂载 React 根节点，再由 `frontend/src/app.tsx` 负责 Apollo、主题、用户状态、资源、模板、Provider 配置与 React Router 数据路由组合。

路由设计采用布局分层：`ProtectedRoute` 与 `PublicRoute` 负责访问控制，`AppLayout`、`MainLayout`、`FlowsLayout`、`SettingsLayout` 负责页面骨架，真正的业务页面落在 `frontend/src/pages/`。Provider 模式用于把用户、Flow、Knowledge、模板、收藏等状态注入到路由子树。

前后端的契约主要通过 GraphQL 类型与 REST 路由完成，前端 `lib`/`hooks`/`schemas` 负责把传输层能力变成更贴近页面的可组合接口。

## 关键运行流

### 服务启动流

1. `backend/cmd/pentagi/main.go` 读取配置并建立日志、观测、数据库与 pgvector 连接。
2. 同一入口初始化 Docker 客户端、Provider 控制器、订阅控制器与 Flow 控制器。
3. `controller.LoadFlows(ctx)` 恢复未完成 Flow。
4. `backend/pkg/server/router.go` 组合 Gin 路由、中间件、REST 服务与 GraphQL 服务。
5. Gin 根据配置启动 HTTP 或 HTTPS 监听。

### 前端渲染流

1. `frontend/src/main.tsx` 挂载 `<App />`。
2. `frontend/src/app.tsx` 创建浏览器路由，并把 Apollo/Theme/User 等 Provider 链挂在根布局上。
3. 路由切换后，页面级组件在 `frontend/src/pages/` 中按 URL 懒加载。
4. 页面通过 `frontend/src/lib/apollo`、GraphQL types、REST/GraphQL hooks 与后端通信。

### 典型请求流

浏览器页面 -> React Router 页面组件 -> Apollo/HTTP 客户端 -> `backend/pkg/server/router.go` 路由 -> `backend/pkg/server/services/*` 处理器 -> `backend/pkg/controller/*` 或 `backend/pkg/database/*` -> Provider/Docker/数据库/订阅器。

## 复杂度热点

- `build/linux-amd64/pentagi`：约 `583129` 行
- `build/linux-amd64/ftester`：约 `528373` 行
- `build/linux-amd64/etester`：约 `355739` 行
- `build/linux-amd64/ctester`：约 `321153` 行
- `observability/jaeger/bin/jaeger-clickhouse-linux-amd64`：约 `232139` 行
- `observability/jaeger/bin/jaeger-clickhouse-linux-arm64`：约 `195918` 行
- `backend/pkg/graph/generated.go`：约 `45737` 行
- `observability/grafana/dashboards/server/node_exporter_full.json`：约 `13903` 行
- `frontend/pnpm-lock.yaml`：约 `12327` 行
- `backend/fern/langfuse/openapi.yml`：约 `10744` 行
- `backend/pkg/server/docs/docs.go`：约 `10501` 行
- `backend/pkg/server/docs/swagger.json`：约 `10476` 行

## 依赖中心文件

- `frontend/src/lib/utils.ts`：被 `90` 个文件直接依赖
- `frontend/src/graphql/types.ts`：被 `59` 个文件直接依赖
- `frontend/src/components/ui/button.tsx`：被 `45` 个文件直接依赖
- `frontend/src/components/ui/tooltip.tsx`：被 `26` 个文件直接依赖
- `frontend/src/components/ui/form.tsx`：被 `21` 个文件直接依赖
- `frontend/src/components/ui/input-group.tsx`：被 `18` 个文件直接依赖
- `frontend/src/lib/utils/format.ts`：被 `18` 个文件直接依赖
- `frontend/src/components/shared/confirmation-dialog.tsx`：被 `17` 个文件直接依赖
- `frontend/src/lib/log.ts`：被 `16` 个文件直接依赖
- `frontend/src/components/shared/file-manager/file-manager-types.ts`：被 `15` 个文件直接依赖
- `frontend/src/components/shared/file-manager/index.ts`：被 `15` 个文件直接依赖
- `frontend/src/components/ui/dropdown-menu.tsx`：被 `15` 个文件直接依赖

## 使用建议

1. 先读本目录下的 `README.md` 与 `relationships.md`，建立模块边界感。
2. 后端调试从 `backend/cmd/pentagi/main.go`、`backend/pkg/server/router.go` 和具体 `services/` 开始。
3. 前端调试从 `frontend/src/app.tsx`、对应 `pages/` 页面和依赖的 `providers/`、`lib/` 开始。
4. 全量文件说明请查看 `catalog/` 目录；机器可消费关系图请看 `relationships.json`。

## 审查观察

- 当前工作区存在未提交改动，因此本文档反映的是当前修改态，而不是某个历史提交的只读快照。
- 后端存在多处大体量生成文件与超长服务/配置文件，后续若继续扩展，建议逐步收敛到更小的垂直模块。
- 前端 `settings`、`file-manager`、`data-table` 等区域文件明显偏长，属于 UI/状态逻辑进一步拆分的优先候选。
