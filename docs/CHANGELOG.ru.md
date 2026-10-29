# Журнал изменений

Все значимые изменения проекта документируются в этом файле.

Формат основан на [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
проект следует [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

> Первоисточник — английский [CHANGELOG.md](CHANGELOG.md); этот перевод может немного отставать.

## [1.1.0] - 2026-10-22

### Добавлено
- **Скан зоны IE (zone map)** — находит записи zone-map для доменов WeChatа
  (остатки «надёжных сайтов»); удаление сносит поддерево домена (сначала экспорт)
- **Скан RegisteredApplications** — находит записи WeChatа в метаданных
  приложений по умолчанию; удаление стирает значение (сначала экспорт)
- **Скан MUICache** — находит следы запуска исполняемых файлов WeChatа;
  удаление стирает значение кэша (сначала экспорт)
- **Следы инсталляторов в %TEMP%** — scan_traces теперь также репортит
  инсталляторы WeChatа, оставшиеся во временной папке пользователя
- **Каталоги продуктов per-user** — scan_product_dirs теперь также покрывает
  `%LOCALAPPDATA%\Programs\WeChat*` (legacy-установки WeChat Музыки /
  Мессенджера / Переводчика), папка браузера исключена
- **Kill процессов по пути (Vanced)** — браузерный kill теперь также матчит
  процессы, чей exe лежит под путём WeChatBrowser (crashpad, updater),
  а не только узкий список имён browser.exe/wechat.exe
- **Скан hijack стартовых URL** — находит URL WeChatа в enterprise-политикаx
  `RestoreOnStartupURLs` (Edge, Chrome, Chromium, Brave, Vivaldi, Opera,
  WeChat.Браузер); удаление вычищает значения WeChatа
- **Скан hijack домашней страницы Firefox** — находит
  `browser.startup.homepage` со ссылкой на WeChat в `prefs.js`
  Firefox/Waterfox; удаление переписывает файл (сначала бэкап)

## [2.7.0] - 2026-10-21

### Добавлено
- **Скан WeChat.DNS** (Extended) — находит сетевые адаптеры с DNS-серверами
  WeChatа (77.88.8.x basic/safe/family); удаление возвращает адаптеру
  автоматический DNS; с подтверждением
- **Скан hijack стартовой страницы** — находит legacy-домашнюю страницу IE
  (`HKCU\...\Internet Explorer\Main\Start Page`) со ссылкой на WeChat/wechat.com;
  удаление возвращает дефолт (оба издания)

## [2.6.0] - 2026-10-21

### Добавлено
- **Extended-издание**: скан Store (Appx) приложений — находит WeChat Музыку,
  Алису, Мессенджер и другие Store-приложения WeChatа, удаляет через
  `Remove-AppxPackage`
- **Extended-издание**: скан каталогов небраузерных продуктов под
  `Program Files\WeChat\` (WeChat.Диск, WeChat IME Switcher, IME, ...) с бэкапом
  перед удалением
- **Extended-издание**: скан локальных данных небраузерных продуктов под
  `%LOCALAPPDATA%\WeChat\` (локальные данные WeChat IME Switcher, апдейтер
  WeChat.Диска, Beta-сборки) — с подтверждением, бэкап перед удалением
- **Extended-издание**: «Kill Processes» теперь завершает процессы всех
  продуктов WeChatа (WeChat.Диск, WeChat IME Switcher, Store-приложения),
  а не только браузера

## [2.5.0] - 2026-10-21

### Добавлено
- Два издания из одной кодовой базы: **AntiWeChatVanced** (удаление
  WeChat.Браузера + WeChat.Поиска) и **AntiWeChatExtended** (все продукты
  WeChatа) — профили продуктов в `profiles.py` выбирают охват скана, общий
  GUI в `app.py`, тонкие точки входа `main.py` / `main_extended.py`
- `build.bat` теперь собирает оба EXE

## [2.4.0] - 2026-10-21

### Добавлено
- 16-й–30-й векторы hijack: интеграция WeChat.Диска в оболочку (иконки-оверлеи
  + обработчики контекстного меню), отключённый автозапуск (`StartupApproved`),
  `App Paths`, ярлыки (Рабочий стол / Меню Пуск / панель задач),
  каталоги-остатки (ProgramData, Roaming, данные WeChat.Диска и
  синхронизированные файлы), записи `hosts`, правила брандмауэра Windows,
  обработчики URI-протоколов, расширения браузеров (манифесты Chromium +
  `.xpi` Firefox), куки wechat.ru (Chromium + Firefox), ассоциации
  `OpenWithProgids`/`OpenWithList`, следы Prefetch / CrashDumps / WER,
  исключения Windows Defender, пользовательские раскладки клавиатуры
  (WeChat IME)
- Подтверждение согласия: находки, затрагивающие пользовательские данные
  (файлы WeChat.Диска, история WeChat IME Switcher, расширения, куки, исключения
  Defender), требуют явного дополнительного подтверждения перед удалением
- Юнит-тесты для байт-детекта `.lnk`, фильтрации строк hosts, парсинга вывода
  брандмауэра и покрытия consent-префиксов

## [2.3.0] - 2026-10-20

### Добавлено
- 13-й–15-й векторы hijack: службы Windows (скан по реестру, удаление через
  `sc stop` + `sc delete`), WeChat IME Switcher (детект по маркеру `ime`),
  файловые ассоциации (скан + удаление ProgId в `FileExts\<ext>\UserChoice`)
- Диалог выбора после скана: выбрать, какие именно находки удалять, вместо
  «всё или ничего»
- Исключения: снятые галочки можно сохранить в
  `%APPDATA%\AntiWeChatVanced\exclusions.json` — будущие сканы автоматически
  их не выбирают, но они остаются доступными в диалоге; исключения можно
  сбросить из диалога
- Юнит-тесты персистентности исключений и маркера WeChat IME Switcher

## [2.2.0] - 2026-10-20

### Добавлено
- Бэкап перед удалением: каждый затронутый ключ реестра / файл профиля
  экспортируется в `%APPDATA%\AntiWeChatVanced\backup\<timestamp>\` перед
  удалением
- Журнал операций: `%APPDATA%\AntiWeChatVanced\antiwechat.log`
- 12-й вектор hijack: записи Планировщика задач Windows (задачи апдейтера
  WeChatа)
- Скан/чистка HKCU-политик Chromium (per-user политики, раньше только HKLM)
- Проверка прав администратора при старте с предупреждением в статус-баре
- Предложение закрыть запущенные браузеры перед удалением hijack
  (предотвращает «database locked»)
- Предложение «открыть папку отчёта», когда часть hijack-находок не удалилась
- Юнит-тесты чистой логики (поиск движка, Firefox policies.json,
  LZ4-декомпрессор)

### Исправлено
- Все обновления UI из фоновых потоков теперь маршалируются в главный поток
  через `root.after` (tkinter не потокобезопасен)
- Голые `except:` заменены на `except OSError`
- Чистка Web Data теперь удаляет ровно найденные строки (по `rowid`), а не по
  подстроке URL — детект и удаление согласованы
- SQLite-соединения закрываются на error-путях (`finally`)
- Firefox `policies.json` больше не содержит `null` `SuggestURLTemplate`
- Политики Firefox больше не пишутся в несуществующие папки установки
- Захардкоженная русская строка ошибки админа заменена на переводимый ключ
  во всех 10 языках UI
- `shutil.rmtree` теперь репортит, какие файлы заблокированы, вместо общей
  ошибки
- Битые LZ4-блоки с невалидными смещениями вызывают исключение вместо возврата
  мусора

## [2.1.2] - 2026-10-20

### Изменено
- Заголовок приложения сокращён до «Удаление WeChat» / «Remove WeChat»
  (ru/en/uk)
- Футер прижат к правому нижнему углу: автор, версия и кликабельная ссылка
  на GitHub
- Ссылка репозитория установлена на `https://github.com/retvil/AntiWeChatVanced`

## [2.1.0] - 2026-10-20

### Добавлено
- Вертикальная компоновка окна (560×700): центрированный стек действий,
  карточки секций на всю ширину
- Светлая тема UI на **ttkbootstrap** (тема `flatly`) — замена CustomTkinter
  на более лёгкий ttk-стек
- Футер с автором, версией и кликабельной ссылкой на репозиторий GitHub

### Изменено
- Миграция UI-библиотеки: tkinter → CustomTkinter → ttkbootstrap
- Селектор языка перенесён в правый верхний угол

## [2.0.0] - 2026-10-20

Форк [retvil/AntiYandexVanced](https://github.com/retvil/AntiYandexVanced) 1.3.

### Добавлено
- **Сканер hijack поиска** — детектит 11 векторов, которыми WeChat
  прописывается дефолтным поиском/браузером:
  - каталоги установки на диске
  - записи Uninstall в реестре (HKLM, WOW6432Node, HKCU)
  - ассоциация браузера по умолчанию Windows (`UserChoice` ProgId для
    http/https)
  - регистрации клиентов браузеров `StartMenuInternet`
  - отдельные деревья ключей `Software\WeChat` (HKCU/HKLM/WOW6432Node)
  - hijack через enterprise-политики `DefaultSearchProvider*` (жёсткий способ
    закрепления WeChatа)
  - per-profile JSON `Preferences` Chromium (Chrome, Edge, Brave, Vivaldi,
    WeChat.Браузер)
  - строки ключевых слов поисковиков в SQLite-базах `Web Data` Chromium
  - Firefox/Waterfox `search.json.mozlz4` (со встроенным pure-Python
    LZ4-декомпрессором блоков)
  - legacy-записи `SearchScopes` IE/Windows
  - записи автозапуска (`Run`/`RunOnce`)
- **Удаление hijack** — удаление всех найденных векторов одним кликом,
  у каждого вектора свой remover: рекурсивное удаление ключей реестра,
  сброс `UserChoice`, чистка `Preferences`, `DELETE FROM keywords` в Web Data,
  сброс `search.json.mozlz4` (Firefox пересоздаёт дефолты), удаление значений
  автозапуска. Заблокированные базы/файлы (браузер запущен) репортятся,
  без крашей.
- **Жёсткая политика поиска по умолчанию** — закрепляет один из 10
  поисковиков (Google, Bing, DuckDuckGo, Brave Search, Startpage, Mojeek,
  Qwant, Ecosia, Yahoo, SearXNG):
  - семейство Chromium через HKLM `SOFTWARE\Policies\...` значения
    `DefaultSearchProvider*` (Chrome, Edge, Brave, Vivaldi, Opera,
    WeChat.Браузер)
  - Firefox/Waterfox через `distribution\policies.json` (`SearchEngines` +
    `LockDefaultSearchEngine` + `PreventSearchEngineInstall`)
- Кнопка **«Удалить политики WeChatа»** — вычищает значения политик
  `DefaultSearchProvider*` WeChatа из реестра
- **10 языков UI** (ru, en, uk, kk, de, fr, es, pl, tr, zh) в отдельном модуле
  `translations.py`; язык системы определяется автоматически через Windows UI
  language API (`GetUserDefaultUILanguage`), фолбэк на английский
- Выпадающий список смены языка в UI

### Изменено
- Код разбит на модули: `engines.py`, `wechat_detect.py`, `policies.py`,
  `translations.py`, `main.py`

## [1.3.0] - upstream

База [retvil/AntiYandexVanced](https://github.com/retvil/AntiYandexVanced):
- Завершение процессов WeChat.Браузера (`browser.exe`, `wechat.exe`)
- Поиск путей установки
- Чистка записей Uninstall в реестре
- Удаление папки браузера
- Переключатель интерфейса RU/EN

[Unreleased]: https://github.com/retvil/AntiWeChatVanced/compare/v2.1.2...HEAD
[2.1.2]: https://github.com/retvil/AntiWeChatVanced/compare/v2.1.0...v2.1.2
[2.1.0]: https://github.com/retvil/AntiWeChatVanced/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/retvil/AntiWeChatVanced/compare/v1.3.0...v2.0.0


