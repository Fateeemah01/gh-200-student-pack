# Task 1: same flow, a different workflow

**20 minutes. Pairs. One types, swap at 10.**

Copy this whole folder into your repo so the path stays `labs/flow-task/`.

## The sentence

> On every pull request to main, when someone clicks Run, and every night at
> 02:00 UTC, validate the config files on **Python 3.10** and **Python 3.13**,
> let both finish even if one fails, and block the merge if either is red.

## The five moves

1. **Boxes first, on paper.** When? Where? How many? What steps? Who enforces?
   Show a neighbour before you type anything.
2. **One YAML key per box**, top to bottom: `on`, `runs-on`, `strategy`, `steps`.
3. **Put it in a file**: `.github/workflows/config-check.yml`, on a branch.
4. **Open a pull request** to main. Two checks should appear, one per Python.
5. **Box 5 is a setting**: Settings, Rules, require both checks on main.

## Done when

Two checks run on your pull request, one per Python version, and one of them is
red **for a real reason**. Read the log and say what the reason is.

## Hints, only when stuck

<details><summary>Hint 1: my matrix says Python 3.1 was not found</summary>

YAML read `3.10` as a number and dropped the zero. Quote it: `'3.10'`.
</details>

<details><summary>Hint 2: YAML error near the cron line</summary>

A value starting with `*` means something special in YAML. Quote the whole cron
string, and remember `schedule` is a list, so the line starts with a dash.
</details>

<details><summary>Hint 3: the 3.10 leg fails with AttributeError</summary>

That is the gate working. `datetime.UTC` only exists from Python 3.11. Fix the
script with `datetime.timezone.utc`, push, and watch both go green.
</details>

The answers are on the slides straight after the task.
