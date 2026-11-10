# TaskForge starter

A planning-only repository for TaskForge, with all 46 production tickets and
one independent learner task generated after each verified ticket.
No production ticket has been started. This folder is not yet a runnable app.

## Start here

1. Extract the ZIP and open the extracted `taskforge-starter/` folder as your
   project in Codex. Keep `AGENTS.md` at its root.
2. Read `PROJECT.md` for requirements, `BACKLOG.md` for the original 46 ticket
   definitions, and `docs/TICKETS.md` for current status.
3. When ready, send: **Implement TSK-001 only. Follow AGENTS.md.**
4. Review the production result, verification evidence, and the one new
   `learning/tasks/TSK-001/TASK.md`. Implement the learner task in its
   `workspace/` folder whenever you choose.
5. Ask for tutoring or a learner review when needed. Request each subsequent
   production ticket explicitly, for example: **Implement TSK-002 only.**

Opening this folder, reading documentation, or asking a question does not
request a production implementation. A completed learner task is not a gate
for requesting the next production ticket.

## Folder guide

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Codex execution and tutoring instructions |
| `PROJECT.md` | TaskForge requirements and updated learning model |
| `BACKLOG.md` | 46 unchanged ticket definitions, dependencies, and acceptance criteria |
| `app/` | Future production Django application; placeholder only |
| `docs/TICKETS.md` | Separate production and learner status for each ID |
| `docs/PROGRESS.md` | Append observed verification and completion evidence |
| `docs/architecture/` | Future decisions; no architecture decisions made yet |
| `docs/operations/` | Future deployment and operations documentation |
| `docs/reference/` | Unmodified source copies and provenance |
| `learning/README.md` | How independent learner tasks work |
| `learning/tasks/` | Empty until a production ticket is verified |

## Starter boundaries

This package prepares folders, ignore rules, and workflow documentation only.
TSK-001 still requires its architecture/scope decisions, request path, and
verification plan. TSK-002 still requires Git/GitHub setup, initial commit,
and a review of ignore rules for the actual environment. No Git repository,
remote, dependencies, Django project, accounts, or deployment is created here.
Installation and test commands will be documented when their tickets implement
them; there is currently no application test suite to run.

The five-day / approximately 50-focused-hour production target and the backlog
estimates are retained. Independent learner practice and tutoring add time.
