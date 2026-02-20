# Skill: Debugging Failures
*Category: general | Type: always-load*

## Rules

- If you hit max-turns, the task is too complex — on the next attempt, start by decomposing into smaller steps
- Timeout (20 min) usually means an infinite loop or waiting for a resource that never arrives — check for blocking calls
- If `ANTHROPIC_API_KEY` is missing, the run fails silently at the agent step — check repo Settings → Secrets → Actions
- If a PR was not created after the agent step, check: did the agent have `pull-requests: write` permission? Did it hit max-turns before creating the PR?
- Workflow YAML errors show as red ✗ on the Actions tab before any step runs — always check the workflow file syntax first
- If the distiller step fails but the agent succeeded, skills are lost for that run — check that `anthropic` pip package installed correctly
- `git push` failures in the distiller usually mean a concurrent push from another run — add `git pull --rebase` before push
