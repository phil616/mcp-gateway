# CSA 上游资料

此处保留第三方服务的接口资料快照，供本插件适配和契约生成使用；不是 MCP 网关管理 API 文档，也不表示全部接口已暴露为工具。

- [插件接入指南](../README.md)：实际支持范围、认证、返回结果和维护命令。
- [OpenAPI](openapi.json)：生成器 `scripts/generate_csa.py` 的输入。
- [接口索引](API_DOCUMENTATION.md)、[接口参考](API_REFERENCE.md)、[行为说明](API_BEHAVIOR.md)、[上游示例](API_EXAMPLES.md)：上游全量资料，含本插件未开放的管理员功能。
- [历史只读验收](reports/csa-live-2026-09-29.md)：当时的测试记录，不证明当前服务状态。

快照未附带上游源码 `app/schemas/` 或 `data-export-fields.md`。这些原文引用属于上游仓库，已标记为未收录，不应解析为本网关文件。上游 Markdown 与 OpenAPI 如有差异，生成逻辑以本地 OpenAPI 和适配器实现为准；无法据此确认线上服务已经采用同一版本。
