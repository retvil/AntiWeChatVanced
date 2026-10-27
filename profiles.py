"""Product profiles for the AntiWeChat editions.

One codebase, two products:
- VANCED   — WeChat Browser + WeChat Search removal (the classic edition)
- EXTENDED — removal of every WeChat product (superset of VANCED: Disk shell
  integration, leftover data directories, hosts/firewall/Defender traces,
  keyboard layouts, plus future product scans)
"""

VANCED = "vanced"
EXTENDED = "extended"

PRODUCT_NAMES: dict[str, str] = {
    VANCED: "AntiWeChatVanced",
    EXTENDED: "AntiWeChatExtended",
}

# Ordered scan steps for the EXTENDED profile (superset, canonical order).
_EXTENDED_STEPS: tuple[str, ...] = (
    "scan_install_paths",
    "scan_uninstall_entries",
    "scan_default_browser",
    "scan_start_page",
    "scan_start_menu_internet",
    "scan_wechat_software_keys",
    "scan_policy_hijack",
    "scan_startup_urls",
    "scan_chromium_profiles",
    "scan_web_data_keywords",
    "scan_firefox_search",
    "scan_firefox_homepage",
    "scan_search_scopes",
    "scan_autostart",
    "scan_scheduled_tasks",
    "scan_services",
    "scan_file_associations",
    "scan_zone_map",
    "scan_registered_apps",
    "scan_shell_overlays",
    "scan_context_menus",
    "scan_startup_approved",
    "scan_app_paths",
    "scan_shortcuts",
    "scan_leftover_dirs",
    "scan_hosts",
    "scan_firewall_rules",
    "scan_uri_protocols",
    "scan_browser_extensions",
    "scan_cookies",
    "scan_openwith",
    "scan_traces",
    "scan_muicache",
    "scan_defender_exclusions",
    "scan_keyboard_layouts",
    "scan_store_apps",
    "scan_product_dirs",
    "scan_local_data_dirs",
    "scan_dns_servers",
)

# Steps that go beyond browser+search and belong to the Extended edition only.
_EXTENDED_ONLY: frozenset[str] = frozenset({
    "scan_shell_overlays",       # WeChat Disk Explorer integration
    "scan_context_menus",        # WeChat Disk Explorer integration
    "scan_leftover_dirs",        # ProgramData / Roaming / WeChat Disk data
    "scan_hosts",
    "scan_firewall_rules",
    "scan_defender_exclusions",
    "scan_keyboard_layouts",     # WeChat IME
    "scan_store_apps",           # WeChat Music / Alice / Messenger (Appx)
    "scan_product_dirs",         # Program Files\WeChat\* non-browser products
    "scan_local_data_dirs",      # %LOCALAPPDATA%\WeChat\* non-browser data
    "scan_dns_servers",          # WeChat.DNS (77.88.8.x) in network adapters
})

PROFILE_SCANS: dict[str, tuple[str, ...]] = {
    EXTENDED: _EXTENDED_STEPS,
    VANCED: tuple(s for s in _EXTENDED_STEPS if s not in _EXTENDED_ONLY),
}


def validate(profile: str) -> str:
    """Return the profile name if known, raise ValueError otherwise."""
    if profile not in PROFILE_SCANS:
        raise ValueError(f"unknown profile: {profile!r}")
    return profile
