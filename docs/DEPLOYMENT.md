# Deployment guide

Цей документ описує release/deployment-процес проєкту Sibway Logistics:
відтворюваний шлях від локальної зміни до продакшн-сайту. Він не повторює
`docs/PROJECT_WORKFLOW.md` (цикл однієї задачі, branch/PR) — фокус тут на
тому, що відбувається після merge: release package, production,
rollback і secrets policy.

## 1. Призначення

Зафіксувати відтворюваний, безпечний і керований release-процес:

```text
Local → GitHub → Production
```

Мета — не допустити розходження Git-коду і хостингу, випадкових
production-змін, витоку доступів або суперечливих інструкцій.

## 2. Ролі репозиторіїв

- **Requirements repo** (`Zsuff/sibway-logistics-website`) — правила,
  рішення, документація, контент, QA і release log. Єдине нормативне
  джерело для Claude Code (`docs/CLAUDE.md`).
- **Code repo** (`Zsuff/sibway-website-`) — runtime-код статичного сайту
  і deployable commit SHA. Не містить вимог, секретів, release-архівів
  чи бізнесової документації.

## 3. Джерело правди

- Вимоги, рішення і контент-стандарти — виключно requirements repo.
- Runtime-release — точний approved commit SHA у code repo, а не стан
  робочої директорії чи будь-який uncommitted код.
- Хостинг (production) не є середовищем розробки.
- Ручні зміни HTML/CSS/JS/assets безпосередньо на хостингу не
  виконуються — усі зміни йдуть через Git.
- Uncommitted код ніколи не деплоїться.

## 4. Середовища

| Environment | URL | Purpose | Rules |
|---|---|---|---|
| Local | — (локальна машина розробника) | Розробка та локальна валідація | Без публічного доступу; тут виконується вся розробка й перевірка перед комітом |
| GitHub | `https://github.com/Zsuff/sibway-website-` | Контроль версій, source of truth для деплойного SHA, Pull Request і код-рев'ю | Push/merge лише за погодженим Git-workflow (`docs/CLAUDE.md`) |
| Production | `https://sibway.com.ua` | Публічний сайт | Публікація — через SFTP (FileZilla) на вже автентифікованій сесії власника, після затвердження й merge у `main`; виконує власник особисто або, за окремим явним дозволом на кожен конкретний деплой, Claude Code через computer-use на цій же вже підключеній сесії (розділ 10); жодних ручних правок поза Git-релізом |

Приватні server paths, host, порти чи облікові дані в цій таблиці не
вказуються.

> `preview.sibway.com.ua` видалено власником і більше не існує — це
> середовище більше не використовується як окреме staging чи QA-етап
> (див. розділ 9).

## 5. Approval gates

Власник окремо погоджує кожен з цих етапів; підтвердження одного етапу
**не поширюється** на інші:

1. реалізацію (зміст і обсяг змін);
2. commit/push, включно з merge у `main` через PR;
3. production deployment (ручний SFTP-деплой власника);
4. cleanup, backup або rollback, якщо це окрема операція.

## 6. Стандартний lifecycle

1. Формулюється задача/вимога.
2. Аналіз вимог у requirements repo (`docs/`, `content/`, `brand/`,
   `design/approved/`, `technical/`).
3. Локальні зміни виконуються лише в code repo.
4. Локальна валідація на MacBook власника (розділ 7): локальний
   сервер, перевірка форм, скриптів і верстки перед комітом.
5. Review і приймання власником.
6. Окремий дозвіл на commit/push (стандартно — branch → PR →
   код-рев'ю → merge у `main`; пряме комітування в `main` лише як
   письмово погоджений виняток, деталі — `docs/CLAUDE.md`).
7. Фіксується GitHub commit SHA (стан `main` після merge).
8. Окремий дозвіл на production deploy.
9. SFTP-деплой того самого SHA на продакшн через FileZilla, на вже
   автентифікованій сесії власника — виконує власник особисто або,
   за окремим дозволом на цей конкретний деплой, Claude Code через
   computer-use (розділ 10).
