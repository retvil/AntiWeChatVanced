"""Unit tests for pure logic: engine lookup, Firefox policies.json, LZ4 decompressor.

No GUI, no registry, no network - everything runs on CPU in milliseconds.
"""

import json
import struct

import pytest

import engines
import policies
import profiles
import wechat_detect


# --- engines -------------------------------------------------------------------


def test_get_engine_returns_matching_engine():
    engine = engines.get_engine("DuckDuckGo")
    assert engine.name == "DuckDuckGo"
    assert "duckduckgo.com" in engine.search_url


def test_get_engine_unknown_name_raises_keyerror():
    with pytest.raises(KeyError):
        engines.get_engine("WeChat")


def test_all_engines_have_unique_names_and_valid_urls():
    names = [e.name for e in engines.SEARCH_ENGINES]
    assert len(names) == len(set(names))
    for engine in engines.SEARCH_ENGINES:
        assert "{searchTerms}" in engine.search_url
        assert engine.search_url.startswith("https://")


# --- Firefox policies.json -----------------------------------------------------


def test_firefox_policies_json_with_suggest_url():
    engine = engines.get_engine("Google")
    doc = policies._firefox_policies_json(engine)
    entry = doc["policies"]["SearchEngines"]["Add"][0]
    assert entry["Name"] == "Google"
    assert "SuggestURLTemplate" in entry


def test_firefox_policies_json_without_suggest_url_has_no_null():
    engine = engines.SearchEngine(
        name="Custom", keyword="custom", search_url="https://c.example/?q={searchTerms}"
    )
    doc = policies._firefox_policies_json(engine)
    entry = doc["policies"]["SearchEngines"]["Add"][0]
    assert "SuggestURLTemplate" not in entry
    serialized = json.dumps(doc)
    assert "null" not in serialized


# --- LZ4 block decompressor ----------------------------------------------------


def _lz4_compress_literals_only(data: bytes) -> bytes:
    out = bytearray()
    src = 0
    while src < len(data):
        chunk = data[src:src + 65535]
        lit_len = len(chunk)
        token = (lit_len if lit_len < 15 else 15) << 4
        out.append(token)
        if lit_len >= 15:
            remaining = lit_len - 15
            while remaining >= 255:
                out.append(255)
                remaining -= 255
            out.append(remaining)
        out += chunk
        src += lit_len
    out.append(0)
    return bytes(out)


def test_lz4_decompress_literals_only_roundtrip():
    original = b"Hello, WeChat removal!" * 100
    compressed = _lz4_compress_literals_only(original)
    size = len(original)
    result = wechat_detect._lz4_block_decompress(compressed, size)
    assert result == original


def test_lz4_decompress_with_match():
    token = (3 << 4) | 2
    block = bytes([token]) + b"abc" + struct.pack("<H", 3)
    assert wechat_detect._lz4_block_decompress(block, 9) == b"abcabcabc"


def test_lz4_decompress_corrupt_offset_raises():
    block = bytes([0x00]) + struct.pack("<H", 0)
    with pytest.raises(ValueError):
        wechat_detect._lz4_block_decompress(block, 100)


# --- markers -------------------------------------------------------------------


def test_is_wechat_positive_markers():
    for text in ("WeChat", "微信", "https://wechat.com/search", "wechat.com"):
        assert wechat_detect._is_wechat(text)


def test_is_wechat_negative():
    for text in ("Google Chrome", "Mozilla Firefox", "https://google.com", ""):
        assert not wechat_detect._is_wechat(text)


# --- scheduled tasks parsing ---------------------------------------------------


def test_decode_schtasks_utf8():
    assert wechat_detect._decode_schtasks("TaskName,Status\n".encode("utf-8")) == "TaskName,Status\n"


def test_scan_scheduled_tasks_handles_missing_schtasks(monkeypatch):
    def boom(*args, **kwargs):
        raise FileNotFoundError("schtasks")
    monkeypatch.setattr(wechat_detect.subprocess, "run", boom)
    assert wechat_detect.scan_scheduled_tasks() == []


# --- exclusions ----------------------------------------------------------------


def test_exclusions_roundtrip(tmp_path, monkeypatch):
    import exclusions
    monkeypatch.setattr(exclusions, "EXCLUSIONS_FILE", tmp_path / "exclusions.json")
    monkeypatch.setattr(exclusions, "BASE_DIR", tmp_path)
    assert exclusions.load() == set()
    exclusions.add("Service: WeChatUpdaterService (WeChat Updater)")
    assert exclusions.is_excluded("Service: WeChatUpdaterService (WeChat Updater)")
    assert not exclusions.is_excluded("Scheduled task: WeChatUpdate")
    exclusions.clear()
    assert exclusions.load() == set()


