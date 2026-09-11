# Блог

Source-of-truth для хабу блогу (`/uk/blog.html`). UA-only v1 за D-012.
Не використовувати YAML frontmatter — конвенція `content/ua/`.

## SEO

**URL:** /uk/blog.html

**Meta title:** Блог про міжнародну логістику для бізнесу | Sibway Logistics

**Meta description:** Практичні матеріали для бізнесу про міжнародні вантажні перевезення між Україною та Європою: підготовку запитів, документи та фактори вартості.

## Hero

**Breadcrumbs:** Головна → Блог

**H1:** Блог про міжнародну логістику для бізнесу

**Lead:** Практичні пояснення для бізнесу, який організовує перевезення між Україною та країнами Європи.

## Article cards

### Картка 1

- **URL:** /uk/blog/yak-pidgotuvaty-zapyt-na-mizhnarodne-perevezennia.html
- **Title:** Як підготувати запит на міжнародне перевезення
- **Dek:** Які дані про маршрут, вантаж і дату готовності варто зібрати перед запитом, щоб предметніше обговорити можливі варіанти перевезення.
- **CTA label:** Читати статтю

### Картка 2

- **URL:** /uk/blog/dokumenty-dlia-mizhnarodnoho-perevezennia.html
- **Title:** Документи для міжнародного перевезення
- **Dek:** Які вихідні дані та документи часто обговорюють під час підготовки перевезення і чому точний перелік залежить від конкретного сценарію.
- **CTA label:** Читати статтю

### Картка 3

- **URL:** /uk/blog/shcho-vplyvaie-na-vartist-mizhnarodnoho-perevezennia.html
- **Title:** Від чого залежить вартість міжнародного перевезення
- **Dek:** Які параметри маршруту, вантажу та організації перевезення впливають на індивідуальний розрахунок.
- **CTA label:** Читати статтю

## CTA

**Primary CTA:** Отримати розрахунок → /uk/contacts.html?service=transport

**Secondary CTA:** Зателефонувати → tel:+380638767270

## SEO / technical notes

**Canonical:** https://sibway.com.ua/uk/blog.html

**Hreflang:** Не додавати у v1 — UA-only за D-012.

**OG image:** https://sibway.com.ua/og-image.png

**OG type:** website

**Schema:** BreadcrumbList (Головна → Блог). BlogPosting до hub не застосовується.

**Visible byline/date:** Показується на хабі — на кожній картці статті першим елементом відображається `Команда Sibway Logistics · Оновлено: DD.MM.YYYY` (автор і дата останнього оновлення відповідної статті).

**Implementation notes:**
- Хаб — 1 рівень вкладеності (`uk/blog.html`), відносні шляхи з префіксом `../` (як `uk/services.html`).
- Повторно використати наявні класи: `hero hero--compact`, `breadcrumbs`, `container`, `section`, `card`, `link-more`, `cta-band`, `btn`. Картки обгорнуті в `<div class="prose"><div class="grid">` (editorial-list layout; клас `grid--3` не використовується).
- Header/footer/cookie-notice/GA4 — ідентичні решті UA-сторінок; у навігації хабу пункт «Блог» позначити `aria-current="page"`.
- Три картки статей: `card` без `card__icon`; першим елементом картки — `<p class="updated">` з байлайном і датою; далі `<h3>` = title, `<p>` = dek, `link-more` з текстом «Читати статтю».
- Картку статті додавати в хаб лише коли відповідний runtime-файл існує (B3 — стаття №1; B4 — статті №2–3).
