import { Alert, Card, Collapse, Steps, Tabs, Typography } from "antd";
import { Link } from "react-router-dom";

const steps = (items: string[]) => (
  <Steps
    orientation="vertical"
    items={items.map((content, index) => ({
      title: `第 ${index + 1} 步`,
      content,
    }))}
  />
);

export function GuideScenarios() {
  return (
    <Card id="guide-scenarios" title="按场景操作">
      <Typography.Paragraph type="secondary">
        先完成一个简单工具的调用，再选择适合你的场景。下面的 ID
        和名称是示例；若已被占用，可以选择表单推荐的其他值，并同步替换后续步骤中的引用。
      </Typography.Paragraph>
      <Collapse
        defaultActiveKey={["first"]}
        items={[
          {
            key: "first",
            label: "场景一：第一次接入，让智能体调用一个测试工具",
            children: (
              <>
                <p>
                  目标：不配置上游服务，先验证客户端、认证和工具调用是否连通。需要管理员已部署示例插件；目录中没有
                  demo.wait 时，请联系部署人员，Web 页面不能上传或安装插件。
                </p>
                {steps([
                  "打开工具目录，找到 demo.wait，确认代码可用且工具已全局启用。它接收 seconds 参数，不需要配置集或上游密钥。",
                  "打开端点组，点击创建，稳定 ID 填 sandbox（或选择未占用的推荐值），先保持禁用。组 ID 会成为 /sandbox/mcp 地址的一部分，创建后不可修改。",
                  "进入 sandbox 组详情添加绑定，选择 demo.wait，MCP 暴露名称填 wait，启用绑定并保存。绑定的稳定 ID 是管理记录标识，不是客户端调用名称。",
                  "在认证配置中新建静态认证配置，再编辑 sandbox 组，在入站认证字段选择它。在访问密钥页面为 sandbox 创建密钥，立即保存弹窗中的完整原文。",
                  "确认绑定可用后启用组。展开组详情的客户端连接配置示例，选择你的客户端，复制配置并替换访问密钥占位符。",
                  "保存客户端配置并重新连接。先查看工具列表应包含 wait，再要求智能体调用 wait，seconds 填 0；预期工具返回 done。客户端可能给工具名称添加服务器名前缀。",
                ])}
                <Alert
                  className="mt-3"
                  type="info"
                  showIcon
                  title="如何判断成功"
                  description="客户端能列出工具，只证明发现成功；看到本次调用返回 done，才说明调用链路也已走通。不要用浏览器直接打开 MCP 地址作为调用测试。"
                />
              </>
            ),
          },
          {
            key: "isolation",
            label: "场景二：两个应用复用同一工具，但使用不同配置和凭据",
            children: (
              <>
                <p>
                  目标：为 support 和 sales 两个组绑定
                  demo.echo，分别返回不同前缀。demo.echo 的 api_key
                  是演示用配置，不会请求真实上游，也不会把密钥返回给客户端。
                </p>
                {steps([
                  "在上游密钥中新建 support-key 和 sales-key，分别保存两个测试值。真实业务应填写对应上游服务签发的 API Key；这里不是创建网关访问密钥。",
                  "创建配置集 support-config：prefix 填 Support，api_key 使用密钥引用 support-key。再创建 sales-config：prefix 填 Sales，api_key 引用 sales-key。配置集使用 JSON 编辑时可参考下方示例。",
                  "创建 support 和 sales 两个组，分别绑定 demo.echo，MCP 暴露名称均可填 echo，因为名称只要求在各自组内唯一。分别选择 support-config 和 sales-config，不填写绑定覆盖值。",
                  "为两个组关联静态认证配置，分别创建所属组的访问密钥。两个组可以复用同一个静态认证配置，但访问密钥不能跨组使用。校验配置后启用绑定和组。",
                  "分别连接两个端点，调用 echo，业务参数填 message: world。support 应返回 message: Support world、group: support；sales 应返回 message: Sales world、group: sales。客户端不需要也不能填写 api_key。",
                ])}
                <Typography.Paragraph
                  copyable={{
                    text: JSON.stringify(
                      {
                        prefix: "Support",
                        api_key: { $secret: "support-key" },
                      },
                      null,
                      2,
                    ),
                  }}
                >
                  <pre className="json">
                    {JSON.stringify(
                      {
                        prefix: "Support",
                        api_key: { $secret: "support-key" },
                      },
                      null,
                      2,
                    )}
                  </pre>
                </Typography.Paragraph>
                <p>
                  配置解析顺序为工具默认值 → 配置集 → 绑定覆盖值。例如某个绑定把
                  prefix 覆盖为 VIP，它会返回 VIP
                  world，其他绑定仍继承原配置集。取消该字段的覆盖即可恢复继承；空字符串是一个实际值，不等于取消覆盖。嵌套字段整体替换，不做深层合并。
                </p>
              </>
            ),
          },
          {
            key: "batch",
            label: "场景三：为一个助手一次性添加多个工具",
            children: (
              <>
                {steps([
                  "先在工具目录确认需要的工具及其配置要求，再进入目标组详情，选择批量绑定。一次最多选择 50 个工具，批量操作面向同一个组。",
                  "勾选要添加的工具，逐项检查 MCP 暴露名称。名称在组内必须唯一；遇到冲突时改用清晰别名，例如 orders_lookup。同一组不能重复绑定同一工具。",
                  "逐项选择配置集并填写覆盖值。不同工具的配置模型可能不同，不要把同一个配置集无条件套用于所有工具。需要上游密钥的工具，先准备好密钥引用。",
                  "默认以禁用草稿创建，提交后逐项补齐并校验配置，再启用。若创建时就选择启用，必须已经满足工具的配置要求。",
                  "批量提交是一个事务：任意一项失败，整批不会创建。根据错误修改后再次提交，不必清理半批记录。保存成功后，让客户端重新获取工具列表。",
                ])}
              </>
            ),
          },
          {
            key: "rotation",
            label: "场景四：更换客户端、设置有效期或轮换访问密钥",
            children: (
              <>
                {steps([
                  "进入访问密钥页面，确认所属组。有效期可用日期时间选择器或快捷选项填写；界面按本地时间展示，提交时转换为 UTC。不设置有效期表示不会因时间自动失效。",
                  "为不同客户端分别创建密钥，便于单独撤销。新密钥原文只在创建弹窗显示一次，应立即保存到对应客户端凭据设置中。",
                  "需要立即替换旧密钥时使用轮换。轮换成功会立即撤销旧密钥，因此需要马上更新客户端 Authorization 并重新连接。",
                  "若希望留出迁移时间，先额外创建一把同组密钥，更新并验证客户端后，再撤销旧密钥。密钥丢失时无法回读原文，只能新建或轮换。",
                ])}
                <p>
                  轮换访问密钥不会更换上游 API
                  Key。更换上游凭据应在上游密钥页面更新对应对象；共享该引用的绑定会在后续请求中使用新值。已经开始的调用继续使用原配置快照。
                </p>
              </>
            ),
          },
          {
            key: "oauth",
            label: "场景五：接入已有企业身份服务（OAuth）",
            children: (
              <>
                <p>
                  适合已经有身份服务和客户端接入方案的团队。需要身份服务管理员提供
                  issuer、JWKS 或 introspection 验证信息、必要
                  scopes，并支持为完整组端点 URL 签发令牌。
                </p>
                {steps([
                  "先确定最终对外端点，例如 https://mcp.example.com/support/mcp。该完整 URL 是资源标识和 audience；域名、路径变化后要同步调整身份服务和客户端配置。",
                  "创建 OAuth 认证配置，选择 JWT 或 introspection 验证方式，填写身份服务参数和必要 scopes，再运行兼容检查。JWT 需要验证签名、issuer、audience、有效期及 scope；不透明令牌需要有效的 introspection 响应。",
                  "在测试组关联该认证配置并启用，使用支持 OAuth 的客户端连接。选择组详情对应客户端的示例，不要填写组静态访问密钥；OpenCode 的 OAuth 配置不能设置 oauth: false。",
                  "完成外部身份服务授权后列出并调用工具。兼容检查不能替代实际登录测试，还应验证过期令牌、错误 audience 和不足 scope 都被拒绝。",
                ])}
                <Alert
                  type="info"
                  showIcon
                  title="令牌验证与完整登录是两件事"
                  description="网关是资源服务器，不提供账号登录页面或签发令牌。完整客户端授权还依赖外部身份服务的发现、PKCE、资源标识和客户端注册能力；仅能验证 Bearer token 不代表任何 MCP 客户端都能完成登录。"
                />
              </>
            ),
          },
        ]}
      />
    </Card>
  );
}

