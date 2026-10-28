# Değişiklik Günlüğü

Bu projedeki tüm önemli değişiklikler bu dosyada belgelenir.

Format [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) temel alınarak
hazırlanmıştır ve bu proje [Semantic Versioning](https://semver.org/spec/v2.0.0.html) ilkelerine uyar.

> Asıl kaynak İngilizce [CHANGELOG.md](CHANGELOG.md) dosyasıdır; bu çeviri biraz geride kalabilir.

## [2.8.0] - 2026-10-22

### Eklendi
- **IE bölge haritası taraması (zone map)** — WeChat alan adlarına ait
  zone-map girdilerini tespit eder («güvenilen siteler» kalıntıları);
  kaldırma, alan adının alt ağacını siler (önce dışa aktarım)
- **RegisteredApplications taraması** — varsayılan uygulama meta
  verilerindeki WeChat girdilerini tespit eder; kaldırma değeri siler
  (önce dışa aktarım)
- **MUICache taraması** — WeChat yürütülebilir dosyalarının çalıştırma
  izlerini tespit eder; kaldırma önbellek değerini siler (önce dışa
  aktarım)
- **%TEMP% içindeki yükleyici izleri** — scan_traces artık kullanıcının
  geçici klasöründe kalan WeChat yükleyicilerini de raporlar
- **Kullanıcı başına ürün dizinleri** — scan_product_dirs artık
  `%LOCALAPPDATA%\Programs\WeChat*` yolunu da kapsar (WeChat Music /
  Messenger / Translate legacy kurulumları), tarayıcı klasörü hariç
  tutulur
- **Yola göre süreç sonlandırma (Vanced)** — tarayıcıya özel kill artık
  yürütülebilir dosyası bir WeChatBrowser yolu altında bulunan süreçleri
  de eşleştirir (crashpad, updater), yalnızca dar browser.exe/wechat.exe
  ad listesini değil
- **Başlangıç URL ele geçirme taraması** — `RestoreOnStartupURLs`
  enterprise ilkelerindeki WeChat URL'lerini tespit eder (Edge, Chrome,
  Chromium, Brave, Vivaldi, Opera, WeChat Browser); kaldırma WeChat
  değerlerini temizler
- **Firefox ana sayfası ele geçirme taraması** — Firefox/Waterfox
  `prefs.js` içinde WeChat'e işaret eden `browser.startup.homepage`
  değerini tespit eder; kaldırma dosyayı yeniden yazar (önce yedek)

## [2.7.0] - 2026-10-21

### Eklendi
- **WeChat.DNS taraması** (Extended) — WeChat DNS sunucularıyla
  (77.88.8.x basic/safe/family) yapılandırılmış ağ bağdaştırıcılarını
  tespit eder; kaldırma bağdaştırıcıyı otomatik DNS'e döndürür; onaylı
- **Başlangıç sayfası ele geçirme taraması** — WeChat/wechat.com'yu işaret eden
  legacy IE başlangıç sayfasını (`HKCU\...\Internet Explorer\Main\Start
  Page`) tespit eder; kaldırma varsayılanı geri yükler (her iki sürüm)

## [2.6.0] - 2026-10-21

### Eklendi
- **Extended sürümü**: Store (Appx) uygulama taraması — WeChat Music,
  Messenger, Messenger ve diğer WeChat Store uygulamalarını tespit eder,
  `Remove-AppxPackage` ile kaldırır
