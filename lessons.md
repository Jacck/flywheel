
---
*20260221-1827 | Fix: pass agent run cost to distiller and save to costs.json | FAILURE | general*

## Lesson: Verify JSON file path accessibility and parsing in workflow context
*Category: general | Outcome: FAILURE | Extracted: 20260221-1827*

- Check that hardcoded file paths like `/home/runner/work/_temp/claude-execution-output.json` actually exist and are readable in the GitHub Actions runner environment before attempting to parse them — the path may not be created by previous steps or may differ across runner configurations
- When extracting values from JSON output files in workflow steps, test the Python parsing logic locally first and ensure error handling covers both missing files and missing JSON fields to avoid silent failures that break downstream job dependencies

---
*20260221-1702 | Test: verify agent spend updates on dashboard | SUCCESS | general*

## Skill: Minimal File Modification for Dashboard Metric Verification
*Category: general | Extracted: 20260221-1702*

- Add a single, non-functional marker (like an HTML comment) to a high-visibility file rather than making logic changes, reducing risk of breaking existing functionality while still triggering system tracking
- Place the marker near the top of the file in a standard format (e.g., `<!-- marker-name -->`) so it's easily discoverable during code review and audit processes
- Use this pattern when the goal is to verify that a system's cost/spend tracking is working correctly by allowing the change itself to appear in CI logs and dashboards as evidence of execution
- Ensure the marker follows a consistent naming convention (e.g., `<!-- task-type-test -->`) to make it machine-readable for future verification steps or automated validation

---
*20260221-1625 | Fix: agent spend not updating on dashboard | SUCCESS | general*

## Skill: Enable Reporting in CI/CD Action Configuration
*Category: general | Extracted: 20260221-1625*

- When observing missing data or frozen metrics in dashboards, check if reporting/display flags are disabled in the corresponding CI/CD workflow configuration files
- Locate the action step responsible for generating the missing data and verify that output/reporting parameters are explicitly enabled (display_report, report_output, etc.)
- Post-execution reporting is often controlled by boolean flags that default to false or are commented out; enabling these flags restores data visibility without code logic changes
- Test the fix by triggering a new workflow run and confirming that the previously frozen data now updates and appears in the expected output location (comments, logs, dashboards)

---
*20260221-1607 | Fix: remove deprecated set-output command from distill.py | SUCCESS | general*

## Skill: Remove Deprecated Commands from Configuration Files
*Category: general | Extracted: 20260221-1607*

- Locate deprecated commands by searching for specific syntax patterns (e.g., `set-output`, `save-state`) that GitHub Actions or similar platforms have marked obsolete
- Delete the entire line containing the deprecated command rather than attempting to refactor or update it, since the task explicitly states it serves no active purpose
- Verify removal by performing a full-file search for the deprecated command syntax to confirm zero matches remain
- Check related workflow files or documentation to confirm the removed command is not referenced elsewhere before finalizing the change

---
*20260221-1554 | Security: remove Dispatch Task box and all issue-creation capability from dashboard | SUCCESS | general*

## Skill: Remove User-Facing Action Capability for Security Hardening
*Category: general | Extracted: 20260221-1554*

- Identify and remove all three layers: UI markup (HTML elements), event wiring (listeners/callbacks), and backend functions (handlers that execute the action) — removing only the UI is insufficient if the function remains callable
- Distinguish between read-only operations (`ghFetch()` for data retrieval) and write operations (`ghPost()`, dispatch functions) to preserve monitoring/display functionality while eliminating action capability
- Verify removal scope by checking for orphaned code: event listeners without targets, functions without callers, and dead imports—these indicate incomplete removal and residual attack surface
- Confirm the action cannot be triggered through alternative paths (direct function calls, alternative buttons, keyboard shortcuts, or programmatic invocation) by searching codebase for function name references

---
*20260221-1540 | Security: remove Dispatch Task box and all issue-creation capability from dashboard | FAILURE | general*

## Lesson: Verify Complete Removal of Dependent Code Before Deletion
*Category: general | Outcome: FAILURE | Extracted: 20260221-1540*

- Before removing a function, search the entire codebase for all references, event listeners, and callbacks that depend on it — incomplete removal leaves broken code paths that cause runtime failures
- When a task specifies "remove X function used only by Y," verify this claim by grepping for all usages first; hidden dependencies in HTML event handlers, closures, or indirect calls can be easily missed during manual inspection

---
*20260220-1606 | Test: add a comment to index.html | FAILURE | general*

I'd be happy to help extract a failure lesson, but I need additional information about the actual failure that occurred. Could you please provide:

1. **The error message or logs** from the failed GitHub Actions run
2. **What the agent attempted** (what commands/edits did it try?)
3. **What the actual outcome was** (file not modified? syntax error? permission denied? etc.)

Without knowing the specific failure mode, I cannot extract an accurate, non-speculative lesson.

Once you share the failure details, I'll provide a lesson in the exact format you specified.

---
*20260220-1545 | Test: verify skillbank loading | FAILURE | general*

## Lesson: Verify file existence before referencing in PR descriptions
*Category: general | Outcome: FAILURE | Extracted: 20260220-1545*

- Check that `.claude/skills/` directory and `skillbank-index.md` file actually exist in the repository before attempting to read and document them in the PR description
- Confirm `index.html` file exists and is writable before attempting to add HTML comments to it; missing files will cause task completion to fail
