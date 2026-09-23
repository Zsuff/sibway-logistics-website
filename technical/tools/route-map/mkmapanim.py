# Анімовані карти в стилі routes-europe для сторінок «Митні послуги», «Складські послуги», «Логістичний аудит».
import math, re
_pre=open('mkeurope.py').read().split('def build')[0].replace("HL={'616':[],'276':[]}","HL={'616':[],'276':[],'203':[]}")
exec(_pre)
FONT='Manrope,Inter,Arial,sans-serif'; G='#d9dde3'; BS='#e8f6fc'; VS='#eeeef6'; D='#201d48'
KX,KY=P(30.52,50.45)
def cubic(p0,p1,p2,p3,n=40):
    return [((1-t)**3*p0[0]+3*(1-t)**2*t*p1[0]+3*(1-t)*t*t*p2[0]+t**3*p3[0],(1-t)**3*p0[1]+3*(1-t)**2*t*p1[1]+3*(1-t)*t*t*p2[1]+t**3*p3[1]) for t in [i/n for i in range(n+1)]]
def plen(pts): return sum(math.dist(pts[i],pts[i+1]) for i in range(len(pts)-1))
def smooth(pts,k=1/6):
    """Catmull-Rom → cubic; повертає d і довжини до кожного вузла"""
    d=f'M{pts[0][0]:.0f},{pts[0][1]:.0f}'; acc=[0.0]
    for i in range(len(pts)-1):
        p0=pts[i-1] if i>0 else pts[i]; p1=pts[i]; p2=pts[i+1]; p3=pts[i+2] if i+2<len(pts) else pts[i+1]
        c1=(p1[0]+(p2[0]-p0[0])*k,p1[1]+(p2[1]-p0[1])*k); c2=(p2[0]-(p3[0]-p1[0])*k,p2[1]-(p3[1]-p1[1])*k)
        d+=f' C{c1[0]:.0f},{c1[1]:.0f} {c2[0]:.0f},{c2[1]:.0f} {p2[0]:.0f},{p2[1]:.0f}'
        acc.append(acc[-1]+plen(cubic(p1,c1,c2,p2)))
    return d,acc
def chip(x,y,text,dark=False):
    w=len(text)*20*0.62+30
    return (f'<g transform="translate({x:.0f},{y:.0f})"><rect x="{-w/2:.0f}" y="-21" width="{w:.0f}" height="42" rx="21" class="{"lb" if dark else "lw"}"/>'
            f'<text y="7" text-anchor="middle" class="{"lt" if dark else "ltd"}">{text}</text></g>')
def truck(sc=1.15): return f'<g transform="scale({sc}) translate(-42,-14)">{semi()}</g>'
def page(title,css,body,hl=()):
    hls=''.join(f'<path class="hl" d="{"".join(HL[h])}"/>' for h in hl)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t"><title id="t">{title}</title>
