# 编码智能体指南：新增工具并接入 MCP 网关

本文是给在本仓库工作的编码智能体使用的执行指南。目标是交付一个可通过标准 MCP 客户端列出、调用的新工具，而不只是写出一个 Python 函数。所有命令默认从仓库根目录执行。

## 1. 先明确“注册”的三个阶段

| 阶段 | 智能体需要完成的工作 | 成功标志 |
|---|---|---|
| 代码声明 | 在约定入口导出 `ToolPackage`，使用 `@package.tool(...)` | `gateway plugins check` 通过 |
| 目录同步与部署 | 将相同插件制品同步到 PostgreSQL，重新启动所有 worker | 管理 API 的工具记录 `available=true`，readiness 正常 |
| 组绑定与发布 | 创建或更新组内绑定，配置认证和配置值，启用绑定及组 | `/{group}/mcp` 的 `tools/list` 和 `tools/call` 成功 |

仅添加 Python 文件、仅运行 check、仅重启服务，都不代表工具已经对客户端可用。新增工具不会自动绑定到已有组。

**扩展工具通常只需修改 `plugins/`，必要时更新依赖和测试。** 不需要修改 `backend/gateway/app.py`，不需要 `include_router`，不需要创建新的 FastMCP 服务器，也不需要手写 JSON-RPC。管理 API 不支持用 `POST /api/v1/tools` 创建代码工具。

## 2. 开始前确认输入和已有实现

先确认业务输入、输出、外部服务、配置项、目标组、暴露名称，以及入站认证方式。缺少真实上游接口信息时，先完成不依赖它的代码和测试，明确列出缺项，不编造上游协议或成功结果。

优先复用目标插件现有的 `package` 对象。查阅以下文件中的实际接口，不引入另一套注册方式：

- [`sdk/gateway_sdk/__init__.py`](../sdk/gateway_sdk/__init__.py)：公开 SDK 和装饰器。
- [`plugins/demo/plugin.py`](../plugins/demo/plugin.py)：配置注入和同步工具示例。
- [`backend/gateway/catalog.py`](../backend/gateway/catalog.py)：发现规则、指纹和目录同步。
- [`backend/gateway/contracts.py`](../backend/gateway/contracts.py)：管理写入字段。
- [`docs/api.md`](api.md)：Cookie、CSRF、版本号和绑定 API。

遵循仓库的 CodeGraph 使用约定。依赖版本以 `pyproject.toml` 和 `uv.lock` 为准；当前 SDK 基于 FastMCP 4.0.10。运行 `uv sync --frozen` 安装仓库锁定的环境。根项目已经包含 SDK，不必再在同一环境安装 `./sdk`。

## 3. 新建最小工具

新建 `plugins/textutils/plugin.py`：

```python
from typing import Literal

from gateway_sdk import ToolPackage

package = ToolPackage(id="textutils", version="1.0.0")


@package.tool(
    id="normalize",
    description="去除文本首尾空白，并按指定模式转换大小写。",
    timeout=5,
)
async def normalize(
    text: str,
    mode: Literal["keep", "lower", "upper"] = "keep",
) -> dict[str, str]:
    value = text.strip()
    if mode == "lower":
        value = value.lower()
    elif mode == "upper":
        value = value.upper()
    return {"text": value}
```

这里的命名各有职责：

| 名称 | 示例 | 含义 |
|---|---|---|
| 插件入口 | `plugins/textutils/plugin.py` | 固定扫描 `plugins/*/plugin.py` |
| 导出的对象 | `package` | 入口必须导出这个名字的 `ToolPackage` |
| 包 ID | `textutils` | 在整个目录中唯一 |
| 工具局部 ID | `normalize` | 在同一个包中唯一 |
| 框架工具 ID | `textutils.normalize` | 绑定 API 使用的 `tool_id`，保持稳定 |
| Python 函数名 | `normalize` | 实现名称，不决定客户端暴露名称 |
| 组内暴露名称 | `normalize_text` | 绑定的 `exposed_name`，客户端调用这个名字 |
| 组 ID | `text-tools` | 端点为 `/text-tools/mcp`，创建后不可重命名 |

