# Skill: API Calls
*Category: general | Type: always-load*

## Rules

- The dashboard fetches data using the GitHub Contents API: `https://api.github.com/repos/Jacck/flywheel/contents/FILENAME`
- Response is base64-encoded — decode with `atob(response.content.replace(/\n/g, ''))`
- Always handle the case where a file does not yet exist (404) — show a sensible empty state, never crash
- Use `fetch` with `cache: 'no-store'` to avoid stale data in the dashboard
- Never hardcode a GitHub token in `index.html` — the Contents API works without auth for public repos
- Rate limit for unauthenticated GitHub API requests: 60/hour — the dashboard should not poll more than once per minute
- JSON files committed to `main` are available via the Contents API within ~5 seconds of the commit landing
