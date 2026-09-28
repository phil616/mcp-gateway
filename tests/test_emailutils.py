import importlib.util
from pathlib import Path

import pytest
from fastmcp import Client, FastMCP
from fastmcp.exceptions import ToolError
from gateway.catalog import Catalog
from gateway_sdk import EmptyConfig

ENTRY = Path(__file__).resolve().parent.parent / "plugins" / "emailutils" / "plugin.py"
ADDRESS_LIMIT = 254


def load_entry():
    spec = importlib.util.spec_from_file_location("emailutils_plugin_under_test", ENTRY)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


plugin = load_entry()

VALID = [
    "alice@example.com",
    "alice+git@example.com",
    "alice.smith+git@sub.example.co.uk",
    "a@b.co",
    "user!#$%&'*+-/=?^_`{|}~@example.com",
    "x@example.museum",
    '"quoted local"@example.com',
    '"a@b"@example.com',
    "alice@[192.0.2.1]",
]

INVALID = [
    "",
    "alice",
    "alice@",
    "@example.com",
    "alice@@example.com",
    "alice+bob@example.com@evil.com",
    ".alice@example.com",
    "alice.@example.com",
    "al..ice@example.com",
    "alice smith@example.com",
    "alice@example .com",
    "alice@exam ple.com",
    "alice@-example.com",
    "alice@example-.com",
    "alice@example..com",
    "alice@.example.com",
    "alice\n@example.com",
    "alice@exämple.com",
    f"{'a' * 65}@example.com",
    f"alice@{'b' * 260}",
    "alice@[192.0.2.1",
]


@pytest.mark.parametrize("address", VALID)
def test_rfc5321_accepts_valid_mailboxes(address):
    assert plugin.check_rfc5321(address)["valid"] is True


@pytest.mark.parametrize("address", INVALID)
def test_rfc5321_rejects_invalid_mailboxes(address):
    result = plugin.check_rfc5321(address)
    assert result["valid"] is False
    assert result["error"]


def test_rfc5321_reports_parsed_parts():
    result = plugin.check_rfc5321("alice+git@example.com")
    assert result["local_part"] == "alice+git"
    assert result["domain"] == "example.com"
    assert result["warnings"]


def test_rfc5321_warns_without_failing_on_subaddress_and_single_label():
    assert plugin.check_rfc5321("alice+git@example.com")["valid"] is True
    single = plugin.check_rfc5321("alice@localhost")
    assert single["valid"] is True
    assert any("fully qualified" in warning for warning in single["warnings"])


def test_rfc5321_enforces_total_length_limit():
    domain = f"{'b' * 63}.{'c' * 63}.{'d' * 61}"
    local = "a" * 64
    assert len(f"{local}@{domain}") == ADDRESS_LIMIT
    assert plugin.check_rfc5321(f"{local}@{domain}")["valid"] is True
    over = plugin.check_rfc5321(f"{local}x@{domain}")
    assert over["valid"] is False
    assert str(ADDRESS_LIMIT) in over["error"]


@pytest.mark.parametrize(
    ("email", "base", "tag"),
    [
        ("alice+git@example.com", "alice@example.com", "git"),
        ("alice+git+ssh@example.com", "alice@example.com", "git+ssh"),
        ("alice.git@example.com", "alice.git@example.com", None),
        ("alice@sub.example.com", "alice@sub.example.com", None),
        ("alice+Git@Example.com", "alice@Example.com", "Git"),
    ],
)
def test_strip_subaddress(email, base, tag):
    result = plugin.strip_subaddress(email)
    assert result == {"ok": True, "error": None, "base": base, "tag": tag}


def test_strip_subaddress_lowercases_on_request():
    result = plugin.strip_subaddress("Alice+Git@Example.COM", lowercase=True)
    assert result["base"] == "alice@example.com"
    assert result["tag"] == "Git"


