# Skill: Code Quality Rules
*Category: general | Type: always-load*

## Rules

- `index.html` must remain a single self-contained file — all CSS and JS inline, no external build step
- Never introduce `<script src="...">` tags pointing to local files — only CDN links are allowed
- Before editing any JavaScript, read the existing event listener structure to avoid duplicate listeners
- Test logic changes mentally against the dashboard's three states: empty (no runs), loading, and populated
- Prefer editing existing functions over adding new ones — the file is intentionally minimal
- Never add `console.log` statements without a corresponding removal plan
