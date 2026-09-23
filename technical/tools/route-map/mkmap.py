import json, math
T=json.load(open('countries-50m.json'))
sc,tr=T['transform']['scale'],T['transform']['translate']
arcs=[]
for a in T['arcs']:
    x=y=0; pts=[]
    for dx,dy in a:
        x+=dx; y+=dy; pts.append((x*sc[0]+tr[0], y*sc[1]+tr[1]))
    arcs.append(pts)
def arc(i): return arcs[i] if i>=0 else arcs[~i][::-1]
def ring(r):
    pts=[]
    for i in r:
        a=arc(i); pts.extend(a if not pts else a[1:])
    return pts
# projection: Lambert azimuthal equal-area centred on Europe
lon0,lat0=math.radians(22),math.radians(51)
def proj(lon,lat):
    l,p=math.radians(lon),math.radians(lat)
    k=math.sqrt(2/(1+math.sin(lat0)*math.sin(p)+math.cos(lat0)*math.cos(p)*math.cos(l-lon0)))
    return k*math.cos(p)*math.sin(l-lon0), k*(math.cos(lat0)*math.sin(p)-math.sin(lat0)*math.cos(p)*math.cos(l-lon0))
# view window in projected coords: set by lon/lat corners
W,H=800,560
x0,y0=proj(2,57)[0],proj(22,59.5)[1]   # left/top
x1,y1=proj(41,44)[0],proj(22,43.3)[1]  # right/bottom
sx=W/(x1-x0); sy=H/(y0-y1); s=min(sx,sy)
def P(lon,lat):
    x,y=proj(lon,lat); return ((x-x0)*s, (y0-y)*s)
def dp(pts,eps):
    if len(pts)<3: return pts
    import math
    keep=[False]*len(pts); keep[0]=keep[-1]=True; st=[(0,len(pts)-1)]
    while st:
        a,b=st.pop(); ax,ay=pts[a]; bx,by=pts[b]; dx,dy=bx-ax,by-ay; L=math.hypot(dx,dy) or 1e-9
        m=-1; mi=None
        for i in range(a+1,b):
            px,py=pts[i]; d=abs(dy*px-dx*py+bx*ay-by*ax)/L if L>1e-9 else math.hypot(px-ax,py-ay)
            if d>m: m=d; mi=i
        if mi is not None and m>eps: keep[mi]=True; st+= [(a,mi),(mi,b)]
    return [p for p,k in zip(pts,keep) if k]
geoms=T['objects']['countries']['geometries']
# Крим — Україна: переносимо полігон Криму з геометрії 643 до 804
_ru=[g for g in geoms if g.get('id')=='643'][0]; _ua=[g for g in geoms if g.get('id')=='804'][0]
def _bbox(poly):
    pts=[p for idx in poly[0] for p in (arcs[idx] if idx>=0 else arcs[~idx])]
    xs=[p[0] for p in pts]; ys=[p[1] for p in pts]; return min(xs),max(xs),min(ys),max(ys)
_crimea=[p for p in _ru['arcs'] if (lambda b: b[0]>32 and b[1]<37 and b[2]>44 and b[3]<46.5)(_bbox(p))]
assert len(_crimea)==1, len(_crimea)
_ru['arcs']=[p for p in _ru['arcs'] if p not in _crimea]
if _ua['type']=='Polygon': _ua['type']='MultiPolygon'; _ua['arcs']=[_ua['arcs']]
_ua['arcs']+= _crimea
paths={}
for g in geoms:
    polys=g['arcs'] if g['type']=='MultiPolygon' else ([g['arcs']] if g['type']=='Polygon' else [])
    d=[]
    for poly in polys:
        for r in poly:
            pts=[P(*pt) for pt in ring(r)]
            xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
            if max(xs)<-50 or min(xs)>W+50 or max(ys)<-50 or min(ys)>H+50: continue
            out=[(round(x),round(y)) for x,y in dp(pts,1.1)]
            out=[p for i,p in enumerate(out) if i==0 or p!=out[i-1]]
            if len(out)<3: continue
            d.append('M'+'L'.join(f'{x},{y}' for x,y in out)+'Z')
    if d: paths[g.get('id') or g.get('properties',{}).get('name','x')]=''.join(d)
json.dump({'paths':paths},open('eu_paths.json','w'))
print(len(paths), sum(len(v) for v in paths.values()))
# representative points
for n,(lo,la) in {'DE':(10.3,51.0),'PL':(19.2,52.1),'UA':(31.3,49.2),'CZ':(15.4,49.8),'RO':(24.9,45.9)}.items():
    print(n,[round(v) for v in P(lo,la)])
