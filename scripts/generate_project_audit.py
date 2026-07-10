#!/usr/bin/env python3
"""Generate architecture, file catalog, and dependency docs for the repository.

The output is written to docs/project-audit/.
"""

from __future__ import annotations

import json
import os
import re
import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = REPO_ROOT / "docs" / "project-audit"
CATALOG_ROOT = DOCS_ROOT / "catalog"
RELATIONSHIPS_JSON = DOCS_ROOT / "relationships.json"

GO_MODULE_ROOT = REPO_ROOT / "backend"
GO_MODULE_NAME = "pentagi"
FRONTEND_SRC_ROOT = REPO_ROOT / "frontend" / "src"

SKIP_DIRS = {
    ".git",
    "node_modules",
    ".pnpm-store",
    "dist",
    "coverage",
    ".turbo",
    ".next",
    ".idea",
    "__pycache__",
}

TEXT_EXTENSIONS = {
    "",
    ".cjs",
    ".conf",
    ".css",
    ".csv",
    ".env",
    ".example",
    ".go",
    ".graphql",
    ".graphqls",
    ".html",
    ".js",
    ".json",
    ".md",
    ".mjs",
    ".ps1",
    ".py",
    ".scss",
    ".sh",
    ".sql",
    ".svg",
    ".tmpl",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}

KNOWN_BINARY_EXTENSIONS = {
    ".dll",
    ".exe",
    ".gif",
    ".gz",
    ".ico",
    ".jpeg",
    ".jpg",
    ".otf",
    ".pdf",
    ".png",
    ".so",
    ".tar",
    ".ttf",
    ".woff",
    ".woff2",
    ".zip",
}

GO_IMPORT_RE = re.compile(r'import\s*(\((?P<block>.*?)\)|(?P<single>"[^"]+"))', re.S)
GO_SYMBOL_RE = re.compile(
    r"^(?:func\s+(?:\([^)]+\)\s*)?(?P<func>[A-Z][A-Za-z0-9_]*)|type\s+(?P<type>[A-Z][A-Za-z0-9_]*)\s+|const\s+(?P<const>[A-Z][A-Za-z0-9_]*)\s*=|var\s+(?P<var>[A-Z][A-Za-z0-9_]*)\s*=)",
    re.M,
)
TS_IMPORT_RE = re.compile(
    r'(?:import|export)\s+(?:[^"\']+?\s+from\s+)?["\'](?P<spec>[^"\']+)["\']',
    re.M,
)
TS_DYNAMIC_IMPORT_RE = re.compile(r'import\(\s*["\'](?P<spec>[^"\']+)["\']\s*\)')
TS_SYMBOL_RE = re.compile(
    r"^export\s+(?:default\s+)?(?:async\s+)?(?:function|class|const|let|var|type|interface|enum)\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)",
    re.M,
)


@dataclass
class FileInfo:
    rel_path: str
    abs_path: Path
    ext: str
    size: int
    is_text: bool
    line_count: int | None = None
    group: str = ""
    role: str = ""
    generated: bool = False
    symbols: list[str] = field(default_factory=list)
    deps: list[str] = field(default_factory=list)
    dep_kinds: dict[str, str] = field(default_factory=dict)
    package_name: str | None = None
    notes: list[str] = field(default_factory=list)


def main() -> None:
    files = scan_files()
    reverse_deps = build_reverse_deps(files)
    group_map = build_group_map(files)

    if DOCS_ROOT.exists():
        shutil.rmtree(DOCS_ROOT)
    DOCS_ROOT.mkdir(parents=True, exist_ok=True)
    CATALOG_ROOT.mkdir(parents=True, exist_ok=True)

    write_overview(files, reverse_deps, group_map)
    write_getting_started()
    write_relationships(files, reverse_deps)
    write_catalog(files, reverse_deps, group_map)
    write_index(files, group_map)
    write_json(files, reverse_deps)

    print(f"Generated project audit at {DOCS_ROOT}")


def scan_files() -> list[FileInfo]:
    file_infos: list[FileInfo] = []

    for path in sorted(REPO_ROOT.rglob("*")):
        if not path.is_file():
            continue

        rel_path = path.relative_to(REPO_ROOT).as_posix()
        if should_skip(path):
            continue
        if rel_path.startswith("docs/project-audit/"):
            continue

        ext = path.suffix.lower()
        is_text = detect_text_file(path, ext)
        text = read_text(path) if is_text else None
        line_count = text.count("\n") + 1 if text else None

        info = FileInfo(
            rel_path=rel_path,
            abs_path=path,
            ext=ext,
            size=path.stat().st_size,
            is_text=is_text,
            line_count=line_count,
        )
        info.group = determine_group(rel_path)
        info.generated = infer_generated(rel_path, text)
        info.package_name = infer_package_name(rel_path, text)
        info.symbols = extract_symbols(rel_path, text)
        deps, dep_kinds = extract_dependencies(rel_path, text)
        info.deps = deps
        info.dep_kinds = dep_kinds
        info.role = infer_role(rel_path, text, info)
        info.notes = build_notes(rel_path, info, text)
        file_infos.append(info)

    return file_infos


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    return bool(parts & SKIP_DIRS)


