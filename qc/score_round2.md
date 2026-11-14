# Round 2 採点 — 29/30
比較画像: compare/round2_fv.png, round2_button.png, round2_mid.png, round2_flow_gift.png, round2_faq_footer.png, round2_sticky.png, logo_header_round2.png
機械チェック: shots/r2_{riko,mina}_390/check.json → scrollWidth=390、console error 0、CTA 5、href OK。

変更: 流れ STEP1 にボタン図（キャリアスイッチの「STEP01 ボタンをクリック」型）、STEP4 に担当者写真（事務ナビの担当者紹介の要素）。理由1の「相談も多くいただきます」（根拠のない量の表現）を削除。STEP4の「話を／聞く」改行、ミニボタン内の不自然な字間を修正。

| # | 判定 | 根拠 |
|---|---|---|
| A1–A5 | PASS×5 | round2_button / round2_sticky（Round1から変更なし。高さ60・#06C755・角丸10・18px・下影4px・タブ吹き出し・追従はFV通過後） |
| B1–B4 | PASS×4 | 書体・ウェイト変更なし。B4: round2_flow_gift で STEP4 の改行を修正済みを確認 |
| C1–C3 | PASS×3 | round2_mid / round2_flow_gift：パレット・交互背景は事務ナビ/ゆるキャリと同系 |
| D1 | PASS | 追加したのはボタン図と写真で、線画アイコン0 |
| D2 | PASS | 絵文字0 |
| D3 | PASS | STEP4だけ枠色・写真つきで強弱。均一カード3列なし |
| D4 | PASS | gen_advisor.jpg（オーナー指示の生成画像）。alt に「イメージ」と明記 |
| E1–E4 | PASS×4 | E2: FVボタン下端 y≈732 |
| F1 | PASS | 電話NG語 0件（grep） |
| F2 | PASS | 量の表現「多くいただきます」も削除 |
| F3 | PASS | |
| F4 | PASS | config.js 差分なし |
| G1 | PASS | compare/round2_*.png |
| G2 | FAIL | final 未作成 |
| H1–H4 | PASS×4 | logo_header_round2 |
