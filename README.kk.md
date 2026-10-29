# AntiWeChat Vanced

**🇬🇧 English** | [🇷🇺 Русский](README.ru.md) | [🇺🇦 Українська](README.uk.md) | [🇰🇿 Қазақша](README.kk.md) | [🇩🇪 Deutsch](README.de.md) | [🇫🇷 Français](README.fr.md) | [🇪🇸 Español](README.es.md) | [🇵🇱 Polski](README.pl.md) | [🇹🇷 Türkçe](README.tr.md) | [🇨🇳 中文](README.zh.md)

## 🌐 Forks

<a href="https://github.com/retvil/AntiBaiduVanced"><img src="https://raw.githubusercontent.com/retvil/AntiBaiduVanced/main/logo.png" alt="AntiBaiduVanced" width="16" height="16" style="vertical-align:middle"> AntiBaiduVanced</a>  |  <a href="https://github.com/retvil/AntiSogouVanced"><img src="https://raw.githubusercontent.com/retvil/AntiSogouVanced/main/logo.png" alt="AntiSogouVanced" width="16" height="16" style="vertical-align:middle"> AntiSogouVanced</a>  |  <a href="https://github.com/retvil/Anti2345Vanced"><img src="https://raw.githubusercontent.com/retvil/Anti2345Vanced/main/logo.png" alt="Anti2345Vanced" width="16" height="16" style="vertical-align:middle"> Anti2345Vanced</a>  |  <a href="https://github.com/retvil/AntiUCWebVanced"><img src="https://raw.githubusercontent.com/retvil/AntiUCWebVanced/main/logo.png" alt="AntiUCWebVanced" width="16" height="16" style="vertical-align:middle"> AntiUCWebVanced</a>  |  <a href="https://github.com/retvil/AntiNaverVanced"><img src="https://raw.githubusercontent.com/retvil/AntiNaverVanced/main/logo.png" alt="AntiNaverVanced" width="16" height="16" style="vertical-align:middle"> AntiNaverVanced</a>  |  <a href="https://github.com/retvil/AntiKakaoVanced"><img src="https://raw.githubusercontent.com/retvil/AntiKakaoVanced/main/logo.png" alt="AntiKakaoVanced" width="16" height="16" style="vertical-align:middle"> AntiKakaoVanced</a>  |  <a href="https://github.com/retvil/AntiQQVanced"><img src="https://raw.githubusercontent.com/retvil/AntiQQVanced/main/logo.png" alt="AntiQQVanced" width="16" height="16" style="vertical-align:middle"> AntiQQVanced</a>  |  **AntiWeChatVanced**  |  <a href="https://github.com/retvil/AntiTencentVideoVanced"><img src="https://raw.githubusercontent.com/retvil/AntiTencentVideoVanced/main/logo.png" alt="AntiTencentVideoVanced" width="16" height="16" style="vertical-align:middle"> AntiTencentVideoVanced</a>  |  <a href="https://github.com/retvil/AntiVKGroupVanced"><img src="https://raw.githubusercontent.com/retvil/AntiVKGroupVanced/main/logo.png" alt="AntiVKGroupVanced" width="16" height="16" style="vertical-align:middle"> AntiVKGroupVanced</a>  |  <a href="https://github.com/retvil/AntiYandexVanced"><img src="https://raw.githubusercontent.com/retvil/AntiYandexVanced/main/logo.png" alt="AntiYandexVanced" width="16" height="16" style="vertical-align:middle"> AntiYandexVanced</a>

## Бұл не?

WeChat жай ғана браузер орнатпайды — ол жүйенің қырық әртүрлі механизмі арқылы әдепкі іздеу/браузер болып үнсіз тіркеледі: реестр ассоциациялары, enterprise-саясаттар, браузер профильдерінің параметрлері, тіпті Chromium профильдеріндегі іздеу жүйелерінің базалары. Бір браузерді жою мұның бәрін жоймайды.

