
---
*20260222-1527 | Add last-updated timestamp to dashboard header | SUCCESS | general*

## Skill: Timestamp Injection at Build Time
*Category: general | Extracted: 20260222-1527*

- Inject dynamic values (dates, versions, build info) into static files during workflow execution rather than hardcoding them manually, using environment variables or direct text replacement in the CI/CD pipeline
- Use ISO 8601 date format (YYYY-MM-DD) for timestamps as it's unambiguous, sortable, and widely recognized across tools and locales
- Apply existing CSS custom properties (like `var(--text-muted)` and `var(--mono)`) to new UI elements to maintain visual consistency without adding new style rules
- For "last updated" metadata, place it in logical proximity to related information (e.g., near the main title or footer) so users naturally see it when checking freshness

---
*20260222-1302 | test: add build date to dashboard footer | SUCCESS | general*

## Skill: Static Content Update with Pipeline Validation
*Category: general | Extracted: 20260222*

- Identify the single file containing the target content and verify it's the only necessary change before modifying to avoid unintended side effects
- Update static strings with concrete, immutable values (like build dates in ISO format) rather than dynamic references to ensure consistency across the pipeline
- Validate that downstream artifacts (like `costs.json`) are generated after the change to confirm the full integration pipeline executed successfully
- Keep UI text changes minimal and self-contained to reduce merge complexity and make the change reviewable at a glance

---
*20260221-1938 | Fix: pass agent run cost to distiller and save to costs.json | FAILURE | general*

## Lesson: Verify file path accessibility before extracting from runner temp files
*Category: general | Outcome: FAILURE | Extracted: 20260221-1938*

- The `/home/runner/work/_temp/claude-execution-output.json` file path may not exist or be accessible at the step where extraction is attempted — verify the agent step actually creates this file and check its exact location before writing extraction logic
- Incomplete Python code in the task description (missing closing parenthesis and exception handling) indicates the task itself was malformed — always validate that provided code snippets are syntactically complete before implementation

---
*20260221-1929 | Fix: pass agent run cost to distiller and save to costs.json | FAILURE | general*

## Lesson: Verify intermediate file existence and JSON structure before consuming in downstream jobs

*Category: general | Outcome: FAILURE | Extracted: 20260221-1929*

- Check that `/home/runner/work/_temp/claude-execution-output.json` is actually generated and contains the `total_cost_usd` field before attempting to read it in the distiller job — this file may not exist in all execution contexts or may have a different schema
- Validate that costs.json can be created/appended to and successfully committed before assuming downstream consumers (dashboard API) will have access to it — test the full write-and-commit cycle in the distiller job rather than assuming it works

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
