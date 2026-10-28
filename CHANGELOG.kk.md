# Өзгеріс журналы

Жобаның барлық маңызды өзгерістері осы файлда құжатталады.

Формат [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) негізінде,
жоба [Semantic Versioning](https://semver.org/spec/v2.0.0.html) ұстанады.

> Бастапқы дереккөз — ағылшын [CHANGELOG.md](CHANGELOG.md); бұл аударма сәл кешігуі мүмкін.

## [2.8.0] - 2026-10-22

### Қосылды
- **IE аймақ картасы сканы (zone map)** — WeChat домендерінің zone-map
  жазбаларын табады («сенімді сайттар» қалдықтары); жою доменнің ішкі ағашын
  алып тастайды (алдымен экспорт)
- **RegisteredApplications сканы** — әдепкі қосымшалар метадеректеріндегі
  WeChat жазбаларын табады; жою мәнді өшіреді (алдымен экспорт)
- **MUICache сканы** — WeChat орындалатын файлдарының іске қосу іздерін
  табады; жою кеш мәнін өшіреді (алдымен экспорт)
- **%TEMP% ішіндегі орнатқыш іздері** — scan_traces енді пайдаланушының
  уақытша папкасында қалған WeChat орнатқыштарын да репорттайды
- **Per-user өнім каталогтары** — scan_product_dirs енді
  `%LOCALAPPDATA%\Programs\WeChat*` жолын да қамтиды (WeChat Music /
  Messenger / Translate legacy-орнатулары), браузер папкасы шығарылып
  тасталады
- **Жол бойынша kill (Vanced)** — браузерлік kill енді exe-сі WeChatBrowser
  жолының астында жатқан процестерді де матчтайды (crashpad, updater),
  тек browser.exe/wechat.exe атауларының тар тізімі емес
- **Бастапқы URL hijack сканы** — `RestoreOnStartupURLs` enterprise-саясаттарындағы
  WeChat URL-дарын табады (Edge, Chrome, Chromium, Brave, Vivaldi, Opera,
  WeChat Browser); жою WeChat мәндерін тазартады
- **Firefox басты беті hijack сканы** — Firefox/Waterfox `prefs.js`
  ішіндегі WeChatке апаратын `browser.startup.homepage` табады; жою файлды
  қайта жазады (алдымен бекап)

## [2.7.0] - 2026-10-21

### Қосылды
- **WeChat.DNS сканы** (Extended) — WeChat DNS серверлерімен (77.88.8.x
  basic/safe/family) бапталған желі адаптерлерін табады; жою адаптерге
  автоматты DNS қайтарады; растаумен
- **Бастапқы бет hijack сканы** — WeChat/wechat.com көрсететін legacy IE басты
  бетін (`HKCU\...\Internet Explorer\Main\Start Page`) табады; жою әдепкіні
  қайтарады (еккі басылым)

## [2.6.0] - 2026-10-21

### Қосылды
- **Extended басылымы**: Store (Appx) қосымша сканы — WeChat Music, Messenger,
  Messenger және басқа WeChat Store қосымшаларын табады,
  `Remove-AppxPackage` арқылы жояды
- **Extended басылымы**: `Program Files\WeChat\` астындағы браузерлік емес
  өнім каталогтарын скан (WeChat Disk, WeChat IME Switcher, IME, ...) — жою
  алдында бекап
- **Extended басылымы**: `%LOCALAPPDATA%\WeChat\` астындағы браузерлік емес
  жергілікті деректер сканы (WeChat IME Switcher жергілікті деректері, WeChat
  Disk апдейтері, Beta жинақтары) — растаумен, жою алдында бекап
- **Extended басылымы**: «Kill Processes» енді тек браузерді емес, WeChatтің
  барлық өнім процестерін (WeChat Disk, WeChat IME Switcher, Store қосымшалары)
  аяқтайды

## [2.5.0] - 2026-10-21

### Қосылды
- Бір код базасынан екі басылым: **AntiWeChatVanced** (WeChat Browser +
  WeChat Search жою) және **AntiWeChatExtended** (WeChatтің барлық
  өнімдері) — `profiles.py` ішіндегі өнім профильдері скан ауқымын таңдайды,
  ортақ GUI `app.py` ішінде, жұқа кіру нүктелері `main.py` / `main_extended.py`
- `build.bat` енді екі EXE де жинайды

## [2.4.0] - 2026-10-21

### Қосылды
- 16-шы–30-шы hijack векторлары: WeChat Disk қабық интеграциясы (белгі
  оверлейлері + контекстік мәзір өңдеушілері), өшірілген автозапуск
  (`StartupApproved`), `App Paths`, жарлықтар (Жұмыс үстелі / Басты мәзір /
  тапсырмалар тақтасы), қалдық каталогтар (ProgramData, Roaming, WeChat Disk
  деректері және синхрондалған файлдар), `hosts` жазбалары, Windows
  брандмауэр ережелері, URI-протокол өңдеушілері, браузер кеңейтулері
  (Chromium манифесттері + Firefox `.xpi`), wechat.ru cookie файлдары
  (Chromium + Firefox), `OpenWithProgids`/`OpenWithList` ассоциациялары,
  Prefetch / CrashDumps / WER іздері, Windows Defender ерекшеліктері,
  пайдаланушы пернетақта орналасулары (WeChat IME)
- Растау: пайдаланушы деректеріне қатысты табылғандар (WeChat Disk файлдары,
  WeChat IME Switcher тарихы, кеңейтулер, cookie файлдары, Defender ерекшеліктері)
  жою алдында нақты қосымша растауды қажет етеді
- `.lnk` байт-детекті, hosts жолдарын сүзгілеу, брандмауэр шығысын парсинг
  және consent-префикстер қамтуы үшін юнит-тесттер

## [2.3.0] - 2026-10-20

### Қосылды
- 13-ші–15-ші hijack векторлары: Windows қызметтері (реестр бойынша скан,
  `sc stop` + `sc delete` арқылы жою), WeChat IME Switcher (`ime` маркері бойынша
  детект), файлдық байланыстырулар (`FileExts\<ext>\UserChoice` ProgId сканы
  + жою)
- Сканнан кейінгі таңдау диалогы: «барлығы немесе ештеңе» орнына нақты қай
  табылғандарды жоятынды таңдау
- Шығарып тастаулар: белгісіз қалдырғандарды
  `%APPDATA%\AntiWeChatVanced\exclusions.json` ішіне сақтауға болады —
  келесі скандар оларды автоматты түрде таңдамайды, бірақ диалогта таңдатылып
  тұрады; шығарып тастауларды диалогтан қайта орнатуға болады
- Шығарып тастаулардың сақталуы және WeChat IME Switcher маркері үшін юнит-тесттер

## [2.2.0] - 2026-10-20

### Қосылды
- Жою алдында бекап: әр қозғалған реестр кілті / профиль файлы жою алдында
  `%APPDATA%\AntiWeChatVanced\backup\<timestamp>\` ішіне экспортталады
- Операциялар журналы: `%APPDATA%\AntiWeChatVanced\antiwechat.log`
- 12-ші hijack векторы: Windows Task Scheduler жазбалары (WeChat апдейтер
  тапсырмалары)
- HKCU Chromium саясаттарының сканы/тазартуы (per-user саясаттар, бұрын тек
  HKLM)
- Бастауда әкімші құқықтарын тексеру, статус-барда ескертумен
- Hijack жою алдында іске қосылған браузерлерді жабу ұсынысы («database
  locked» алдын алады)
- Кейбір hijack элементтері жойылмаса «есеп папкасын ашу» ұсынысы
- Таза логика юнит-тесттері (двигун іздеу, Firefox policies.json,
  LZ4-декомпрессор)

### Түзетілді
- Фондық ағындардан келген барлық UI жаңартулары енді `root.after` арқылы
  басты ағынға бағытталады (tkinter ағын-қауіпсіз емес)
- Жалаң `except:` тармақтары `except OSError` болып ауыстырылды
- Web Data тазартуы енді дәл табылған жолдарды (`rowid` бойынша) жояды, URL
  ішкі жолы бойынша емес — детект пен жою үйлеседі
- SQLite байланыстары error-жолдарында жабылады (`finally`)
- Firefox `policies.json` енді `null` `SuggestURLTemplate` қамтымайды
- Firefox саясаттары енді жоқ орнату папкаларына жазылмайды
- Қатты кодталған орысша әкімші-қате жолы барлық 10 UI тілінде аударылатын
  кілтпен ауыстырылды
- `shutil.rmtree` енді жалпы қатенің орнына қай файлдар бұғатталғанын
  репорттайды
- Инвалидтік ығысулары бар бұзылған LZ4 блоктары қоқыс қайтарудың орнына
  ерекше жағдай көтереді

## [2.1.2] - 2026-10-20

### Өзгерді
- Қосымша тақырыбы «Удаление WeChat» / «Remove WeChat» (ru/en/uk) болып
  қысқартылды
- Футер оң жақ төменгі бұрышқа бекітілді: автор, нұсқа және GitHub
  сілтемесі
- Репозиторий сілтемесі `https://github.com/retvil/AntiWeChatVanced`
  болып орнатылды

## [2.1.0] - 2026-10-20

### Қосылды
- Терезенің вертикальді компоновкасы (560×700): ортадағы әрекеттер стегі,
  толық енді секция карталары
- **ttkbootstrap** негізіндегі жарық тема (`flatly`) — CustomTkinter орнына
  жеңілдірек ttk-стек
- Автор, нұсқа және GitHub репозиторий сілтемесі бар футер

### Өзгерді
- UI-кітапхана көші: tkinter → CustomTkinter → ttkbootstrap
- Тіл таңдағыш оң жақ жоғарғы бұрышқа көшті

## [2.0.0] - 2026-10-20

[TheCawa/AntiWeChat](https://github.com/TheCawa/AntiWeChat) 1.3 форкі.

### Қосылды
- **Іздеу hijack сканері** — WeChatтің әдепкі іздеу/браузер болып тіркелуіне
  қолданатын 11 векторды анықтайды:
  - дискідегі орнату каталогтары
  - реестрдегі Uninstall жазбалары (HKLM, WOW6432Node, HKCU)
  - Windows әдепкі-браузер ассоциациясы (http/https үшін `UserChoice` ProgId)
  - `StartMenuInternet` браузер клиент тіркелулері
  - жеке `Software\WeChat` кілт ағаштары (HKCU/HKLM/WOW6432Node)
  - `DefaultSearchProvider*` enterprise-саясаттары арқылы hijack (WeChatтің
    өзін бекітудің қатты жолы)
  - Chromium профильдерінің per-profile `Preferences` JSON (Chrome, Edge,
    Brave, Vivaldi, WeChat Browser)
  - Chromium `Web Data` SQLite базаларындағы іздеу жүйелерінің кілт сөз
    жолдары
  - Firefox/Waterfox `search.json.mozlz4` (құрамында pure-Python LZ4 блок
    декомпрессоры бар)
  - legacy IE/Windows `SearchScopes` жазбалары
  - автозапуск жазбалары (`Run`/`RunOnce`)
- **Hijack жою** — табылған барлық векторды бір батырмамен жою, әр вектордың
  өз remover-ы бар: реестр кілттерін рекурсивті жою, `UserChoice` қайта
  орнату, `Preferences` тазарту, Web Data ішінде `DELETE FROM keywords`,
  `search.json.mozlz4` қайта орнату (Firefox әдепкілерін қайта жасайды),
  автозапуск мәндерін жою. Бұғатталған базалар/файлдар (браузер іске қосулы)
  репортталады, крашсыз.
- **Қатаң әдепкі-іздеу саясаты** — 10 іздеу жүйесінің бірін бекітеді
  (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia,
  Yahoo, SearXNG):
  - Chromium тұқымдасы HKLM `SOFTWARE\Policies\...` `DefaultSearchProvider*`
    мәндері арқылы (Chrome, Edge, Brave, Vivaldi, Opera, WeChat Browser)
  - Firefox/Waterfox `distribution\policies.json` арқылы (`SearchEngines` +
    `LockDefaultSearchEngine` + `PreventSearchEngineInstall`)
- **«WeChat саясаттарын жою»** батырмасы — WeChat `DefaultSearchProvider*`
  саясат мәндерін реестрден тазартады
- **10 UI тілі** (ru, en, uk, kk, de, fr, es, pl, tr, zh) жеке `translations.py`
  модулінде; жүйе тілі Windows UI language API арқылы автоматты анықталады
  (`GetUserDefaultUILanguage`), сәйкессіздікте ағылшынша фолбэк
- UI-дағы тіл ауыстыру ашылмалы тізімі

### Өзгерді
- Код модульдерге бөлінді: `engines.py`, `wechat_detect.py`, `policies.py`,
  `translations.py`, `main.py`

## [1.3.0] - upstream

[TheCawa/AntiWeChat](https://github.com/TheCawa/AntiWeChat) базасы:
- WeChat Browser процестерін аяқтау (`browser.exe`, `wechat.exe`)
- Орнату жолдарын іздеу
- Реестрдегі Uninstall жазбаларын тазарту
- Браузер папкасын жою
- RU/EN интерфейс ауыстырғышы

[Unreleased]: https://github.com/retvil/AntiWeChatVanced/compare/v2.1.2...HEAD
[2.1.2]: https://github.com/retvil/AntiWeChatVanced/compare/v2.1.0...v2.1.2
[2.1.0]: https://github.com/retvil/AntiWeChatVanced/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/retvil/AntiWeChatVanced/compare/v1.3.0...v2.0.0
