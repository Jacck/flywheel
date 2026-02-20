# Skill: Git Operations
*Category: general | Type: always-load*

## Rules

- Branch naming: `agent/ISSUE-NUMBER-short-slug` — e.g. `agent/42-add-cost-display`
- Commit message format: `type(scope): description` — e.g. `feat(dashboard): add cost per run display`
- Valid types: `feat`, `fix`, `refactor`, `docs`, `chore`, `style`
- Never force-push — if you need to amend, create a new commit
- Never commit directly to `main` — always work on a branch and open a PR
- The distiller job commits skills directly to `main` — this is the only exception and is handled by the workflow, not the agent
- Always run `git diff --stat` before committing to confirm only intended files are staged
