# セクション単位の横並べ比較（自社 | 競合A | 競合B | 競合C、同縮尺 390px幅）
# usage: make_compare.py <tag(r1|final)> <outprefix(round1|final)>
import sys, json
from PIL import Image, ImageDraw, ImageFont
tag, pre = sys.argv[1], sys.argv[2]
F = ImageFont.truetype('/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc', 20)
S = f'shots/{tag}_riko_390'; secs = json.load(open(f'{S}/check.json'))['secs']
C = lambda n: f'shots/comp_{n}/full.png'
def crop(path, y0, y1, scale=1.0):
    im = Image.open(path).convert('RGB'); s = im.width / 390
    im = im.crop((0, int(y0 * s), im.width, min(im.height, int(y1 * s))))
    return im.resize((int(390 * scale), int(im.height / s * scale)))
def sheet(out, items, scale=1.0):
    ims = [(l, crop(p, a, b, scale) if a is not None else Image.open(p).convert('RGB').resize((int(390*scale), int(Image.open(p).height/2*scale)))) for l, p, a, b in items]
    W = sum(i.width for _, i in ims) + 16 * (len(ims) - 1); H = max(i.height for _, i in ims) + 34
    o = Image.new('RGB', (W, H), '#d6d6d6'); d = ImageDraw.Draw(o); x = 0
    for l, i in ims:
        d.text((x + 6, 6), l, fill='#111', font=F); o.paste(i, (x, 34)); x += i.width + 16
    o.save(f'compare/{out}'); print(out, o.size)
me = lambda a, b: ('自社 キャリアハック', f'{S}/full.png', a, b)
sheet(f'{pre}_fv.png', [me(0, 844), ('事務ナビ', C('c3_jimunavi'), 0, 844), ('ゆるキャリ', C('c6_yuru'), 0, 844), ('キャリアスイッチ', C('c2_careerswitch'), 0, 844)])
b = secs['cta-fv']
sheet(f'{pre}_button.png', [me(b[0] - 6, b[1] + 6), ('キャリカミ', C('c1_careercoming'), 600, 770), ('キャリアスイッチ', C('c2_careerswitch'), 615, 760), ('事務ナビ', C('c3_jimunavi'), 560, 720)], scale=1.6)
sheet(f'{pre}_mid.png', [me(secs['worry'][0], secs['reasons'][1]), ('事務ナビ', C('c3_jimunavi'), 844, 3100), ('ゆるキャリ', C('c6_yuru'), 700, 2950), ('キャリアスイッチ', C('c2_careerswitch'), 1300, 3600)], scale=.6)
sheet(f'{pre}_flow_gift.png', [me(secs['jobs'][0], secs['flow'][1]), ('事務ナビ', C('c3_jimunavi'), 2300, 4100), ('ゆるキャリ', C('c6_yuru'), 2950, 3300), ('キャリアスイッチ', C('c2_careerswitch'), 6950, 8800)], scale=.6)
sheet(f'{pre}_faq_footer.png', [me(secs['faq'][0], secs['privacy'][1]), ('事務ナビ', C('c3_jimunavi'), 6100, 8440), ('ゆるキャリ', C('c6_yuru'), 3300, 4321), ('キャリアスイッチ', C('c2_careerswitch'), 8900, 10612)], scale=.6)
sheet(f'{pre}_sticky.png', [('自社 キャリアハック', f'{S}/sticky.png', None, None), ('キャリカミ', 'shots/comp_c1_careercoming/sticky.png', None, None), ('事務ナビ', 'shots/comp_c3_jimunavi/sticky.png', None, None), ('ゆるキャリ', 'shots/comp_c6_yuru/sticky.png', None, None)], scale=.8)
# ロゴ・ヘッダー（上部 90px を拡大）
hdr = [me(0, 90)] + [(l, C(n), 0, 90) for l, n in [('キャリカミ', 'c1_careercoming'), ('キャリアスイッチ', 'c2_careerswitch'), ('事務ナビ', 'c3_jimunavi'), ('SHE Career', 'c4_shecareer'), ('Her Next', 'c5_hernext'), ('ゆるキャリ', 'c6_yuru'), ('ハックツ', 'c7_hakkutu')]]
ims = [(l, crop(p, a, bb, 1.4)) for l, p, a, bb in hdr]
W = ims[0][1].width * 2 + 16; rows = (len(ims) + 1) // 2; RH = max(i.height for _, i in ims) + 30
o = Image.new('RGB', (W, rows * RH), '#d6d6d6'); d = ImageDraw.Draw(o)
for k, (l, i) in enumerate(ims):
    x = (k % 2) * (i.width + 16); y = (k // 2) * RH; d.text((x + 4, y + 4), l, fill='#111', font=F); o.paste(i, (x, y + 28))
rn = pre.replace('round', '') if pre.startswith('round') else pre
o.save(f'compare/logo_header_round{rn}.png' if pre.startswith('round') else f'compare/{pre}_logo_header.png'); print('logo', o.size)
