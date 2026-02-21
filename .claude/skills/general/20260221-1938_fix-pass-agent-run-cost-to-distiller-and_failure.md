## Lesson: Verify file path accessibility before extracting from runner temp files
*Category: general | Outcome: FAILURE | Extracted: 20260221-1938*

- The `/home/runner/work/_temp/claude-execution-output.json` file path may not exist or be accessible at the step where extraction is attempted — verify the agent step actually creates this file and check its exact location before writing extraction logic
- Incomplete Python code in the task description (missing closing parenthesis and exception handling) indicates the task itself was malformed — always validate that provided code snippets are syntactically complete before implementation
