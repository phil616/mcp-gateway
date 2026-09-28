import re
from typing import NamedTuple

from gateway_sdk import ToolPackage

package = ToolPackage(id="emailutils", version="1.0.0")

LOCAL_PART_LIMIT = 64
DOMAIN_LIMIT = 255
ADDRESS_LIMIT = 254

ATEXT = r"A-Za-z0-9!#$%&'*+\-/=?^_`{|}~"
DOT_STRING = re.compile(rf"[{ATEXT}]+(?:\.[{ATEXT}]+)*")
QUOTED_STRING = re.compile(r'"(?:[\x20\x21\x23-\x5b\x5d-\x7e]|\\[\x20-\x7e])*"')
LABEL = r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?"
DOMAIN = re.compile(rf"{LABEL}(?:\.{LABEL})*")
ADDRESS_LITERAL = re.compile(r"\[(?:[\x21-\x5a\x5e-\x7e]|\\[\x20-\x7e])*\]")
FORBIDDEN = re.compile(r"[\x00-\x20\x7f]")


class Parsed(NamedTuple):
    valid: bool
    error: str | None
    local: str | None
    domain: str | None
    warnings: list[str]


def split(address: str) -> tuple[str, str] | None:
    if address.startswith('"'):
        index = 1
        while index < len(address):
            char = address[index]
            if char == "\\":
                index += 2
                continue
            if char == '"':
                break
            index += 1
        else:
            return None
        remainder = address[index + 1 :]
        if not remainder.startswith("@"):
            return None
        return address[: index + 1], remainder[1:]
    if address.count("@") != 1:
        return None
    local, domain = address.split("@")
    return local, domain


def detail(part: str) -> str:
    if FORBIDDEN.search(part):
        return "whitespace and control characters are not allowed here"
    return "expected a dot-string or quoted-string"


def domain_detail(part: str) -> str:
    if FORBIDDEN.search(part):
        return "whitespace and control characters are not allowed here"
    return "expected a subdomain sequence or an address literal"


def check(address: str) -> Parsed:
    if not address:
        return Parsed(False, "empty address", None, None, [])
    if not address.isascii():
        return Parsed(False, "non-ASCII mailbox; SMTPUTF8 (RFC 6531) is not accepted", None, None, [])
    if len(address.encode()) > ADDRESS_LIMIT:
        return Parsed(False, f"address exceeds the {ADDRESS_LIMIT} octet limit", None, None, [])
    parts = split(address)
    if parts is None:
        return Parsed(False, "expected exactly one local-part@domain mailbox", None, None, [])
    local, domain = parts
    if len(local.encode()) > LOCAL_PART_LIMIT:
        return Parsed(False, f"local-part exceeds {LOCAL_PART_LIMIT} octets", None, None, [])
    if not (DOT_STRING.fullmatch(local) or QUOTED_STRING.fullmatch(local)):
        return Parsed(False, f"local-part rejected: {detail(local)}", local, domain, [])
    if len(domain.encode()) > DOMAIN_LIMIT:
        return Parsed(False, f"domain exceeds {DOMAIN_LIMIT} octets", local, domain, [])
    if not (DOMAIN.fullmatch(domain) or ADDRESS_LITERAL.fullmatch(domain)):
        return Parsed(False, f"domain rejected: {domain_detail(domain)}", local, domain, [])
    warnings: list[str] = []
    if QUOTED_STRING.fullmatch(local):
        warnings.append("local-part is quoted, treat it as opaque and case-sensitive")
    elif "+" in local:
        warnings.append("local-part carries a subaddress tag, it may not be a real mailbox")
    if ADDRESS_LITERAL.fullmatch(domain):
        warnings.append("domain is an address literal, not a resolvable name")
    elif "." not in domain:
        warnings.append("domain has a single label and is not a fully qualified domain name")
    return Parsed(True, None, local, domain, warnings)