def detect_text_file(path: Path, ext: str) -> bool:
    if ext in KNOWN_BINARY_EXTENSIONS:
        return False
    if ext in TEXT_EXTENSIONS:
        return True

    try:
        chunk = path.read_bytes()[:2048]
    except OSError:
        return False

    if b"\x00" in chunk:
        return False
    if not chunk:
        return True

    control_bytes = sum(1 for byte in chunk if byte < 9 or 13 < byte < 32)
    if control_bytes / len(chunk) > 0.15:
        return False
    return True


def read_text(path: Path) -> str | None:
    for encoding in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
        except OSError:
            return None
    return None


def determine_group(rel_path: str) -> str:
    parts = rel_path.split("/")
    if len(parts) == 1:
        return "root"

    if parts[0] == "backend":
        if len(parts) >= 3 and parts[1] in {"cmd", "pkg"} and "." not in parts[2]:
            return "/".join(parts[:3])
        if parts[1] in {"cmd", "pkg"}:
            return "/".join(parts[:2])
        if len(parts) >= 2 and "." not in parts[1]:
            return "/".join(parts[:2])
        return "backend"

    if parts[0] == "frontend":
        if len(parts) >= 3 and parts[1] in {"src", "public"} and "." not in parts[2]:
            return "/".join(parts[:3])
        if parts[1] in {"src", "public"}:
            return "/".join(parts[:2])
        if len(parts) >= 2 and "." not in parts[1]:
            return "/".join(parts[:2])
        return "frontend"

    if len(parts) >= 2 and "." not in parts[1]:
        return "/".join(parts[:2])
    return parts[0]


def infer_generated(rel_path: str, text: str | None) -> bool:
    generated_names = {
        "backend/pkg/graph/generated.go",
        "backend/pkg/server/docs/docs.go",
        "backend/pkg/server/docs/swagger.json",
        "backend/pkg/server/docs/swagger.yaml",
        "frontend/src/graphql/types.ts",
        "frontend/pnpm-lock.yaml",
        "backend/go.sum",
    }
    if rel_path in generated_names:
        return True
    if text:
        head = "\n".join(text.splitlines()[:8]).lower()
        if "code generated" in head or "do not edit" in head:
            return True
    return False


def infer_package_name(rel_path: str, text: str | None) -> str | None:
    if not text:
        return None
    if rel_path.endswith(".go"):
        match = re.search(r"^package\s+([A-Za-z0-9_]+)", text, re.M)
        if match:
            return match.group(1)
    if rel_path.endswith((".ts", ".tsx", ".js", ".jsx")):
        return rel_path.replace("/", ".")
    return None


def extract_symbols(rel_path: str, text: str | None) -> list[str]:
    if not text:
        return []
    if rel_path.endswith(".go"):
        symbols: list[str] = []
        for match in GO_SYMBOL_RE.finditer(text):
            for key in ("func", "type", "const", "var"):
                value = match.group(key)
                if value:
                    symbols.append(value)
                    break
        return symbols[:12]

    if rel_path.endswith((".ts", ".tsx", ".js", ".jsx")):
        return [m.group("name") for m in TS_SYMBOL_RE.finditer(text)][:12]

    return []


def extract_dependencies(rel_path: str, text: str | None) -> tuple[list[str], dict[str, str]]:
    if not text:
        return [], {}

    deps: list[str] = []
    dep_kinds: dict[str, str] = {}

    if rel_path.endswith(".go"):
        for match in GO_IMPORT_RE.finditer(text):
            raw_block = match.group("block") or match.group("single") or ""
            for spec in re.findall(r'"([^"]+)"', raw_block):
                resolved = resolve_go_import(spec)
                if resolved:
                    deps.append(resolved)
                    dep_kinds[resolved] = "go-package"
        return dedupe(deps), dep_kinds

    if rel_path.endswith((".ts", ".tsx", ".js", ".jsx")):
        specs = [m.group("spec") for m in TS_IMPORT_RE.finditer(text)]
        specs.extend(m.group("spec") for m in TS_DYNAMIC_IMPORT_RE.finditer(text))
        for spec in specs:
            resolved = resolve_ts_import(rel_path, spec)
            if resolved:
                deps.append(resolved)
                dep_kinds[resolved] = "file"
        return dedupe(deps), dep_kinds

    return [], {}


def resolve_go_import(spec: str) -> str | None:
    if not spec.startswith(f"{GO_MODULE_NAME}/"):
        return None
    target = spec.removeprefix(f"{GO_MODULE_NAME}/")
    return f"backend/{target}"


def resolve_ts_import(rel_path: str, spec: str) -> str | None:
    if spec.startswith("@/"):
        base = FRONTEND_SRC_ROOT / spec[2:]
    elif spec.startswith("."):
        base = (REPO_ROOT / rel_path).parent / spec
    else:
        return None

    resolved = resolve_module_path(base)
    if resolved is None:
        return None
    try:
        return resolved.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return None


