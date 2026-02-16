Adding a Dashboard Feature
Procedure

Read project-map.md for current line ranges
Add HTML card in the stats grid or main grid section
Add a JS async function loadXxx() with try/catch and UI updates
Add loadXxx() to ALL THREE Promise.all calls (search for "Promise.all" to find them)
Match existing card styles: card-title with icon, stat-value with color class, stat-label
Update project-map.md line ranges after editing

Common pitfalls

Promise.all appears in 3 places — missing one breaks refresh
Always grep for existing element IDs before adding new ones
The $ function is a shorthand for getElementById — use it consistently
Bot comments use github-actions[bot] username, not claude[bot]
