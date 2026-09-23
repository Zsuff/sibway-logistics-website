# route-map — генератори анімованих карт Sibway

SVG-карти й ілюстрації для першого екрана (hero) сторінок сайту, у кольорах
Sibway. Затверджений стиль (2026-09-23): уся Європа одним силуетом без
внутрішніх кордонів, розмиті краї, Україна (з Кримом) виділена, плавні дуги,
«пульсація» з міст, повільна сідельна фура (тягач + напівпричіп).

```bash
curl -sLO https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/countries-50m.json
python3 mkmap.py        # проєкція, спрощення, Крим → Україна (спільна основа)
python3 mkeurope.py     # routes-europe.svg, route-{poland,germany,czechia}-ukraine.svg
python3 mkmapanim.py    # map-customs.svg, map-warehouse.svg, map-audit.svg
python3 mkservices.py   # map-services.svg («Наші послуги»: аудит → перевезення → склад → митниця)
python3 mkwide.py       # map-about.svg, map-blog.svg, map-contacts.svg (широкі, невисокі)
python3 mkillus.py      # illus-hub.svg (головна) та ранні ілюстрації
```

| Файл | Призначення |
|---|---|
| `semi.py` | Фура: тягач + напівпричіп (спільна для всіх карт) |
| `mkmap.py` | Проєкція Lambert (центр 22E 51N), Douglas–Peucker, перенесення Криму |
| `mkeurope.py` | Карта «вся Європа → Україна» і карти країн (виділена країна) |
| `mkmapanim.py` | Митниця, склад, аудит; спільні `page()`, `pulses()`, `qcurve()` |
| `mkservices.py` | Сторінка «Наші послуги» |
| `mkwide.py` | Широкі карти для компактних hero (про компанію, блог, контакти) |
| `mkillus.py` | Ілюстрація-хаб на головній; ранні ілюстрації (не використовуються) |
| `mkroutes.py`, `mksvg.py` | Ранні варіанти (лише потрібні країни / мережа напрямків) — відхилені, для історії |

- Дані кордонів: Natural Earth (public domain) через `world-atlas` (ISC).
- **Крим:** у `world-atlas` Крим віднесено до Росії (643); `mkmap.py`
  переносить полігон до України (804). Не прибирати.
- Нова країна: ISO 3166 numeric id у `HL` і новий рядок унизу `mkeurope.py`
  (міста — лише ті, що підтверджені на сайті).
- Усі анімації вимикаються при `prefers-reduced-motion` (показується статична фура).
- Підписи на картах українською; для EN/PL потрібні окремі SVG.
