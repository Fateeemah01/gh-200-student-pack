# Final task: make it production grade

**60 minutes, teams of three. Part 1 for 35 minutes, Part 2 for 25.**

`deploy.yml` in this folder works, and it is dangerous. Rewrite it as a pipeline
you would trust:

- pull requests test, pushes to main deploy
- the deploy waits for the tests and for a human
- nothing unpinned, nothing secret in the file
- nothing a stranger can type ends up inside a command
- a failed step on the server makes the run red
- after deploying, it checks the site is actually up

**Write the list of problems before you touch the YAML.** There are at least
fifteen.

## Part 2: give it a rollback

Write `.github/workflows/rollback.yml`:

- a **Run workflow** button with one input, the commit SHA to put back
- check the input really is a 40-character SHA before using it
- behind the `production` environment, same as a deploy
- in the same concurrency group as the deploy, so they never race
- puts that commit back on the server and checks the health URL
- pass the SHA to the server with `envs:`, never pasted into `script:`

The class repo's [rollback.yml](https://github.com/Greyisheep/gh-200-deploy/blob/main/.github/workflows/rollback.yml)
is the same shape for Cloud Run.

## Check your work with two tools

Both run in seconds and need nothing installed on GitHub.

```bash
# actionlint: finds mistakes (needs Docker)
docker run --rm -v "$PWD:/repo" --workdir /repo rhysd/actionlint:latest -color labs/final/deploy.yml

# zizmor: finds security problems (needs Python)
pipx run zizmor labs/final/deploy.yml
```

Run them on the original first, then on your versions.

Patterns you need are in the slides, Parts 1 to 4, and the cheatsheet at the
back of the Day 2 slide PDF. The answers are on the slides after the task.
