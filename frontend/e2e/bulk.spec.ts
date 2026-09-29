import { test, expect } from "@playwright/test";

test.beforeEach(async ({ page }) => {
  await page.route("**/api/v1/**", async (route) => {
    const url = new URL(route.request().url());
    const path = url.pathname.replace("/api/v1", "");
    let body: unknown = { items: [], total: 0 };
    if (path === "/me") body = { username: "admin", csrf: "test" };
    if (path === "/groups") {
      const all = Array.from({ length: 21 }, (_, i) => ({
        id: `group-${String(i).padStart(2, "0")}`,
        version: 1,
        enabled: false,
      }));
      const offset = Number(url.searchParams.get("offset") || 0);
      const limit = Number(url.searchParams.get("limit") || 20);
      body = { items: all.slice(offset, offset + limit), total: all.length };
    }
    if (path === "/tools")
      body = {
        items: Array.from({ length: 61 }, (_, i) => ({
          id: `csa.tool-${i}`,
          available: true,
          config_schema: { type: "object", properties: {} },
        })),
        total: 61,
      };
    await route.fulfill({ json: body });
  });
});

test("大量删除引用分页显示，长 ID 不撑破弹窗", async ({ page }) => {
  const errors: string[] = [];
  page.on("pageerror", (e) => errors.push(e.message));
  await page.route("**/groups/group-00/dependencies", (route) =>
    route.fulfill({
      json: {
        items: Array.from({ length: 125 }, (_, i) => ({
          resource: "bindings",
          id: `binding-${i}-` + "x".repeat(110),
        })),
      },
    }),
  );
  await page.goto("/groups");
  await page
    .getByRole("row")
    .filter({ hasText: "group-00" })
    .getByRole("button", { name: /^删\s*除$/ })
    .click();
  const dialog = page.getByRole("dialog");
  await expect(
    dialog.getByText("请先解除以下引用", { exact: true }),
  ).toBeVisible();
  await expect(dialog.getByText("共 125 项")).toBeVisible();
  await expect(dialog.getByRole("button", { name: "确认删除" })).toBeDisabled();
  await expect(dialog.locator("tbody tr[data-row-key]")).toHaveCount(10);
  await dialog.locator(".ant-pagination-next").click();
  await expect(dialog.getByText(/^binding-10-/)).toBeVisible();
  await page.setViewportSize({ width: 390, height: 844 });
  const size = await dialog.evaluate((el) => ({
    width: el.getBoundingClientRect().width,
    viewport: innerWidth,
    overflow: el.scrollWidth > el.clientWidth + 2,
  }));
  expect(size.width).toBeLessThanOrEqual(size.viewport);
  expect(size.overflow).toBe(false);
  expect(errors).toEqual([]);
});

test("跨页选中对象并提交版本化批量删除", async ({ page }) => {
  await page.route("**/groups/batch-delete", (route) =>
    route.fulfill({ json: { deleted: 2 } }),
  );
  await page.goto("/groups");
  await page
    .getByRole("row")
    .filter({ hasText: "group-00" })
    .getByRole("checkbox")
    .check();
  await page.locator(".ant-pagination-next").click();
  await page
    .getByRole("row")
    .filter({ hasText: "group-20" })
    .getByRole("checkbox")
    .check();
  await page.getByRole("button", { name: "批量删除（2）" }).click();
  const request = page.waitForRequest((r) =>
    r.url().endsWith("/groups/batch-delete"),
  );
  await page
    .getByRole("dialog")
    .getByRole("button", { name: "确认删除" })
    .click();
  expect((await request).postDataJSON().items).toEqual([
    { id: "group-00", version: 1 },
    { id: "group-20", version: 1 },
  ]);
  await expect(page.getByRole("dialog")).toHaveCount(0);
});

test("按前缀一次添加超过 50 个工具，跳过已绑定工具", async ({ page }) => {
  await page.route("**/api/v1/bindings?**", (route) =>
    route.fulfill({
      json: {
        items: [
          {
            id: "existing",
            group_id: "group-00",
            tool_id: "csa.tool-0",
            exposed_name: "existing",
            version: 1,
          },
        ],
        total: 1,
      },
    }),
  );
  await page.route("**/bindings/batch", (route) =>
    route.fulfill({ json: { items: Array.from({ length: 60 }, () => ({})) } }),
  );
  await page.goto("/bindings");
  await page.getByRole("button", { name: "批量绑定", exact: true }).click();
  await page.getByLabel("目标组", { exact: true }).click();
  await page
    .locator(".ant-select-item-option-content")
    .getByText("group-00", { exact: true })
    .click();
  await page.getByLabel("工具 ID 前缀", { exact: true }).fill("csa.");
  await page.getByRole("button", { name: "添加匹配工具（60）" }).click();
  await expect(page.getByLabel("绑定 ID", { exact: true })).toHaveCount(60);
  const request = page.waitForRequest((r) =>
    r.url().endsWith("/bindings/batch"),
  );
  await page.getByRole("button", { name: "创建 60 个绑定" }).click();
  const items = (await request).postDataJSON().items;
  expect(items).toHaveLength(60);
  expect(items.some((i: any) => i.data.tool_id === "csa.tool-0")).toBe(false);
  expect(new Set(items.map((i: any) => i.id)).size).toBe(60);
  await expect(page.locator(".ant-drawer")).toHaveCount(0);
});
