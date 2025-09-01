# DSA Mastery

A lightweight structure to practice data structures and algorithms daily.

## Layout

```
roadmap/              # Milestones and progress tracking
problems/             # Curated problems and day-wise assignments (no solutions)
solutions/            # Your code, organized by day
templates/            # Reusable templates for solutions and daily notes
notes/                # Patterns and mistakes log
scripts/              # Utility scripts (e.g., scaffold a new day)
```

## Daily flow
- Pick today’s tasks from `problems/daily_assignments/day_XXX.md`.
- Solve in `solutions/day_XXX/` (copy `templates/solution_template.py` if helpful).
- Log takeaways in `notes/patterns/*` and `notes/mistakes_log.md`.
- Update `roadmap/topic_progress.md` as you finish topics.

## Scaffolding a new day
Use the helper script to create a day folder and problem stubs:

```
python scripts/scaffold_day.py --day 3 --problems 2
```

- Adds `solutions/day_003/problem_01.py`, `problem_02.py`, etc.
- Creates `problems/daily_assignments/day_003.md` if missing.
- Pass `--dry-run` to preview without writing files.

## Templates
- `templates/solution_template.py`: minimal starter for a solution file.
- `templates/daily_notes_template.md`: quick jot template for daily reflections.

## Notes
- Solutions under `solutions/` currently include day 1 and day 2 starters.
- Keep `problems/` free of solutions to avoid spoilers.