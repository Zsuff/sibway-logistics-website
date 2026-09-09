# Changelog

## 2026-09-10

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
