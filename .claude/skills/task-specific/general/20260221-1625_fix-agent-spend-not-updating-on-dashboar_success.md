## Skill: Enable Reporting in CI/CD Action Configuration
*Category: general | Extracted: 20260221-1625*

- When observing missing data or frozen metrics in dashboards, check if reporting/display flags are disabled in the corresponding CI/CD workflow configuration files
- Locate the action step responsible for generating the missing data and verify that output/reporting parameters are explicitly enabled (display_report, report_output, etc.)
- Post-execution reporting is often controlled by boolean flags that default to false or are commented out; enabling these flags restores data visibility without code logic changes
- Test the fix by triggering a new workflow run and confirming that the previously frozen data now updates and appears in the expected output location (comments, logs, dashboards)
