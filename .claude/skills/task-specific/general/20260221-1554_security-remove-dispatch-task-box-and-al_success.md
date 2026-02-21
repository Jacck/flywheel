## Skill: Remove User-Facing Action Capability for Security Hardening
*Category: general | Extracted: 20260221-1554*

- Identify and remove all three layers: UI markup (HTML elements), event wiring (listeners/callbacks), and backend functions (handlers that execute the action) — removing only the UI is insufficient if the function remains callable
- Distinguish between read-only operations (`ghFetch()` for data retrieval) and write operations (`ghPost()`, dispatch functions) to preserve monitoring/display functionality while eliminating action capability
- Verify removal scope by checking for orphaned code: event listeners without targets, functions without callers, and dead imports—these indicate incomplete removal and residual attack surface
- Confirm the action cannot be triggered through alternative paths (direct function calls, alternative buttons, keyboard shortcuts, or programmatic invocation) by searching codebase for function name references
