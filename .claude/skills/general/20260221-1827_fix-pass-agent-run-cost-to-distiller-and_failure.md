## Lesson: Verify JSON file path accessibility and parsing in workflow context
*Category: general | Outcome: FAILURE | Extracted: 20260221-1827*

- Check that hardcoded file paths like `/home/runner/work/_temp/claude-execution-output.json` actually exist and are readable in the GitHub Actions runner environment before attempting to parse them — the path may not be created by previous steps or may differ across runner configurations
- When extracting values from JSON output files in workflow steps, test the Python parsing logic locally first and ensure error handling covers both missing files and missing JSON fields to avoid silent failures that break downstream job dependencies
