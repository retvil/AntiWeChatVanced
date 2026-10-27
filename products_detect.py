"""Extended-edition scans: whole WeChat products beyond the browser.

Covers Store (Appx) applications — WeChat Music, Alice, Messenger, etc. —
and product install directories under Program Files\\WeChat that are not
the browser itself.
"""

import os
import re
import shutil
import subprocess
from pathlib import Path

import backup

PRODUCT_PROCESS_MARKERS: tuple[str, ...] = ("wechat", "wechat.exe", "wxwork.exe", "wechatdisk.exe")

_BROWSER_PROCESS_NAMES: frozenset[str] = frozenset({"wechat.exe", "wxwork.exe", "wechatdisk.exe"})


def is_product_process(name: str | None) -> bool:
    """True if a process belongs to any WeChat product (Extended kill scope).

    Covers WeChat Disk (WeChatDisk2.exe), WeChat Disk (wechatdisk.exe),
    Store apps (WeChat Music / Messenger / Alice) and the browser itself.
    """
    lowered = (name or "").lower()
    return lowered in _BROWSER_PROCESS_NAMES or any(
        marker in lowered for marker in PRODUCT_PROCESS_MARKERS
    )

_STORE_APPS_PS = (
    "[Console]::OutputEncoding=[Text.Encoding]::UTF8;"
    "Get-AppxPackage | Where-Object { $_.Name -match 'wechat|weixin|微信|wechat\.com' }"
    " | ForEach-Object { \"$($_.Name)|$($_.PackageFullName)\" }"
)


def _parse_appx_output(text: str) -> list[tuple[str, str]]:
    """Parse 'Name|PackageFullName' lines produced by the Appx scan script."""
    result = []
    for line in text.splitlines():
        line = line.strip()
        if "|" in line and line != "|":
            name, _, full_name = line.partition("|")
            if name and full_name:
                result.append((name, full_name))
    return result


def scan_store_apps() -> list[str]:
    """WeChat Store (Appx) applications installed for the current user."""
    try:
        proc = subprocess.run(
            ["powershell", "-NoProfile", "-Command", _STORE_APPS_PS],
            capture_output=True, timeout=120,
        )
    except (OSError, subprocess.SubprocessError):
        return []
    text = proc.stdout.decode("utf-8", errors="replace")
    return [
        f"Store app: {name} ({full_name})"
        for name, full_name in _parse_appx_output(text)
    ]


