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

## TSK-003

### 2026-11-10 — Production verification and learner handoff

- Request: implement TSK-003 only. Read the root agreement, `PROJECT.md`,
  backlog requirements/dependency/milestone rules, tracker, earlier production
  evidence and `learning/README.md`. File inventory and `find . -name AGENTS.md
  -not -path './.git/*'` found no nested agreement before implementation.
- Starting state: `git status --short` was empty. TSK-002 was DONE with its
  ignore rules, README guidance, evidence and learner task present. Git history
  contained `bde80ae TSK-002: base ticket commit`. No other ticket was active.
  TSK-003 is within Foundations; no preceding milestone exit gate blocks it.
- Lifecycle: marked only TSK-003 IN_PROGRESS before implementation. Verified
  production before creating the one learner task, then marked DONE/READY.
- Changed files: `.python-version`, `requirements.txt`, `README.md`,
  `app/manage.py`, `app/config/{__init__,settings,urls,asgi,wsgi}.py`,
  `app/tasks/{__init__,admin,apps,models,tests,views}.py`,
  `app/tasks/migrations/__init__.py`, removal of `app/.gitkeep`, the tracker,
  this log, and `learning/tasks/TSK-003/{TASK.md,workspace/.gitkeep}`.
- Decisions: use Python 3.14.x, Django 5.2.19 and its two pinned macOS/Linux
  runtime dependencies (asgiref 3.13.0, sqlparse 0.6.1). `.python-version`
  records the supported series; the README explains the interpreter prerequisite.
  Use Django's generated project and empty registered `tasks` app under `app/`.
  Preserve built-in auth, CSRF and escaping defaults. Replace the generated
  stored development key with a fresh in-memory key per process; no stored
  credential is delivered. Restarted signatures/sessions are intentionally
  temporary until environment-dependent settings in TSK-004.
- SQLite is disposable bootstrap storage only; no task model, health route,
  accounts, PostgreSQL driver or deployment stack was implemented. Foundations
  and the project remain incomplete.

Acceptance and requirement evidence:

| Criterion / requirement | Observed evidence | Result |
| --- | --- | --- |
| Pin Python compatibility and direct dependencies | `.python-version` contains `3.14`; README specifies Python 3.14.x on macOS/Linux. Requirements exactly pin Django 5.2.19 plus its resolved runtime dependencies. Fresh install and `pip freeze` matched all three pins. | PASS |
| Create Django project/app | `startproject config app` and `startapp tasks` produced management, settings, URL, WSGI/ASGI and app skeleton files. `tasks.apps.TasksConfig` is in INSTALLED_APPS; Django checks and migration dry-run passed. | PASS |
| Record installation/run commands | README provides interpreter/venv creation, installation, dependency checks, migrations, loopback runserver, browser URL and shutdown commands, plus development limitations and generated-file guidance. | PASS |
| Clean checkout can install dependencies and start development server | Copied all available tracked and nonignored untracked source paths to a new temporary directory, excluding Git metadata, virtual environments, caches and SQLite. Created a fresh venv, downloaded pinned dependencies without pip cache, migrated new SQLite and started real runserver. GET `/` returned HTTP 200 and Django installation success content. | PASS |

Checks and environment (actual execution):

- Shell work ran from `/Users/tategraham/workspace/tate/taskforge-starter`
  on macOS/zsh. Initial `python3 --version` was 3.14.7. The available
  Homebrew `python3.12 --version` was 3.12.14, but
  `python3.12 -m pip index versions Django` failed with a pyexpat/libexpat
  missing-symbol ImportError. Switched to the working Python 3.14.7 rather
  than altering the host installation. Django's official 5.2 compatibility
  page confirms 3.14 support from 5.2.8 onward.
- Initial sandboxed `python3 -m pip index versions Django`, the first
  `.venv/bin/python -m pip install --no-cache-dir 'Django>=5.2.8,<5.3'`,
  and first temporary-copy install failed because sandbox DNS could not
  resolve PyPI. Retried installation and clean-copy verification with approved
  network access; both succeeded. These were environment access failures,
  not successful dependency checks. pip also reported its unwritable user
  cache; installs used `--no-cache-dir`.
