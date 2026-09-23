# Карта «Уся Європа → Україна» для сторінки «Міжнародні вантажні перевезення».
# Один силует Європи без внутрішніх кордонів, Україна (з Кримом) виділена, м'які імпульси з міст ЄС до Києва,
# одна сідельна фура (тягач + напівпричіп) на головному маршруті. Краї розмиті маскою.
import json, math, re
src=open('mkmap.py').read().split('paths={}')[0]
src=src.replace("W,H=800,560","W,H=1000,1000")
src=re.sub(r"x0,y0=proj\(.*?\n","x0,y0=proj(-10,38)[0],proj(8,61.5)[1]\n",src)
src=re.sub(r"x1,y1=proj\(.*?\n","x1,y1=proj(42.5,47)[0],min(proj(-6,35.6)[1],proj(33,35.6)[1])\n",src)
src=src.replace("sx=W/(x1-x0); sy=H/(y0-y1); s=min(sx,sy)","s=W/(x1-x0); H=round((y0-y1)*s)")
exec(src)
from semi import semi
EU={'008','020','040','056','070','100','112','191','196','203','208','233','246','250','276','300','348','372','380','428','438','440','442','470','492','498','499','528','807','578','616','620','642','674','688','703','705','724','752','756','792','804','826','336','234','831','832','833','248'}
EU_NAMES={'Kosovo','N. Cyprus'}
land=[]; ua=[]; HL={'616':[],'276':[],'203':[]}
for g in geoms:
    gid=g.get('id'); name=g.get('properties',{}).get('name','')
    if not (gid in EU or name in EU_NAMES): continue
    polys=g['arcs'] if g['type']=='MultiPolygon' else ([g['arcs']] if g['type']=='Polygon' else [])
    for poly in polys:
        for r in poly:
            pts=[P(*pt) for pt in ring(r)]
            xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
            if max(xs)<-60 or min(xs)>W+60 or max(ys)<-60 or min(ys)>H+60: continue
            out=[(round(x),round(y)) for x,y in dp(pts,1.2)]
            out=[p for i,p in enumerate(out) if i==0 or p!=out[i-1]]
            if len(out)<3: continue
            dd='M'+'L'.join(f'{x},{y}' for x,y in out)+'Z'
            (ua if gid=='804' else land).append(dd)
            if gid in HL: HL[gid].append(dd)
