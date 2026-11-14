# 閲覧専用: 競合の追従CTAを見るため、中盤までスクロールした1画面を撮る（クリックなし・LINE系遮断）
import sys, asyncio, os
from playwright.async_api import async_playwright
UA=("Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148")
BLOCK=["lin.ee","line.me","liff.","lmes.jp","l-tra.com"]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for name,url in [("c1_careercoming","https://ad-lp2.career-coming.com/mt/c001/?fv=a005"),("c3_jimunavi","https://jimunavi.com/"),("c6_yuru","https://career-coming.com/yuru/a001/")]:
            ctx=await b.new_context(viewport={"width":390,"height":844},device_scale_factor=2,is_mobile=True,has_touch=True,user_agent=UA,locale="ja-JP")
            pg=await ctx.new_page()
            await pg.route("**/*",lambda r: r.abort() if any(h in r.request.url for h in BLOCK) else r.continue_())
            await pg.goto(url,wait_until="domcontentloaded",timeout=60000); await pg.wait_for_timeout(2500)
            for y in range(0,2300,300): await pg.evaluate(f"window.scrollTo(0,{y})"); await pg.wait_for_timeout(150)
            await pg.wait_for_timeout(1200)
            await pg.screenshot(path=os.path.expanduser(f"~/career-hack-lp/qc/shots/comp_{name}/sticky.png")); await ctx.close()
        await b.close()
asyncio.run(main())
