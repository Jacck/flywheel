# Skill: Cost Tracking
*Category: task-specific | Load when: issue label is `cost` or `cost-tracking`*

## Architecture

```
claude-code-action
  └── writes execution output → ${{ steps.agent.outputs.execution_file }}
        └── contains: { "total_cost_usd": 0.123, ... }

extract-cost step (in claude-agent.yml)
  └── 3-fallback path resolution (see below)
        └── writes TASK_COST to $GITHUB_OUTPUT

distill.py
  └── reads os.environ["TASK_COST"]
        └── appends { "cost_usd": 0.123, ... } to costs.json

costs.json
  └── read by index.html dashboard via GitHub raw URL
```

## 3-Fallback Path Resolution (the working pattern)

Always resolve the execution output file in this order:

1. `steps.agent.outputs.execution_file` — the action sets this; most reliable
2. `$RUNNER_TEMP/claude-execution-output.json` — env-var-based fallback
3. `glob($RUNNER_TEMP, "*execution-output*.json")` — survives renames

Log each attempt. Never fall through silently to `0.0`.

## Field Names
- Action output JSON field: `total_cost_usd` (float)
- `costs.json` field: `cost_usd` (float)
- `$GITHUB_OUTPUT` variable: `TASK_COST`

## Common Failure Modes
| Symptom | Root Cause | Fix |
|---------|-----------|-----|
| All entries show `0.0` | Hardcoded path not found, silent fallback | Use output var as primary source |
| `KeyError: cost_usd` | Wrong field name | Field is `total_cost_usd` in action output |
| Step succeeds but distiller gets empty string | `$GITHUB_OUTPUT` write missing or wrong var name | Check `echo "TASK_COST=..." >> $GITHUB_OUTPUT` |

## Rules
- Never hardcode `/home/runner/work/_temp/` — use `$RUNNER_TEMP`
- Always log resolution path so failures are diagnosable
- `distill.py` defaults cost to `0.0` if env var missing — a non-zero value confirms the chain worked
