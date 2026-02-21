## Skill: Minimal File Modification for Dashboard Metric Verification
*Category: general | Extracted: 20260221-1702*

- Add a single, non-functional marker (like an HTML comment) to a high-visibility file rather than making logic changes, reducing risk of breaking existing functionality while still triggering system tracking
- Place the marker near the top of the file in a standard format (e.g., `<!-- marker-name -->`) so it's easily discoverable during code review and audit processes
- Use this pattern when the goal is to verify that a system's cost/spend tracking is working correctly by allowing the change itself to appear in CI logs and dashboards as evidence of execution
- Ensure the marker follows a consistent naming convention (e.g., `<!-- task-type-test -->`) to make it machine-readable for future verification steps or automated validation
