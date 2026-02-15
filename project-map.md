# project-map.md — index.html Structure Map

## HTML Head (lines 1-8)
DOCTYPE, meta tags, title, Google Fonts (JetBrains Mono, DM Sans)

## CSS (lines 9-423)

### Variables and root (lines 10-31)
Custom properties: colors (bg, text, accents), fonts, spacing, radius

### Global reset and body (lines 33-60)
Box-sizing reset, body background, ambient gradient animation (drift keyframes)

### Layout (lines 61-62)
App container: max-width, padding, z-index

### Header (lines 64-131)
Header layout, logo (spinning animation), logo text, status badge, status dot (pulse animation)

### Grid (lines 132-141)
3-column and 2:1 grid layouts

### Cards (lines 142-167)
Card container, title styles, icon styles

### Stat cards (lines 168-186)
Large stat values with color variants, stat labels

### Activity feed (lines 187-229)
Feed list, feed items, dots (commit/pr/issue/error), text, timestamp

### Task queue (lines 230-272)
Task cards, task ID badge, title, status labels (queued/running/done)

### Config panel (lines 273-296)
Config rows, key-value pairs

### Terminal (lines 297-316)
Terminal container, text styles (prompt/info/warn/err/dim)

### Setup banner (lines 317-358)
Setup instructions display, steps, code snippets

### Input area (lines 359-401)
Input fields, buttons (primary and small variants)

### Footer (lines 402-411)
Footer text and styling

### Responsive (lines 413-417)
Mobile: single-column layout, header stacking

### Scrollbar (lines 419-423)
Custom scrollbar styling

## HTML Body (lines 425-585)

### App container (line 427)
Main wrapper

### Header (lines 429-442)
Logo, title, subtitle, status badge

### Setup banner (lines 444-469)
Connection form, repo input, PAT input, instructions

### Stats grid (lines 471-488)
Three stat cards: Total Tasks, Commits, PRs Merged

### Main grid (lines 490-562)
Activity feed (left), right column with Agent Config, Workflow Runs, Dispatch Task

### Task queue card (lines 564-570)
Task queue container (initially hidden)

### Terminal card (lines 572-580)
Agent log terminal

### Footer (lines 582-584)
Version info, branding

## JavaScript (lines 587-962)

### State and config (lines 588-596)
State object, localStorage persistence, GitHub API URL, $ helper

### Terminal logging (lines 598-607)
log() function for terminal output

### Connection management (lines 609-641)
connectRepo(), disconnect() functions

### GitHub API helpers (lines 643-693)
ghFetch() and ghPost() for authenticated API calls

### Initialization (lines 695-749)
init() — connects to repo, displays UI, loads data

### Data loading functions (lines 751-894)
loadIssues(), loadCommits(), loadPRs(), loadWorkflowRuns(), loadActivity()

### Task dispatch (lines 896-931)
dispatchTask() — creates issues via API or opens GitHub

### Utility functions (lines 933-947)
escHtml(), timeAgo()

### Auto-refresh (lines 949-955)
60-second interval for data polling

### Boot sequence (lines 957-961)
Auto-connect if repo stored in localStorage

## Recent Changes

From CHANGELOG.md v1.0.0 (2026-02-11):
- Initial dashboard UI with GitHub integration
- Event-driven + scheduled agent workflows
- Task dispatch, activity feed, stats, terminal log
- Auto-refresh polling (60s interval)
