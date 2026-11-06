# career-hack-lp

りこ／みな共用の人材LP（1本）。スマホ幅390px想定。GitHub Pages で `docs/` を配信。

- 公開URL: https://eiichispiritual-ops.github.io/career-hack-lp/
- アカウント指定: `?a=riko` / `?a=mina`（旧 `?src=` も可。未指定・未登録は riko）
- LINE URL の差し替え: `docs/config.js` の `accounts.<名前>.line`
- 一時上書き: `?line=<URLエンコードしたURL>`（`lineHosts` のドメインの https のみ有効）
- ヘッダー画像: `docs/img/hero_riko.jpg` / `hero_mina.jpg` を同名で上書き（推奨 1170×780・3:2）。読めない時は `*_face.jpg` に切り替わる
- 社名・許可番号: `docs/config.js` の `operator` / `partner` / `permit`
- LINE 1通目の文面: `line/first_message.md`（LP の `#first` と同じ文面。変えるときは両方直す）

## ローカルで見る
```
cd docs && python3 -m http.server 8000
# http://localhost:8000/?a=mina
```

## 構成
FV（女性ヘッダー＋完全無料＋出典つき数字メダル3つ）→ 共感（悩み5択）→ なぜエージェント（比較表）→ 落とし穴（辞める前3つ／求人票4つ／承諾前）→ 自社（やる・やらない6つ）→ 届く1通目の実物 → FAQ → 最終CTA → 個人情報。CTA は6か所＋追従バー。

## 数字の出典（LP の ※1〜3）
1. 相談料0円: 職業安定法 第32条の3 第2項
2. 高卒の3年以内離職 36.9%: 厚生労働省「新規学卒就職者の離職状況（令和5年3月卒業者）」2026-10-23公表 https://www.mhlw.go.jp/stf/houdou/0000177553_00011.html
3. 有休取得率 66.9%: 厚生労働省「令和7年就労条件総合調査」2025-12-19公表
