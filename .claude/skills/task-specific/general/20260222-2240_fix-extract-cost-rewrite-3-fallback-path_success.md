## Skill: Robust CI Cost Extraction via Layered Path Resolution
*Category: cost-tracking | Outcome: SUCCESS | Extracted: 20260222-2240*

### Context
The `extract-cost` step silently wrote `cost_usd: 0.0` to `costs.json` on every run because
hardcoded runner temp paths did not reliably resolve. Three prior FAILURE attempts patched the
path string; the fix was to redesign the strategy entirely.

### Solution Pattern: 3-Fallback Path Resolution

```
Strategy 1 → steps.agent.outputs.execution_file   (action's own output var — authoritative)
Strategy 2 → $RUNNER_TEMP/claude-execution-output.json  (env-var-based, not hardcoded string)
Strategy 3 → glob $RUNNER_TEMP for *execution-output*.json  (survives filename changes)
```

Each strategy logs: path tried → file exists? → parse result → cost value found.
If all three fail, write `0.0` AND emit a visible warning — never fail silently.

### Key Facts
- Correct field name in `claude-code-action` output: **`total_cost_usd`** (not `cost_usd`)
- Pass extracted value downstream via `$GITHUB_OUTPUT` as `TASK_COST`
- `$RUNNER_TEMP` resolves correctly on both GitHub-hosted and self-hosted runners; `/home/runner/work/_temp/` does not

### Rules
- Never hardcode runner filesystem paths — always use `$RUNNER_TEMP`, `$GITHUB_WORKSPACE`, etc.
- Always use the action's own output variable as primary source before falling back to file paths
- Log every resolution attempt — silent `0` fallbacks make cost bugs invisible for days/weeks
- When 3+ consecutive failures share the same root cause, redesign rather than re-patch
