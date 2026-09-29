import { test, expect } from "@playwright/test";
import { execFileSync } from "node:child_process";

test("管理员在浏览器创建配置、绑定并通过真实 MCP 客户端调用", async ({
  page,
}) => {
  const id = "browser-" + Date.now();
  const errors: string[] = [];
  page.on("pageerror", (e) => errors.push(e.message));
  await page.goto("/");
  await page.getByLabel("用户名").fill("admin");
  await page.getByLabel("密码", { exact: true }).fill("test-password-1234");
  await page.getByRole("button", { name: /^登\s*录$/ }).click();
  await expect(
    page.getByRole("heading", { name: "端点组", exact: true }),
  ).toBeVisible();
  async function newRecord(path: string) {
    await page.goto("/" + path);
    await page.getByRole("button", { name: /^创\s*建$/ }).click();
    await page.getByLabel("稳定 ID（创建后不可修改）").fill(id);
  }
  async function save() {
    await page.getByRole("button", { name: /^保\s*存$/ }).click();
    await expect(page.locator(".ant-drawer")).toHaveCount(0);
  }
  await newRecord("secrets");
  await page
    .getByLabel("密钥值", { exact: true })
    .fill("browser-test-upstream-key");
  await save();
  await newRecord("config-profiles");
  await page
    .locator("textarea")
    .fill(JSON.stringify({ prefix: "Browser", api_key: { $secret: id } }));
  await save();
  await newRecord("groups");
  await page.getByLabel("启用", { exact: true }).click();
  await save();
  await newRecord("bindings");
  async function choose(label: string, value: string) {
    await page.getByLabel(label, { exact: true }).click();
    await page.getByLabel(label, { exact: true }).fill(value);
    await page
      .locator(".ant-select-dropdown:visible")
      .locator(".ant-select-item-option-content")
      .filter({
        hasText: new RegExp(
          "^" + value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + "$",
        ),
      })
      .click();
  }
  await choose("所属组", id);
  await choose("工具", "demo.echo");
  await page.getByLabel("MCP 暴露名称").fill("echo");
  await choose("配置集", id);
  await page.getByLabel("启用", { exact: true }).click();
  await save();
  await page.goto("/groups/" + id);
  await expect(page.getByText("MCP 暴露名称")).toHaveCount(0);
  await expect(
    page.getByText(
      (process.env.TEST_BASE_URL || "http://localhost:8000") +
        "/" +
        id +
        "/mcp",
      { exact: true },
    ),
  ).toBeVisible();
  const result = execFileSync(
    "uv",
    [
      "run",
      "python",
      "-c",
      `import asyncio,sys,json
from fastmcp import Client
async def main():
 async with Client(sys.argv[1]) as c:
  result=await c.call_tool('echo',{'message':'success'})
  print(json.dumps(result.data))
asyncio.run(main())`,
      `${process.env.TEST_BASE_URL || "http://localhost:8000"}/${id}/mcp`,
    ],
    { cwd: "..", encoding: "utf8" },
  );
  expect(JSON.parse(result.trim())).toEqual({
    message: "Browser success",
    group: id,
  });
  await page.screenshot({ path: "test-results/console.png", fullPage: true });
  expect(errors).toEqual([]);
});
