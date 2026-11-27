# Release review — v0.1.0

## Verified locally
- Node test suite: 6 / 6 PASS
- Syntax check: PASS
- Curriculum: 12 modules, 48 weeks, 288 tasks, 24 case prompts and 10 skills

## Not verified
- Chromium Playwright browser smoke test is blocked by the local environment's loopback navigation policy.
- iPhone Safari / PWA installation is not tested.
- GitHub Pages deployment is not tested.

## Limitations
- LocalStorage only; no multi-device sync.
- No automatic ChatGPT API.
- Coaching JSON export includes notes and could include private data.
- Browser storage can be cleared; backups required.
- Additional cases are prompts, not interactive simulations.
- No production readiness assertion.

Release candidate only. Do not tag v1.0.0 until browser and mobile acceptance tests pass.
