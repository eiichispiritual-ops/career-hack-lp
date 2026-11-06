/* アカウント別の差し替え設定（共通LP1本）
 *
 * アカウントごとに変わるのは LINE の URL だけ。ページに名前や顔は出さない。
 *   https://…/career-hack-lp/?a=riko   → accounts.riko.line を使う
 *   https://…/career-hack-lp/?a=mina   → accounts.mina.line を使う
 *   ?a= が無い・未登録の値            → defaultAccount を使う
 *   （旧URLの ?src=riko / ?src=mina も同じ扱い）
 *
 * LINEのURLを一時的に試すときは ?line=<URLエンコードしたURL> でも上書きできる。
 * ただし lineHosts に載っているドメインの https URL だけを受け付ける
 * （任意のURLを通すと、細工したリンクで別サイトへ飛ばせてしまうため）。
 */
window.LP_CONFIG = {
  defaultAccount: 'riko',

  accounts: {
    // UTAGEで発行したLINE友だち追加URLに差し替える（ダミー）
    riko: { line: 'https://lin.ee/REPLACE_ME_riko' },
    mina: { line: 'https://lin.ee/REPLACE_ME_mina' }
  },

  // ?line= で受け付けるドメイン（サブドメインも可）
  lineHosts: ['lin.ee', 'line.me', 'utage-system.com'],

  // CTAのURL末尾に ?src=アカウント を付けるか
  appendParams: true,

  // 確定したら記入。空のあいだは「確定後に記載」と表示される
  operator: '',          // 運営会社名
  partner: '',           // 提携人材紹介会社名
  permit: ''             // 例: '13-ユ-000000'
};
