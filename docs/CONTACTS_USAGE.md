# Contact Channel Usage Rules

## Purpose

This document defines the mandatory rules for displaying and linking Sibway Logistics contact channels across all website languages and pages.

## Primary phone for calls and CTA

- **Visible number:** `+38 (063) 876-72-70`
- **Clickable link:** `tel:+380638767270`
- **Use in:** all CTA blocks, "Call" buttons, direct phone links and contact sections.
- **Rule:** this is the only number that may be displayed as a telephone number on the website.

### Canonical call button

```md
[Call us](tel:+380638767270)
```

Use language-appropriate button text, for example: `Зателефонувати`, `Call us`, `Zadzwoń`.

## Messenger-only number

- **Number used in URLs only:** `+380687583263`
- **Do not display:** the number must never be shown as visible text on the website.
- **Use only for:** Telegram, Viber and WhatsApp buttons or small clickable icons.

### Canonical Markdown messenger block

```md
- [![Telegram](https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg)](https://t.me/+380687583263){:target="_blank" rel="noopener" aria-label="Telegram"}
- [![Viber](https://upload.wikimedia.org/wikipedia/commons/9/99/Viber_logo_2019.svg)](viber://chat?number=%2B380687583263){:target="_blank" rel="noopener" aria-label="Viber"}
- [![WhatsApp](https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg)](https://wa.me/380687583263){:target="_blank" rel="noopener" aria-label="WhatsApp"}
```

### Implementation requirements

- Render the messenger links as compact icons, not as visible phone numbers.
- Preserve an accessible `aria-label` for each icon.
- Open external messenger links in a new tab with `target="_blank"` and `rel="noopener"`.
- Use the same destination links in Ukrainian, English and Polish versions.

## Rules by content area

| Content element | Required contact channel | Implementation |
|---|---|---|
| CTA button: call | Primary phone | `tel:+380638767270` |
| CTA button: messenger | Messenger-only number | Telegram, Viber or WhatsApp icon URL |
| Contact page phone | Primary phone | Show `+38 (063) 876-72-70` and link it |
| Contact page messengers | Messenger-only number | Show only clickable icons |
| 404 page help block | Primary phone and/or messenger icons | Never show the messenger-only number |
| Privacy or legal contacts | Primary phone | Show `+38 (063) 876-72-70` where a telephone number is required |

## Pre-publication checklist

- [ ] Every call CTA uses `tel:+380638767270`.
- [ ] The displayed telephone number is `+38 (063) 876-72-70`.
- [ ] Telegram uses `https://t.me/+380687583263`.
- [ ] Viber uses `viber://chat?number=%2B380687583263`.
- [ ] WhatsApp uses `https://wa.me/380687583263`.
- [ ] The messenger-only number is not visible as text on any page.
- [ ] Messenger controls render as clickable icons with accessible labels.
- [ ] Rules are applied consistently in `content/ua/`, `content/en/` and `content/pl/`.
