# MCP 网关文档

网关将可信 Python 插件中的工具按组发布为独立 MCP HTTP 端点，提供管理、认证、配置注入和执行控制。本目录只描述通用网关能力。

| 阅读任务 | 文档 |
| --- | --- |
| 首次启动并调用工具 | [项目 README](../README.md) |
| 理解模块、数据关系和请求生命周期 | [架构与边界](architecture.md) |
| 配置环境变量与部署入口 | [配置参考](configuration.md) |
| 发布、备份、健康检查和排错 | [部署指南](deployment.md) |
| 登录控制台、管理工具和组 | [前端指南](frontend.md) |
| 自动化管理资源 | [管理 API](api.md)、[OpenAPI 快照](openapi.json) |
| 管理员、组访问和上游凭据 | [认证](auth.md) |
| 编写插件与接入工具 | [插件契约](plugins.md)、[执行指南](agent-tool-guide.md) |
| 重现检查与验收 | [验证指南](verification.md) |

第三方业务说明、上游 API 契约和插件专属验收归入 [插件目录](../plugins/README.md)；业务场景及历史证据归入 [场景目录](../scenarios/README.md)。第三方服务的路由、账号和权限不属于网关管理 API。

## 维护约定

修改功能时同步对应文档：环境变量以 `backend/gateway/settings.py` 和 `compose.yml` 为准；管理请求以 `app.py`、`contracts.py`、`service.py` 为准；插件接口以 SDK 和目录加载器为准；页面行为以 `frontend/src/` 为准。依赖版本以锁文件为准。

API 路由或模型变化后更新 OpenAPI 快照，命令见验证指南。新增第三方插件时将接入说明放在 `plugins/<name>/README.md`，上游资料放在其 `docs/` 下，并在插件目录登记。上游原始资料应注明适用范围及未随仓库提供的引用，不能作为网关实现说明。

历史报告只说明当时的运行结果；验证指南说明当前如何重现检查，不以历史通过数代替当前测试结果。所有文档命令默认从仓库根目录执行，另有说明除外。
