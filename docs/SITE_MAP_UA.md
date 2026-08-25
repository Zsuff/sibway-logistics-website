# Карта сайту Sibway Logistics

## Призначення

Документ визначає сторінки, маршрути, мовні версії та джерела контенту для корпоративного сайту Sibway Logistics.

## Контентний контракт

Усі сторінки мають три мовні версії. Файли зберігаються за єдиною схемою:

```text
content/{lang}/{lang}_{page}.md
```

Доступні мови:

- `ua` — українська
- `en` — англійська
- `pl` — польська

Приклади:

```text
content/ua/ua_homepage.md
content/en/en_homepage.md
content/pl/pl_homepage.md
```

## Маршрути сайту

### Українська версія

| Сторінка | Маршрут | Контент | Статус дизайну |
|---|---|---|---|
| Головна | `/` | `content/ua/ua_homepage.md` | ✅ Затверджено |
| Послуги | `/services` | `content/ua/ua_services.md` | ✅ Затверджено |
| Міжнародні вантажні перевезення | `/services/transport` | `content/ua/ua_services-transport.md` | 📝 У роботі |
| Митне оформлення | `/services/customs` | `content/ua/ua_services-customs.md` | ⏳ Заплановано |
| Складські послуги | `/services/warehouse` | `content/ua/ua_services-warehouse.md` | ⏳ Заплановано |
| Логістичний аудит | `/services/audit` | `content/ua/ua_services-audit.md` | ⏳ Заплановано |
| Про компанію | `/about` | `content/ua/ua_about.md` | ⏳ Заплановано |
| Контакти | `/contacts` | `content/ua/ua_contacts.md` | ⏳ Заплановано |
| Політика конфіденційності | `/privacy` | `content/ua/ua_privacy.md` | ⏳ Заплановано |
| Умови використання | `/terms` | `content/ua/ua_terms.md` | ⏳ Заплановано |
| 404 | `/404` | `content/ua/ua_404.md` | ⏳ Заплановано |

### Англійська версія

| Сторінка | Маршрут | Контент |
|---|---|---|
| Home | `/en/` | `content/en/en_homepage.md` |
| Services | `/en/services` | `content/en/en_services.md` |
| International freight transport | `/en/services/transport` | `content/en/en_services-transport.md` |
| Customs clearance | `/en/services/customs` | `content/en/en_services-customs.md` |
| Warehousing services | `/en/services/warehouse` | `content/en/en_services-warehouse.md` |
| Logistics audit | `/en/services/audit` | `content/en/en_services-audit.md` |
| About | `/en/about` | `content/en/en_about.md` |
| Contact us | `/en/contacts` | `content/en/en_contacts.md` |
| Privacy policy | `/en/privacy` | `content/en/en_privacy.md` |
| Terms of use | `/en/terms` | `content/en/en_terms.md` |
| 404 | `/en/404` | `content/en/en_404.md` |

### Польська версія

| Сторінка | Маршрут | Контент |
|---|---|---|
| Strona główna | `/pl/` | `content/pl/pl_homepage.md` |
| Usługi | `/pl/services` | `content/pl/pl_services.md` |
| Transport towarowy | `/pl/services/transport` | `content/pl/pl_services-transport.md` |
| Odprawa celna | `/pl/services/customs` | `content/pl/pl_services-customs.md` |
| Usługi magazynowe | `/pl/services/warehouse` | `content/pl/pl_services-warehouse.md` |
| Audyt logistyczny | `/pl/services/audit` | `content/pl/pl_services-audit.md` |
| O firmie | `/pl/about` | `content/pl/pl_about.md` |
| Kontakt | `/pl/contacts` | `content/pl/pl_contacts.md` |
| Polityka prywatności | `/pl/privacy` | `content/pl/pl_privacy.md` |
| Warunki korzystania | `/pl/terms` | `content/pl/pl_terms.md` |
| 404 | `/pl/404` | `content/pl/pl_404.md` |

## Правила мовних URL

- Українська версія є версією за замовчуванням і використовує URL без мовного префікса.
- Англійська версія використовує префікс `/en/`.
- Польська версія використовує префікс `/pl/`.
- Перемикач мови має переводити користувача на відповідну сторінку іншою мовою, а не лише на головну.
- Якщо відповідного перекладу немає, перемикач має вести на головну цільової мови або показувати узгоджену fallback-сторінку.

## SEO для мультимовності

Для кожної індексованої сторінки необхідно:

- додати унікальні `title`, `meta description` та один `H1` мовою сторінки;
- встановити canonical URL на поточну мовну версію;
- додати взаємні `hreflang` для `uk`, `en`, `pl` і `x-default`;
- включити всі мовні URL до `sitemap.xml`;
- перевірити, що `robots.txt` не блокує важливі сторінки;
- зберігати логічні внутрішні посилання в межах відповідної мовної версії.

## Статуси дизайну

- ✅ Затверджено — дизайн і структура погоджені, сторінка може переходити у розробку.
- 📝 У роботі — макет або структура опрацьовуються.
- ⏳ Заплановано — сторінка включена в план, але макет ще не створено.

## Пов’язані документи

- Детальна структура блоків: `docs/SITE_STRUCTURE.md`
- SEO-чернетка українською: `docs/SEO_DRAFT_UA.md`
- Правила проекту: `docs/RULES.md`
- Використання контактів: `docs/CONTACTS_USAGE.md`
- План робіт: `docs/PROJECT_TODO.md`
