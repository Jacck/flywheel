#!/usr/bin/env python3
"""
distill.py — SkillRL-inspired skill distiller for Flywheel
============================================================
Runs after every agent task (success or failure).
Calls Claude Haiku to extract a reusable skill or lesson,
then commits it directly to main.

Environment variables (set by the workflow):
  TASK_TITLE        — GitHub issue title
  TASK_DESCRIPTION  — GitHub issue body
  TASK_LABELS       — comma-separated issue labels
  TASK_OUTCOME      — "success" or "failure"
  PR_NUMBER         — PR number opened by agent (if success)
  PR_TITLE          — PR title (if success)
  PR_BODY           — PR description written by agent (if success)
  ANTHROPIC_API_KEY — injected automatically from secrets
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime, timezone


# ── Config ────────────────────────────────────────────────────────────────────

HAIKU_MODEL    = "claude-haiku-4-5-20251001"
MAX_TOKENS     = 400
SKILLS_DIR     = Path(".claude/skills")
LESSONS_FILE   = Path("lessons.md")
SKILLBANK_FILE = Path(".claude/skillbank-index.md")

# Map issue labels → task-specific skill subdirectory names
LABEL_CATEGORY_MAP = {
    "ui":            "ui-changes",
    "ui-change":     "ui-changes",
    "dashboard":     "ui-changes",
    "cost":          "cost-tracking",
    "cost-tracking": "cost-tracking",
    "workflow":      "workflow-fixes",
    "workflow-fix":  "workflow-fixes",
    "bug":           "bug-fixes",
    "fix":           "bug-fixes",
    "feature":       "new-features",
    "docs":          "documentation",
    "infra":         "infrastructure",
    "agent":         "agent-config",
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def run(cmd: str) -> str:
    """Run a shell command and return stdout."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()


def get_git_diff_summary() -> str:
    """Get a concise summary of what files changed."""
    stat = run("git diff HEAD~1 --stat 2>/dev/null || git diff --cached --stat 2>/dev/null || echo 'no diff available'")
    # Limit to first 30 lines to avoid bloating the prompt
    lines = stat.split("\n")[:30]
    return "\n".join(lines)


def resolve_category(labels_raw: str) -> tuple[str, str]:
    """
    Returns (category_slug, skill_dir_type).
    skill_dir_type is either 'task-specific' or 'general'.
    """
    labels = [l.strip().lower() for l in labels_raw.split(",") if l.strip()]
    for label in labels:
        if label in LABEL_CATEGORY_MAP:
            return LABEL_CATEGORY_MAP[label], "task-specific"
    # No matching label → treat as general
    return "general", "general"


def slugify(text: str, max_len: int = 40) -> str:
    """Turn a string into a safe filename slug."""
    import re
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    slug = re.sub(r"[\s_-]+", "-", slug).strip("-")
    return slug[:max_len]


