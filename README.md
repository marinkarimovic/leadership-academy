# Leadership Academy 2027 — v0.1.0

Mobile-first local-first PWA. No dependencies or API keys. German UI. Data is stored in browser localStorage, not Git or a cloud database. Do not enter confidential employee or company data. Backups are plain JSON; protect them. Multiple tabs/devices do not sync; use one active device and export backups. Browser storage can be cleared or evicted.

## Run
`npm test` (Node 22+). `npm start` serves on localhost:8080. Open the URL in a browser. For browser tests install Python Playwright and Chromium, then `python tests/browser.py` (CHROMIUM_PATH configurable).

## Publish
In Settings > Pages select Deploy from a branch > main > / (root) after merging the reviewed release branch. Public Pages serves app code publicly; never commit personal exports. On iPhone open HTTPS URL in Safari, Share > Add to Home Screen. Verify offline reload after initial installation.

## Coaching
In Journal choose ISO week. In Coach export a package and inspect it before sharing (includes historical notes and assessments). Ask ChatGPT to return a JSON response with schemaVersion 1, type coaching-response, unique id, feedback string, tasks string array, assessments array with skill, score 1–5, evidence. Save as JSON and import under Coach. Imported tasks can be checked off there. Backup/restore in Karriere. Restore replaces local data after confirmation.

## Scope
12 modules, 48 thematic learning weeks (extra calendar days for catch-up), 288 tasks, 24 case prompts, 10 skills. Book sections are thematic rather than edition-specific page assignments. Case 001 is based on the conversation; other cases are introductory scenario prompts, not completed multi-round simulations. Scores are self or coach assessments, not certifications. Timer assigns sessions to their starting date/week. No concurrent-tab locking, cloud authentication, cross-device sync, automatic AI or CSV export in this release. No claim of production readiness.