export function GuideConnections() {
  const endpoint = {
    url: "http://localhost:8000/sandbox/mcp",
    headers: { Authorization: "Bearer <YOUR_GROUP_ACCESS_KEY>" },
  };
  const clients = [
    {
      key: "opencode",
      label: "OpenCode",
      file: "opencode.json",
      config: {
        mcp: { sandbox: { type: "remote", ...endpoint, oauth: false } },
      },
      note: "合并到项目的 opencode.json 中，保留已有配置。运行 opencode mcp list 检查状态；静态密钥模式设置 oauth: false，避免进入 OAuth 授权流程。",
    },
    {
      key: "claude",
      label: "Claude Code",
      file: ".mcp.json",
      config: { mcpServers: { sandbox: { type: "http", ...endpoint } } },
      note: "合并到项目的 .mcp.json 中，再重新连接 MCP 服务。必须保留 type: http，不能只填写 url。",
    },
    {
      key: "vscode",
      label: "VS Code",
      file: ".vscode/mcp.json",
      config: { servers: { sandbox: { type: "http", ...endpoint } } },
      note: "合并到工作区的 .vscode/mcp.json 中，再启动或重启该 MCP 服务。顶层字段是 servers，不是 mcpServers。",
    },
  ];
  return (
    <Card id="guide-clients" title="客户端接入：选择正确的配置格式">
      <p>
        以下均为静态认证示例。实际使用时优先复制组详情生成的配置，把地址换成真实端点，把占位符整体替换为该组访问密钥原文，保留
        Bearer
        后的一个空格。若配置文件已有其他服务，只合并新条目，不覆盖整个文件。
      </p>
      <Tabs
        items={clients.map((client) => ({
          key: client.key,
          label: client.label,
          children: (
            <>
              <Typography.Text strong>{client.file}</Typography.Text>
              <p>{client.note}</p>
              <Typography.Paragraph
                copyable={{ text: JSON.stringify(client.config, null, 2) }}
              >
                <pre className="json code-block">
                  {JSON.stringify(client.config, null, 2)}
                </pre>
              </Typography.Paragraph>
            </>
          ),
        }))}
      />
      <Alert
        type="info"
        showIcon
        title="地址要从客户端所在的位置判断"
        description="localhost 指运行客户端的那台机器或容器。客户端在另一台电脑、远程服务器或容器内时，应使用它能够访问的网关域名或地址。MCP 客户端连接的是后端组地址（如 :8000/sandbox/mcp），不是管理控制台（如 :5173），也不是 /api/v1。"
      />
      <p className="mt-3">
        其他客户端请选择远程 HTTP / Streamable HTTP，并按照其界面设置 URL 和
        Authorization 请求头。不要填本地启动命令；只支持 stdio
        的客户端不能直接连接这个 HTTP 端点。公开组不需要认证头；OAuth
        组应按外部授权流程连接。
      </p>
    </Card>
  );
}

