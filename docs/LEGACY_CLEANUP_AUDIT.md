# Legacy cleanup audit (T-003) — production `sibway.com.ua`

Дата: 2026-09-22. Режим: **read-only**, лише публічні GET/HEAD-запити до
`https://sibway.com.ua` (≈180 адрес), без SFTP/FileZilla, без видалень.
Дозвіл власника на read-only HTTP-перевірки production отримано 22.09.2026.

## Метод і обмеження

- Еталон «поточного runtime» — файли, відстежувані в `sibway-website-`
  (`git ls-files`: HTML uk/en/pl, `css/style.css`, `js/main.js`,
  `img/hero-truck.webp`, `img/about-warehouse.webp`, `img/brand/*`,
  `favicon.svg`, `og-image.png`, `robots.txt`, `sitemap.xml`, кореневий
  `index.html`). Службові `README.md`, `DEPLOYMENT.md`, `content-drafts/`
  на хостинг не потрапляють (перевірено: 404/заблоковано).
- Перелік legacy-файлів зібрано з трьох джерел: відомі шляхи з T-003,
  посилання в HTML старого сайту (`/index.php`) і **публічно доступні
  `.DS_Store`-файли** (macOS-службові файли, які розкривають імена файлів
  у каталогах — див. S-3).
- Повного дерева файлів хостингу звідси не видно (listing каталогів
  закритий, 403). Для 100% inventory потрібен експорт списку файлів із
  FileZilla від власника.
- ⚠️ Під час перевірки `GET /contact_form.php` виконано двічі (звичайне
  відкриття адреси). Скрипт відповів «Ваш запит надіслано!» — можливо,
  на `sibway@ukr.net` прийшли 1–2 порожні листи від старої форми. Це
  побічний ефект самої вразливості S-1, не нова відправка даних.

## Критичні знахідки

| ID | Шлях | Що відбувається | Ризик |
|---|---|---|---|
| **S-1** | `/contact_form.php` | Старий обробник форми відповідає 200 і текстом «Ваш запит надіслано!» навіть на простий GET без даних | Будь-хто (боти) може слати через нього листи / спам на пошту компанії; можлива зловживання як mail-relay. **Security exposure** |
| **S-2** | `/index.php` | Повністю робочий **старий сайт** (39 КБ): старий дизайн, `canonical` → `https://sibway.com.ua/`, старий GA4 `G-CN7867WYLT`, сторонній трекер `cstat.nextel.com.ua`, форма `#form`, jQuery 3.4.1 / Bootstrap 5.0.0 з CDN, при цьому підвантажує **нові** `css/style.css` і `js/main.js` (зламана верстка) | Дублікат/застарілий контент, плутанина в аналітиці (подвійний GA), застарілі залежності. У Google наразі **не проіндексовано** (URL Inspection: «URL-адреси немає в Google») — вікно, щоб прибрати без SEO-втрат |
| **S-3** | `/.DS_Store`, `/img/.DS_Store`, `/lib/.DS_Store`, `/fonts/.DS_Store`, `/js/.DS_Store`, `/fonts/Gilroy/.DS_Store`, `/img/service-tmp/.DS_Store` | macOS-службові файли, доступні публічно (200) | Розкривають структуру каталогів (саме з них зібрано цей inventory). Info-leak, низька складність усунення |

## Повний inventory і класифікація

Легенда: **R** — current runtime; **C** — candidate for removal; **S** — security exposure candidate; **L** — leave for now; **O** — unknown / owner decision.

### Корінь

| Шлях | HTTP | Розмір | Клас | Коментар |
|---|---|---|---|---|
| `/index.html` | 200 | 329 Б | R | Редирект-файл на `uk/index.html`, `noindex` (див. T-002: рекомендовано серверний 301) |
| `/index.php` | 200 | 39 КБ | S / C | Старий сайт (S-2) |
| `/contact_form.php` | 200 | 98 Б | **S** | Старий обробник форми (S-1) |
| `/.DS_Store` | 200 | 6 КБ | S / C | S-3 |
| `/robots.txt`, `/sitemap.xml`, `/favicon.svg`, `/og-image.png`, `/404.html` | 200 | — | R | |
| `/.htaccess`, `/.git/*`, `/.env`, `/wp-config.php`, `/README.md` | 424 | — | L | Закрито WAF Cityhost («Failed Dependency») — наявність файлів невідома |
| `/.htpasswd` | 403 | — | L | Закрито |
| `/wp-login.php`, `/wp-admin/`, `/admin/`, `/administrator/` | 423 | — | L | Сторінка «Secured by CityHost.ua» — захист хостингу, не файли сайту |
| Бекапи/архіви/дампи/логи (`*.zip`, `*.tar.gz`, `*.sql`, `error_log`, `phpinfo.php` тощо, 30+ імен) | 404 | — | — | Не знайдено ✅ |

### `/css/`

| Шлях | HTTP | Розмір | Клас | Коментар |
|---|---|---|---|---|
| `/css/style.css` | 200 | 31 КБ | R | Поточний (перезаписаний новим сайтом) |
| `/css/bootstrap.min.css` | 200 | 164 КБ | C | Legacy, новим сайтом не використовується |

### `/js/`

| Шлях | HTTP | Розмір | Клас | Коментар |
|---|---|---|---|---|
| `/js/main.js` | 200 | 24 КБ | R | Поточний |
| `/js/internationalisation.js` | 200 | 14 КБ | C | Legacy (i18n старого сайту) |
| `/js/.DS_Store` | 200 | 6 КБ | S / C | S-3 |

### `/lib/` (усе legacy, використовується лише `index.php`)

