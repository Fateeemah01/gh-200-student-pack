# Capstone: build the gate

## The story

Last Friday somebody merged a change that worked fine on their laptop and on
the build server, and broke for half the team on Monday morning. Nobody caught
it because the checks only ever ran in one place.

Your job is to build the gate that would have stopped it.

`check.py` in this folder is the code. It has the bug already. **Do not fix it
yet.** Build the gate, let the gate catch it, then fix it.

---

## Part 1: draw it, 10 minutes

Open [excalidraw.com](https://excalidraw.com). Before anyone touches YAML, draw
the pipeline. Boxes and arrows only. Your drawing has to answer all six:

1. What event starts this?
2. What are the jobs, and which of them run at the same time?
3. Which job has to wait for another, and why?
4. What runs more than once, and how many times?
5. What actually stops the merge? (It is not the workflow.)
6. Where does a human read the result without opening a log?

Show it to another team before you build. If they cannot follow it, redraw it.

---

## Part 2: build it, 30 minutes

Create `.github/workflows/pr-gate.yml`. It must do all of this:

| # | Requirement |
|---|-------------|
| 1 | Runs on a **pull request to main**, and can also be started **by hand** |
| 2 | A job that prints **who** opened it, **which branch**, and **which commit**, read from contexts |
| 3 | A job that runs `check.py` on **both Ubuntu and Windows**, using a matrix |
| 4 | That matrix must **not** stop at the first failure. You want to see both results |
| 5 | A final job that **waits for the other two** and runs **even when they fail** |
| 6 | That final job writes a **pass or fail table** to the run summary |
| 7 | Every `uses:` is pinned to a **full commit SHA**, with the version in a comment |
| 8 | Branch protection on `main` requires your check, so a red run **blocks the merge** |

## Part 3: prove it, 5 minutes

1. Open a pull request. Watch Ubuntu go green and Windows go red.
2. Screenshot the merge button being unavailable. That is the whole point.
3. Now fix `check.py`. One line.
4. Push the fix. Watch both legs go green and the merge unlock.

---

## Done when

Someone who was not on your team can open your pull request and, **without
opening a single log**, say what broke and on which operating system.

## Hints, if you are stuck

- Requirement 4 is one key on the `strategy` block.
- Requirement 5 is one key in an `if:`.
- Requirement 6 is a file path in an environment variable. You used it in Lab 3.
- Requirement 8 is not in the YAML at all. It is in Settings.