<defs><filter id="fb" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="38"/></filter>
<mask id="fade"><rect x="60" y="60" width="{W-120}" height="{H-120}" fill="#fff" filter="url(#fb)"/></mask></defs>
<style>.eu{{fill:#e1f0f9;stroke:#e1f0f9;stroke-width:1.4;stroke-linejoin:round}}.ua{{fill:#e6e4f4;stroke:{V};stroke-width:2;stroke-linejoin:round}}
.hl{{fill:#bfe3f5;stroke:{B};stroke-width:1.6;stroke-linejoin:round}}
.rb{{fill:none;stroke:{B};stroke-width:1.8;opacity:.35}}.flow{{fill:none;stroke:{B};stroke-width:3;stroke-linecap:round;stroke-dasharray:2 11;animation:flow 1.6s linear infinite}}@keyframes flow{{to{{stroke-dashoffset:-26}}}}
.hub{{transform-box:fill-box;transform-origin:center;animation:hub 2.6s ease-out infinite}}@keyframes hub{{0%{{transform:scale(.7);opacity:.6}}100%{{transform:scale(2.8);opacity:0}}}}
.lb{{fill:{V}}}.lt{{font:700 20px {FONT};fill:#fff}}.lw{{fill:#fff;stroke:#bfe3f5;stroke-width:1.5}}.ltd{{font:700 20px {FONT};fill:{V}}}
{css}
.static{{display:none}}@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}.anim{{display:none}}.static{{display:inline}}.hub{{opacity:0}}}}</style>
<g mask="url(#fade)"><path class="eu" d="{''.join(land)}"/><path class="ua" d="{''.join(ua)}"/></g>{hls}
{body}
</svg>'''
KYIV=f'<circle class="hub" cx="{KX:.0f}" cy="{KY:.0f}" r="10" fill="{V}"/><circle cx="{KX:.0f}" cy="{KY:.0f}" r="9" fill="{V}" stroke="#fff" stroke-width="3"/>'+chip(KX,KY+48,'Україна',True)


# ---------- спільне: плавні дуги та «пульсація» з міст (як на routes-europe) ----------
def qcurve(o,t,bend):
    ox,oy=o; tx,ty=t; mx,my=(ox+tx)/2,(oy+ty)/2; vx,vy=tx-ox,ty-oy
    cx,cy=mx+vy*bend*(1 if vx>0 else -1), my-abs(vx)*bend
    pts=[((1-u)**2*ox+2*(1-u)*u*cx+u*u*tx,(1-u)**2*oy+2*(1-u)*u*cy+u*u*ty) for u in [i/200 for i in range(201)]]
    return f'M{ox:.0f},{oy:.0f} Q{cx:.0f},{cy:.0f} {tx:.0f},{ty:.0f}', pts
def pulses(cities,target,pref='p',step=1.3,act=3.4,bend=0.18,seg=46,dots=True):
    n=len(cities); cyc=n*step; pa=act/cyc*100; base=[];pl=[];dt=[];css=[]
    for i,c in enumerate(cities):
        o=P(*c); d,pts=qcurve(o,target,bend); ln=plen(pts)
        base.append(f'<path class="rb" d="{d}"/>')
        css.append(f'.{pref}{i}{{stroke-dasharray:{seg} {ln+seg:.0f};stroke-dashoffset:{seg};animation:{pref}k{i} {cyc:.1f}s linear {i*step:.1f}s infinite}}'
                   f'@keyframes {pref}k{i}{{0%{{stroke-dashoffset:{seg};opacity:1}}{pa:.1f}%{{stroke-dashoffset:{-ln:.0f};opacity:1}}{pa+0.1:.1f}%,100%{{stroke-dashoffset:{-ln:.0f};opacity:0}}}}')
        pl.append(f'<path class="rp {pref}{i}" d="{d}"/>')
        if dots:
            css.append(f'.{pref}d{i}{{animation:dp {cyc:.1f}s ease-out {i*step:.1f}s infinite}}')
            dt.append(f'<circle class="dt" cx="{o[0]:.0f}" cy="{o[1]:.0f}" r="5"/><circle class="dr {pref}d{i}" cx="{o[0]:.0f}" cy="{o[1]:.0f}" r="5"/>')
    return ''.join(base),''.join(pl),''.join(dt),''.join(css)
PCSS=(f'.rb{{fill:none;stroke:{B};stroke-width:1.6;opacity:.28}}.rp{{fill:none;stroke:{B};stroke-width:3.4;stroke-linecap:round;opacity:0}}'
      f'.dt{{fill:#fff;stroke:{B};stroke-width:2.6}}.dr{{fill:none;stroke:{B};stroke-width:2;transform-box:fill-box;transform-origin:center;opacity:0}}'
      '@keyframes dp{0%{transform:scale(1);opacity:.8}8%,100%{transform:scale(3.2);opacity:0}}'
      '@media (prefers-reduced-motion:reduce){.rp,.dr{display:none}}')
EU_CITIES=[(-3.7,40.4),(4.48,51.92),(9.19,45.46),(9.99,53.55),(11.58,48.14),(14.42,50.08),(18.6,54.35),(19.04,47.5),(26.1,44.43),(28.97,41.0),(-0.12,51.5)]
EASE='.42 0 .58 1'
g=lambda x: f'{x*100:.1f}%'

# ---------- 1) МИТНИЦЯ: плавна дуга Париж → Київ, митний пост на кордоні, пульсація з міст ----------
o=P(2.35,48.86); main,mp=qcurve(o,(KX,KY),0.08)
cum=[0.0]
for i in range(len(mp)-1): cum.append(cum[-1]+math.dist(mp[i],mp[i+1]))
LT=cum[-1]
polys=[[tuple(map(int,p.split(','))) for p in s_[1:-1].split('L')] for s_ in ua]; big=max(polys,key=len)
def inside(x,y,poly):
    c=False
    for i in range(len(poly)):
        x1,y1=poly[i]; x2,y2=poly[i-1]
        if (y1>y)!=(y2>y) and x<(x2-x1)*(y-y1)/(y2-y1)+x1: c=not c
    return c
ci=next(i for i,p in enumerate(mp) if inside(*p,big)); bx,by=mp[ci]; Lb=cum[ci]
R=30
fs=(Lb-R-8-48*1.1)/LT
v=LT/12.0
t1=fs*LT/v; tp=3.2; t2=(1-fs)*LT/v; T=round(t1+tp+t2+1.0,1)
k1=t1/T; k2=(t1+tp)/T; k3=(t1+tp+t2)/T
css=PCSS+f'''
.tv{{animation:tv {T}s linear infinite}}@keyframes tv{{0%{{opacity:0}}3%,{g(k3-0.01)}{{opacity:1}}{g(k3+0.03)},100%{{opacity:0}}}}
.arm{{transform-origin:{bx+2:.0f}px {by+1:.0f}px;animation:arm {T}s ease-in-out infinite}}@keyframes arm{{0%,{g(k1+0.06)}{{transform:rotate(0)}}{g(k1+0.11)},{g(k2+0.1)}{{transform:rotate(80deg)}}{g(k2+0.16)},100%{{transform:rotate(0)}}}}
.lamp{{animation:lamp {T}s steps(1) infinite}}@keyframes lamp{{0%,{g(k1+0.06)}{{fill:#e5484d}}{g(k1+0.061)},{g(k2+0.16)}{{fill:#2fb37a}}{g(k2+0.161)},100%{{fill:#e5484d}}}}
.doc{{transform-box:fill-box;transform-origin:center bottom;opacity:0;animation:doc {T}s ease-in-out infinite}}@keyframes doc{{0%,{g(k1)}{{opacity:0;transform:translateY(10px) scale(.85)}}{g(k1+0.03)},{g(k2-0.02)}{{opacity:1;transform:none}}{g(k2+0.03)},100%{{opacity:0;transform:translateY(-10px)}}}}
.tick{{stroke-dasharray:40;stroke-dashoffset:40;animation:tick {T}s ease-in-out infinite}}@keyframes tick{{0%,{g(k1+0.03)}{{stroke-dashoffset:40}}{g(k1+0.06)},100%{{stroke-dashoffset:0}}}}
.bd{{transform-box:fill-box;transform-origin:center;opacity:0;animation:bd {T}s ease-out infinite}}@keyframes bd{{0%,{g(k1)}{{transform:scale(1);opacity:0}}{g(k1+0.01)}{{opacity:.7}}{g(k1+0.09)},100%{{transform:scale(2);opacity:0}}}}'''
stripes=''.join(f'M{bx-25+i*7:.0f} {by-1:.0f}h4l-3 3h-4z' for i in range(3))
badge=(f'<circle class="bd" cx="{bx:.0f}" cy="{by:.0f}" r="{R}" fill="none" stroke="{B}" stroke-width="3"/>'
       f'<circle cx="{bx:.0f}" cy="{by:.0f}" r="{R}" fill="#fff" stroke="{V}" stroke-width="2.6"/>'
       f'<rect x="{bx+6:.0f}" y="{by-15:.0f}" width="14" height="24" rx="3" fill="{VS}" stroke="{V}" stroke-width="1.8"/>'
       f'<circle class="lamp" cx="{bx+13:.0f}" cy="{by+2:.0f}" r="2.6" fill="#e5484d"/>'
       f'<rect x="{bx:.0f}" y="{by-4:.0f}" width="4" height="15" rx="1" fill="{V}"/>'
       f'<g class="arm"><rect x="{bx-27:.0f}" y="{by-2:.0f}" width="31" height="5" rx="2.5" fill="#fff" stroke="{V}" stroke-width="1.4"/><path d="{stripes}" fill="#e5484d"/></g>'
       f'<path d="M{bx-24:.0f} {by+11:.0f}h44" stroke="{G}" stroke-width="2" stroke-linecap="round"/>')
doc=(f'<g class="doc"><rect x="{bx-32:.0f}" y="{by-128:.0f}" width="62" height="78" rx="9" fill="#fff" stroke="{V}" stroke-width="2.2"/>'
     f'<path d="M{bx-21:.0f} {by-112:.0f}h40M{bx-21:.0f} {by-100:.0f}h40M{bx-21:.0f} {by-88:.0f}h24" stroke="{G}" stroke-width="5" stroke-linecap="round"/>'
     f'<circle cx="{bx+24:.0f}" cy="{by-54:.0f}" r="17" fill="{B}"/><path class="tick" d="M{bx+16:.0f} {by-54:.0f}l6 6 11-12" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></g>')
pb,pp,pd,pc=pulses(EU_CITIES,(KX,KY))
css+=pc
sm=mp[int(len(mp)*0.45)]
body=(f'{pb}<path class="rb" d="{main}" style="opacity:.45;stroke-width:2"/>{pp}{pd}<path id="cm" d="{main}" fill="none"/>'
      f'<circle class="dt" cx="{o[0]:.0f}" cy="{o[1]:.0f}" r="6"/>{KYIV}'
      f'<g class="anim"><g class="tv">{truck()}</g><animateMotion dur="{T}s" repeatCount="indefinite" rotate="auto" calcMode="spline" keyPoints="0;{fs:.4f};{fs:.4f};1;1" keyTimes="0;{k1:.3f};{k2:.3f};{k3:.3f};1" keySplines="{EASE};0 0 1 1;{EASE};0 0 1 1"><mpath href="#cm"/></animateMotion></g>'
      f'<g class="static" transform="translate({sm[0]:.0f},{sm[1]:.0f}) rotate(-8)">{truck()}</g>{badge}{doc}')
open('map-customs.svg','w').write(page('Митне оформлення вантажу на кордоні під час перевезення з Європи в Україну',css,body))
print('customs T',T,'border',round(bx),round(by))

# ---------- 2) СКЛАД: склад по центру карти, до 6 вантажів зʼїжджаються з усіх куточків Європи й стають на стелаж ----------
T=13
CX,CY=500,318                                  # центр кадру (схематично, без привʼязки до міста)
BW,BH=190,150                                  # будівля складу
bx0,by0=CX-BW/2,CY-BH/2+14
roof=f'M{bx0-14:.0f} {by0:.0f}L{CX:.0f} {by0-52:.0f}L{bx0+BW+14:.0f} {by0:.0f}Z'
slots=[(bx0+22,by0+82),(bx0+75,by0+82),(bx0+128,by0+82),(bx0+22,by0+28),(bx0+75,by0+28),(bx0+128,by0+28)]
SRC=[(-8.6,41.2),(-1.5,53.0),(10.7,59.9),(12.5,41.9),(28.97,41.0),(32.0,49.3)]   # Порту, Англія, Осло, Рим, Стамбул, Україна
dep=[i*1.4 for i in range(6)]; TR_=2.6        # старт і тривалість руху кожного вантажу
def mini(sc=1.0):
    return (f'<g transform="scale({sc}) translate(-19,-14)"><rect x="0" y="22" width="38" height="5" rx="1.5" fill="#b98b5a"/>'
            f'<rect x="3" y="0" width="32" height="22" rx="3" fill="{BS}" stroke="{V}" stroke-width="2"/><path d="M3 8h32M19 0v22" stroke="{V}" stroke-width="1.4" opacity=".35"/></g>')
paths=[];movers=[];css=[];ends=[]
for i,src in enumerate(SRC):
    ox,oy=P(*src); sx,sy=slots[i]; tx,ty=sx+22,sy+18      # ціль — центр комірки стелажа
    d,_=qcurve((ox,oy),(tx,ty),0.16)
    paths.append(f'<path class="rb" d="{d}"/><path id="w{i}" d="{d}" fill="none"/>')
    a=dep[i]/T; b=(dep[i]+TR_)/T
    movers.append(f'<g class="anim"><g class="mv{i}">{mini(1.05)}</g><animateMotion dur="{T}s" repeatCount="indefinite" calcMode="spline" keyPoints="0;0;1;1" keyTimes="0;{a:.3f};{b:.3f};1" keySplines="0 0 1 1;{EASE};0 0 1 1"><mpath href="#w{i}"/></animateMotion></g>'
                  f'<circle class="dt" cx="{ox:.0f}" cy="{oy:.0f}" r="5"/><circle class="dr sd{i}" cx="{ox:.0f}" cy="{oy:.0f}" r="5"/>')
    css.append(f'.mv{i}{{opacity:0;animation:mv{i} {T}s linear infinite}}@keyframes mv{i}{{0%,{g(a)}{{opacity:0}}{g(a+0.01)},{g(b-0.005)}{{opacity:1}}{g(b)},100%{{opacity:0}}}}'
               f'.sl{i}{{opacity:0;animation:sl{i} {T}s ease-out infinite}}@keyframes sl{i}{{0%,{g(b-0.004)}{{opacity:0;transform:translateY(-6px)}}{g(b+0.02)},94%{{opacity:1;transform:none}}98%,100%{{opacity:0}}}}'
               f'.sd{i}{{animation:sd{i} {T}s ease-out infinite}}@keyframes sd{i}{{0%,{g(a)}{{transform:scale(1);opacity:0}}{g(a+0.005)}{{opacity:.8}}{g(a+0.08)},100%{{transform:scale(3);opacity:0}}}}')
    ends.append(f'<g transform="translate({tx:.0f},{ty:.0f})"><g class="sl{i}">{mini(1.05)}</g></g>')
bld=(f'<ellipse cx="{CX}" cy="{by0+BH+6:.0f}" rx="{BW/2+30:.0f}" ry="12" fill="{V}" opacity=".08"/>'
     f'<path d="{roof}" fill="{V}"/>'
     f'<rect x="{bx0:.0f}" y="{by0:.0f}" width="{BW}" height="{BH}" rx="6" fill="#fff" stroke="{V}" stroke-width="3"/>'
     f'<g fill="none" stroke="{V}" stroke-width="3.2" stroke-linecap="round"><path d="M{bx0+16:.0f} {by0+BH-8:.0f}V{by0+14:.0f}M{bx0+BW-16:.0f} {by0+BH-8:.0f}V{by0+14:.0f}"/>'
     f'<path d="M{bx0+12:.0f} {by0+128:.0f}h{BW-24}M{bx0+12:.0f} {by0+74:.0f}h{BW-24}"/></g>'
     f'<path d="M{bx0+69:.0f} {by0+20:.0f}v106M{bx0+122:.0f} {by0+20:.0f}v106" stroke="{V}" stroke-width="1.6" opacity=".25"/>'
     f'<circle class="whub" cx="{CX}" cy="{by0-18:.0f}" r="9" fill="{B}"/><circle cx="{CX}" cy="{by0-18:.0f}" r="8" fill="#fff" stroke="{B}" stroke-width="3"/>')
css=PCSS+''.join(css)+(f'.whub{{transform-box:fill-box;transform-origin:center;animation:hub 2.6s ease-out infinite}}')
body=f'{"".join(paths)}{bld}{"".join(ends)}{"".join(movers)}'
open('map-warehouse.svg','w').write(page('Складські послуги Sibway Logistics: вантажі з усієї Європи зберігаються на складі',css,body))

# ---------- 3) АУДИТ: спершу заплутаний маршрут, потім після аудиту — прямий і чіткий ----------
T=14
tang=[P(*c) for c in [(9.99,53.55),(11.58,48.14),(14.42,50.08),(18.65,54.35),(19.04,47.5),(21.01,52.23),(26.1,44.43),(30.52,50.45)]]
td,acc=smooth(tang,1/5); TL=acc[-1]
hx,hy=tang[0]; sd,spts=qcurve((hx,hy),(KX,KY),0.1); SL=plen(spts)
css=f'''
.tgm{{stroke-dasharray:{TL+20:.0f};stroke-dashoffset:{TL+20:.0f};animation:tgm {T}s ease-in-out infinite}}@keyframes tgm{{0%{{stroke-dashoffset:{TL+20:.0f}}}26%,100%{{stroke-dashoffset:0}}}}
.tg{{animation:tg {T}s ease-in-out infinite}}@keyframes tg{{0%,32%{{opacity:1}}42%,100%{{opacity:.1}}}}
.wp{{opacity:0;animation:wp {T}s ease-out infinite}}@keyframes wp{{0%,1%{{opacity:0}}30%{{opacity:1}}32%{{opacity:1}}42%,100%{{opacity:.15}}}}
.st{{stroke-dasharray:{SL+20:.0f};stroke-dashoffset:{SL+20:.0f};animation:st {T}s ease-in-out infinite}}@keyframes st{{0%,38%{{stroke-dashoffset:{SL+20:.0f}}}50%,100%{{stroke-dashoffset:0}}}}
.tv{{opacity:0;animation:tv {T}s linear infinite}}@keyframes tv{{0%,48%{{opacity:0}}51%,93%{{opacity:1}}97%,100%{{opacity:0}}}}
.c1{{animation:c1 {T}s steps(1) infinite}}@keyframes c1{{0%,37%{{opacity:1}}37.1%,100%{{opacity:0}}}}
.c2{{animation:c2 {T}s steps(1) infinite}}@keyframes c2{{0%,37%{{opacity:0}}37.1%,97%{{opacity:1}}97.1%,100%{{opacity:0}}}}
.all{{animation:all {T}s linear infinite}}@keyframes all{{0%{{opacity:0}}2%,96%{{opacity:1}}100%{{opacity:0}}}}'''
# вузли заплутаного маршруту зʼявляються по мірі прорисовки
wp=''.join(f'<circle class="wp{j}" cx="{x:.0f}" cy="{y:.0f}" r="5.5" fill="#fff" stroke="#8b94a5" stroke-width="2.6"/>' for j,(x,y) in enumerate(tang[1:-1],1))
css+=''.join(f'.wp{j}{{opacity:0;animation:wp{j} {T}s ease-out infinite}}@keyframes wp{j}{{0%,{acc[j]/TL*26:.1f}%{{opacity:0;transform:scale(.4)}}{acc[j]/TL*26+2:.1f}%,32%{{opacity:1;transform:none}}42%,100%{{opacity:.15}}}}' for j in range(1,len(tang)-1))
css+='[class^=wp]{transform-box:fill-box;transform-origin:center}'

cx0,cy0=hx+10,hy-78
chipc=(f'<g class="c1">{chip(cx0,cy0,"До аудиту")}</g>'
       f'<g class="c2"><g transform="translate({cx0:.0f},{cy0:.0f})"><rect x="-86" y="-21" width="172" height="42" rx="21" fill="{B}"/><text y="7" text-anchor="middle" style="font:700 20px {FONT};fill:#fff">Після аудиту</text></g></g>')
body=(f'<defs><mask id="tm"><path d="{td}" fill="none" stroke="#fff" stroke-width="14" class="tgm"/></mask></defs>'
      f'<g class="all"><g class="tg"><path d="{td}" mask="url(#tm)" fill="none" stroke="#8b94a5" stroke-width="3.6" stroke-dasharray="2 10" stroke-linecap="round"/>{wp}</g>'
      f'<path class="st" d="{sd}" fill="none" stroke="{B}" stroke-width="5" stroke-linecap="round"/></g><path id="am" d="{sd}" fill="none"/>'
      f'<g transform="translate({hx:.0f},{hy:.0f})"><circle r="16" fill="#fff" stroke="{V}" stroke-width="3"/><path d="M-8 6v-9l8-6 8 6v9z" fill="{V}"/></g>{KYIV}{chipc}'
      f'<g class="anim"><g class="tv">{truck()}</g><animateMotion dur="{T}s" repeatCount="indefinite" rotate="auto" calcMode="spline" keyPoints="0;0;1;1" keyTimes="0;0.5;0.93;1" keySplines="0 0 1 1;{EASE};0 0 1 1"><mpath href="#am"/></animateMotion></g>'
      f'<g class="static" transform="translate({(hx+KX)/2:.0f},{(hy+KY)/2-34:.0f}) rotate(8)">{truck()}</g>')
open('map-audit.svg','w').write(page('Логістичний аудит: заплутаний маршрут стає прямим і чітким',css,body))
print('ok')
