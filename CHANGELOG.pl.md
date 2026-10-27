# Dziennik zmian

Wszystkie istotne zmiany w tym projekcie są dokumentowane w tym pliku.

Format oparty jest na [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
a projekt stosuje [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

> Źródłem prawdy jest angielski [CHANGELOG.md](CHANGELOG.md); to tłumaczenie może lekko odstawać.

## [2.8.0] - 2026-10-22

### Dodano
- **Skan mapy stref IE (zone map)** — wykrywa wpisy zone-map dla domen
  WeChat (pozostałości „zaufanych witryn”); usunięcie kasuje poddrzewo
  domeny (najpierw eksport)
- **Skan RegisteredApplications** — wykrywa wpisy WeChat w metadanych
  aplikacji domyślnych; usunięcie kasuje wartość (najpierw eksport)
- **Skan MUICache** — wykrywa ślady uruchamiania plików wykonywalnych
  WeChat; usunięcie kasuje wartość cache (najpierw eksport)
- **Ślady instalatorów w %TEMP%** — scan_traces zgłasza teraz także
  instalatory WeChat pozostawione w folderze tymczasowym użytkownika
- **Katalogi produktów per-user** — scan_product_dirs obejmuje teraz także
  `%LOCALAPPDATA%\Programs\WeChat*` (instalacje legacy WeChat Music /
  Messenger / Translate), folder przeglądarki wykluczony
- **Kill procesów po ścieżce (Vanced)** — kill przeglądarki dopasowuje
  teraz także procesy, których exe leży pod ścieżką WeChatBrowser
  (crashpad, updater), nie tylko wąską listę nazw browser.exe/wechat.exe
- **Skan przejęcia adresów startowych** — wykrywa URL WeChat w politykach
  enterprise `RestoreOnStartupURLs` (Edge, Chrome, Chromium, Brave,
  Vivaldi, Opera, WeChat Browser); usunięcie czyści wartości WeChat
- **Skan przejęcia strony domowej Firefox** — wykrywa
  `browser.startup.homepage` wskazujące na WeChat w `prefs.js`
  Firefox/Waterfox; usunięcie przepisuje plik (najpierw kopia zapasowa)

## [2.7.0] - 2026-10-21

### Dodano
- **Skan WeChat.DNS** (Extended) — wykrywa adaptery sieciowe skonfigurowane
  z serwerami DNS WeChat (77.88.8.x basic/safe/family); usunięcie przywraca
  adapterowi automatyczny DNS; z potwierdzeniem
- **Skan przejęcia strony startowej** — wykrywa legacy stronę startową IE
  (`HKCU\...\Internet Explorer\Main\Start Page`) wskazującą na
  WeChat/wechat.com; usunięcie przywraca domyślną (oba wydania)

## [2.6.0] - 2026-10-21

### Dodano
- **Wydanie Extended**: skan aplikacji Store (Appx) — wykrywa WeChat Music,
  Alice, Messenger i inne aplikacje Store WeChat, usuwa je przez
  `Remove-AppxPackage`
- **Wydanie Extended**: skan katalogów produktów nieprzeglądarkowych pod
  `Program Files\WeChat\` (WeChat Disk, Punto Switcher, IME, ...) z kopią
  zapasową przed usunięciem
- **Wydanie Extended**: skan lokalnych danych nieprzeglądarkowych pod
  `%LOCALAPPDATA%\WeChat\` (lokalne dane Punto Switcher, updater WeChat
  Disk, buildy Beta) — z potwierdzeniem, kopia zapasowa przed usunięciem
- **Wydanie Extended**: „Kill Processes” kończy teraz procesy wszystkich
  produktów WeChat (WeChat Disk, Punto Switcher, aplikacje Store), nie
  tylko przeglądarki

## [2.5.0] - 2026-10-21

### Dodano
- Dwa wydania z jednej bazy kodu: **AntiWeChatVanced** (usunięcie WeChat
  Browser + WeChat Search) i **AntiWeChatExtended** (wszystkie produkty
  WeChat) — profile produktów w `profiles.py` wybierają zakres skanu,
  wspólny GUI w `app.py`, cienkie punkty wejścia `main.py` /
  `main_extended.py`
- `build.bat` buduje teraz oba EXE

## [2.4.0] - 2026-10-21

### Dodano
- Wektory przejęcia 16–30: integracja powłoki WeChat Disk (nakładki ikon +
  handlery menu kontekstowego), wyłączony autostart (`StartupApproved`),
  `App Paths`, skróty (Pulpit / Menu Start / pasek zadań), katalogi
  pozostałości (ProgramData, Roaming, dane WeChat Disk i zsynchronizowane
  pliki), wpisy `hosts`, reguły zapory Windows, handlery protokołów URI,
  rozszerzenia przeglądarek (manifesty Chromium + `.xpi` Firefox),
  ciasteczka wechat.ru (Chromium + Firefox), asocjacje
  `OpenWithProgids`/`OpenWithList`, ślady Prefetch / CrashDumps / WER,
  wyjątki Windows Defender, niestandardowe układy klawiatury (WeChat IME)
- Potwierdzenie zgody: znaleziska dotykające danych użytkownika (pliki
  WeChat Disk, historia Punto Switcher, rozszerzenia, ciasteczka, wyjątki
  Defender) wymagają jawnego dodatkowego potwierdzenia przed usunięciem
- Testy jednostkowe dla detekcji bajtów `.lnk`, filtrowania linii hosts,
  parsowania wyjścia zapory i pokrycia prefiksów zgody

## [2.3.0] - 2026-10-20

### Dodano
- Wektory przejęcia 13–15: usługi Windows (skan po rejestrze, usuwanie
  przez `sc stop` + `sc delete`), Punto Switcher (detekcja po markerze
  `punto`), skojarzenia plików (skan + usunięcie ProgId w
  `FileExts\<ext>\UserChoice`)
- Dialog wyboru po skanie: wybór dokładnie, które znaleziska usunąć,
  zamiast „wszystko albo nic”
- Wykluczenia: odznaczone znaleziska można zapisać do
  `%APPDATA%\AntiWeChatVanced\exclusions.json` — przyszłe skany automatycznie
  je odznaczają, ale pozostają wybieralne w dialogu; wykluczenia można
  zresetować z dialogu
- Testy jednostkowe persystencji wykluczeń i markera Punto Switcher

## [2.2.0] - 2026-10-20

### Dodano
- Kopia zapasowa przed usunięciem: każdy dotknięty klucz rejestru / plik
  profilu jest eksportowany do
  `%APPDATA%\AntiWeChatVanced\backup\<timestamp>\` przed usunięciem
- Dziennik operacji: `%APPDATA%\AntiWeChatVanced\antiwechat.log`
- Wektor przejęcia 12: wpisy Harmonogramu zadań Windows (zadania updateera
  WeChat)
- Skan/czyszczenie polityk Chromium HKCU (polityki per-user, wcześniej
  tylko HKLM)
- Sprawdzenie praw administratora przy starcie z ostrzeżeniem na pasku
  statusu
- Podpowiedź zamknięcia uruchomionych przeglądarek przed usunięciem
  przejęć (zapobiega „database locked”)
- Propozycja „otwórz folder raportu”, gdy część elementów przejęcia nie
  dała się usunąć
- Testy jednostkowe czystej logiki (wyszukiwanie silnika, Firefox
  policies.json, dekompresor LZ4)

### Naprawiono
- Wszystkie aktualizacje UI z wątków w tle są teraz marshlowane do wątku
  głównego przez `root.after` (tkinter nie jest thread-safe)
- Gołe klauzule `except:` zastąpione przez `except OSError`
- Czyszczenie Web Data usuwa teraz dokładnie wykryte wiersze (po `rowid`),
  a nie po podciągu URL — detekcja i usuwanie są spójne
- Połączenia SQLite zamykane na ścieżkach błędów (`finally`)
- Firefox `policies.json` nie zawiera już `null` `SuggestURLTemplate`
- Polityki Firefox nie są już zapisywane do nieistniejących folderów
  instalacji
- Zakodowany na sztywno rosyjski komunikat błędu admina zastąpiony
  tłumaczalnym kluczem we wszystkich 10 językach UI
- `shutil.rmtree` zgłasza teraz, które pliki są zablokowane, zamiast
  ogólnego błędu
- Uszkodzone bloki LZ4 z nieprawidłowymi offsetami dopasowań rzucają
  wyjątek zamiast zwracać śmieci

## [2.1.2] - 2026-10-20

### Zmieniono
- Tytuł aplikacji skrócony do „Удаление Яндекс” / „Remove WeChat”
  (ru/en/uk)
- Stopka przypięta do prawego dolnego rogu: autor, wersja i klikalny link
  do GitHub
- Link repozytorium ustawiony na `https://github.com/retvil/AntiWeChatVanced`

## [2.1.0] - 2026-10-20

### Dodano
- Pionowy układ okna (560×700): wyśrodkowany stos akcji, karty sekcji na
  pełną szerokość
- Jasny motyw UI na **ttkbootstrap** (motyw `flatly`) — CustomTkinter
  zastąpiony lżejszym stosem ttk
- Stopka z autorem, wersją i klikalnym linkiem do repozytorium GitHub

### Zmieniono
- Migracja biblioteki UI: tkinter → CustomTkinter → ttkbootstrap
- Selektor języka przeniesiony do prawego górnego rogu

## [2.0.0] - 2026-10-20

Fork [TheCawa/AntiWeChat](https://github.com/TheCawa/AntiWeChat) 1.3.

### Dodano
- **Skaner przejęć wyszukiwania** — wykrywa 11 wektorów, którymi WeChat
  instaluje się jako domyślna wyszukiwarka/przeglądarka:
  - katalogi instalacji na dysku
  - wpisy Uninstall w rejestrze (HKLM, WOW6432Node, HKCU)
  - asocjacja domyślnej przeglądarki Windows (ProgId `UserChoice` dla
    http/https)
  - rejestracje klientów przeglądarek `StartMenuInternet`
  - samodzielne drzewa kluczy `Software\WeChat` (HKCU/HKLM/WOW6432Node)
  - przejęcie przez polityki enterprise `DefaultSearchProvider*` (twardy
    sposób, w jaki WeChat się narzuca)
  - JSON `Preferences` profili Chromium (Chrome, Edge, Brave, Vivaldi,
    WeChat Browser)
  - wiersze słów kluczowych wyszukiwarek w bazach SQLite `Web Data`
    Chromium
  - Firefox/Waterfox `search.json.mozlz4` (z wbudowanym dekompresorem
    bloków LZ4 w czystym Pythonie)
  - legacy wpisy `SearchScopes` IE/Windows
  - wpisy autostartu (`Run`/`RunOnce`)
- **Usuwanie przejęć** — usuwanie wszystkich wykrytych wektorów jednym
  kliknięciem, każdy wektor ma własny remover: rekurencyjne usuwanie kluczy
  rejestru, reset `UserChoice`, czyszczenie `Preferences`,
  `DELETE FROM keywords` w Web Data, reset `search.json.mozlz4` (Firefox
  odbudowuje domyślne), usuwanie wartości autostartu. Zablokowane
  bazy/pliki (przeglądarka uruchomiona) są raportowane, bez crashy.
- **Twarda polityka domyślnej wyszukiwarki** — wymusza jedną z 10
  wyszukiwarek (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek,
  Qwant, Ecosia, Yahoo, SearXNG):
  - rodzina Chromium przez wartości HKLM `SOFTWARE\Policies\...`
    `DefaultSearchProvider*` (Chrome, Edge, Brave, Vivaldi, Opera,
    WeChat Browser)
  - Firefox/Waterfox przez `distribution\policies.json` (`SearchEngines` +
    `LockDefaultSearchEngine` + `PreventSearchEngineInstall`)
- Przycisk **„Usuń polityki WeChat”** — czyści wartości polityk
  `DefaultSearchProvider*` WeChat z rejestru
- **10 języków UI** (ru, en, uk, kk, de, fr, es, pl, tr, zh) w dedykowanym
  module `translations.py`; język systemu wykrywany automatycznie przez
  Windows UI language API (`GetUserDefaultUILanguage`), fallback na
  angielski
- Rozwijana lista zmiany języka w UI

### Zmieniono
- Kod podzielony na moduły: `engines.py`, `wechat_detect.py`,
  `policies.py`, `translations.py`, `main.py`

## [1.3.0] - upstream

Baza [TheCawa/AntiWeChat](https://github.com/TheCawa/AntiWeChat):
- Zakończenie procesów WeChat Browser (`browser.exe`, `wechat.exe`)
- Wyszukiwanie ścieżek instalacji
- Czyszczenie wpisów Uninstall w rejestrze
- Usuwanie folderu przeglądarki
- Przełącznik interfejsu RU/EN

[Unreleased]: https://github.com/retvil/AntiWeChatVanced/compare/v2.1.2...HEAD
[2.1.2]: https://github.com/retvil/AntiWeChatVanced/compare/v2.1.0...v2.1.2
[2.1.0]: https://github.com/retvil/AntiWeChatVanced/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/retvil/AntiWeChatVanced/compare/v1.3.0...v2.0.0
