# 横並べ比較: sheet.py out.png label1=img1[:y0:y1] label2=img2[:y0:y1] ...  (y は CSS px, 画像は DPR2 想定。幅390に縮小)
import sys
from PIL import Image, ImageDraw, ImageFont
out=sys.argv[1]; items=[]
F=ImageFont.truetype('/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc',22)
for a in sys.argv[2:]:
    lab,spec=a.split('=',1); parts=spec.split(':'); im=Image.open(parts[0]).convert('RGB')
    s=im.width/390
    if len(parts)==3: im=im.crop((0,int(float(parts[1])*s),im.width,min(im.height,int(float(parts[2])*s))))
    im=im.resize((390,int(im.height/s)))
    items.append((lab,im))
H=max(i.height for _,i in items)+40; W=len(items)*390+(len(items)-1)*16
o=Image.new('RGB',(W,H),'#d9d9d9'); d=ImageDraw.Draw(o)
for k,(lab,im) in enumerate(items):
    x=k*406; d.text((x+6,8),lab,fill='#111',font=F); o.paste(im,(x,40))
o.save(out); print(out,o.size)
