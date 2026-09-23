#!/usr/bin/env python3
"""Статична перевірка сайту Sibway перед запитом на коміт.

Використання:
    python3 technical/tools/site_check.py <шлях до sibway-website-> [--json]

Лише читає локальні файли: нічого не змінює, мережу не використовує.
Код виходу: 1 — є P0 (коміт не просити), 0 — P0 немає.
"""
import glob
import html
import json
import os
import re
import sys
from collections import Counter, defaultdict
from html.parser import HTMLParser
from urllib.parse import urlparse

BASE = "https://sibway.com.ua/"
LANGS = ("uk", "en", "pl")
TITLE_MAX, DESC_MAX, DESC_MIN = 65, 160, 70
BAD_MARKERS = ("preview.sibway", "localhost", "127.0.0.1", "github.io", "lorem ipsum", "TEMP-PREVIEW")


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.imgs, self.linkrel, self.scripts = [], [], [], []
        self.meta, self.ids, self.h1, self.ld = {}, [], [], []
        self.title, self.lang = "", None
        self._t = self._h1 = self._ld = False
        self._buf = ""
        self.blank_no_noopener = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "a":
            self.links.append(a.get("href"))
            if a.get("target") == "_blank" and "noopener" not in (a.get("rel") or ""):
                self.blank_no_noopener += 1
        elif tag == "img":
            self.imgs.append(a)
        elif tag == "meta":
            k = a.get("name") or a.get("property")
            if k:
                self.meta[k] = a.get("content")
        elif tag == "link":
            self.linkrel.append(a)
        elif tag == "title":
            self._t = True
        elif tag == "h1":
            self._h1, self._buf = True, ""
        elif tag == "script":
            self.scripts.append(a.get("src"))
            if a.get("type") == "application/ld+json":
                self._ld, self._buf = True, ""

    def handle_endtag(self, tag):
        if tag == "title":
            self._t = False
        elif tag == "h1" and self._h1:
            self._h1 = False
            self.h1.append(re.sub(r"\s+", " ", self._buf).strip())
        elif tag == "script" and self._ld:
            self._ld = False
            self.ld.append(self._buf)

    def handle_data(self, d):
        if self._t:
            self.title += d
        if self._h1 or self._ld:
            self._buf += d


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    root = os.path.abspath(os.path.expanduser(sys.argv[1]))
    as_json = "--json" in sys.argv
    skip = ("/.git/", "/content-drafts/", "/node_modules/")
    files = sorted(
        os.path.relpath(p, root)
        for p in glob.glob(os.path.join(root, "**", "*.html"), recursive=True)
        if not any(s in p for s in skip)
    )
    allf = {
        os.path.relpath(p, root)
        for p in glob.glob(os.path.join(root, "**", "*"), recursive=True)
        if os.path.isfile(p) and not any(s in p for s in skip)
    }
    pages, raw = {}, {}
    for f in files:
        raw[f] = open(os.path.join(root, f), encoding="utf-8").read()
        p = Page()
        p.feed(raw[f])
        pages[f] = p

    issues = []

    def add(sev, where, msg):
        issues.append((sev, where, msg))

    def resolve(f, href):
        u = urlparse(href)
        if u.scheme in ("mailto", "tel", "javascript", "data"):
            return None
        if u.netloc and u.netloc not in ("sibway.com.ua", "www.sibway.com.ua"):
            return None
        if u.netloc:
            rel = u.path.lstrip("/")
        else:
            rel = os.path.normpath(os.path.join(os.path.dirname(f), u.path)) if u.path else f
        if rel in ("", ".") or rel.endswith("/"):
            rel = os.path.join(rel, "index.html")
        return os.path.normpath(rel), u.fragment

    def noindex(p):
        return "noindex" in (p.meta.get("robots") or "")

    titles, descs = defaultdict(list), defaultdict(list)
    for f, p in pages.items():
        is404 = f.endswith("404.html")
        t = html.unescape(p.title.strip())
        d = p.meta.get("description")
        if not noindex(p):
            titles[t].append(f)
            descs[d].append(f)
        if f == "index.html":
            continue
        if not t:
            add("P1", f, "немає <title>")
        elif len(t) > TITLE_MAX:
            add("P2", f, f"title {len(t)} симв. (> {TITLE_MAX})")
        if not d:
            add("P1", f, "немає meta description")
        elif len(d) > DESC_MAX:
            add("P2", f, f"description {len(d)} симв. (> {DESC_MAX})")
        elif len(d) < DESC_MIN:
            add("P2", f, f"description короткий: {len(d)} симв.")
        if len(p.h1) != 1 and not is404:
            add("P1", f, f"кількість H1 = {len(p.h1)}")
        exp = f.split("/")[0] if f.split("/")[0] in LANGS else None
        if not p.lang:
            add("P1", f, "немає атрибута lang")
        elif exp and not p.lang.startswith(exp):
            add("P1", f, f"lang={p.lang}, очікується {exp}")
        can = [l.get("href") for l in p.linkrel if l.get("rel") == "canonical"]
        if not can and not noindex(p):
            add("P1", f, "немає canonical")
        for c in can:
            if not c.startswith(BASE):
                add("P0", f, f"canonical не на {BASE}: {c}")
            elif c != BASE + f:
                add("P1", f, f"canonical ≠ URL файлу: {c}")
        p.hl = {l.get("hreflang"): l.get("href") for l in p.linkrel
                if l.get("rel") == "alternate" and l.get("hreflang")}
        for k, v in p.hl.items():
            if v and not v.startswith(BASE):
                add("P0", f, f"hreflang {k} не на {BASE}: {v}")
            elif v and v[len(BASE):] not in allf:
                add("P1", f, f"hreflang {k} веде на неіснуючий файл: {v}")
        if not noindex(p):
            for k in ("og:title", "og:description", "og:url", "og:image"):
                if k not in p.meta:
                    add("P2", f, f"немає {k}")
        for img in p.imgs:
            if "alt" not in img:
                add("P1", f, f"img без alt: {img.get('src')}")
            if not img.get("width") or not img.get("height"):
                add("P2", f, f"img без width/height: {img.get('src')}")
        for j in p.ld:
            try:
                json.loads(j)
            except ValueError as e:
                add("P0", f, f"JSON-LD не парситься: {e}")
        dup = sorted({i for i in p.ids if p.ids.count(i) > 1})
        if dup:
            add("P1", f, f"дублікати id: {dup}")
        if p.blank_no_noopener:
            add("P2", f, f"target=_blank без rel=noopener: {p.blank_no_noopener}")
        for h in p.links:
            if h is None:
                add("P2", f, "<a> без href")
                continue
            if h == "#":
                add("P0", f, 'посилання href="#" (заглушка)')
                continue
            r = resolve(f, h)
            if not r:
                continue
            rel, frag = r
            if rel not in allf:
                add("P0", f, f"бите посилання: {h}")
            elif frag and rel.endswith(".html") and rel in pages and frag not in pages[rel].ids:
                add("P2", f, f"якір #{frag} не знайдено в {rel}")
        for l in p.linkrel:
            if l.get("rel") in ("stylesheet", "icon", "preload", "apple-touch-icon"):
                r = resolve(f, l.get("href", ""))
                if r and r[0] not in allf:
                    add("P0", f, f"відсутній ресурс ({l.get('rel')}): {l.get('href')}")
        for s in p.scripts:
            if s:
                r = resolve(f, s)
                if r and r[0] not in allf:
                    add("P0", f, f"відсутній скрипт: {s}")
        for img in p.imgs:
            r = resolve(f, img.get("src", ""))
            if r and r[0] not in allf:
                add("P0", f, f"відсутнє зображення: {img.get('src')}")
        low = raw[f].lower()
        for m in BAD_MARKERS:
            if m.lower() in low:
                add("P0", f, f'знайдено "{m}" у HTML')

    for t, fs in titles.items():
        if t and len(fs) > 1:
            add("P1", ", ".join(fs), f"однаковий title: {t}")
    for d, fs in descs.items():
        if d and len(fs) > 1:
            add("P1", ", ".join(fs), "однаковий meta description")

    for f, p in pages.items():
        for k, v in getattr(p, "hl", {}).items():
            if v and v.startswith(BASE):
                tp = pages.get(v[len(BASE):])
                if tp is not None and getattr(tp, "hl", None) and BASE + f not in tp.hl.values():
                    add("P1", f, f"hreflang {k} → {v[len(BASE):]} не взаємний")

    by_lang = {l: {x[len(l) + 1:] for x in files if x.startswith(l + "/")} for l in LANGS}
    for l in LANGS:
        for o in LANGS:
            for m in sorted(by_lang[l] - by_lang[o]):
                add("INFO", f"{l}/{m}", f"немає відповідника в /{o}/")

    sm_path = os.path.join(root, "sitemap.xml")
    if os.path.exists(sm_path):
        locs = re.findall(r"<loc>([^<]+)</loc>", open(sm_path, encoding="utf-8").read())
        in_sm = {u[len(BASE):] for u in locs if u.startswith(BASE)}
        for u in locs:
            rel = u[len(BASE):]
            if not u.startswith(BASE):
                add("P0", "sitemap.xml", f"URL не на {BASE}: {u}")
            elif rel not in allf:
                add("P0", "sitemap.xml", f"URL без файлу: {u}")
            elif rel in pages and noindex(pages[rel]):
                add("P1", "sitemap.xml", f"noindex-сторінка в sitemap: {u}")
        for f, p in pages.items():
            if f != "index.html" and not f.endswith("404.html") and not noindex(p) and f not in in_sm:
                add("P0", f, "індексована сторінка відсутня в sitemap.xml")
    else:
        add("P0", "sitemap.xml", "файл відсутній")

    order = {"P0": 0, "P1": 1, "P2": 2, "INFO": 3}
    issues.sort(key=lambda i: (order[i[0]], i[1]))
    cnt = Counter(i[0] for i in issues)
    if as_json:
        print(json.dumps({"pages": len(files), "counts": cnt, "issues": issues}, ensure_ascii=False, indent=1))
    else:
        print(f"Сторінок: {len(files)} | P0: {cnt['P0']} | P1: {cnt['P1']} | P2: {cnt['P2']} | INFO: {cnt['INFO']}")
        for sev, where, msg in issues:
            print(f"[{sev}] {where}: {msg}")
    sys.exit(1 if cnt["P0"] else 0)


if __name__ == "__main__":
    main()