10. Production post-deploy smoke-check; rollback за потреби
    (розділ 11).

## 7. Локальна валідація

Перед запитом на commit:

```bash
git diff --check
git diff --stat
git status --short
```

QA-рівні та перевірки за релевантністю:

- mobile 375 px, tablet 768 px, desktop;
- keyboard accessibility;
- Console / Network без нових critical errors або asset-404;
- UA / EN / PL parity;
- SEO-перевірка, якщо зачіпаються SEO-файли чи `<head>`
  (`title`, `canonical`, `hreflang`, `meta description`, Open Graph,
  `robots.txt`, `sitemap.xml`);
- critical paths, внутрішні посилання та assets;
- CTA, контакти, trust signals, consent.

Formspree submit і live-перевірка GA4-подій виконуються лише за окремим
дозволом власника — за замовчуванням форми перевіряються без реального
надсилання.

## 8. Release package

- Формується точно з approved commit SHA (не з робочої директорії).
- Містить лише runtime web-файли сайту.
- Виключає: службові файли Git (`.git/`), файли IDE, системну
  документацію, secrets, архіви попередніх релізів.
- Перед використанням перевіряється manifest (перелік і, за потреби,
  контрольні суми файлів).
- Після затвердження на production і окремого рішення на cleanup —
  package/ZIP не лишається у web-root хостингу.

## 9. Preview (видалено)

`preview.sibway.com.ua` видалено власником і більше не існує — воно
більше не використовується як окреме staging-середовище чи проміжний
QA-етап. Раніше цей розділ описував preview-only SFTP і Basic Auth на
цьому піддомені; ця процедура застаріла й тут навмисно не деталізується.

Post-deploy перевірка тепер виконується напряму на production
(розділ 10) одразу після SFTP-деплою — окремого staging-кроку між
merge у `main` і production більше немає.

## 10. Production deployment

- Деплоїться лише той самий commit SHA, що пройшов review і merge у
  `main` — ніякий інший SHA чи uncommitted стан.
- Публікація — через SFTP (FileZilla), на вже автентифікованій
  сесії власника. Виконує або власник особисто, або Claude Code через
  computer-use (керування вже підключеною FileZilla-сесією на екрані
  власника) — **лише за окремим явним дозволом власника на кожен
  конкретний деплой**, з точним переліком файлів.
- Незалежно від того, хто саме натискає "Upload" у FileZilla: hosting
  credentials (host, порт, логін, пароль) Claude Code не отримує,
  не бачить і не зберігає — лише керує вже автентифікованою сесією,
  яку відкрив власник (розділ 12).
- Перед змінами виконується backup production і перевіряється його
  успішність.
- Перевіряється відповідність цільового server target.
- Після деплою — production post-deploy smoke-check.
- Production не використовується як майданчик для hotfix-правок
  повз Git-процес.

## 11. Rollback

- Виконується лише за окремим дозволом власника.
- Повертає середовище до останнього verified release або backup.
- Для кожного rollback фіксується: дата, commit SHA (до і після),
  причина (reason), обсяг (scope) і результат.

## 12. Secrets і доступи

- Host, порти, username, паролі, токени, SSH-ключі, приватні remote
  paths, backups або IP allowlist **не зберігаються і не виводяться**
  у Git, документації, конфігураціях, логах чи звітах.
- Облікові дані зберігаються лише в безпечному локальному password
  manager / Keychain власника.
- Доступи мають діяти за принципом найменших привілеїв (least
  privilege); preview і production профілі ізольовані один від
  одного.

## 13. Release log

```md
| Date | Environment | Commit SHA | Scope | QA result | Owner approval | Notes |
|---|---|---|---|---|---|---|
```

Release log фіксує факт і результат релізу для трасованості. Приватні
дані та secrets (host, credentials, шляхи, ключі) у цей журнал не
потрапляють — лише дата, середовище, SHA, обсяг змін, результат QA,
підтвердження власника та нейтральні нотатки.
