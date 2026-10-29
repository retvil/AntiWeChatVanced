# AntiWeChat Vanced

[![1.1.0](https://img.shields.io/badge/version-1.1.0-brightgreen)](https://github.com/retvil/AntiWeChatVanced/releases) [![Platform Windows](https://img.shields.io/badge/platform-Windows-blue)](https://github.com/retvil/AntiWeChatVanced/releases) [![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)

**Remove WeChat Browser completely and lock your default search against hijacking — 28 detection vectors (VANCED) / 39 detection vectors (EXTENDED), 10 search engines, 10 UI languages.**

## 🌐 Forks

<a href="https://github.com/retvil/AntiBaiduVanced"><img src="https://raw.githubusercontent.com/retvil/AntiBaiduVanced/main/logo.png" alt="AntiBaiduVanced" width="16" height="16" style="vertical-align:middle"> AntiBaiduVanced</a>  |  <a href="https://github.com/retvil/AntiSogouVanced"><img src="https://raw.githubusercontent.com/retvil/AntiSogouVanced/main/logo.png" alt="AntiSogouVanced" width="16" height="16" style="vertical-align:middle"> AntiSogouVanced</a>  |  <a href="https://github.com/retvil/Anti2345Vanced"><img src="https://raw.githubusercontent.com/retvil/Anti2345Vanced/main/logo.png" alt="Anti2345Vanced" width="16" height="16" style="vertical-align:middle"> Anti2345Vanced</a>  |  <a href="https://github.com/retvil/AntiUCWebVanced"><img src="https://raw.githubusercontent.com/retvil/AntiUCWebVanced/main/logo.png" alt="AntiUCWebVanced" width="16" height="16" style="vertical-align:middle"> AntiUCWebVanced</a>  |  <a href="https://github.com/retvil/AntiNaverVanced"><img src="https://raw.githubusercontent.com/retvil/AntiNaverVanced/main/logo.png" alt="AntiNaverVanced" width="16" height="16" style="vertical-align:middle"> AntiNaverVanced</a>  |  <a href="https://github.com/retvil/AntiKakaoVanced"><img src="https://raw.githubusercontent.com/retvil/AntiKakaoVanced/main/logo.png" alt="AntiKakaoVanced" width="16" height="16" style="vertical-align:middle"> AntiKakaoVanced</a>  |  <a href="https://github.com/retvil/AntiQQVanced"><img src="https://raw.githubusercontent.com/retvil/AntiQQVanced/main/logo.png" alt="AntiQQVanced" width="16" height="16" style="vertical-align:middle"> AntiQQVanced</a>  |  **AntiWeChatVanced**  |  <a href="https://github.com/retvil/AntiTencentVideoVanced"><img src="https://raw.githubusercontent.com/retvil/AntiTencentVideoVanced/main/logo.png" alt="AntiTencentVideoVanced" width="16" height="16" style="vertical-align:middle"> AntiTencentVideoVanced</a>  |  <a href="https://github.com/retvil/AntiVKGroupVanced"><img src="https://raw.githubusercontent.com/retvil/AntiVKGroupVanced/main/logo.png" alt="AntiVKGroupVanced" width="16" height="16" style="vertical-align:middle"> AntiVKGroupVanced</a>  |  <a href="https://github.com/retvil/AntiYandexVanced"><img src="https://raw.githubusercontent.com/retvil/AntiYandexVanced/main/logo.png" alt="AntiYandexVanced" width="16" height="16" style="vertical-align:middle"> AntiYandexVanced</a>

## 🌐 Languages

**🇬🇧 English** | [🇷🇺 Русский](docs/README.ru.md) | [🇺🇦 Українська](docs/README.uk.md) | [🇰🇿 Қазақша](docs/README.kk.md) | [🇩🇪 Deutsch](docs/README.de.md) | [🇫🇷 Français](docs/README.fr.md) | [🇪🇸 Español](docs/README.es.md) | [🇵🇱 Polski](docs/README.pl.md) | [🇹🇷 Türkçe](docs/README.tr.md) | [🇨🇳 中文](docs/README.zh.md)



## What is this?

WeChat doesn't just install a browser — it quietly registers itself as the default search and browser through multiple system mechanisms: registry associations, enterprise policies, per-profile browser settings, even search-engine databases inside Chromium profiles. Removing the browser alone doesn't undo all of that.

**AntiWeChat Vanced** (a fork of [retvil/AntiYandexVanced](https://github.com/retvil/AntiYandexVanced)) finds **all hijack vectors** (28 in VANCED, 39 in EXTENDED), removes them with one click, and then **hard-locks your default search** to an engine of your choice via Windows enterprise policies — so nothing can silently take it back.

## Features

- **Hijack scanner** — detects 28 vectors (VANCED) / 39 vectors (EXTENDED): install paths, uninstall registry entries, `UserChoice` default-browser association, `StartMenuInternet` registrations, `Software\WeChat` key trees, `DefaultSearchProvider*` policy hijack, Chromium profile `Preferences`, `Web Data` SQLite keywords, Firefox `search.json.mozlz4`, legacy `SearchScopes`, autostart entries, scheduled tasks, Windows services, IME Switcher, file associations, WeChat Disk shell integration, disabled autostart, App Paths, shortcuts, ProgramData/Roaming leftovers, hosts entries, firewall rules, URI protocols, browser extensions, wechat.ru cookies, open-with associations, Prefetch/WER traces, Defender exclusions, keyboard layouts, IE Start Page hijack, startup-URL policies (`RestoreOnStartupURLs`), Firefox homepage, IE zone map, RegisteredApplications entries, MUICache traces, %TEMP% installers, Store apps (WeChat Music), product directories, local data directories, WeChat.DNS
- **One-click removal** — every detected vector is removed with a dedicated remover; locked databases are reported, never crash
- **Hard search policy** — locks the default search to one of 10 engines (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia, Yahoo, SearXNG) via HKLM policies for Chrome, Edge, Brave, Vivaldi, Opera and WeChat Browser, plus `policies.json` for Firefox/Waterfox
- **Policy cleanup** — strips WeChat `DefaultSearchProvider*` values from the registry
- **10 UI languages** — ru, en, uk, kk, de, fr, es, pl, tr, zh; system language auto-detected
- **Light UI** — ttkbootstrap, vertical layout, pinned status bar and footer

## Screenshot

<details>
<summary>Main window</summary>

![AntiWeChatVanced main window](docs/screenshot.png)

</details>

## Ready builds

Download from [Releases](https://github.com/retvil/AntiWeChatVanced/releases):

- **Windows** — `AntiWeChatVanced.exe` (portable, single file, ~35 MB) — removes WeChat Browser and WeChat Search
- **Windows** — `AntiWeChatExtended.exe` (portable, single file, ~35 MB) — removal of every WeChat product (WeChat Disk, IME Switcher history, system-wide traces, Store apps, WeChat.DNS)

Run it **as administrator** — HKLM policies and registry cleanup require elevated rights.

## Install from source

Requires Python 3.10+ ([python.org](https://python.org)).

```bash
git clone https://github.com/retvil/AntiWeChatVanced.git
cd AntiWeChatVanced
pip install psutil ttkbootstrap
python main.py
```

Build your own EXE: run `build.bat` (PyInstaller, output in `dist/`).

## Usage

1. **Kill Processes** → **Search WeChat** → **Delete WeChat** — remove the browser itself.
2. **Scan Search Hijacks** — lists every way WeChat hooked into your system.
3. **Remove Hijacks** — close all browsers first, then remove everything found.
4. Pick an engine → **Apply Policy** — your default search is now locked system-wide.

## FAQ

- **Why administrator?** Default-search policies live in HKLM and hijack cleanup touches system registry — both need elevation.
- **"Database locked" in results?** A Chromium browser was running during cleanup. Close all browsers and run the removal again.
- **How do I undo the search policy?** The **Remove WeChat Policies** button strips the policy values; Firefox users can also delete the `distribution\policies.json` file.

## Author & support

Author: **Nod33Eset**. Original idea: [TheCawa/AntiYandex](https://github.com/TheCawa/AntiYandex). We have moved well beyond a simple fork. Issues and PRs are welcome.

If the tool saved you from WeChat, you can support development:

**Crypto:**

- BTC: `bc1qunld3rsp37qf5gg69aune50y0qqkd0eugg7j97`
- TON: `UQDmvr4SKOxSION3Yky6aOgzAnCDXySPuAbG4EKJa5JUT7tC`
- USDT (TRC20): `TBPJSSLu1mUcX54g9UyxUohYGf2fuRvbwd`
- USDT (ERC20): `0x25CAED3776Ef5b18E03392bC5b254Bbd78E8180C`
- USDT (SOL): `3qgN5z291CEcj2FUi2Zza5DioxKgNw72kC7P52pCcTrG`

## License

MIT — see [LICENSE](LICENSE).











