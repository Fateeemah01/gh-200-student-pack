# Task 2: fill in the five blanks

**12 minutes. Pairs. Paper first for 4 minutes, then run it.**

Job `test` measures coverage. Job `report` prints it. Job `alert` runs only if
something failed. Replace `___A___` to `___E___`, save it as
`.github/workflows/blanks.yml`, and run it.

```yaml
name: Blanks
on: workflow_dispatch
jobs:
  test:
    runs-on: ubuntu-latest
    outputs:
      score: ${{ ___A___ }}
    steps:
      - id: coverage
        run: echo "percent=87" >> ___B___
  report:
    ___C___: test
    runs-on: ubuntu-latest
    steps:
      - run: echo "Coverage ${{ ___D___ }}%"
  alert:
    needs: [test, report]
    if: ___E___
    runs-on: ubuntu-latest
    steps:
      - run: echo "Something failed"
```

| Blank | What goes there |
|---|---|
| A | The chain that reads the step's output, inside the same job |
| B | The file the step writes to |
| C | The key that lets `report` read `test`'s outputs |
| D | The chain that reads the **job's** output, from another job |
| E | The condition that makes `alert` a failure-only job |

**Done when** the run prints `Coverage 87%` and `alert` shows as skipped.

**Extension:** add `exit 1` to the coverage step after the echo. Predict which
jobs run before you look.

## How to read a chain

Read the dots left to right, like a folder path. At every dot, ask "which one?"

`steps.coverage.outputs.percent` = the **steps** in this job, the one with id
**coverage**, its **outputs**, the one called **percent**.

Every name after the first word was chosen by a person: the step id, the output
name, the job output name. They only have to match where they are set and where
they are read.
