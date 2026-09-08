#!/usr/bin/env python3
"""
Regenerates the progress table in the root README.md by counting solved
problems in each patterns/<pattern>/README.md table.

A problem counts as "solved" once its row in the pattern README is no longer
the placeholder "_none yet_" row. Run manually with `python3 scripts/update_progress.py`,
or let .github/workflows/update-readme.yml run it automatically on push.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATTERNS_DIR = ROOT / "patterns"
README = ROOT / "README.md"

# NeetCode 150's official per-pattern counts (neetcode.io/practice/neetcode150).
# "Advanced Graphs" is folded into "Graphs" and "1-D"/"2-D DP" are folded into
# "Dynamic Programming" here to keep this repo's 16-pattern layout; counts still
# sum to 150.
TOTALS = {
    "arrays-hashing": 9,
    "two-pointers": 5,
    "sliding-window": 6,
    "stack": 6,
    "binary-search": 7,
    "linked-list": 11,
    "trees": 15,
    "tries": 3,
    "heap-priority-queue": 7,
    "backtracking": 10,
    "graphs": 19,
    "dynamic-programming": 23,
    "greedy": 8,
    "intervals": 6,
    "math-geometry": 8,
    "bit-manipulation": 7,
}

DISPLAY_NAMES = {
    "arrays-hashing": "Arrays & Hashing",
    "two-pointers": "Two Pointers",
    "sliding-window": "Sliding Window",
    "stack": "Stack",
    "binary-search": "Binary Search",
    "linked-list": "Linked List",
    "trees": "Trees",
    "tries": "Tries",
    "heap-priority-queue": "Heap / Priority Queue",
    "backtracking": "Backtracking",
    "graphs": "Graphs",
    "dynamic-programming": "Dynamic Programming",
    "greedy": "Greedy",
    "intervals": "Intervals",
    "math-geometry": "Math & Geometry",
    "bit-manipulation": "Bit Manipulation",
}


def count_solved(pattern_readme: Path) -> int:
    """Count non-placeholder rows in the pattern's problems table."""
    if not pattern_readme.exists():
        return 0
    text = pattern_readme.read_text()
    rows = re.findall(r"^\|.+\|.+\|.+\|.+\|$", text, re.MULTILINE)
    # Drop the header row and the separator row (---), and the placeholder row.
    solved = [
        r for r in rows
        if "_none yet_" not in r and not re.match(r"^\|\s*#\s*\|", r) and "---" not in r
    ]
    return len(solved)


def bar(pct: float, width: int = 10) -> str:
    filled = round(pct / 100 * width)
    return "█" * filled + "░" * (width - filled)


def build_table() -> str:
    lines = ["| Pattern | Solved | Total | Progress |", "|---|---|---|---|"]
    total_solved = 0
    total_all = 0
    for slug, total in TOTALS.items():
        solved = count_solved(PATTERNS_DIR / slug / "README.md")
        solved = min(solved, total)  # guard against manual edits going over
        pct = (solved / total * 100) if total else 0
        lines.append(f"| {DISPLAY_NAMES[slug]} | {solved} | {total} | {bar(pct)} {pct:.0f}% |")
        total_solved += solved
        total_all += total
    total_pct = (total_solved / total_all * 100) if total_all else 0
    lines.append(f"| **Total** | **{total_solved}** | **{total_all}** | {bar(total_pct)} {total_pct:.0f}% |")
    return "\n".join(lines)


def main():
    readme_text = README.read_text()
    new_table = build_table()
    updated = re.sub(
        r"(<!--PROGRESS_TABLE_START-->\n).*?(\n<!--PROGRESS_TABLE_END-->)",
        lambda m: m.group(1) + new_table + m.group(2),
        readme_text,
        flags=re.DOTALL,
    )
    if updated != readme_text:
        README.write_text(updated)
        print("README.md progress table updated.")
    else:
        print("No changes needed.")


if __name__ == "__main__":
    main()
