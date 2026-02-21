## Lesson: Verify Complete Removal of Dependent Code Before Deletion
*Category: general | Outcome: FAILURE | Extracted: 20260221-1540*

- Before removing a function, search the entire codebase for all references, event listeners, and callbacks that depend on it — incomplete removal leaves broken code paths that cause runtime failures
- When a task specifies "remove X function used only by Y," verify this claim by grepping for all usages first; hidden dependencies in HTML event handlers, closures, or indirect calls can be easily missed during manual inspection
