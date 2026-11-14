# ロゴSVG生成: Zen Maru Gothic Black（OFL）の字形をパス化して自己完結SVGにする。
# マーク = 角の丸い吹き出し（コーラル）＋ 右上がりの3段ステップ（白）。競合マークとは別形状。
import sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
FONT = sys.argv[1]; OUT = sys.argv[2]
f = TTFont(FONT); gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f['head'].unitsPerEm
ROSE, CORAL = '#9A4460', '#E98F85'
def word(text, size, x0, base, track):
    s = size / upm; x = x0; parts = []
    for ch in text:
        g = cmap[ord(ch)]; pen = SVGPathPen(gs)
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x, base)))
        parts.append(pen.getCommands()); x += gs[g].width * s + track
    return ' '.join(parts), x - track
MARK = ('<path d="M4 2h24a4 4 0 0 1 4 4v17a4 4 0 0 1-4 4H14l-6 5v-5H4a4 4 0 0 1-4-4V6a4 4 0 0 1 4-4z" fill="%s"/>'
        '<path d="M7 21h5.5v-4.5H18V12h5.5V7.5" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>'
        '<circle cx="25.5" cy="7.5" r="2.6" fill="#FFF04A"/>') % CORAL
d1, w1 = word('キャリアハック', 20, 40, 24, 0.6)
W = int(w1 + 2)
open(f'{OUT}/logo.svg', 'w').write(
  f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 34" width="{W}" height="34" role="img" aria-label="キャリアハック">'
  f'{MARK}<path d="{d1}" fill="{ROSE}"/></svg>\n')
open(f'{OUT}/logo-mark.svg', 'w').write(
  f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 0 36 34" width="36" height="34">{MARK}</svg>\n')
d2, w2 = word('キャリアハック', 20, 40, 24, 0.6)
open(f'{OUT}/logo-white.svg', 'w').write(
  f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 34" width="{W}" height="34" role="img" aria-label="キャリアハック">'
  f'{MARK}<path d="{d2}" fill="#fff"/></svg>\n')
print('logo width', W)
