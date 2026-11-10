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

## TSK-002

### 2026-11-10 — Production verification and learner handoff

- Request: implement TSK-002 only. Read `AGENTS.md`, relevant `PROJECT.md`
  sections, the full TSK-002 block and dependency/milestone rules in
  `BACKLOG.md`, `docs/TICKETS.md`, the TSK-001 evidence and
  `learning/README.md`. Inspected tracked files and existing ignore rules;
  `find . -name AGENTS.md -not -path './.git/*'` found only the root agreement.
- Prerequisite: TSK-001 is DONE/READY with an architecture README, recorded
  acceptance evidence and its existing learner task. No other production
  ticket was active. TSK-002 remains within Foundations; no preceding
  milestone exit gate applies. Foundations itself is not complete.
- Starting state: `git status --short` was empty. TSK-002 was
  NOT_STARTED/NOT_GENERATED. `git branch --show-current` returned `main`;
  `git remote -v` showed the credential-free HTTPS origin
  `https://github.com/Steranko96/task_forge.git` for fetch/push.
- Existing repository evidence: `git log --reverse --format='%h %s'` returned
  `ba8fd3a first commit` and `3ad8164 TSK-001: base ticket commit`.
  `git show --stat --oneline ba8fd3a` showed the initial 17-file skeleton.
  A read-only GitHub connector `fetch_commit` call for
  `Steranko96/task_forge`, commit `ba8fd3a`, resolved successfully to
  [`ba8fd3a743fc8bdc1271dc65b95569a4c0c4ab12`](https://github.com/Steranko96/task_forge/commit/ba8fd3a743fc8bdc1271dc65b95569a4c0c4ab12).
  Thus Git and GitHub initialization and the initial commit already existed;
  no reinitialization, replacement repository or new commit was needed.
- Lifecycle: marked only TSK-002 IN_PROGRESS before implementation. Verified
  production changes before generating the learner task; marked DONE/READY
  after the handoff existed. TSK-001 and TSK-003–TSK-046 remain unchanged.
- Changed files: `.gitignore`, `README.md`, `docs/TICKETS.md`, this log,
  `learning/tasks/TSK-002/TASK.md` and its empty `workspace/.gitkeep`.
- Decisions: retain the existing ignore rules and add `env/` plus SQLite
  `-wal`/`-shm` sidecars. Document repository identity, focused ticket
  branches/commits, explicit staging, diff review, safe example configuration
  and response to accidental secret exposure. Do not add configuration
  variables or install software belonging to future tickets.

Acceptance and requirement evidence:

| Criterion / requirement | Observed evidence | Result |
| --- | --- | --- |
| Repository has initial commit | Local root commit assertion and successful GitHub lookup of the same initial commit, as recorded above. | PASS |
| Ignores local secrets | Root and nested `.env` variants, private keys and `secrets/` paths passed effective ignore checks; safe `.env` examples remained trackable. | PASS |
| No credentials tracked | Inspected tracked inventory and credential-free remote; pattern scan of all 19 tracked working files and all 19 unique blobs across 2 reachable commits found no credential candidates. No tracked paths matched ignore rules. | PASS, within inspection limits below |
| Ignore environments and generated assets | Probe matrix covered virtual environments, Python caches/builds, SQLite/journals/sidecars, logs, static collection, uploads and backups; authored static files and migrations remained trackable. | PASS |
| Document branches/commits | README “Version control and local files” gives branch/commit examples and the review/staging procedure, including authorization boundaries. | PASS |

Checks and environment:

- Shell commands ran from
  `/Users/tategraham/workspace/tate/taskforge-starter`, on macOS with zsh,
  Git 2.54.0 and the available `python3` standard library. No packages,
  services, credentials or database connections were needed.
- Ran `python3 - <<'PY' ... PY` with `pathlib`, `re` and `subprocess`
  assertions. Each probe invoked
  `git -c core.excludesFile=/dev/null check-ignore --no-index -q -- <path>`;
  expected return codes were 0 for ignored and 1 for trackable. No probe
  files or real secrets were created. Inspected `.git/info/exclude` implicitly
  through Git's effective result; global ignore rules were disabled.
- Ignored probes (33): `.env`, `.env.local`, `.env.production`, `app/.env`,
  `app/.env.test`, `secrets/password.txt`, `app/secrets/password.txt`,
  `server.pem`, `server.key`, `.venv/bin/python`, `venv/bin/python`,
  `env/bin/python`, `app/.venv/bin/python`,
  `app/__pycache__/views.cpython-313.pyc`, `.pytest_cache/state`,
  `.ruff_cache/state`, `.mypy_cache/state`, `.coverage`, `htmlcov/index.html`,
  `build/output`, `dist/package.whl`, `sample.egg-info/PKG-INFO`,
  `app/db.sqlite3`, `app/db.sqlite3-journal`, `app/db.sqlite3-wal`,
  `app/db.sqlite3-shm`, `app/server.log`, `server.pid`,
  `staticfiles/admin.css`, `media/upload.txt`, `backups/local.txt`,
  `local.dump`, `local.sql.gz`.
- Trackable probes (11): `.env.example`, `.env.production.example`,
  `app/.env.example`, `app/.env.test.example`, `app/static/tasks/style.css`,
  `app/tasks/migrations/0001_initial.py`, `app/templates/tasks/list.html`,
  `app/requirements.txt`, `README.md`, `learning/tasks/TSK-002/TASK.md`,
  `learning/tasks/TSK-002/workspace/.gitkeep`.
- Credential audit used `git ls-files -z` for working files,
  `git rev-list --all` for both reachable commits,
  `git ls-tree -r <commit>` to enumerate unique blobs and
  `git cat-file blob <oid>` to inspect their contents in memory. Patterns
  covered private-key headers, GitHub/OpenAI/AWS token formats, quoted
  password/secret/API-key/token assignments and authenticated HTTP/PostgreSQL
  URLs. Output reported counts only, not file contents. Also asserted that
  no tracked file was effectively ignored and that
  `git rev-list --max-parents=0 HEAD` matched the initial commit above.
  Observed exit 0:

  ```text
  PASS: 33 secret/environment/generated paths ignored; 11 example/source/handoff paths trackable
  PASS: 19 tracked working files and 19 unique blobs across 2 reachable commits have no credential-pattern matches
  PASS: no tracked files match repository ignore rules
  PASS: existing initial commit verified
  ```

- Ran `git diff --check`: exit 0, no whitespace errors. Reviewed
  `git diff --stat` and `git diff -- .gitignore README.md docs/TICKETS.md`
  against the unchanged ticket. Only the intended ignore additions, README
  guidance and TSK-002 lifecycle row were present at that stage.
- Opened and verified all three official Git/GitHub documentation links used
  in the README and learner task via the web tool on 2026-11-10.
- Application tests: NOT RUN; this ticket changes Git hygiene/documentation,
  and `app/` still contains only its placeholder. No future runtime behavior
  is claimed.

Limits: pattern scans and review cannot prove absence of every possible
credential format. The audit covers tracked working files and locally
reachable history, not deleted/unreachable objects, other clones or all
remote branches. The GitHub lookup verifies the existing initial commit;
pending TSK-002 changes remain local and uncommitted. No commits, branch
changes, pushes, PRs, repository creation or publication were performed.
No blockers or scope deviations remain.

Learner handoff: exactly one new task at
[`learning/tasks/TSK-002/TASK.md`](../learning/tasks/TSK-002/TASK.md), using a
fictional weather notebook repository to practice selective tracking, local
history and secret handling. Its workspace contains only an empty `.gitkeep`;
no solution was generated. Learner status is READY, with no submission,
review or completion claimed. Existing learner work was preserved.

### 2026-11-10 — Final checks

From the repository root, ran `python3 - <<'PY' ... PY` with `pathlib`, `re`
and `subprocess` assertions over local Markdown targets, required learner
headings, workspace contents, tracker rows compared with HEAD, the changed
file inventory (`git diff --name-only` plus
`git ls-files --others --exclude-standard`), application contents and HEAD.
Observed exit 0:

```text
PASS: 12 local Markdown link targets exist
PASS: one TSK-002 task, nine required sections, workspace contains only empty .gitkeep
PASS: only TSK-002 tracker row changed; no active ticket remains
PASS: exactly six intended changed/new files; production app, prior learner task and Git history unchanged
```

Manually reviewed the learner task against the nine-section contract: one
local exercise, binary criteria, synthetic data, official references and
validation/submission guidance, with no solution or future dependency.
Ran `git diff --check`: exit 0, no output. `git status --short` showed only
the four modified root/tracking files and the new TSK-002 learner directory.
TSK-002 production is DONE and learner is READY; no subsequent ticket started.
