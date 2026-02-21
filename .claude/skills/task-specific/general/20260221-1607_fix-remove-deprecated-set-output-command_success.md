## Skill: Remove Deprecated Commands from Configuration Files
*Category: general | Extracted: 20260221-1607*

- Locate deprecated commands by searching for specific syntax patterns (e.g., `set-output`, `save-state`) that GitHub Actions or similar platforms have marked obsolete
- Delete the entire line containing the deprecated command rather than attempting to refactor or update it, since the task explicitly states it serves no active purpose
- Verify removal by performing a full-file search for the deprecated command syntax to confirm zero matches remain
- Check related workflow files or documentation to confirm the removed command is not referenced elsewhere before finalizing the change
