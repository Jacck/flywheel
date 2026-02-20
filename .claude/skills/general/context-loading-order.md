# Skill: Context Loading Order
*Category: general | Type: always-load*

## Rules

Load context in this exact order at the start of every task:

1. `.claude/skillbank-index.md` — read first to know which skills apply
2. `.claude/skills/general/*.md` — load ALL general skills
3. `.claude/skills/task-specific/[category].md` — load only the matching category
4. `CLAUDE.md` — general agent guidelines for this repo
5. `project-map.md` — codebase structure and file locations
6. The GitHub issue body — the actual task

Do NOT skip steps 1-5 even for tasks that seem simple — the skills contain hard-won lessons that prevent repeated mistakes.
If `skillbank-index.md` does not exist yet, load `CLAUDE.md` and `project-map.md` directly and proceed.