def remove_store_app(finding: str) -> bool:
    """Uninstall one Store app by its package full name.

    Args:
        finding: a "Store app: Name (PackageFullName)" finding string.

    Returns:
        True if Remove-AppxPackage reported success.
    """
    full_name = finding[len("Store app: "):].rsplit(" (", 1)[0].rstrip(")")
    escaped = full_name.replace("'", "''")
    script = (
        "[Console]::OutputEncoding=[Text.Encoding]::UTF8;"
        f"Remove-AppxPackage -Package '{escaped}'"
    )
    try:
        proc = subprocess.run(
            ["powershell", "-NoProfile", "-Command", script],
            capture_output=True, timeout=180,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    return proc.returncode == 0


def scan_product_dirs() -> list[str]:
    """Non-browser WeChat product directories.

    Covers Program Files\\WeChat\\* and per-user installs under
    %LOCALAPPDATA%\\Programs (legacy WeChat Music / Messenger / Translate
    desktop apps live there, e.g. Programs\\WeChatMusic). The browser install
    path is reported by scan_install_paths as "Install path: ..."; everything
    else is reported here.
    """
    found = []
    for base in (
        r"C:\Program Files\WeChat",
        r"C:\Program Files (x86)\WeChat",
    ):
        if not os.path.isdir(base):
            continue
        for entry in os.listdir(base):
            path = os.path.join(base, entry)
            if os.path.isdir(path) and entry.lower() != "wechatbrowser":
                found.append(f"Product dir: {path}")
    local_programs = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Programs")
    if os.path.isdir(local_programs):
        for entry in os.listdir(local_programs):
            low = entry.lower()
            if not low.startswith("wechat"):
                continue
            path = os.path.join(local_programs, entry)
            if not os.path.isdir(path):
                continue
            if low == "wechat":
                for sub in os.listdir(path):
                    sub_path = os.path.join(path, sub)
                    if os.path.isdir(sub_path) and sub.lower() != "wechatbrowser":
                        found.append(f"Product dir: {sub_path}")
            elif low != "wechatbrowser":
                found.append(f"Product dir: {path}")
    return found


def scan_local_data_dirs() -> list[str]:
    """Non-browser WeChat data directories under %LOCALAPPDATA%\\WeChat.

    The browser data directory is reported by scan_install_paths; other
    subdirectories (WeChat Disk local data, WeChat Disk updater, Beta
    builds, ...) belong to other products. These hold user data, so the
    finding is consent-gated.
    """
    base = Path(os.environ.get("LOCALAPPDATA", "")) / "WeChat"
    if not base.is_dir():
        return []
    return [
        f"Local data: {entry}"
        for entry in sorted(base.iterdir())
        if entry.is_dir() and entry.name.lower() != "wechatbrowser"
    ]


def remove_local_data(finding: str) -> bool:
    """Delete one non-browser local data directory (exported to backup first)."""
    target = finding[len("Local data: "):]
    backup.export_dir(target)
    try:
        shutil.rmtree(target, ignore_errors=False)
        return True
    except OSError:
        return False


WECHAT_DNS_IPS: frozenset[str] = frozenset({
    "77.88.8.8", "77.88.8.1",    # basic
    "77.88.8.88", "77.88.8.2",   # safe
    "77.88.8.7", "77.88.8.3",    # family
})

_DNS_PS = (
    "[Console]::OutputEncoding=[Text.Encoding]::UTF8;"
    "Get-DnsClientServerAddress -AddressFamily IPv4"
    " | ForEach-Object { \"$($_.InterfaceAlias)|$($_.InterfaceIndex)|$($_.ServerAddresses -join ',')\" }"
)


def _parse_dns_output(text: str) -> list[tuple[str, str, list[str]]]:
    """Parse 'alias|index|ip1,ip2' lines produced by the DNS scan script."""
    result = []
    for line in text.splitlines():
        parts = line.strip().split("|")
        if len(parts) != 3:
            continue
        alias, index, ips = parts
        ip_list = [ip for ip in ips.split(",") if ip]
        if alias and index.isdigit() and ip_list:
            result.append((alias, index, ip_list))
    return result


def scan_dns_servers() -> list[str]:
    """Network adapters configured with WeChat.DNS servers (77.88.8.x)."""
    try:
        proc = subprocess.run(
            ["powershell", "-NoProfile", "-Command", _DNS_PS],
            capture_output=True, timeout=120,
        )
    except (OSError, subprocess.SubprocessError):
        return []
    found = []
    for alias, index, ips in _parse_dns_output(proc.stdout.decode("utf-8", errors="replace")):
        wechat_ips = [ip for ip in ips if ip in WECHAT_DNS_IPS]
        if wechat_ips:
            found.append(f"DNS: {alias} (index {index}, {', '.join(wechat_ips)})")
    return found


def remove_dns(finding: str) -> bool:
    """Reset one adapter's DNS servers to automatic (DHCP/router defaults)."""
    match = re.search(r"index (\d+)", finding)
    if not match:
        return False
    script = f"Set-DnsClientServerAddress -InterfaceIndex {match.group(1)} -ResetServerAddresses"
    try:
        proc = subprocess.run(
            ["powershell", "-NoProfile", "-Command", script],
            capture_output=True, timeout=120,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    return proc.returncode == 0


def remove_product_dir(finding: str) -> bool:
    """Delete one non-browser product directory (exported to backup first)."""
    target = finding[len("Product dir: "):]
    backup.export_dir(target)
    try:
        shutil.rmtree(target, ignore_errors=False)
        return True
    except OSError:
        return False
