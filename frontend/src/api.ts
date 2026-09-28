const configuredBase = (
  import.meta.env.VITE_API_URL || "http://localhost:8000"
).replace(/\/$/, "");
const loopback = new Set(["localhost", "127.0.0.1", "[::1]"]);
const apiUrl = new URL(configuredBase, window.location.origin);
// Keep local development cookies on the same hostname as the console.
if (
  apiUrl.protocol === "http:" &&
  window.location.protocol === "http:" &&
  loopback.has(apiUrl.hostname) &&
  loopback.has(window.location.hostname)
) {
  apiUrl.hostname = window.location.hostname;
}
export const base = apiUrl.href.replace(/\/$/, "");
export class ApiError extends Error {
  constructor(
    message: string,
    public status: number,
    public requestId?: string,
  ) {
    super(requestId ? `${message}（请求编号：${requestId}）` : message);
  }
}
let csrf = "";
export function setCsrf(value: string) {
  csrf = value;
}
export async function api(path: string, method = "GET", body?: unknown) {
  let response: Response;
  try {
    response = await fetch(`${base}/api/v1${path}`, {
      method,
      credentials: "include",
      headers: { "Content-Type": "application/json", "X-CSRF-Token": csrf },
      body: body === undefined ? undefined : JSON.stringify(body),
    });
  } catch {
    throw new ApiError(
      `无法连接管理 API ${base}。请检查服务是否启动，以及 CONSOLE_ORIGIN 是否允许当前页面来源 ${window.location.origin}。`,
      0,
    );
  }
  const requestId = response.headers.get("X-Request-ID") || undefined;
  let data;
  try {
    data = await response.json();
  } catch {
    throw new ApiError(
      `管理 API 返回 HTTP ${response.status}，但响应不是有效 JSON。请检查反向代理与 API 地址配置。`,
      response.status,
      requestId,
    );
  }
  if (!response.ok) {
    const detail = data?.detail;
    throw new ApiError(
      response.status === 409 && detail === "Version conflict"
        ? "此记录已被其他操作更新。请保留当前输入，关闭编辑并刷新列表后重试。"
        : typeof detail === "string"
          ? detail
          : detail
            ? JSON.stringify(detail)
            : `管理 API 请求失败（HTTP ${response.status}）`,
      response.status,
      requestId,
    );
  }
  return data;
}