| Шлях | HTTP | Розмір | Клас |
|---|---|---|---|
| `/lib/animate/animate.min.css` | 200 | 17 КБ | C |
| `/lib/counterup/counterup.min.js` | 200 | 2 КБ | C |
| `/lib/easing/easing.min.js` | 200 | 2 КБ | C |
| `/lib/owlcarousel/owl.carousel.min.js` | 200 | 43 КБ | C |
| `/lib/owlcarousel/assets/owl.carousel.min.css` | 200 | 3 КБ | C |
| `/lib/waypoints/waypoints.min.js` | 200 | 9 КБ | C |
| `/lib/wow/wow.min.js` | 200 | 8 КБ | C |
| `/lib/jquery.inputmask.min.js` | 200 | 228 КБ | C |
| `/lib/.DS_Store` | 200 | 8 КБ | S / C |

### `/scss/`

| Шлях | HTTP | Розмір | Клас | Коментар |
|---|---|---|---|---|
| `/scss/bootstrap.scss` | 200 | <1 КБ | C | Вихідний SCSS старого сайту відкрито публічно |
| `/scss/bootstrap.css` | 200 | 256 КБ | C | Скомпільований CSS старого сайту |
| `/scss/bootstrap/` | 403 | — | C / O | Каталог існує, вміст невідомий |

### `/fonts/`

| Шлях | HTTP | Клас | Коментар |
|---|---|---|---|
| `/fonts/Gilroy/`, `/fonts/TTNorms/` | 403 | C / O | Шрифти старого сайту. Новий сайт їх не підключає. ⚠️ Комерційні шрифти — перевірити ліцензію; публічний хостинг файлів шрифтів без ліцензії — юридичний ризик |
| `/fonts/.DS_Store`, `/fonts/Gilroy/.DS_Store` | 200 | S / C | S-3 |

### `/img/`

| Шлях | HTTP | Розмір | Клас |
|---|---|---|---|
| `/img/hero-truck.webp`, `/img/about-warehouse.webp`, `/img/brand/*` | 200 | — | R |
| `/img/logo.svg`, `/img/favicon.ico`, `/img/map.png` | 200 | 4 КБ / 15 КБ / 33 КБ | C |
| `/img/about.jpg` | 200 | 23 КБ | C |
| `/img/carousel-2.jpg`, `carousel-22.jpg`, `carousel-3.jpg`, `carousel-33.jpg` | 200 | 187 КБ / 176 КБ / 1,5 МБ / 159 КБ | C |
| `/img/feature-1.jpg`, `feature-2.jpg`, `feature-3.jpg` | 200 | **4,9 МБ / 6,9 МБ** / 464 КБ | C |
| `/img/service-1.jpg` … `service-4.jpg` | 200 | 1,6 МБ / 2,1 МБ / 49 КБ / 612 КБ | C |
| `/img/team-1.jpg` … `team-4.jpg` | 200 | 10–14 КБ | C / O (можливо, фото людей — персональні дані) |
| `/img/testimonial-1.jpg` … `-4.jpg` | 200 | 3 КБ | C / O (фото «відгуків» старого шаблону) |
| `/img/service-tmp/` | 403 | — | C / O |
| `/img/.DS_Store`, `/img/service-tmp/.DS_Store` | 200 | 8 КБ / 6 КБ | S / C |

Разом legacy у `/img/` — ≈ 18 МБ публічних файлів.

## Інші технічні спостереження (для техаудиту)

- Сервер повертає **стандартну Apache-сторінку 404** (196 байт, iso-8859-1),
  хоча на сайті є брендована `/404.html` → не налаштовано `ErrorDocument 404`.
- `/favicon.ico` → 404 (браузери запитують його автоматично); новий сайт
  використовує `favicon.svg`. Legacy `img/favicon.ico` існує.
- Сторінки `*/services/import-poland.html` на production поки 404 — очікувано,
  вони ще не задеплоєні.

## Запропоновані cleanup-хвилі (виконання — лише за окремим рішенням власника)

Перед кожною хвилею: бекап видалюваних файлів локально (не в web-root),
після — перевірка критичних URL production (`/`, `/uk/`, `/en/`, `/pl/`,
сторінки послуг, форма, `robots.txt`, `sitemap.xml`) і повтор цього аудиту.

| Хвиля | Що | Навіщо | Ризик |
|---|---|---|---|
| **1 — безпека (рекомендовано якнайшвидше)** | `contact_form.php`; усі `.DS_Store` (7 шт.) | Закрити відкритий обробник пошти й info-leak | Мінімальний: новий сайт їх не використовує (форма нового сайту — Formspree) |
| **2 — старий сайт** | `index.php` | Прибрати дубль старого сайту, старий GA-тег і сторонній трекер | Мінімальний; у Google не проіндексовано. Опційно замість видалення — 301 на `/uk/index.html` (server rules — окремий дозвіл) |
| **3 — legacy-ресурси** | `lib/`, `scss/`, `css/bootstrap.min.css`, `js/internationalisation.js`, legacy-картинки `img/*.jpg`, `img/logo.svg`, `img/map.png`, `img/favicon.ico`, `img/service-tmp/` | Прибрати ~19 МБ непотрібних файлів | Низький: використовуються лише `index.php` (після хвилі 2 — ніким) |
| **4 — рішення власника** | `fonts/Gilroy/`, `fonts/TTNorms/`, фото `team-*`, `testimonial-*` | Ліцензія шрифтів, персональні дані на фото | Потрібне рішення: видалити чи зберегти архівно поза web-root |
| **5 — конфігурація (окремий дозвіл, server rules)** | `ErrorDocument 404 /404.html`; 301 для `/index.html` і `/index.php` | UX + SEO | Зміна `.htaccess` на production |

## Статус

Inventory + класифікація + хвилі готові до рішення власника. Жоден файл
на хостингу не змінено й не видалено.
