(() => {
  'use strict';

  const config = window.LP_CONFIG || {};
  const accounts = config.accounts || {};
  const query = new URLSearchParams(window.location.search);
  const requested = (query.get('a') || query.get('src') || '').toLowerCase();
  const account = Object.prototype.hasOwnProperty.call(accounts, requested)
    ? requested
    : config.defaultAccount;
  const allowedHosts = config.lineHosts || ['lin.ee', 'line.me', 'utage-system.com'];

  function parseDestination(value) {
    if (!value || /REPLACE_ME/i.test(value)) return null;
    try {
      const url = new URL(value);
      return url.protocol === 'https:' && !url.username && !url.password ? url : null;
    } catch {
      return null;
    }
  }

  // Site-managed account settings can contain the partner's own registration
  // domain. Query-string overrides must match an explicitly allowed hostname.
  let destination = parseDestination(accounts[account]?.line);
  const override = parseDestination(query.get('line'));
  if (override && allowedHosts.some(host =>
    override.hostname === host || override.hostname.endsWith('.' + host)
  )) {
    destination = override;
  }
  if (destination && config.appendParams && account) {
    destination.searchParams.set('src', account);
  }

  for (const key of ['operator', 'partner', 'permit']) {
    if (typeof config[key] !== 'string' || !config[key].trim()) continue;
    for (const node of document.querySelectorAll('[data-' + key + ']')) {
      node.textContent = config[key].trim();
    }
  }

  const statusDialog = document.getElementById('consult-status');
  let statusOpener = null;
  statusDialog?.addEventListener('close', () => {
    statusOpener?.focus({preventScroll: true});
    statusOpener = null;
  });
  const ctas = document.querySelectorAll('a[data-cta]');
  for (const link of ctas) {
    if (destination) {
      link.href = destination.href;
      link.addEventListener('click', () => {
        if (Array.isArray(window.dataLayer)) {
          window.dataLayer.push({
            event: 'career_hack_line_click',
            placement: link.dataset.cta,
            source_account: account
          });
        }
      });
    } else {
      link.setAttribute('role', 'button');
      link.setAttribute('aria-haspopup', 'dialog');
      link.addEventListener('keydown', event => {
        if (event.key === ' ') {
          event.preventDefault();
          link.click();
        }
      });
      link.addEventListener('click', event => {
        event.preventDefault();
        if (typeof statusDialog?.showModal === 'function') {
          statusOpener = link;
          if (!statusDialog.open) statusDialog.showModal();
        } else {
          window.alert('ただいま受付準備中です。電話相談のお申し込みは、公式LINEの受付開始後にご利用いただけます。');
        }
      });
    }
  }

  const sticky = document.querySelector('[data-sticky]');
  const hero = document.querySelector('[data-cta="hero"]');
  if (!sticky || !hero || !('IntersectionObserver' in window)) return;

  // Keep at most one prominent LINE action on screen. Leave the operator
  // information and disclosures at the bottom unobstructed.
  const inlineActions = [...ctas].filter(link => !sticky.contains(link));
  const footer = document.querySelector('footer');
  const observed = footer ? [...inlineActions, footer] : inlineActions;
  function updateSticky() {
    const someVisible = observed.some(node => {
      const bounds = node.getBoundingClientRect();
      return bounds.top < window.innerHeight && bounds.bottom > 0;
    });
    sticky.hidden = hero.getBoundingClientRect().bottom >= 0 || someVisible;
  }
  const observer = new IntersectionObserver(updateSticky);
  observed.forEach(node => observer.observe(node));
  updateSticky();
})();
