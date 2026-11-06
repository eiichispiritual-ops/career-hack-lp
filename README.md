# career-hack-lp

りこ／みな共用の人材LP（1本）。スマホ幅390px想定。GitHub Pages で `docs/` を配信。

- 公開URL: https://eiichispiritual-ops.github.io/career-hack-lp/
- アカウント指定: `?a=riko` / `?a=mina`（旧 `?src=` も可。未指定・未登録は riko）
- LINE URL の差し替え: `docs/config.js` の `accounts.<名前>.line`
- 一時上書き: `?line=<URLエンコードしたURL>`（`lineHosts` のドメインの https のみ有効）
- 女性ヘッダー（全アカウント共通1枚）: `docs/config.js` の `header`（既定 `img/header_woman_1.png`・縦3:4推奨）。ファイルが無い間は差し替え枠が出る。FV・理由見出し・不安・タイミング・ポップアップの5か所で同じ画像を使う
- 「中の人」欄の丸アイコン: `accounts.<名前>.face`
- 社名・許可番号: `docs/config.js` の `operator` / `partner` / `permit`
- LINE 1通目の文面: `line/first_message.md`（LP の `#first` と同じ文面。変えるときは両方直す）

## ローカルで見る
```
cd docs && python3 -m http.server 8000
# http://localhost:8000/?a=mina
```

## 構成（参考: ai-plus.school/meta01.html と同じ順）
FV（帯見出し＋女性ヘッダー＋0円メダル）→CTA→3つの安心→相談テーマのマーキー→数字の例カルーセル→LINEで聞く5つの理由→7つのテーマ→3大特典（届く文面を展開）→でも不安…→大丈夫→LINE相談では…→もう少し考えてから…→中の人紹介→流れ→FAQ→最終CTA→黒フッター。CTA 6か所＋追従CTA＋離脱前ポップアップ（後半で大きく上に戻したとき1回）。

## 数字の出典（LP の ※1〜3）
1. 相談料0円: 職業安定法 第32条の3 第2項
2. 高卒の3年以内離職 36.9%: 厚生労働省「新規学卒就職者の離職状況（令和5年3月卒業者）」2026-10-23公表 https://www.mhlw.go.jp/stf/houdou/0000177553_00011.html