- Ran `python3 -m venv .venv`, then the successful install command above.
  It resolved Django 5.2.19, asgiref 3.13.0 and sqlparse 0.6.1. Ran
  `.venv/bin/python -m django startproject config app`, then from `app/`,
  `../.venv/bin/python manage.py startapp tasks`; both exited 0.
- After settings/README/requirements edits, root checks:
  `.venv/bin/python -m pip check` → no broken requirements;
  `.venv/bin/python app/manage.py check` → no issues;
  `.venv/bin/python app/manage.py makemigrations --check --dry-run` → no changes;
  `git diff --check` → exit 0 with no output.
- Ran `python3 /private/tmp/taskforge_tsk003_verify.py` with network access.
  The temporary verification script copied source via
  `git ls-files --cached --others --exclude-standard -z`, skipped removed
  files, and asserted there was no copied `.venv` or SQLite database. Since
  changes are intentionally uncommitted, this was a clean source snapshot of
  the pending implementation, not a clone of an already published commit.
  Successful copy working directory:
  `/private/var/folders/5_/kkhp61cd4z516r63rwf760pr0000gn/T/taskforge-tsk003-tozd6pvk/checkout`.
  From there it ran these commands using the fresh `.venv/bin/python`:

  ```text
  python3 -m venv .venv
  .venv/bin/python -m pip install --no-cache-dir -r requirements.txt
  .venv/bin/python -m pip check
  .venv/bin/python -m pip freeze
  .venv/bin/python -m django --version
  .venv/bin/python app/manage.py check
  .venv/bin/python app/manage.py makemigrations --check --dry-run
  .venv/bin/python app/manage.py migrate --noinput
  .venv/bin/python -u app/manage.py runserver 127.0.0.1:8000 --noreload
  ```

  Observed all commands succeed; version 5.2.19, exact three dependency pins,
  no broken requirements, no system-check issues, no model changes, and all
  18 built-in migrations applied. The script used `urllib.request.urlopen`
  against the real loopback server, asserted HTTP 200 and
  `The install worked successfully!` in the response, then terminated and
  waited for the server. Its log recorded `GET / HTTP/1.1` 200. No production
  database or credentials were used. The script exited 0.
- Consulted and verified official Python 3.14 venv documentation, Django 5.2
  installation/compatibility, tutorial part 1, and Django 5.2.19 release notes
  via the web tool. Learner references use those verified documentation pages.
- No custom application test suite was run: generated `tests.py` is empty;
  this ticket's runtime acceptance was verified by fresh installation,
  system/migration checks and a real HTTP request. Health and routing tests
  belong to TSK-005. No deployment/production checks were claimed.

Limitations: verified on macOS with Python 3.14.7; Linux is documented but
was not executed here. Windows is outside the documented bootstrap target.
Dependency versions will need deliberate future updates. These are development
settings with temporary keys and SQLite, not production settings. No remaining
blocker or scope deviation; no commits, pushes, PRs or publication performed.

Learner handoff: exactly one new independent museum-catalogue bootstrap task at
[`learning/tasks/TSK-003/TASK.md`](../learning/tasks/TSK-003/TASK.md).
Its workspace contains only empty `.gitkeep`; no solution was provided.
Existing learner tasks/workspaces were preserved. Learner is READY, not reviewed
or COMPLETE. No subsequent production ticket was started.

### 2026-11-10 — Final handoff checks

From the repository root, ran
`.venv/bin/python app/manage.py shell -c "from django.apps import apps; assert apps.is_installed('tasks'); print('PASS: tasks app registered')"`:
exit 0, app registration confirmed. Ran `python3 - <<'PY' ... PY` with
`pathlib`, `re` and `subprocess` assertions over tracker rows compared with
HEAD, all nine required learner headings, task count/workspace contents,
existing learner diffs, local Markdown targets, Python series and the combined
tracked/untracked change inventory. Observed exit 0:

```text
PASS: only TSK-003 tracker row changed; DONE/READY; no active production ticket
PASS: one new task with all nine sections; empty workspace; existing learner work unchanged
PASS: README and learner task local link targets exist
PASS: changes limited to TSK-003; requirements and agreements unchanged; generated runtime files excluded
```