def test_exclusions_load_corrupt_file_returns_empty(tmp_path, monkeypatch):
    import exclusions
    bad = tmp_path / "exclusions.json"
    bad.write_text("{not json", encoding="utf-8")
    monkeypatch.setattr(exclusions, "EXCLUSIONS_FILE", bad)
    assert exclusions.load() == set()


# --- extended vectors (16-30) ---------------------------------------------------


def test_lnk_mentions_wechat_ascii_and_utf16(tmp_path):
    import wechat_detect
    plain = tmp_path / "plain.lnk"
    plain.write_bytes(b"\x00\x01chrome" + b"\x00" * 32)
    assert not wechat_detect._lnk_mentions_wechat(plain)
    ascii_lnk = tmp_path / "ascii.lnk"
    ascii_lnk.write_bytes(b"\x00\x01" + b"C:\\wechat\\browser.exe" + b"\x00" * 8)
    assert wechat_detect._lnk_mentions_wechat(ascii_lnk)


def test_hosts_wechat_lines_skips_comments_and_other_domains():
    text = "\n".join([
        "# comment wechat.com",
        "127.0.0.1 wechat.com",
        "  0.0.0.0 wechat.com  ",
        "1.2.3.4 google.com",
        "",
    ])
    lines = wechat_detect._hosts_wechat_lines(text)
    assert lines == ["127.0.0.1 wechat.com", "0.0.0.0 wechat.com"]


def test_parse_firewall_output():
    text = "\nRule1|Display One\n\nRule2|Display Two\n|\n"
    assert wechat_detect._parse_firewall_output(text) == [
        ("Rule1", "Display One"),
        ("Rule2", "Display Two"),
    ]


def test_consent_prefixes_cover_consent_findings():
    samples = [
        "Roaming: C:\\Users\\X\\AppData\\Roaming\\Tencent",
        "Extension: C:\\Users\\X\\...\\Extensions\\abc",
        "Cookies: Google Chrome [Default] (3 rows)",
        "Defender exclusion: C:\\Tencent",
    ]
    for sample in samples:
        assert sample.startswith(wechat_detect.CONSENT_PREFIXES), sample


def test_new_scan_functions_return_lists():
    for name in (
        "scan_shell_overlays", "scan_context_menus", "scan_startup_approved",
        "scan_app_paths", "scan_shortcuts", "scan_leftover_dirs", "scan_hosts",
        "scan_firewall_rules", "scan_uri_protocols", "scan_browser_extensions",
        "scan_cookies", "scan_openwith", "scan_traces",
        "scan_defender_exclusions",
    ):
        assert isinstance(getattr(wechat_detect, name)(), list), name


# --- product profiles (Vanced / Extended) ---------------------------------------


def test_profile_steps_reference_existing_scan_functions():
    for profile, steps in profiles.PROFILE_SCANS.items():
        for name in steps:
            assert callable(getattr(wechat_detect, name, None)), (profile, name)


def test_extended_is_superset_of_vanced():
    assert set(profiles.PROFILE_SCANS[profiles.VANCED]) < set(
        profiles.PROFILE_SCANS[profiles.EXTENDED]
    )


def test_vanced_excludes_product_wide_vectors():
    vanced = set(profiles.PROFILE_SCANS[profiles.VANCED])
    for name in (
        "scan_shell_overlays", "scan_context_menus", "scan_leftover_dirs",
        "scan_hosts", "scan_firewall_rules", "scan_defender_exclusions",
        "scan_store_apps", "scan_product_dirs", "scan_local_data_dirs",
    ):
        assert name not in vanced, name


def test_validate_rejects_unknown_profile():
    with pytest.raises(ValueError):
        profiles.validate("nope")


def test_scan_all_vanced_runs_and_is_list():
    assert isinstance(wechat_detect.scan_all(profiles.VANCED), list)


def test_scan_all_default_is_extended():
    import inspect
    signature = inspect.signature(wechat_detect.scan_all)
    assert signature.parameters["profile"].default is None


# --- Extended product scans (Store apps, product dirs) ---------------------------


