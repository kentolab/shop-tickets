# shop-tickets

Practice tickets from **Hanami Goods**, a mock online shop. I work here as if I were a junior engineer on the team: I pick up a ticket (GitHub Issue), fix bugs or add features on a branch, open a pull request, and get a code review before merging.

## How work flows

1. A ticket is filed as a GitHub Issue (e.g. a bug report from the accounting team).
2. Create a branch from `main` (`fix/...` for bug fixes, `feature/...` for new features).
3. Commit in small steps with English commit messages.
4. Open a pull request that links the Issue (`Closes #1`) and explains the cause, the change, and how it was verified.
5. After review, merge into `main`.

## Folder layout

| Path | What it holds |
|---|---|
| `sales_report.py` | Existing weekly sales report script (written by the backend team) |
| `daily/` | Daily reports, one file per day (`daily/YYYY-MM-DD.md`) |
| `reviews/weekly/` | Weekly reviews with week-over-week numbers (`reviews/weekly/2026-W48.md`) |
| `reviews/monthly/` | Monthly reviews with month-over-month numbers (`reviews/monthly/2026-11.md`) |
| `templates/` | Templates for the daily, weekly and monthly reports |

## Run

```
python sales_report.py
```

Requires Python 3.
