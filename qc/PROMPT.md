# タスク: career-hack-lp を「これAIなん？」レベルに仕上げる（あなたはトップLPデザイナー兼マーケター）

## 前提
- リポジトリ: ~/career-hack-lp（ブランチ design-polish。main には絶対に push しない・main に切り替えない）。公開は docs/（GitHub Pages）。?a=riko / ?a=mina でアカウント出し分け。
- ベースは現在の docs/（ChatGPT版 d9d01a2 は使わない。`git show d9d01a2:docs/...` でアイデアを見るのは可）。
- 採点基準: ~/career-hack-lp/QC_RUBRIC.md（26項目）。全PASSが目標。
- 既存競合調査: ~/lp_research/result.md, result2.md, data/*.json(約42LP, DOM/色/リンク), shots/<LP>/（390px スクショ）, scripts/(shoot.py, color.py, sheet.py, crop.py 等 Playwright スクリプト)。まずこれを読む。
- オーナーの不満: 「ボタンやちょっとした細かいところがめっちゃAIっぽい」。競合のいいとこ取りの継ぎはぎにして、フォント・色味まで競合に寄せ、見た人が「これAIなん？」と思うレベルに。

## 禁止
- docs/config.js を変更しない（LINE URL・運営者・提携先・許可番号）。
- 数字・実績・お客様の声・社名・人物写真の捏造禁止。出典が無い数字は使わない（特徴メダルで代替）。
- フォーム送信、LINE友だち追加、lin.ee/LIFF/lmes 遷移、アフィリエイトURLクリック、ログイン、外部への投稿・送信は禁止。閲覧のみ。
- ~/Instagram 以下や Google Drive には触れない（~/lp_research は読み取り可、新規保存は ~/career-hack-lp/qc/ 配下）。
- git push は `git push origin design-polish` のみ可。main への push / force push 禁止。

## 電話の表現（重要）
相談は電話のアポイントになる。それは隠さず、やわらかく：「ご希望の日時に、担当者から相談のお電話をします」「話を聞くだけでもOK」「無理に応募をすすめることはありません」等。
NG: 「こちらから電話はしません」「しつこい電話なし」「電話が来ません」など断定・不安を想起させる語。既存コピーにあれば全て書き換える。

## 手順（ループ）
1. 調査: (a) ~/lp_research の競合を読み、ボタン/フォント/色/余白/アイコンを実測値で表にまとめる（qc/competitor_specs.md）。必要なら主要5〜8社のLPを Playwright(390x844, DPR2) で撮り直し、computed style（font-family, font-size, font-weight, line-height, letter-spacing, button の background/border-radius/height/box-shadow）を JS で抽出して qc/specs/*.json に保存。
   (b) X(Twitter)広告/投稿でよく見る 転職・女性転職・在宅ワーク・事務転職 のLPを Web検索で 5件以上追加で探し、同様に撮影・実測（閲覧のみ）。見つけ方とURLを qc/x_ads_research.md に記録。X広告ライブラリが見られなければその旨記録。
2. 自社を 390px で撮影（file:// か `python3 -m http.server` で docs/ を配信、?a=riko と ?a=mina 両方）。
3. セクション単位で横並べ比較画像を作る（自社 | 競合A | 競合B | 競合C、同縮尺）: FV / CTAボタン拡大 / 悩み〜選ばれる理由 / 流れ・特典 / FAQ・最終CTA・フッター / 追従CTA。qc/compare/round<N>_<section>.png
4. 比較画像を自分の目（Read で画像を見る）で見て、AIっぽさの差分を列挙 → docs/index.html, docs/style.css（必要ならJS）を修正。AI tell の例: 紫青グラデ、グロー、均一な角丸カード+影の3列、lucide/heroicons風線画アイコン、絵文字見出し、全部太字、間延びした余白、英語の小見出し(“Features”等)、ピル型タグの乱用、完全対称レイアウト、ありがちなコピー。
   競合の具体的な部品を真似る: 「＼ 登録1分・完全無料 ／」吹き出し、LINE緑の立体ボタン(下影)、マーカー黄下線、数字だけ大きい強調、番号バッジ付きステップ、吹き出しのお客様の声（実在しないなら声は作らない→「よくある相談」形式などで代替）、アコーディオンFAQ、追従CTA。女性向けならくすみピンク/コーラル系パレット（競合実測色から）。
   フォントは競合実測に合わせる（例: Hiragino/Noto Sans JP、見出し900/700、本文400、line-height 1.7前後）。
5. 再撮影 → 採点 → qc/score_round<N>.md に 26項目それぞれ PASS/FAIL と根拠（どの比較画像で判断したか）を書く。
6. FAILがあれば 3 に戻る。最低3ラウンド、最大8ラウンド。各ラウンド終わりに git commit（メッセージに round とスコア）し、`git push origin design-polish`。
7. 完了時: qc/final/ に riko/mina の 390px フルページと 1280px のスクショ、qc/compare/final_*.png（FV・ボタン・中盤・FAQ/フッター の4枚以上）を置き、qc/DONE.md に 最終スコア(PASS/26)、主な変更、残課題、比較画像パス一覧を書く。

## 品質
- 自己採点は甘くしない。「競合と並べて区別がつかない」と言えないものは FAIL。
- 実装後に HTML の構文エラー・JS コンソールエラー・横スクロール（390pxで scrollWidth>390）が無いことを確認。
- ?a=riko / ?a=mina 両方で確認。
