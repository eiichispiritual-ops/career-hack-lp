# 画像生成リクエスト（career-hack-lp / design-polish）
方針: 競合（事務ナビ・キャリアスイッチ・ゆるキャリ）同等の「ストックフォト/スマホ撮影っぽい自然な実写」。
ターゲット = 20代の日本人女性（未経験・第二新卒・販売/接客から事務・在宅へ）。LPのパレット: くすみコーラル #E8826E / 薄ピンク地 #FFF3F0 / LINE緑 #06C755 / 文字 #3A3330。
共通NG: 完全左右対称の構図・顔、プラスチック肌/過剰なツヤ、手指の本数・関節の破綻、画面や紙に文字（文字化け防止のため画面は無地かボケ）、過剰な背景ボケ、HDR調、ネオン/紫青の照明、モデル然とした過剰メイク、ロゴ・ブランド名、白人風の顔立ち、カメラ目線のキメ顔ポーズ。
共通推奨: 自然光（窓からの昼光）、少しだけ生活感（マグカップ、ノート、観葉植物）、iPhone撮影風（35mm相当、f/2.8程度、軽いノイズ）、肌の質感（毛穴・小じわの自然さ）、服はオフィスカジュアル（ベージュ・白・淡ピンクのニット/ブラウス）。

| # | ファイル名 | 用途 | サイズ(px) | 英語プロンプト | 個別NG |
|---|---|---|---|---|---|
| 1 | docs/img/gen_fv_woman.jpg | FV右側の人物（背景は白〜淡ピンクに自然に溶ける。切り抜きしなくてよい／右寄せ配置） | 900x1200 (3:4縦) | Candid waist-up photo of a Japanese woman in her mid-20s standing in a bright, modern Japanese office near a window, holding a smartphone in one hand at chest height, gentle natural smile looking slightly off-camera, shoulder-length dark brown hair, beige knit cardigan over a white blouse, soft daylight from the left, plain light wall background with a little green plant at the edge, shot on iPhone, 35mm, natural skin texture, subject placed on the right two-thirds of the frame leaving the left third empty light background, photorealistic stock photo style | 両手でスマホを持つ・画面を見せる構図、手指の破綻、ピースサイン、白飛び |
| 2 | docs/img/gen_call.jpg | 「ご希望の日時に担当者から相談のお電話」セクション（電話で話す様子） | 1200x900 (4:3横) | Natural lifestyle photo of a Japanese woman in her 20s sitting on a sofa at home in the evening, talking on her smartphone held to her ear, relaxed and smiling softly, a notebook and a mug of tea on a low wooden table, warm indoor light mixed with window light, casual knit sweater, slightly messy lived-in Japanese apartment, shot on iPhone, candid, photorealistic | 電話を耳から離した不自然な持ち方、スマホ画面の文字、イヤホンの破綻 |
| 3 | docs/img/gen_home_desk.jpg | 「在宅・事務も相談できる」求人例セクションの写真 | 1200x800 (3:2横) | Over-the-shoulder candid photo of a young Japanese woman working on a laptop at a small wooden desk at home by a window, daylight, a ceramic mug, a small plant and a paper notebook beside the laptop, laptop screen blurred and unreadable, cozy minimal Japanese apartment, shot on iPhone, natural colors, photorealistic | 画面に読める文字、左右対称の机配置、二重のキーボード |
| 4 | docs/img/gen_line_phone.jpg | 「キャリアハックとは」スマホで相談を始めるシーン（手元アップ） | 1000x1000 (1:1) | Close-up candid photo of a Japanese woman's hands holding a smartphone on a cafe table, thumb lightly on the screen, screen shows a plain soft green and white chat interface without readable text, latte cup out of focus in background, natural daylight, shot on iPhone, realistic hands with five fingers, photorealistic | 6本指・指の融合、読める文字/ロゴ、LINEの公式ロゴ |
| 5 | docs/img/gen_advisor.jpg | 「担当者より」吹き出し横の担当者イメージ（小さい丸切り抜きで使用） | 800x800 (1:1) | Friendly candid portrait of a Japanese woman in her early 30s, career advisor, wearing a light gray blazer, sitting at a meeting table in a bright office, warm natural smile, looking at the camera, shoulders visible, soft daylight, background softly out of focus office, shot on iPhone, natural skin texture, photorealistic | 名札・社名、過剰なボケ、完全正面の証明写真風 |

## 受け入れ基準（届いたら比較）
- qc/compare/round<N>_fv.png で競合FV（事務ナビ・キャリアスイッチ）と並べて「素材写真」と見分けがつかないこと。
- 指・歯・耳・髪の境界・スマホの形を 200% で確認。破綻があれば下に修正依頼を追記。

## 修正依頼ログ
（なし）
