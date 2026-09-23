#!/usr/bin/env python3
"""Переносить затверджений текст посадкових сторінок імпорту (content/ua/ua_services-import-pl-de-cz.md)
у HTML-сторінки uk/services/import-{poland,germany,czechia}.html сайту, зберігаючи hero-карту, форму й класи.
Запуск: python3 render_import_pages.py <шлях до md> <корінь сайту>"""
import re, sys, html

MD, SITE = sys.argv[1], sys.argv[2]
KEYS = {'Імпорт із Польщі': 'poland', 'Імпорт із Німеччини': 'germany', 'Імпорт із Чехії': 'czechia'}
esc = lambda t: html.escape(t, quote=False)

def parse(md):
    pages = {}
    for block in re.split(r'\n(?=# \d+\. )', md)[1:]:
        name = re.match(r'# \d+\. (.+)', block).group(1).strip()
        key = KEYS[name]
        title = re.search(r'## Meta title\s*```text\n(.*?)\n```', block, re.S).group(1).strip()
        desc = re.search(r'## Meta description\s*```text\n(.*?)\n```', block, re.S).group(1).strip()
        body = block.split('## H1', 1)[1]
        h1 = re.search(r'^# (.+)$', body, re.M).group(1).strip()
        after_h1 = body.split('# ' + h1, 1)[1]
        hero_part, rest = after_h1.split('\n## ', 1)
        lead = [p.strip() for p in hero_part.strip().split('\n\n') if p.strip() and not p.strip().startswith('[')]
        sections = []
        for sec in ('## ' + rest).split('\n## '):
            sec = sec.lstrip('# ').strip()
            if not sec or sec.startswith('---'):
                continue
            head, _, txt = sec.partition('\n')
            txt = txt.split('\n---')[0]
            sections.append((head.strip(), blocks(txt)))
        pages[key] = dict(title=title, desc=desc, h1=h1, lead=lead, sections=sections)
    return pages

def blocks(txt):
    out = []
    for chunk in re.split(r'\n\s*\n', txt.strip()):
        c = chunk.strip()
        if not c:
            continue
        if c.startswith('### '):
            out.append(('h3', c[4:].strip()))
        elif c.startswith('- '):
            out.append(('ul', [l[2:].strip() for l in c.splitlines() if l.startswith('- ')]))
        elif c.startswith('[Кнопка:'):
            out.append(('btn', c.strip('[]').split(':', 1)[1].strip()))
        elif c.startswith('[Форма'):
            out.append(('form', ''))
        else:
            out.append(('p', ' '.join(c.split())))
    return out

P = lambda t, cls='': f'<p{" class=" + chr(34) + cls + chr(34) if cls else ""}>{esc(t)}</p>'
UL = lambda items, cls: f'<ul class="{cls}">' + ''.join(f'<li>{esc(i)}</li>' for i in items) + '</ul>'

def split_list(bl):
    """(p до списку, список, p після списку, інше)"""
    before, lst, after = [], None, []
    for k, v in bl:
        if k == 'ul' and lst is None:
            lst = v
        elif k == 'p':
            (before if lst is None else after).append(v)
    return before, lst, after

def sec_audience(h, bl):
    before, lst, after = split_list(bl)
    s = f'<section class="section section--tint"><div class="container"><div class="section-head section-head--left"><h2>{esc(h)}</h2>' + ''.join(P(p) for p in before) + '</div>'
    s += UL(lst, 'ticks ticks--2')
    if after:
        s += '<div class="section-head section-head--left section-head--after">' + ''.join(P(p) for p in after) + '</div>'
    return s + '</div></section>'

def sec_cards(h, bl):
    cards, cur = [], None
    for k, v in bl:
        if k == 'h3':
            cur = [v, []]; cards.append(cur)
        elif k == 'p' and cur:
            cur[1].append(v)
    grid = 'grid--2' if len(cards) % 2 == 0 else 'grid--3'
    s = f'<section class="section"><div class="container"><div class="section-head"><h2>{esc(h)}</h2></div><div class="grid {grid}">'
    for t, ps in cards:
        s += f'<article class="card reveal prose"><h3>{esc(t)}</h3>' + ''.join(P(p) for p in ps) + '</article>'
    return s + '</div></div></section>'

def sec_steps(h, bl):
    steps, cur = [], None
    for k, v in bl:
        if k == 'h3':
            cur = [v, []]; steps.append(cur)
        elif k == 'p' and cur:
            cur[1].append(v)
    s = f'<section class="section section--alt"><div class="container"><div class="section-head"><h2>{esc(h)}</h2></div><ol class="steps">'
    for t, ps in steps:
        s += f'<li class="reveal"><h3>{esc(t)}</h3>' + ''.join(P(p) for p in ps) + '</li>'
    return s + '</ol></div></section>'