def resolve_module_path(base: Path) -> Path | None:
    candidates: list[Path] = []
    if base.suffix:
        candidates.append(base)
    else:
        candidates.append(base)
        for ext in (".ts", ".tsx", ".js", ".jsx", ".json"):
            candidates.append(base.with_suffix(ext))
        for name in ("index.ts", "index.tsx", "index.js", "index.jsx"):
            candidates.append(base / name)

    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            return candidate.resolve()
    return None


def infer_role(rel_path: str, text: str | None, info: FileInfo) -> str:
    parts = rel_path.split("/")
    filename = parts[-1]
    stem = Path(filename).stem

    path_rules: list[tuple[str, str]] = [
        ("backend/cmd/pentagi/main.go", "后端主程序入口，负责装配配置、数据库、Docker 运行时、Provider 控制器、Flow 控制器和 HTTP 服务器。"),
        ("backend/pkg/server/router.go", "Gin 路由总装配文件，绑定 REST、GraphQL、认证、中间件和前端静态资源回退逻辑。"),
        ("frontend/src/main.tsx", "前端浏览器入口，挂载 React 根节点并引入全局样式。"),
        ("frontend/src/app.tsx", "前端路由与全局 Provider 组合入口，定义页面布局和访问控制。"),
    ]
    for exact, description in path_rules:
        if rel_path == exact:
            return description

    if rel_path.startswith("backend/cmd/"):
        return "后端命令行或测试辅助可执行入口，用于启动服务或验证子系统。"
    if rel_path.startswith("backend/pkg/server/services/"):
        return "REST 服务处理器文件，承接路由层请求并调用 ORM、控制器或 Provider 完成具体业务。"
    if rel_path.startswith("backend/pkg/server/auth/"):
        return "认证与鉴权支持文件，负责 Token、会话或用户身份校验。"
    if rel_path.startswith("backend/pkg/server/oauth/"):
        return "第三方 OAuth 登录适配文件，封装 Google/GitHub 等登录流程。"
    if rel_path.startswith("backend/pkg/server/"):
        return "后端 HTTP 服务层文件，负责中间件、路由、模型绑定或服务支撑。"
    if rel_path.startswith("backend/pkg/controller/"):
        return "业务编排控制器文件，负责把数据库、Provider、Docker 执行器和订阅系统串成完整流程。"
    if rel_path.startswith("backend/pkg/providers/"):
        return "LLM 或嵌入模型 Provider 适配文件，负责统一封装外部 AI 能力。"
    if rel_path.startswith("backend/pkg/database/knowledge/"):
        return "知识库数据访问层文件，连接数据库记录、向量索引和订阅更新。"
    if rel_path.startswith("backend/pkg/database/"):
        return "数据库层文件，包含 SQLC 查询、GORM 模型、迁移辅助或持久化工具。"
    if rel_path.startswith("backend/pkg/graph/"):
        return "GraphQL 相关文件，包含 schema、resolver、订阅和生成代码边界。"
    if rel_path.startswith("backend/pkg/docker/"):
        return "Docker 沙箱执行层文件，负责容器生命周期与命令执行隔离。"
    if rel_path.startswith("backend/pkg/terminal/"):
        return "终端会话与命令交互文件，用于在容器或运行时中维护交互式会话。"
    if rel_path.startswith("backend/pkg/tools/"):
        return "安全测试工具适配文件，封装外部工具的调用与结果转换。"
    if rel_path.startswith("backend/pkg/queue/"):
        return "异步任务队列文件，用于流转后台作业或事件处理。"
    if rel_path.startswith("backend/pkg/observability/"):
        return "可观测性支撑文件，负责日志、指标、Tracing 或 Langfuse 集成。"
    if rel_path.startswith("backend/pkg/config/"):
        return "后端配置加载与环境变量解析文件。"
    if rel_path.startswith("backend/migrations/"):
        return "数据库迁移文件，定义 schema 或枚举演进。"
    if rel_path.startswith("backend/sqlc/"):
        return "SQLC 配置或生成相关文件，用于声明 SQL 到 Go 的映射。"
    if rel_path.startswith("frontend/src/pages/"):
        return "路由级页面文件，直接对应浏览器 URL 或页面组合逻辑。"
    if rel_path.startswith("frontend/src/components/layouts/"):
        return "前端布局壳层文件，组织侧边栏、标题区和内容容器。"
    if rel_path.startswith("frontend/src/components/ui/"):
        return "可复用 UI 基础组件文件，服务于多页面共享的展示和交互能力。"
    if rel_path.startswith("frontend/src/components/routes/"):
        return "前端路由守卫或导航控制文件，处理公开/受保护页面切换。"
    if rel_path.startswith("frontend/src/components/shared/"):
        return "跨页面共享的前端业务组件文件。"
    if rel_path.startswith("frontend/src/features/"):
        return "按业务场景组织的前端功能模块文件。"
    if rel_path.startswith("frontend/src/providers/"):
        return "React Context Provider 文件，向子树分发全局状态或远程数据。"
    if rel_path.startswith("frontend/src/hooks/"):
        return "前端自定义 Hook 文件，抽出复用状态和副作用逻辑。"
    if rel_path.startswith("frontend/src/lib/"):
        return "前端基础设施文件，负责 Apollo、HTTP、路由标题或报表等通用支撑。"
    if rel_path.startswith("frontend/src/graphql/"):
        return "GraphQL 文档或生成类型文件，连接前端与后端 Schema。"
    if rel_path.startswith("frontend/src/schemas/"):
        return "前端验证模式文件，通常封装 Zod 表单校验或数据约束。"
    if rel_path.startswith("frontend/public/"):
        return "前端静态资源文件，供浏览器直接加载。"
    if rel_path.startswith("observability/"):
        return "观测栈部署或配置文件，支撑 Grafana、Loki、Jaeger 等组件。"
    if rel_path.startswith("scripts/"):
        return "仓库自动化脚本文件，用于版本生成、镜像入口或许可证处理。"
    if rel_path.startswith("examples/"):
        return "示例配置或示例数据文件，用于演示扩展 Provider 或部署方式。"
    if rel_path.startswith(".github/"):
        return "仓库协作与自动化元数据文件，通常承载工作流、模板或社区规范。"
    if rel_path.startswith(".vscode/"):
        return "本地开发环境配置文件，帮助统一编辑器行为。"
    if filename.startswith("docker-compose"):
        return "Docker Compose 编排文件，定义本地整套依赖和可选增强栈。"
    if filename.startswith("Dockerfile"):
        return "镜像构建文件，定义服务运行镜像或本地运行时镜像。"
    if filename in {".env", ".env.example"}:
        return "环境变量模板或本地配置文件，驱动后端、前端与外部集成。"
    if filename in {"README.md", "CONTRIBUTING.md", "CLAUDE.md", "AGENTS.md"}:
        return "项目文档或协作约束文件，帮助开发者与智能代理理解仓库规则。"

    kind = "文本文件" if info.is_text else "二进制资源文件"
    return f"{kind}，当前未命中特定规则，建议结合所在目录 `{info.group}` 的上下文阅读。"