包 ID 和工具局部 ID 必须匹配 `[a-z][a-z0-9_-]*`。所有参数与返回值都要有类型注解；超时必须大于 0，默认 30 秒。描述需要说明用途、参数语义及重要副作用。尽量使用明确参数，避免无边界的 `*args`、`**kwargs`。

没有配置时省略 `config_model`，使用默认的空配置模型；不需要注入 runtime。新增同包工具时在现有 `package` 上添加装饰器，不要重新赋值 `package`。如果将工具放到其他模块，入口必须显式导入这些模块以执行装饰器；扫描器不会递归自动导入辅助文件。注意避免循环导入。

## 4. 需要配置、密钥或组上下文时

客户端提供的业务参数写入函数签名；管理员配置和密钥放入 Pydantic 配置模型，通过 runtime 注入。例如另一个独立入口 `plugins/upstream/plugin.py`：

```python
import httpx
from pydantic import BaseModel, SecretStr

from gateway_sdk import Depends, ToolPackage, ToolRuntime, current_runtime

package = ToolPackage(id="upstream", version="1.0.0")


class LookupConfig(BaseModel):
    model_config = {"extra": "forbid"}
    base_url: str
    api_key: SecretStr


@package.tool(id="lookup", config_model=LookupConfig, timeout=15)
async def lookup(
    query: str,
    runtime: ToolRuntime = Depends(current_runtime),
) -> dict:
    """查询管理员配置的上游服务；不向调用者返回访问凭据。"""
    config = runtime.config(LookupConfig)
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(
            config.base_url.rstrip("/") + "/lookup",
            params={"q": query},
            headers={"Authorization": "Bearer " + config.api_key.get_secret_value()},
        )
        response.raise_for_status()
        return response.json()
```

此处 `/lookup`、`q` 和响应结构只是上游适配模板，必须替换为目标服务的真实协议；不要把模板当成已验证的业务接口。`httpx` 已在本仓库依赖中。引入其他库时使用 `uv add '包名==验证过的版本'`，提交 `pyproject.toml` 和 `uv.lock`，并重新构建镜像。

必须遵循这些约束：

- 从 `gateway_sdk` 导入 `Depends`，不要使用 FastAPI 的同名对象。注入的 runtime、配置及凭据不得进入客户端业务参数 schema。
- `runtime.config(LookupConfig)` 取得本次调用的类型化配置；`runtime.group` 和 `runtime.call_id` 提供组和调用标识。不要读取 SDK 私有 ContextVar 或自行设置全局运行时。
- 配置优先级是 **模型默认值 → 配置集 values → 绑定 overrides**。这是字段级浅覆盖，嵌套对象整体替换。每个绑定最多引用一个配置集。
- 密钥必须通过 `{"$secret":"密钥ID"}` 引用，不能把明文直接填入 `SecretStr` 配置字段。普通字符串不进行环境变量或模板展开。
- 不将组密钥写进 `.env`、`os.environ`、全局变量或共享上游客户端；带凭据客户端按调用创建并关闭。不要透传 Agent 入站 Bearer token。
- `async def` 使用异步 I/O。同步 SDK 可使用 `def` 工具，由框架在线程池执行；不要在异步函数中直接调用阻塞 SDK、`time.sleep` 或执行长时间 CPU 计算。
- 为上游请求设置超时并关闭资源。网关超时不能停止已开始的同步线程，也不能撤销已经发生的外部副作用；写操作需要设计幂等性。
- 不记录或返回凭据、完整请求头、敏感参数和上游原始错误。框架会掩码执行异常，但插件自己写出的日志仍由插件负责。

配置工具的管理顺序如下，资源 ID 可按项目实际命名：

