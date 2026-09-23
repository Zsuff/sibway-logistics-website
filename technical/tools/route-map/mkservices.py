# «Наші послуги»: увесь ланцюжок на одному маршруті — аудит → перевезення → склад → митниця → Україна.
exec(open('mkmapanim.py').read().split('# ---------- 1)')[0])
T=15
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
ci=next(i for i,p in enumerate(mp) if inside(*p,big))
def at_len(f):   # індекс точки за часткою довжини
    L=f*LT; return min(range(len(cum)),key=lambda i:abs(cum[i]-L))
def ic(kind,col):
    if kind=='audit': return f'<rect x="-10" y="-9" width="20" height="18" rx="3" fill="none" stroke="{col}" stroke-width="2.2"/><path d="M-6 4l4-5 4 3 5-7" fill="none" stroke="{col}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>'
    if kind=='truck': return f'<g transform="translate(-13,-8) scale(.31)">{semi(col,col,"#fff",col)}</g>'
    if kind=='wh': return f'<path d="M-11 9v-10l11-8 11 8v10z" fill="none" stroke="{col}" stroke-width="2.2" stroke-linejoin="round"/><rect x="-5" y="1" width="10" height="8" fill="none" stroke="{col}" stroke-width="2"/>'
    return f'<rect x="3" y="-9" width="6" height="18" rx="1.5" fill="{col}"/><rect x="-12" y="-4" width="17" height="4" rx="2" fill="{col}"/><path d="M-12 9h22" stroke="{col}" stroke-width="2" stroke-linecap="round"/>'
t0,t1=0.05,0.9                                  # фура рухається рівномірно між t0 і t1
ST=[('audit','Аудит',0),('truck','Перевезення',at_len(0.24)),('wh','Склад',at_len(0.52)),('cust','Митниця',ci)]
css=[f'.tv{{animation:tv {T}s linear infinite}}@keyframes tv{{0%,{g(t0-0.02)}{{opacity:0}}{g(t0)},{g(t1)}{{opacity:1}}{g(t1+0.03)},100%{{opacity:0}}}}']
st=[]
for k,(kind,label,idx) in enumerate(ST):
    x,y=mp[idx]; f=cum[idx]/LT; a=max(t0+(t1-t0)*f,0.03)
    w=len(label)*10.5+30; dy=44 if k%2==0 else -44
    st.append(f'<circle class="ring r{k}" cx="{x:.0f}" cy="{y:.0f}" r="22"/>'
              f'<g transform="translate({x:.0f},{y:.0f})"><circle r="22" fill="#fff" stroke="{V}" stroke-width="2.4"/>{ic(kind,V)}'
              f'<g class="on{k}"><circle r="22" fill="{B}" stroke="{B}" stroke-width="2.4"/>{ic(kind,"#fff")}</g></g>'
              f'<g transform="translate({x:.0f},{y+dy:.0f})"><rect x="{-w/2:.0f}" y="-16" width="{w:.0f}" height="32" rx="16" class="lw"/><text y="6" text-anchor="middle" style="font:700 16px {FONT};fill:{V}">{label}</text>'
              f'<g class="on{k}"><rect x="{-w/2:.0f}" y="-16" width="{w:.0f}" height="32" rx="16" fill="{B}"/><text y="6" text-anchor="middle" style="font:700 16px {FONT};fill:#fff">{label}</text></g></g>')
    css.append(f'.on{k}{{opacity:0;animation:on{k} {T}s ease-out infinite}}@keyframes on{k}{{0%,{g(a-0.005)}{{opacity:0}}{g(a+0.02)},{g(t1+0.03)}{{opacity:1}}{g(t1+0.07)},100%{{opacity:0}}}}'
               f'.r{k}{{animation:r{k} {T}s ease-out infinite}}@keyframes r{k}{{0%,{g(a-0.005)}{{transform:scale(1);opacity:0}}{g(a)}{{opacity:.8}}{g(a+0.08)},100%{{transform:scale(2.3);opacity:0}}}}')
css.append(f'.ring{{fill:none;stroke:{B};stroke-width:2.5;transform-box:fill-box;transform-origin:center;opacity:0}}'
           f'.pr{{stroke-dasharray:{LT+10:.0f};stroke-dashoffset:{LT+10:.0f};animation:pr {T}s linear infinite}}@keyframes pr{{0%,{g(t0)}{{stroke-dashoffset:{LT+10:.0f};opacity:1}}{g(t1)}{{stroke-dashoffset:0;opacity:1}}{g(t1+0.05)},100%{{stroke-dashoffset:0;opacity:0}}}}')
body=(f'<path class="rb" d="{main}" style="opacity:.5;stroke-width:2.2"/><path class="pr" d="{main}" fill="none" stroke="{B}" stroke-width="4" stroke-linecap="round"/><path id="sm" d="{main}" fill="none"/>'
      f'{KYIV}'
      f'<g class="anim"><g class="tv">{truck()}</g><animateMotion dur="{T}s" repeatCount="indefinite" rotate="auto" calcMode="linear" keyPoints="0;0;1;1" keyTimes="0;{t0};{t1};1"><mpath href="#sm"/></animateMotion></g>'
      f'<g class="static" transform="translate({mp[70][0]:.0f},{mp[70][1]:.0f}) rotate(-6)">{truck()}</g>'+''.join(st))
open('map-services.svg','w').write(page('Послуги Sibway Logistics на одному маршруті: аудит, перевезення, склад, митне оформлення, доставка в Україну',''.join(css),body))
print('ok',T)
