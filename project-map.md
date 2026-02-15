# Project Map — index.html Structure

Quick reference for navigating the Flywheel dashboard codebase. All application code lives in a single file: `index.html`

---

## HTML Head (lines 1-8)
DOCTYPE, meta tags, fonts (JetBrains Mono + DM Sans from Google Fonts CDN)

## CSS (lines 9-423)

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

### Stat cards (lines 168-186)
Large numeric values with color variants (cyan/green/amber/purple), stat labels

### Activity feed (lines 187-229)
Feed list items with colored dots (commit/pr/issue/error), timestamps, text formatting

### Task queue (lines 230-272)
Task cards with ID badges, titles, status pills (queued/running/done)

### Config panel (lines 273-296)
Key-value rows for agent configuration display

### Terminal (lines 297-316)
Code-style log output with color classes (prompt/info/warn/err/dim), fixed height with scroll

### Setup banner (lines 317-358)
Onboarding UI with instructions, code snippets, centered layout

### Input area and buttons (lines 359-401)
Form inputs with focus states, primary action buttons with hover effects

### Footer (lines 402-412)
Centered version info and credits

### Responsive (lines 413-417)
Media query for mobile: collapse grids to single column, stack header

### Scrollbar (lines 419-423)
Custom webkit scrollbar styling

## HTML Body (lines 425-585)

### Header section (lines 429-442)
Logo, branding, status indicator

### Setup banner (lines 444-469)
Initial connection form — repo input, PAT input, connect button, instructions

### Stats grid (lines 471-492)
Four stat cards: Total Tasks, Commits, PRs Merged, Total Spend (hidden until connected)

### Main grid (lines 494-566)
Two-column layout:
- **Left**: Activity feed card (lines 497-509)
- **Right column** (lines 511-565):
  - Agent Config card (lines 515-544) — model, mode, schedule, repo, pages, auth, disconnect button
  - Workflow Runs card (lines 546-552)
  - Dispatch Task card (lines 554-564) — input field + create issue button

### Task queue card (lines 568-574)
Displays open/closed agent-task issues (hidden until connected)

### Terminal log card (lines 576-584)
Scrollable log output for dashboard events

### Footer (lines 586-588)
Version info

## JavaScript (lines 591-1005)

### State and config (lines 592-600)
Global state object (repo, pat, connected), localStorage persistence, constants (GITHUB_API), DOM helper

### Terminal logging (lines 602-611)
Log function with timestamp formatting

### Connection management (lines 613-645)
`connectRepo()` — validate input, save to localStorage, initialize
`disconnect()` — clear state, reset UI, hide main panels

### GitHub API helpers (lines 647-697)
`ghFetch()` — GET requests with auth, rate limit handling, error logging
`ghPost()` — POST requests for creating issues

### Initialization (lines 699-753)
`init()` — connect to repo, test connection, show UI, load all data, display auth status

### Data loading functions (lines 755-937)
`loadIssues()` — fetch agent-task issues, populate task queue, update stats (lines 755-788)
`loadCommits()` — fetch commits, filter agent commits, update stat (lines 790-803)
`loadPRs()` — fetch PRs, count merged, update stat (lines 805-812)
`loadCosts()` — fetch issue comments, parse Claude Code Report costs, aggregate spend (lines 814-846)
`loadWorkflowRuns()` — fetch recent Actions runs, display status (lines 848-880)
`loadActivity()` — combine commits/issues/PRs, sort by time, populate feed (lines 882-932)

### Task dispatch (lines 939-974)
`dispatchTask()` — create issue via API (if PAT) or open GitHub issue form

### Utilities (lines 976-990)
`escHtml()` — XSS protection, sanitize text
`timeAgo()` — relative timestamp formatting

### Auto-refresh (lines 992-998)
60-second polling interval for data updates

### Boot (lines 1000-1004)
Auto-connect if repo saved in localStorage

---

## Recent Changes
From CHANGELOG.md v1.0.0 (2026-02-11):
- Initial dashboard UI — self-contained single-page app
- GitHub Actions workflow for event-driven Claude Code agent
- Activity feed, task queue, stats, terminal log
- Task dispatch (creates GitHub Issues from dashboard)
- Auto-refresh polling (60s interval)
