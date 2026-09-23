# Генератор SVG-карт маршрутів Sibway (варіант "лише потрібні країни").
import json, math
exec(open('mkmap.py').read().split("json.dump({'paths'")[0])   # paths (id->d), P()
PTS={'276':(10.3,51.0),'616':(19.2,52.1),'203':(15.4,49.8),'703':(19.5,48.7),'348':(19.3,47.2),
     '642':(24.9,45.9),'792':(30.2,40.1),'100':(25.3,42.7),'804':(31.3,49.2)}
from semi import semi
TRUCK='<g transform="translate(-42,-14)">'+semi()+'</g>'
def bbox_of(d):
    import re
    nums=list(map(int,re.findall(r'-?\d+',d))); xs=nums[0::2]; ys=nums[1::2]; return min(xs),min(ys),max(xs),max(ys)
def build(origins, title, labels=True, scale_truck=1.0, font=20, dur=7, arc=95, plain=False):
    ids=[o for o,_ in origins]+['804']
    bb=[bbox_of(paths[i]) for i in ids]
    x0=min(b[0] for b in bb); y0=min(b[1] for b in bb); x1=max(b[2] for b in bb); y1=max(b[3] for b in bb)
    pad=40; x0-=pad; y0-=pad+30; x1+=pad; y1+=pad
    tx,ty=P(*PTS['804'])
    shapes=[f'<path class="o" d="{paths[o]}"/>' for o,_ in origins]+[f'<path class="u" d="{paths["804"]}"/>']
    routes=[]; trucks=[]; statics=[]; labs=[]; dots=[]
    n=len(origins)
    for k,(o,lab) in enumerate(origins):
        ox,oy=P(*PTS[o])
        mx0,my0=(ox+tx)/2,(oy+ty)/2; vx,vy=tx-ox,ty-oy; L=math.hypot(vx,vy) or 1
        cx,cy=mx0+vy/L*arc*(-1 if vx>0 else 1), my0-abs(vx)/L*arc   # вигин дуги вгору/вбік
        d=f'M{ox:.0f},{oy:.0f} Q{cx:.0f},{cy:.0f} {tx:.0f},{ty:.0f}'
        routes.append(f'<path id="r{k}" class="r flow" d="{d}"/>')
        dots.append(f'<circle cx="{ox:.0f}" cy="{oy:.0f}" r="6.5" fill="#fff" stroke="#189cd9" stroke-width="3.5"/>')
        begin=f'{-k*dur/n:.2f}s'
        trucks.append(f'<g class="anim"><g transform="scale({scale_truck})">{TRUCK}</g><animateMotion dur="{dur}s" begin="{begin}" repeatCount="indefinite" rotate="auto"><mpath href="#r{k}"/></animateMotion></g>')
        t=0.5; mx=(1-t)**2*ox+2*(1-t)*t*cx+t*t*tx; my=(1-t)**2*oy+2*(1-t)*t*cy+t*t*ty
        dx=2*(1-t)*(cx-ox)+2*t*(tx-cx); dy=2*(1-t)*(cy-oy)+2*t*(ty-cy); ang=math.degrees(math.atan2(dy,dx))
        statics.append(f'<g class="static" transform="translate({mx:.0f},{my:.0f}) rotate({ang:.0f}) scale({scale_truck})">{TRUCK}</g>')
        if labels and plain:
            labs.append(f'<text x="{ox:.0f}" y="{oy+font*1.5:.0f}" text-anchor="middle" class="pt">{lab}</text>')
        elif labels:
            w=len(lab)*font*0.62+30; h=font*2.1
            labs.append(f'<g transform="translate({ox:.0f},{oy-h*0.95:.0f})"><rect x="{-w/2:.0f}" y="{-h/2:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{h/2:.0f}" class="lb"/><text y="{font*0.35:.0f}" text-anchor="middle" class="lt">{lab}</text></g>')
    w=len('Україна')*font*0.62+30; h=font*2.1
    uy=ty+h*1.05 if not plain else ty+h*1.1
    ux=tx if not plain else tx+w*0.35
    labs.append(f'<g transform="translate({ux:.0f},{uy:.0f})"><rect x="{-w/2:.0f}" y="{-h/2:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{h/2:.0f}" class="lb to"/><text y="{font*0.35:.0f}" text-anchor="middle" class="lt">Україна</text></g>')
    W,H=x1-x0,y1-y0
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0} {y0} {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t"><title id="t">{title}</title>
<style>.o{{fill:#dff1fa;stroke:#189cd9;stroke-width:1.6;stroke-linejoin:round}}.u{{fill:#e6e4f4;stroke:#29265b;stroke-width:1.6;stroke-linejoin:round}}
.r{{fill:none;stroke:#189cd9;stroke-width:3.2;stroke-linecap:round;stroke-dasharray:2 10}}
.lb{{fill:#fff;stroke:#bfe3f5}}.lb.to{{fill:#29265b;stroke:#29265b}}.lt{{font:700 {font}px Manrope,Inter,Arial,sans-serif;fill:#29265b}}.to+.lt{{fill:#fff}}.pt{{font:700 {font}px Manrope,Inter,Arial,sans-serif;fill:#0f6c97;paint-order:stroke;stroke:#fff;stroke-width:4px}}
.flow{{animation:dash 1.2s linear infinite}}@keyframes dash{{to{{stroke-dashoffset:-24}}}}
.pulse{{transform-origin:center;transform-box:fill-box;animation:pulse 2.4s ease-out infinite}}@keyframes pulse{{0%{{transform:scale(.6);opacity:.7}}100%{{transform:scale(2.6);opacity:0}}}}
.static{{display:none}}@media (prefers-reduced-motion:reduce){{.anim{{display:none}}.static{{display:inline}}.flow,.pulse{{animation:none}}.pulse{{opacity:0}}}}</style>
{''.join(shapes)}
{''.join(routes)}
{''.join(dots)}
<circle class="pulse" cx="{tx:.0f}" cy="{ty:.0f}" r="9" fill="#29265b"/><circle cx="{tx:.0f}" cy="{ty:.0f}" r="8" fill="#29265b" stroke="#fff" stroke-width="3"/>
{''.join(trucks)}{''.join(statics)}
{''.join(labs)}
</svg>''', (W,H)
out={}
for fn,orig,title,kw in [
 ('route-poland-ukraine',[('616','Польща')],'Маршрут імпортного перевезення: Польща — Україна',{}),
 ('route-germany-ukraine',[('276','Німеччина')],'Маршрут імпортного перевезення: Німеччина — Україна',{}),
 ('routes-network',[('276','Німеччина'),('616','Польща'),('203','Чехія'),('703','Словаччина'),('348','Угорщина'),('642','Румунія'),('100','Болгарія'),('792','Туреччина')],
  'Напрямки перевезень Sibway Logistics: Німеччина, Польща, Чехія, Словаччина, Угорщина, Румунія, Болгарія, Туреччина — Україна',dict(font=17,scale_truck=0.95,dur=10,arc=28,plain=True)),
]:
    svgtxt,wh=build(orig,title,**kw); open(fn+".svg","w").write(svgtxt); out[fn]=wh
print(out)
