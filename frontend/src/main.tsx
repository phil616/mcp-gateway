import React, { useState } from "react";
import { createRoot } from "react-dom/client";
import {
  BrowserRouter,
  Link,
  useLocation,
  useNavigate,
  useParams,
  Routes,
  Route,
} from "react-router-dom";
import {
  QueryClient,
  QueryClientProvider,
  useQuery,
  useQueryClient,
} from "@tanstack/react-query";
import {
  Alert,
  App,
  Button,
  Card,
  Checkbox,
  ConfigProvider,
  Drawer,
  Form,
  Input,
  InputNumber,
  Layout,
  Menu,
  Modal,
  Breadcrumb,
  Collapse,
  Empty,
  Grid,
  Result,
  Skeleton,
  Select,
  Space,
  Switch,
  Table,
  Tabs,
  Tag,
  Typography,
} from "antd";
import { api, ApiError, base, setCsrf, sessionExpiredEvent } from "./api";
import zhCN from "antd/locale/zh_CN";
import {
  ApiOutlined,
  AppstoreOutlined,
  LinkOutlined,
  SettingOutlined,
  LockOutlined,
  SafetyCertificateOutlined,
  KeyOutlined,
  AuditOutlined,
  BookOutlined,
  MenuOutlined,
  PlusOutlined,
  ReloadOutlined,
} from "@ant-design/icons";
import { guidance, ResourceHelp, GuidePage } from "./guidance";
import { IdSuggestions, ExpiryPicker, uniqueId } from "./form-helpers";
import "./style.css";

type Row = Record<string, any>;
const resources: Record<string, string> = {
  tools: "工具目录",
  groups: "端点组",
  bindings: "工具绑定",
  "config-profiles": "配置集",
  secrets: "密钥",
  "auth-profiles": "认证配置",
  "access-keys": "访问密钥",
  audit: "审计日志",
};
const resourceIcons: Record<string, React.ReactNode> = {
  tools: <AppstoreOutlined aria-hidden />,
  groups: <ApiOutlined aria-hidden />,
  bindings: <LinkOutlined aria-hidden />,
  "config-profiles": <SettingOutlined aria-hidden />,
  secrets: <LockOutlined aria-hidden />,
  "auth-profiles": <SafetyCertificateOutlined aria-hidden />,
  "access-keys": <KeyOutlined aria-hidden />,
  audit: <AuditOutlined aria-hidden />,
};
const defaults: Record<string, Row> = {
  groups: { enabled: false },
  bindings: { enabled: false, overrides: {} },
  "config-profiles": { values: {} },
  "auth-profiles": { mode: "public", validation: "jwt", scopes: [] },
  secrets: {},
  "access-keys": { revoked: false },
};
const queryClient = new QueryClient({
  defaultOptions: { queries: { retry: false } },
});
function useRows(resource: string) {
  return useQuery({
    queryKey: ["options", resource],
    queryFn: async () => {
      let items: Row[] = [];
      let offset = 0;
      while (true) {
        const page = await api(`/${resource}?limit=200&offset=${offset}`);
        items = items.concat(page.items);
        if (items.length >= page.total) return items;
        offset += 200;
      }
    },
  });
}