| API | 请求体示例 |
|---|---|
| `POST /api/v1/secrets` | `{"id":"upstream-key","data":{"value":"由安全输入提供的实际密钥"}}` |
| `POST /api/v1/config-profiles` | `{"id":"lookup-config","data":{"values":{"base_url":"https://实际上游域名","api_key":{"$secret":"upstream-key"}}}}` |
| `POST /api/v1/bindings` | `{"id":"lookup-binding","data":{"group_id":"目标组","tool_id":"upstream.lookup","exposed_name":"lookup","profile_id":"lookup-config","overrides":{},"enabled":false}}` |

然后校验绑定并启用。不要将表中的密钥占位文字提交为真实密钥。密钥读取接口只返回掩码；已有掩码不能作为新密钥写回。

## 5. 先做本地检查，再部署代码

```sh
uv run gateway plugins check
uv run ruff check plugins
```

若使用自定义插件目录，check 需要显式传入路径：`uv run gateway plugins check --path /实际目录`。同步和服务启动使用 `PLUGINS_PATH`，应指向同一目录。导入失败、缺失依赖、重复 ID、缺失类型注解都必须修复；check 不会执行工具函数。

对上面的纯文本示例，可以在不启动数据库的情况下检查 schema 和真实 FastMCP 调用：

```sh
uv run python - <<'PY'
import asyncio
from fastmcp import Client, FastMCP
from gateway.catalog import Catalog

async def main():
    spec = Catalog("plugins").tools["textutils.normalize"]
    assert set(spec.tool.parameters["properties"]) == {"text", "mode"}
    server = FastMCP("plugin-contract-check")
    server.add_tool(spec.tool)
    async with Client(server) as client:
        result = await client.call_tool(
            "textutils.normalize", {"text": "  HeLLo  ", "mode": "lower"}
        )
        assert result.data == {"text": "hello"}

asyncio.run(main())
PY
```

这只验证插件契约和函数行为，不能替代下面的组路由、配置注入和认证测试。配置工具应通过网关绑定后调用，不能直接调用带 `Depends` 默认值的 Python 函数并期待框架自动注入 runtime。外部服务使用受控测试服务或 mock 验证错误路径，不能仅凭导入成功宣称业务可用。

### Compose 发布

基础设施、管理员和主密钥按 [README](../README.md) 初始化。已有部署增加插件时：

```sh
# 分别构建这些服务，确保 check、sync、backend 使用新代码。
docker compose --profile setup build backend migrate sync
docker compose run --rm --no-deps backend gateway plugins check

# 代码发布采用整批停止/重启，禁止新旧 worker 混用插件制品。
docker compose stop backend
docker compose run --rm migrate
docker compose run --rm sync
docker compose up -d --force-recreate backend
```

`migrate`、`sync` 和 `backend` 在当前 Compose 中可能有不同镜像标签，不能只重建 backend 后直接运行旧 sync 镜像。不要使用 `down --volumes` 发布代码，它会删除持久数据。同步失败时先处理错误，不能跳过同步或启动旧制品服务。

### 宿主机发布

停止现有网关全部 worker，再在安装好依赖、配好基础设施环境的部署目录执行：

```sh
uv run alembic upgrade head
uv run gateway plugins sync
uv run uvicorn gateway.app:create_app --factory --port 8000 --no-access-log
```

新增 Python 工具通常不需要新增数据库迁移，但部署时仍应将现有迁移应用到 head。新增代码、修改代码或删除代码都需要 check、sync 和整批重启；不支持热加载。目录同步覆盖整个插件制品，不能从只包含单个新插件的临时目录对生产数据库运行 sync，否则其他工具会被标记不可用。

## 6. 将工具绑定到组

可以通过 Web 完成：工具目录确认 `textutils.normalize` 可用 → 创建或选择组 → 配置入站认证 → 添加绑定（暴露名称 `normalize_text`）→ 校验 → 启用绑定 → 启用组。新组和新绑定默认禁用。同一个组中，同一 tool_id 只能绑定一次，不同工具的 exposed_name 必须唯一。