def build_notes(rel_path: str, info: FileInfo, text: str | None) -> list[str]:
    notes: list[str] = []
    if info.generated:
        notes.append("生成产物，优先修改上游 schema、注解或源码后再重新生成。")
    if rel_path.endswith("_test.go") or rel_path.endswith(".test.ts") or rel_path.endswith(".test.tsx"):
        notes.append("测试文件，用于验证对应模块行为。")
    if info.line_count and info.line_count > 800:
        notes.append(f"长文件（{info.line_count} 行），属于复杂度热点，阅读时建议先看对外导出和测试。")
    if text and "TODO" in text:
        notes.append("包含 TODO，后续维护时可重点留意未完成事项。")
    return notes


def build_reverse_deps(files: list[FileInfo]) -> dict[str, list[str]]:
    reverse: dict[str, list[str]] = defaultdict(list)
    for info in files:
        for dep in info.deps:
            reverse[dep].append(info.rel_path)
    for key, value in reverse.items():
        reverse[key] = sorted(set(value))
    return dict(reverse)


def build_group_map(files: list[FileInfo]) -> dict[str, list[FileInfo]]:
    groups: dict[str, list[FileInfo]] = defaultdict(list)
    for info in files:
        groups[info.group].append(info)
    for file_list in groups.values():
        file_list.sort(key=lambda item: item.rel_path)
    return dict(sorted(groups.items()))


