# 本地邮箱工具

本插件执行邮箱字符串解析和语法检查。实际工具签名及返回字段见 [plugin.py](plugin.py)，测试见 [test_emailutils.py](../../tests/test_emailutils.py)。不访问 DNS、SMTP 或其他上游，不证明邮箱存在或可以投递。

使用网关通用的[工具绑定流程](../../docs/agent-tool-guide.md#6-将工具绑定到组)，从目录选择 `emailutils.*` 工具。无上游凭据配置；参数和 schema 以管理工具目录为准。

离线验证：`uv run pytest -q tests/test_emailutils.py`。