编码智能体可使用管理 REST API 自动化。下面脚本展示**创建全新资源**的完整最小路径，使用静态 Key 认证，适用于隔离开发环境。先完成第 5 节的代码部署，再将脚本保存到仓库内的临时 Python 文件，用 `uv run python 文件路径` 运行。密码使用交互输入，不写进代码：

```python
from getpass import getpass
import httpx

base = input("网关 URL [http://localhost:8000]: ").strip() or "http://localhost:8000"
base = base.rstrip("/")
origin = input("CONSOLE_ORIGIN [http://localhost:5173]: ").strip() or "http://localhost:5173"
username = input("管理员账号: ").strip()
password = getpass("管理员密码: ")

# 这些 ID 必须尚未存在；若使用已有资源，按下文的更新规则处理。
group_id = "text-tools"
auth_id = "text-tools-auth"
binding_id = "text-tools-normalize"

with httpx.Client(base_url=base, headers={"Origin": origin}, timeout=20) as client:
    def request(method, path, body=None):
        response = client.request(method, path, json=body)
        response.raise_for_status()
        return response.json()

    session = request("POST", "/api/v1/login", {
        "username": username, "password": password,
    })
    client.headers["X-CSRF-Token"] = session["csrf"]
    try:
        tool = request("GET", "/api/v1/tools/textutils.normalize")
        assert tool["available"] and tool["enabled"], "工具不可用或被全局禁用"
        request("POST", "/api/v1/auth-profiles", {
            "id": auth_id, "data": {"mode": "static"},
        })
        group = request("POST", "/api/v1/groups", {
            "id": group_id,
            "data": {"enabled": False, "auth_profile_id": auth_id},
        })
        binding = request("POST", "/api/v1/bindings", {
            "id": binding_id,
            "data": {
                "group_id": group_id,
                "tool_id": "textutils.normalize",
                "exposed_name": "normalize_text",
                "overrides": {},
                "enabled": False,
            },
        })
        request("POST", f"/api/v1/bindings/{binding_id}/validate")
        request("PUT", f"/api/v1/bindings/{binding_id}", {
            "version": binding["version"], "data": {"enabled": True},
        })
        key = request("POST", "/api/v1/access-keys", {
            "id": "text-tools-access", "data": {"group_id": group_id},
        })
        # token 仅在创建响应出现一次。立即交给安全凭据存储，禁止写入日志或提交仓库。
        access_token = key["token"]
        print("开发环境访问 Key（仅显示一次，请安全保存）:", access_token)
        request("PUT", f"/api/v1/groups/{group_id}", {
            "version": group["version"], "data": {"enabled": True},
        })
        print("MCP endpoint:", f"{base}/{group_id}/mcp")
    finally:
        request("POST", "/api/v1/logout")
```

不要把此脚本作为盲目重跑的幂等脚本。各个 HTTP 写请求是独立事务，中途失败时已创建的对象仍然存在。再次执行前查询现状，从失败步骤继续；不要为了避开 409 删除已有资源。

已有资源的处理规则：

1. 用 `GET /api/v1/{resource}/{id}` 读取当前对象，确认目标环境、所有权语义、组认证和原有配置。
2. 用 `PUT` 提交 `{ "version": 当前版本, "data": 必要改动 }`。版本号来自实时读取，不硬编码 1。
3. 409 时重新读取并分析冲突；不要无条件覆盖其他管理员修改。已有组不要被自动改为公开模式，也不要覆盖已有配置集或密钥。
4. 配置工具的绑定填写 `profile_id` 和必要 overrides。共享配置集更新会验证所有有效绑定，失败则整次更新拒绝；缺少必填配置不能启用。
5. 删除前读取 dependencies；工具代码的创建和删除由部署管理。移除代码会保留历史工具记录和绑定并标记不可用。

脚本中的 `Origin` 必须与后端 `CONSOLE_ORIGIN` 完全相同。管理认证是 Cookie + CSRF，**不能用组访问 Key 调管理 API**。`COOKIE_SECURE=true` 时必须通过 HTTPS 登录，不能通过 HTTP 绕过安全 Cookie。

## 7. 使用真实组端点验证

