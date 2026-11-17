/* v2 用のアカウント別設定（トップの docs/config.js と同じ仕組み）
 *
 * アカウントごとに変わるのは LINE の URL だけ。ページに名前や顔は出さない。
 *   …/career-hack-lp/v2/?a=riko   → accounts.riko.line
 *   …/career-hack-lp/v2/?a=mina   → accounts.mina.line
 *   ?a= が無い・未登録の値         → defaultAccount
 *   （旧URLの ?src=riko / ?src=mina も同じ扱い）
 *
 * 試しに別のURLへ向けるときは ?line=<URLエンコードしたURL>。
 * lineHosts にあるドメインの https URL だけを受け付ける。
 */
window.LP_CONFIG = {
  defaultAccount: 'riko',

  accounts: {
    // UTAGEで発行したLINE友だち追加URLに差し替える（ダミー）
    riko: { line: 'https://lin.ee/REPLACE_ME_riko' },
    mina: { line: 'https://lin.ee/REPLACE_ME_mina' }
  },

  lineHosts: ['lin.ee', 'line.me', 'utage-system.com'],

  // CTAのURL末尾に ?src=アカウント を付けるか
  appendParams: true
};
