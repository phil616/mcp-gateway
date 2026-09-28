import { Button, DatePicker, Space, Typography } from "antd";
import dayjs from "dayjs";
import "dayjs/locale/zh-cn";
dayjs.locale("zh-cn");

export function uniqueId(base: string, taken: string[], max = 128) {
  const stem =
    base
      .toLowerCase()
      .replace(/[^a-z0-9-]+/g, "-")
      .replace(/^-+|-+$/g, "")
      .slice(0, max - 6) || "binding";
  let candidate = stem;
  for (let n = 2; taken.includes(candidate); n++) candidate = `${stem}-${n}`;
  return candidate;
}
export function IdSuggestions({
  resource,
  group,
  tool,
  mode,
  taken,
  onSelect,
}: {
  resource: string;
  group?: string;
  tool?: string;
  mode?: string;
  taken: string[];
  onSelect: (id: string) => void;
}) {
  const seeds: Record<string, string[]> = {
    groups: ["support-agent", "data-analysis", "workflow-automation"],
    bindings: [
      group && tool ? `${group}-${tool}` : "tool-binding",
      tool ? `${tool}-default` : "default-binding",
    ],
    "config-profiles": [
      "development-config",
      "production-config",
      "shared-service-config",
    ],
    secrets: ["upstream-api-key", "orders-api-key", "service-password"],
    "auth-profiles": [
      `${mode || "public"}-auth`,
      `${mode || "public"}-internal`,
    ],
    "access-keys": [
      `${group || "agent"}-access`,
      `${group || "agent"}-development`,
    ],
  };
  return (
    <div className="id-suggestions">
      <Typography.Text type="secondary">
        推荐 ID（点击选用，可继续修改）：
      </Typography.Text>
      <Space wrap>
        {(seeds[resource] || []).map((seed) => {
          const id = uniqueId(seed, taken, resource === "groups" ? 63 : 128);
          return (
            <Button key={seed} size="small" onClick={() => onSelect(id)}>
              {id}
            </Button>
          );
        })}
      </Space>
      <div>
        <Typography.Text type="secondary">
          根据用途命名，并避开已加载的 ID；保存时仍会检查重名。
        </Typography.Text>
      </div>
    </div>
  );
}
export function ExpiryPicker({
  value,
  onChange,
  id,
}: {
  value?: string | null;
  onChange?: (v: string | null) => void;
  id?: string;
}) {
  return (
    <div>
      <DatePicker
        id={id}
        value={value ? dayjs(value) : null}
        onChange={(v) => onChange?.(v ? v.toISOString() : null)}
        showTime
        format="YYYY-MM-DD HH:mm"
        inputReadOnly
        allowClear
        showNow={false}
        disabledDate={(date) => date.isBefore(dayjs(), "day")}
        presets={[7, 30, 90].map((days) => ({
          label: `${days} 天后`,
          value: () => dayjs().add(days, "day"),
        }))}
        placeholder="选择到期日期和时间"
        style={{ width: "100%" }}
      />
      <Space wrap className="mt-3">
        {[7, 30, 90].map((days) => (
          <Button
            key={days}
            size="small"
            onClick={() => onChange?.(dayjs().add(days, "day").toISOString())}
          >
            {days} 天后
          </Button>
        ))}
        <Button size="small" onClick={() => onChange?.(null)}>
          不过期
        </Button>
      </Space>
      <div>
        <Typography.Text type="secondary">
          按本地时区 {Intl.DateTimeFormat().resolvedOptions().timeZone}{" "}
          选择，自动转换为 UTC 保存。留空表示不过期。
        </Typography.Text>
      </div>
    </div>
  );
}
