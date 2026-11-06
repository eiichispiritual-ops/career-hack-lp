/* アカウント別の差し替え設定（りこ／みな共用LP）
 *
 * 1本のLPを複数アカウントで使い回す。アカウントごとに変わるのはここだけ。
 *   https://…/career-hack-lp/?a=riko   → accounts.riko を使う
 *   https://…/career-hack-lp/?a=mina   → accounts.mina を使う
 *   ?a= が無い・未登録の値            → defaultAccount を使う
 *   （旧URLの ?src=riko / ?src=mina も同じ扱い）
 *
 * LINEのURLを一時的に試すときは ?line=<URLエンコードしたURL> でも上書きできる。
 * ただし lineHosts に載っているドメインの https URL だけを受け付ける
 * （任意のURLを通すと、細工したリンクで別サイトへ飛ばせてしまうため）。
 *
 * アカウントを増やすときは accounts に1ブロック足し、face 画像を img/ に置く。
 */
window.LP_CONFIG = {
  defaultAccount: 'riko',

  // 女性ヘッダー画像（全アカウント共通で1枚）。縦長 3:4 推奨（例 900x1200）。
  // 同名で上書きすれば差し替え完了。読めない間は差し替え枠が表示される。
  header: 'img/header_woman_1.png',

  accounts: {
    riko: {
      name: 'りこ',
      // UTAGEで発行したLINE友だち追加URLに差し替える（ダミー）
      line: 'https://lin.ee/REPLACE_ME_riko',
      face: 'img/riko_face.jpg',   // 「中の人」欄の丸アイコン
      reel: '',      // 例: 'https://www.instagram.com/reel/xxxxxxxxx/'
      profile: ''    // 例: 'https://www.instagram.com/xxxxxxxx/'
    },
    mina: {
      name: 'みな',
      line: 'https://lin.ee/REPLACE_ME_mina',
      face: 'img/mina_face.jpg',
      reel: '',
      profile: ''
    }
  },

  // ?line= で受け付けるドメイン（サブドメインも可）
  lineHosts: ['lin.ee', 'line.me', 'utage-system.com'],

  // CTAのURL末尾に ?src=アカウント を付けるか。
  // LINEの友だち追加URL(lin.ee)は引き継がないので実害はないが、不要なら false
  appendParams: true,

  // 確定したら記入。空のあいだは「確定後に記載」と表示される
  operator: '',          // 運営会社名
  partner: '',           // 提携人材紹介会社名
  permit: ''             // 例: '13-ユ-000000'
};
