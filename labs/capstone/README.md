# Capstone: build the gate

**45 minutes. In your team. One person types, swap every ten minutes.**

> Syntax reference for everything below: **[../../CHEATSHEET.md](../../CHEATSHEET.md)**.
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

One workflow file that stands between a pull request and the `main` branch, and
refuses to let a broken change through. Not a workflow that *reports* a problem.
One that *stops* it.

Everything you need you did today. Nothing here is new.

---

## Part 1: draw it, 10 minutes

Open [excalidraw.com](https://excalidraw.com). **Nobody opens an editor yet.**

Boxes and arrows. Your drawing has to answer all six:

1. What event starts this?
2. What are the jobs, and which of them run at the same time?
3. Which job has to wait for another, and why?
4. What runs more than once, and how many times?
5. **What actually stops the merge?** (It is not the workflow file.)
6. Where does a human read the result without opening a log?

**A good drawing** has one box per job, arrows only where something genuinely
waits, and an annotation on question 5 that is not part of the workflow at all.

**A weak drawing** is a single vertical line of boxes. If yours looks like that,
you have probably made everything wait for everything, which is slow and wrong.

Show it to another team before you build. If they cannot follow it, redraw it.

---

## Part 2: build it, 30 minutes

Create `.github/workflows/pr-gate.yml`.

| # | Requirement |
|---|-------------|
| 1 | Runs on a **pull request to main**, and can also be started **by hand** |
| 2 | A job that prints **who** opened it, **which branch**, **which commit**, read from contexts |
| 3 | A job that runs `check.py` on **both Ubuntu and Windows**, using a matrix |
| 4 | That matrix must **not** stop at the first failure |
| 5 | A final job that **waits for the other two** and runs **even when they fail** |
| 6 | That final job writes a **pass or fail table** to the run summary |
| 7 | Every `uses:` is pinned to a **full commit SHA**, with the version in a comment |
| 8 | Branch protection on `main` requires your check, so a red run **blocks the merge** |

---

## Why each requirement is there

Read this if a requirement feels arbitrary. None of them are.

**1. Two triggers.** `pull_request` is the one that matters: it runs the gate
before the merge, which is the only time stopping it is useful. `workflow_dispatch`
is for you, so you can re-run the thing by hand while you are building it without
pushing a commit every time.

**2. Contexts, not guesswork.** Your gate should be able to say who is asking and
what they are changing. Contexts like `github.actor` are filled in *before* the
job reaches a machine, which is why they work in places an environment variable
does not.

**3. Two operating systems.** This is the whole point of the story. The bug is
invisible on one platform and obvious on the other. A matrix means you write the
job once and GitHub runs it once per entry.

**4. Do not stop at the first failure.** By default, one red leg cancels the
others. That is efficient and it is terrible for diagnosis: you see one failure
and have no idea whether the other platform is fine or also broken. You want both
answers.

**5. A job that runs anyway.** Jobs are skipped by default once something upstream
fails, so the job that summarises the result would never run on exactly the runs
you most need it for. Reports should survive failure.

**6. A table a human reads.** Nobody should have to open a log to find out what
broke. The run summary is a Markdown page attached to the run. You wrote to it in
Lab 3.

**7. Pinned actions.** A tag is a pointer and pointers move. If you reference an
action by tag, somebody else's new code can start running in your pipeline
without a pull request in your repo. A commit SHA cannot move.

**8. The gate is not the workflow.** This is the requirement people get wrong.
A workflow *reports* a result. Only a branch protection rule, or a ruleset, can
*enforce* it. Without it you have built a very informative sign next to an open
door.

---

## Hints

Open these one at a time, only when you are properly stuck. They get more
specific as you go down.

<details>
<summary><b>Hint 1</b> &nbsp; My two jobs run in the wrong order</summary>

You need one key on the job that should go second. It takes the name, or a list
of names, of the jobs it waits for. It does **not** move any files between them.

Docs: [Workflow syntax, `needs`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idneeds)
</details>

<details>
<summary><b>Hint 2</b> &nbsp; How do I run the same job on two operating systems?</summary>

Under the job, add a `strategy` block, and under that a `matrix`. Give it a key
with a list of two values. Then use that value in `runs-on` with an expression
rather than hardcoding a label.

Docs: [Running variations of jobs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations)
</details>

<details>
<summary><b>Hint 3</b> &nbsp; One leg failed and the other said "cancelled"</summary>

That is requirement 4, and it is the default behaviour. There is a single key you
set to `false`, and it lives on the `strategy` block, next to `matrix`, not
inside it.
</details>

<details>
<summary><b>Hint 4</b> &nbsp; My summary job never runs when something fails</summary>

Two separate things are needed and most teams only do one.

`needs:` makes it wait. But a job whose dependency failed is skipped, because
GitHub adds an invisible "only if everything so far succeeded" to every job.
You override that with an `if:` on the job, using one of the status functions
from Part 3. You want the one that runs no matter what.
</details>

<details>
<summary><b>Hint 5</b> &nbsp; How do I write the table?</summary>

There is an environment variable holding a file path. Anything you append to that
file is rendered as Markdown on the run page.

Append, do not overwrite. `>>` and not `>`, or each line wipes the last one.

You can read another job's outcome with the `needs` context, for example
`needs.<job-id>.result`, which is one of `success`, `failure`, `cancelled` or
`skipped`.

Docs: [Adding a job summary](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/control-jobs#adding-a-job-summary)
</details>

<details>
<summary><b>Hint 6</b> &nbsp; Where do I get the SHA for an action?</summary>

Open the action's repository, go to its releases, find the version you want, and
copy the full 40 character commit hash it points at. Put the human readable
version in a comment on the same line so the next person can tell what it is.
</details>

<details>
<summary><b>Hint 7</b> &nbsp; My run is red but I can still merge</summary>

Requirement 8. Repository **Settings**, then **Rules** or **Branches**, and add a
rule on `main` that requires a status check to pass.

The tricky part: the name you must select is the **job** name, not the workflow
name. And when a job comes from a matrix, each leg has its own name that includes
the matrix value in brackets. So you are not looking for `check`.
</details>

---

## Common mistakes

| What you see | What it usually is |
|---|---|
| The workflow never runs on your PR | `on:` is `push`, not `pull_request` |
| Only one OS ran | Missing requirement 4, the other leg was cancelled |
| Summary job skipped | `needs:` without an `if:` |
| Summary shows only one line | You used `>` instead of `>>` |
| Check not listed in branch protection | The check has to have run at least once before it appears |
| Can still merge with a red run | You are an admin, and the rule does not apply to admins by default |

---

## Part 3: prove it, 5 minutes

1. Open a pull request from a branch. Watch one OS go green, the other red.
2. Read the failure. **Screenshot the merge button you cannot press.** That
   screenshot is the deliverable.
3. Now fix `check.py`. It is one line.
4. Push the fix. Watch both legs go green and the merge unlock.

### Reading the failure

Do not open the longest log and scroll. Do this instead:

1. Find the **red X** in the job list on the left. That names the leg that broke.
2. Read the **annotations** at the top of the run page first.
3. In the log, the line that says `Process completed with exit code 1` is the
   *symptom*. The **cause is the line above it**.

---

## Done when

Someone who was not on your team can open your pull request and, **without
opening a single log**, say what broke and on which operating system.

---

## Going further, if you finish early

- Add `macos-latest` as a third matrix leg. It passes. Work out why.
- Make the gate skip entirely when the only changed files are Markdown.
  (Look up `paths-ignore`.)
- Make the report a comment on the pull request instead of a summary. This needs
  write permission on the workflow token, which is a Day 2 conversation, and a
  good one.
