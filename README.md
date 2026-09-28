# MCP Gateway

React 管理端 + FastAPI 管理 API + FastMCP 动态 Provider。开发者部署可信 Python 插件，管理员将工具绑定到不同组；每个组提供独立的 `/{group}/mcp` 无状态 Streamable HTTP 端点。

编码智能体新增工具请先阅读 [新增工具与网关注册执行指南](docs/agent-tool-guide.md)，其中包含可运行模板、部署命令、绑定 API 和调用验收步骤。

## 本地启动

需要 Docker Compose。若在宿主机开发，还需要 Python 3.12+、uv、Node 24。

```sh
cp .env.example .env
# 生成密钥，将输出填入 .env 的 MASTER_KEY（只需生成一次，务必备份）
docker run --rm python:3.13-slim python -c 'import base64,secrets; print(base64.urlsafe_b64encode(secrets.token_bytes(32)).decode())'
docker compose build
docker compose up -d --wait postgres redis
# 独立部署步骤：不要让每个 worker 自动迁移或同步目录
docker compose run --rm migrate
docker compose run --rm sync
docker compose run --rm backend gateway admin-create admin
# 交互式输入至少 12 位密码
docker compose up -d backend frontend
```

管理端内置“入门指南”，说明工具、组、绑定和两类密钥的关系。界面与维护说明见 [前端指南](docs/frontend.md)。

管理端：<http://localhost:5173>；API 文档：<http://localhost:8000/docs>。登录后：

1. 创建密钥 `demo-key`。
2. 创建配置集 `demo-config`，值为 `{"prefix":"Hello","api_key":{"$secret":"demo-key"}}`。
3. 创建组 `user1`，默认禁用。未指定认证配置时是公开模式。
4. 创建绑定：组 `user1`、工具 `demo.echo`、暴露名称 `echo`、配置集 `demo-config`，启用绑定。
5. 编辑并启用组。组详情提供 URL 和连接示例。

```python
import asyncio
from fastmcp import Client

async def main():
    async with Client("http://localhost:8000/user1/mcp") as client:
        print(await client.list_tools())
        print((await client.call_tool("echo", {"message": "world"})).data)

asyncio.run(main())
```

## 开发与验证

```sh
uv sync --frozen
npm --prefix frontend ci
uv run gateway plugins check
# .env 中设置实际可访问的 PostgreSQL、Redis 和 MASTER_KEY
uv run alembic upgrade head
uv run gateway plugins sync
uv run gateway admin-create admin
uv run uvicorn gateway.app:create_app --factory --port 8000 --no-access-log
npm --prefix frontend run dev
```

前端独立部署时，在构建时设置 `VITE_API_URL`。后端只允许 `CONSOLE_ORIGIN` 的带 Cookie 管理请求。

完整验收使用随机端口和独立 Compose 项目，创建临时 PostgreSQL、Redis、HTTPS 测试 IDP，启动两个后端 worker，并运行 Chromium 管理闭环；退出后销毁测试容器和数据，不使用当前 `.env` 的数据库。

```sh
cd frontend && npx playwright install chromium && cd ..
uv run python tests/run.py
uv run ruff check backend sdk plugins tests migrations
npm --prefix frontend run build
```

`uv run python tests/run.py tests/test_oauth.py` 可以只运行指定后端测试。测试 IDP 自动同意授权，仅供验收；生产镜像 `runtime` 不包含它。FastMCP 固定为 `4.0.10`，完整 Python 和前端依赖分别锁定在 `uv.lock`、`frontend/package-lock.json`。

## 真实智能体场景

已使用 Codex CLI 和 Claude Code 创建四个物流分诊智能体，让它们通过网关读取商户规则、检查订单并创建内部工单草稿。四个任务均完成，覆盖组隔离、故障重试和业务幂等性。模型调用真实运行，订单数据为测试数据。

- [运行场景](scenarios/fulfillment/README.md)
- [实测报告与调用证据](docs/reports/fulfillment-2026-09-27/report.md)

## 目录

- `backend/gateway/`：管理、认证、请求快照、Provider、CLI。
- `sdk/gateway_sdk/`：独立插件 SDK，可用 `uv pip install ./sdk` 安装。
- `plugins/demo/plugin.py`：配置注入和同步工具示例。
- `frontend/`：Ant Design、官方图标、Tailwind CSS、Router、TanStack Query 管理端。
- `migrations/`：Alembic 数据库迁移。
- `tests/`、`compose.test.yml`：真实协议、隔离、认证、并发和浏览器验收。

详见 [插件契约](docs/plugins.md)、[管理 API](docs/api.md)、[认证兼容性](docs/auth.md)、[部署与故障排查](docs/deployment.md)。

首版仅支持可信本地工具和 PostgreSQL；不包含远程 MCP 聚合、代码热加载、代码沙箱、resources/prompts、多租户管理权限、持久 MCP 会话或主动 `list_changed` 广播。