def write_overview(files: list[FileInfo], reverse_deps: dict[str, list[str]], group_map: dict[str, list[FileInfo]]) -> None:
    text_files = [f for f in files if f.is_text]
    large_files = sorted((f for f in text_files if f.line_count), key=lambda item: item.line_count or 0, reverse=True)[:12]
    hubs = sorted(files, key=lambda item: len(reverse_deps.get(item.rel_path, [])), reverse=True)[:12]

    ext_counter = Counter(f.ext or "<none>" for f in files)
    top_groups = sorted(group_map.items(), key=lambda item: len(item[1]), reverse=True)[:20]

    content = [
        "# 项目审查与使用文档",
        "",
        "## 说明",
        "",
        "本目录由 `scripts/generate_project_audit.py` 根据当前工作区代码自动生成，用于快速理解 PentAGI 的整体设计、文件职责与依赖关系。",
        "",
        "以下结论基于当前工作树，未覆盖运行时动态反射、数据库内容驱动逻辑或 Docker 容器内部的二次调用链。",
        "",
        "## 仓库规模",
        "",
        f"- 文件总数：`{len(files)}`",
        f"- 文本文件：`{len(text_files)}`",
        f"- 生成产物：`{sum(1 for f in files if f.generated)}`",
        "",
        "### 主要目录",
        "",
    ]
    for group, members in top_groups:
        content.append(f"- `{group}`：`{len(members)}` 个文件")

    content.extend(
        [
            "",
            "### 文件类型分布",
            "",
        ]
    )
    for ext, count in ext_counter.most_common(15):
        content.append(f"- `{ext}`：`{count}`")

    content.extend(
        [
            "",
            "## 整体设计思路",
            "",
            "### 后端",
            "",
            "后端以 `backend/cmd/pentagi/main.go` 为主入口：先加载环境配置，再初始化数据库连接、GORM、pgvector 连接池、迁移、Docker 客户端、Provider 控制器、Flow 控制器与订阅器，最后把这些依赖交给 `backend/pkg/server/router.go` 组装成 Gin HTTP 服务。",
            "",
            "HTTP 层采用 REST + GraphQL 并存设计：REST 资源主要落在 `backend/pkg/server/services/`，GraphQL 入口由 `GraphqlService` 承接。路由层只负责鉴权、中间件与路径分发，业务编排继续下沉到 `backend/pkg/controller/`、`backend/pkg/providers/`、`backend/pkg/docker/` 与 `backend/pkg/database/`。",
            "",
            "AI Agent 运行路径的核心思想是把长生命周期的渗透测试 Flow 抽象成可恢复的后台编排对象：Flow 控制器管理执行状态，Provider 统一封装模型能力，Docker 层隔离工具执行，数据库与订阅层分别承担持久化和实时推送。",
            "",
            "### 前端",
            "",
            "前端以 `frontend/src/main.tsx` 挂载 React 根节点，再由 `frontend/src/app.tsx` 负责 Apollo、主题、用户状态、资源、模板、Provider 配置与 React Router 数据路由组合。",
            "",
            "路由设计采用布局分层：`ProtectedRoute` 与 `PublicRoute` 负责访问控制，`AppLayout`、`MainLayout`、`FlowsLayout`、`SettingsLayout` 负责页面骨架，真正的业务页面落在 `frontend/src/pages/`。Provider 模式用于把用户、Flow、Knowledge、模板、收藏等状态注入到路由子树。",
            "",
            "前后端的契约主要通过 GraphQL 类型与 REST 路由完成，前端 `lib`/`hooks`/`schemas` 负责把传输层能力变成更贴近页面的可组合接口。",
            "",
            "## 关键运行流",
            "",
            "### 服务启动流",
            "",
            "1. `backend/cmd/pentagi/main.go` 读取配置并建立日志、观测、数据库与 pgvector 连接。",
            "2. 同一入口初始化 Docker 客户端、Provider 控制器、订阅控制器与 Flow 控制器。",
            "3. `controller.LoadFlows(ctx)` 恢复未完成 Flow。",
            "4. `backend/pkg/server/router.go` 组合 Gin 路由、中间件、REST 服务与 GraphQL 服务。",
            "5. Gin 根据配置启动 HTTP 或 HTTPS 监听。",
            "",
            "### 前端渲染流",
            "",
            "1. `frontend/src/main.tsx` 挂载 `<App />`。",
            "2. `frontend/src/app.tsx` 创建浏览器路由，并把 Apollo/Theme/User 等 Provider 链挂在根布局上。",
            "3. 路由切换后，页面级组件在 `frontend/src/pages/` 中按 URL 懒加载。",
            "4. 页面通过 `frontend/src/lib/apollo`、GraphQL types、REST/GraphQL hooks 与后端通信。",
            "",
            "### 典型请求流",
            "",
            "浏览器页面 -> React Router 页面组件 -> Apollo/HTTP 客户端 -> `backend/pkg/server/router.go` 路由 -> `backend/pkg/server/services/*` 处理器 -> `backend/pkg/controller/*` 或 `backend/pkg/database/*` -> Provider/Docker/数据库/订阅器。",
            "",
            "## 复杂度热点",
            "",
        ]
    )
    for info in large_files:
        content.append(f"- `{info.rel_path}`：约 `{info.line_count}` 行")

    content.extend(
        [
            "",
            "## 依赖中心文件",
            "",
        ]
    )
    for info in hubs:
        incoming = len(reverse_deps.get(info.rel_path, []))
        if incoming == 0:
            continue
        content.append(f"- `{info.rel_path}`：被 `{incoming}` 个文件直接依赖")

    content.extend(
        [
            "",
            "## 使用建议",
            "",
            "1. 先读本目录下的 `README.md` 与 `relationships.md`，建立模块边界感。",
            "2. 后端调试从 `backend/cmd/pentagi/main.go`、`backend/pkg/server/router.go` 和具体 `services/` 开始。",
            "3. 前端调试从 `frontend/src/app.tsx`、对应 `pages/` 页面和依赖的 `providers/`、`lib/` 开始。",
            "4. 全量文件说明请查看 `catalog/` 目录；机器可消费关系图请看 `relationships.json`。",
            "",
            "## 审查观察",
            "",
            "- 当前工作区存在未提交改动，因此本文档反映的是当前修改态，而不是某个历史提交的只读快照。",
            "- 后端存在多处大体量生成文件与超长服务/配置文件，后续若继续扩展，建议逐步收敛到更小的垂直模块。",
            "- 前端 `settings`、`file-manager`、`data-table` 等区域文件明显偏长，属于 UI/状态逻辑进一步拆分的优先候选。",
            "",
        ]
    )

    (DOCS_ROOT / "architecture-overview.md").write_text("\n".join(content), encoding="utf-8")


