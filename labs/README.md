# Lab files

Copy these into **your own** repo at `.github/workflows/`. They do not run from
here, this folder is just the source.

| File | What it does |
|------|--------------|
| `task-1-two-jobs.yml` | Task 1. Two jobs, one file. **Meant to fail.** |
| `capstone/` | The end-of-day team task. Start with its README. |

Syntax reference for all of it: **[../CHEATSHEET.md](../CHEATSHEET.md)**

## task-1-two-jobs.yml

Commit it, open the Actions tab, and look at the run.

Job `one` goes green. Job `two` goes red with:

```
cat: note.txt: No such file or directory
##[error]Process completed with exit code 1.
```

That is the point. Work out why before you read any further.
