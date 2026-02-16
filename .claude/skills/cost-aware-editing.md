# Efficient Codebase Navigation

## Rules
- ALWAYS read project-map.md first — it maps every section with line ranges
- NEVER read full index.html unless change touches >40% of file
- Use line ranges from project-map.md to read only the relevant 50-200 lines
- If the issue provides line numbers, go directly to those lines
- Solve in minimum tool calls — plan first, execute second
- grep for existing IDs/functions before adding new ones

## Token-saving patterns
- One Read call with a line range is cheaper than multiple Grep calls
- Combine related edits into a single MultiEdit when possible
- Skip exploratory reads — trust the project map
- If a task is purely CSS, only read the CSS section
- If a task is purely JS, only read the relevant JS function block
