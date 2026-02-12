# ⚡ Flywheel

**An autonomous, event-driven coding agent powered by Claude Code, hosted on GitHub Pages.**

Flywheel is a self-contained single-page dashboard that serves as the control panel for an autonomous Claude Code agent running in GitHub Actions. Create a GitHub Issue → Claude picks it up → implements the code → opens a PR. The flywheel spins.

## Architecture

```
┌─────────────────────────┐    issue/comment      ┌──────────────────────┐
│  GitHub Pages Dashboard │ ◄──── reads ────────── │  GitHub Repository   │
│  (index.html)           │                        │  (Issues, PRs, Code) │
│                         │                        └──────────┬───────────┘
│  • Task dispatch        │                                   │
│  • Activity feed        │                        triggers   │
│  • Agent logs           │                                   ▼
│  • Stats & metrics      │                        ┌──────────────────────┐
│                         │ ◄──── reads results ── │  GitHub Actions      │
└─────────────────────────┘                        │  (Claude Code Agent) │
                                                   │                      │
                                                   │  • Reads issue       │
                                                   │  • Implements code   │
                                                   │  • Creates PR        │
                                                   │  • Commits changes   │
                                                   └──────────────────────┘
```

## How It Works

1. **You create a GitHub Issue** (labeled `agent-task`) describing what you want built or fixed
2. **Claude Code Agent** (running in GitHub Actions) picks up the issue automatically
3. **Agent implements** the changes, following `CLAUDE.md` guidelines
4. **Agent opens a PR** with the implementation
5. **Dashboard** (GitHub Pages) shows real-time activity, stats, and task status
6. You can also **@claude** in any issue or PR comment for interactive assistance

## Quick Setup

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "feat: initial flywheel setup"
git remote add origin https://github.com/Jacck/flywheel.git
git branch -M main
git push -u origin main
```

### 2. Add API Key
Go to **Settings → Secrets and variables → Actions** and add:
- `ANTHROPIC_API_KEY` — your Anthropic API key

### 3. Install Claude GitHub App
Visit [github.com/apps/claude](https://github.com/apps/claude) and install it on the `flywheel` repository.

### 4. Enable GitHub Pages
Go to **Settings → Pages** → set source to `main` branch, root folder.

Your dashboard will be live at: `https://jacck.github.io/flywheel/`

### 5. Create Your First Task
Create a new Issue with the label `agent-task`:
> **Title:** Add a dark/light theme toggle to the dashboard
>
> **Body:** Implement a theme toggle button in the header that switches between dark and light modes. Persist the choice in localStorage.

The agent will automatically pick it up and create a PR.

## Workflows

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `claude-agent.yml` | `@claude` mentions, `agent-task` issues | Respond to tasks and comments |
| `maintenance.yml` | Daily at 06:00 UTC, manual dispatch | Autonomous repo maintenance |

## Dashboard Features

- **Live stats** — tasks processed, commits, PRs merged
- **Activity feed** — real-time stream of repo events
- **Task queue** — visual queue of agent-task issues
- **Task dispatch** — create new agent tasks from the UI
- **Agent log** — terminal-style event log
- **Auto-refresh** — polls GitHub API every 60 seconds

## Files

```
flywheel/
├── index.html                    # Self-contained dashboard (GitHub Pages)
├── CLAUDE.md                     # Agent behavior guidelines
├── README.md                     # This file
├── CHANGELOG.md                  # Auto-maintained by agent
└── .github/
    └── workflows/
        ├── claude-agent.yml      # Event-driven agent workflow
        └── maintenance.yml       # Scheduled autonomous maintenance
```

## License

MIT
