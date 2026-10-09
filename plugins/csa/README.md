# CSA APIKey MCP 工具

插件 `plugins/csa/plugin.py` 将 `plugins/csa/docs/openapi.json` 中明确允许普通用户通过账号 APIKey 访问的 **61 个操作**注册为网关工具，默认上游地址为 `https://api.altasci.com`。每个接口都是独立工具，管理员可分别绑定、重命名、启停；未绑定的工具不会出现在组端点。无需修改网关路由或创建另一台 MCP 服务器。

本文属于第三方插件接入文档。命令从仓库根目录执行；上游资料见 [资料边界](docs/README.md)，网关通用能力见 [主体文档](../../docs/README.md)。

## 调用方式

调用方每次提供 `api_key` 与 `request`。插件将 APIKey 写入此次上游请求的 `X-API-Key`，不会保存到数据库、配置、环境变量或共享客户端，也不会透传网关入站 Bearer token。调用方应在 MCP 客户端安全注入密钥，避免把含密钥的工具参数记录到客户端日志或共享对话。

| 凭据 | 用途 |
| --- | --- |
| CSA 账号 APIKey | 61 个用户工具；以账号权限和资源归属执行 |
| 网关组访问 Key | 组使用 static 认证时，作为访问 `/{group}/mcp` 的 Bearer；与上述密钥独立 |

本插件采用**调用方传入 APIKey**，是通常“管理员通过 `$secret` 注入上游密钥”模式的明确例外。配置 schema 仅有 `base_url`，默认值已设为实际服务地址；密钥不能写进配置集。

```python
import asyncio
from getpass import getpass

from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

endpoint = input("网关组 MCP URL: ").strip()
gateway_key = getpass("网关组访问 Key: ")
csa_key = getpass("CSA 账号 APIKey: ")

async def main():
    transport = StreamableHttpTransport(
        endpoint, headers={"Authorization": "Bearer " + gateway_key}
    )
    async with Client(transport) as client:
        # 使用管理员绑定的 exposed_name；下例假设名称为 csa_list_tickets。
        result = await client.call_tool("csa_list_tickets", {
            "api_key": csa_key,
            "request": {"query": {"skip": 0, "limit": 10, "status_filter": "pending"}},
        })
        print(result.data)

asyncio.run(main())
```

所有工具的输入均为 `{api_key, request}`。`request` 的精确 schema 按接口生成：

- `path`：路径参数，如 `{"ticket_id":"实际ID"}`。
- `query`：查询参数，保留各接口的分页上限、枚举与实际名称。省略参数不主动补默认值；`null` 查询值省略发送。
- `body`：原始 JSON body，保留字段缺省、显式 `null`、兼容标量的区别。
- 无业务参数时仍传 `request: {}`，例如 `csa.get_me`。

创建工单调用 `csa.create_ticket`，request 示例：

```json
{"body":{"title":"服务故障","ticket_type":"technical","content":"控制台无法打开"}}
```

用户可通过 `csa.get_file_download_url` 获取自己项目文件的下载授权。项目上传及文件登记属于管理员接口，不暴露；插件不自动访问上游返回的授权 URL。

## 响应与业务约束

成功为 `{"ok":true,"status":200,"data":上游结果}`，保留真实状态码；204 的 data 为 null。JSON、JSON null、Markdown/文本附件均可返回，不将响应错误地统一当成上游 `data` 包装。响应上限 10 MiB。

失败为 `{"ok":false,"status":401,"error":"upstream_http_error"}` 等安全错误。调用者必须检查 `ok`；它是结构化业务结果，网关框架异常才是 MCP `isError`。不返回上游错误正文、敏感参数或响应头。网络超时、传输失败、无效参数、错误 JSON、超大响应分别有稳定错误码；没有响应时 status 为 null。

APIKey 及常见认证材料（key、token、client secret、TOTP secret、恢复码等）从成功结果中脱敏。因此密钥生成/轮转工具可以执行管理动作，但不会通过 MCP 交付生成的明文；需要取得新凭据时请使用 CSA 官方管理界面。管理员数据导出、账号管理、系统密钥管理等接口不注册。

写请求没有自动重试。商城下单必须由调用者提供并保留 `request_id`；网关超时不能证明写操作未发生。下单所需目录 revision、项目归属和用户权限由 CSA 验证。插件提前拒绝路径注入、未知 path/query 参数及项目 path/body ID 不一致；OpenAPI 无法描述的跨字段业务规则仍由上游判断。

