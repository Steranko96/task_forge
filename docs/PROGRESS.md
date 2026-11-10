# Production and learning evidence

Ticket-specific production and learner evidence follows below.

When a ticket is requested, add a `## TSK-XXX` heading and dated updates with:

- Request/scope and dependencies verified.
- Production status, changed files, and important decisions.
- Each acceptance criterion and its actual verification evidence.
- Check commands, working directory, observed result, and environment details
  needed for reproduction (no secrets). Distinguish passed, failed, and not run.
- Blockers, deviations, and any remaining work.
- The single learner TASK.md path when generated.
- Separately dated learner progress, submitted work, review, and evidence.

Record commit references only when commits actually exist. Append corrections
instead of erasing previous failures. A planned check is not a successful check.

## TSK-001

### 2026-11-10 — Production verification and learner handoff

- Request: implement TSK-001 only. Read `AGENTS.md`, `PROJECT.md`, the backlog,
  ticket tracking, this log and `learning/README.md`; inspected the file
  inventory and existing README. No nested AGENTS.md files were present.
- Starting evidence: `git status --short` produced no output; all 46 tracker
  rows were NOT_STARTED/NOT_GENERATED; `app/` contained only `.gitkeep`.
  TSK-001 has no dependencies and is in the first milestone, so no prior
  milestone exit gate blocks it. No other ticket was active.
- Lifecycle: marked only TSK-001 IN_PROGRESS before editing; reviewed the
  production documentation before generating the learner task; then marked
  production DONE and learner READY. No later ticket was started.
- Changed files: `README.md`, `docs/TICKETS.md`, `docs/PROGRESS.md`,
  `learning/tasks/TSK-001/TASK.md` and its `workspace/.gitkeep`.
- Decision: keep the architecture record in the README, the ticket's required
  acceptance surface. Use Django's built-in User and sessions, server-rendered
  forms, required task ownership and PostgreSQL; leave field details to
  TSK-007 and actual configuration/deployment to their own tickets.

Acceptance evidence (manual review against the unchanged TSK-001 block):

| Criterion | Observed evidence | Result |
| --- | --- | --- |
| README describes components | “Components and decisions” assigns responsibilities to browser, Django, auth/ownership, PostgreSQL, tests and delivery stack. | PASS |
| README describes request path | “Request path” traces browser/Caddy/Gunicorn/Django/ORM/PostgreSQL and the response; prose covers GET, POST, authentication, validation and access denial. | PASS |
| README describes excluded features | “Excluded and deferred features” explicitly defers registration, REST API, JS SPA and decorative styling; retains required usable UI and operations. | PASS |
| README describes two-user verification plan | Matrix covers distinct accounts, all task operations, anonymous access, list and direct-object isolation in both directions, forged owner, CSRF, invalid input, logout and persistence. Expected outcomes are explicit and labeled as future verification. | PASS |

The functional requirements are also covered: required ownership is
server-enforced, PostgreSQL is authoritative storage, and “Deployment
boundary” separates public Caddy HTTPS from private app/database services on
the intended DigitalOcean VPS. No infrastructure was provisioned.

Checks and environment:

- All shell checks ran from
  `/Users/tategraham/workspace/tate/taskforge-starter` on macOS with zsh and
  the available `python3`; no packages were installed and no credentials or
  database connections were needed.
- Ran `git diff --check` after the README change: exit 0, no whitespace errors.
  Ran `git diff --stat` and `git diff -- README.md docs/TICKETS.md` and manually
  reviewed the production diff against scope and the four criteria above.
- Opened the official Django 5.2 overview and security URLs via the web tool;
  both resolved to their expected Django documentation pages. Used these
  verified links in the README and learner task; runtime versions remain
  deferred to TSK-003.
- Final local-link, scope, tracker and empty-workspace checks are recorded in
  the dated final-check entry below.
- Runtime Django, database, container and two-user checks: NOT RUN because
  this is a documentation-only ticket and no application exists. The README
  matrix is a plan, not a claim that those later features work.

No blockers or scope deviations. Foundations and the project remain
incomplete. No commits, pushes, PRs or publishing were requested or performed.

Learner handoff: exactly one task at
[`learning/tasks/TSK-001/TASK.md`](../learning/tasks/TSK-001/TASK.md), applying
architecture and request-flow concepts to a private reading journal.
`workspace/` contains only `.gitkeep`; no answer was provided. Learner status
is READY; no learner submission, review or completion is claimed.

### 2026-11-10 — Final checks

Ran `python3 - <<'PY' ... PY` from the repository root, using `pathlib`,
`re` and `subprocess` assertions to inspect Markdown targets, task/workspace
contents, all tracker rows, `app/`, `git diff --name-only` and
`git ls-files --others --exclude-standard`. Observed exit 0 and:

```text
PASS: 10 local Markdown link targets exist
PASS: exactly one learner task; workspace contains only empty .gitkeep
PASS: only TSK-001 is DONE/READY; other 45 tickets unchanged
PASS: application remains a placeholder; changes confined to requested documentation and learner handoff
```

Ran `git diff --check`: exit 0 with no output. `git status --short` showed
only modified README, progress and ticket files, plus the new TSK-001 learner
folder. Reviewed the learner task against all nine required sections in
`learning/README.md`: one written design exercise, binary criteria, local
setup, verified official references, validation and submission guidance;
no solution or future-ticket dependency. All TSK-001 criteria and handoff
requirements are met; no remaining work for this ticket.