function SchemaFields({
  schema,
  value,
  onChange,
  inherited,
  secrets: secretRows,
}: {
  schema: Row;
  value: Row;
  onChange: (value: Row) => void;
  inherited: Row;
  secrets: Row[];
}) {
  return (
    <>
      {Object.entries(schema.properties || {}).map(([name, raw]) => {
        const field = raw as Row;
        const active = Object.hasOwn(value, name);
        const isSecret = field.writeOnly || field.format === "password";
        const set = (v: unknown) => onChange({ ...value, [name]: v });
        return (
          <div className="schema-field" key={name}>
            <Space>
              <Checkbox
                checked={active}
                onChange={(e) => {
                  const next = { ...value };
                  if (e.target.checked)
                    next[name] = isSecret
                      ? { $secret: "" }
                      : (inherited[name] ??
                        field.default ??
                        (field.type === "boolean"
                          ? false
                          : field.type === "integer" || field.type === "number"
                            ? 0
                            : ""));
                  else delete next[name];
                  onChange(next);
                }}
              >
                {name}
                {schema.required?.includes(name) ? " *" : ""}
              </Checkbox>
              <Tag>{active ? "绑定覆盖" : "继承配置集 / 声明默认值"}</Tag>
            </Space>
            <div className="field-control">
              {active ? (
                isSecret ? (
                  <Select
                    style={{ width: "100%" }}
                    placeholder="选择密钥引用"
                    value={value[name]?.$secret}
                    options={secretRows.map((s) => ({
                      value: s.id,
                      label: s.id,
                    }))}
                    onChange={(v) => set({ $secret: v })}
                  />
                ) : field.enum ? (
                  <Select
                    value={value[name]}
                    options={field.enum.map((v: string) => ({
                      value: v,
                      label: v,
                    }))}
                    onChange={set}
                  />
                ) : field.type === "boolean" ? (
                  <Switch checked={value[name]} onChange={set} />
                ) : ["integer", "number"].includes(field.type) ? (
                  <InputNumber value={value[name]} onChange={set} />
                ) : ["object", "array"].includes(field.type) || field.$ref ? (
                  <JsonInput value={value[name]} onChange={set} />
                ) : (
                  <Input
                    value={value[name]}
                    onChange={(e) => set(e.target.value)}
                  />
                )
              ) : (
                <Typography.Text type="secondary">
                  {isSecret
                    ? "密钥通过引用注入"
                    : JSON.stringify(
                        inherited[name] ?? field.default ?? "未设置",
                      )}
                </Typography.Text>
              )}
            </div>
            {field.description && (
              <Typography.Text type="secondary">
                {field.description}
              </Typography.Text>
            )}
          </div>
        );
      })}
    </>
  );
}
function JsonInput({
  value,
  onChange,
}: {
  value?: unknown;
  onChange?: (v: any) => void;
}) {
  const [raw, setRaw] = useState(JSON.stringify(value ?? {}, null, 2));
  const [error, setError] = useState("");
  return (
    <>
      <Input.TextArea
        rows={6}
        value={raw}
        onChange={(e) => {
          setRaw(e.target.value);
          try {
            onChange?.(JSON.parse(e.target.value));
            setError("");
          } catch {
            onChange?.(e.target.value);
            setError("JSON 格式无效；修正后才能保存此字段");
          }
        }}
      />
      {error && <Alert type="error" title={error} />}
    </>
  );
}
function Editor({
  resource,
  row,
  group,
  close,
}: {
  resource: string;
  row?: Row;
  group?: string;
  close: () => void;
}) {
  const [form] = Form.useForm();
  const { message, modal } = App.useApp();
  const qc = useQueryClient();
  const [saving, setSaving] = useState(false);
  const tools = useRows("tools");
  const profiles = useRows("config-profiles");
  const secrets = useRows("secrets");
  const auth = useRows("auth-profiles");
  const groups = useRows("groups");
  const existingIds = useRows(resource);
  const groupId = Form.useWatch("group_id", form);
  const toolId = Form.useWatch("tool_id", form);
  const profileId = Form.useWatch("profile_id", form);
  const mode = Form.useWatch("mode", form);
  const validation = Form.useWatch("validation", form);
  const overrides = Form.useWatch("overrides", form) || {};
  const selected = tools.data?.find((r: Row) => r.id === toolId);
  const options = (rows: Row[] = []) =>
    rows.map((r) => ({ value: r.id, label: r.id }));
  const choose = (
    name: string,
    label: string,
    rows?: Row[],
    required = false,
  ) => (
    <Form.Item
      name={name}
      label={label}
      rules={required ? [{ required: true }] : []}
    >
      <Select
        allowClear={!required}
        showSearch
        options={options(rows)}
        onClear={() => form.setFieldValue(name, null)}
      />
    </Form.Item>
  );
  async function save() {
    try {
      const values = await form.validateFields();
      setSaving(true);
      const { id, ...data } = values;
      const result = await api(
        `/${resource}${row ? "/" + encodeURIComponent(row.id) : ""}`,
        row ? "PUT" : "POST",
        row ? { version: row.version, data } : { id, data },
      );
      if (result.token)
        modal.info({
          title: "访问密钥仅展示一次，请立即保存",
          content: (
            <Typography.Paragraph copyable>{result.token}</Typography.Paragraph>
          ),
          width: 600,
        });
      await qc.invalidateQueries();
      message.success("已保存");
      close();
    } catch (e) {
      if (e instanceof Error) message.error(e.message);
    } finally {
      setSaving(false);
    }
  }
  return (
    <Drawer
      open
      width={640}
      title={`${row ? "编辑" : "创建"}${resources[resource]}`}
      onClose={close}
      extra={
        <Button type="primary" loading={saving} onClick={save}>
          保存
        </Button>
      }
    >
      <Alert
        className="editor-help"
        showIcon
        type="info"
        title={guidance[resource]?.summary}
        description={guidance[resource]?.detail}
      />
      <Form
        form={form}
        layout="vertical"
        initialValues={{
          ...defaults[resource],
          ...row,
          ...(group ? { group_id: group } : {}),
          ...(resource === "secrets" ? { value: undefined } : {}),
        }}
      >
        {!row && (
          <Form.Item
            name="id"
            label="稳定 ID（创建后不可修改）"
            rules={[{ required: true }]}
            extra={
              <IdSuggestions
                resource={resource}
                group={groupId}
                tool={toolId}
                mode={mode}
                taken={(existingIds.data || []).map((r: Row) => r.id)}
                onSelect={(id) => form.setFieldValue("id", id)}
              />
            }
          >
            <Input />
          </Form.Item>
        )}
        {["groups", "bindings", "tools"].includes(resource) && (
          <Form.Item name="enabled" label="启用" valuePropName="checked">
            <Switch />
          </Form.Item>
        )}
        {resource === "groups" &&
          choose("auth_profile_id", "入站认证（未选择时为公开）", auth.data)}
        {resource === "bindings" && (
          <>
            {choose("group_id", "所属组", groups.data, true)}
            {choose("tool_id", "工具", tools.data, true)}
            <Form.Item
              name="exposed_name"
              label="MCP 暴露名称"
              extra="客户端看到的工具名称，同一组内不能重复。"
              rules={[{ required: true }]}
            >
              <Input />
            </Form.Item>
            {choose("profile_id", "配置集", profiles.data)}
            <Form.Item name="overrides" hidden>
              <Input />
            </Form.Item>
            {selected && (
              <SchemaFields
                schema={selected.config_schema}
                value={overrides}
                onChange={(v) => form.setFieldValue("overrides", v)}
                inherited={
                  profiles.data?.find((p) => p.id === profileId)?.values || {}
                }
                secrets={secrets.data || []}
              />
            )}
            <Alert
              type="info"
              title="未勾选的字段继承配置集或工具默认值。密钥字段只能选择引用。"
            />
          </>
        )}
        {resource === "config-profiles" && (
          <>
            <Alert
              title={
                '配置值为 JSON 对象；密钥使用 {"$secret":"密钥ID"}。更新将验证全部有效绑定。'
              }
              type="info"
            />
            <Form.Item name="values" label="配置值">
              <JsonInput />
            </Form.Item>
          </>
        )}
        {resource === "secrets" && (
          <>
            <Form.Item
              name="value"
              label={row ? "替换密钥（留空保留）" : "密钥值"}
              rules={row ? [] : [{ required: true }]}
            >
              <Input.Password autoComplete="new-password" />
            </Form.Item>
            <Form.Item name="description" label="说明">
              <Input />
            </Form.Item>
          </>
        )}
        {resource === "auth-profiles" && (
          <>
            <Form.Item name="mode" label="认证模式">
              <Select
                options={["public", "static", "oauth"].map((v) => ({
                  value: v,
                  label: (
                    {
                      public: "公开 · 无需凭据",
                      static: "静态密钥 · Bearer Key",
                      oauth: "OAuth · 外部身份服务",
                    } as Record<string, string>
                  )[v],
                }))}
              />
            </Form.Item>
            {mode === "oauth" && (
              <>
                <Form.Item
                  name="issuer"
                  label="Issuer（HTTPS）"
                  rules={[{ required: true }]}
                >
                  <Input />
                </Form.Item>
                <Form.Item name="validation" label="令牌验证">
                  <Select
                    options={["jwt", "introspection"].map((v) => ({
                      value: v,
                      label: v,
                    }))}
                  />
                </Form.Item>
                {validation === "jwt" ? (
                  <Form.Item
                    name="jwks_url"
                    label="JWKS URL"
                    rules={[{ required: true }]}
                  >
                    <Input />
                  </Form.Item>
                ) : (
                  <>
                    <Form.Item
                      name="introspection_url"
                      label="Introspection URL"
                      rules={[{ required: true }]}
                    >
                      <Input />
                    </Form.Item>
                    <Form.Item name="client_id" label="Client ID">
                      <Input />
                    </Form.Item>
                    <Form.Item name="client_secret" label="Client Secret 引用">
                      <JsonInput />
                    </Form.Item>
                  </>
                )}
                <Form.Item name="scopes" label="必要 scopes">
                  <Select mode="tags" />
                </Form.Item>
                <Alert
                  type="info"
                  title="此处配置资源服务器验证。完整 MCP 登录还要求 IDP 支持发现、PKCE、资源标识和客户端注册。"
                />
              </>
            )}
          </>
        )}
        {resource === "access-keys" &&
          (row ? (
            <Form.Item name="revoked" label="撤销" valuePropName="checked">
              <Switch />
            </Form.Item>
          ) : (
            <>
              {choose("group_id", "所属组", groups.data, true)}
              <Form.Item
                name="expires_at"
                label="到期时间"
                rules={[
                  {
                    validator: (_, v) =>
                      !v || Date.parse(v) > Date.now()
                        ? Promise.resolve()
                        : Promise.reject(new Error("请选择未来的到期时间")),
                  },
                ]}
              >
                <ExpiryPicker />
              </Form.Item>
            </>
          ))}
      </Form>
    </Drawer>
  );
}
function BatchBindingEditor({
  group,
  close,
}: {
  group?: string;
  close: () => void;
}) {
  const [form] = Form.useForm();
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");
  const [selectedIds, setSelectedIds] = useState<string[]>([]);
  const [prefix, setPrefix] = useState("");
  const qc = useQueryClient();
  const { message } = App.useApp();
  const groups = useRows("groups"),
    tools = useRows("tools"),
    bindings = useRows("bindings"),
    profiles = useRows("config-profiles"),
    secrets = useRows("secrets");
  const groupId = Form.useWatch("group_id", form);
  const items: Row[] = Form.useWatch("items", { form, preserve: true }) || [];
  const queries = [groups, tools, bindings, profiles, secrets];
  const loading = queries.some((q) => q.isPending);
  const failed = queries.find((q) => q.error)?.error;
  const boundIds = new Set(
    (bindings.data || [])
      .filter((b: Row) => b.group_id === groupId)
      .map((b: Row) => b.tool_id),
  );
  const matchingIds = (tools.data || [])
    .filter(
      (t: Row) =>
        t.available && !boundIds.has(t.id) && t.id.startsWith(prefix.trim()),
    )
    .map((t: Row) => t.id as string);
  const combinedIds = Array.from(new Set([...selectedIds, ...matchingIds]));
  function selectTools(ids: string[]) {
    const previous: Row[] = form.getFieldValue("items") || [];
    const taken = (bindings.data || [])
      .map((r: Row) => r.id)
      .concat(previous.map((r) => r.id));
    const names = (bindings.data || [])
      .filter((r: Row) => r.group_id === groupId)
      .map((r: Row) => r.exposed_name)
      .concat(previous.map((r) => r.exposed_name));
    const next = ids.map((toolId) => {
      const old = previous.find((r) => r.tool_id === toolId);
      if (old) return old;
      const id = uniqueId(`${groupId}-${toolId}`, taken);
      taken.push(id);
      const alias = uniqueId(toolId, names);
      names.push(alias);
      return {
        id,
        tool_id: toolId,
        exposed_name: alias,
        profile_id: null,
        overrides: {},
      };
    });
    setSelectedIds(ids);
    form.setFieldValue("items", next);
    setError("");
  }
  async function save() {
    try {
      const values = await form.validateFields();
      if (!values.items?.length) {
        setError("请至少选择一个工具");
        return;
      }
      setSaving(true);
      setError("");
      const result = await api("/bindings/batch", "POST", {
        items: values.items.map((item: Row) => {
          const { id, ...data } = item;
          return {
            id,
            data: {
              ...data,
              group_id: values.group_id,
              enabled: values.enabled,
            },
          };
        }),
      });
      await qc.invalidateQueries();
      message.success(`已创建 ${result.items.length} 个绑定`);
      close();
    } catch (e) {
      if (e instanceof Error) setError(e.message);
    } finally {
      setSaving(false);
    }
  }
  return (
    <Drawer
      open
      width={800}
      title="批量创建工具绑定"
      onClose={() => {
        if (!saving) close();
      }}
      maskClosable={!saving}
      closable={!saving}
      extra={
        <Button
          type="primary"
          loading={saving}
          disabled={loading || !!failed || !selectedIds.length}
          onClick={save}
        >
          创建 {selectedIds.length} 个绑定
        </Button>
      }
    >
      <Alert
        showIcon
        type="info"
        title="同一组一次绑定多个工具，全部成功才会保存"
        description="每次最多 200 个。已绑定的工具不可重复选择；推荐的 ID 和暴露名称可以修改。默认保存为禁用草稿，启用时会严格校验每项配置。"
        className="editor-help"
      />
      {failed && (
        <Alert
          type="error"
          title="无法加载工具或配置，请关闭后重试"
          description={failed.message}
        />
      )}
      {error && (
        <Alert
          showIcon
          type="error"
          title="未能确认创建成功"
          description={
            <>
              <div className="json">{error}</div>
              <div>
                校验失败时整批回滚。若网络中断，请先刷新绑定列表确认结果再提交，避免重复创建。
              </div>
            </>
          }
          className="editor-help"
        />
      )}
      <Form
        form={form}
        layout="vertical"
        disabled={saving || loading || !!failed}
        initialValues={{ group_id: group, enabled: false, items: [] }}
      >
        <Form.Item name="group_id" label="目标组" rules={[{ required: true }]}>
          <Select
            disabled={!!group || selectedIds.length > 0}
            placeholder="先选择一个组"
            options={(groups.data || []).map((r: Row) => ({
              value: r.id,
              label: r.id,
            }))}
          />
        </Form.Item>
        <Form.Item
          label="工具 ID 前缀"
          htmlFor="tool-prefix"
          extra="按开头精确匹配，例如 csa.；自动跳过已绑定或不可用工具。"
        >
          <Space.Compact style={{ width: "100%" }}>
            <Input
              id="tool-prefix"
              value={prefix}
              onChange={(e) => setPrefix(e.target.value)}
              placeholder="例如 csa."
              disabled={!groupId}
            />
            <Button
              disabled={
                !groupId ||
                !prefix.trim() ||
                !matchingIds.length ||
                combinedIds.length > 200
              }
              onClick={() => selectTools(combinedIds)}
            >
              添加匹配工具（{prefix.trim() ? matchingIds.length : 0}）
            </Button>
          </Space.Compact>
          {prefix.trim() && combinedIds.length > 200 && (
            <Typography.Text type="danger">
              合计超过 200 个，请缩小前缀范围后添加。
            </Typography.Text>
          )}
        </Form.Item>
        <Form.Item
          label="选择工具"
          htmlFor="batch-tools"
          extra="切换组前请清空工具选择；移除工具会丢弃该项尚未保存的配置。"
        >
          <Select
            id="batch-tools"
            aria-label="选择工具"
            mode="multiple"
            showSearch
            optionFilterProp="label"
            value={selectedIds}
            disabled={!groupId || saving || loading || !!failed}
            maxCount={200}
            maxTagCount="responsive"
            placeholder="可搜索并多选工具"
            onChange={selectTools}
            options={(tools.data || []).map((r: Row) => ({
              value: r.id,
              label: r.id,
              disabled:
                !r.available ||
                (bindings.data || []).some(
                  (b: Row) => b.group_id === groupId && b.tool_id === r.id,
                ),
            }))}
          />
        </Form.Item>
        <Form.Item
          name="enabled"
          label="创建后启用全部绑定"
          valuePropName="checked"
          extra="保持关闭可先保存草稿，再逐项补齐配置。"
        >
          <Switch />
        </Form.Item>
        {items.map((item, index) => {
          const tool = tools.data?.find((t: Row) => t.id === item.tool_id);
          return (
            <Card
              key={item.tool_id}
              title={`${index + 1}. ${item.tool_id}`}
              className="editor-help"
            >
              <Form.Item name={["items", index, "tool_id"]} hidden>
                <Input />
              </Form.Item>
              <Form.Item
                name={["items", index, "id"]}
                label="绑定 ID"
                rules={[
                  { required: true },
                  {
                    pattern: /^[a-zA-Z0-9_.-]{1,128}$/,
                    message: "使用 1–128 位字母、数字、点、横线或下划线",
                  },
                  {
                    validator: (_, v) =>
                      items.filter((r) => r.id === v).length > 1
                        ? Promise.reject(new Error("本批次 ID 重复"))
                        : Promise.resolve(),
                  },
                ]}
              >
                <Input />
              </Form.Item>
              <Form.Item
                name={["items", index, "exposed_name"]}
                label="暴露名称"
                rules={[
                  { required: true },
                  {
                    pattern: /^[a-zA-Z0-9_.-]{1,128}$/,
                    message: "名称格式不正确",
                  },
                  {
                    validator: (_, v) =>
                      items.filter((r) => r.exposed_name === v).length > 1
                        ? Promise.reject(new Error("本批次暴露名称重复"))
                        : Promise.resolve(),
                  },
                ]}
              >
                <Input />
              </Form.Item>
              <Form.Item
                name={["items", index, "profile_id"]}
                label="使用配置集"
              >
                <Select
                  allowClear
                  onClear={() =>
                    form.setFieldValue(["items", index, "profile_id"], null)
                  }
                  options={(profiles.data || []).map((r: Row) => ({
                    value: r.id,
                    label: r.id,
                  }))}
                />
              </Form.Item>
              <Form.Item name={["items", index, "overrides"]} hidden>
                <Input />
              </Form.Item>
              {tool && (
                <SchemaFields
                  schema={tool.config_schema}
                  value={item.overrides || {}}
                  inherited={
                    profiles.data?.find((r: Row) => r.id === item.profile_id)
                      ?.values || {}
                  }
                  secrets={secrets.data || []}
                  onChange={(v) =>
                    form.setFieldValue(["items", index, "overrides"], v)
                  }
                />
              )}
            </Card>
          );
        })}
      </Form>
    </Drawer>
  );
}

