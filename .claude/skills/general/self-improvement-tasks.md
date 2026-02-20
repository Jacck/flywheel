# Skill: Self-Improvement Tasks
*Category: general | Type: always-load*

## Rules

These rules apply when the task involves editing the agent's own workflow, skills, or configuration.

- You MAY edit: `.claude/skills/`, `.claude/skillbank-index.md`, `CLAUDE.md`, `project-map.md`
- You MAY edit: `.github/workflows/claude-agent.yml` — but only the `prompt:` block or timeout values, not the job structure
- You MAY NOT edit: `.github/scripts/distill.py` — distiller changes require human review
- You MAY NOT change: `permissions:` block, `secrets` references, or the `distiller` job's `if: always()` condition
- Never promote a skill to general if it has only been observed once — patterns need at least 2 occurrences
- When updating `skillbank-index.md`, only add entries — never delete existing ones without explicit instruction
- Self-improvement PRs must include in the description: what behavior this changes and why it is safe to merge
