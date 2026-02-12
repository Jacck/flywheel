# CLAUDE.md — Flywheel Agent Guidelines

## Project Overview
Flywheel is a self-contained single-page application hosted on GitHub Pages that serves as both:
1. A **control panel/dashboard** for monitoring autonomous agent activity
2. The **target codebase** that the autonomous Claude Code agent maintains and evolves

## Architecture
- **Single file**: `index.html` — self-contained HTML/CSS/JS application
- **Hosting**: GitHub Pages from the `main` branch root
- **Agent**: Claude Code via GitHub Actions (`anthropics/claude-code-action@v1`)
- **Communication**: GitHub Issues (task queue) → Agent executes → Commits results → Pages updates

## Code Standards
- All application code lives in `index.html` (inline CSS + JS, no external dependencies except CDN)
- Use modern ES6+ JavaScript, CSS custom properties, semantic HTML5
- Keep the app functional without a build step — it must work as a raw static file
- External libraries loaded via CDN only (e.g., cdnjs.cloudflare.com)
- No server-side code — everything runs client-side

## Agent Behavior Rules
- Never force-push or rewrite history
- Always create feature branches for non-trivial changes
- Commit messages follow conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`
- Run validation before committing (check HTML structure, no syntax errors)
- When implementing features from issues, reference the issue number in commits
- Keep `index.html` under 5000 lines — refactor if approaching limit

## Task Processing
- Tasks arrive as GitHub Issues with labels: `agent-task`, `bug`, `feature`, `enhancement`
- Agent reads issue description, implements changes, creates PR
- Complex tasks should be broken into sub-issues if needed
- Always update the dashboard UI to reflect new capabilities added

## Security
- Never commit API keys or secrets
- No eval() or dynamic code execution from user input in the dashboard
- Sanitize any data displayed from GitHub API responses
