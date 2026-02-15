# Project Map — index.html Structure

Quick reference for navigating the Flywheel dashboard codebase. All application code lives in a single file: `index.html`

---

## HTML Head (lines 1-8)
DOCTYPE, meta tags, fonts (JetBrains Mono + DM Sans from Google Fonts CDN)

## CSS (lines 9-428)

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

### Input area and buttons (lines 359-406)
Form inputs and textareas with focus states, primary action buttons with hover effects

### Footer (lines 407-417)
Centered version info and credits

### Responsive (lines 418-422)
Media query for mobile: collapse grids to single column, stack header

### Scrollbar (lines 424-428)
Custom webkit scrollbar styling

## HTML Body (lines 430-590)

### Header section (lines 434-447)
Logo, branding, status indicator

### Setup banner (lines 449-474)
Initial connection form — repo input, PAT input, connect button, instructions

### Stats grid (lines 476-493)
Three stat cards: Total Tasks, Commits, PRs Merged (hidden until connected)

### Main grid (lines 495-567)
Two-column layout:
- **Left**: Activity feed card (lines 498-510)
- **Right column** (lines 512-566):
  - Agent Config card (lines 516-545) — model, mode, schedule, repo, pages, auth, disconnect button
  - Workflow Runs card (lines 547-553)
  - Dispatch Task card (lines 555-565) — textarea (5 rows) + create issue button

### Task queue card (lines 569-575)
Displays open/closed agent-task issues (hidden until connected)

### Terminal log card (lines 577-585)
Scrollable log output for dashboard events

### Footer (lines 587-589)
Version info

## JavaScript (lines 592-967)

### State and config (lines 593-601)
Global state object (repo, pat, connected), localStorage persistence, constants (GITHUB_API), DOM helper

### Terminal logging (lines 603-612)
Log function with timestamp formatting

### Connection management (lines 614-646)
`connectRepo()` — validate input, save to localStorage, initialize
`disconnect()` — clear state, reset UI, hide main panels

### GitHub API helpers (lines 648-698)
`ghFetch()` — GET requests with auth, rate limit handling, error logging
`ghPost()` — POST requests for creating issues

### Initialization (lines 700-754)
`init()` — connect to repo, test connection, show UI, load all data, display auth status

### Data loading functions (lines 756-899)
`loadIssues()` — fetch agent-task issues, populate task queue, update stats (lines 756-789)
`loadCommits()` — fetch commits, filter agent commits, update stat (lines 791-804)
`loadPRs()` — fetch PRs, count merged, update stat (lines 806-813)
`loadWorkflowRuns()` — fetch recent Actions runs, display status (lines 815-847)
`loadActivity()` — combine commits/issues/PRs, sort by time, populate feed (lines 849-899)

### Task dispatch (lines 901-936)
`dispatchTask()` — create issue via API (if PAT) or open GitHub issue form

### Utilities (lines 938-952)
`escHtml()` — XSS protection, sanitize text
`timeAgo()` — relative timestamp formatting

### Auto-refresh (lines 954-960)
60-second polling interval for data updates

### Boot (lines 962-966)
Auto-connect if repo saved in localStorage

---

## Recent Changes
From CHANGELOG.md v1.0.0 (2026-02-11):
- Initial dashboard UI — self-contained single-page app
- GitHub Actions workflow for event-driven Claude Code agent
- Activity feed, task queue, stats, terminal log
- Task dispatch (creates GitHub Issues from dashboard)
- Auto-refresh polling (60s interval)
