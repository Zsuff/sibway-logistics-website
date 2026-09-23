# technical/tools

Допоміжні інструменти перевірки. Живуть у репозиторії вимог, бо
`sibway-website-` — лише runtime-код сайту (див. `docs/CLAUDE.md`, «Ролі
репозиторіїв»).

## site_check.py

Статична перевірка локальної копії сайту перед запитом на коміт.
Входить в обов'язковий quality gate (`docs/CLAUDE.md`).

```bash
python3 technical/tools/site_check.py ../sibway-website-
python3 technical/tools/site_check.py ../sibway-website- --json   # машинний формат
```

Лише читає файли; мережу не використовує; нічого не змінює.
Потрібен лише Python 3 (без зовнішніх бібліотек).

Перевіряє всі `*.html` (крім `content-drafts/`):

| Рівень | Що |
|---|---|
| P0 | биті внутрішні посилання, відсутні CSS/JS/зображення, `href="#"`, маркери `TEMP-PREVIEW` / `localhost` / `preview.sibway` / тестові домени, canonical чи hreflang не на `https://sibway.com.ua`, невалідний JSON-LD, індексована сторінка поза `sitemap.xml`, URL у sitemap без файлу |
| P1 | немає title/description/canonical/lang, H1 ≠ 1, canonical ≠ URL файлу, hreflang не взаємний або на неіснуючий файл, img без alt, дублікати id, однакові title/description, noindex у sitemap |
| P2 | title > 65, description > 160 або < 70, немає OG-тегів, img без width/height, `target=_blank` без `noopener`, неіснуючі якорі |
| INFO | сторінки без відповідника в іншій мові (напр. UA-only блог — погоджений виняток D-012) |

Код виходу `1`, якщо є хоча б одне P0 — тоді коміт не просити, спершу
виправити.

Не замінює: візуальну перевірку 375 / 768 / desktop, консоль і мережу в
браузері, перевірку доступності (контраст тощо), ручну перевірку форм.