- **Extended sürümü**: `Program Files\WeChat\` altındaki tarayıcı dışı
  ürün dizinleri taraması (WeChat Disk, WeChat IME Switcher, IME, ...) —
  kaldırmadan önce yedek
- **Extended sürümü**: `%LOCALAPPDATA%\WeChat\` altındaki tarayıcı dışı
  yerel veri taraması (WeChat IME Switcher yerel verileri, WeChat Disk
  güncelleyicisi, Beta derlemeleri) — onaylı, kaldırmadan önce yedek
- **Extended sürümü**: «Kill Processes» artık yalnızca tarayıcıyı değil,
  tüm WeChat ürün süreçlerini (WeChat Disk, WeChat IME Switcher, Store
  uygulamaları) sonlandırır

## [2.5.0] - 2026-10-21

### Eklendi
- Tek kod tabanından iki sürüm: **AntiWeChatVanced** (WeChat Browser +
  WeChat Arama kaldırma) ve **AntiWeChatExtended** (tüm WeChat ürünleri) —
  `profiles.py` içindeki ürün profilleri tarama kapsamını seçer, ortak GUI
  `app.py` içinde, ince giriş noktaları `main.py` / `main_extended.py`
- `build.bat` artık her iki EXE'yi de derler

## [2.4.0] - 2026-10-21

### Eklendi
- 16.–30. ele geçirme vektörleri: WeChat Disk kabuk entegrasyonu (simge
  kaplamaları + bağlam menüsü işleyicileri), devre dışı otostart
  (`StartupApproved`), `App Paths`, kısayollar (Masaüstü / Başlat Menüsü /
  görev çubuğu), kalıntı dizinleri (ProgramData, Roaming, WeChat Disk
  verileri ve senkronize dosyalar), `hosts` girdileri, Windows güvenlik
  duvarı kuralları, URI protokol işleyicileri, tarayıcı eklentileri
  (Chromium manifestleri + Firefox `.xpi`), wechat.ru çerezleri (Chromium
  + Firefox), `OpenWithProgids`/`OpenWithList` ilişkilendirmeleri,
  Prefetch / CrashDumps / WER izleri, Windows Defender istisnaları,
  özel klavye düzenleri (WeChat IME)
- Onay mekanizması: kullanıcı verilerine dokunan bulgular (WeChat Disk
  dosyaları, WeChat IME Switcher geçmişi, eklentiler, çerezler, Defender
  istisnaları) kaldırmadan önce açık ek onay gerektirir
- `.lnk` bayt tespiti, hosts satır filtreleme, güvenlik duvarı çıktısı
  ayrıştırma ve onay öneki kapsamı için birim testler

## [2.3.0] - 2026-10-20

### Eklendi
- 13.–15. ele geçirme vektörleri: Windows hizmetleri (kayıt defteri
  tabanlı tarama, `sc stop` + `sc delete` ile kaldırma), WeChat IME Switcher
  (`ime` işaretiyle tespit), dosya ilişkilendirmeleri
  (`FileExts\<ext>\UserChoice` ProgId taraması + kaldırma)
- Tarama sonrası seçim diyaloğu: «hepsi ya da hiçbiri» yerine tam olarak
  hangi bulguların kaldırılacağını seçme
- Hariç tutmalar: işareti kaldırılan bulgular
  `%APPDATA%\AntiWeChatVanced\exclusions.json` içine kaydedilebilir —
  gelecekteki taramalar bunları otomatik olarak seçmez, ancak diyalogda
  seçilebilir kalırlar; hariç tutmalar diyalogdan sıfırlanabilir
- Hariç tutma kalıcılığı ve WeChat IME Switcher işareti için birim testler

## [2.2.0] - 2026-10-20

### Eklendi
- Kaldırmadan önce yedek: dokunulan her kayıt defteri anahtarı / profil
  dosyası silmeden önce
  `%APPDATA%\AntiWeChatVanced\backup\<timestamp>\` içine dışa aktarılır
- İşlem günlüğü: `%APPDATA%\AntiWeChatVanced\antiwechat.log`
- 12. ele geçirme vektörü: Windows Görev Zamanlayıcı girdileri (WeChat
  güncelleyici görevleri)
- HKCU Chromium ilke taraması/temizliği (kullanıcı başına ilkeler, daha
  önce yalnızca HKLM)
- Başlangıçta yönetici hakları kontrolü, durum çubuğunda uyarıyla
- Ele geçirme kaldırmadan önce çalışan tarayıcıları kapatma istemi
  («database locked» engeller)
- Bazı ele geçirme öğeleri kaldırılamadığında «rapor klasörünü aç» önerisi
- Saf mantık için birim testler (motor arama, Firefox policies.json,
  LZ4 açıcı)

### Düzeltildi
- Arka plan iş parçacıklarından gelen tüm UI güncellemeleri artık
  `root.after` aracılığıyla ana iş parçacığına yönlendirilir (tkinter iş
  parçacığı güvenli değildir)
- Çıplak `except:` blokları `except OSError` ile değiştirildi
- Web Data temizliği artık tam olarak tespit edilen satırları siler
  (`rowid` ile), URL alt dizesine göre değil — tespit ve silme tutarlıdır
- SQLite bağlantıları hata yollarında kapatılır (`finally`)
- Firefox `policies.json` artık `null` `SuggestURLTemplate` içermiyor
- Firefox ilkeleri artık var olmayan kurulum klasörlerine yazılmıyor
- Sert kodlanmış Rusça yönetici hata metni, 10 UI dilinde çevrilebilir
  bir anahtarla değiştirildi
- `shutil.rmtree` artık genel bir hata yerine hangi dosyaların kilitli
  olduğunu raporlar
- Geçersiz eşleşme ofsetleri olan bozuk LZ4 blokları çöp döndürmek yerine
  istisna fırlatır

## [2.1.2] - 2026-10-20

### Değiştirildi
- Uygulama başlığı «Удаление WeChat» / «Remove WeChat» (ru/en/uk) olarak
  kısaltıldı
- Alt bilgi sağ alt köşeye sabitlendi: yazar, sürüm ve tıklanabilir
  GitHub bağlantısı
- Depo bağlantısı `https://github.com/retvil/AntiWeChatVanced` olarak
  ayarlandı