def write_relationships(files: list[FileInfo], reverse_deps: dict[str, list[str]]) -> None:
    backend_edges: Counter[tuple[str, str]] = Counter()
    frontend_edges: Counter[tuple[str, str]] = Counter()
    exact_file_edges: list[tuple[str, str]] = []

    for info in files:
        for dep in info.deps:
            if info.rel_path.startswith("backend/") and dep.startswith("backend/"):
                backend_edges[(directory_of(info.rel_path), dep)] += 1
            elif info.rel_path.startswith("frontend/") and dep.startswith("frontend/"):
                frontend_edges[(directory_of(info.rel_path), directory_of(dep))] += 1
                exact_file_edges.append((info.rel_path, dep))

    backend_edges_top = backend_edges.most_common(40)
    frontend_edges_top = frontend_edges.most_common(40)

    content = [
        "# 文件与模块关系图谱",
        "",
        "## 关系口径",
        "",
        "- Go：以 `import` 产生的包级依赖为主，因此更适合读成“文件所属包 -> 目标包”的关系。",
        "- TypeScript/TSX：以具体模块导入为主，因此同时保留“文件 -> 文件”和“目录 -> 目录”的关系。",
        "- 非代码配置文件仅在文件索引中给出职责说明，不强行构造虚假的调用链。",
        "",
        "## 后端主启动链",
        "",
        "```mermaid",
        "graph TD",
        '    A["backend/cmd/pentagi/main.go"] --> B["backend/pkg/config"]',
        '    A --> C["backend/pkg/database"]',
        '    A --> D["backend/pkg/docker"]',
        '    A --> E["backend/pkg/providers"]',
        '    A --> F["backend/pkg/controller"]',
        '    A --> G["backend/pkg/graph/subscriptions"]',
        '    A --> H["backend/pkg/server/router.go"]',
        '    H --> I["backend/pkg/server/services"]',
        '    I --> C',
        '    I --> F',
        '    I --> E',
        '    F --> D',
        '    F --> E',
        "```",
        "",
        "## 前端主渲染链",
        "",
        "```mermaid",
        "graph TD",
        '    A["frontend/src/main.tsx"] --> B["frontend/src/app.tsx"]',
        '    B --> C["frontend/src/providers/*"]',
        '    B --> D["frontend/src/components/layouts/*"]',
        '    B --> E["frontend/src/pages/*"]',
        '    E --> F["frontend/src/lib/*"]',
        '    E --> G["frontend/src/hooks/*"]',
        '    E --> H["frontend/src/components/shared/*"]',
        "```",
        "",
        "## 后端包级高频依赖",
        "",
        "| 源目录 | 目标目录 | 直接 import 次数 |",
        "|---|---|---:|",
    ]
    for (source, target), count in backend_edges_top:
        content.append(f"| `{source}` | `{target}` | {count} |")

    content.extend(
        [
            "",
            "## 前端目录级高频依赖",
            "",
            "| 源目录 | 目标目录 | 直接 import 次数 |",
            "|---|---|---:|",
        ]
    )
    for (source, target), count in frontend_edges_top:
        content.append(f"| `{source}` | `{target}` | {count} |")

    hubs = sorted(
        (info for info in files if info.rel_path.startswith(("backend/", "frontend/"))),
        key=lambda item: len(reverse_deps.get(item.rel_path, [])),
        reverse=True,
    )[:25]
    content.extend(
        [
            "",
            "## 最常被直接引用的文件",
            "",
            "| 文件 | 入边数量 | 典型角色 |",
            "|---|---:|---|",
        ]
    )
    for info in hubs:
        incoming = len(reverse_deps.get(info.rel_path, []))
        if incoming == 0:
            continue
        content.append(f"| `{info.rel_path}` | {incoming} | {escape_pipes(info.role)} |")

    content.extend(
        [
            "",
            "## 前端文件到文件示例关系",
            "",
            "以下仅展示前 120 条解析到的前端具体文件引用，完整图请查阅 `relationships.json`。",
            "",
            "| 源文件 | 目标文件 |",
            "|---|---|",
        ]
    )
    for source, target in exact_file_edges[:120]:
        content.append(f"| `{source}` | `{target}` |")

    (DOCS_ROOT / "relationships.md").write_text("\n".join(content), encoding="utf-8")