function DeleteDialog({
  resource,
  rows,
  close,
  complete,
}: {
  resource: string;
  rows: Row[];
  close: () => void;
  complete: () => Promise<void>;
}) {
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");
  const { message } = App.useApp();
  const dependencies = useQuery({
    queryKey: [
      "delete-dependencies",
      resource,
      rows.map((r) => [r.id, r.version]),
    ],
    staleTime: 0,
    queryFn: async () => {
      const items: Row[] = [];
      for (const row of rows) {
        const result = await api(
          `/${resource}/${encodeURIComponent(row.id)}/dependencies`,
        );
        items.push(...result.items.map((d: Row) => ({ ...d, owner: row.id })));
      }
      return items;
    },
  });
  const blocked = !!dependencies.data?.length;
  return (
    <Modal
      open
      title={
        blocked
          ? "请先解除以下引用"
          : `删除 ${rows.length} 项${resources[resource]}？`
      }
      width={850}
      onCancel={() => {
        if (!saving) close();
      }}
      closable={!saving}
      maskClosable={!saving}
      cancelButtonProps={{ disabled: saving }}
      okText="确认删除"
      okButtonProps={{
        danger: true,
        disabled: blocked || dependencies.isFetching || !!dependencies.error,
      }}
      confirmLoading={saving}
      styles={{
        body: { maxHeight: "65vh", overflow: "auto", overflowWrap: "anywhere" },
      }}
      onOk={async () => {
        setSaving(true);
        setError("");
        try {
          const result = await api(`/${resource}/batch-delete`, "POST", {
            items: rows.map((r) => ({ id: r.id, version: r.version })),
          });
          message.success(`已删除 ${result.deleted} 项`);
          await complete();
        } catch (e) {
          setError((e as Error).message);
        } finally {
          setSaving(false);
        }
      }}
    >
      <Alert
        showIcon
        type={blocked ? "warning" : "info"}
        title={
          blocked
            ? `发现 ${dependencies.data!.length} 条引用，请先删除相关绑定或访问密钥，或修改引用配置。`
            : "删除后无法恢复；任意一项失败时，整批均不删除。"
        }
      />
      {(error || dependencies.error) && (
        <Alert
          type="error"
          className="editor-help"
          title={error || dependencies.error?.message}
        />
      )}
      <Table
        size="small"
        loading={dependencies.isFetching}
        rowKey={(r: Row) =>
          blocked ? `${r.owner}:${r.resource}:${r.id}` : r.id
        }
        dataSource={blocked ? dependencies.data : rows}
        columns={
          blocked
            ? [
                { title: "待删除对象", dataIndex: "owner" },
                {
                  title: "引用类型",
                  dataIndex: "resource",
                  render: (v: string) => resources[v] || v,
                },
                { title: "引用 ID", dataIndex: "id" },
              ]
            : [
                { title: "ID", dataIndex: "id" },
                { title: "版本", dataIndex: "version", width: 80 },
              ]
        }
        tableLayout="fixed"
        className="dependency-table"
        scroll={{ y: 300 }}
        pagination={{
          pageSize: 10,
          showSizeChanger: false,
          showTotal: (total) => `共 ${total} 项`,
        }}
      />
    </Modal>
  );
}