@package.tool(id="check_rfc5321", timeout=5)
def check_rfc5321(email: str) -> dict[str, object]:
    """判断邮箱是否满足 RFC 5321 邮箱（Mailbox）语法与长度限制。

    校验 local-part（dot-string 或 quoted-string）、domain（子域序列或 address literal）
    以及 octet 长度上限 64/255/254；语法之外不接受空白与控制字符，非 ASCII 邮箱（SMTPUTF8 / RFC 6531）
    一律判为不符合（quoted-string 内部的空格除外，它在 RFC 5321 里合法）。
    仅做语法判断：不联网验证域名或邮箱是否真实存在。
    返回 valid、error、local_part、domain 和 warnings；warnings 只提示可送达性风险，不影响 valid。
    """
    parsed = check(email)
    return {
        "valid": parsed.valid,
        "error": parsed.error,
        "local_part": parsed.local,
        "domain": parsed.domain,
        "warnings": parsed.warnings,
    }


@package.tool(id="strip_subaddress", timeout=5)
def strip_subaddress(email: str, lowercase: bool = False) -> dict[str, object]:
    """把带子地址的邮箱还原为通用（唯一）邮箱：alice+git@example.com → alice@example.com。

    取 local-part 中第一个 "+" 之前的部分作为通用邮箱，并返回剥离出的 tag。
    输入必须先通过 RFC 5321 语法校验；带引号的 local-part（如 "a+b"@example.com）中的 "+" 是字面字符，
    不做剥离而是返回错误。lowercase=True 时对结果整体转小写（local-part 理论上大小写敏感，默认不转换）。
    输入本来就没有子地址时，base 与输入相同且 tag 为 null。校验失败返回 ok=false 与 error，不抛异常。
    """
    parsed = check(email)
    if not parsed.valid or parsed.local is None or parsed.domain is None:
        return {"ok": False, "error": parsed.error, "base": None, "tag": None}
    if QUOTED_STRING.fullmatch(parsed.local):
        return {
            "ok": False,
            "error": "quoted local-part keeps '+' literal, refusing to strip",
            "base": None,
            "tag": None,
        }
    local, marker, tag = parsed.local.partition("+")
    if marker and not tag:
        return {"ok": False, "error": "subaddress tag after '+' is empty", "base": None, "tag": None}
    base = f"{local}@{parsed.domain}"
    if lowercase:
        base = base.lower()
    return {"ok": True, "error": None, "base": base, "tag": tag or None}


@package.tool(id="add_subaddress", timeout=5)
def add_subaddress(base: str, tag: str) -> dict[str, object]:
    """给通用邮箱加子地址标签：alice@example.com 加标签 info → alice+info@example.com。

    base 必须是已通过 RFC 5321 校验、且 local-part 中不含 "+" 的通用邮箱。
    tag 不能为空，不能含 "@"、空白或控制字符，拼接后仍需满足 64 octet 的 local-part 上限。
    校验失败返回 ok=false 与 error，不抛异常。
    """
    parsed = check(base)
    if not parsed.valid or parsed.local is None or parsed.domain is None:
        return {"ok": False, "error": parsed.error, "email": None}
    if QUOTED_STRING.fullmatch(parsed.local):
        return {
            "ok": False,
            "error": "quoted local-part cannot carry a subaddress tag",
            "email": None,
        }
    if "+" in parsed.local:
        return {
            "ok": False,
            "error": "base already carries a subaddress, pass the address without '+'",
            "email": None,
        }
    if not tag:
        return {"ok": False, "error": "tag must not be empty", "email": None}
    if "@" in tag or FORBIDDEN.search(tag):
        return {"ok": False, "error": "tag must not contain '@' or whitespace", "email": None}
    email = f"{parsed.local}+{tag}@{parsed.domain}"
    composed = check(email)
    if not composed.valid:
        return {"ok": False, "error": f"tag breaks the local-part: {composed.error}", "email": None}
    return {"ok": True, "error": None, "email": email}
