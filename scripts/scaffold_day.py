"""Scaffold a new day with solution stubs and an assignment note.

Examples:
    python scripts/scaffold_day.py --day 3 --problems 2
    python scripts/scaffold_day.py --day 10 --problems 3 --dry-run
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import List


REPO_ROOT = Path(__file__).resolve().parent.parent


def _day_str(day: int) -> str:
    return f"day_{day:03d}"


def _solution_stub(problem_index: int) -> str:
    return (
        "from __future__ import annotations\n"
        "\n"
        "def solve():\n"
        "    \"\"\"Add your solution.\"\"\"\n"
        "    raise NotImplementedError\n"
        "\n\n"
        "if __name__ == \"__main__\":\n"
        "    print(solve())\n"
    )


def ensure_day(day: int, problem_count: int, dry_run: bool = False) -> List[Path]:
    created: List[Path] = []

    day_folder = REPO_ROOT / "solutions" / _day_str(day)
    assign_file = REPO_ROOT / "problems" / "daily_assignments" / f"{_day_str(day)}.md"

    if not dry_run:
        day_folder.mkdir(parents=True, exist_ok=True)

    for idx in range(1, problem_count + 1):
        fname = day_folder / f"problem_{idx:02d}.py"
        if dry_run:
            created.append(fname)
            continue
        if fname.exists():
            continue
        fname.write_text(_solution_stub(idx), encoding="utf-8")
        created.append(fname)

    if not assign_file.exists():
        content = (
            f"# { _day_str(day).replace('_', ' ').title() } — Assignments\n\n"
            "Problems (no solutions in this folder):\n"
            + "\n".join(f"{i}. ____" for i in range(1, problem_count + 1))
            + "\n\nNotes:\n- Timebox: ____ minutes\n- Review mistakes in `notes/mistakes_log.md`\n"
        )
        if dry_run:
            created.append(assign_file)
        else:
            assign_file.write_text(content, encoding="utf-8")
            created.append(assign_file)

    return created


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scaffold a new practice day")
    parser.add_argument("--day", type=int, required=True, help="Day number (e.g., 3)")
    parser.add_argument("--problems", type=int, default=3, help="How many problem stubs to create")
    parser.add_argument("--dry-run", action="store_true", help="List what would be created without writing")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    created = ensure_day(args.day, args.problems, dry_run=args.dry_run)
    prefix = "Would create" if args.dry_run else "Created"
    for path in created:
        print(f"{prefix}: {path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