V='#29265b'; B='#189cd9'
def build(cities, truck_from, title, highlight=None, hl_label=None, hl_pos=None):
    tx,ty=P(30.52,50.45)
    def curve(ox,oy,bend=0.18):
        mx,my=(ox+tx)/2,(oy+ty)/2; vx,vy=tx-ox,ty-oy; L=math.hypot(vx,vy)
        cx,cy=mx+vy*bend*(1 if vx>0 else -1), my-abs(vx)*bend
        # довжина кривої
        n=60; pts=[((1-t)**2*ox+2*(1-t)*t*cx+t*t*tx,(1-t)**2*oy+2*(1-t)*t*cy+t*t*ty) for t in [i/n for i in range(n+1)]]
        ln=sum(math.dist(pts[i],pts[i+1]) for i in range(n))
        return f'M{ox:.0f},{oy:.0f} Q{cx:.0f},{cy:.0f} {tx:.0f},{ty:.0f}', ln
    N=len(cities); STEP=1.3; CYC=N*STEP; ACT=3.4; pa=ACT/CYC*100
    base=[]; pulses=[]; dots=[]; css=[]
    for i,(lo,la) in enumerate(cities):
        ox,oy=P(lo,la); d,ln=curve(ox,oy)
        base.append(f'<path class="rb" d="{d}"/>')
        seg=46
        css.append(f'.p{i}{{stroke-dasharray:{seg} {ln+seg:.0f};stroke-dashoffset:{seg};animation:k{i} {CYC:.1f}s linear {i*STEP:.1f}s infinite}}'
                   f'@keyframes k{i}{{0%{{stroke-dashoffset:{seg};opacity:1}}{pa:.1f}%{{stroke-dashoffset:{-ln:.0f};opacity:1}}{pa+0.1:.1f}%,100%{{stroke-dashoffset:{-ln:.0f};opacity:0}}}}'
                   f'.d{i}{{animation:dp {CYC:.1f}s ease-out {i*STEP:.1f}s infinite}}')
        pulses.append(f'<path class="rp p{i}" d="{d}"/>')
        dots.append(f'<circle class="dt" cx="{ox:.0f}" cy="{oy:.0f}" r="5"/><circle class="dr d{i}" cx="{ox:.0f}" cy="{oy:.0f}" r="5"/>')
    # головний маршрут для фури: truck_from → Київ
    hx,hy=P(*truck_from); main,_=curve(hx,hy,0.12)
    TR=f'<g transform="scale(1.15) translate(-42,-14)">{semi()}</g>'
    w=len('Україна')*20*0.62+30; h=42
    hl=''
    if highlight:
        hl='<path class="hl" d="'+''.join(HL[highlight])+'"/>'
        lx,ly=P(*hl_pos); lw=len(hl_label)*20*0.62+30
        hl+=f'<g transform="translate({lx:.0f},{ly:.0f})"><rect x="{-lw/2:.0f}" y="-21" width="{lw:.0f}" height="42" rx="21" class="lw"/><text y="7" text-anchor="middle" class="ltd">{hl_label}</text></g>'
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t"><title id="t">{title}</title>
    <defs><filter id="fb" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="38"/></filter>
    <mask id="fade"><rect x="60" y="60" width="{W-120}" height="{H-120}" fill="#fff" filter="url(#fb)"/></mask></defs>
    <style>.eu{{fill:#e1f0f9;stroke:#e1f0f9;stroke-width:1.4;stroke-linejoin:round}}.ua{{fill:#e6e4f4;stroke:{V};stroke-width:2;stroke-linejoin:round}}
    .rb{{fill:none;stroke:{B};stroke-width:1.6;opacity:.28}}.rp{{fill:none;stroke:{B};stroke-width:3.4;stroke-linecap:round;opacity:0}}
    .dt{{fill:#fff;stroke:{B};stroke-width:2.6}}.dr{{fill:none;stroke:{B};stroke-width:2;transform-box:fill-box;transform-origin:center;opacity:0}}
    @keyframes dp{{0%{{transform:scale(1);opacity:.8}}8%,100%{{transform:scale(3.2);opacity:0}}}}
    .hub{{transform-box:fill-box;transform-origin:center;animation:hub 2.6s ease-out infinite}}@keyframes hub{{0%{{transform:scale(.7);opacity:.6}}100%{{transform:scale(2.8);opacity:0}}}}
    .lb{{fill:{V}}}.hl{{fill:#bfe3f5;stroke:{B};stroke-width:2;stroke-linejoin:round}}.lw{{fill:#fff;stroke:#bfe3f5;stroke-width:1.5}}.ltd{{font:700 20px Manrope,Inter,Arial,sans-serif;fill:{V}}}.lt{{font:700 20px Manrope,Inter,Arial,sans-serif;fill:#fff}}
    {''.join(css)}
    .static{{display:none}}@media (prefers-reduced-motion:reduce){{.anim,.rp,.dr{{display:none}}.static{{display:inline}}.hub{{animation:none;opacity:0}}}}</style>
    <g mask="url(#fade)"><path class="eu" d="{''.join(land)}"/><path class="ua" d="{''.join(ua)}"/></g>{hl}
    {''.join(base)}{''.join(pulses)}{''.join(dots)}
    <path id="main" d="{main}" fill="none"/>
    <circle class="hub" cx="{tx:.0f}" cy="{ty:.0f}" r="10" fill="{V}"/><circle cx="{tx:.0f}" cy="{ty:.0f}" r="9" fill="{V}" stroke="#fff" stroke-width="3"/>
    <g class="anim">{TR}<animateMotion dur="9s" repeatCount="indefinite" rotate="auto"><mpath href="#main"/></animateMotion></g>
    <g class="static" transform="translate({(hx+tx)/2:.0f},{(hy+ty)/2-40:.0f}) rotate(8)">{TR}</g>
    <g transform="translate({tx:.0f},{ty+48:.0f})"><rect x="{-w/2:.0f}" y="{-h/2}" width="{w:.0f}" height="{h}" rx="21" class="lb"/><text y="7" text-anchor="middle" class="lt">Україна</text></g>
    </svg>'''
    return svg

EU_CITIES=[(-3.7,40.4),(2.35,48.86),(4.48,51.92),(9.19,45.46),(9.99,53.55),(11.58,48.14),
        (14.42,50.08),(18.6,54.35),(19.04,47.5),(26.1,44.43),(28.97,41.0),(-0.12,51.5)]
PL=[(21.01,52.23),(19.94,50.06),(18.65,54.35),(17.04,51.11),(16.93,52.41)]   # Варшава, Краків, Гданськ, Вроцлав, Познань
CZ=[(14.42,50.08),(16.61,49.2),(18.26,49.82)]   # Прага, Брно, Острава
DE=[(13.40,52.52),(9.99,53.55),(11.58,48.14),(8.68,50.11),(6.96,50.94)]      # Берлін, Гамбург, Мюнхен, Франкфурт, Кельн
for fn,args in [
  ('routes-europe',dict(cities=EU_CITIES,truck_from=(9.99,53.55),title='Перевезення вантажів з усієї Європи в Україну')),
  ('route-poland-ukraine',dict(cities=PL,truck_from=(16.93,52.41),title='Маршрут імпортного перевезення: Польща — Україна',highlight='616',hl_label='Польща',hl_pos=(19.2,55.5))),
  ('route-germany-ukraine',dict(cities=DE,truck_from=(6.96,50.94),title='Маршрут імпортного перевезення: Німеччина — Україна',highlight='276',hl_label='Німеччина',hl_pos=(10.0,55.6))),
  ('route-czechia-ukraine',dict(cities=CZ,truck_from=(14.42,50.08),title='Маршрут імпортного перевезення: Чехія — Україна',highlight='203',hl_label='Чехія',hl_pos=(15.3,51.9))),
]:
    open(fn+'.svg','w').write(build(**args)); print(fn)
