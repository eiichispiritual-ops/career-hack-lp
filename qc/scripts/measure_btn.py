# 画像ボタンの実測: CTAリンク領域を full.png(DPR2) から切り出し、緑ボタン本体の高さ/色/角丸/下影を画素で測る
import json, sys, glob
from PIL import Image
from collections import Counter
def isgreen(p): r,g,b=p[:3]; return g>150 and g-r>60 and g-b>40
def measure(name):
    d=json.load(open(f'specs/{name}.json')); im=Image.open(f'shots/comp_{name}/full.png').convert('RGB')
    res=[]
    for c in d['ctas'][:6]:
        if c['h']<30 or c['y']<0 or c['y']*2>=im.height: continue
        x0,y0=0,c['y']*2; box=im.crop((0,max(0,y0-20),780,min(im.height,y0+c['h']*2+20)))
        W,H=box.size; px=box.load()
        # 中央列で緑の縦ラン
        best=(0,0,0)
        for x in range(W//4, 3*W//4, 7):
            run=0;start=0
            for y in range(H):
                if isgreen(px[x,y]):
                    if run==0:start=y
                    run+=1
                    if run>best[0]: best=(run,start,x)
                else: run=0
        h,top,x=best
        if h<20: continue
        midy=top+h//2
        row=[i for i in range(W) if isgreen(px[i,midy])]; left,right=min(row),max(row)
        # 角丸: 上端から左端の緑開始位置がどれだけ内側か
        ytop=top+1; rowt=[i for i in range(W) if isgreen(px[i,ytop])]
        rad=(min(rowt)-left) if rowt else 0
        cols=Counter(px[i,midy] for i in range(left+40,right-40,3) if isgreen(px[i,midy])).most_common(1)[0][0]
        under=px[x,min(H-1,top+h+3)]
        res.append(dict(text=c['text'][:16], y=c['y'], body_h=round(h/2), body_w=round((right-left)/2), radius_px_est=round(rad/2),
                        color='#%02x%02x%02x'%cols, below_color='#%02x%02x%02x'%under))
        box.save(f'shots/comp_{name}/btn_{c["y"]}.png')
    return res
out={}
for n in sys.argv[1:]: out[n]=measure(n); print(n, out[n][:3])
json.dump(out,open('specs/_buttons_pixel.json','w'),ensure_ascii=False,indent=1)
