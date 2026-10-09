# 插件目录

本目录是网关的扩展层。业务接口、上游认证和第三方服务资料在各插件内维护；网关只通过 [SDK 契约](../docs/plugins.md) 加载工具。

| 插件 | 类型 | 入口与说明 |
| --- | --- | --- |
| demo | 网关 SDK 示例，配置注入和同步超时 | [源码](demo/plugin.py)，[快速开始](../README.md) |
| emailutils | 本地邮箱语法工具，不连接邮件服务 | [说明](emailutils/README.md) |
| csa | 第三方 CSA API 适配 | [接入指南](csa/README.md) |
| storage | 第三方网盘 API 适配 | [接入指南](storage/README.md) |

默认镜像包含上述插件，但同步只将工具加入目录，不会自动创建组或绑定。插件的上游 API `/api/...` 与网关管理 API `/api/v1/...` 属于不同服务，调用时应分别使用对应服务的地址和凭据。

## 按需部署

网关本身不要求安装某个业务插件。可将所需插件子目录复制到独立根目录，使用 `gateway plugins check --path /实际目录` 检查，并为同步命令与全部 worker 设置同一个 `PLUGINS_PATH`。保留插件相对导入依赖；网关 Python 依赖和插件额外依赖需要在构建阶段安装。

默认 Dockerfile 复制整个 plugins 目录，默认 Compose 没有插件选择开关。容器部署时需在自定义镜像或 Compose override 中挂载选定根目录，并为 backend、sync（以及执行检查的服务）设置相同路径。不要仅同步某个插件的临时目录到仍运行完整制品的数据库；未包含的工具会标记不可用，指纹也会改变。

变更插件集合时使用[整批发布流程](../docs/agent-tool-guide.md#5-先做本地检查再部署代码)。已有绑定不会因删除代码而被删除。上游资料仅供开发维护，运行时适配器使用生成的 `contract.py`。
