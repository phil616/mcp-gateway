import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";
import react from "@vitejs/plugin-react";
export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    proxy: {
      "^/(api(?:/|$)|health(?:/|$)|\\.well-known(?:/|$)|docs(?:/|$)|redoc(?:/|$)|openapi\\.json$|[^/]+/mcp(?:/|$))": {
        target: "http://127.0.0.1:8000",
      },
    },
  },
  build: {
    rollupOptions: {
      onwarn(warning, warn) {
        if (warning.code !== "MODULE_LEVEL_DIRECTIVE") warn(warning);
      },
      output: {
        manualChunks: {
          ui: ["antd"],
          react: ["react", "react-dom", "react-router-dom"],
          query: ["@tanstack/react-query"],
        },
      },
    },
  },
});
