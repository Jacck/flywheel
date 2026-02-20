# Skill: Single File Constraint
*Category: general | Type: always-load*

## Rules

- `index.html` is the ONLY output file — the entire app lives in one file, always
- Never create `style.css`, `app.js`, or any companion files — they will not be served by GitHub Pages config
- All CSS goes inside `<style>` tags in `<head>` — never in a separate file or inline `style=""` attributes for anything more than 2 properties
- All JavaScript goes inside `<script>` tags before `</body>` — one script block, not multiple
- External libraries are allowed via CDN `<script src="...">` only — no npm, no bundler, no build step
- If a change would require splitting the file, it is the wrong approach — find a simpler implementation
- Before submitting a PR, verify the result is still a single file with no new file dependencies added
