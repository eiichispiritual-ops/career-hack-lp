# 閲覧専用: 競合LPを 390x844 DPR2 で撮影し、computed style を抽出して qc/specs/<name>.json に保存。
# クリック・入力・送信は一切しない。LINE/LIFF/lmes 等へのリクエストは遮断。
# usage: python3 spec_shoot.py <name> <url>
import sys, os, json, asyncio
from playwright.async_api import async_playwright
UA = ("Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 "
      "(KHTML, like Gecko) Mobile/15E148 Instagram 330.0.0.0 (iPhone14,5; iOS 17_5; ja_JP; ja; scale=3.00; 1170x2532)")
BLOCK = ["lin.ee", "line.me", "liff.", "lmes.jp", "l-tra.com"]
Q = os.path.expanduser("~/career-hack-lp/qc")
JS = r"""() => {
 const px = v => Math.round(parseFloat(v)*10)/10;
 const st = e => { const c=getComputedStyle(e), r=e.getBoundingClientRect();
   return {tag:e.tagName.toLowerCase(), cls:(e.className&&e.className.baseVal===undefined?e.className:'').toString().slice(0,60),
    text:(e.innerText||e.querySelector?.('img')?.alt||'').trim().replace(/\s+/g,' ').slice(0,50),
    y:Math.round(r.top+scrollY), w:Math.round(r.width), h:Math.round(r.height),
    font:c.fontFamily, size:c.fontSize, weight:c.fontWeight, lh:c.lineHeight, ls:c.letterSpacing, color:c.color,
    bg:c.backgroundColor, bgimg:c.backgroundImage.slice(0,120), radius:c.borderRadius, shadow:c.boxShadow, border:c.border, borderBottom:c.borderBottom,
    pad:c.padding}; };
 const vis = e => { const r=e.getBoundingClientRect(); return r.width>0 && r.height>0; };
 const ctaRe = /lin\.ee|line\.me|liff|lmes|l-tra|utage|#form|entry|regist|LINE|無料|相談|登録/i;
 const ctas = [...document.querySelectorAll('a,button')].filter(vis).filter(a => ctaRe.test((a.href||'')+' '+(a.innerText||'')+' '+(a.querySelector('img')?.alt||'')));
 const ctaOut = ctas.slice(0,15).map(a => { const s=st(a); const im=a.querySelector('img');
   if (im) { const r=im.getBoundingClientRect(); s.img={src:(im.currentSrc||im.src).slice(-80), w:Math.round(r.width), h:Math.round(r.height)}; }
   const inner=[...a.querySelectorAll('*')].filter(vis).slice(0,6).map(st); s.inner=inner; s.href=(a.href||'').slice(0,80); return s; });
 const pick = sel => [...document.querySelectorAll(sel)].filter(vis).slice(0,8).map(st);
 const body = st(document.body);
 const ps = [...document.querySelectorAll('p,li,dd')].filter(vis).filter(e=>e.innerText.trim().length>15);
 const freq = k => { const m={}; ps.forEach(e=>{const v=getComputedStyle(e)[k]; m[v]=(m[v]||0)+1}); return Object.entries(m).sort((a,b)=>b[1]-a[1]).slice(0,5); };
 const secs = [...document.querySelectorAll('section, main > div, .section, [class*=sec]')].filter(vis).slice(0,40).map(e=>{const c=getComputedStyle(e),r=e.getBoundingClientRect();return {cls:String(e.className).slice(0,40),y:Math.round(r.top+scrollY),h:Math.round(r.height),pt:c.paddingTop,pb:c.paddingBottom,pl:c.paddingLeft,bg:c.backgroundColor}});
 const imgs=[...document.querySelectorAll('img')].filter(vis);
 const imgArea = imgs.reduce((s,i)=>{const r=i.getBoundingClientRect();return s+r.width*r.height},0);
 const fixed=[...document.querySelectorAll('body *')].filter(e=>{const p=getComputedStyle(e).position;return (p==='fixed'||p==='sticky')&&vis(e)}).slice(0,5).map(st);
 return {url:location.href, title:document.title, height:document.documentElement.scrollHeight, body,
   imgCoverage: Math.round(imgArea/(390*document.documentElement.scrollHeight)*100)/100,
   bodyText:{family:freq('fontFamily'), size:freq('fontSize'), lh:freq('lineHeight'), weight:freq('fontWeight'), ls:freq('letterSpacing'), color:freq('color')},
   h1:pick('h1'), h2:pick('h2'), h3:pick('h3'), ctas:ctaOut, fixed, sections:secs,
   summaries:pick('summary, dt, .faq dt, [class*=faq] [class*=q]')};
}"""
async def main(name, url):
    out = f"{Q}/shots/comp_{name}"; os.makedirs(out, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True,
                                  has_touch=True, user_agent=UA, locale="ja-JP")
        pg = await ctx.new_page()
        await pg.route("**/*", lambda r: r.abort() if any(h in r.request.url for h in BLOCK) else r.continue_())
        await pg.goto(url, wait_until="domcontentloaded", timeout=60000)
        try: await pg.wait_for_load_state("networkidle", timeout=15000)
        except Exception: pass
        await pg.wait_for_timeout(2000)
        h = await pg.evaluate("document.documentElement.scrollHeight"); y = 0
        while y < h:
            y += 400; await pg.evaluate(f"window.scrollTo(0,{y})"); await pg.wait_for_timeout(200)
            h = await pg.evaluate("document.documentElement.scrollHeight")
        await pg.wait_for_timeout(1200); await pg.evaluate("window.scrollTo(0,0)"); await pg.wait_for_timeout(800)
        await pg.screenshot(path=f"{out}/00_fv.png")
        await pg.screenshot(path=f"{out}/full.png", full_page=True)
        spec = await pg.evaluate(JS)
        json.dump(spec, open(f"{Q}/specs/{name}.json", "w"), ensure_ascii=False, indent=1)
        print(name, spec["height"], "ctas", len(spec["ctas"]), "imgCov", spec["imgCoverage"], spec["bodyText"]["family"][:1])
        await b.close()
asyncio.run(main(sys.argv[1], sys.argv[2]))
