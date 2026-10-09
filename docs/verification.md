# 验证指南

本页说明当前仓库的检查入口，不将历史测试次数或一次构建结果当作持续通过证明。测试覆盖以源码和实际运行输出为准。

## 离线检查

需要 Python 3.12+、uv；前端使用 Node 24 和 npm。从仓库根目录执行：

```sh
uv sync --frozen
uv run gateway plugins check
uv run ruff check backend sdk plugins tests migrations scripts
uv run pytest -q tests/test_emailutils.py tests/test_csa.py tests/test_storage.py
npm --prefix frontend ci
npm --prefix frontend run build
```

上面选出的插件测试不需要真实上游凭据。其他依赖运行中网关的测试应通过隔离 runner 执行，避免直接对开发服务运行整个 pytest 套件。第三方插件契约的生成与一致性检查见[插件目录](../plugins/README.md)中的各自指南。

## 隔离集成与浏览器验收

额外需要 Docker Compose 和 Chromium：

```sh
cd frontend
npx playwright install chromium
cd ..
uv run python tests/run.py
```

runner 建立随机项目名和端口的 PostgreSQL、Redis、HTTPS 测试 IDP，复制插件并添加测试 probe；运行迁移、目录同步和管理员初始化，然后启动两个 Uvicorn worker。

未传参数时运行后端套件、前端构建和 Playwright，并检查 worker 重启后会话、组和工具目录恢复。传参数时将参数传给 pytest，跳过前端构建与浏览器套件，仍执行基础设施准备和重启检查：

```sh
uv run python tests/run.py tests/test_oauth.py
```

退出时清理临时服务及数据。该 runner 覆盖数据库和 Redis 连接环境，不使用当前 `.env` 的数据库；不要将它替换为对现有生产数据库的直接 pytest 调用。

## 覆盖对应关系

| 实现领域 | 测试文件 |
| --- | --- |
| 插件发现、目录同步、组与配置、执行超时 | `tests/test_gateway.py` |
| 管理员创建、登录、密码重置 | `tests/test_admin_auth.py` |
| OAuth 发现、PKCE、JWT、introspection | `tests/test_oauth.py` |
| 批量绑定、删除、回滚 | `tests/test_batch.py` |
| HTTP 请求编号、错误与跨域诊断 | `tests/test_http_diagnostics.py` |
| 修复回归 | `tests/test_review_fixes.py` |
| 管理页面、引导、交互、批量操作 | `frontend/e2e/*.spec.ts` |
| 第三方插件协议与 MCP 接入 | 对应 `tests/test_<plugin>.py` 和 `test_<plugin>_gateway.py` |

测试 IDP 自动同意授权，只用于验收，不代表任意商业 IDP 的配置都兼容。真实业务场景的准备和历史证据见[场景目录](../scenarios/README.md)。

## 更新管理 OpenAPI 快照

下面只创建应用和生成 schema，不启动 lifespan、不连接数据库；导入本地插件需要安装好依赖：

```sh
uv run python - <<'PY'
import json
from pathlib import Path
from cryptography.fernet import Fernet
from gateway.app import create_app
from gateway.settings import Settings

settings = Settings(_env_file=None, master_key=Fernet.generate_key().decode(), plugins_path='plugins')
schema = create_app(settings).openapi()
Path('docs/openapi.json').write_text(json.dumps(schema, ensure_ascii=False, indent=2) + '\n')
PY
```

这是通用管理路由的 OpenAPI，不包含 MCP 工具业务 schema。`data` 的具体资源校验规则还应查阅 [管理 API](api.md) 和 `contracts.py`、`service.py`；工具参数通过 MCP tools/list 或工具目录读取。
