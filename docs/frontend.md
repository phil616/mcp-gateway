# 管理端界面与帮助说明

管理端使用 Ant Design 6 作为统一 UI 库，配合官方 `@ant-design/icons`、React Router 和 TanStack Query。通过 Tailwind CSS 4 的 Vite 插件，处理页面栅格、间距和响应式布局；仅加载 theme 与 utilities，不引入 Preflight，避免覆盖 Ant Design 的组件样式。依赖版本固定在 package.json 和 package-lock.json。

## 页面使用

- **入门指南 `/guide`**：解释 MCP、工具、组、绑定的关系，提供从部署工具到客户端调用的五步流程，区分入站访问密钥和出站上游密钥。
- **资源页**：标题下展示资源用途；展开“使用说明”查看生效条件、配置优先级或认证要求。空列表提供下一步提示，失败可以刷新重试。
- **组详情**：优先显示端点 URL、启停状态、认证方式与有效工具。客户端配置示例可以展开并复制；不同客户端仍需遵循自身配置格式。
- **编辑抽屉**：说明当前操作的影响，保留原有 schema 配置表单。遇到版本冲突时保留输入，并提示刷新后重新编辑。
- **手机端**：顶部按钮打开导航抽屉，宽表格在容器内滚动。

帮助内容位于 `frontend/src/guidance.tsx` 和 `frontend/src/guide-details.tsx`，更新网关机制时应同步修改。Ant Design 全局主题与中文 locale 在 `main.tsx` 中配置；Tailwind 用于布局，组件外观优先通过 Ant Design token 调整。

## 验证

```sh
npm --prefix frontend ci
npm --prefix frontend run build
uv run python tests/run.py
```

完整测试运行临时数据库、Redis 和双 worker 后端，验证浏览器创建配置与绑定后由真实 MCP 客户端调用。`frontend/e2e/guidance.spec.ts` 使用 API fixtures 单独验证帮助内容、移动端导航、空状态、失败重试、未知路由和版本冲突，不将这些 fixture 测试视为后端验证。

如果系统 inotify 资源不足，使用 `npm --prefix frontend run build` 后执行 `npm --prefix frontend run preview`，无需调整宿主机 watcher 限额。

技术参考：[Ant Design 主题](https://ant.design/docs/react/customize-theme/)、[Tailwind Vite 集成](https://tailwindcss.com/docs/installation/using-vite)。

生产包体积以当前 `npm --prefix frontend run build` 输出为准；共享组件和编辑器的体积需要结合实际加载路径评估。

## ID 推荐、批量绑定与时间选择

新建表单在稳定 ID 下方提供可点击候选：端点组包含客服、数据分析、自动化场景；绑定结合组与工具；访问密钥结合所属组；其他资源按开发/生产配置或凭据用途推荐。推荐避开已加载的同类 ID，但不预占名称，保存时服务端仍检查冲突。候选不会自动覆盖手工输入，创建后 ID 仍不可修改。

工具绑定列表与组详情提供“批量绑定”：先选择目标组，再选择最多 200 个尚未绑定且代码可用的工具，逐项检查推荐 ID、暴露名称、配置集和覆盖值。默认整批保存为禁用草稿；打开“创建后启用全部绑定”时，每项必须满足配置要求。后端使用同一事务提交，失败时整批回滚，抽屉保留输入供修正。

访问密钥的到期时间使用日期时间选择器，支持 7、30、90 天快捷选择及“不过期”。界面显示浏览器本地时区，提交时转换为带 UTC 时区的 ISO 时间；禁止保存已经过去的到期时间。清空日期表示不过期。

工具绑定抽屉支持“工具 ID 前缀”，例如 `demo.`，按开头匹配并加入当前选择，自动跳过已绑定和不可用工具；合计超过 200 项时需缩小前缀范围。选择不会直接写入，确认“创建 N 个绑定”后才提交。

资源列表（工具目录和审计除外）支持跨页勾选批量删除。切换资源或筛选条件会清空选择；删除前显示分页确认列表。有引用时展示可滚动、分页的引用表格，长 ID 自动换行。必须先解除引用才能删除，版本冲突时整批回滚。
