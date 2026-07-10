# 使用文档

## 项目定位

PentAGI 是一个以 AI Agent 为核心的自动化安全测试平台。它把一次渗透测试流程拆成多类代理与工具执行链，并通过数据库、向量存储、Docker 沙箱和前端工作台把这些能力组合起来。

## 运行形态

- 后端：Go 服务，提供 REST、GraphQL、认证、Flow 编排、Provider 接入与工具执行能力。
- 前端：React + TypeScript 单页应用，负责 Flow 管理、Provider 配置、资源管理和实时状态展示。
- 数据层：PostgreSQL + pgvector；可选 Neo4j、Langfuse 与观测栈。
- 执行层：Docker 沙箱运行安全工具与部分代理任务。

## 环境准备

至少准备以下依赖：

- Go 1.25.x
- Node.js + pnpm
- Docker / Docker Compose
- PostgreSQL（需可用 pgvector）
- 至少一个可用的大模型 Provider Key

复制环境文件：

```bash
cp .env.example .env
```

然后至少补齐数据库连接和一个 Provider 的配置。

## 推荐启动方式

### 方式一：Docker Compose 启动整套栈

在仓库根目录执行：

```bash
docker compose up -d
```

如果需要可观测性或扩展组件：

```bash
docker compose -f docker-compose.yml -f docker-compose-observability.yml up -d
docker compose -f docker-compose.yml -f docker-compose-langfuse.yml up -d
docker compose -f docker-compose.yml -f docker-compose-graphiti.yml up -d
```

默认完整栈地址通常为 `https://localhost:8443`。

### 方式二：本地分别运行前后端

#### 后端

```bash
cd backend
go mod download
go build -trimpath -o pentagi ./cmd/pentagi
go test ./...
```

直接运行主程序：

```bash
go run ./cmd/pentagi
```

#### 前端

```bash
cd frontend
pnpm install
pnpm run dev
```

前端开发服务器默认运行在 `http://localhost:8000`。

## 常用开发命令

### 后端

```bash
go test ./...
go test ./pkg/foo/... -v -run TestName
golangci-lint run --timeout=5m
```

### 前端

```bash
pnpm run build
pnpm run lint
pnpm run lint:fix
pnpm run prettier
pnpm run prettier:fix
pnpm run test
pnpm run test:coverage
```

## 代码生成入口

以下场景需要重新生成代码：

- 修改 `backend/pkg/graph/schema.graphqls` 后：

```bash
cd backend
go run github.com/99designs/gqlgen --config ./gqlgen/gqlgen.yml
```

- 修改 REST Swagger 注解后：

```bash
cd backend
swag init -g ../../pkg/server/router.go -o pkg/server/docs/ --parseDependency --parseInternal --parseDepth 2 -d cmd/pentagi
```

- 修改 `frontend/src/graphql/*.graphql` 后：

```bash
cd frontend
pnpm run graphql:generate
```

## 主要业务使用路径

1. 登录系统并进入 Dashboard。
2. 在 Flows 页面创建一次新的安全测试 Flow。
3. 后端调度 Researcher / Developer / Executor 等代理，并把状态写入数据库。
4. 前端通过 GraphQL / REST 拉取 Flow、任务、文件、日志与截图信息。
5. 如需管理模型能力，在 Settings 中配置 Provider、Prompt 和 API Token。

## 排障阅读顺序

- 服务启动失败：先看 `backend/cmd/pentagi/main.go`、`.env`、数据库连接和 Docker 配置。
- API 路由问题：先看 `backend/pkg/server/router.go`，再看对应 `backend/pkg/server/services/*.go`。
- Flow 编排异常：重点看 `backend/pkg/controller/`、`backend/pkg/providers/`、`backend/pkg/docker/`。
- 前端页面问题：从 `frontend/src/app.tsx` 找到对应页面，再追 `pages/ -> features/ -> components/ -> providers/`。
