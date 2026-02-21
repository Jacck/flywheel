# SkillBank Index
*Flywheel SkillRL — Phase 2*

This file is the FIRST thing the agent reads at the start of every task.
Use it to decide which skill files to load before beginning work.

---

## How to use this index

1. Read your task's GitHub issue labels
2. Match labels to the **Task-Specific Skills** section below
3. Load the matching skill file(s) by reading them
4. Always load ALL files listed under **General Skills**

---

## General Skills
- [Lesson: Verify file path accessibility before extracting from runner temp files](.claude/skills/general/20260221-1938_fix-pass-agent-run-cost-to-distiller-and_failure.md)
- [Lesson: Verify intermediate file existence and JSON structure before consuming in downstream jobs](.claude/skills/general/20260221-1929_fix-pass-agent-run-cost-to-distiller-and_failure.md)
- [Lesson: Verify JSON file path accessibility and parsing in workflow context](.claude/skills/general/20260221-1827_fix-pass-agent-run-cost-to-distiller-and_failure.md)
- [Skill: Minimal File Modification for Dashboard Metric Verification](.claude/skills/task-specific/general/20260221-1702_test-verify-agent-spend-updates-on-dashb_success.md)
- [Skill: Enable Reporting in CI/CD Action Configuration](.claude/skills/task-specific/general/20260221-1625_fix-agent-spend-not-updating-on-dashboar_success.md)
- [Skill: Remove Deprecated Commands from Configuration Files](.claude/skills/task-specific/general/20260221-1607_fix-remove-deprecated-set-output-command_success.md)
- [Skill: Remove User-Facing Action Capability for Security Hardening](.claude/skills/task-specific/general/20260221-1554_security-remove-dispatch-task-box-and-al_success.md)
- [Lesson: Verify Complete Removal of Dependent Code Before Deletion](.claude/skills/general/20260221-1540_security-remove-dispatch-task-box-and-al_failure.md)
- [I'd be happy to help extract a failure lesson, but I need additional information about the actual failure that occurred. Could you please provide:](.claude/skills/general/20260220-1606_test-add-a-comment-to-indexhtml_failure.md)
- [Lesson: Verify file existence before referencing in PR descriptions](.claude/skills/general/20260220-1545_test-verify-skillbank-loading_failure.md)
*Load these on EVERY task — no exceptions*

- [PR Conventions](.claude/skills/general/pr-conventions.md)
- [Code Quality Rules](.claude/skills/general/code-quality.md)
- [GitHub Actions Awareness](.claude/skills/general/github-actions-awareness.md)

---

## Task-Specific Skills
*Load based on issue labels*

### Label: `ui` / `ui-change` / `dashboard`
- [UI Changes](.claude/skills/task-specific/ui-changes.md)

### Label: `cost` / `cost-tracking`
- [Cost Tracking](.claude/skills/task-specific/cost-tracking.md)

### Label: `workflow` / `workflow-fix` / `infra`
- [Workflow Fixes](.claude/skills/task-specific/workflow-fixes.md)

---

## Auto-Generated Skills
*Written automatically by the Distiller after each run*
*Newest entries appear at the top of each section*

### task-specific/ui-changes
<!-- distiller inserts here: ui-changes -->

### task-specific/cost-tracking
<!-- distiller inserts here: cost-tracking -->

### task-specific/workflow-fixes
<!-- distiller inserts here: workflow-fixes -->

### general
<!-- distiller inserts here: general -->

---

## Stats
*Updated by distiller*

- Total skills: 5
- Last distillation: *(not yet run)*
- Tasks processed: 0
