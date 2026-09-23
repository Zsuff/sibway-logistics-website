# Анімовані ілюстрації Sibway (customs / warehouse / audit / hub). Кольори бренду.
V='#29265b'; B='#189cd9'; BS='#e8f6fc'; VS='#eeeef6'; G='#d9dde3'
from semi import semi
TRUCK=semi(V,B,BS)
RM='@media (prefers-reduced-motion:reduce){*{animation:none!important}}'
FONT='font-family:Manrope,Inter,Arial,sans-serif'
def svg(w,h,title,css,body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="t"><title id="t">{title}</title><style>{css}{RM}</style>{body}</svg>'

# 1) Митниця (шлагбаум вгору, авто позаду поста): вантажівка під'їжджає, документи перевірено, шлагбаум піднімається
customs=svg(800,500,'Митне оформлення вантажу в межах перевезення',f'''
.truck{{animation:drive 9s ease-in-out infinite}}
@keyframes drive{{0%{{transform:translate(-260px,322px) scale(2.6);opacity:0}}8%{{opacity:1}}30%,58%{{transform:translate(22px,322px) scale(2.6)}}88%{{transform:translate(760px,322px) scale(2.6);opacity:1}}94%,100%{{transform:translate(860px,322px) scale(2.6);opacity:0}}}}
.arm{{transform-origin:470px 318px;animation:arm 9s ease-in-out infinite}}
@keyframes arm{{0%,46%{{transform:rotate(0)}}54%,80%{{transform:rotate(78deg)}}90%,100%{{transform:rotate(0)}}}}
.doc{{transform-origin:360px 170px;animation:doc 9s ease-in-out infinite;opacity:0}}
@keyframes doc{{0%,30%{{opacity:0;transform:translateY(20px) scale(.8)}}36%,54%{{opacity:1;transform:none}}62%,100%{{opacity:0;transform:translateY(-20px)}}}}
.tick{{stroke-dasharray:60;stroke-dashoffset:60;animation:tick 9s ease-in-out infinite}}
@keyframes tick{{0%,40%{{stroke-dashoffset:60}}47%,100%{{stroke-dashoffset:0}}}}
.lamp{{animation:lamp 9s steps(1) infinite}}@keyframes lamp{{0%,46%{{fill:#e5484d}}47%,88%{{fill:#2fb37a}}89%,100%{{fill:#e5484d}}}}''',
f'''<rect x="0" y="392" width="800" height="6" rx="3" fill="{G}"/>
<path d="M0 420h800" stroke="{G}" stroke-width="3" stroke-dasharray="26 22"/>
<g class="truck">{TRUCK}</g>
<rect x="478" y="236" width="86" height="156" rx="10" fill="{VS}" stroke="{V}" stroke-width="3"/>
<rect x="494" y="258" width="54" height="40" rx="6" fill="#fff" stroke="{V}" stroke-width="3"/>
<circle class="lamp" cx="521" cy="326" r="9" fill="#e5484d"/>
<rect x="462" y="306" width="18" height="86" rx="4" fill="{V}"/>
<g class="arm"><rect x="250" y="310" width="220" height="16" rx="8" fill="#fff" stroke="{V}" stroke-width="3"/>
<path d="M280 312h26l-12 12h-26zM335 312h26l-12 12h-26zM390 312h26l-12 12h-26zM445 312h14l-12 12h-14z" fill="#e5484d"/></g>
<g class="doc"><rect x="300" y="96" width="120" height="150" rx="12" fill="#fff" stroke="{V}" stroke-width="3"/>
<path d="M322 130h76M322 152h76M322 174h52" stroke="{G}" stroke-width="8" stroke-linecap="round"/>
<circle cx="400" cy="222" r="30" fill="{B}"/><path class="tick" d="M386 222l10 10 20-22" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>''')

# 2) Склад: палети по черзі стають на стелаж
pal=lambda x,y,c: f'<g><rect x="{x}" y="{y+52}" width="96" height="10" rx="2" fill="#b98b5a"/><rect x="{x+6}" y="{y}" width="84" height="52" rx="5" fill="{c}" stroke="{V}" stroke-width="2.5"/><path d="M{x+6} {y+18}h84M{x+48} {y}v52" stroke="{V}" stroke-width="2" opacity=".35"/></g>'
slots=[(250,256),(380,256),(510,256),(250,146),(380,146),(510,146)]
cols=[BS,VS,BS,VS,BS,VS]
wcss=''.join(f'.p{i}{{animation:p{i} 8.5s ease-out infinite}}@keyframes p{i}{{0%,{5+i*12}%{{transform:translate({-x-200}px,0);opacity:0}}{7+i*12}%{{opacity:1}}{13+i*12}%,90%{{transform:none;opacity:1}}96%,100%{{transform:none;opacity:0}}}}' for i,(x,y) in enumerate(slots))
warehouse=svg(800,500,'Складське зберігання палетних вантажів',wcss,
f'''<rect x="0" y="392" width="800" height="6" rx="3" fill="{G}"/>
<g fill="none" stroke="{V}" stroke-width="6" stroke-linecap="round"><path d="M232 392V100M628 392V100"/><path d="M226 330h408M226 220h408M226 110h408"/></g>
<path d="M362 110v282M492 110v282" stroke="{V}" stroke-width="3" opacity=".25"/>
{''.join(f'<g class="p{i}">{pal(x,y,cols[i])}</g>' for i,(x,y) in enumerate(slots))}''')

# 3) Аудит (старт одразу, фура їде ~4 с): заплутаний маршрут перетворюється на прямий
tangled='M120 330 C 170 140, 260 440, 310 250 S 420 90, 460 300 S 560 420, 600 210 S 660 160, 680 250'
straight='M120 330 C 300 330, 500 250, 680 250'
audit=svg(800,500,'Логістичний аудит: оптимізація маршруту',f'''
.tg{{animation:tg 6s ease-in-out infinite}}@keyframes tg{{0%,6%{{opacity:1}}20%,100%{{opacity:.12}}}}
.st{{stroke-dasharray:700;stroke-dashoffset:700;animation:st 6s ease-in-out infinite}}@keyframes st{{0%,6%{{stroke-dashoffset:700}}24%,100%{{stroke-dashoffset:0}}}}
.tr{{opacity:0;animation:trf 6s linear infinite}}@keyframes trf{{0%,22%{{opacity:0}}25%,93%{{opacity:1}}97%,100%{{opacity:0}}}}''',
f'''<path class="tg" d="{tangled}" fill="none" stroke="#9aa3b2" stroke-width="5" stroke-dasharray="3 12" stroke-linecap="round"/>
<path class="st" d="{straight}" fill="none" stroke="{B}" stroke-width="7" stroke-linecap="round"/>
<path id="sp" d="{straight}" fill="none"/>
<g class="tr"><g transform="scale(1.25) translate(-42,-14)">{TRUCK}</g><animateMotion dur="6s" repeatCount="indefinite" rotate="auto" keyPoints="0;0;1;1" keyTimes="0;0.24;0.93;1" calcMode="linear"><mpath href="#sp"/></animateMotion></g>
<g><circle cx="120" cy="330" r="30" fill="#fff" stroke="{V}" stroke-width="4"/><path d="M106 340v-16l14-10 14 10v16z" fill="{V}"/></g>
<g><circle cx="680" cy="250" r="30" fill="{V}"/><path d="M670 236v30M670 238h22l-6 8 6 8h-22" fill="#fff" stroke="#fff" stroke-width="3" stroke-linejoin="round"/></g>''')

# 4) Головна, блок «Зовнішній логіст»: хаб — перевезення, митниця, склад, аудит навколо Sibway
icons={
 'Перевезення':f'<g transform="translate(-45,-16) scale(1.07)">{TRUCK}</g>',
 'Митне оформлення':f'<g><rect x="-20" y="-26" width="40" height="52" rx="6" fill="#fff" stroke="{V}" stroke-width="3"/><path d="M-11 -12h22M-11 -2h22M-11 8h14" stroke="{G}" stroke-width="4" stroke-linecap="round"/></g>',
 'Склад':f'<g><path d="M-30 24v-30l30-20 30 20v30z" fill="#fff" stroke="{V}" stroke-width="3" stroke-linejoin="round"/><rect x="-12" y="4" width="24" height="20" fill="{BS}" stroke="{V}" stroke-width="2.5"/></g>',
 'Аудит':f'<g><rect x="-26" y="-22" width="52" height="44" rx="6" fill="#fff" stroke="{V}" stroke-width="3"/><path d="M-16 12l10-12 10 6 12-16" fill="none" stroke="{B}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></g>'}
pos=[(170,130),(630,130),(170,370),(630,370)]
cx,cy=400,250
lines=''.join(f'<path d="M{cx} {cy}L{x} {y}" class="ln" style="animation-delay:{-i*0.4}s"/>' for i,(x,y) in enumerate(pos))
nodes=''.join(f'<g transform="translate({x},{y})"><circle r="62" fill="{BS if i%2==0 else VS}"/><circle r="62" class="ring" style="animation-delay:{i*1.2}s"/>{ic}<text y="92" text-anchor="middle" class="lbl">{name}</text></g>' for i,((x,y),(name,ic)) in enumerate(zip(pos,icons.items())))
hub=svg(800,500,'Sibway Logistics — перевезення, митне оформлення, склад і аудит в одному місці',f'''
.ln{{stroke:{B};stroke-width:4;stroke-dasharray:3 12;stroke-linecap:round;fill:none;animation:dash 1.4s linear infinite}}@keyframes dash{{to{{stroke-dashoffset:-30}}}}
.ring{{fill:none;stroke:{B};stroke-width:3;transform-box:fill-box;transform-origin:center;opacity:0;animation:ring 4.8s ease-out infinite}}@keyframes ring{{0%{{transform:scale(1);opacity:.6}}40%,100%{{transform:scale(1.35);opacity:0}}}}
.lbl{{{FONT};font-weight:700;font-size:20px;fill:{V}}}
.core{{transform-box:fill-box;transform-origin:center;animation:core 3s ease-in-out infinite}}@keyframes core{{50%{{transform:scale(1.06)}}}}''',
f'''{lines}{nodes}<g class="core"><circle cx="{cx}" cy="{cy}" r="72" fill="{V}"/><text x="{cx}" y="{cy+8}" text-anchor="middle" style="{FONT};font-weight:800;font-size:26px;fill:#fff">Sibway</text></g>''')
for n,s in [('illus-customs',customs),('illus-warehouse',warehouse),('illus-audit',audit),('illus-hub',hub)]:
    open(n+'.svg','w').write(s)
print('ok')
