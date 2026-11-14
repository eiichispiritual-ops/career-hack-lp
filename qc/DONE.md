# DONE — career-hack-lp「これAIなん？」仕上げ
最終スコア: **30/30 PASS**（score_round3.md）。経過: Round1 29/30 → Round2 29/30 → Round3 30/30（Round1・2 の FAIL は G2 の final 未作成のみ）。

## 主な変更
- **方向性**: 20代女性向けに統一（riko/mina の集客先、調査 BRIEF の前提）。骨格は事務ナビ・ゆるキャリ、ボタンはキャリカミ・キャリアスイッチ寄せ。
- **ボタン**: 高さ60・#06C755・角丸10・下影 0 4px 0。「¥0」丸＋LINE吹き出し＋「›」、上にタブ吹き出し「＼ 登録1分・完全無料 ／」、下にグレー注記。CTAは本文4＋追従1。追従は FV 通過後に出て、最終CTA表示中は引っ込む。
- **書体・色**: 本文 Noto Sans JP 400（15px / lh1.75）、見出し Zen Maru Gothic 900。Oswald は廃止。色はローズ #9A4460・コーラル #E98F85・薄ピンク #FDF3F6・ベージュ #F8F1EC・マーカー黄。いずれも競合実測値。
- **ロゴ**: 吹き出し＋上り階段の独自マークに、Zen Maru Gothic の字形をパス化した文字を組み合わせた。docs/img/logo.svg / logo-white.svg / logo-mark.svg（favicon）。旧ロゴの棒グラフ型はキャリカミに似ていたため廃止。
- **電話表現**: 「電話なし」「電話は0回」「電話・来社なし」を全削除。「ご希望の日時に、担当者から相談のお電話をします」「話を聞くだけでも大丈夫」「無理に応募をすすめることはありません」に統一。流れの STEP3〜4 と FAQ で、電話で相談することを明記。
- **捏造リスクの除去**: 根拠未確定の 93万円UP/98%/94% メダル・実績帯、仮置きの事例3名（Kさん等）、日曜夜の通知モック（架空の金額入り）を削除。メダルは数字なしの特徴（相談料0円・経験資格なしでOK・相談の日時を選べる）にした。
- **個人情報の取り扱い**: 電話相談の実態に合わせ、提携先へ渡るものに「相談のお電話の日時と電話番号」を追記（要確認）。
- **写真**: PM 生成の gen_*.jpg 5枚を採用。手指・スマホ・顔を200%で確認済み。依頼・確認ログは image_requests.md。

## 残課題（オーナー確認が必要）
1. 女性向けに振り切った（旧版は男女兼用）。男性も対象に残すなら FV コピーと写真の差し替えが必要。
2. 個人情報欄の追記（電話番号・日時）は運用に合わせた推定。法務/提携先と文言の確認を。
3. 「登録1分」「選ばれる3つの理由」は自社フローの説明として使っている。実際の登録所要時間を確認してほしい。
4. 職種の例（一般事務・カスタマーサポート・営業アシスタント）と「在宅ありの求人も」は、提携先が実際に扱える求人に合わせて調整を。
5. config.js の LINE URL・運営者・提携先・許可番号はダミー/空のまま（触っていない）。
6. 旧素材（ic_*.svg, il_*.svg, fv_pair.png など）は docs/img に残置。未使用なので削除してよい。
7. X 広告ライブラリは EU 配信分しか見られず、日本の広告は確認できない。x_ads_research.md は検索で見つけた SNS 広告型 LP 6件の実測。

## 比較画像
- 最終: compare/final_fv.png, final_button.png, final_mid.png, final_flow_gift.png, final_faq_footer.png, final_sticky.png, final_logo_header.png
- 経過: compare/round1_*.png, round2_*.png, logo_header_round1.png, logo_header_round2.png
- 最終スクショ: final/riko_390_full.png, mina_390_full.png, riko_1280_full.png, mina_1280_full.png（＋各 _fv, _390_sticky）

## 調査資料
competitor_specs.md（競合7社の実測）、x_ads_research.md（X広告系6件）、specs/*.json、scripts/（spec_shoot.py, measure_btn.py, shoot_self.py, make_compare.py, make_logo.py）