def test_parse_appx_output():
    import products_detect
    text = "ABC123.WeChat.Music|ABC123.WeChat.Music_4.54_x64__vfvw9svesycw6\n\njunk\n|"
    parsed = products_detect._parse_appx_output(text)
    assert parsed == [
        ("ABC123.WeChat.Music", "ABC123.WeChat.Music_4.54_x64__vfvw9svesycw6"),
    ]


def test_scan_store_apps_returns_list():
    import products_detect
    assert isinstance(products_detect.scan_store_apps(), list)


def test_remove_one_store_app_and_product_dir_dispatch(monkeypatch):
    import products_detect
    calls = []
    monkeypatch.setattr(
        products_detect, "remove_store_app",
        lambda finding: calls.append("store") or True,
    )
    monkeypatch.setattr(
        products_detect, "remove_product_dir",
        lambda finding: calls.append("dir") or True,
    )
    removed: list[str] = []
    failed: list[str] = []
    wechat_detect._remove_one("Store app: X (Y)", removed, failed)
    wechat_detect._remove_one("Product dir: C:\\Tencent\\Disk", removed, failed)
    assert calls == ["store", "dir"]
    assert failed == []
    assert removed == ["X (Y)", "C:\\Tencent\\Disk"]


def test_is_product_process_matches_products_and_browser():
    import products_detect
    assert products_detect.is_product_process("wechat.exe") is True
    assert products_detect.is_product_process("wxwork.exe") is True
    assert products_detect.is_product_process("chrome.exe") is False
    assert products_detect.is_product_process("agent-browser-win32-x64.exe") is False
    assert products_detect.is_product_process(None) is False
    assert products_detect.is_product_process("") is False


# --- DNS servers and Start Page vectors ------------------------------------------


def test_parse_dns_output():
    import products_detect
    text = "Ethernet|14|1.2.3.4,5.6.7.8\nWi-Fi|5|\njunk\nbad|line\n"
    parsed = products_detect._parse_dns_output(text)
    assert parsed == [("Ethernet", "14", ["1.2.3.4", "5.6.7.8"])]


def test_scan_dns_servers_returns_list():
    import products_detect
    assert isinstance(products_detect.scan_dns_servers(), list)


def test_scan_start_page_returns_list():
    assert isinstance(wechat_detect.scan_start_page(), list)


def test_start_page_in_vanced_dns_extended_only():
    vanced = set(profiles.PROFILE_SCANS[profiles.VANCED])
    extended = set(profiles.PROFILE_SCANS[profiles.EXTENDED])
    assert "scan_start_page" in vanced
    assert "scan_dns_servers" not in vanced
    assert "scan_dns_servers" in extended


def test_remove_one_dns_and_start_page_dispatch(monkeypatch):
    import products_detect
    calls = []
    monkeypatch.setattr(
        products_detect, "remove_dns",
        lambda finding: calls.append("dns") or True,
    )
    removed: list[str] = []
    failed: list[str] = []
    wechat_detect._remove_one("DNS: Ethernet (index 14, 1.2.3.4)", removed, failed)
    assert calls == ["dns"]
    assert removed == ["Ethernet (index 14, 1.2.3.4)"]
    assert failed == []


def test_consent_prefixes_cover_dns():
    assert "DNS: " in wechat_detect.CONSENT_PREFIXES


# --- Startup URLs and Firefox homepage vectors -----------------------------------


def test_scan_startup_urls_returns_list():
    assert isinstance(wechat_detect.scan_startup_urls(), list)


def test_scan_firefox_homepage_returns_list():
    assert isinstance(wechat_detect.scan_firefox_homepage(), list)


def test_startup_urls_and_firefox_homepage_in_both_editions():
    for name in ("scan_startup_urls", "scan_firefox_homepage"):
        assert name in profiles.PROFILE_SCANS[profiles.VANCED]
        assert name in profiles.PROFILE_SCANS[profiles.EXTENDED]


# --- Zone map, RegisteredApplications and MUICache vectors -----------------------


def test_scan_zone_map_returns_list():
    assert isinstance(wechat_detect.scan_zone_map(), list)


def test_scan_registered_apps_returns_list():
    assert isinstance(wechat_detect.scan_registered_apps(), list)


def test_scan_muicache_returns_list():
    assert isinstance(wechat_detect.scan_muicache(), list)


def test_new_registry_scans_in_both_editions():
    for name in ("scan_zone_map", "scan_registered_apps", "scan_muicache"):
        assert name in profiles.PROFILE_SCANS[profiles.VANCED]
        assert name in profiles.PROFILE_SCANS[profiles.EXTENDED]