def write_getting_started() -> None:
    content = [
        "# 使用文档",
        "",
        "## 项目定位",
        "",
        "PentAGI 是一个以 AI Agent 为核心的自动化安全测试平台。它把一次渗透测试流程拆成多类代理与工具执行链，并通过数据库、向量存储、Docker 沙箱和前端工作台把这些能力组合起来。",
        "",
        "## 运行形态",
        "",
        "- 后端：Go 服务，提供 REST、GraphQL、认证、Flow 编排、Provider 接入与工具执行能力。",
        "- 前端：React + TypeScript 单页应用，负责 Flow 管理、Provider 配置、资源管理和实时状态展示。",
        "- 数据层：PostgreSQL + pgvector；可选 Neo4j、Langfuse 与观测栈。",
        "- 执行层：Docker 沙箱运行安全工具与部分代理任务。",
        "",
        "## 环境准备",
        "",
        "至少准备以下依赖：",
        "",
        "- Go 1.25.x",
        "- Node.js + pnpm",
        "- Docker / Docker Compose",
        "- PostgreSQL（需可用 pgvector）",
        "- 至少一个可用的大模型 Provider Key",
        "",
        "复制环境文件：",
        "",
        "```bash",
        "cp .env.example .env",
        "```",
        "",
        "然后至少补齐数据库连接和一个 Provider 的配置。",
        "",
        "## 推荐启动方式",
        "",
        "### 方式一：Docker Compose 启动整套栈",
        "",
        "在仓库根目录执行：",
        "",
        "```bash",
        "docker compose up -d",
        "```",
        "",
        "如果需要可观测性或扩展组件：",
        "",
        "```bash",
        "docker compose -f docker-compose.yml -f docker-compose-observability.yml up -d",
        "docker compose -f docker-compose.yml -f docker-compose-langfuse.yml up -d",
        "docker compose -f docker-compose.yml -f docker-compose-graphiti.yml up -d",
        "```",
        "",
        "默认完整栈地址通常为 `https://localhost:8443`。",
        "",
        "### 方式二：本地分别运行前后端",
        "",
        "#### 后端",
        "",
        "```bash",
        "cd backend",
        "go mod download",
        "go build -trimpath -o pentagi ./cmd/pentagi",
        "go test ./...",
        "```",
        "",
        "直接运行主程序：",
        "",
        "```bash",
        "go run ./cmd/pentagi",
        "```",
        "",
        "#### 前端",
        "",
        "```bash",
        "cd frontend",
        "pnpm install",
        "pnpm run dev",
        "```",
        "",
        "前端开发服务器默认运行在 `http://localhost:8000`。",
        "",
        "## 常用开发命令",
        "",
        "### 后端",
        "",
        "```bash",
        "go test ./...",
        "go test ./pkg/foo/... -v -run TestName",
        "golangci-lint run --timeout=5m",
        "```",
        "",
        "### 前端",
        "",
        "```bash",
        "pnpm run build",
        "pnpm run lint",
        "pnpm run lint:fix",
        "pnpm run prettier",
        "pnpm run prettier:fix",
        "pnpm run test",
        "pnpm run test:coverage",
        "```",
        "",
        "## 代码生成入口",
        "",
        "以下场景需要重新生成代码：",
        "",
        "- 修改 `backend/pkg/graph/schema.graphqls` 后：",
        "",
        "```bash",
        "cd backend",
        "go run github.com/99designs/gqlgen --config ./gqlgen/gqlgen.yml",
        "```",
        "",
        "- 修改 REST Swagger 注解后：",
        "",
        "```bash",
        "cd backend",
        "swag init -g ../../pkg/server/router.go -o pkg/server/docs/ --parseDependency --parseInternal --parseDepth 2 -d cmd/pentagi",
        "```",
        "",
        "- 修改 `frontend/src/graphql/*.graphql` 后：",
        "",
        "```bash",
        "cd frontend",
        "pnpm run graphql:generate",
        "```",
        "",
        "## 主要业务使用路径",
        "",
        "1. 登录系统并进入 Dashboard。",
        "2. 在 Flows 页面创建一次新的安全测试 Flow。",
        "3. 后端调度 Researcher / Developer / Executor 等代理，并把状态写入数据库。",
        "4. 前端通过 GraphQL / REST 拉取 Flow、任务、文件、日志与截图信息。",
        "5. 如需管理模型能力，在 Settings 中配置 Provider、Prompt 和 API Token。",
        "",
        "## 排障阅读顺序",
        "",
        "- 服务启动失败：先看 `backend/cmd/pentagi/main.go`、`.env`、数据库连接和 Docker 配置。",
        "- API 路由问题：先看 `backend/pkg/server/router.go`，再看对应 `backend/pkg/server/services/*.go`。",
        "- Flow 编排异常：重点看 `backend/pkg/controller/`、`backend/pkg/providers/`、`backend/pkg/docker/`。",
        "- 前端页面问题：从 `frontend/src/app.tsx` 找到对应页面，再追 `pages/ -> features/ -> components/ -> providers/`。",
        "",
    ]
    (DOCS_ROOT / "getting-started.md").write_text("\n".join(content), encoding="utf-8")


