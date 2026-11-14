# Round 1 採点（390px / riko・mina）— 29/30
比較画像: compare/round1_fv.png, round1_button.png, round1_mid.png, round1_flow_gift.png, round1_faq_footer.png, round1_sticky.png, logo_header_round1.png
機械チェック: shots/r1_{riko,mina}_390/check.json → scrollWidth=390（横スクロールなし）、console error 0、CTA 5（本文4＋追従1）、href は riko/mina それぞれの lin.ee。

| # | 判定 | 根拠 |
|---|---|---|
| A1 | PASS | round1_button: 高さ60・#06C755・角丸10（キャリカミ実測≈8）・文字18px/700・右「›」・左にLINE吹き出し・左上「¥0」丸。キャリカミ/ゆるキャリと同型 |
| A2 | PASS | ボタン上にタブ吹き出し「＼ 登録1分・完全無料 ／」（キャリアスイッチ型）、下にグレー注記（事務ナビ型） |
| A3 | PASS | round1_sticky: FVのボタン通過後に表示、最終CTA表示中は引っ込む。フッター下に110pxの余白を確保し本文を隠さない |
| A4 | PASS | FV・理由のあと・流れのあと・最終 の4つ＋追従 |
| A5 | PASS | グラデ・グロー無し。影は 0 4px 0 #04963F のみ、押下で沈む |
| B1 | PASS | 本文 "Noto Sans JP"→Hiragino→Meiryo（キャリカミ/事務ナビ実測）、見出し Zen Maru Gothic（事務ナビ実測）のみ。Oswald 廃止 |
| B2 | PASS | 400/700/900 の3種。本文15px lh1.75、h2 23px lh1.55（事務ナビ 23.4px） |
| B3 | PASS | 黄マーカー・「無料」だけ色文字・「3」「2」の数字だけ大きく。本文は400 |
| B4 | PASS | 全ビューポートを目視。特典タイトルの「言い／換え」分断を修正済み（nw） |
| C1 | PASS | ローズ#9A4460・薄ピンク#FDF3F6（事務ナビ）、コーラル#E98F85（SHE Career）、ベージュ#F8F1EC（ゆるキャリ）＋LINE緑 |
| C2 | PASS | 紫青グラデ・ネオン・ガラス無し |
| C3 | PASS | 薄ピンク→白→薄ピンク→白→ベージュ→薄ピンク→白→ベージュ→白→ローズ（事務ナビと同じ交互） |
| D1 | PASS | 線画アイコン0。旧 ic_*.svg を廃止し、写真＋番号バッジ＋吹き出し |
| D2 | PASS | 絵文字0 |
| D3 | PASS | 理由カードは枠線/ベージュ地/写真入りで形を変え、角丸も左右非対称。職種はカラーバー違いの縦積み |
| D4 | PASS | 写真は docs/img の既存素材と、オーナー指示（ADDENDUM 追加指示2）で生成した gen_*.jpg のみ。偽ロゴなし。フッターに「写真はイメージです」 |
| E1 | PASS | 左右20px、セクション48px（事務ナビ 44px/20px） |
| E2 | PASS | キャッチ＋「無料」＋特徴メダル3（数字なし）＋CTA。FVボタン下端 y=732 < 844 |
| E3 | PASS | 悩み→解決→できること→理由→CTA→職種→特典→流れ→FAQ→CTA |
| E4 | PASS | 無料？/電話は？/地方・在宅でも？/未経験でも？ ほか計7問、アコーディオン |
| F1 | PASS | 「ご希望の日時に、担当者から相談のお電話をします」「話を聞くだけでも」「無理に応募をすすめることはありません」。NG語 grep 0件（電話なし/電話は0回/しつこい 等） |
| F2 | PASS | 旧版の 93万円UP/98%/94%・事例3名（仮置き）を削除。数字は法令出典（※1）のみ |
| F3 | PASS | 「〜しませんか？」は見出し1回のみ、三点リーダ0 |
| F4 | PASS | git diff docs/config.js なし。riko/mina とも同一表示・href切替OK |
| G1 | PASS | compare/round1_*.png 6枚（自社＋競合3社） |
| G2 | FAIL | qc/final/ 未作成（最終ラウンドで作成） |
| H1 | PASS | logo_header_round1: 吹き出し＋上り階段の独自マーク＋Zen Maru Gothic 900 のローズ文字。競合（棒グラフ・S字四角・欧文）と別形状 |
| H2 | PASS | 高さ52px・白・下線1px・右に2行コピー（キャリアスイッチ型）。競合 42〜94px の範囲 |
| H3 | PASS | logo.svg は字形をパス化した自己完結SVG。グラデ無し |
| H4 | PASS | favicon=logo-mark.svg、ヘッダー/解決ボックス/フッター（白抜き）で同じロゴ |

## 次ラウンドで直す（PASSでも見劣りする箇所）
- 流れのSTEPが文字だけ。競合（キャリアスイッチ・事務ナビ）はSTEPごとに画像/ボタン図あり → STEP1にボタン図、STEP4に担当者写真
- 悩みの中央写真が2段目の吹き出しに少しかぶる → 位置調整
- 理由1「相談も多くいただきます」は根拠のない量の表現 → 言い換え
