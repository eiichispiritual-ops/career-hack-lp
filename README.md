# career-hack-lp

アカウント共用の人材LP（1本・名前や顔は出さない）。スマホ幅390px想定。GitHub Pages で `docs/` を配信。

- 公開URL: https://eiichispiritual-ops.github.io/career-hack-lp/
- アカウント指定: `?a=riko` / `?a=mina`（旧 `?src=` も可。未指定・未登録は riko）
- LINE URL の差し替え: `docs/config.js` の `accounts.<名前>.line`
- 一時上書き: `?line=<URLエンコードしたURL>`（`lineHosts` のドメインの https のみ有効）
- 社名・許可番号: `docs/config.js` の `operator` / `partner` / `permit`
- LINE 1通目の文面: `line/first_message.md`
- FV人物（男女ペア）: `docs/img/fv_pair.png`（透過PNG）を置けば表示。無い間は差し替え枠の図。生成指示は `~/lp_research/goal/PROMPT_IMG_CAREER.md`

## ローカルで見る
```
cd docs && python3 -m http.server 8000
# http://localhost:8000/?a=mina
```

## 構成（正本: キャリカミ mt/c001 = ~/lp_research/data/notes_A1.md）
ロゴ帯→FV（青斜め帯・完全無料の転職相談・#自己分析/#履歴書/#面接練習・金縁メダル3）→CTA→相談例3→悩み（黄雲4）→暗転「我慢して働き続けても」→どうすれば（チェック5）→エージェントを使え＋注意点→そこで自社→とは→理由01〜04→だから→CTA→相談の多い職種→こんな自分でも？→お任せください→お願い（キャンセルは前日までに一言）→流れSTEP1〜4→CTA→FAQ5→フッター。CTAは3か所＋追従ボタン常時（A1と同じ文言「＼簡単1分で登録／今すぐ無料で相談する」）。A1の実績数字・お客様の声は根拠がないので入れていない。

## 数字の出典（LP の ※1〜3）
1. 相談料0円: 職業安定法 第32条の3 第2項
2. 高卒の3年以内離職 36.9%: 厚生労働省「新規学卒就職者の離職状況（令和5年3月卒業者）」2026-10-23公表 https://www.mhlw.go.jp/stf/houdou/0000177553_00011.html
