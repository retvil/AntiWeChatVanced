# AntiWeChat Vanced

**🇬🇧 English** | [🇷🇺 Русский](README.ru.md) | [🇺🇦 Українська](README.uk.md) | [🇰🇿 Қазақша](README.kk.md) | [🇩🇪 Deutsch](README.de.md) | [🇫🇷 Français](README.fr.md) | [🇪🇸 Español](README.es.md) | [🇵🇱 Polski](README.pl.md) | [🇹🇷 Türkçe](README.tr.md) | [🇨🇳 中文](README.zh.md)

## 🌐 Forks

[![AntiBaiduVanced](https://raw.githubusercontent.com/retvil/AntiBaiduVanced/main/logo.png =16)AntiBaiduVanced](https://github.com/retvil/AntiBaiduVanced)  |  [![AntiSogouVanced](https://raw.githubusercontent.com/retvil/AntiSogouVanced/main/logo.png =16)AntiSogouVanced](https://github.com/retvil/AntiSogouVanced)  |  [![Anti2345Vanced](https://raw.githubusercontent.com/retvil/Anti2345Vanced/main/logo.png =16)Anti2345Vanced](https://github.com/retvil/Anti2345Vanced)  |  [![AntiUCWebVanced](https://raw.githubusercontent.com/retvil/AntiUCWebVanced/main/logo.png =16)AntiUCWebVanced](https://github.com/retvil/AntiUCWebVanced)  |  [![AntiNaverVanced](https://raw.githubusercontent.com/retvil/AntiNaverVanced/main/logo.png =16)AntiNaverVanced](https://github.com/retvil/AntiNaverVanced)  |  [![AntiKakaoVanced](https://raw.githubusercontent.com/retvil/AntiKakaoVanced/main/logo.png =16)AntiKakaoVanced](https://github.com/retvil/AntiKakaoVanced)  |  [![AntiQQVanced](https://raw.githubusercontent.com/retvil/AntiQQVanced/main/logo.png =16)AntiQQVanced](https://github.com/retvil/AntiQQVanced)  |  **AntiWeChatVanced**  |  [![AntiTencentVideoVanced](https://raw.githubusercontent.com/retvil/AntiTencentVideoVanced/main/logo.png =16)AntiTencentVideoVanced](https://github.com/retvil/AntiTencentVideoVanced)  |  [![AntiVKGroupVanced](https://raw.githubusercontent.com/retvil/AntiVKGroupVanced/main/logo.png =16)AntiVKGroupVanced](https://github.com/retvil/AntiVKGroupVanced)  |  [![AntiYandexVanced](https://raw.githubusercontent.com/retvil/AntiYandexVanced/main/logo.png =16)AntiYandexVanced](https://github.com/retvil/AntiYandexVanced)

## Qu'est-ce que c'est ?

WeChat n'installe pas qu'un navigateur — il s'enregistre silencieusement comme recherche et navigateur par défaut via quarante mécanismes système : associations dans le registre, politiques d'entreprise, paramètres de profils de navigateurs, même les bases de données de moteurs de recherche dans les profils Chromium. Supprimer le navigateur seul ne suffit pas.

**AntiWeChat Vanced** (un fork de [TheCawa/AntiYandex](https://github.com/TheCawa/AntiYandex)) trouve **les 28 vecteurs (VANCED) / 39 (EXTENDED) de détournement**, les supprime en un clic, puis **verrouille ta recherche par défaut** sur le moteur de ton choix via les politiques d'entreprise Windows — pour que rien ne puisse la reprendre silencieusement.

## Fonctionnalités

- **Scanner de détournements** — détecte 28 vecteurs (VANCED) / 39 vecteurs (EXTENDED): chemins d'installation, entrées Uninstall du registre, association `UserChoice`, enregistrements `StartMenuInternet`, arbres de clés `Software\WeChat`, détournement via les politiques `DefaultSearchProvider*`, `Preferences` des profils Chromium, mots-clés dans `Web Data` (SQLite), `search.json.mozlz4` Firefox, `SearchScopes` legacy, entrées d'autostart, tâches planifiées, services Windows, IME Switcher, associations de fichiers, intégration shell de WeChat Disk, autostart désactivé, App Paths, raccourcis, restes ProgramData/Roaming, entrées hosts, règles de pare-feu, protocoles URI, extensions de navigateur, cookies wechat.ru, associations « Ouvrir avec », traces Prefetch/WER, exclusions Defender, dispositions clavier, détournement de la page de démarrage IE, politiques d'URL de démarrage (`RestoreOnStartupURLs`), page d'accueil Firefox, zone map IE, entrées RegisteredApplications, traces MUICache, programmes d'installation dans %TEMP%, applications Store (WeChat Music), répertoires de produits, répertoires de données locales, WeChat.DNS
- **Suppression en un clic** — chaque vecteur a son propre remover ; les bases verrouillées sont signalées honnêtement, sans crash
- **Politique stricte de recherche** — verrouille la recherche par défaut sur l'un des 10 moteurs (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia, Yahoo, SearXNG) via les politiques HKLM pour Chrome, Edge, Brave, Vivaldi, Opera et WeChat Browser + `policies.json` pour Firefox/Waterfox
- **Nettoyage des politiques** — purge les valeurs `DefaultSearchProvider*` de WeChat du registre
- **10 langues d'interface** — ru, en, uk, kk, de, fr, es, pl, tr, zh ; langue du système détectée automatiquement
- **Interface légère** — ttkbootstrap, disposition verticale, barre d'état et pied de page fixés

## Capture d'écran

<details>
<summary>Fenêtre principale</summary>

![Fenêtre principale d'AntiWeChatVanced](docs/screenshot.png)

</details>

## Builds prêts à l'emploi

Téléchargez depuis [Releases](https://github.com/retvil/AntiWeChatVanced/releases) :

- **Windows** — `AntiWeChatVanced.exe` (portable, fichier unique, ~35 Mo) — supprime WeChat Browser et WeChat Search
- **Windows** — `AntiWeChatExtended.exe` (portable, fichier unique, ~35 Mo) — suppression de tous les produits WeChat (WeChat Disk, historique IME Switcher, traces système, applications Store, WeChat.DNS)

Lancez-le **en tant qu'administrateur** — les politiques HKLM et le nettoyage du registre exigent des droits élevés.

## Installation depuis les sources

Python 3.10+ requis ([python.org](https://python.org)).

```bash
git clone https://github.com/retvil/AntiWeChatVanced.git
cd AntiWeChatVanced
pip install psutil ttkbootstrap
python main.py
```

Compiler votre propre EXE : lancez `build.bat` (PyInstaller, résultat dans `dist/`).

## Utilisation

1. **Terminer les processus** → **Rechercher WeChat** → **Supprimer WeChat** — on retire le navigateur lui-même.
2. **Scanner les détournements** — liste toutes les façons dont WeChat s'est enraciné dans le système.
3. **Supprimer les détournements** — fermez d'abord tous les navigateurs, puis retirez tout ce qui est trouvé.
4. Choisissez un moteur → **Appliquer la politique** — la recherche par défaut est verrouillée au niveau du système.

## FAQ

- **Pourquoi administrateur ?** Les politiques de recherche vivent dans HKLM, le nettoyage touche le registre système — droits élevés requis.
- **« Database locked » dans les résultats ?** Un navigateur Chromium tournait pendant le nettoyage. Fermez tous les navigateurs et relancez la suppression.
- **Comment retirer la politique de recherche ?** Le bouton **Supprimer les politiques WeChat** purge les valeurs ; dans Firefox, vous pouvez aussi supprimer le fichier `distribution\policies.json`.

## Auteur & support

Автор: **Nod33Eset**. Изначальная идея: [TheCawa/AntiYandex](https://github.com/TheCawa/AntiYandex). Мы уже ушли далеко от простого форка.

Si l'outil t'a débarrassé de WeChat, tu peux soutenir le développement :

**Crypto :**

- BTC : `bc1qunld3rsp37qf5gg69aune50y0qqkd0eugg7j97`
- TON : `UQDmvr4SKOxSION3Yky6aOgzAnCDXySPuAbG4EKJa5JUT7tC`
- USDT (TRC20) : `TBPJSSLu1mUcX54g9UyxUohYGf2fuRvbwd`
- USDT (ERC20) : `0x25CAED3776Ef5b18E03392bC5b254Bbd78E8180C`
- USDT (SOL) : `3qgN5z291CEcj2FUi2Zza5DioxKgNw72kC7P52pCcTrG`

## Licence

MIT — voir [LICENSE](LICENSE).