@pytest.mark.parametrize(
    ("email", "message"),
    [
        ("alice", "local-part"),
        ("alice smith@example.com", "whitespace"),
        ("alice@example .com", "whitespace"),
        ('"a+b"@example.com', "quoted"),
        ("alice+@example.com", "empty"),
    ],
)
def test_strip_subaddress_rejects_unsafe_input(email, message):
    result = plugin.strip_subaddress(email)
    assert result["ok"] is False
    assert result["base"] is None
    assert message in result["error"]


@pytest.mark.parametrize(
    ("base", "tag", "email"),
    [
        ("alice@example.com", "info", "alice+info@example.com"),
        ("alice.smith@sub.example.com", "git", "alice.smith+git@sub.example.com"),
        ("alice@example.com", "a.b", "alice+a.b@example.com"),
        ("alice@example.com", "a+b", "alice+a+b@example.com"),
    ],
)
def test_add_subaddress(base, tag, email):
    assert plugin.add_subaddress(base, tag) == {"ok": True, "error": None, "email": email}


@pytest.mark.parametrize(
    ("base", "tag", "message"),
    [
        ("alice+git@example.com", "info", "already carries"),
        ("alice", "info", "local-part"),
        ("alice@example.com", "", "empty"),
        ("alice@example.com", "in fo", "whitespace"),
        ("alice@example.com", "a@b", "@"),
        ('"quoted"@example.com', "info", "quoted"),
        (f"{'a' * 64}@example.com", "x", "64 octet"),
    ],
)
def test_add_subaddress_rejects_unsafe_input(base, tag, message):
    result = plugin.add_subaddress(base, tag)
    assert result["ok"] is False
    assert result["email"] is None
    assert message in result["error"]


def test_round_trip_is_stable():
    email = plugin.add_subaddress("alice@example.com", "info")["email"]
    assert plugin.strip_subaddress(email)["base"] == "alice@example.com"


def catalog_specs():
    return Catalog(str(ENTRY.parent.parent)).tools


def test_catalog_registers_three_tools_with_business_only_schemas():
    specs = catalog_specs()
    assert {key for key in specs if key.startswith("emailutils.")} == {
        "emailutils.check_rfc5321",
        "emailutils.strip_subaddress",
        "emailutils.add_subaddress",
    }
    assert set(specs["emailutils.check_rfc5321"].tool.parameters["properties"]) == {"email"}
    assert set(specs["emailutils.strip_subaddress"].tool.parameters["properties"]) == {
        "email",
        "lowercase",
    }
    assert set(specs["emailutils.add_subaddress"].tool.parameters["properties"]) == {"base", "tag"}
    for spec in specs.values():
        if spec.id.startswith("emailutils."):
            assert not spec.config_model.model_json_schema().get("properties")
            assert spec.config_model is EmptyConfig


async def test_real_mcp_client_lists_and_calls_the_tools():
    specs = catalog_specs()
    server = FastMCP("emailutils-contract-check")
    for key, spec in specs.items():
        if key.startswith("emailutils."):
            server.add_tool(spec.tool)
    async with Client(server) as client:
        assert {tool.name for tool in await client.list_tools()} == {
            "emailutils.check_rfc5321",
            "emailutils.strip_subaddress",
            "emailutils.add_subaddress",
        }
        checked = await client.call_tool(
            "emailutils.check_rfc5321", {"email": "alice+git@example.com"}
        )
        assert checked.data["valid"] is True
        assert checked.data["local_part"] == "alice+git"
        assert (await client.call_tool(
            "emailutils.check_rfc5321", {"email": "alice@@example.com"}
        )).data["valid"] is False
        stripped = await client.call_tool(
            "emailutils.strip_subaddress", {"email": "alice+git@example.com"}
        )
        assert stripped.data["base"] == "alice@example.com"
        assert stripped.data["tag"] == "git"
        added = await client.call_tool(
            "emailutils.add_subaddress", {"base": "alice@example.com", "tag": "info"}
        )
        assert added.data["email"] == "alice+info@example.com"
        with pytest.raises(ToolError):
            await client.call_tool("emailutils.add_subaddress", {"base": "alice@example.com"})

