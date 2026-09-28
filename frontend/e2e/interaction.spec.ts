import { test, expect } from "@playwright/test";

test("推荐 ID、日历到期时间和批量绑定完整流程", async ({ page }) => {
  await page.goto("/groups");
  await page.getByLabel("账号").fill("admin");
  await page.getByLabel("密码", { exact: true }).fill("test-password-1234");
  await page.getByRole("button", { name: /^登\s*录$/ }).click();
  await page.getByRole("button", { name: "创建", exact: true }).click();
  await page.getByRole("button", { name: /^support-agent/ }).click();
  const group = await page.getByLabel("稳定 ID（创建后不可修改）").inputValue();
  expect(group).toMatch(/^support-agent/);
  await page.getByRole("button", { name: /^保\s*存$/ }).click();
  await expect(page.locator(".ant-drawer")).toHaveCount(0);
  await page.goto("/groups/" + group);
  await page.getByRole("button", { name: "批量绑定", exact: true }).click();
  await page.getByLabel("选择工具", { exact: true }).click();
  for (const tool of ["demo.echo", "demo.wait"])
    await page
      .locator(".ant-select-dropdown:visible .ant-select-item-option-content")
      .getByText(tool, { exact: true })
      .click();
  await page.getByText("批量创建工具绑定", { exact: true }).click();
  await expect(page.getByLabel("绑定 ID", { exact: true })).toHaveCount(2);
  await page.screenshot({
    path: "test-results/batch-bindings.png",
    fullPage: true,
  });
  await page
    .getByRole("button", { name: "创建 2 个绑定", exact: true })
    .click();
  await expect(page.locator(".ant-drawer")).toHaveCount(0);
  await expect(
    page.getByText(`${group} / demo.echo`, { exact: false }),
  ).toBeVisible();
  await expect(
    page.getByText(`${group} / demo.wait`, { exact: false }),
  ).toBeVisible();
  await page.goto("/access-keys");
  await page.getByRole("button", { name: "创建", exact: true }).click();
  await page.getByLabel("所属组", { exact: true }).fill(group);
  await page
    .locator(".ant-select-dropdown:visible .ant-select-item-option-content")
    .getByText(group, { exact: true })
    .click();
  await page
    .getByRole("button", { name: group + "-access", exact: true })
    .click();
  await page.getByLabel("到期时间", { exact: true }).click();
  await expect(page.locator(".ant-picker-dropdown:visible")).toBeVisible();
  await page.screenshot({
    path: "test-results/expiry-picker.png",
    fullPage: true,
  });
  await page.keyboard.press("Escape");
  await page.getByRole("button", { name: "7 天后", exact: true }).click();
  const request = page.waitForRequest(
    (r) => r.method() === "POST" && r.url().endsWith("/api/v1/access-keys"),
  );
  await page.getByRole("button", { name: /^保\s*存$/ }).click();
  const data = (await request).postDataJSON().data;
  expect(data.expires_at).toMatch(/Z$/);
  expect(Date.parse(data.expires_at) - Date.now()).toBeGreaterThan(
    6 * 86400000,
  );
  await expect(
    page.getByRole("dialog", {
      name: "访问密钥仅展示一次，请立即保存",
      exact: true,
    }),
  ).toBeVisible();
});

test("127.0.0.1 控制台可以登录并保留管理员会话", async ({ page, baseURL }) => {
  const url = new URL(baseURL!);
  url.hostname = "127.0.0.1";
  await page.goto(url.href);
  await page.getByLabel("账号").fill("admin");
  await page.getByLabel("密码", { exact: true }).fill("test-password-1234");
  await page.getByRole("button", { name: /^登\s*录$/ }).click();
  await expect(
    page.getByRole("heading", { name: "端点组", exact: true }),
  ).toBeVisible();
  await page.reload();
  await expect(
    page.getByRole("heading", { name: "端点组", exact: true }),
  ).toBeVisible();
});
