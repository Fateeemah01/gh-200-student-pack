# GH-200 student pack

**Automate your workflow with GitHub Actions.** Days 1 and 2.

## Start here

| | |
|---|---|
| **[CHEATSHEET.md](CHEATSHEET.md)** | Every bit of syntax from today on one page. Keep it open in a second tab. |
| [GH-200-Day-1-slides.pdf](GH-200-Day-1-slides.pdf) | The deck, 32 slides |
| [labs/](labs/) | Files to copy into your own repo |
| [labs/capstone/](labs/capstone/) | The Day 1 team task, solved step by step at the start of Day 2 |
| [GH-200-Day-2-slides.pdf](GH-200-Day-2-slides.pdf) | Day 2, 90 slides. Every task is followed by its answers. **The cheatsheet is the last five pages** |

## Day 2 labs

| Folder | Task |
|---|---|
| [labs/flow-task/](labs/flow-task/) | Task 1: same flow, a different workflow |
| [labs/syntax-task/](labs/syntax-task/) | Task 2: fill in the five blanks, and how to read a chain |
| [labs/secrets-lab/](labs/secrets-lab/) | Lab 1: a secret, a gate, and a fork |
| [labs/security-task/](labs/security-task/) | Task 3: find six problems in fifteen lines |
| [labs/composite-task/](labs/composite-task/) | Task 4: take the repeat out |
| [labs/final/](labs/final/) | Final task: make it production grade |

The class deploys to a real URL from [Greyisheep/gh-200-deploy](https://github.com/Greyisheep/gh-200-deploy).
Read its `.github/workflows/pipeline.yml`: it is the shape to aim for.

## The day

| Time | Part |
|------|------|
| 09:00 | Why automate |
| 09:30 | 1. Fundamentals |
| 11:30 | 2. Workflows, jobs and runners |
| 15:30 | Capstone: build the gate, 30 min |
| 16:00 | Kahoot and wrap up |

Day 2 opens with the capstone solved as a flowchart, then outputs and chains,
secrets and environments, production CI, a real deploy, security and speed,
reusable workflows and composite actions, and organisation settings.

## The three things worth remembering

1. **Every job is a brand new machine.** Nothing on disk survives between jobs.
2. **A workflow reports. A branch protection rule enforces.** They are not the
   same thing, and only one of them stops a merge.
3. **The first red step is the cause.** `Process completed with exit code 1` is
   the symptom, and the real error is the line above it.

## If you get stuck

- [CHEATSHEET.md](CHEATSHEET.md) first, it covers everything we did.
- [Understanding GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions)
- [Workflow syntax reference](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