将下面代码保存为临时 Python 文件，并用 `uv run python 文件路径` 执行。交互输入第 6 节创建的 Key：

```python
import asyncio
from getpass import getpass

from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

endpoint = input("MCP endpoint: ").strip()
access_key = getpass("组访问 Key: ")


async def main():
    transport = StreamableHttpTransport(
        endpoint, headers={"Authorization": "Bearer " + access_key}
    )
    async with Client(transport) as client:
        tools = await client.list_tools()
        tool = next(t for t in tools if t.name == "normalize_text")
        assert set(tool.input_schema["properties"]) == {"text", "mode"}
        result = await client.call_tool(
            "normalize_text", {"text": "  HeLLo  ", "mode": "lower"}
        )
        assert result.data == {"text": "hello"}
        print("组端点验证通过")


asyncio.run(main())
```

调用组内暴露名 `normalize_text`，不是代码 ID `textutils.normalize`。工具列表是按组过滤的，绑定修改后重新执行 `tools/list`；本版不主动广播 `list_changed`。

有配置或副作用的工具还应验证：

- 同一工具绑定两个组，配置及密钥不同，并发调用没有串用；不要通过返回原始密钥证明隔离。
- 非法业务参数由 FastMCP 拒绝；业务结果符合声明的结构。
- 缺少必要配置无法启用，错误的组 Key、过期或撤销 Key 被拒绝。
- 禁用绑定或全局工具后，后续请求看不到或无法调用它。
- 上游失败、超时、取消后资源能清理，错误和日志不泄漏敏感信息。
- 写操作的测试使用可控目标，不对真实业务重复产生副作用。

需要回归网关全链路时运行 `uv run python tests/run.py`，它会创建临时 Compose 基础设施并执行后端及浏览器验收；所需依赖和 Chromium 安装见 [README](../README.md)。

## 8. 失败时按这一顺序定位

| 现象 | 首先检查 |
|---|---|
| check 没发现新工具 | 入口是否正好是 `plugins/<目录>/plugin.py`，是否导出 package，辅助模块是否被入口导入 |
| check 导入失败 | 构建依赖、类型注解、ID 重复、模块循环导入；不要吞掉异常 |
| 启动 artifact mismatch | sync 与 worker 的插件目录/镜像是否一致，是否整批重启 |
| API 找不到工具 | 是否成功同步目录；是否误用了函数名代替框架 ID |
| 绑定保存/启用 422 | 必填配置、密钥引用、字段类型、profile_id 和覆盖值 |
| 管理 API 401/403 | 管理员会话、精确 Origin、CSRF、Cookie Secure 与 HTTPS |
| MCP 404 | 组是否存在并已启用，URL 是否是 `/{group}/mcp` |
| MCP 401/403 | 使用的是该组入站凭据，Key 有效；OAuth audience 是该组完整端点 URL |
| tools/list 缺少工具 | 工具 available/enabled、绑定 enabled、正确组和暴露名称 |
| 工具执行错误 | 业务参数、上游协议和超时；用受控测试复现，不临时关闭异常掩码 |

## 9. 智能体的完成标准与交付说明

交付前逐项确认：

- [ ] 工具声明、配置模型、依赖及必要测试已提交为可审阅文件。
- [ ] check 通过，输入 schema 不包含 runtime、配置或凭据。
- [ ] 在目标部署中完成目录同步和全部 worker 重启，readiness 正常。
- [ ] 绑定的 tool_id、exposed_name、组认证、配置集和启停状态正确。
- [ ] 真实 MCP 客户端成功列出并调用，关键失败路径得到验证。
- [ ] 交付说明包含修改文件、框架 ID、暴露名、组端点、配置字段、执行命令和验证结果，不包含密钥。

如果任务范围只有编写代码，或缺少目标环境/管理员凭据，则完成可执行的本地检查，提供准确的部署与绑定步骤，并明确哪些步骤尚未执行。不要把“插件本地可导入”描述成“已在目标网关注册并调用成功”。
