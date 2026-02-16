// ============================================================
// FLYWHEEL COST TRACKING — PATCH INSTRUCTIONS
// Apply these 3 changes to index.html in order
// ============================================================

// ============================================================
// CHANGE 1: Add cost stats card to the stats grid
// ============================================================
// FIND this block (around line 487):
//
//     </div>
//   </div>
//
//   <!-- Main content -->
//
// REPLACE WITH (adds a 4th stat card):
//
//     </div>
//     <div class="card">
//       <div class="card-title"><span class="icon">◆</span> Agent Spend</div>
//       <div class="stat-value amber" id="statSpend">—</div>
//       <div class="stat-label" id="statSpendLabel">total cost</div>
//     </div>
//   </div>
//
//   <!-- Main content -->


// ============================================================
// CHANGE 2: Add loadCostData() function
// ============================================================
// FIND this line (around line 857):
//
//   async function loadActivity() {
//
// INSERT THIS ENTIRE BLOCK *BEFORE* that line:

  // ── Load cost data from claude[bot] comments ──
  async function loadCostData() {
    try {
      // Fetch comments from issues with agent-task label
      const issues = await ghFetch('/issues?state=all&labels=agent-task&per_page=50');
      if (!issues || !Array.isArray(issues)) return;

      let totalCost = 0;
      let runCount = 0;
      let lastCost = 0;

      // For each issue, fetch comments and look for cost reports
      const commentPromises = issues.map(issue =>
        ghFetch(`/issues/${issue.number}/comments?per_page=30`)
      );
      const allComments = await Promise.all(commentPromises);

      for (const comments of allComments) {
        if (!comments || !Array.isArray(comments)) continue;
        for (const comment of comments) {
          // Match claude[bot] comments with cost pattern
          if (comment.user && comment.user.login === 'claude[bot]') {
            // Pattern: "Cost: $0.4108" or "total_cost_usd: 0.38"
            const costMatch = comment.body.match(/Cost:\s*\$?([\d.]+)/i);
            if (costMatch) {
              const cost = parseFloat(costMatch[1]);
              if (!isNaN(cost) && cost > 0) {
                totalCost += cost;
                runCount++;
                lastCost = cost; // last one chronologically
              }
            }
          }
        }
      }

      // Update UI
      if (runCount > 0) {
        const avg = totalCost / runCount;
        $('statSpend').textContent = '$' + totalCost.toFixed(2);
        $('statSpendLabel').textContent =
          `${runCount} runs · avg $${avg.toFixed(2)} · last $${lastCost.toFixed(2)}`;
      } else {
        $('statSpend').textContent = '$0.00';
        $('statSpendLabel').textContent = 'no agent runs found';
      }
    } catch (e) {
      console.error('Cost tracking error:', e);
      $('statSpend').textContent = '—';
      $('statSpendLabel').textContent = 'error loading costs';
    }
  }


// ============================================================
// CHANGE 3: Add loadCostData() to all Promise.all calls
// ============================================================
// There are 3 places where Promise.all is called with the load functions.
// Add loadCostData() to each one.
//
// FIND (appears 3 times):
//   Promise.all([loadIssues(), loadCommits(), loadPRs(), loadActivity(), loadWorkflowRuns()])
//
// REPLACE EACH with:
//   Promise.all([loadIssues(), loadCommits(), loadPRs(), loadActivity(), loadWorkflowRuns(), loadCostData()])
