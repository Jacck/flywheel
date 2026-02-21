
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
