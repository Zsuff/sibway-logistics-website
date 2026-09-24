# Changelog

## 2026-09-24 (3)

### P2-техаудит виконано (PR #16 змерджено), P1-2/P2-11 (.htaccess) на продакшені

- **PR #16** (`fix/a11y-contrast-jsonld-p2`, 50 файлів) змерджено в `main`
  (squash, sha `41a93a1`). Зміст:
  - **P1-3/P2-5**: контраст CTA-кнопок і бренд-синього/сірого тексту
    приведено до WCAG 2.1 AA (`--blue-dark`/`--blue-darker`/`--gray-500`
    затемнено; брендовий `--blue #189CD9` не чіпали).
  - **P2-3**: JSON-LD `Service` + `BreadcrumbList` додано на 18 сторінках
    (4 сервісні + about + contacts × 3 мови) — 52 валідних блоки.
  - **P2-4**: блок «Читайте також» (посилання на блог) на 7 сервісних
    сторінках (uk).
  - **P2-6**: тап-цілі посилань футера збільшено (padding-block).
  - **P2-7**: підкреслення посилання «Політика конфіденційності».
  - **P2-8**: `contacts.html` — заголовки карток контактів H3→H2 (3 мови).
  - **P2-9**: `.reveal` не ховає контент без JS (`<noscript>` фолбек,
    48 сторінок).
  - **P2-10**: додано `favicon.ico`.
  - Перевірка: `site_check.py` P0=0/P1=0/P2=0 (48 сторінок), 52/52 ld+json
    валідні, баланс тегів ОК.
- **P1-2 + P2-11** (`.htaccess`, production): додано `ErrorDocument 404
  /404.html` і серверний `RewriteRule` 301 для кореня (`/`, `/index.php`
  → `/uk/index.html`); `DirectoryIndex` залишено без змін. Застосовано
  через FileZilla на автентифікованій сесії власника, окреме підтвердження
  отримано окремо від загального P2-схвалення (server rules — свій
  approval-gate). Смоук-тест після заливки:
  - `/` → 301 → `/uk/index.html`; `/index.php` → 301 → `/uk/index.html`.
  - `/index.html` (пряме звернення) — і далі 200 без серверного редиректу:
    хостинг віддає статичні `.html`-файли через nginx напряму, минаючи
    Apache/`.htaccess`; для цього шляху й далі працює лише клієнтський
    редирект (`meta refresh` + `location.replace()` в самому `index.html`,
    він уже був). Це особливість інфраструктури хостингу, не помилка
    правила.
  - Неіснуючий URL → 404, віддає наш брендований `404.html`.
  - `robots.txt`, `sitemap.xml`, `css/style.css`, `js/main.js`,
    `en/index.html`, `pl/index.html`, `uk/contacts.html`,
    `contact_form.php`/`.DS_Store` (легасі, мають бути 404) — всі ОК.
- **Заміна GitHub-токена** — за рішенням власника відкладено
  («забий на це»), не виконувалось.

## 2026-09-24 (2)

### T-004 DONE; legacy cleanup хвиля 1 на хостингу

- **T-004** → DONE: власник підтвердив ручну перевірку форми/CTA/мобільного
  меню на production — без зауважень.
- **Legacy cleanup — хвиля 1** (`docs/LEGACY_CLEANUP_AUDIT.md`) виконана:
  видалено `contact_form.php` (відкритий legacy-обробник форми, S-1) і всі
  7 `.DS_Store` (корінь, `img/`, `img/service-tmp/`, `js/`, `lib/`, `fonts/`,
  `fonts/Gilroy/`) через FileZilla на автентифікованій сесії власника.
  Пост-перевірка: критичні URL → 200, усі 8 видалених шляхів → 404.
- Хвилі 2–5 (старий `index.php`, legacy-ресурси `lib/`/`scss/`,
  шрифти/фото, server rules) — далі за рішенням власника.

## 2026-09-24

