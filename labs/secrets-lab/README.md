# Lab 1: a secret, a gate, and a fork

**25 minutes. Pairs.**

1. In your repo: **Settings, Secrets and variables, Actions**.
   - Secrets tab: **New repository secret**, name `DEMO_SECRET`, any fake value.
   - Variables tab: **New repository variable**, name `GREETING`, any text.
2. Create `.github/workflows/secrets-lab.yml` that prints `GREETING`, prints
   `DEMO_SECRET`, and prints the **length** of `DEMO_SECRET`.
   Pass both in through `env:`, then use `$GREETING`, `$DEMO` and `${#DEMO}`.
3. **Settings, Environments, New environment** called `staging`. Tick
   **Required reviewers** and add your teammate.
4. Add a second job with `environment: staging` and `needs:` on the first.
   Run it from the Actions tab and watch it wait for your teammate.
5. **Bonus:** inside `staging`, add an environment secret `STAGING_ONLY`.
   Print its length in both jobs. Which one sees it, and why?

## What you should see

- The greeting in full.
- `***` where the secret is.
- A number for its length.
- `0` for the staging-only secret in the first job, a real length in the second.

## If it goes wrong

| You see | It is usually |
|---|---|
| The secret printed in full | You created it on the Variables tab |
| The second job never waits | The environment name in the file does not match Settings, so GitHub made a new unprotected one |
| You cannot approve | Prevent self-review is on, or you are the only reviewer. Ask your teammate |