function ResourcePage({ forced, group }: { forced?: string; group?: string }) {
  const params = useParams();
  const resource = forced || params.resource || "groups";
  const [batchOpen, setBatchOpen] = useState(false);
  const [page, setPage] = useState(1);
  const [search, setSearch] = useState("");
  const [editing, setEditing] = useState<Row | null | undefined>(undefined);
  const [view, setView] = useState<Row | null>(null);
  const { message, modal } = App.useApp();
  const qc = useQueryClient();
  const query = useQuery({
    queryKey: ["list", resource, group, page, search],
    queryFn: () =>
      api(
        `/${resource}?offset=${(page - 1) * 20}&limit=20&q=${encodeURIComponent(search)}${group ? "&group_id=" + encodeURIComponent(group) : ""}`,
      ),
  });
  const [selectedRows, setSelectedRows] = useState<Row[]>([]);
  const [deleting, setDeleting] = useState<Row[] | null>(null);
  React.useEffect(() => {
    setSelectedRows([]);
    setDeleting(null);
    setPage(1);
  }, [resource, group, search]);
  const columns =
    resource === "audit"
      ? ["at", "actor", "action", "resource", "object_id"].map((k) => ({
          title: (
            {
              at: "时间",
              actor: "操作者",
              action: "操作",
              resource: "资源类型",
              object_id: "对象 ID",
            } as Record<string, string>
          )[k],
          dataIndex: k,
        }))
      : [
          {
            title: "ID",
            dataIndex: "id",
            render: (id: string) =>
              resource === "groups" ? (
                <Link to={`/groups/${id}`}>{id}</Link>
              ) : (
                <strong>{id}</strong>
              ),
          },
          {
            title: "关联 / 说明",
            render: (_: unknown, r: Row) => (
              <Typography.Text type="secondary">
                {resource === "bindings"
                  ? `${r.group_id} / ${r.tool_id} → ${r.exposed_name}`
                  : resource === "groups"
                    ? r.auth_profile_id
                      ? `认证配置：${r.auth_profile_id}`
                      : "公开访问（未设置认证）"
                    : resource === "access-keys"
                      ? `所属组：${r.group_id}`
                      : r.description || "—"}
              </Typography.Text>
            ),
          },
          {
            title: "状态 / 版本",
            render: (_: unknown, r: Row) => (
              <Space wrap>
                {r.enabled !== undefined && (
                  <Tag color={r.enabled ? "green" : "default"}>
                    {r.enabled ? "启用" : "禁用"}
                  </Tag>
                )}
                {r.available === false && <Tag color="red">代码不可用</Tag>}
                {r.mode && <Tag>{r.mode}</Tag>}
                {r.revoked && <Tag color="red">已撤销</Tag>}
                <span>v{r.version}</span>
              </Space>
            ),
          },
          {
            title: "操作",
            render: (_: unknown, r: Row) => (
              <Space wrap>
                <Button size="small" onClick={() => setView(r)}>
                  详情
                </Button>
                <Button size="small" onClick={() => setEditing(r)}>
                  编辑
                </Button>
                {resource !== "tools" && (
                  <Button size="small" danger onClick={() => setDeleting([r])}>
                    删除
                  </Button>
                )}
                {resource === "auth-profiles" && r.mode === "oauth" && (
                  <Button
                    size="small"
                    onClick={async () => {
                      try {
                        const report = await api(
                          `/auth-profiles/${r.id}/compatibility`,
                        );
                        modal.info({
                          title: "OAuth 兼容性检查",
                          content: (
                            <pre className="json">
                              {JSON.stringify(report, null, 2)}
                            </pre>
                          ),
                        });
                      } catch (e) {
                        message.error((e as Error).message);
                      }
                    }}
                  >
                    兼容检查
                  </Button>
                )}
                {resource === "access-keys" && !r.revoked && (
                  <Button
                    size="small"
                    onClick={() =>
                      modal.confirm({
                        title: "轮换密钥并立即撤销旧密钥？",
                        onOk: async () => {
                          const result = await api(
                            `/access-keys/${r.id}/rotate`,
                            "POST",
                            { version: r.version, data: {} },
                          );
                          await qc.invalidateQueries();
                          modal.info({
                            title: "新密钥仅展示一次",
                            content: (
                              <Typography.Paragraph copyable>
                                {result.token}
                              </Typography.Paragraph>
                            ),
                          });
                        },
                      })
                    }
                  >
                    轮换
                  </Button>
                )}
                {resource === "bindings" && (
                  <Button
                    size="small"
                    onClick={async () => {
                      try {
                        await api(`/bindings/${r.id}/validate`, "POST");
                        message.success("配置有效");
                      } catch (e) {
                        message.error((e as Error).message);
                      }
                    }}
                  >
                    校验
                  </Button>
                )}
              </Space>
            ),
          },
        ];
  return (
    <>
      <div className="page-heading">
        <div>
          <Typography.Title level={2}>{resources[resource]}</Typography.Title>
          <Typography.Text type="secondary">
            {guidance[resource]?.summary}
          </Typography.Text>
        </div>
        <Space wrap>
          {!["tools", "audit"].includes(resource) && (
            <Button
              danger
              disabled={!selectedRows.length}
              onClick={() => setDeleting(selectedRows)}
            >
              批量删除（{selectedRows.length}）
            </Button>
          )}
          {resource === "bindings" && (
            <Button onClick={() => setBatchOpen(true)}>批量绑定</Button>
          )}
          {!["tools", "audit"].includes(resource) && (
            <Button
              type="primary"
              aria-label="创建"
              icon={<PlusOutlined aria-hidden />}
              onClick={() => setEditing(null)}
            >
              创建
            </Button>
          )}
        </Space>
      </div>
      <ResourceHelp resource={resource} />
      <Card>
        <div className="flex flex-wrap items-center justify-between gap-3 mb-5">
          <Input.Search
            placeholder="按 ID 筛选"
            style={{ maxWidth: 360 }}
            aria-label="按 ID 筛选"
            allowClear
            onSearch={(v) => {
              setSearch(v);
              setPage(1);
            }}
          />
          <Button
            icon={<ReloadOutlined aria-hidden />}
            loading={query.isFetching}
            onClick={() => query.refetch()}
          >
            刷新
          </Button>
        </div>
        {query.error && (
          <Alert
            showIcon
            type="error"
            title="加载失败"
            description={query.error.message}
          />
        )}
        <Table
          locale={{
            emptyText: (
              <Empty
                image={Empty.PRESENTED_IMAGE_SIMPLE}
                description={
                  query.error
                    ? "数据暂不可用，请重试"
                    : search
                      ? "没有匹配的结果，请调整筛选条件"
                      : guidance[resource]?.empty
                }
              />
            ),
          }}
          rowKey="id"
          rowSelection={
            !["tools", "audit"].includes(resource)
              ? {
                  selectedRowKeys: selectedRows.map((r) => r.id),
                  preserveSelectedRowKeys: true,
                  onChange: (_, rows) => {
                    if (rows.length > 200) {
                      message.warning("每次最多选择 200 项");
                      return;
                    }
                    setSelectedRows(rows);
                  },
                  getCheckboxProps: (row: Row) => ({
                    disabled:
                      selectedRows.length >= 200 &&
                      !selectedRows.some((r) => r.id === row.id),
                  }),
                }
              : undefined
          }
          loading={query.isLoading}
          dataSource={query.data?.items || []}
          columns={columns}
          showHeader={Boolean(query.data?.items?.length)}
          scroll={query.data?.items?.length ? { x: 700 } : undefined}
          pagination={{
            current: page,
            pageSize: 20,
            total: query.data?.total,
            onChange: setPage,
            showSizeChanger: false,
          }}
        />
      </Card>
      {deleting && (
        <DeleteDialog
          resource={resource}
          rows={deleting}
          close={() => setDeleting(null)}
          complete={async () => {
            setDeleting(null);
            setSelectedRows([]);
            setPage(1);
            await qc.invalidateQueries();
          }}
        />
      )}
      {batchOpen && (
        <BatchBindingEditor group={group} close={() => setBatchOpen(false)} />
      )}
      {editing !== undefined && (
        <Editor
          resource={resource}
          row={editing || undefined}
          group={group}
          close={() => setEditing(undefined)}
        />
      )}
      <Drawer
        title="详情"
        width={640}
        open={!!view}
        onClose={() => setView(null)}
      >
        <pre className="json">{JSON.stringify(view, null, 2)}</pre>
      </Drawer>
    </>
  );
}
function GroupPage() {
  const { id } = useParams();
  const query = useQuery({
    queryKey: ["group", id],
    queryFn: () => api(`/groups/${id}`),
  });
  if (query.isLoading) return <Skeleton active />;
  if (query.error)
    return (
      <Result
        status="error"
        title="无法加载端点组"
        subTitle={query.error.message}
        extra={<Button onClick={() => query.refetch()}>重试</Button>}
      />
    );
  const data = query.data;
  const mode = data.auth_mode || "public";
  return (
    <>
      <Card
        className="endpoint-card"
        title={
          <Space wrap>
            <ApiOutlined aria-hidden />
            {id}
            <Tag color={data.enabled ? "green" : "default"}>
              {data.enabled ? "已启用" : "已禁用"}
            </Tag>
          </Space>
        }
        extra={<Link to="/groups">管理组设置</Link>}
      >
        <div className="grid gap-6 lg:grid-cols-2">
          <div>
            <Typography.Text type="secondary">
              客户端连接地址 · Streamable HTTP
            </Typography.Text>
            <Typography.Paragraph className="endpoint-url" copyable>
              {data.endpoint || `${base}/${id}/mcp`}
            </Typography.Paragraph>
            <Tag color={mode === "public" ? "orange" : "blue"}>
              {
                (
                  {
                    public: "公开访问",
                    static: "静态访问密钥",
                    oauth: "外部 OAuth",
                  } as Row
                )[mode]
              }
            </Tag>
            <Typography.Paragraph className="mt-3">
              {!data.enabled
                ? "该组尚未启用，客户端目前无法使用此端点。"
                : mode === "public"
                  ? "此端点无需凭据即可访问。若需要限制访问，请在组设置中选择认证配置。"
                  : mode === "static"
                    ? "在客户端安全凭据设置中添加 Authorization: Bearer <访问密钥>。密钥必须属于本组。"
                    : "由外部身份服务完成授权；令牌的 audience 必须包含此完整端点 URL。"}
            </Typography.Paragraph>
          </div>
          <div>
            <Typography.Text type="secondary">当前有效工具</Typography.Text>
            <div className="mt-3">
              {data.effective_tools?.length ? (
                <Space wrap>
                  {data.effective_tools.map((t: Row) => (
                    <Tag key={t.name} color="blue">
                      {t.name}
                    </Tag>
                  ))}
                </Space>
              ) : (
                <Typography.Paragraph>
                  暂无。请检查组、绑定和工具的启用状态，以及工具代码是否可用。
                </Typography.Paragraph>
              )}
            </div>
            <Typography.Paragraph type="secondary" className="mt-3">
              配置变更后，客户端重新获取工具列表即可看到更新。
            </Typography.Paragraph>
          </div>
        </div>
        <Collapse
          items={[
            {
              key: "connection",
              label: "客户端连接配置示例",
              children: (
                <>
                  <Typography.Paragraph type="secondary">
                    请先选择客户端再复制配置，合并到对应配置文件中。OpenCode
                    使用 mcp 和 type: remote；Claude Code 使用 mcpServers 和
                    type: http；VS Code 使用 servers 和 type: http。
                  </Typography.Paragraph>
                  <Alert
                    showIcon
                    type="info"
                    className="editor-help"
                    title="这是远程 HTTP 服务，不需要本地启动命令"
                    description="若出现 The argument 'file' cannot be empty，通常是客户端正在启动空的本地命令。请将已有注册改为 HTTP / Streamable HTTP，删除 command、args 等 stdio 字段，保存后重新连接。VS Code 使用顶层 servers 而非 mcpServers；只支持 stdio 的客户端不能直接使用此配置。"
                  />
                  {mode === "static" && (
                    <Alert
                      showIcon
                      type="warning"
                      className="editor-help"
                      title="使用前必须替换访问密钥占位符"
                      description={
                        <>
                          将 &lt;YOUR_GROUP_ACCESS_KEY&gt;
                          替换为本组访问密钥的完整原文，保留 Bearer
                          和后面的空格，不保留尖括号。 请勿填写密钥
                          ID、掩码、上游密钥或管理员密码。原文仅在创建或轮换时展示一次；若已丢失，请前往{" "}
                          <Link to="/access-keys">访问密钥</Link> 新建或轮换。
                          客户端若使用独立的 HTTP 请求头设置，请添加同样的
                          Authorization 值。静态密钥模式不使用 OAuth 登录。
                        </>
                      }
                    />
                  )}
                  {mode === "oauth" && (
                    <Alert
                      showIcon
                      type="info"
                      className="editor-help"
                      title="此端点使用外部 OAuth 授权"
                      description="请使用支持 OAuth 的 MCP 客户端完成外部身份服务授权；此模式不使用组静态访问密钥。"
                    />
                  )}
                  <Tabs
                    items={Object.entries(
                      data.client_examples ?? { claude: data.client_example },
                    ).map(([key, config]) => ({
                      key,
                      label:
                        (
                          {
                            claude: "Claude Code",
                            opencode: "OpenCode",
                            vscode: "VS Code",
                          } as Record<string, string>
                        )[key] ?? key,
                      children: (
                        <Typography.Paragraph
                          copyable={{ text: JSON.stringify(config, null, 2) }}
                        >
                          <pre className="json code-block">
                            {JSON.stringify(config, null, 2)}
                          </pre>
                        </Typography.Paragraph>
                      ),
                    }))}
                  />
                </>
              ),
            },
          ]}
        />
      </Card>
      <ResourcePage forced="bindings" group={id} />
    </>
  );
}