### EN/PL переклади сторінок імпорту (Польща/Німеччина/Чехія): PR на злиття

- **sibway-website- PR #15** злито в `main` (commit `5c6193f`): опубліковано
  EN/PL переклади 3 import-сторінок (`en/pl/services/import-{poland,germany,
  czechia}.html`) — тексти перекладені із затвердженого uk-джерела
  `content/ua/ua_services-import-pl-de-cz.md`, попередньо показані власнику
  в окремому Claude Docs review і підтверджені ("підтверджую").
- Вкладене підменю "Import from X" та посилання у футері поширено на всі
  22 наявні en/pl сторінки (раніше патерн був лише на uk-сторінках).
- 3 uk import-сторінки: додано зворотні `hreflang="en"/"pl"` (раніше лише
  uk+x-default) і перенаправлено мовний перемикач EN/PL з `services.html`
  на конкретні import-сторінки.
- `sitemap.xml`: +6 нових EN/PL URL.
- `site_check.py` після змін: P0=0, P1=0, P2=0 (48 сторінок).

## 2026-09-23 (3)

### Публікація затверджених текстів: злиття PR

- **sibway-website- PR #14** злито в `main`: сторінки імпорту з Польщі,
  Німеччини, Чехії опубліковано з фінальними затвердженими текстами
  власника (тексти без згадки про приватні посилки — прибрано за
  рішенням власника), sitemap оновлено, TEMP-PREVIEW-мітки прибрано.
- **sibway-logistics-website PR #7** злито в `main`: затверджений
  контент `content/ua/ua_services-import-pl-de-cz.md` і скрипт
  `technical/tools/import-landing/render_import_pages.py`.
- Пост-мерж перевірка `site_check.py`: P0=0 у складі репозиторію
  (2 P0 з некомітнутих локальних файлів `en/pl/import-poland.html`,
  не входять у git).
- EN/PL версії сторінок імпорту — перенесено на окрему задачу.

## 2026-09-23 (2)

### Анімовані карти, меню, однакові hero (сайт: PR #13 злито; PR #14 — чернетка)

- **sibway-website- PR #13** (злито в `main`): карти-анімації в hero uk-сторінок
  (послуги, перевезення, митне, склад, аудит, про компанію, блог, контакти),
  однакова висота hero в групах сторінок, виправлення меню (передчасне
  відкриття випадаючого меню, компактна панель на планшеті/мобільному).
- **sibway-website- PR #14** (draft, не зливати): сторінки імпорту з Польщі,
  Німеччини, Чехії та пункти в меню — тексти на затвердженні власника.