def write_catalog(files: list[FileInfo], reverse_deps: dict[str, list[str]], group_map: dict[str, list[FileInfo]]) -> None:
    for group, members in group_map.items():
        slug = group.replace("/", "__")
        lines = [
            f"# `{group}` 文件清单",
            "",
            f"本组共 `{len(members)}` 个文件。",
            "",
        ]

        for info in members:
            incoming = reverse_deps.get(info.rel_path, [])
            incoming_label = "被这些文件直接引用"
            if not incoming and info.rel_path.endswith(".go"):
                incoming = reverse_deps.get(directory_of(info.rel_path), [])
                if incoming:
                    incoming_label = "被这些文件直接引用（按 Go 包级 import 统计）"
            lines.extend(
                [
                    f"## `{info.rel_path}`",
                    "",
                    f"- 文件类型：`{info.ext or '<none>'}`",
                    f"- 大小：`{info.size}` 字节",
                    f"- 文本行数：`{info.line_count if info.line_count is not None else '二进制/未统计'}`",
                    f"- 所属分组：`{info.group}`",
                    f"- 所属包/模块：`{info.package_name or '未识别'}`",
                    f"- 推断作用：{info.role}",
                    f"- 生成文件：`{'是' if info.generated else '否'}`",
                ]
            )

            if info.symbols:
                lines.append(f"- 关键导出/符号：`{', '.join(info.symbols[:12])}`")
            else:
                lines.append("- 关键导出/符号：`无或未解析`")

            if info.deps:
                dep_preview = ", ".join(f"`{dep}`" for dep in info.deps[:12])
                if len(info.deps) > 12:
                    dep_preview += f" 等 {len(info.deps)} 项"
                lines.append(f"- 直接依赖：{dep_preview}")
            else:
                lines.append("- 直接依赖：`无或未解析`")

            if incoming:
                incoming_preview = ", ".join(f"`{src}`" for src in incoming[:12])
                if len(incoming) > 12:
                    incoming_preview += f" 等 {len(incoming)} 项"
                lines.append(f"- {incoming_label}：{incoming_preview}")
            else:
                lines.append("- 被这些文件直接引用：`当前未发现`")

            if info.notes:
                lines.append(f"- 备注：{'；'.join(info.notes)}")

            lines.append("")

        (CATALOG_ROOT / f"{slug}.md").write_text("\n".join(lines), encoding="utf-8")


def write_index(files: list[FileInfo], group_map: dict[str, list[FileInfo]]) -> None:
    total_groups = len(group_map)
    root_lines = [
        "# 项目审查文档索引",
        "",
        "## 文档入口",
        "",
        "- [架构总览](./architecture-overview.md)",
        "- [使用文档](./getting-started.md)",
        "- [关系图谱](./relationships.md)",
        "- [机器可读关系图](./relationships.json)",
        "",
        "## 文件目录索引",
        "",
        f"共拆分为 `{total_groups}` 个分组文档，按目录职责组织：",
        "",
        "| 分组 | 文件数 | 入口文档 |",
        "|---|---:|---|",
    ]

    for group, members in group_map.items():
        slug = group.replace("/", "__")
        root_lines.append(f"| `{group}` | {len(members)} | [查看](./catalog/{slug}.md) |")

    root_lines.extend(
        [
            "",
            "## 生成范围",
            "",
            f"- 文件总数：`{len(files)}`",
            f"- Catalog 文档数：`{total_groups}`",
            "",
            "## 推荐阅读顺序",
            "",
            "1. 先读 `architecture-overview.md` 理解运行路径与设计边界。",
            "2. 再读 `getting-started.md` 熟悉实际运行、构建和代码生成方式。",
            "3. 再读 `relationships.md` 理解启动链、目录依赖与热点模块。",
            "4. 最后进入 `catalog/` 逐组查看具体文件职责与上下游关系。",
            "",
        ]
    )

    (DOCS_ROOT / "README.md").write_text("\n".join(root_lines), encoding="utf-8")


def write_json(files: list[FileInfo], reverse_deps: dict[str, list[str]]) -> None:
    nodes = []
    file_paths = {info.rel_path for info in files}
    synthetic_targets = {dep for info in files for dep in info.deps if dep not in file_paths}
    edges = []
    for info in files:
        nodes.append(
            {
                "path": info.rel_path,
                "nodeType": "file",
                "group": info.group,
                "role": info.role,
                "generated": info.generated,
                "size": info.size,
                "lineCount": info.line_count,
                "symbols": info.symbols,
            }
        )
        for dep in info.deps:
            edges.append(
                {
                    "source": info.rel_path,
                    "target": dep,
                    "kind": info.dep_kinds.get(dep, "unknown"),
                }
            )

    for target in sorted(synthetic_targets):
        nodes.append(
            {
                "path": target,
                "nodeType": "package",
                "group": directory_of(target),
                "role": "Go 包目录节点，用于承接包级 import 关系。",
                "generated": False,
                "size": None,
                "lineCount": None,
                "symbols": [],
            }
        )

    payload = {
        "repoRoot": REPO_ROOT.as_posix(),
        "generatedBy": "scripts/generate_project_audit.py",
        "nodes": nodes,
        "edges": edges,
        "reverseDependencies": reverse_deps,
    }
    RELATIONSHIPS_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def directory_of(rel_path: str) -> str:
    return str(Path(rel_path).parent).replace("\\", "/")


def dedupe(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def escape_pipes(value: str) -> str:
    return value.replace("|", "\\|")


if __name__ == "__main__":
    main()
