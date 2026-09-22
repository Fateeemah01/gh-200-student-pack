# GH-200 student pack

**Automate your workflow with GitHub Actions.** Day 1.

## Start here

| | |
|---|---|
| **[CHEATSHEET.md](CHEATSHEET.md)** | Every bit of syntax from today on one page. Keep it open in a second tab. |
| [GH-200-Day-1-slides.pdf](GH-200-Day-1-slides.pdf) | The deck, 32 slides |
| [labs/](labs/) | Files to copy into your own repo |
| [labs/capstone/](labs/capstone/) | The end-of-day team task |

## The day

| Time | Part |
|------|------|
| 09:00 | Why automate |
| 09:30 | 1. Fundamentals |
| 11:30 | 2. Workflows, jobs and runners |
| 15:30 | Capstone: build the gate, 30 min |
| 16:00 | Kahoot and wrap up |

Day 1 stops at workflows, actions and runners. Variables, contexts and
expressions open Day 2, followed by artifacts, caching, environments and reuse.

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