Reviewed generated project/app files and the README/tracker diff. Ran
`git diff --check`: exit 0, no whitespace errors. `git status --short` showed
only the intended README/tracking changes, removed app placeholder and new
runtime source/version/requirements and TSK-003 learner files. The learner
exercise has one independent bootstrap objective, binary criteria, local setup,
official references and submission guidance without a solution. All TSK-003
production and handoff requirements are met; no later ticket started.

## TSK-004

### 2026-11-10 — Production verification and learner handoff

- Request/scope: implement TSK-004 only, separating the key, database,
  debug and allowed-host configuration from source. Read `AGENTS.md`,
  `PROJECT.md`, the requested backlog block and dependency/milestone rules,
  tracker, TSK-003 production evidence, relevant source and `learning/README.md`.
  `find . -name AGENTS.md -not -path './.git/*' -not -path './.venv/*'`
  found only the root agreement. Initial `git status --short` was empty.
- Dependencies: TSK-003 DONE/READY, with actual pinned requirements,
  Python selector, runnable project/app and prior verification evidence present.
  Existing `.venv` reports Python 3.14.7 and Django 5.2.19. No active ticket
  or earlier milestone gate blocks Foundations work. Learner completion
  was not required. TSK-005 and all later tickets remain untouched.
- Lifecycle: changed only TSK-004 to IN_PROGRESS before implementation;
  verified production before creating the one learner task; then DONE/READY.
- Changed files: `app/config/settings.py`, `app/config/test_settings.py`,
  `.env.example`, `.env.production.example`, `README.md`, `docs/TICKETS.md`,
  this log, `learning/tasks/TSK-004/TASK.md` and empty `workspace/.gitkeep`.
- Decisions: use the standard-library process environment, no dotenv package
  or implicit file loading. Require a stable externally supplied key in every
  mode. Default to production with DEBUG false; development conveniences
  require explicit mode selection. Reject malformed modes/boolean values and
  production DEBUG true. Require explicit non-wildcard production hosts.
  SQLite remains a development-only bootstrap. Map PostgreSQL connection
  fields now without installing a driver, connecting or implementing TSK-006.
  No generated key fallback, credentials, real `.env` or deployment added.
- Consulted official Django 5.2 deployment checklist and database settings,
  Twelve-Factor configuration, Python 3.14 `os.environ` and unittest docs via
  the web tool. Links in README/task point to the verified official pages.

Acceptance and requirement evidence:

| Criterion / requirement | Observed evidence | Result |
| --- | --- | --- |
| Read key, database connection, debug and allowed hosts from environment | 13 automated tests verify environment key mapping, PostgreSQL name/user/password/host/port mapping, default and custom ports, SQLite development default/override, boolean parsing and host list parsing. Django HttpRequest accepts the configured host and rejects an untrusted host. | PASS |
| Missing production secrets fail clearly | Tests cover missing, empty and whitespace-only required fields, including key/password, and assert errors name variables without echoing either synthetic secret. Separate real `manage.py check` subprocesses exit 1 with `ImproperlyConfigured` for missing DJANGO_SECRET_KEY and missing DB_PASSWORD. | PASS |
| DEBUG disabled in production configuration | Both explicit and omitted production mode reject debug true. Omitted debug loads as False. Production example explicitly sets false. Typoed modes/boolean values fail rather than enabling development. | PASS |
| Safe sample variables, placeholders only | Reviewed both templates and parsed their assignments: key/password empty in both, production name/user are `replace_me`, domains end in reserved `.example.com`. Development contains only local hosts, SQLite selector and blank connection values. | PASS |
| No production secrets in repository | Changed settings read secrets externally; examples have no secret values; test values are explicitly synthetic. `git ls-files -- .env .env.production` returns nothing; example files are trackable. Reviewed changed source/docs and new templates/tests; no real credential supplied or copied. | PASS within the changed-file review scope |

Actual checks and environment:

