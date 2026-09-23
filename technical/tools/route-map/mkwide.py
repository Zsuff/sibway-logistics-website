# Широкі (невисокі) анімовані карти для компактних hero: «Про компанію», «Блог», «Контакти».
exec(open('mkmapanim.py').read().split('# ---------- 1)')[0])
VX,VY,VW,VH=70,64,930,470
def wpage(title,css,body,hl=()):
    hls=''.join(f'<path class="hl" d="{"".join(HL[h])}"/>' for h in hl)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VX} {VY} {VW} {VH}" width="{VW}" height="{VH}" role="img" aria-labelledby="t"><title id="t">{title}</title>
<defs><filter id="fb" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="20"/></filter>
<mask id="fade"><rect x="{VX+45}" y="{VY+40}" width="{VW-90}" height="{VH-80}" fill="#fff" filter="url(#fb)"/></mask></defs>
<style>.coast{{fill:none;stroke:#86bfe2;stroke-width:3.2;stroke-linejoin:round}}.eu{{fill:#d9ecf8;stroke:#d9ecf8;stroke-width:1.6;stroke-linejoin:round}}.ua{{fill:#e6e4f4;stroke:{V};stroke-width:2;stroke-linejoin:round}}
.hl{{fill:#bfe3f5;stroke:{B};stroke-width:1.6}}
.hub{{transform-box:fill-box;transform-origin:center;animation:hub 2.6s ease-out infinite}}@keyframes hub{{0%{{transform:scale(.7);opacity:.6}}100%{{transform:scale(2.8);opacity:0}}}}
.lb{{fill:{V}}}.lt{{font:700 20px {FONT};fill:#fff}}.lw{{fill:#fff;stroke:#bfe3f5;stroke-width:1.5}}.ltd{{font:700 20px {FONT};fill:{V}}}
{PCSS}{css}
.static{{display:none}}@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}.anim{{display:none}}.static{{display:inline}}.hub{{opacity:0}}}}</style>
<g mask="url(#fade)"><path class="coast" d="{''.join(land)}"/><path class="eu" d="{''.join(land)}"/><path class="ua" d="{''.join(ua)}"/></g>{hls}
{body}
</svg>'''
RX,RY=P(26.25,50.62)                        # Рівне — офіс компанії
def hubdot(x,y,label,dy=46):
    return f'<circle class="hub" cx="{x:.0f}" cy="{y:.0f}" r="10" fill="{V}"/><circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="{V}" stroke="#fff" stroke-width="3"/>'+chip(x,y+dy,label,True)
CITIES=[(-0.12,51.5),(2.35,48.86),(12.5,41.9),(4.48,51.92),(9.99,53.55),(11.58,48.14),(14.42,50.08),(18.6,54.35),(19.04,47.5),(16.37,48.2),(8.68,50.11)]

# ---------- ПРО КОМПАНІЮ: двосторонній рух Україна ⇄ Європа (імпорт і експорт) ----------
imp=CITIES[::2]; exp_=CITIES[1::2]
b1,p1,d1,c1=pulses(imp,(RX,RY),pref='i',step=1.6,act=3.2)
# експорт: з України до міст (фіолетові імпульси)
n=len(exp_); cyc=n*1.6; act=3.2; pa=act/cyc*100; eb=[];ep=[];ec=[]
for i,c in enumerate(exp_):
    d,pts=qcurve((RX,RY),P(*c),0.16); ln=plen(pts); seg=46
    eb.append(f'<path class="rb" d="{d}"/>'); ep.append(f'<path class="rp ex e{i}" d="{d}"/>')
    ox,oy=P(*c); ep.append(f'<circle class="dt ed" cx="{ox:.0f}" cy="{oy:.0f}" r="5"/>')
    ec.append(f'.e{i}{{stroke-dasharray:{seg} {ln+seg:.0f};stroke-dashoffset:{seg};animation:ek{i} {cyc:.1f}s linear {i*1.6+0.8:.1f}s infinite}}'
              f'@keyframes ek{i}{{0%{{stroke-dashoffset:{seg};opacity:1}}{pa:.1f}%{{stroke-dashoffset:{-ln:.0f};opacity:1}}{pa+0.1:.1f}%,100%{{stroke-dashoffset:{-ln:.0f};opacity:0}}}}')
css=c1+''.join(ec)+f'.ex{{stroke:{V}}}.ed{{stroke:{V}}}'
body=f'{b1}{"".join(eb)}{p1}{"".join(ep)}{d1}'+hubdot(RX,RY,'Україна')
open('map-about.svg','w').write(wpage('Sibway Logistics: перевезення між Україною та Європою в обидва боки',css,body))

# ---------- БЛОГ: маршрут, уздовж якого по черзі зʼявляються картки-теми ----------
T=13
o=P(4.48,51.92); main,mp=qcurve(o,(RX,RY),0.1)
topics=[(0.1,'Документи','doc',-1),(0.5,'Вартість','cost',1),(0.86,'Запит','req',-1)]
def icon(kind):
    if kind=='doc': return f'<rect x="-8" y="-10" width="16" height="20" rx="2.5" fill="#fff" stroke="{V}" stroke-width="2"/><path d="M-4 -4h8M-4 0h8M-4 4h5" stroke="{B}" stroke-width="1.8" stroke-linecap="round"/>'
    if kind=='cost': return f'<circle r="10" fill="#fff" stroke="{V}" stroke-width="2"/><text y="5" text-anchor="middle" style="font:800 13px {FONT};fill:{B}">€</text>'
    return f'<rect x="-9" y="-10" width="18" height="20" rx="3" fill="#fff" stroke="{V}" stroke-width="2"/><path d="M-5 -3l2 2 4-4M-5 5l2 2 4-4" stroke="{B}" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
tv=0.08; te=0.9
cards=[];css=[f'.tv{{animation:tv {T}s linear infinite}}@keyframes tv{{0%,{g(tv-0.02)}{{opacity:0}}{g(tv)},{g(te)}{{opacity:1}}{g(te+0.03)},100%{{opacity:0}}}}']
for i,(f,label,kind,side) in enumerate(topics):
    x,y=mp[int(f*200)]; at=tv+(te-tv)*f
    w=len(label)*11.5+62
    tail_=f'M-8 22l8 10 8-10z' if side<0 else f'M-8 -22l8 -10 8 10z'
    cards.append(f'<g transform="translate({x:.0f},{y+62*side:.0f})"><g class="cd{i}"><path d="{tail_}" fill="#fff" stroke="#bfe3f5" stroke-width="1.5"/>'
                 f'<rect x="{-w/2:.0f}" y="-22" width="{w:.0f}" height="44" rx="12" fill="#fff" stroke="#bfe3f5" stroke-width="1.5"/>'
                 f'<g transform="translate({-w/2+24:.0f},0)">{icon(kind)}</g><text x="{-w/2+44:.0f}" y="6" style="font:700 17px {FONT};fill:{V}">{label}</text></g></g>'
                 f'<circle cx="{x:.0f}" cy="{y:.0f}" r="5" class="dt"/>')
    css.append(f'.cd{i}{{transform-box:fill-box;transform-origin:center bottom;opacity:0;animation:cd{i} {T}s ease-out infinite}}@keyframes cd{i}{{0%,{g(at-0.01)}{{opacity:0;transform:translateY(10px) scale(.9)}}{g(at+0.03)},{g(te+0.02)}{{opacity:1;transform:none}}{g(te+0.06)},100%{{opacity:0}}}}')
body=(f'<path class="rb" d="{main}" style="opacity:.5;stroke-width:2.2"/><path class="flow" d="{main}"/><path id="bm" d="{main}" fill="none"/>'
      f'<circle class="dt" cx="{o[0]:.0f}" cy="{o[1]:.0f}" r="6"/>'+hubdot(RX,RY,'Україна')+''.join(cards)+
      f'<g class="anim"><g class="tv">{truck(1.0)}</g><animateMotion dur="{T}s" repeatCount="indefinite" rotate="auto" calcMode="spline" keyPoints="0;0;1;1" keyTimes="0;{tv:.2f};{te:.2f};1" keySplines="0 0 1 1;{EASE};0 0 1 1"><mpath href="#bm"/></animateMotion></g>'
      f'<g class="static" transform="translate({mp[120][0]:.0f},{mp[120][1]:.0f})">{truck(1.0)}</g>')
open('map-blog.svg','w').write(wpage('Блог Sibway Logistics: документи, вартість і підготовка запиту на перевезення',''.join(css)+'.flow{fill:none;stroke:'+B+';stroke-width:3;stroke-linecap:round;stroke-dasharray:2 11;animation:flow 1.6s linear infinite}@keyframes flow{to{stroke-dashoffset:-26}}',body))

# ---------- КОНТАКТИ: звернення (лист, дзвінок, повідомлення) летять з Європи до офісу в Рівному ----------
T=12
SRC=[(-0.12,51.5),(2.35,48.86),(9.99,53.55),(12.5,41.9),(18.6,54.35),(19.04,47.5)]
kinds=['mail','phone','chat','mail','chat','phone']
def cicon(kind):
    base=f'<circle r="15" fill="#fff" stroke="{V}" stroke-width="2.2"/>'
    if kind=='mail': return base+f'<rect x="-8" y="-6" width="16" height="12" rx="2" fill="none" stroke="{B}" stroke-width="2"/><path d="M-7 -4l7 5 7-5" fill="none" stroke="{B}" stroke-width="2" stroke-linejoin="round"/>'
    if kind=='phone': return base+f'<path d="M-5 -8c-2 0-3 2-3 4 1 7 6 12 13 12 2 0 4-1 4-3l-1-3-4-1-2 2c-2-1-4-3-5-5l2-2-1-4z" fill="{B}" transform="scale(.8)"/>'
    return base+f'<path d="M-8 -6h16v10h-9l-4 4v-4h-3z" fill="none" stroke="{B}" stroke-width="2" stroke-linejoin="round"/>'
dep=[i*1.7 for i in range(6)]; TR_=2.6
paths=[];mv=[];css=[]
for i,src in enumerate(SRC):
    ox,oy=P(*src); d,_=qcurve((ox,oy),(RX,RY),0.16)
    paths.append(f'<path class="rb" d="{d}"/><path id="k{i}" d="{d}" fill="none"/><circle class="dt" cx="{ox:.0f}" cy="{oy:.0f}" r="5"/><circle class="dr sd{i}" cx="{ox:.0f}" cy="{oy:.0f}" r="5"/>')
    a=dep[i]/T; b=(dep[i]+TR_)/T
    mv.append(f'<g class="anim"><g class="m{i}">{cicon(kinds[i])}</g><animateMotion dur="{T}s" repeatCount="indefinite" calcMode="spline" keyPoints="0;0;1;1" keyTimes="0;{a:.3f};{b:.3f};1" keySplines="0 0 1 1;{EASE};0 0 1 1"><mpath href="#k{i}"/></animateMotion></g>')
    css.append(f'.m{i}{{opacity:0;animation:m{i} {T}s linear infinite}}@keyframes m{i}{{0%,{g(a)}{{opacity:0}}{g(a+0.015)},{g(b-0.02)}{{opacity:1}}{g(b)},100%{{opacity:0}}}}'
               f'.sd{i}{{animation:sd{i} {T}s ease-out infinite}}@keyframes sd{i}{{0%,{g(a)}{{transform:scale(1);opacity:0}}{g(a+0.005)}{{opacity:.8}}{g(a+0.08)},100%{{transform:scale(3);opacity:0}}}}'
               f'.ar{i}{{animation:ar{i} {T}s ease-out infinite}}@keyframes ar{i}{{0%,{g(b-0.005)}{{transform:scale(1);opacity:0}}{g(b)}{{opacity:.9}}{g(b+0.1)},100%{{transform:scale(3.4);opacity:0}}}}')
rings=''.join(f'<circle class="ring ar{i}" cx="{RX:.0f}" cy="{RY:.0f}" r="12"/>' for i in range(6))
pin=(f'<g transform="translate({RX:.0f},{RY:.0f})"><path d="M0 0c-9-12-16-19-16-28a16 16 0 0 1 32 0c0 9-7 16-16 28z" fill="{V}"/><circle cy="-28" r="6.5" fill="#fff"/></g>')
css=''.join(css)+f'.ring{{fill:none;stroke:{B};stroke-width:2.5;transform-box:fill-box;transform-origin:center;opacity:0}}'
body=f'{"".join(paths)}{rings}{pin}'+chip(RX,RY+34,'Рівне',True)+''.join(mv)
open('map-contacts.svg','w').write(wpage('Контакти Sibway Logistics: звернення з усієї Європи до офісу в Рівному',css,body))
print('ok')
