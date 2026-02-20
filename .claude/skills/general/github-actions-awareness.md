# Skill: GitHub Actions Awareness
*Category: general | Type: always-load*

## Rules

- Workflow files live in `.github/workflows/` — changes there take effect on the NEXT run, not the current one
- `GITHUB_TOKEN` has write access to the repo but cannot trigger new workflow runs (prevents infinite loops)
- The agent runs as `github-actions[bot]` — PRs it opens are attributed to this user
- `secrets.ANTHROPIC_API_KEY` must be set in repo Settings → Secrets → Actions for the agent to function
- GitHub Pages deploys from the `main` branch automatically — merging a PR triggers deployment within ~60 seconds
- Max run time is set to 20 minutes (`timeout-minutes: 20`) — break large tasks into smaller issues if they risk hitting this
