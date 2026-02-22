## Skill: Static Content Update with Pipeline Validation
*Category: general | Extracted: 20260222*

- Identify the single file containing the target content and verify it's the only necessary change before modifying to avoid unintended side effects
- Update static strings with concrete, immutable values (like build dates in ISO format) rather than dynamic references to ensure consistency across the pipeline
- Validate that downstream artifacts (like `costs.json`) are generated after the change to confirm the full integration pipeline executed successfully
- Keep UI text changes minimal and self-contained to reduce merge complexity and make the change reviewable at a glance
