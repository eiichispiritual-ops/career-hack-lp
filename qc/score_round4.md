# Round 4 採点（PMレビュー反映・厳しめ再採点）— 30/30
前提: PM_FEEDBACK.md の6点は Round3 時点で FAIL 扱いとした（A1・D3・E2・H2・D4・G2 に相当）。下表はそれを直したあとの判定。
比較画像: compare/round4_fv.png, round4_button.png, round4_mid.png, round4_flow_gift.png, round4_faq_footer.png, round4_sticky.png, logo_header_round4.png（final_*.png は同じ撮影から作成）
機械チェック: shots/r4_{riko,mina}_{390,1280}/check.json → scrollWidth 390/1280、console error 0、CTAリンク 5（ヘッダー/FV/流れ後/最終/追従）、href は riko/mina それぞれの lin.ee。HTMLタグ対応: 未閉じ0・不一致0。電話NG語 grep 0件。config.js 差分なし。

## Round3 → Round4 の修正（PM指摘との対応）
| PM指摘 | Round3判定(再評価) | 修正 | Round4 |
|---|---|---|---|
| 1 FVボタンが暗く平板 | A1 FAIL | 上下グラデ #25D870→#06C755→#00B900、下影 0 4px 0 #008F2A、上端に1pxの白ハイライト、高さ62、文字18px/900（「無料」だけ黄 #FFF35A）、右矢印を太く(3.5px)。round4_button でキャリカミ/キャリアスイッチ/事務ナビと明度が同等 | PASS |
| 2 メダルが白丸で弱い | D3 FAIL（FVの訴求部品が競合より見劣り） | 自作SVGメダル（波形ロゼット #F6D3C6＋ゴールドベージュ #C9A274 の二重リング＋星＋コーラルのリボン2本）。文言は 0円 / なしでもOK / ご希望に合わせます（数字は0円のみ） | PASS |
| 3 写真が浮く | E2 FAIL（FVのまとまり） | 人物を右下に大きく配置（268×330）。左・上・下をグラデマスクでフェードし、乗算で淡ピンク地に溶かした。左に「専任の担当者が／求人さがしから／面接まで伴走」の帯と #タグ（キャリカミ/キャリアスイッチ型）。390×844 に キャッチ＋写真＋メダル＋CTA（ボタン下端 y=702） | PASS |
| 4 ヘッダーにLINEボタン | H2 FAIL（事務ナビ型の右ボタンなし） | 右に小さいLINEボタン「LINEで無料相談」（34px・ピル・同じ緑グラデ）。CTA総数を5に抑えるため、理由セクション後の中間CTAを削除（中盤は追従CTAが担う） | PASS |
| 5 生成写真に注記 | D4 FAIL | FV写真と STEP4 担当者写真に「※写真はイメージです」を小さく添えた（フッターにも一括注記あり） | PASS |
| 6 final/DONE/push | G2 FAIL | final/ を r4 で撮り直し、compare/final_*.png・DONE.md を更新 | PASS |

## 30項目
| # | 判定 | 根拠 |
|---|---|---|
| A1 | PASS | round4_button（上記） |
| A2 | PASS | 「＼ 登録1分・完全無料 ／」タブ吹き出し＋下に「ご希望の日時に、担当者から相談のお電話をします」 |
| A3 | PASS | round4_sticky: FVボタン通過後に出現、最終CTA中は格納、フッター下余白で本文を隠さない |
| A4 | PASS | ヘッダー・FV・流れ後・最終・追従＝合計5（上限内） |
| A5 | PASS | グラデ＋下影のみ（競合と同じ）。グロー・ぼかし影・絵文字・ホバー浮きなし |
| B1 | PASS | Noto Sans JP / Zen Maru Gothic（競合実測） |
| B2 | PASS | 400/700/900、本文 lh1.75 |
| B3 | PASS | マーカー・色文字・数字だけ大 |
| B4 | PASS | STEP4 の「お電話で／相談」改行は注記幅の固定で解消。riko/mina 全ビューポート目視 |
| C1 | PASS | 実測パレット内（メダルのベージュ/コーラルも同系） |
| C2 | PASS | 紫青グラデ・ネオン・全面グラデなし |
| C3 | PASS | 白/薄ピンク/ベージュの交互（中間CTA削除後も 理由=白→職種=薄ピンク で交互維持） |
| D1 | PASS | 線画アイコン0（✓は文字） |
| D2 | PASS | 絵文字0 |
| D3 | PASS | メダルはリボン付き装飾枠、理由カードは形違い、STEP4 だけ強調 |
| D4 | PASS | 既存素材＋オーナー指示の生成写真、イメージ注記あり。偽ロゴなし |
| E1 | PASS | 左右20px・セクション48px |
| E2 | PASS | round4_fv |
| E3 | PASS | 悩み→解決→できること→理由→職種→特典→流れ→FAQ→CTA |
| E4 | PASS | 7問アコーディオン |
| F1 | PASS | NG語0、電話相談を明記しやわらかい表現 |
| F2 | PASS | 数字は0円と法令出典※1のみ |
| F3 | PASS | |
| F4 | PASS | config.js 差分なし、riko/mina 正常 |
| G1 | PASS | compare/round4_*・final_* |
| G2 | PASS | final/{riko,mina}_{390,1280}_full.png 崩れなし |
| H1 | PASS | logo_header_round4 |
| H2 | PASS | 52px白ヘッダー＋右LINEボタン（事務ナビ型） |
| H3 | PASS | パス化SVG |
| H4 | PASS | favicon/ヘッダー/フッターで同ロゴ |