All shell commands were invoked from
`/Users/tategraham/workspace/tate/taskforge-starter` on macOS/zsh unless noted.
Used the existing `.venv` with Python 3.14.7 and Django 5.2.19; no install,
service access, real secrets or production database. Configuration tests clear
ambient environment variables per load and use synthetic inputs only.

- `.venv/bin/python -m unittest discover -s app/config -p 'test_*.py' -v`:
  first run had 12 passing tests and one host-test error because Django's
  default settings were not initialized by the standalone runner. An initial
  harness repair exposed unittest discovery inspecting an unconfigured lazy
  settings import. Moved the import into class setup and initialize defaults
  only when unconfigured. Final run: exit 0, 13 tests passed. These failures
  were test-harness failures; no acceptance claim was made from them.
- `.venv/bin/python /private/tmp/taskforge_tsk004_verify.py`: exit 0. This
  temporary verification script used `subprocess.run` with explicit environment
  dictionaries (no inherited credentials) and absolute venv Python. Child
  working directory was the repository's `app/`. Development inputs were
  `DJANGO_ENV=development`, a synthetic key, `DJANGO_DEBUG=true`, local
  allowed hosts, and `DB_NAME=:memory:`. It ran:

  ```text
  <root>/.venv/bin/python manage.py check
    exit 0: System check identified no issues (0 silenced).
  <root>/.venv/bin/python manage.py makemigrations --check --dry-run
    exit 0: No changes detected
  <root>/.venv/bin/python manage.py test -v 2
    exit 0: Found 13 tests; all passed; no system-check issues;
    skipped setup of unused database default.
  ```

  It then ran `manage.py check` with an empty environment: expected exit 1,
  ending with `ImproperlyConfigured: DJANGO_SECRET_KEY must be set and nonblank.`
  A second production-default subprocess supplied synthetic key, allowed host,
  DB name/user/host but omitted the password: expected exit 1 ending with
  `ImproperlyConfigured: DB_PASSWORD must be set and nonblank.` The script
  asserted the synthetic key was absent from stderr in both cases.
- The same verification script parsed both example files and asserted empty
  key/password fields and production placeholders. For each template,
  `git -c core.excludesFile=/dev/null check-ignore --no-index -q <path>`
  returned 1 (trackable). `git ls-files -- .env .env.production` returned no
  paths. These checks plus manual diff review support the sample/secret scope.
- `git diff --check`: exit 0, no whitespace errors. Reviewed
  `git diff -- app/config/settings.py README.md docs/TICKETS.md` and the new
  templates/test source against the ticket. README records setup/export,
  all variables/defaults, tests, and production limitations.

Limits: PostgreSQL mapping and failure handling are verified without a driver
or live DB; PostgreSQL checks/migrations/persistence remain TSK-006. No live
production deployment or `check --deploy` pass is claimed; HTTPS/proxy/cookie
hardening and deployment checks remain later tickets. No server route or
health endpoint was added. Verification was on macOS, not Linux. No blocker
or scope deviation remains; no commits, pushes, PRs or publication performed.

Learner handoff: exactly one new task at
[`learning/tasks/TSK-004/TASK.md`](../learning/tasks/TSK-004/TASK.md),
a separate offline seed-library configuration validator using Python's standard
library. The nine-section exercise has binary criteria, official references,
local synthetic inputs and validation/submission guidance. Its workspace
contains only empty `.gitkeep`, with no solution. Existing learner work was
preserved. Learner status READY; no learner completion or review claimed.

### 2026-11-10 — Final handoff checks

Ran `python3 - <<'PY' ... PY` from the repository root using pathlib, regex
and Git subprocess assertions. Exit 0, observed:

```text
PASS: only TSK-004 tracker row changed; DONE/READY; no active production ticket
PASS: one learner task, nine required sections, empty workspace, prior learner files unchanged
PASS: README/task local link targets exist
PASS: exactly nine intended changed/new files; requirements, agreements and other production files unchanged
```

Manually reviewed the single independent exercise against the learning contract;
no solution or future dependency was included. `git diff --check` exited 0.
`git status --short` showed only the nine intended changed/new files above.
TSK-004 is DONE, its learner task is READY, and no other ticket was started.
