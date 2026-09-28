import { Alert, Card, Collapse, Steps, Tag, Typography } from "antd";
import { Link } from "react-router-dom";
import {
  GuideScenarios,
  GuideConnections,
  GuideChecklist,
} from "./guide-details";

export const guidance: Record<
  string,
  { summary: string; detail: string; empty: string }
> = {
  tools: {
    summary: "从本地 Python 插件发现的工具，是智能体可调用的能力。",
    detail:
      "先由开发者部署插件并同步目录，再在端点组中创建绑定。目录里的工具不会自动对外开放；全局禁用会影响所有组，代码不可用时也无法调用。",
    empty: "尚未发现工具，请先部署插件并运行目录同步命令。",
  },
  groups: {
    summary: "为不同应用组合工具，每个组提供一个独立 MCP 地址。",
    detail:
      "创建组 → 添加工具绑定 → 配置认证 → 启用组 → 将端点 URL 填入客户端。组和绑定默认禁用；未选择认证配置时，启用后的端点为公开访问。",
    empty: "创建第一个端点组，为你的智能体准备工具入口。",
  },
  bindings: {
    summary: "把目录中的工具加入指定组，并配置名称和运行参数。",
    detail:
      "MCP 暴露名称是客户端看到的名称，在同一组内必须唯一。同一工具可以服务多个组，各自使用独立配置。工具、绑定和组均启用且代码可用时，客户端才能发现并调用它。",
    empty: "还没有工具绑定。选择一个工具，并为它设置客户端可见的名称。",
  },
  "config-profiles": {
    summary: "复用工具运行配置，例如服务地址、默认参数与密钥引用。",
    detail:
      "优先级：工具默认值 → 配置集 → 绑定覆盖值，后者覆盖前者。同一字段整体替换，不做深层合并。修改共享配置集会校验所有启用的引用绑定，任何一个不通过都不会保存。",
    empty: "暂时没有配置集。多个绑定需要相同参数时，可以在这里集中管理。",
  },
  secrets: {
    summary: "保存工具访问上游服务时使用的 API Key、密码等凭据。",
    detail:
      '这是工具访问外部服务的出站凭据，不是客户端连接网关的访问密钥。保存后无法读取原文；在配置中通过 {"$secret":"密钥ID"} 引用，不要把凭据直接写入普通配置字段。',
    empty: "尚未保存上游密钥。仅在工具需要外部服务凭据时创建。",
  },
  "auth-profiles": {
    summary: "决定谁可以连接端点组：公开、静态访问密钥或外部 OAuth。",
    detail:
      "公开模式无需凭据；静态模式使用所属组的 Bearer Key；OAuth 模式验证外部身份服务签发的令牌。创建认证配置后，还需要在组中选用。网关自身不签发 OAuth 令牌，也不提供授权登录页面。",
    empty: "暂无认证配置。需要限制端点访问时，先选择一种认证方式。",
  },
  "access-keys": {
    summary: "供智能体或 MCP 客户端连接指定组的静态 Bearer 凭据。",
    detail:
      "只有组使用静态认证时才会验证这些密钥；密钥不能跨组使用。创建和轮换时只展示一次，轮换立即撤销旧密钥。请在客户端的安全凭据设置中配置 Authorization: Bearer <密钥>。",
    empty: "暂无访问密钥。先为组选择静态认证配置，再创建该组的密钥。",
  },
  audit: {
    summary: "查看谁在何时修改了网关配置。",
    detail:
      "这里记录管理变更，不是工具调用历史。配置变更与审计一起提交；不会在这里记录工具参数、返回正文或凭据。",
    empty: "暂无审计记录，后续管理变更会显示在这里。",
  },
};
export function ResourceHelp({ resource }: { resource: string }) {
  const info = guidance[resource];
  return info ? (
    <Collapse
      className="resource-help"
      size="small"
      items={[
        {
          key: "help",
          label: "使用说明",
          children: (
            <Typography.Paragraph className="mb-0">
              {info.detail}
            </Typography.Paragraph>
          ),
        },
      ]}
    />
  ) : null;
}
export function GuidePage() {
  return (
    <div className="guide-page flex flex-col gap-6">
      <div className="guide-hero">
        <Tag color="blue">入门指南</Tag>
        <Typography.Title level={2}>
          让智能体通过一个地址使用工具
        </Typography.Title>
        <Typography.Paragraph>
          MCP 是智能体与工具沟通的标准协议。网关将开发者编写的 Python
          函数组织为可访问的端点，客户端连接后可以发现工具并发起调用。
        </Typography.Paragraph>
      </div>
      <nav aria-label="指南章节" className="guide-toc">
        <a href="#guide-basics">基本流程</a>
        <a href="#guide-scenarios">场景与操作步骤</a>
        <a href="#guide-clients">客户端配置</a>
        <a href="#guide-checklist">上线与变更</a>
        <a href="#guide-troubleshooting">问题排查</a>
      </nav>
      <Alert
        showIcon
        type="info"
        title="开始前需要准备什么"
        description="本指南面向管理控制台的使用者。你需要能登录的管理员账号、可用的后端服务，以及至少一个已部署并同步的工具。管理员账号用于管理网页；MCP 客户端使用组的认证方式，不使用管理员登录密码。"
      />
      <Card id="guide-basics" title="从工具到一次调用">
        <Steps
          orientation="vertical"
          items={[
            {
              title: "确认工具已就绪",
              content: (
                <span>
                  开发者部署插件并同步目录。在 <Link to="/tools">工具目录</Link>{" "}
                  查看可用能力和参数。
                </span>
              ),
            },
            {
              title: "创建应用自己的端点组",
              content: (
                <span>
                  在 <Link to="/groups">端点组</Link> 创建稳定 ID，例如
                  support；它对应 /support/mcp。先保持禁用。
                </span>
              ),
            },
            {
              title: "绑定工具并提供配置",
              content: (
                <span>
                  在组详情添加绑定。按需创建 <Link to="/secrets">上游密钥</Link>{" "}
                  和 <Link to="/config-profiles">配置集</Link>
                  ，校验配置后启用绑定。
                </span>
              ),
            },
            {
              title: "选择认证并启用组",
              content: (
                <span>
                  在 <Link to="/auth-profiles">认证配置</Link>{" "}
                  选择访问方式，再编辑组进行关联。静态认证还需创建{" "}
                  <Link to="/access-keys">访问密钥</Link>。
                </span>
              ),
            },
            {
              title: "连接并验证",
              content:
                "复制组详情中的端点 URL 到支持 Streamable HTTP 的 MCP 客户端，配置对应凭据，刷新工具列表并调用。不同客户端的配置格式可能不同。",
            },
          ]}
        />
      </Card>
      <div className="grid gap-4 md:grid-cols-3">
        <Card title="工具：能做什么">
          <p>
            例如查询订单。工具 ID
            对应代码定义；客户端无法填写工具的注入配置或密钥。
          </p>
          <Link to="/tools">查看工具目录 →</Link>
        </Card>
        <Card title="组：给谁使用">
          <p>
            例如客服助手的 support
            端点。不同组可以复用同一工具，并使用不同凭据。
          </p>
          <Link to="/groups">管理端点组 →</Link>
        </Card>
        <Card title="绑定：如何使用">
          <p>
            选择组内的工具名称、配置集与覆盖值。新增目录工具不会自动加入已有组。
          </p>
          <Link to="/bindings">管理工具绑定 →</Link>
        </Card>
      </div>
      <Card title="分清两种密钥">
        <div className="grid gap-6 md:grid-cols-2">
          <div>
            <Tag color="purple">客户端 → 网关</Tag>
            <h3>访问密钥</h3>
            <p>证明客户端有权访问某个组。由网关生成，创建时仅展示一次。</p>
          </div>
          <div>
            <Tag color="cyan">网关工具 → 上游服务</Tag>
            <h3>上游密钥</h3>
            <p>
              例如订单服务的 API
              Key。由管理员保存，再通过配置引用注入工具；客户端令牌不会被透传给上游。
            </p>
          </div>
        </div>
      </Card>
      <GuideScenarios />
      <GuideConnections />
      <GuideChecklist />
      <Card id="guide-troubleshooting" title="常见问题">
        <Collapse
          ghost
          items={[
            {
              key: "file",
              label: "出现 The argument 'file' cannot be empty 怎么办？",
              children:
                "这通常表示客户端试图启动一个空的本地命令。检查是否误用 stdio：OpenCode 需要 type: remote，Claude Code 和 VS Code 需要 type: http。删除不适用的 command、args 字段，按上方对应客户端示例保存并重新连接。这里的 file 不是工具参数，不需要给工具补文件路径。",
            },
            {
              key: "unauthorized",
              label: "401、403 或 Invalid access token 应该检查什么？",
              children:
                "先区分出错位置。MCP 静态端点：检查 Authorization 是否为 Bearer 加空格加完整密钥，密钥是否属于当前组、是否过期或已撤销；不能填写上游密钥、密钥 ID、管理员密码或示例占位符。OAuth 端点：检查令牌有效期、issuer、完整端点 audience 和必要 scope。管理页面：401 通常需要重新登录，403 则需检查访问域名及 CSRF；不要用 MCP 访问密钥替代网页登录。",
            },
            {
              key: "network",
              label: "无法连接、404 或 API 返回 400，但不知道原因？",
              children:
                "确认请求发往后端地址，组 ID 和 /mcp 路径正确，并且组已启用；远程客户端不要使用指向自己机器的 localhost。管理页面报错时记录页面显示的 HTTP 状态和请求编号，用编号查后端日志；若浏览器提示网络或 CORS 错误，请部署人员核对控制台域名、API 地址和允许来源。不要仅凭 400 判断是工具执行失败。",
            },
            {
              key: "validation",
              label: "绑定无法启用，或配置集修改失败？",
              children:
                "在工具详情查看配置 schema，核对必填项和字段类型，再检查绑定选择的配置集、覆盖值及密钥引用是否存在。对绑定执行校验，按错误修正后再启用。共享配置集更新失败时，需要修正所有受影响的启用绑定；不要反复提交同一份无效配置。",
            },
            {
              key: "conflict",
              label: "保存提示 409 版本冲突怎么办？",
              children:
                "该记录可能已被另一个管理员或浏览器标签页修改。先记下尚未保存的内容，重新加载最新记录，核对差异后再编辑提交，避免覆盖他人的修改。",
            },
            {
              key: "timeout",
              label: "工具能列出，但调用失败或超时？",
              children:
                "先按工具参数 schema 检查本次输入，再检查上游服务连通性和配置凭据。让部署人员通过请求编号、组和工具名称查看后端日志。超时并不保证同步工具已经停止，也不撤销外部副作用；涉及写入、发信或下单时，先确认结果再决定是否重试。演示 demo.wait 的超时是 0.2 秒，连通测试请使用 seconds: 0。",
            },
            {
              key: "missing",
              label: "连接成功，为什么没有工具？",
              children:
                "依次检查：组已启用、绑定已启用、工具全局已启用且代码可用。保存后让客户端重新获取工具列表；网关不主动广播工具列表更新。",
            },
            {
              key: "changes",
              label: "修改配置后，什么时候生效？",
              children:
                "组、绑定、配置和访问权限的变更从后续请求生效；已经开始的调用继续使用原配置。插件代码的变化则需要同步目录并重启部署。",
            },
            {
              key: "oauth",
              label: "选择 OAuth 就能让所有客户端登录吗？",
              children:
                "不能直接保证。网关仅验证令牌，令牌的 audience 必须包含完整组端点 URL，并满足必要 scope。标准客户端的完整授权还依赖外部身份服务的发现、PKCE、资源标识和客户端注册能力，可在认证配置中运行兼容检查。",
            },
            {
              key: "delete",
              label: "为什么配置或密钥无法删除？",
              children:
                "仍有对象引用它。删除前先查看依赖并修改相应绑定或认证配置，避免破坏正在使用的工具。",
            },
          ]}
        />
      </Card>
      <Alert
        showIcon
        type="info"
        title="先用测试组验证"
        description="建议先绑定一个简单工具，完成客户端发现与调用，再逐步增加工具和上游服务配置。"
      />
    </div>
  );
}
