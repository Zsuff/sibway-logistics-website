import json, math, sys
exec(open('mkmap.py').read().split("json.dump({'paths'")[0])  # builds paths, P
PTS={'276':(10.3,51.0),'616':(19.2,52.1),'203':(15.4,49.8),'642':(24.9,45.9),'804':(31.3,49.2)}
def svg(origin, label_from, label_to, animated, title):
    ox,oy=P(*PTS[origin]); tx,ty=P(*PTS['804'])
    cx,cy=(ox+tx)/2,min(oy,ty)-95
    route=f'M{ox:.0f},{oy:.0f} Q{cx:.0f},{cy:.0f} {tx:.0f},{ty:.0f}'
    def q(t):
        x=(1-t)**2*ox+2*(1-t)*t*cx+t*t*tx; y=(1-t)**2*oy+2*(1-t)*t*cy+t*t*ty
        dx=2*(1-t)*(cx-ox)+2*t*(tx-cx); dy=2*(1-t)*(cy-oy)+2*t*(ty-cy)
        return x,y,math.degrees(math.atan2(dy,dx))
    base=[]; hl=[]
    for cid,d in paths.items():
        if cid==origin: hl.append(f'<path class="o" d="{d}"/>')
        elif cid=='804': hl.append(f'<path class="u" d="{d}"/>')
        else: base.append(d)
    truck='''<g class="truck"><g transform="scale(1.35) translate(-24,-15)">
<rect x="0" y="2" width="31" height="19" rx="3" fill="#29265b"/>
<rect x="3" y="5" width="25" height="3" rx="1.5" fill="#189cd9"/>
<path d="M32 8h7.5a3 3 0 0 1 2.6 1.5l3.6 6.2a3 3 0 0 1 .3 1.3V21H32z" fill="#29265b"/>
<path d="M35 10.5h4.6l3 5H35z" fill="#e8f6fc"/>
<circle cx="9" cy="23" r="3.6" fill="#201d48" stroke="#fff" stroke-width="1.6"/>
<circle cx="38" cy="23" r="3.6" fill="#201d48" stroke="#fff" stroke-width="1.6"/></g></g>'''
    def label(x,y,text,cls,dy):
        w=len(text)*12.4+34
        return f'<g transform="translate({x:.0f},{y+dy:.0f})"><rect x="{-w/2:.0f}" y="-21" width="{w:.0f}" height="42" rx="21" class="lb {cls}"/><text x="0" y="7" text-anchor="middle" class="lt">{text}</text></g>'
    mx,my,ang=q(0.5)
    if animated:
        moving=f'''<g class="anim">{truck.replace('class="truck"','class="truck"')}<animateMotion dur="7s" repeatCount="indefinite" rotate="auto" keyPoints="0;1" keyTimes="0;1" calcMode="linear"><mpath href="#route"/></animateMotion></g>
<g class="static" transform="translate({mx:.0f},{my:.0f}) rotate({ang:.0f})">{truck}</g>'''
        extra_css='''.flow{animation:dash 1.2s linear infinite}@keyframes dash{to{stroke-dashoffset:-30}}
.pulse{transform-origin:center;transform-box:fill-box;animation:pulse 2.4s ease-out infinite}@keyframes pulse{0%{transform:scale(.6);opacity:.7}100%{transform:scale(2.4);opacity:0}}
.static{display:none}
@media (prefers-reduced-motion:reduce){.anim{display:none}.static{display:inline}.flow,.pulse{animation:none}.pulse{opacity:0}}'''
        pulse=f'<circle class="pulse" cx="{tx:.0f}" cy="{ty:.0f}" r="9" fill="#29265b"/>'
    else:
        moving=f'<g transform="translate({mx:.0f},{my:.0f}) rotate({ang:.0f})">{truck}</g>'
        extra_css=''; pulse=''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t">
<title id="t">{title}</title>
<style>.c{{fill:#dde3ec;stroke:#fff;stroke-width:.8;stroke-linejoin:round}}.o{{fill:#9fd6f0;stroke:#fff;stroke-width:.8}}.u{{fill:#c9c6e6;stroke:#fff;stroke-width:.8}}
.r{{fill:none;stroke:#189cd9;stroke-width:3.2;stroke-linecap:round;stroke-dasharray:2 10}}
.lb{{fill:#fff;stroke:#d9dde3}}.lb.to{{fill:#29265b;stroke:#29265b}}.lt{{font:700 20px Manrope,Inter,Arial,sans-serif;fill:#29265b}}.to+.lt{{fill:#fff}}
{extra_css}</style>
<path class="c" d="{''.join(base)}"/>
{''.join(hl)}
<path id="route" class="r flow" d="{route}"/>
<circle cx="{ox:.0f}" cy="{oy:.0f}" r="7" fill="#fff" stroke="#189cd9" stroke-width="3.5"/>
{pulse}<circle cx="{tx:.0f}" cy="{ty:.0f}" r="8" fill="#29265b" stroke="#fff" stroke-width="3"/>
{moving}
{label(ox,oy,label_from,'from',-42)}
{label(tx,ty,label_to,'to',46)}
</svg>'''
open('route-poland-ukraine.svg','w').write(svg('616','Польща','Україна',True,'Маршрут імпортного перевезення: Польща — Україна'))
open('route-germany-ukraine.svg','w').write(svg('276','Німеччина','Україна',True,'Маршрут імпортного перевезення: Німеччина — Україна'))
import os; print(os.path.getsize('route-poland-ukraine.svg'),os.path.getsize('route-germany-ukraine.svg'))
