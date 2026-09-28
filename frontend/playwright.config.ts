import { defineConfig } from "@playwright/test";
export default defineConfig({
  testDir: "./e2e",
  timeout: 45000,
  workers: 1,
  use: {
    baseURL: process.env.TEST_CONSOLE_URL || "http://localhost:5173",
    headless: true,
  },
  reporter: "list",
});
