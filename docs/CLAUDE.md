# Інструкція для Claude Code

## Мета проєкту

Створити новий багатомовний B2B-сайт Sibway Logistics для міжнародних
вантажних перевезень, митного супроводу, складських послуг і
логістичного аудиту.

## Контекст

- Код сайту: https://github.com/Zsuff/sibway-website-
- Репозиторій вимог: https://github.com/Zsuff/sibway-logistics-website
- Фінальний домен: https://sibway.com.ua
- Preview: https://preview.sibway.com.ua (захищений Basic Auth, середовище staging QA)
- Мови: `/uk/`, `/en/`, `/pl/`.
- Розробка виконується через Claude Code у застосунку на Mac.
- Antigravity більше не використовується.

## Ролі репозиторіїв

- `sibway-logistics-website` — єдине нормативне джерело вимог, затверджених рішень, контенту, дизайну, правил, QA і release policy.
- `sibway-website-` — runtime source code статичного сайту; не місце зберігання вимог, секретів, релізних архівів чи бізнесової документації.
- Повні policy-інструкції не дублюються в code-репозиторії — там лишається лише короткий операційний `DEPLOYMENT.md`.
- Для кожної зміни Claude Code спочатку звіряє вимоги з цим репозиторієм, а реалізацію виконує в code-репозиторії.

## Перед роботою

1. Прочитай цей файл і `docs/RULES.md` — правила проєкту зберігаються лише тут, у репозиторії вимог.
2. Визнач відповідні документи: бренд — `brand/`, контент — `content/`, макети — `design/approved/`, правила — `docs/`, технічні обмеження — `technical/`.
3. Сформуй план без змін: мета, файли, ризики, перевірки.
4. Дочекайся підтвердження власника.

## Під час роботи

- Виконуй лише погоджений обсяг.
- Не вигадуй юридичні положення, контакти, строки, ціни або результати кейсів.
- Зберігай синхронну структуру сторінок у трьох мовах.
- Для SEO використовуй тільки `https://sibway.com.ua`.
- Не використовуй тестові домени у canonical, hreflang, sitemap або Open Graph.
- Не змінюй DNS, хостинг, інтеграції, форми, аналітику чи секрети без окремої команди.

## Git-workflow: branch → review/PR → merge

За замовчуванням Claude Code дотримується чинного workflow із `docs/RULES.md` та `docs/PROJECT_WORKFLOW.md`:

```text
branch → review / Pull Request → merge власником
```

Це означає: окрема гілка на задачу, коміт і push лише в цю гілку, Pull Request до `main`, перегляд і merge виконує власник.

**Прямий commit і push у `main` не є звичайним workflow.** Він можливий лише як виняток — за окремим явним письмовим дозволом власника, у якому зазначені:

- конкретний репозиторій;
- цільова гілка `main`;
- точний scope файлів або зміни;
- commit message;
- дозвіл на push саме у `origin/main`.

Без усіх цих елементів прямий commit/push у `main` не виконується — застосовується стандартний branch → PR → merge.

## Approval gates

Без прямого, окремого дозволу власника заборонено:

- `git add`, commit, push, PR, merge, rebase, reset, amend, force push;
- створювати release package або archive;
- upload, deploy, overwrite, create, delete, move, sync, mirror, cleanup, backup або rollback на будь-якому хостингу;
- SFTP/FTP/SSH, File Manager, CityHost;
- production access, читання чи зміни;
- DNS, SSL, Basic Auth, server rules;
- надсилати форми або створювати реальні GA4 events;
- змінювати інтеграції або зберігати/виводити secrets.

## Preview-only SFTP

- Preview SFTP може використовуватися виключно в межах preview (`https://preview.sibway.com.ua`).
- Спершу виконується read-only preflight.
- Remote write-операція можлива лише після окремого дозволу, який містить точний environment, commit SHA, перелік файлів і тип дії.
- Не застосовується automatic deploy, mirror, `delete extraneous files`, `replace all` або масові операції без окремо погодженого плану.
- Host, port, username, passwords, keys, private paths та інші credentials не передаються і не записуються — ні в код, ні в документацію, ні в звіти.

## Обов'язковий quality gate

До запиту на commit:

```bash
git diff --check
git diff --stat
git status --short
```

Додатково за релевантністю:

- UA / EN / PL parity;
- critical paths, internal links і assets;
- mobile 375 px, tablet 768 px, desktop;
- keyboard accessibility;
- Console / Network без нових critical errors або asset-404;
- SEO check, якщо зачіпаються SEO-файли чи `<head>`;
- CTA, contacts, trust signals і consent;
- форми без submit, якщо не погоджено тестову відправку;
- не погіршувати performance, CLS, Core Web Vitals і доступність.

## Після роботи

1. Покажи список змінених файлів.
2. Покажи diff або точний опис змін.
3. Опиши перевірки та невирішені ризики.
4. Не створюй коміт, push або pull request без явного підтвердження.
