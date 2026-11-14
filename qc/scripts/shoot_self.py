# 自社LPを 390x844 DPR2 で撮影。full + 844px刻み。コンソールエラーと横スクロールも検査
import sys, os, asyncio, json
from playwright.async_api import async_playwright
OUT = os.path.expanduser("~/career-hack-lp/qc/shots")
async def run(tag, acct, width=390, height=844):
    out = f"{OUT}/{tag}_{acct}_{width}"; os.makedirs(out, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context(viewport={"width": width, "height": height}, device_scale_factor=2,
                                  is_mobile=width < 600, has_touch=width < 600, locale="ja-JP")
        pg = await ctx.new_page(); errs = []
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append(str(e)))
        # LINE等の外部遷移はブロック（閲覧のみ）
        await pg.route("**/*", lambda r: r.abort() if any(h in r.request.url for h in ["lin.ee", "line.me", "liff", "lmes"]) else r.continue_())
        await pg.goto(f"http://localhost:8765/?a={acct}", wait_until="networkidle")
        await pg.wait_for_timeout(800)
        h = await pg.evaluate("document.documentElement.scrollHeight")
        y = 0
        while y < h:
            await pg.evaluate(f"window.scrollTo(0,{y})"); await pg.wait_for_timeout(120); y += 600
        await pg.evaluate("window.scrollTo(0,0)"); await pg.wait_for_timeout(500)
        sw = await pg.evaluate("document.documentElement.scrollWidth")
        hrefs = await pg.evaluate("[...document.querySelectorAll('a[data-cta]')].map(a=>a.href)")
        i = 0; y = 0
        while True:
            await pg.evaluate(f"window.scrollTo(0,{y})"); await pg.wait_for_timeout(350)
            await pg.screenshot(path=f"{out}/{i:02d}_y{y}.png"); i += 1
            if y + height >= h: break
            y += height - 84
        await pg.evaluate("window.scrollTo(0,0)"); await pg.wait_for_timeout(300)
        await pg.screenshot(path=f"{out}/full.png", full_page=True)
        res = {"acct": acct, "width": width, "height": h, "scrollWidth": sw, "errors": errs, "cta": len(hrefs), "hrefs": sorted(set(hrefs))}
        json.dump(res, open(f"{out}/check.json", "w"), ensure_ascii=False, indent=1); print(res)
        await b.close()
tag = sys.argv[1]
for acct in ["riko", "mina"]:
    asyncio.run(run(tag, acct))
if len(sys.argv) > 2:
    for acct in ["riko", "mina"]:
        asyncio.run(run(tag, acct, 1280, 800))