export function GuideChecklist() {
  return (
    <Card id="guide-checklist" title="上线前检查与日常变更">
      <ul>
        <li>
          确认地址和认证：组关联了预期认证配置。未选择认证配置的启用组是公开的；保存一个认证配置并不会自动把它关联到组。
        </li>
        <li>
          确认工具范围：组详情的有效工具只包含该应用需要的能力。目录中新增工具不会自动对外暴露，需要创建绑定。
        </li>
        <li>
          确认配置来源：必填字段齐全，密钥以引用方式配置。调用参数是每次任务传入的内容，配置集是管理员预先设置的运行环境，两者用途不同。
        </li>
        <li>
          确认真实调用：用目标客户端先列出工具，再调用一个可预期结果的工具；不要仅根据“配置保存成功”判断接入成功。
        </li>
        <li>
          确认影响范围：禁用绑定只影响该组中的工具；全局禁用工具会影响所有组；禁用组会阻止该端点的访问。
        </li>
        <li>
          修改共享配置集前检查依赖。系统会校验受影响的启用绑定，任何一项不通过都会拒绝整次更新。删除仍被引用的配置或密钥时，也需要先解除依赖。
        </li>
      </ul>
      <p>
        组和配置修改从后续请求生效，已开始的调用使用原快照。客户端需要重新获取工具列表才能看到工具增删；新增或修改
        Python 插件代码则需要开发者部署、同步目录并重启。
      </p>
      <p>
        管理变更可在 <Link to="/audit">审计日志</Link>{" "}
        追踪。工具调用诊断查看后端日志；审计页面不保存工具输入和返回正文。
      </p>
    </Card>
  );
}
