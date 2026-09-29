import { test, expect } from "@playwright/test";

test("登录响应成功但 Cookie 未生效时保留登录页并给出诊断", async ({ page }) => {
  await page.route("**/api/v1/**", async (route) => {
    const login = new URL(route.request().url()).pathname.endsWith("/login");
    await route.fulfill({
      status: login ? 200 : 401,
      json: login
        ? { username: "admin", csrf: "test" }
        : { detail: "Login required" },
    });
  });
  await page.goto("/groups");
  await page.getByLabel("用户名").fill("admin");
  await page.getByLabel("密码", { exact: true }).fill("test-password-1234");
  await page.getByRole("button", { name: /^登\s*录$/ }).click();
  await expect(page.getByText(/浏览器未保存或发送登录 Cookie/)).toBeVisible();
  await expect(page.getByLabel("用户名")).toBeVisible();
});

test("管理请求返回 401 后回到登录页", async ({ page }) => {
  await page.route("**/api/v1/**", async (route) => {
    const me = new URL(route.request().url()).pathname.endsWith("/me");
    await route.fulfill({
      status: me ? 200 : 401,
      json: me
        ? { username: "admin", csrf: "test" }
        : { detail: "Login required" },
    });
  });
  await page.goto("/groups");
  await expect(page.getByLabel("用户名")).toBeVisible();
});
