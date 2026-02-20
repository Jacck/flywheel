# Skill: Task Decomposition
*Category: general | Type: always-load*

## Rules

- If a task requires more than 15 tool calls to complete, it is too large — stop, open a comment on the issue explaining the split, and implement only the first logical piece
- A task is too large if it touches more than 3 distinct areas of `index.html` (e.g. HTML structure + CSS + JS logic all at once)
- Split criteria: "add X and also Y" in the same issue = two tasks, not one
- When splitting, name the sub-tasks clearly in your PR description so a human can create follow-up issues
- Never silently do less than asked — if you implement a subset, say so explicitly in the PR
- Dashboard features and workflow changes should always be separate PRs — they have different rollback risk
