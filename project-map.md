# Project Map — index.html Structure

Quick reference for navigating the Flywheel dashboard codebase. All application code lives in a single file: `index.html`

---

## HTML Head (lines 1-8)
DOCTYPE, meta tags, fonts (JetBrains Mono + DM Sans from Google Fonts CDN)

## CSS (lines 9-424)
Note: CSS ends at line 424, body starts at line 426

### Variables and root (lines 10-31)
Custom properties: color palette (void/surface/elevated/hover backgrounds, cyan/green/amber/red/purple accents), fonts (mono/sans), spacing, border-radius

### Global reset and body (lines 33-60)
Box-sizing reset, body background, ambient gradient animation with drift keyframes

### Layout (lines 61-62)
Main `.app` container — max-width 1400px, centered, padding

### Header (lines 64-130)
Header bar with logo (spinning gradient), title text, status badge with pulsing dot (idle/active/error states)

### Grid system (lines 132-141)
3-column grid for stats, 2-column grid for main content, responsive collapse

### Cards (lines 143-167)
Base card styles, titles with icon prefixes, hover effects

### Stat cards (lines 168-187)
Large numeric values with color variants (cyan/green/amber/red/purple), stat labels

### Activity feed (lines 188-230)
Feed list items with colored dots (commit/pr/issue/error), timestamps, text formatting

### Task queue (lines 231-273)
Task cards with ID badges, titles, status pills (queued/running/done)

### Config panel (lines 274-297)
Key-value rows for agent configuration display

### Terminal (lines 298-317)
Code-style log output with color classes (prompt/info/warn/err/dim), fixed height with scroll

### Setup banner (lines 318-359)
Onboarding UI with instructions, code snippets, centered layout

### Input area and buttons (lines 360-402)
Form inputs with focus states, primary action buttons with hover effects

### Footer (lines 403-413)
Centered version info and credits

### Responsive (lines 414-418)
Media query for mobile: collapse grids to single column, stack header

### Scrollbar (lines 420-424)
Custom webkit scrollbar styling

## HTML Body (lines 426-591)

### Header section (lines 430-443)
Logo, branding, status indicator

### Setup banner (lines 445-470)
Initial connection form — repo input, PAT input, connect button, instructions

### Stats grid (lines 472-494)
Four stat cards: Total Tasks, Commits, PRs Merged, Agent Spend (red) (hidden until connected)

### Main grid (lines 496-568)
Two-column layout:
- **Left**: Activity feed card (lines 499-511)
- **Right column** (lines 513-567):
  - Agent Config card (lines 517-546) — model, mode, schedule, repo, pages, auth, disconnect button
  - Workflow Runs card (lines 548-554)
  - Dispatch Task card (lines 556-566) — input field + create issue button

### Task queue card (lines 570-576)
Displays open/closed agent-task issues (hidden until connected)

### Terminal log card (lines 578-586)
Scrollable log output for dashboard events

### Footer (lines 588-590)
Version info

## JavaScript (lines 593-1042)

### State and config (lines 594-602)
Global state object (repo, pat, connected), localStorage persistence, constants (GITHUB_API), DOM helper

### Terminal logging (lines 604-613)
Log function with timestamp formatting

### Connection management (lines 615-647)
`connectRepo()` — validate input, save to localStorage, initialize (lines 615-629)
`disconnect()` — clear state, reset UI, hide main panels (lines 631-647)

### GitHub API helpers (lines 649-710)
`ghFetch()` — GET requests with auth, rate limit handling, error logging (lines 649-689)
`ghPost()` — POST requests for creating issues (lines 691-710)

### Initialization (lines 712-767)
`init()` — connect to repo, test connection, show UI, load all data, display auth status, start refresh loop

### Data loading functions (lines 769-960)
`loadIssues()` — fetch agent-task issues, populate task queue, update stats (lines 769-802)
`loadCommits()` — fetch commits, filter agent commits, update stat (lines 804-817)
`loadPRs()` — fetch PRs, count merged, update stat (lines 819-826)
`loadWorkflowRuns()` — fetch recent Actions runs, display status (lines 828-860)
`loadCostData()` — fetch issue comments, parse Claude Code Report costs, aggregate spend (lines 863-921)
`loadActivity()` — combine commits/issues/PRs, sort by time, populate feed (lines 923-960)

### Task dispatch (lines 962-997)
`dispatchTask()` — create issue via API (if PAT) or open GitHub issue form

### Utilities (lines 999-1013)
`escHtml()` — XSS protection, sanitize text (lines 999-1004)
`timeAgo()` — relative timestamp formatting (lines 1006-1013)

### Auto-refresh (lines 1015-1035)
Rate-limited polling: 60s with PAT, 5min without PAT. Handles rate limit awareness.

### Boot (lines 1037-1041)
Auto-connect if repo saved in localStorage

---

## Recent Changes
From CHANGELOG.md v1.0.0 (2026-02-11):
- Initial dashboard UI — self-contained single-page app
- GitHub Actions workflow for event-driven Claude Code agent
- Activity feed, task queue, stats, terminal log
- Task dispatch (creates GitHub Issues from dashboard)
- Auto-refresh polling with rate limit awareness (60s with PAT, 5min without)
- Cost tracking: parses Claude Code Report comments to display Agent Spend stat
