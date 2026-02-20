
---
*20260220-1545 | Test: verify skillbank loading | FAILURE | general*

## Lesson: Verify file existence before referencing in PR descriptions
*Category: general | Outcome: FAILURE | Extracted: 20260220-1545*

- Check that `.claude/skills/` directory and `skillbank-index.md` file actually exist in the repository before attempting to read and document them in the PR description
- Confirm `index.html` file exists and is writable before attempting to add HTML comments to it; missing files will cause task completion to fail
