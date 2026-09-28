# 插件契约

编码智能体执行新增工具任务时，使用 [新增工具与网关注册指南](agent-tool-guide.md) 按步骤完成编写、部署、绑定和验收。

每个插件固定入口为 `plugins/<package>/plugin.py`，导出 `package`。只扫描入口，普通辅助模块由插件自行导入；目录会加入 Python 模块查找路径，支持包内相对导入。入口应只声明工具，不连接外部服务、不执行工具。插件运行在网关进程中，必须可信。

```python
from pydantic import BaseModel, SecretStr
from gateway_sdk import ToolPackage, ToolRuntime, Depends, current_runtime
import httpx

package = ToolPackage(id="weather", version="1.0.0")

class WeatherConfig(BaseModel):
    model_config = {"extra": "forbid"}
    base_url: str
    api_key: SecretStr

@package.tool(id="forecast", config_model=WeatherConfig, timeout=10)
async def forecast(city: str, runtime: ToolRuntime = Depends(current_runtime)) -> dict:
    config = runtime.config(WeatherConfig)
    async with httpx.AsyncClient(timeout=8) as client:
        result = await client.get(
            config.base_url + "/forecast",
            params={"city": city},
            headers={"Authorization": "Bearer " + config.api_key.get_secret_value()},
        )
        result.raise_for_status()
        return result.json()
```

框架 ID 为 `weather.forecast`，绑定的 `exposed_name` 是客户端可见名称。包 ID、工具 ID 稳定且唯一；所有参数和返回值必须有类型注解。`Depends` 来自 FastMCP 的依赖注入系统，不是 FastAPI 的同名对象。FastMCP 负责业务参数校验、schema 和结果编码，注入参数不进入 MCP schema。

`runtime.group` 是当前组；`runtime.call_id` 是本次调用 ID；`runtime.config(Model)` 返回绑定的类型化配置副本。配置合并采用字段级浅覆盖：模型默认值 → 配置集 → 绑定 overrides。嵌套对象作为整个字段替换，不进行隐式深合并。字符串不会被展开成环境变量或模板。

`SecretStr` / `SecretBytes` 字段必须使用 `{"$secret":"id"}` 引用；对象、列表中的引用递归解析。管理 API 不返回解密后的密钥。配置模型错误只返回字段路径，避免 Pydantic 的输入值泄漏凭据。草稿绑定允许不完整；启用时必须验证通过。共享配置集更新会验证全部有效绑定，失败则回滚。

`async def` 必须使用异步 I/O。`def` 工具由 FastMCP 在线程池中执行，网关按 `THREAD_LIMIT` 限制在执行的同步工具调用。排队时间计入超时；排队中超时的调用不会开始执行。正在执行的同步线程超时后仍占用容量直到结束，不能被强制终止，也不能回滚外部副作用。异步调用超时时取消任务；插件要在 `finally` 或上下文管理器中释放资源。所有工具应自行设置上游网络超时。长期不退出的同步函数会拖延进程优雅关闭，应由进程管理器最终终止。

不要把 Agent Bearer token 发送给上游，不要将凭据写入 `os.environ` 或全局客户端。带凭据的客户端按调用创建和关闭。工具错误对客户端统一掩码，日志只记录请求 ID、组、工具、耗时和结果状态；插件自身也应遵守日志规范。

发布流程：构建镜像时安装依赖 → `gateway plugins check` → 停止旧 worker → 迁移 → `gateway plugins sync` → 启动所有相同镜像的 worker。目录指纹覆盖插件目录全部 `.py` 文件。同步失败（导入、重复 ID、缺失依赖、已有有效绑定不兼容）会回滚。删除工具代码后，历史目录记录及绑定保留，`available=false`，不能调用或创建新绑定。

SDK 单独打包：`uv build sdk`。后端根包也包含 SDK，便于统一镜像部署；不要在同一环境同时安装两个提供同名模块的发行包。

实现采用 [FastMCP Provider](https://gofastmcp.com/python-sdk/fastmcp-server-providers-__init__) 和 [依赖注入](https://gofastmcp.com/servers/dependency-injection)。