def sec_terms(h, bl):
    before, lst, after = split_list(bl)
    s = f'<section class="section section--tint"><div class="container"><div class="section-head section-head--left"><h2>{esc(h)}</h2>' + ''.join(P(p) for p in before) + '</div>'
    s += UL(lst, 'plain-list')
    if after:
        s += '<div class="section-head section-head--left section-head--after">' + ''.join(P(p) for p in after) + '</div>'
    return s + '</div></section>'

def sec_price(h, bl):
    before, lst, after = split_list(bl)
    s = f'<section class="section section--tight"><div class="container"><div class="section-head section-head--left"><h2>{esc(h)}</h2>' + ''.join(P(p) for p in before) + '</div>' + UL(lst, 'plain-list') + '</div></section>'
    ps = ''.join(f'<p><strong>{esc(p)}</strong></p>' if p.startswith('Надішліть') else P(p) for p in after)
    btn = next((v for k, v in bl if k == 'btn'), 'Отримати прорахунок')
    return s + f'\n\n<section class="section section--alt"><div class="container"><div class="section-head">{ps}</div><div class="btn-row"><a class="btn btn--primary" href="#quote-form">{esc(btn)}</a></div></div></section>'

def sec_customs(h, bl):
    ps = [v for k, v in bl if k == 'p']
    btn = next((v for k, v in bl if k == 'btn'), 'Детальніше про митний супровід')
    return (f'<section class="section section--tint"><div class="container"><div class="section-head section-head--left"><h2>{esc(h)}</h2>'
            + ''.join(P(p) for p in ps) + f'</div><div class="btn-row"><a class="btn btn--secondary" href="../../uk/services/customs.html">{esc(btn)}</a></div></div></section>')

def sec_faq(h, bl):
    qa, cur = [], None
    for k, v in bl:
        if k == 'h3':
            cur = [v, []]; qa.append(cur)
        elif k == 'p' and cur:
            cur[1].append(v)
    s = f'<section class="section"><div class="container"><div class="section-head"><h2>{esc(h)}</h2></div><div class="faq">'
    for q, ps in qa:
        s += f'<details><summary>{esc(q)}</summary>' + ''.join(P(p) for p in ps) + '</details>'
    return s + '</div></div></section>'

def render(page):
    parts, form = [], None
    for h, bl in page['sections']:
        if h.startswith('Для кого'): parts.append(sec_audience(h, bl))
        elif h.startswith('Які вантажі'): parts.append(sec_cards(h, bl))
        elif h.startswith('Як працює'): parts.append(sec_steps(h, bl))
        elif h.startswith('Орієнтовні строки'): parts.append(sec_terms(h, bl))
        elif h.startswith('Що впливає'): parts.append(sec_price(h, bl))
        elif h.startswith('Митний супровід'): parts.append(sec_customs(h, bl))
        elif h.startswith('Часті запитання'): parts.append(sec_faq(h, bl))
        elif h.startswith('Залиште заявку'): form = (h, [v for k, v in bl if k == 'p'])
        else: raise SystemExit('невідомий розділ: ' + h)
    return '\n\n'.join(parts), form

def apply(key, page):
    f = f'{SITE}/uk/services/import-{key}.html'
    s = open(f, encoding='utf-8').read()
    head, body = s.split('</head>', 1)
    old_title = re.search(r'<title>(.*?)</title>', head).group(1)
    old_desc = re.search(r'<meta name="description" content="([^"]*)"', head).group(1)
    head = head.replace(old_title, esc(page['title'])).replace(old_desc, html.escape(page['desc']))
    # hero: заголовок і лід
    lead = f'<p class="hero__lead">{esc(page["lead"][0])}</p>' + ''.join(P(p) for p in page['lead'][1:])
    body, n = re.subn(r'<h1>.*?</h1>(?:<p class="hero__lead">.*?</p>)(?:<p>.*?</p>)*(?=<div class="btn-row">)',
                      lambda m: f'<h1>{esc(page["h1"])}</h1>' + lead, body, count=1, flags=re.S)
    assert n == 1, 'hero ' + key
    sections, form = render(page)
    i = body.index('</section>', body.index('<section class="hero')) + len('</section>')
    j = body.index('<section class="section section--alt" id="quote-form">')
    body = body[:i] + '\n\n' + sections + '\n\n' + body[j:]
    fh, fps = form
    body, n = re.subn(r'(<section class="section section--alt" id="quote-form"><div class="container"><div class="section-head">)<h2>.*?</h2>(?:<p>.*?</p>)+',
                      lambda m: m.group(1) + f'<h2>{esc(fh)}</h2>' + ''.join(P(p) for p in fps), body, count=1, flags=re.S)
    assert n == 1, 'form ' + key
    open(f, 'w', encoding='utf-8').write(head + '</head>' + body)
    return f

pages = parse(open(MD, encoding='utf-8').read())
for k, p in pages.items():
    print('ok', apply(k, p), len(p['sections']), 'розділів')
