# Skill: PR Conventions
*Category: general | Type: always-load*

## Rules

- Always write a PR title in imperative mood: "Add X", "Fix Y", "Update Z" — not "Added" or "Adding"
- PR description must include: **What** was changed, **Why** it was changed, and **How to verify** it works
- Never open a PR that touches more than one logical concern — split into separate PRs if needed
- If the task is unclear after reading the issue, implement the most conservative interpretation and note the ambiguity in the PR description
- Always check that `index.html` remains self-contained (no external file dependencies added)