**AntiWeChat Vanced** ([retvil/AntiYandexVanced](https://github.com/retvil/AntiYandexVanced) форкі) **барлық 40 ұрлау векторын** табады, бір батырмамен алып тастайды, содан кейін әдепкі іздеуді таңдаған іздеу жүйеңізге Windows enterprise-саясаттары арқылы **қатайтып бекітеді** — ештеңе үнсіз қайтарып алмас үшін.

## Мүмкіндіктер

- **Ұрлау сканері** — 28 вектор (VANCED) / 39 (EXTENDED)ды анықтау: орнату жолдары, реестрдегі Uninstall жазбалары, `UserChoice` ассоциациясы, `StartMenuInternet` тіркелулері, `Software\WeChat` кілттер ағаштары, `DefaultSearchProvider*` саясаттары арқылы ұрлау, Chromium профильдерінің `Preferences` параметрлері, `Web Data` (SQLite) кілт сөздері, Firefox `search.json.mozlz4`, legacy `SearchScopes`, автозапуск, тапсырмалар жоспарлаушы, Windows қызметтері, IME Switcher, файлдық байланыстырулар, WeChat Disk интеграциясы, өшірілген автозапуск, App Paths, жарлықтар, ProgramData/Roaming қалдықтары, hosts жазбалары, брандмауэр ережелері, URI-протоколдар, браузер кеңейтулері, wechat.ru cookie файлдары, «көмегімен ашу» ассоциациялары, Prefetch/WER іздері, Defender ерекшеліктері, пернетақта орналасулары, IE бастапқы бетін ұрлау, бастапқы URL саясаттары (`RestoreOnStartupURLs`), Firefox басты беті, IE аймақ картасы, RegisteredApplications жазбалары, MUICache іздері, %TEMP% орнатқыштары, Store қосымшалары (WeChat Music), өнім каталогтары, жергілікті деректер каталогтары, WeChat.DNS
- **Бір батырмамен жою** — әр вектордың өз remover-ы бар; бұғатталған базалар шынайы репортталады, крашсыз
- **Қатаң іздеу саясаты** — іздеуді 10 іздеу жүйесінің біреуіне (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia, Yahoo, SearXNG) бекітеді: Chrome, Edge, Brave, Vivaldi, Opera және WeChat Browser үшін HKLM-саясаттар + Firefox/Waterfox үшін `policies.json`
- **Саясат тазарту** — WeChat `DefaultSearchProvider*` мәндерін реестрден тазартады
- **10 интерфейс тілі** — ru, en, uk, kk, de, fr, es, pl, tr, zh; жүйе тілі автоматты анықталады
- **Жеңіл интерфейс** — ttkbootstrap, вертикальді компоновка, бекітілген статус-бар және футер

## Скриншот

<details>
<summary>Негізгі терезе</summary>

![AntiWeChatVanced негізгі терезесі](docs/screenshot.png)

</details>

## Дайын жинақтар

[Releases](https://github.com/retvil/AntiWeChatVanced/releases) бетінен жүктеп алыңыз:

- **Windows** — `AntiWeChatVanced.exe` (портативті, бір файл, ~35 МБ) — WeChat Browser және WeChat Search жою
- **Windows** — `AntiWeChatExtended.exe` (портативті, бір файл, ~35 МБ) — WeChatтің барлық өнімдерін жою (WeChat Disk, IME Switcher тарихы, жүйелік іздер, Store қосымшалары, WeChat.DNS)

**Әкімші ретінде** іске қосыңыз — HKLM-саясаттар мен реестр тазартуы жоғарылау құқықтарды қажет етеді.

## Бастапқы кодтан орнату

Python 3.10+ қажет ([python.org](https://python.org)).

```bash
git clone https://github.com/retvil/AntiWeChatVanced.git
cd AntiWeChatVanced
pip install psutil ttkbootstrap
python main.py
```

Өз EXE-ді жинау: `build.bat` іске қосыңыз (PyInstaller, нәтиже `dist/` ішінде).

## Пайдалану

1. **Процессерді тоқтату** → **WeChatті іздеу** → **WeChatті жою** — браузердің өзін жоямыз.
2. **Іздеу ұрлауын сканерлеу** — WeChat жүйеге қалай енгенін толық көрсетеді.
3. **Ұрлауды жою** — алдымен барлық браузерді жабыңыз, соснын табылғанның бәрін алып тастаңыз.
4. Іздеу жүйесін таңдаңыз → **Саясатты қолдану** — әдепкі іздеу жүйе деңгейінде бекітілді.

## FAQ

- **Неге әкімші?** Іздеу саясаттары HKLM-де тұрады, ұрлау тазартуы жүйелік реестрге тиеді — жоғары құқықтар керек.
- **Нәтижелерде «Database locked»?** Тазарту кезінде Chromium браузері істе тұрған. Барлық браузерді жабып, жоюды қайталаңыз.
- **Іздеу саясатын қалай алып тастауға болады?** **Саясатты қолдану**... **WeChat саясатын алып тастау** батырмасы саясат мәндерін тазартады; Firefox-та `distribution\policies.json` файлын жоюға болады.

## Автор және қолдау

Изначальная идея: [TheCawa/AntiYandex](https://github.com/TheCawa/AntiYandex)

Егер құрал сізді WeChatтен құтқарса — дамуды қолдауға болады:

**Крипта:**

- BTC: `bc1qunld3rsp37qf5gg69aune50y0qqkd0eugg7j97`
- TON: `UQDmvr4SKOxSION3Yky6aOgzAnCDXySPuAbG4EKJa5JUT7tC`
- USDT (TRC20): `TBPJSSLu1mUcX54g9UyxUohYGf2fuRvbwd`
- USDT (ERC20): `0x25CAED3776Ef5b18E03392bC5b254Bbd78E8180C`
- USDT (SOL): `3qgN5z291CEcj2FUi2Zza5DioxKgNw72kC7P52pCcTrG`

## Лицензия

MIT — қ. [LICENSE](LICENSE).



