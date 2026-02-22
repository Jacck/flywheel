## Skill: Timestamp Injection at Build Time
*Category: general | Extracted: 20260222-1527*

- Inject dynamic values (dates, versions, build info) into static files during workflow execution rather than hardcoding them manually, using environment variables or direct text replacement in the CI/CD pipeline
- Use ISO 8601 date format (YYYY-MM-DD) for timestamps as it's unambiguous, sortable, and widely recognized across tools and locales
- Apply existing CSS custom properties (like `var(--text-muted)` and `var(--mono)`) to new UI elements to maintain visual consistency without adding new style rules
- For "last updated" metadata, place it in logical proximity to related information (e.g., near the main title or footer) so users naturally see it when checking freshness