OpenAPI 已声明 `AccountAPIKey`，但部分旧 Markdown 仍只写 Bearer；本插件以机器契约为准，不进行登录或 JWT 兑换。仅注册 `AccountAPIKey` 且 `x-access` 明确为“登录；资源归属限制见接口说明”的操作。57 个管理员接口、4 个超级管理员接口、2 个服务专用接口及其余 27 个接口均不注册；缺少或未知权限标记也不注册。用户与管理员共用的接口保留，角色相关的过滤和资源归属仍由上游校验。

## 部署与绑定

工具清单可通过管理端目录查看；`gateway plugins check` 只输出工具总数和指纹；代码 ID 为 `csa.` 加上 OpenAPI operationId 的 `_api_` 前缀之前部分。例如：

| 代码 ID | API |
| --- | --- |
| `csa.get_me` | GET /api/users/me |
| `csa.list_tickets` / `csa.create_ticket` | GET / POST /api/tickets |
| `csa.get_ticket` / `csa.update_ticket` / `csa.delete_ticket` | GET / PUT / DELETE /api/tickets/{ticket_id} |
| `csa.list_my_projects` | GET /api/projects/me |
| `csa.catalog` / `csa.preview_quote` / `csa.create_order` | 商城目录、报价、下单 |
| `csa.my_commissions` | GET /api/agents/commissions |

遵循[新增工具指南](../../docs/agent-tool-guide.md)的整批发布流程，禁止新旧 worker 混用插件制品：

```sh
uv sync --frozen
uv run python scripts/generate_csa.py --check
uv run gateway plugins check
uv run ruff check backend sdk plugins tests migrations scripts
uv run pytest -q tests/test_csa.py
# 隔离 PostgreSQL/Redis + 两个 worker + 标准 HTTP MCP 的端到端验收
uv run python tests/run.py tests/test_csa.py tests/test_csa_gateway.py

# 目标 Compose 部署（需在实际部署环境执行）
docker compose --profile setup build backend migrate sync
docker compose run --rm --no-deps backend gateway plugins check
docker compose stop backend
docker compose run --rm migrate
docker compose run --rm sync
docker compose up -d --force-recreate backend
```

在管理端创建 static 认证组（例如 `csa`），创建组访问 Key，然后只绑定需要的工具。每个工具可使用默认配置，不需要配置集。新绑定示例（使用管理员 Cookie + CSRF 调用管理 API）：

```json
{
  "id": "csa-list-tickets",
  "data": {
    "group_id": "csa",
    "tool_id": "csa.list_tickets",
    "exposed_name": "csa_list_tickets",
    "overrides": {},
    "enabled": false
  }
}
```

提交至 `POST /api/v1/bindings` 后，调用 `POST /api/v1/bindings/csa-list-tickets/validate`，通过 GET 读取绑定和组的实时 version 后分别启用（validate 仅返回 valid）。端点为 `https://你的网关/csa/mcp`。完整的组、认证、访问 Key 创建与版本更新示例见[新增工具指南第 6 节](../../docs/agent-tool-guide.md#6-将工具绑定到组)。不要将 CSA APIKey 用作管理 API 登录凭据。

需要更换上游时通过管理员 overrides 设置 `{"base_url":"https://另一个可信CSA地址"}`，仅接受 HTTPS 根地址；回环 HTTP 用于本地测试。调用方不能更改目标 URL 或认证头。

## 契约维护

```sh
# plugins/csa/docs/openapi.json 更新后显式重新生成并审阅差异
uv run python scripts/generate_csa.py
uv run python scripts/generate_csa.py --check
```

生成器仅选取明确支持 AccountAPIKey 且权限标记为普通登录用户的操作，并把 schema、说明、路径和成功状态编译到 `plugins/csa/contract.py`。运行时无须 `plugins/csa/docs`。生成文件为 Python，因此被网关现有制品指纹覆盖。更新后仍需 check、sync、全部 worker 重启；不会自动绑定新增工具到组。

从旧版升级时，执行目录同步会将已移除的管理员/服务工具标记为 `available=false`，历史绑定保留但不可调用。必须按上述流程同步并重启全部 worker，生产环境才会应用此变更。
