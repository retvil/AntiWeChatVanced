# AntiWeChat Vanced

**🇬🇧 English** | [🇷🇺 Русский](README.ru.md) | [🇺🇦 Українська](README.uk.md) | [🇰🇿 Қазақша](README.kk.md) | [🇩🇪 Deutsch](README.de.md) | [🇫🇷 Français](README.fr.md) | [🇪🇸 Español](README.es.md) | [🇵🇱 Polski](README.pl.md) | [🇹🇷 Türkçe](README.tr.md) | [🇨🇳 中文](README.zh.md)

## 🌐 Forks

<a href="https://github.com/retvil/AntiBaiduVanced"><img src="https://raw.githubusercontent.com/retvil/AntiBaiduVanced/main/logo.png" alt="AntiBaiduVanced" width="16" height="16" style="vertical-align:middle"> AntiBaiduVanced</a>  |  <a href="https://github.com/retvil/AntiSogouVanced"><img src="https://raw.githubusercontent.com/retvil/AntiSogouVanced/main/logo.png" alt="AntiSogouVanced" width="16" height="16" style="vertical-align:middle"> AntiSogouVanced</a>  |  <a href="https://github.com/retvil/Anti2345Vanced"><img src="https://raw.githubusercontent.com/retvil/Anti2345Vanced/main/logo.png" alt="Anti2345Vanced" width="16" height="16" style="vertical-align:middle"> Anti2345Vanced</a>  |  <a href="https://github.com/retvil/AntiUCWebVanced"><img src="https://raw.githubusercontent.com/retvil/AntiUCWebVanced/main/logo.png" alt="AntiUCWebVanced" width="16" height="16" style="vertical-align:middle"> AntiUCWebVanced</a>  |  <a href="https://github.com/retvil/AntiNaverVanced"><img src="https://raw.githubusercontent.com/retvil/AntiNaverVanced/main/logo.png" alt="AntiNaverVanced" width="16" height="16" style="vertical-align:middle"> AntiNaverVanced</a>  |  <a href="https://github.com/retvil/AntiKakaoVanced"><img src="https://raw.githubusercontent.com/retvil/AntiKakaoVanced/main/logo.png" alt="AntiKakaoVanced" width="16" height="16" style="vertical-align:middle"> AntiKakaoVanced</a>  |  <a href="https://github.com/retvil/AntiQQVanced"><img src="https://raw.githubusercontent.com/retvil/AntiQQVanced/main/logo.png" alt="AntiQQVanced" width="16" height="16" style="vertical-align:middle"> AntiQQVanced</a>  |  **AntiWeChatVanced**  |  <a href="https://github.com/retvil/AntiTencentVideoVanced"><img src="https://raw.githubusercontent.com/retvil/AntiTencentVideoVanced/main/logo.png" alt="AntiTencentVideoVanced" width="16" height="16" style="vertical-align:middle"> AntiTencentVideoVanced</a>  |  <a href="https://github.com/retvil/AntiVKGroupVanced"><img src="https://raw.githubusercontent.com/retvil/AntiVKGroupVanced/main/logo.png" alt="AntiVKGroupVanced" width="16" height="16" style="vertical-align:middle"> AntiVKGroupVanced</a>  |  <a href="https://github.com/retvil/AntiYandexVanced"><img src="https://raw.githubusercontent.com/retvil/AntiYandexVanced/main/logo.png" alt="AntiYandexVanced" width="16" height="16" style="vertical-align:middle"> AntiYandexVanced</a>

## ¿Qué es esto?

WeChat no instala solo un navegador — se registra silenciosamente como buscador y navegador predeterminado a través de cuarenta mecanismos del sistema: asociaciones en el registro, políticas de empresa, ajustes de perfiles de navegadores, incluso bases de datos de buscadores dentro de los perfiles Chromium. Eliminar el navegador por sí solo no deshace todo eso.

