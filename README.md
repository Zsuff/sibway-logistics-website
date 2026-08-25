# Sibway Logistics Website

Репозиторій для розробки сайту логістичної компанії Sibway Logistics.

## Структура проекту

```
sibway-logistics-website/
├── README.md              # Цей файл — опис проекту
├── docs/                  # Документація та контент сайту
│   ├── SITE_MAP_UA.md           # Карта сайту
│   ├── SEO_DRAFT_UA.md          # SEO-основа
│   ├── HOMEPAGE_DRAFT_UA.md     # Чернетка головної сторінки
│   ├── TRANSPORT_PAGE_DRAFT_UA.md  # Чернетка сторінки послуги
│   ├── RULES.md                 # Правила проекту
│   ├── AGENTS.md                # Інструкції для агентів
│   ├── PROJECT_OVERVIEW.md      # Огляд проекту
│   ├── PROJECT_TODO.md          # Список задач
│   └── CHANGELOG.md             # Історія змін
├── design/                # Майбутні файли дизайну (макети, натхнення)
├── content/               # Майбутні готові тексти для сайту
└── technical/             # Майбутні технічні документи
```

## Як користуватися

- **docs/** — вся документація, чернетки контенту, SEO, карта сайту
- **design/** — сюди будуть додаватися макети, візуальні матеріали
- **content/** — готові тексти для публікації
- **technical/** — технічні специфікації, інструкції для розробки

## Посилання

- [Карта сайту](docs/SITE_MAP_UA.md)
- [Головна сторінка (чернетка)](docs/HOMEPAGE_DRAFT_UA.md)
- [Сторінка послуги (чернетка)](docs/TRANSPORT_PAGE_DRAFT_UA.md)

React + TypeScript + Vite
This template provides a minimal setup to get React working in Vite with HMR and some Oxlint rules.

Currently, two official plugins are available:

@vitejs/plugin-react uses Oxc
@vitejs/plugin-react-swc uses SWC
React Compiler
The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see this documentation.

Expanding the Oxlint configuration
If you are developing a production application, we recommend enabling type-aware lint rules by installing oxlint-tsgolint and editing .oxlintrc.json:

{
  "$schema": "./node_modules/oxlint/configuration_schema.json",
  "plugins": ["react", "typescript", "oxc"],
  "options": {
    "typeAware": true
  },
  "rules": {
    "react/rules-of-hooks": "error",
    "react/only-export-components": ["warn", { "allowConstantExport": true }]
  }
}
See the Oxlint rules documentation for the full list of rules and categories.

# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some Oxlint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the Oxlint configuration

If you are developing a production application, we recommend enabling type-aware lint rules by installing `oxlint-tsgolint` and editing `.oxlintrc.json`:

```json
{
  "$schema": "./node_modules/oxlint/configuration_schema.json",
  "plugins": ["react", "typescript", "oxc"],
  "options": {
    "typeAware": true
  },
  "rules": {
    "react/rules-of-hooks": "error",
    "react/only-export-components": ["warn", { "allowConstantExport": true }]
  }
}
```

See the [Oxlint rules documentation](https://oxc.rs/docs/guide/usage/linter/rules) for the full list of rules and categories.
