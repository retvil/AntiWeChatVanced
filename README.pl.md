# AntiWeChat Vanced

**🇬🇧 English** | [🇷🇺 Русский](README.ru.md) | [🇺🇦 Українська](README.uk.md) | [🇰🇿 Қазақша](README.kk.md) | [🇩🇪 Deutsch](README.de.md) | [🇫🇷 Français](README.fr.md) | [🇪🇸 Español](README.es.md) | [🇵🇱 Polski](README.pl.md) | [🇹🇷 Türkçe](README.tr.md) | [🇨🇳 中文](README.zh.md)

## 🌐 Forks

[![AntiBaiduVanced](https://raw.githubusercontent.com/retvil/AntiBaiduVanced/main/logo.png =16)AntiBaiduVanced](https://github.com/retvil/AntiBaiduVanced)  |  [![AntiSogouVanced](https://raw.githubusercontent.com/retvil/AntiSogouVanced/main/logo.png =16)AntiSogouVanced](https://github.com/retvil/AntiSogouVanced)  |  [![Anti2345Vanced](https://raw.githubusercontent.com/retvil/Anti2345Vanced/main/logo.png =16)Anti2345Vanced](https://github.com/retvil/Anti2345Vanced)  |  [![AntiUCWebVanced](https://raw.githubusercontent.com/retvil/AntiUCWebVanced/main/logo.png =16)AntiUCWebVanced](https://github.com/retvil/AntiUCWebVanced)  |  [![AntiNaverVanced](https://raw.githubusercontent.com/retvil/AntiNaverVanced/main/logo.png =16)AntiNaverVanced](https://github.com/retvil/AntiNaverVanced)  |  [![AntiKakaoVanced](https://raw.githubusercontent.com/retvil/AntiKakaoVanced/main/logo.png =16)AntiKakaoVanced](https://github.com/retvil/AntiKakaoVanced)  |  [![AntiQQVanced](https://raw.githubusercontent.com/retvil/AntiQQVanced/main/logo.png =16)AntiQQVanced](https://github.com/retvil/AntiQQVanced)  |  **AntiWeChatVanced**  |  [![AntiTencentVideoVanced](https://raw.githubusercontent.com/retvil/AntiTencentVideoVanced/main/logo.png =16)AntiTencentVideoVanced](https://github.com/retvil/AntiTencentVideoVanced)  |  [![AntiVKGroupVanced](https://raw.githubusercontent.com/retvil/AntiVKGroupVanced/main/logo.png =16)AntiVKGroupVanced](https://github.com/retvil/AntiVKGroupVanced)  |  [![AntiYandexVanced](https://raw.githubusercontent.com/retvil/AntiYandexVanced/main/logo.png =16)AntiYandexVanced](https://github.com/retvil/AntiYandexVanced)

## Co to jest?

WeChat nie instaluje tylko przeglądarki — po cichu rejestruje się jako domyślna wyszukiwarka i przeglądarka przez czterdzieści różnych mechanizmów systemu: asocjacje w rejestrze, polityki enterprise, ustawienia profili przeglądarek, a nawet bazy wyszukiwarek wewnątrz profili Chromium. Samo usunięcie przeglądarki tego nie cofa.

**AntiWeChat Vanced** (fork [TheCawa/AntiYandex](https://github.com/TheCawa/AntiYandex)) znajduje **wszystkie 28 wektorów (VANCED) / 39 (EXTENDED) przejęcia**, usuwa je jednym kliknięciem, a następnie **twardo blokuje wyszukiwarkę domyślną** na wybranej przez Ciebie wyszukiwarce przez polityki enterprise Windows — żeby nic nie mogło po cichu przywrócić starych ustawień.

## Funkcje

- **Skaner przejęć** — wykrywa 28 wektorów (VANCED) / 39 wektorów (EXTENDED): ścieżki instalacji, wpisy Uninstall w rejestrze, asocjacja `UserChoice`, rejestracje `StartMenuInternet`, drzewa kluczy `Software\WeChat`, przejęcie przez polityki `DefaultSearchProvider*`, `Preferences` profili Chromium, słowa kluczowe w `Web Data` (SQLite), `search.json.mozlz4` Firefox, legacy `SearchScopes`, wpisy autostartu, zaplanowane zadania, usługi Windows, IME Switcher, skojarzenia plików, integracja powłoki WeChat Disk, wyłączony autostart, App Paths, skróty, pozostałości w ProgramData/Roaming, wpisy hosts, reguły zapory, protokoły URI, rozszerzenia przeglądarek, ciasteczka wechat.ru, asocjacje „otwórz za pomocą“, ślady Prefetch/WER, wyjątki Defender, układy klawiatury, przejęcie strony startowej IE, polityki adresów startowych (`RestoreOnStartupURLs`), strona domowa Firefox, mapa stref IE, wpisy RegisteredApplications, ślady MUICache, instalatory w %TEMP%, aplikacje ze Store (WeChat Music), katalogi produktów, katalogi danych lokalnych, WeChat.DNS
- **Usuwanie jednym kliknięciem** — każdy wektor ma własny remover; zablokowane bazy są uczciwie raportowane, bez crashy
- **Twarda polityka wyszukiwania** — blokuje wyszukiwarkę domyślną na jednej z 10 wyszukiwarek (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia, Yahoo, SearXNG) przez polityki HKLM dla Chrome, Edge, Brave, Vivaldi, Opera i WeChat Browser + `policies.json` dla Firefox/Waterfox
- **Czyszczenie polityk** — usuwa wartości `DefaultSearchProvider*` WeChata z rejestru
- **10 języków interfejsu** — ru, en, uk, kk, de, fr, es, pl, tr, zh; język systemu wykrywany automatycznie
- **Lekki interfejs** — ttkbootstrap, układ pionowy, przypięty pasek statusu i stopka

## Zrzut ekranu

<details>
<summary>Okno główne</summary>

![Okno główne AntiWeChatVanced](docs/screenshot.png)

</details>

## Gotowe buildy

Pobierz z [Releases](https://github.com/retvil/AntiWeChatVanced/releases):

- **Windows** — `AntiWeChatVanced.exe` (portable, jeden plik, ~35 MB) — usuwa WeChat Browser i WeChat Search
- **Windows** — `AntiWeChatExtended.exe` (portable, jeden plik, ~35 MB) — usuwanie wszystkich produktów WeChat (WeChat Disk, historia IME Switcher, ślady w całym systemie, aplikacje ze Store, WeChat.DNS)

Uruchom **jako administrator** — polityki HKLM i czyszczenie rejestru wymagają podwyższonych uprawnień.

## Instalacja ze źródeł

Wymagany Python 3.10+ ([python.org](https://python.org)).

```bash
git clone https://github.com/retvil/AntiWeChatVanced.git
cd AntiWeChatVanced
pip install psutil ttkbootstrap
python main.py
```

Budowa własnego EXE: uruchom `build.bat` (PyInstaller, wynik w `dist/`).

## Użycie

1. **Zakończ procesy** → **Szukaj WeChata** → **Usuń WeChata** — usuwamy samą przeglądarkę.
2. **Skanuj przejęcia wyszukiwania** — pokaże wszystkie sposoby, jakimi WeChat zapuścił korzenie w systemie.
3. **Usuń przejęcia** — najpierw zamknij wszystkie przeglądarki, potem usuń wszystko znalezione.
4. Wybierz wyszukiwarkę → **Zastosuj politykę** — wyszukiwarka domyślna zablokowana na poziomie systemu.

## FAQ

- **Po co administrator?** Polityki wyszukiwania mieszkają w HKLM, czyszczenie dotyka rejestru systemowego — potrzebne podwyższone uprawnienia.
- **„Database locked" w wynikach?** Podczas czyszczenia działała przeglądarka Chromium. Zamknij wszystkie przeglądarki i powtórz usuwanie.
- **Jak zdjąć politykę wyszukiwania?** Przycisk **Usuń polityki WeChata** czyści wartości polityk; w Firefoxie można też usunąć plik `distribution\policies.json`.

## Autor i wsparcie

Автор: **Nod33Eset**. Изначальная идея: [TheCawa/AntiYandex](https://github.com/TheCawa/AntiYandex). Мы уже ушли далеко от простого форка.

Jeśli narzędzie uwolniło Cię od WeChata — możesz wesprzeć rozwój:

**Krypto:**

- BTC: `bc1qunld3rsp37qf5gg69aune50y0qqkd0eugg7j97`
- TON: `UQDmvr4SKOxSION3Yky6aOgzAnCDXySPuAbG4EKJa5JUT7tC`
- USDT (TRC20): `TBPJSSLu1mUcX54g9UyxUohYGf2fuRvbwd`
- USDT (ERC20): `0x25CAED3776Ef5b18E03392bC5b254Bbd78E8180C`
- USDT (SOL): `3qgN5z291CEcj2FUi2Zza5DioxKgNw72kC7P52pCcTrG`

## Licencja

MIT — zob. [LICENSE](LICENSE).