**AntiWeChat Vanced** (un fork de [retvil/AntiYandexVanced](https://github.com/retvil/AntiYandexVanced)) encuentra **los 28/39 vectores de secuestro**, los elimina con un clic y luego **bloquea tu buscador predeterminado** al motor que elijas mediante políticas de empresa de Windows — para que nada pueda recuperarlo silenciosamente.

## Características

- **Escáner de secuestros** — detecta 28 vectores (VANCED) / 39 vectores (EXTENDED): rutas de instalación, entradas Uninstall del registro, asociación `UserChoice`, registros `StartMenuInternet`, árboles de claves `Software\WeChat`, secuestro vía políticas `DefaultSearchProvider*`, `Preferences` de perfiles Chromium, palabras clave en `Web Data` (SQLite), `search.json.mozlz4` de Firefox, `SearchScopes` legacy, entradas de autostart, tareas programadas, servicios de Windows, IME Switcher, asociaciones de archivos, integración de shell de WeChat Disk, autostart deshabilitado, App Paths, accesos directos, restos en ProgramData/Roaming, entradas de hosts, reglas de firewall, protocolos URI, extensiones de navegador, cookies de wechat.ru, asociaciones «Abrir con», rastros Prefetch/WER, exclusiones de Defender, distribuciones de teclado, secuestro de la página de inicio de IE, políticas de URL de inicio (`RestoreOnStartupURLs`), página de inicio de Firefox, zone map de IE, entradas RegisteredApplications, rastros MUICache, instaladores en %TEMP%, aplicaciones de la Store (WeChat Music), directorios de productos, directorios de datos locales, WeChat.DNS
- **Eliminación con un clic** — cada vector tiene su propio remover; las bases bloqueadas se reportan honestamente, sin crashes
- **Política estricta de búsqueda** — bloquea el buscador predeterminado a uno de 10 motores (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek, Qwant, Ecosia, Yahoo, SearXNG) vía políticas HKLM para Chrome, Edge, Brave, Vivaldi, Opera y WeChat Browser + `policies.json` para Firefox/Waterfox
- **Limpieza de políticas** — purga los valores `DefaultSearchProvider*` de WeChat del registro
- **10 idiomas de interfaz** — ru, en, uk, kk, de, fr, es, pl, tr, zh; idioma del sistema detectado automáticamente
- **Interfaz ligera** — ttkbootstrap, disposición vertical, barra de estado y pie de página fijados

## Captura de pantalla

<details>
<summary>Ventana principal</summary>

![Ventana principal de AntiWeChatVanced](screenshot.png)

</details>

## Builds listos

Descarga desde [Releases](https://github.com/retvil/AntiWeChatVanced/releases):

- **Windows** — `AntiWeChatVanced.exe` (portable, archivo único, ~35 MB) — elimina WeChat Browser y la Búsqueda de WeChat
- **Windows** — `AntiWeChatExtended.exe` (portable, archivo único, ~35 MB) — eliminación de todos los productos de WeChat (WeChat Disk, historial de IME Switcher, rastros en todo el sistema, aplicaciones de la Store, WeChat.DNS)

Ejecútalo **como administrador** — las políticas HKLM y la limpieza del registro requieren permisos elevados.

## Instalación desde el código fuente

Se requiere Python 3.10+ ([python.org](https://python.org)).

```bash
git clone https://github.com/retvil/AntiWeChatVanced.git
cd AntiWeChatVanced
pip install psutil ttkbootstrap
python main.py
```

Compilar tu propio EXE: ejecuta `build.bat` (PyInstaller, resultado en `dist/`).

## Uso

1. **Terminar procesos** → **Buscar WeChat** → **Eliminar WeChat** — eliminamos el navegador en sí.
2. **Escanear secuestros de búsqueda** — muestra todas las formas en que WeChat se enraizó en el sistema.
3. **Eliminar secuestros** — cierra primero todos los navegadores, luego elimina todo lo encontrado.
4. Elige un motor → **Aplicar política** — el buscador predeterminado queda bloqueado a nivel del sistema.

## FAQ

- **¿Por qué administrador?** Las políticas de búsqueda viven en HKLM, la limpieza toca el registro del sistema — se necesitan permisos elevados.
- **¿«Database locked» en los resultados?** Un navegador Chromium estaba en ejecución durante la limpieza. Cierra todos los navegadores y repite la eliminación.
- **¿Cómo quito la política de búsqueda?** El botón **Quitar políticas de WeChat** purga los valores; en Firefox también puedes eliminar el archivo `distribution\policies.json`.

## Autor y apoyo

Изначальная идея: [retvil/AntiYandexVanced](https://github.com/retvil/AntiYandexVanced)

Si la herramienta te libró de WeChat, puedes apoyar el desarrollo:

**Cripto:**

- BTC: `bc1qunld3rsp37qf5gg69aune50y0qqkd0eugg7j97`
- TON: `UQDmvr4SKOxSION3Yky6aOgzAnCDXySPuAbG4EKJa5JUT7tC`
- USDT (TRC20): `TBPJSSLu1mUcX54g9UyxUohYGf2fuRvbwd`
- USDT (ERC20): `0x25CAED3776Ef5b18E03392bC5b254Bbd78E8180C`
- USDT (SOL): `3qgN5z291CEcj2FUi2Zza5DioxKgNw72kC7P52pCcTrG`

## Licencia

MIT — ver [LICENSE](../LICENSE).





