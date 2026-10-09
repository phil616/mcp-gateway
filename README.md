# MCP Gateway

React 管理端 + FastAPI 管理 API + FastMCP 动态 Provider。开发者部署可信 Python 插件，管理员将工具绑定到不同组；每个组提供独立的 `/{group}/mcp` 无状态 Streamable HTTP 端点。

编码智能体新增工具请先阅读 [新增工具与网关注册执行指南](docs/agent-tool-guide.md)，其中包含可运行模板、部署命令、绑定 API 和调用验收步骤。

## 本地启动

需要 Docker Compose。若在宿主机开发，还需要 Python 3.12+、uv、Node 24。

```sh
cp .env.example .env
# 生成密钥，将输出填入 .env 的 MASTER_KEY（只需生成一次，务必备份）
docker run --rm python:3.13-slim python -c 'import base64,secrets; print(base64.urlsafe_b64encode(secrets.token_bytes(32)).decode())'
docker compose --profile setup build backend migrate sync frontend
docker compose up -d --wait postgres redis
# 独立部署步骤：不要让每个 worker 自动迁移或同步目录
docker compose run --rm migrate
docker compose run --rm sync
docker compose run --rm backend gateway admin-create admin
# 交互式输入至少 12 位密码
docker compose up -d backend frontend
```

管理端内置“入门指南”，说明工具、组、绑定和两类密钥的关系。界面与维护说明见 [前端指南](docs/frontend.md)。

管理端：<http://localhost:5173>；API 文档：<http://localhost:5173/docs>。登录后：

1. 创建上游密钥 `demo-key`，值可填本地演示字符串（该工具不访问上游）。
2. 创建配置集 `demo-config`，值为 `{"prefix":"Hello","api_key":{"$secret":"demo-key"}}`。
3. 创建组 `user1`，默认禁用。未指定认证配置时是公开模式。
4. 创建绑定：组 `user1`、工具 `demo.echo`、暴露名称 `echo`、配置集 `demo-config`，启用绑定。
5. 编辑并启用组。组详情提供 URL 和连接示例。

```python
import asyncio
from fastmcp import Client

async def main():
    async with Client("http://localhost:5173/user1/mcp") as client:
        print(await client.list_tools())
        print((await client.call_tool("echo", {"message": "world"})).data)

asyncio.run(main())
```

## 开发与验证

```sh
uv sync --frozen
npm --prefix frontend ci
uv run gateway plugins check
# 宿主机运行前设置 DATABASE_URL、REDIS_URL、MASTER_KEY
# PUBLIC_URL=http://localhost:8000，CONSOLE_ORIGIN=http://localhost:5173
# COOKIE_SECURE=false；Compose 的数据库/Redis 默认不映射宿主机端口
uv run alembic upgrade head
uv run gateway plugins sync
uv run gateway admin-create admin
uv run uvicorn gateway.app:create_app --factory --port 8000 --no-access-log
npm --prefix frontend run dev
```

默认 Compose 仅发布 `5173` 一个端口，前端 nginx 将 API、MCP、OAuth 元数据和健康检查转发到 Docker 内网后端。Vite 开发服务器也默认代理本地 `8000` 后端。单域名 HTTPS 配置见 [部署文档](docs/deployment.md)。

前端独立部署时，在构建时设置 `VITE_API_URL`。后端只允许 `CONSOLE_ORIGIN` 的带 Cookie 管理请求。

完整验收使用随机端口和独立 Compose 项目，创建临时 PostgreSQL、Redis、HTTPS 测试 IDP，启动两个后端 worker，并运行 Chromium 管理闭环；退出后销毁测试容器和数据，不使用当前 `.env` 的数据库。

```sh
cd frontend && npx playwright install chromium && cd ..
uv run python tests/run.py
uv run ruff check backend sdk plugins tests migrations scripts
npm --prefix frontend run build
```

`uv run python tests/run.py tests/test_oauth.py` 可以只运行指定后端测试。测试 IDP 自动同意授权，仅供验收；生产镜像 `runtime` 不包含它。FastMCP 固定为 `4.0.10`，完整 Python 和前端依赖分别锁定在 `uv.lock`、`frontend/package-lock.json`。

## 文档与扩展

[网关文档入口](docs/README.md)提供架构、配置、管理 API、认证、插件 SDK、前端和验证指南。主体负责工具接入、分组、认证、配置和执行生命周期；业务接口由插件实现。

- [插件目录](plugins/README.md)：随仓库提供的示例、工具及第三方适配器，各自维护业务说明和上游契约。
- [场景目录](scenarios/README.md)：独立业务演示、运行步骤及历史验收证据。

## 目录与能力边界

| 目录 | 职责 |
| --- | --- |
| `backend/gateway/` | 通用管理 API、认证、请求快照、动态 Provider、CLI |
| `sdk/gateway_sdk/` | 插件契约；可独立打包，不依赖网关数据库或应用 |
| `frontend/` | React 管理控制台 |
| `migrations/` | PostgreSQL 迁移 |
| `docs/` | 网关主体使用和维护文档、管理 API 快照 |
| `plugins/` | 插件实现及各自文档，第三方业务不属于网关内建 API |
| `scripts/` | 开发维护工具，包括插件契约生成器 |
| `tests/` | 网关及插件测试，隔离验收入口为 `tests/run.py` |
| `scenarios/` | 独立业务场景及其报告 |

当前仅加载可信本地 Python 工具；不支持远程 MCP 服务器聚合、代码热加载、代码沙箱、resources/prompts、多租户管理权限、持久 MCP 会话或主动 `list_changed` 广播。组是工具和访问密钥的隔离单位，所有管理员拥有相同管理权限。