def call_claude(prompt: str) -> str:
    """Call Claude Haiku via the Anthropic SDK."""
    try:
        import anthropic
        client = anthropic.Anthropic()
        response = client.messages.create(
            model=HAIKU_MODEL,
            max_tokens=MAX_TOKENS,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text.strip()
    except ImportError:
        print("ERROR: anthropic package not installed. Run: pip install anthropic")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR calling Claude API: {e}")
        sys.exit(1)


def update_skillbank_index(skill_path: Path, category: str, skill_type: str, title: str):
    """Add the new skill to skillbank-index.md if not already listed."""
    if not SKILLBANK_FILE.exists():
        return  # index managed separately, don't create here

    content = SKILLBANK_FILE.read_text()
    rel_path = str(skill_path)

    if rel_path in content:
        return  # already indexed

    # Find the right section and append
    section_header = "## General Skills" if skill_type == "general" else f"### {category}"
    if section_header in content:
        content = content.replace(
            section_header,
            f"{section_header}\n- [{title}]({rel_path})"
        )
    else:
        content += f"\n{section_header}\n- [{title}]({rel_path})\n"

    SKILLBANK_FILE.write_text(content)
    print(f"  Updated skillbank-index.md → {rel_path}")


# ── Main distillation logic ───────────────────────────────────────────────────

def distill():
    # Read env vars
    task_title       = os.environ.get("TASK_TITLE", "unknown task")
    task_description = os.environ.get("TASK_DESCRIPTION", "")
    task_labels      = os.environ.get("TASK_LABELS", "")
    outcome          = os.environ.get("TASK_OUTCOME", "failure").lower()
    pr_title         = os.environ.get("PR_TITLE", "")
    pr_body          = os.environ.get("PR_BODY", "")

    timestamp      = datetime.utcnow().strftime("%Y%m%d-%H%M")
    diff_summary   = get_git_diff_summary()
    category, skill_type = resolve_category(task_labels)
    task_slug      = slugify(task_title)

    print(f"\n{'='*60}")
    print(f"Flywheel Distiller — SkillRL Phase 1")
    print(f"Task:    {task_title}")
    print(f"Outcome: {outcome.upper()}")
    print(f"Category: {category} ({skill_type})")
    print(f"{'='*60}\n")

    # ── Build prompt based on outcome ─────────────────────────────────────────

    if outcome == "success":
        prompt = f"""You are a skill extractor for an autonomous coding agent system.

A GitHub Actions coding agent just SUCCESSFULLY completed this task:

TASK TITLE: {task_title}
TASK DESCRIPTION:
{task_description[:800]}

PR TITLE: {pr_title}
PR DESCRIPTION:
{pr_body[:600]}

FILES CHANGED:
{diff_summary}

Extract ONE reusable skill pattern that future agent runs should follow for similar tasks.

Rules:
- 3-5 bullet points maximum
- Focus on WHAT WORKED and WHY — not the specific code values
- Make it general enough to apply to similar future tasks
- Be concrete, not vague ("always check X before Y" not "be careful")
- Do NOT include code snippets

Format your response EXACTLY like this:
## Skill: [short descriptive name]
*Category: {category} | Extracted: {timestamp}*

- [bullet 1]
- [bullet 2]
- [bullet 3]
"""
        skill_dir = SKILLS_DIR / "task-specific" / category
        filename  = f"{timestamp}_{task_slug}_success.md"

    else:  # failure
        prompt = f"""You are a skill extractor for an autonomous coding agent system.

A GitHub Actions coding agent FAILED to complete this task:

TASK TITLE: {task_title}
TASK DESCRIPTION:
{task_description[:800]}

Extract ONE concise failure lesson that future agent runs should remember.

Rules:
- 2-3 bullet points maximum
- Focus on what to AVOID or CHECK FIRST before attempting similar tasks
- Be specific about the failure mode, not generic
- Do NOT speculate about causes — only state what is known

Format your response EXACTLY like this:
## Lesson: [short descriptive name]
*Category: {category} | Outcome: FAILURE | Extracted: {timestamp}*

- [bullet 1]
- [bullet 2]
"""
        skill_dir = SKILLS_DIR / "general"
        filename  = f"{timestamp}_{task_slug}_failure.md"

    # ── Call Haiku ─────────────────────────────────────────────────────────────

    print("Calling Claude Haiku for distillation...")
    skill_content = call_claude(prompt)
    print(f"Distilled:\n{skill_content}\n")

    # ── Write skill file ───────────────────────────────────────────────────────

    skill_dir.mkdir(parents=True, exist_ok=True)
    skill_path = skill_dir / filename
    skill_path.write_text(skill_content + "\n")
    print(f"Written: {skill_path}")

    # ── Update lessons.md ──────────────────────────────────────────────────────

    LESSONS_FILE.touch(exist_ok=True)
    existing = LESSONS_FILE.read_text()

    entry = f"\n---\n*{timestamp} | {task_title} | {outcome.upper()} | {category}*\n\n{skill_content}\n"

    # Prepend so most recent is at top
    LESSONS_FILE.write_text(entry + existing)
    print(f"Updated: {LESSONS_FILE}")

    # ── Update skillbank index ─────────────────────────────────────────────────

    # Extract skill title from first line
    first_line = skill_content.split("\n")[0].replace("## ", "").strip()
    update_skillbank_index(skill_path, category, skill_type, first_line)

    # ── Emit summary for GitHub Actions log ───────────────────────────────────

    print(f"\n✅ Distillation complete")
    print(f"   Skill file : {skill_path}")
    print(f"   Lessons    : {LESSONS_FILE}")
    print(f"   Cost       : ~$0.001 (Haiku)")

    # ── Write costs.json ──────────────────────────────────────────────────────

    costs_file = Path("costs.json")
    existing_costs = json.loads(costs_file.read_text()) if costs_file.exists() else []
    existing_costs.insert(0, {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "issue_title": task_title,
        "outcome": outcome,
        "cost_usd": float(os.environ.get("TASK_COST", 0))
    })
    costs_file.write_text(json.dumps(existing_costs, indent=2))
    print(f"Updated: {costs_file}")


if __name__ == "__main__":
    distill()
