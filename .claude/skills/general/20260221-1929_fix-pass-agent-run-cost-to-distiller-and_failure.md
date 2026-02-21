## Lesson: Verify intermediate file existence and JSON structure before consuming in downstream jobs

*Category: general | Outcome: FAILURE | Extracted: 20260221-1929*

- Check that `/home/runner/work/_temp/claude-execution-output.json` is actually generated and contains the `total_cost_usd` field before attempting to read it in the distiller job — this file may not exist in all execution contexts or may have a different schema
- Validate that costs.json can be created/appended to and successfully committed before assuming downstream consumers (dashboard API) will have access to it — test the full write-and-commit cycle in the distiller job rather than assuming it works
