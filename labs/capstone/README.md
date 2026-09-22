# Capstone: build the gate

**30 minutes. In your team. One person types, swap halfway.**

> Syntax for everything below: **[../../CHEATSHEET.md](../../CHEATSHEET.md)**.
> You are not expected to remember any of it. Look it up.

---

## The story

Last Friday somebody merged a change that worked on their laptop and worked on
the build server. On Monday it was broken for half the team. Nobody caught it,
because the checks only ever ran in one place.

`check.py` in this folder is that code. The bug is already in it.

**Do not fix it yet.** Build the gate first. Let the gate catch it. Then fix it.
Fixing the bug before you have seen the gate catch it skips the entire point.

---

## What you are building

One workflow file that stands between a pull request and `main`, and refuses to
let a broken change through. Not a workflow that *reports* a problem. One that
*stops* it.

Everything you need you did today. Nothing here is new.

---

## Part 1: draw it, 7 minutes

Open [excalidraw.com](https://excalidraw.com). **Nobody opens an editor yet.**

Boxes and arrows. Four questions:

1. What event starts this?
2. What runs **more than once**, and how many times?
3. **What actually stops the merge?** (It is not the workflow file.)
4. How will somebody tell **which** operating system broke, without opening a log?

Seven minutes is not long. Do not make it pretty, make it answer the four.

---

## Part 2: build it, 18 minutes

Create `.github/workflows/pr-gate.yml`.

| # | Requirement |
|---|-------------|
| 1 | Runs on a **pull request to main**, and can also be started **by hand** |
| 2 | Runs `check.py` on **both Ubuntu and Windows**, using a matrix |
| 3 | The matrix does **not** stop at the first failure |
| 4 | Every `uses:` is pinned to a **full commit SHA**, with the version in a comment |
| 5 | Branch protection on `main` makes a red run **block the merge** |

You will need `actions/checkout` to get the code onto the runner, and
`actions/setup-python` to have a Python to run it with. Both are in the cheatsheet
with SHAs you can copy.

---

## Why each requirement is there

**1. Two triggers.** `pull_request` is the one that matters: it runs the gate
before the merge, which is the only moment stopping it is useful.
`workflow_dispatch` is for you, so you can re-run it by hand while building
instead of pushing a commit every time.

**2. Two operating systems.** This is the whole story. The bug is invisible on one
platform and obvious on the other. A matrix means you write the job once and
GitHub runs it once per entry.

**3. Do not stop at the first failure.** By default one red leg cancels the
others. That is efficient and it is useless for diagnosis: you see one failure and
cannot tell whether the other platform is fine or also broken.

**4. Pinned actions.** A tag is a pointer, and pointers move. Reference an action
by tag and somebody else's new code can start running in your pipeline without a
pull request in your repo. A commit SHA cannot move.

**5. The gate is not the workflow.** The one people get wrong. A workflow
*reports* a result. Only a branch protection rule can *enforce* it. Without it you
have built a very informative sign next to an open door.

---

## Hints

Open one at a time, only when properly stuck.

<details>
<summary><b>Hint 1</b> &nbsp; How do I run the same job on two operating systems?</summary>

Under the job add a `strategy` block, and under that a `matrix`. Give it a key
with a list of two values. Then use that value in `runs-on` with an expression
instead of hardcoding a label.

Cheatsheet: *Running the same job several times*.
</details>

<details>
<summary><b>Hint 2</b> &nbsp; One leg failed and the other said "cancelled"</summary>

That is requirement 3, and it is the default behaviour. One key, set to `false`.
It lives on the `strategy` block, next to `matrix`, **not inside it**.
</details>

<details>
<summary><b>Hint 3</b> &nbsp; My script cannot find itself / ModuleNotFound / no such file</summary>

Nothing of yours is on the runner until you check it out. Add
`actions/checkout` as the first step. And you need a Python: `actions/setup-python`.

Both are in the cheatsheet under *Steps: run versus uses*, with SHAs.
</details>

<details>
<summary><b>Hint 4</b> &nbsp; Where do I get the SHA for an action?</summary>

Open the action's repository, go to **Releases**, find the version you want, and
copy the full 40 character commit hash. Put the readable version in a trailing
comment so the next person can tell what it is.

Or copy the two in the cheatsheet, which are current.
</details>

<details>
<summary><b>Hint 5</b> &nbsp; My run is red but I can still merge</summary>

Requirement 5. **Settings**, then **Rules** or **Branches**, add a rule on `main`
requiring a status check to pass.

Two traps:
- The name to pick is the **job** name, not the workflow name. From a matrix each
  leg has its own name with the value in brackets, so you are **not** looking for
  `check`.
- The check only appears in that list **after it has run at least once.**
</details>

---

## Common mistakes

| What you see | What it usually is |
|---|---|
| The workflow never runs on your PR | `on:` is `push`, not `pull_request` |
| Only one OS ran | Missing requirement 3, the other leg was cancelled |
| `No such file or directory` | No `actions/checkout` step |
| `python: command not found` | No `actions/setup-python` step |
| Check not listed in branch protection | It has to have run at least once first |
| Still able to merge on red | You are an admin, and rules skip admins by default |

---

## Part 3: prove it, 5 minutes

1. Open a pull request from a branch. One OS goes green, the other red.
2. **Screenshot the merge button you cannot press.** That is the deliverable.
3. Fix `check.py`. One line.
4. Push. Watch both legs go green and the merge unlock.

### Reading the failure

Do not open the longest log and scroll. Do this:

1. Find the **red X** in the job list on the left. That names the leg that broke.
2. Read the **annotations** at the top of the run page first.
3. In the log, `Process completed with exit code 1` is the **symptom**. The
   **cause is the line above it**.

---

## Done when

Somebody who was not on your team can open your pull request and, **without
opening a single log**, say what broke and on which operating system.

---

## If you finish early

- Add `macos-latest` as a third leg. It passes. Work out why.
- Make the gate skip when only Markdown changed. Look up `paths-ignore`.
- Have a third job write a summary table of which legs passed. You need
  `needs:`, `if: always()` and `$GITHUB_STEP_SUMMARY`, which is tomorrow morning.