- **technical/tools/route-map/** (новий): генератори карт і README.
- **docs/PATTERNS.md**: Крим у world-atlas, заборонені фрази й переноси,
  пастка з вкладеним меню, класи однакових hero, CSS-transform в SVG.

## 2026-09-23

### Рамка якості: рольові рев'ю, патерни, автоматична перевірка

- **docs/CLAUDE.md**: новий розділ «Рольові рев'ю перед запитом на коміт» —
  чеклісти ролей «Безпека», «Дані та аналітика», «Методолог»; у quality gate
  додано запуск `technical/tools/site_check.py`; у «Після роботи» — звіт про
  рольові рев'ю та поповнення `docs/PATTERNS.md`.
- **docs/PATTERNS.md** (новий): база канонічних рішень і пасток — канонічна
  форма, дворівневе меню, специфічність CSS, кеш CSS, локаль Google Sheets,
  git у Cowork, wildcard DNS, legacy `contact_form.php`, ефект reveal.
- **technical/tools/site_check.py** (новий) + README: статична перевірка
  сайту перед комітом (P0/P1/P2), код виходу 1 при P0. Перевірено:
  на `sibway-website-`@HEAD (= production) P0 = 0; на поточній локальній
  копії знаходить відомі P0 (TEMP-PREVIEW, `href="#"`, `import-poland`
  поза sitemap).

## 2026-09-22

### Preview-середовище видалено (T-001)

- Власник видалив піддомен `preview.sibway.com.ua` на Cityhost (разом
  із файлами) і його DNS-запис. Причина: після переходу на production
  preview був публічно відкритою копією сайту без Basic Auth і noindex —
  ризик дублікатів для SEO і зайва відкрита поверхня.
- Wildcard-запис `*.sibway.com.ua` свідомо залишено: адреса preview
  тепер показує лише заглушку Cityhost, без контенту Sibway.
- **docs/DEPLOYMENT.md** (§9): додано дату й фактичний стан після
  видалення.
- **docs/CLAUDE.md**: прибрано preview з розділу «Контекст»; розділ
  «Preview-only SFTP» замінено приміткою про скасування процедури.
- **docs/PROJECT_TODO.md**: рядок B6 (preview deploy + QA) позначено
  як застарілий.
- **docs/TASKS.md**: T-001 → DONE.

## 2026-09-10

### Blog MVP (D-012)

- Затверджено Blog MVP: UA-only hub і 3 статті, правила навігації,
  language switcher, canonical/hreflang, schema, OG image, content
  boundaries та source-content model (D-012). Це governance-фіксація
  й погоджений UA source-контент; runtime-реалізація (HTML, меню,
  sitemap) — окремий цикл B2–B5. Блог ще не реалізовано, не
  проіндексовано, не задеплоєно і не опубліковано.

### Documentation cleanup

- **docs/**: Moved six obsolete/duplicated documents to `docs/archive/`
  with an archive notice explaining the replacement: `AGENTS.md`,
  `PROJECT_OVERVIEW.md`, `SEO_DRAFT_UA.md`, `SITE_MAP_UA.md`,
  `HOMEPAGE_DRAFT_UA.md`, `TRANSPORT_PAGE_DRAFT_UA.md`.
- **docs/CLAUDE.md**: Added the project mission statement previously
  carried by the now-archived `PROJECT_OVERVIEW.md`.
- **docs/SEO_CONTENT_ROADMAP.md**: Removed the duplicated business-facts
  section (§4) that had drifted out of sync with `docs/PROJECT_FACTS.md`
  (missing the D-010 insurance/tracking confirmations); replaced with a
  pointer to the single source of truth. Updated `terms.html` and
  `contacts.html` status entries to reflect the published/implemented
  state (`a5be88f`, `749e4f3`, `d8b0d13`, `23aba1e`).
- **docs/SITE_STRUCTURE.md**: Removed the stale claim that
  `SESSION_HANDOFF.md` is "not yet implemented" (it exists and is in
  active use); refreshed the `docs/` file-purpose table and the
  source-of-truth priority table to include `CLAUDE.md`, `DEPLOYMENT.md`,
  `SESSION_HANDOFF.md`, the privacy source-of-truth documents and
  `docs/archive/`.
- **docs/PROJECT_FACTS.md**: Updated the owner-confirmation date to
  2026-09-09 to match the D-010 addition already present in the file.
- **docs/PROJECT_WORKFLOW.md**: Added a cross-reference to
  `docs/CLAUDE.md` for git-workflow details instead of duplicating them.

### Runtime and requirements sync (2026-09-08 – 2026-09-10)

- Release/deployment process defined: `docs/CLAUDE.md` extended,
  `docs/DEPLOYMENT.md` added (`1ba848a`); short root `DEPLOYMENT.md`
  added in the code repo (`4a3d152`).
- Localized `terms.html` legal text published in UA/EN/PL in the code
  repo (`a5be88f`); no source-of-truth document or `DECISIONS.md` entry
  exists for it yet (open item — see `docs/PROJECT_TODO.md`, P1-06).
- Service-aware contact form and CTA routing (`?service=`) implemented
  in the code repo (`23aba1e`); customs case-study wording synced
  between both repos (`23aba1e`, `25d51e2`).
- Vinnytsia–Warsaw transport case, full-value cargo insurance and
  real-time tracking confirmed by the owner and recorded as D-010
  (`5fe5d32`).
- Font-rendering artifact investigated and fixed; CTA styling unified
  between hero and cta-band buttons; recorded as D-011 (`d2a55b8`,
  `09861a4`). Mandatory Windows 11 / Chrome 128 post-deploy check still
  pending.
- Homepage quote-form textarea placeholder added in UA/EN/PL
  (`37c2bbf`).
- `docs/SESSION_HANDOFF.md` and `docs/PROJECT_TODO.md` synced with the
  above (`66dcdf8`, `14c954e`).

## 2026-09-04

### Documentation correction

- **docs/CHANGELOG.md**: Corrected the stale 2026-08-20 entry below claiming
  React + Vite + TypeScript as the approved project stack. The site
  (`Zsuff/sibway-website-`) is, and has been implemented as, static
  HTML/CSS/JS with no framework or build tooling — no `package.json`,
  `vite.config.*`, `tsconfig.*` or `node_modules` exist in the repository.
  `docs/RULES.md` no longer contains that approval; the current authoritative
  stack description lives in `docs/SITE_STRUCTURE.md` (rewritten
  2026-09-04). The original entry is left below unedited as a historical
  record, not as current guidance.

## 2026-08-25

### Content and localisation

- **content/ua/**: Ukrainian content moved to a dedicated language directory and renamed to the unified `ua_*.md` format.
- **content/en/**: Added the complete English content set using the `en_*.md` naming format.
- **content/pl/**: Added the complete Polish content set using the `pl_*.md` naming format.
- **content/**: Established the multilingual content convention: `content/{lang}/{lang}_{page}.md`.
- **content/**: Added 33 content files covering the Ukrainian, English and Polish versions of the site.

### Documentation

- **docs/CONTACTS_USAGE.md**: Added mandatory rules for the primary CTA telephone number and clickable Telegram, Viber and WhatsApp messenger icons.
- **docs/**: Updated project documentation to reflect multilingual content and the current implementation status.

### Repository maintenance

- **root / content/**: Removed unnecessary macOS `.DS_Store` files.
- **content/**: Removed obsolete `.gitkeep` files from directories that now contain content.
- **design/**: Removed obsolete `design/.gitkeep`.

## 2026-08-24

### Content

- **content/**: Added and expanded Ukrainian SEO/GEO content for the homepage, services, transport, customs clearance, warehousing, logistics audit, contacts, privacy policy and 404 page.
- **content/**: Added service-specific GEO blocks and AI-assistant links.
- **content/**: Updated company contact details and messenger links in Ukrainian source content.

## 2026-08-20

- **RULES.md**: Approved React + Vite + TypeScript as the primary project stack. It may be used without additional approval. Other frameworks and platforms (Next.js, Vue, Tailwind, CMS) require separate approval.

## 2026-08-19

- **brand**: Added design system for Stitch (`DESIGN.md`, `BRAND_COLORS.md`).
- **brand/fonts**: Added README with font usage guidelines.
- **brand/patterns**: Added Sibway pattern documentation.
- **brand/references**: Added visual references.

## 2026-08-14

- **docs/**: Restored original project-file content.
- **root**: Removed legacy documentation from the repository root and organised it in `docs/`.

## 2026-08-13

- **docs/**: Added content documentation files: `SITE_MAP_UA.md`, `SEO_DRAFT_UA.md`, `HOMEPAGE_DRAFT_UA.md` and `TRANSPORT_PAGE_DRAFT_UA.md`.
- **docs/**: Organised project documentation into dedicated directories.

## 2026-08-12

- **docs/**: Added the site map and SEO draft.

## 2026-08-10

- **docs/**: Marked GitHub setup as complete.

## 2026-08-07

- **docs/**: Initialised project memory in Ukrainian.
- **root**: Created `README.md`.
- Initial commit.
