# Round 3（最終）採点 — 30/30
比較画像: compare/final_fv.png, final_button.png, final_mid.png, final_flow_gift.png, final_faq_footer.png, final_sticky.png, final_logo_header.png
機械チェック: shots/r3_{riko,mina}_{390,1280}/check.json → scrollWidth 390/1280（横スクロールなし）、console error 0、CTA 5、href = lin.ee/REPLACE_ME_{riko,mina}?src={riko,mina}。HTMLタグ対応チェック: 未閉じ0・不一致0。

変更: FVメダル3つ目「ご希望に合わせます」が月桂樹に重なっていた → 「選べます」に短縮（final_fv で重なり解消を確認）。PC幅1280を確認（480px中央カラム＋薄い地紋。競合と同じ作り）。

| # | 判定 | 根拠 |
|---|---|---|
| A1 | PASS | final_button: 60px・#06C755・角丸10・18px/700・「›」・LINE吹き出し・「¥0」丸 |
| A2 | PASS | 「＼ 登録1分・完全無料 ／」タブ吹き出し＋下にグレー注記 |
| A3 | PASS | final_sticky: FV通過後に表示、最終CTA表示中は引っ込む、本文を隠さない |
| A4 | PASS | 本文CTA 4（FV/理由後/流れ後/最終）＋追従 |
| A5 | PASS | 下影 0 4px 0 のみ |
| B1 | PASS | Noto Sans JP（本文）＋Zen Maru Gothic（見出し）。どちらも競合実測 |
| B2 | PASS | 400/700/900、本文 lh1.75、h2 23px |
| B3 | PASS | マーカー・色文字・数字だけ大 |
| B4 | PASS | riko/mina 390 の全ビューポートを目視、孤立文字・不自然改行なし |
| C1 | PASS | 事務ナビ/SHE Career/ゆるキャリの実測色＋LINE緑 |
| C2 | PASS | 該当なし |
| C3 | PASS | 白/薄ピンク/ベージュの交互 |
| D1 | PASS | 線画アイコン0 |
| D2 | PASS | 絵文字0 |
| D3 | PASS | 理由カード3つは形が違い、STEP4だけ強調。均一な3列なし |
| D4 | PASS | 既存素材＋オーナー指示の生成写真のみ（image_requests.md に記録）。偽ロゴなし |
| E1 | PASS | 左右20px・セクション48px |
| E2 | PASS | FVボタン下端 y≈732 < 844 |
| E3 | PASS | 悩み→解決→できること→理由→職種→特典→流れ→FAQ→CTA |
| E4 | PASS | 7問のアコーディオン（無料/電話/地方・在宅/未経験を含む） |
| F1 | PASS | NG語 grep 0件。電話相談であることを明記 |
| F2 | PASS | 数字は法令出典の※1のみ |
| F3 | PASS | 該当表現なし |
| F4 | PASS | config.js 差分なし、riko/mina とも正常 |
| G1 | PASS | compare/final_*.png 7枚 |
| G2 | PASS | final/{riko,mina}_390_full.png・_1280_full.png ほか。崩れなし |
| H1 | PASS | final_logo_header |
| H2 | PASS | 52px白ヘッダー |
| H3 | PASS | パス化したSVG |
| H4 | PASS | favicon/ヘッダー/フッターで同じロゴ |
