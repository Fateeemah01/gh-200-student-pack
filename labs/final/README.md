# Final task: make it production grade

**30 minutes. Pairs. 10 minutes finding, 20 fixing.**

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

## Check your work with two tools

Both run in seconds and need nothing installed on GitHub.

```bash
# actionlint: finds mistakes (needs Docker)
docker run --rm -v "$PWD:/repo" --workdir /repo rhysd/actionlint:latest -color labs/final/deploy.yml

# zizmor: finds security problems (needs Python)
pipx run zizmor labs/final/deploy.yml
```

Run them on the original first, then on your version.

Patterns you need are in the slides, Parts 1 to 4, and the cheatsheet at the
back of the Day 2 slide PDF. The answers are on the slides after the task.