function Console() {
  const [submitting, setSubmitting] = useState(false);
  const [session, setSession] = useState<Row | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [menuOpen, setMenuOpen] = useState(false);
  const screens = Grid.useBreakpoint();
  const nav = useNavigate();
  const location = useLocation();
  React.useEffect(() => {
    const expired = () => {
      setSession(null);
      setCsrf("");
      queryClient.clear();
    };
    window.addEventListener(sessionExpiredEvent, expired);
    return () => window.removeEventListener(sessionExpiredEvent, expired);
  }, []);
  React.useEffect(() => {
    api("/me")
      .then((s) => {
        setCsrf(s.csrf);
        setSession(s);
      })
      .catch((e: Error) => {
        if (!(e instanceof ApiError && e.status === 401)) setError(e.message);
      })
      .finally(() => setLoading(false));
  }, []);
  if (loading) return <div className="login">加载会话…</div>;
  if (!session)
    return (
      <div className="login">
        <Card title="MCP Gateway · 管理员登录" style={{ width: 400 }}>
          {error && <Alert type="error" title={error} />}
          <Form
            layout="vertical"
            onFinish={async (values) => {
              if (submitting) return;
              setSubmitting(true);
              setError("");
              try {
                await api("/login", "POST", values);
                // Verify that the browser accepted and sent the session cookie.
                const s = await api("/me");
                setCsrf(s.csrf);
                setSession(s);
              } catch (e) {
                setError(
                  e instanceof ApiError &&
                    e.status === 401 &&
                    e.message.includes("Login required")
                    ? "浏览器未保存或发送登录 Cookie。请检查 HTTPS、COOKIE_SECURE 及跨站 Cookie 设置。"
                    : (e as Error).message,
                );
              } finally {
                setSubmitting(false);
              }
            }}
          >
            <Form.Item
              name="username"
              label="用户名"
              extra="区分大小写；邮箱形式的账号也按完整用户名匹配。"
              rules={[{ required: true }, { max: 128 }]}
            >
              <Input autoComplete="username" maxLength={128} />
            </Form.Item>
            <Form.Item
              name="password"
              label="密码"
              rules={[{ required: true }, { max: 1024 }]}
            >
              <Input.Password autoComplete="current-password" />
            </Form.Item>
            <Button type="primary" htmlType="submit" block loading={submitting}>
              登录
            </Button>
          </Form>
          <Typography.Paragraph type="secondary" style={{ marginTop: 16 }}>
            管理员账号由部署人员使用 gateway admin-create 创建，无需邮箱验证。
            忘记密码请联系部署人员重置。
          </Typography.Paragraph>
        </Card>
      </div>
    );
  const current = location.pathname.split("/")[1] || "groups";
  const menu = (
    <Menu
      selectedKeys={[current]}
      items={[
        { key: "guide", icon: <BookOutlined aria-hidden />, label: "入门指南" },
        {
          type: "group",
          label: "工具与端点",
          children: Object.entries(resources)
            .slice(0, 3)
            .map(([key, label]) => ({ key, label, icon: resourceIcons[key] })),
        },
        {
          type: "group",
          label: "配置与安全",
          children: Object.entries(resources)
            .slice(3, 7)
            .map(([key, label]) => ({ key, label, icon: resourceIcons[key] })),
        },
        { key: "audit", label: resources.audit, icon: resourceIcons.audit },
      ]}
      onClick={({ key }) => {
        nav("/" + key);
        setMenuOpen(false);
      }}
    />
  );
  return (
    <Layout style={{ minHeight: "100vh" }}>
      {screens.lg ? (
        <Layout.Sider width={240} theme="light" className="sidebar">
          <div className="brand">
            <ApiOutlined aria-hidden /> MCP Gateway
            <small>工具接入与访问管理</small>
          </div>
          {menu}
          <div className="sidebar-note">
            工具准备好之后，从端点组开始连接你的智能体。
          </div>
        </Layout.Sider>
      ) : (
        <Drawer
          title="MCP Gateway"
          destroyOnHidden
          placement="left"
          open={menuOpen}
          onClose={() => setMenuOpen(false)}
          width={280}
        >
          {menu}
        </Drawer>
      )}
      <Layout className="main-layout">
        <Layout.Header className="header">
          <Space>
            {!screens.lg && (
              <Button
                aria-label="打开导航"
                icon={<MenuOutlined aria-hidden />}
                onClick={() => setMenuOpen(true)}
              />
            )}
            <Breadcrumb
              items={[
                { title: "控制台" },
                {
                  title:
                    current === "guide"
                      ? "入门指南"
                      : resources[current] || "页面",
                },
                ...(location.pathname.startsWith("/groups/")
                  ? [
                      {
                        title: decodeURIComponent(
                          location.pathname.split("/")[2],
                        ),
                      },
                    ]
                  : []),
              ]}
            />
          </Space>
          <Space>
            <Link to="/guide" className="header-guide">
              <BookOutlined aria-hidden /> 使用指南
            </Link>
            <span className="admin-name">{session.username}</span>
            <Button
              onClick={async () => {
                try {
                  await api("/logout", "POST");
                  setSession(null);
                  setCsrf("");
                  queryClient.clear();
                } catch (e) {
                  if (!(e instanceof ApiError && e.status === 401))
                    window.alert((e as Error).message);
                }
              }}
            >
              退出
            </Button>
          </Space>
        </Layout.Header>
        <Layout.Content className="content">
          <Routes>
            <Route path="/guide" element={<GuidePage />} />
            <Route path="/groups/:id" element={<GroupPage />} />
            <Route
              path="/:resource"
              element={
                resources[current] ? (
                  <ResourcePage key={location.pathname} />
                ) : (
                  <Result
                    status="404"
                    title="页面不存在"
                    extra={<Link to="/groups">返回端点组</Link>}
                  />
                )
              }
            />
            <Route path="/" element={<ResourcePage forced="groups" />} />
          </Routes>
        </Layout.Content>
      </Layout>
    </Layout>
  );
}
createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <ConfigProvider
      locale={zhCN}
      theme={{
        token: {
          colorPrimary: "#3159cf",
          borderRadius: 10,
          colorBgLayout: "#f5f7fb",
          fontFamily: "Inter, system-ui, sans-serif",
        },
        components: {
          Layout: { headerBg: "#ffffff", siderBg: "#ffffff" },
          Menu: { itemHeight: 44 },
        },
      }}
    >
      <App>
        <QueryClientProvider client={queryClient}>
          <BrowserRouter>
            <Console />
          </BrowserRouter>
        </QueryClientProvider>
      </App>
    </ConfigProvider>
  </React.StrictMode>,
);