## [2.1.0] - 2026-10-20

### Eklendi
- Dikey pencere düzeni (560×700): ortalanmış eylem yığını, tam genişlikte
  bölüm kartları
- **ttkbootstrap** üzerinde açık tema (`flatly`) — CustomTkinter yerine
  daha hafif bir ttk yığını
- Yazar, sürüm ve tıklanabilir GitHub deposu bağlantısı içeren alt bilgi

### Değiştirildi
- UI kitaplığı göçü: tkinter → CustomTkinter → ttkbootstrap
- Dil seçici sağ üst köşeye taşındı

## [2.0.0] - 2026-10-20

[TheCawa/AntiYandex](https://github.com/TheCawa/AntiYandex) 1.3 çatalı.

### Eklendi
- **Arama ele geçirme tarayıcısı** — WeChat'in varsayılan
  arama/tarayıcı olarak kurulmasını sağlayan 11 vektörü tespit eder:
  - diskteki kurulum dizinleri
  - kayıt defterindeki Uninstall girdileri (HKLM, WOW6432Node, HKCU)
  - Windows varsayılan tarayıcı ilişkilendirmesi (http/https için
    `UserChoice` ProgId)
  - `StartMenuInternet` tarayıcı istemci kayıtları
  - bağımsız `Software\WeChat` anahtar ağaçları (HKCU/HKLM/WOW6432Node)
  - `DefaultSearchProvider*` enterprise ilkeleri üzerinden ele geçirme
    (WeChat'in kendini dayattığı «sert» yol)
  - Chromium profillerinin profil başına `Preferences` JSON'u (Chrome,
    Edge, Brave, Vivaldi, WeChat Browser)
  - Chromium `Web Data` SQLite veritabanlarındaki arama motoru anahtar
    kelime satırları
  - Firefox/Waterfox `search.json.mozlz4` (yerleşik pure-Python LZ4 blok
    açıcı ile)
  - legacy IE/Windows `SearchScopes` girdileri
  - otostart girdileri (`Run`/`RunOnce`)
- **Ele geçirme kaldırma** — tespit edilen her vektörün tek tıkla
  kaldırılması, her vektörün kendi remover'ı vardır: kayıt defteri
  anahtarlarının özyinelemeli silinmesi, `UserChoice` sıfırlama,
  `Preferences` temizliği, Web Data içinde `DELETE FROM keywords`,
  `search.json.mozlz4` sıfırlama (Firefox varsayılanları yeniden
  oluşturur), otostart değerlerinin silinmesi. Kilitli
  veritabanları/dosyalar (tarayıcı çalışıyor) raporlanır, çökme yok.
- **Sert varsayılan arama politikası** — 10 arama motorundan birini
  zorunlu kılar (Google, Bing, DuckDuckGo, Brave Search, Startpage,
  Mojeek, Qwant, Ecosia, Yahoo, SearXNG):
  - Chromium ailesi HKLM `SOFTWARE\Policies\...` `DefaultSearchProvider*`
    değerleriyle (Chrome, Edge, Brave, Vivaldi, Opera, WeChat Browser)
  - Firefox/Waterfox `distribution\policies.json` ile (`SearchEngines` +
    `LockDefaultSearchEngine` + `PreventSearchEngineInstall`)
- **«WeChat ilkelerini kaldır»** düğmesi — WeChat `DefaultSearchProvider*`
  ilke değerlerini kayıt defterinden temizler
- **10 UI dili** (ru, en, uk, kk, de, fr, es, pl, tr, zh) ayrılmış
  `translations.py` modülünde; sistem dili Windows UI language API
  aracılığıyla otomatik algılanır (`GetUserDefaultUILanguage`), eşleşme
  yoksa İngilizceye düşer
- UI'da dil değiştirme açılır listesi

### Değiştirildi
- Kod modüllere bölündü: `engines.py`, `wechat_detect.py`, `policies.py`,
  `translations.py`, `main.py`

## [1.3.0] - upstream

[TheCawa/AntiYandex](https://github.com/TheCawa/AntiYandex) tabanı:
- WeChat Browser süreçlerinin sonlandırılması (`browser.exe`, `wechat.exe`)
- Kurulum yollarının aranması
- Kayıt defterindeki Uninstall girdilerinin temizlenmesi
- Tarayıcı klasörünün silinmesi
- RU/EN arayüz anahtarı

[Unreleased]: https://github.com/retvil/AntiWeChatVanced/compare/v2.1.2...HEAD
[2.1.2]: https://github.com/retvil/AntiWeChatVanced/compare/v2.1.0...v2.1.2
[2.1.0]: https://github.com/retvil/AntiWeChatVanced/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/retvil/AntiWeChatVanced/compare/v1.3.0...v2.0.0

