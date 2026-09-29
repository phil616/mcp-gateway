import { test, expect } from "@playwright/test";

// Fixture tests cover UI states; management.spec.ts uses the real backend and MCP client.
test.beforeEach(async ({ page }) => {
  await page.route("**/api/v1/**", async (route) => {
    const path = new URL(route.request().url()).pathname;
    await route.fulfill({
      json: path.endsWith("/me")
        ? { username: "admin", csrf: "fixture" }
        : { items: [], total: 0 },
    });
  });
});
test("入门说明、资源帮助与空状态提供下一步", async ({ page }) => {
  await page.goto("/guide");
  await expect(
    page.getByRole("heading", { name: "让智能体通过一个地址使用工具" }),
  ).toBeVisible();
  await expect(page.getByText("分清两种密钥", { exact: true })).toBeVisible();
  await page
    .getByRole("button", { name: "连接成功，为什么没有工具？" })
    .click();
  await expect(
    page.getByText("依次检查：组已启用", { exact: false }),
  ).toBeVisible();
  await page.screenshot({
    path: "test-results/guide-desktop.png",
    fullPage: true,
  });
  await page.getByRole("link", { name: "管理端点组 →" }).click();
  await expect(
    page.getByText("创建第一个端点组，为你的智能体准备工具入口。"),
  ).toBeVisible();
  await page.getByRole("button", { name: /使用说明/ }).click();
  await expect(
    page.getByText("创建组 → 添加工具绑定", { exact: false }),
  ).toBeVisible();
  await page.getByRole("button", { name: /^创\s*建$/ }).click();
  await expect(
    page.locator(".ant-drawer").getByText(/启用后的端点为公开访问/),
  ).toBeVisible();
});
test("手机导航可访问所有页面且无横向溢出", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/guide");
  await page.getByRole("button", { name: "打开导航" }).click();
  await page.getByRole("menuitem", { name: /访问密钥/ }).click();
  await expect(
    page.getByRole("heading", { name: "访问密钥", exact: true }),
  ).toBeVisible();
  await expect(page.locator(".ant-drawer")).not.toBeVisible();
  await expect(page.locator(".ant-spin-spinning")).toHaveCount(0);
  await expect
    .poll(() => page.evaluate(() => document.documentElement.scrollHeight))
    .toBe(844);
  await page.screenshot({
    path: "test-results/mobile.png",
    fullPage: true,
    animations: "disabled",
  });
  expect(
    await page.evaluate(
      () => document.documentElement.scrollWidth <= innerWidth,
    ),
  ).toBeTruthy();
});
test("加载失败可重试，未知页面显示引导", async ({ page }) => {
  let failing = true;
  await page.route("**/api/v1/groups?**", (route) =>
    failing
      ? route.fulfill({ status: 503, json: { detail: "暂时无法连接数据库" } })
      : route.fulfill({ json: { items: [], total: 0 } }),
  );
  await page.goto("/groups");
  await expect(page.getByText("加载失败", { exact: true })).toBeVisible();
  failing = false;
  await page.getByRole("button", { name: /刷\s*新/ }).click();
  await expect(page.getByText("加载失败", { exact: true })).toHaveCount(0);
  await page.goto("/unknown-resource");
  await expect(page.getByText("页面不存在", { exact: true })).toBeVisible();
});
test("版本冲突保留编辑内容并提示恢复方法", async ({ page }) => {
  await page.route("**/api/v1/groups?**", (route) =>
    route.fulfill({
      json: {
        items: [{ id: "support", enabled: false, version: 1 }],
        total: 1,
      },
    }),
  );
  await page.route("**/api/v1/groups/support", (route) =>
    route.fulfill({ status: 409, json: { detail: "Version conflict" } }),
  );
  await page.goto("/groups");
  await page.getByRole("button", { name: /^编\s*辑$/ }).click();
  await page.getByLabel("启用", { exact: true }).click();
  await page.getByRole("button", { name: /^保\s*存$/ }).click();
  await expect(page.getByText(/此记录已被其他操作更新/)).toBeVisible();
  await expect(page.getByLabel("启用", { exact: true })).toBeChecked();
  await expect(page.locator(".ant-drawer")).toBeVisible();
});

test("会话请求网络错误不会被吞掉", async ({ page }) => {
  await page.route("**/api/v1/me", (route) => route.abort("failed"));
  await page.goto("/");
  await expect(page.getByText(/无法连接管理 API/)).toBeVisible();
  await expect(page.getByLabel("用户名")).toBeVisible();
});

test("代理非 JSON 错误显示 HTTP 状态和请求编号", async ({ page }) => {
  await page.route("**/api/v1/me", (route) =>
    route.fulfill({
      status: 502,
      contentType: "text/html",
      body: "<h1>Bad Gateway</h1>",
      headers: {
        "X-Request-ID": "proxy-test-123",
        "Access-Control-Expose-Headers": "X-Request-ID",
      },
    }),
  );
  await page.goto("/");
  await expect(page.getByText(/HTTP 502.*proxy-test-123/)).toBeVisible();
});

test("静态端点展示可复制的 Bearer 请求头及密钥填写说明", async ({ page }) => {
  const config = {
    mcpServers: {
      support: {
        type: "http",
        url: "http://localhost:8000/support/mcp",
        headers: { Authorization: "Bearer <YOUR_GROUP_ACCESS_KEY>" },
      },
    },
  };
  await page.route("**/api/v1/groups/support", (route) =>
    route.fulfill({
      json: {
        id: "support",
        enabled: true,
        auth_mode: "static",
        effective_tools: [],
        client_example: config,
        client_examples: {
          claude: config,
          opencode: {
            mcp: {
              support: {
                ...config.mcpServers.support,
                type: "remote",
                oauth: false,
              },
            },
          },
        },
      },
    }),
  );
  await page.goto("/groups/support");
  await page.getByRole("button", { name: /客户端连接配置示例/ }).click();
  await expect(
    page.getByText("使用前必须替换访问密钥占位符", { exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("这是远程 HTTP 服务，不需要本地启动命令", { exact: true }),
  ).toBeVisible();
  const code = page.locator("pre.code-block");
  await expect(code).toContainText('"type": "http"');
  await expect(code).toContainText(
    '"Authorization": "Bearer <YOUR_GROUP_ACCESS_KEY>"',
  );
  expect(JSON.parse(await code.innerText())).toEqual(config);
  await page.getByRole("tab", { name: "OpenCode", exact: true }).click();
  const remote = page
    .getByRole("tabpanel", { name: "OpenCode" })
    .locator("pre.code-block");
  expect(JSON.parse(await remote.innerText())).toEqual({
    mcp: {
      support: { ...config.mcpServers.support, type: "remote", oauth: false },
    },
  });
  await expect(
    page.getByRole("link", { name: "访问密钥", exact: true }),
  ).toBeVisible();
});
