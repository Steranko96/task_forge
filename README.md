# TaskForge

TaskForge will be a multi-user task manager built with Python, Django,
server-rendered HTML/CSS and PostgreSQL. This README records the architecture
and scope decisions for TSK-001. TSK-003 provides a runnable local Django
bootstrap; task features, PostgreSQL and deployment are still pending.
See [ticket status](docs/TICKETS.md) and [verification evidence](docs/PROGRESS.md).

## Components and decisions

| Component | Responsibility and reason |
| --- | --- |
| Browser | Displays Django-rendered HTML and submits ordinary forms; no separate frontend application. |
| Django in `app/` | URL routing, views, forms, templates and business rules in one application, keeping the required workflow small. |
| Django authentication | Built-in User model and session-based login/logout; two accounts provisioned through a secure management procedure rather than public registration. |
| Task ownership | Each task has one required user owner; one user can own many tasks. Every task query and mutation is restricted to the authenticated owner on the server. |
| PostgreSQL | Durable application storage accessed through Django's ORM and versioned migrations. Schema details and validation choices belong to TSK-007. |
| Django TestCase | Disposable test databases for authentication, CRUD, validation and negative ownership tests. |
| Docker and Docker Compose | Package and run the app and PostgreSQL consistently, with persistent database storage. |
| Gunicorn and Caddy | Gunicorn serves Django behind Caddy; Caddy provides the public HTTPS entry point. |
| Git/GitHub and GitHub Actions | Version control, automated lint/tests and a gated deployment workflow. Repository setup and delivery configuration arrive in their own tickets. |

The user-facing scope is login/logout and creating, listing, editing,
completing/uncompleting and deleting personal tasks. Hiding controls in HTML
is insufficient: views must enforce ownership even for direct object requests.
New tasks receive the authenticated user as owner; client-supplied owner values
cannot select another account. Keep Django's password handling, CSRF protection,
form validation and template escaping. State changes use POST; GET only reads.

## Request path

The intended production request/response path is:

```text
Browser --HTTPS--> Caddy --private HTTP--> Gunicorn --> Django
                                                       |
                                  middleware/session authentication
                                                       |
                                         URL route --> view/form
                                                       |
                                      owner-scoped ORM query
                                                       |
                                                   PostgreSQL
                                                       |
                               template/redirect --> HTTP response
Browser <--HTTPS-- Caddy <------------ Gunicorn <-------+
```

For a task list GET, Django identifies the session user, redirects an anonymous
visitor to login, and retrieves only that user's tasks before rendering HTML.
For a create/edit POST, Django checks CSRF, authentication, ownership where an
existing task is addressed, and form validity before saving through the ORM.
Invalid input returns form errors without saving; success redirects to a GET
so refreshing does not repeat the write. A request for another user's task
must disclose no task data and must leave stored data unchanged. The exact
denial response will be established and tested in the relevant route tickets.

## Deployment boundary

The intended host is one DigitalOcean Linux VPS running the Compose app and
PostgreSQL behind Caddy. Public application traffic enters through Caddy on
HTTP/HTTPS, with HTTP redirected to HTTPS. Gunicorn and PostgreSQL are private;
SSH is restricted to key-based administration. Django's development server is
for local work only. Production uses environment-provided secrets, DEBUG off,
validated hosts/origins and secure cookies; credentials stay outside Git.
A domain, DNS control and VPS access are external deployment prerequisites.
Nothing in this ticket provisions or purchases those resources.

Persistent database storage, migrations, static asset delivery, health checks,
logs, uptime notification, controlled deployment/rollback, off-host backups and
an actually verified isolated restore remain required delivery work. They are
implemented and evidenced by later tickets, not implied by this design.

## Excluded and deferred features

- Self-service registration is deferred to optional TSK-043 after core release;
  the required two-user workflow uses securely provisioned accounts.
- A REST API and JavaScript SPA are outside the core scope; Django templates
  and forms provide the required browser workflow.
- Decorative styling extras are deferred; readable HTML/CSS, usable forms,
  navigation and errors remain required.
- Celery/Redis, Kubernetes and a third-party observability platform are outside
  the core scope. Basic logging, health monitoring and recovery remain required.
- Optional ordering/filters, backup automation and error-rate extensions remain
  TSK-044–TSK-046, requested separately after their prerequisites.

These choices keep the mandatory work within the planned five focused days /
approximately 50 production hours without dropping security or operations.
Learner practice and tutoring take additional time.

## Two-user verification plan

This is a future acceptance plan, not evidence of a working application.
Use two distinct non-staff accounts A and B, separate browser sessions and
synthetic tasks in a local/disposable environment. Never commit credentials
or use production data for automated tests.

| Check | Procedure | Required outcome |
| --- | --- | --- |
| Authentication | Try invalid credentials, then log in as A and B in separate sessions. | Invalid credentials establish no session; each valid login authenticates the correct account. |
| Protected routes | Request task pages and submit task actions while logged out. | Authentication is required; no task data is exposed or changed. |
| Owner workflow | Each user creates, lists, edits, completes, uncompletes and deletes their own synthetic tasks. | Each action works for its owner; list contents and persisted changes are correct. |
| List isolation | Create distinct A and B tasks and inspect each list. | Each account sees only its own records. |
| Direct-object isolation | As B, use A's task identifier in read/edit GETs and valid-CSRF edit, completion and delete POSTs; repeat with roles reversed. | All foreign access is denied, no task data is disclosed, and the owner's record remains unchanged. |
| Forged ownership | Submit another user's owner value while creating/editing a task. | The submitted value cannot grant or transfer ownership. |
| Input and CSRF | Submit invalid forms and mutations without a valid CSRF token; try mutation URLs with GET. | Invalid forms do not save; CSRF failures and GET requests do not mutate data. |
| Logout | Log out and retry protected requests with the former session. | The old authenticated session no longer grants task access. |
| Persistence | Create an owned task, restart the app/database normally without deleting storage, then log back in. | The task and its ownership remain intact. |

Automate authentication, CRUD and negative ownership cases with Django
TestCase as their tickets arrive; explicitly enforce CSRF checks in tests
covering CSRF. Later container and deployed HTTPS checks must also record
observed results. The full release must still satisfy [PROJECT.md](PROJECT.md),
including CI, HTTPS, logs, monitoring, backup and demonstrated restoration.

## Official references

The runtime uses Django 5.2.19 and Python 3.14.x. The backlog’s Django 5.2
documentation matches this implementation.

- [Django overview: models, routing, views and templates](https://docs.djangoproject.com/en/5.2/intro/overview/)
- [Django security: escaping, CSRF and deployment protections](https://docs.djangoproject.com/en/5.2/topics/security/)

## Working in this repository

Read [PROJECT.md](PROJECT.md), [BACKLOG.md](BACKLOG.md) and
[AGENTS.md](AGENTS.md) for scope, ticket requirements and execution rules.
Codex implements exactly one explicitly requested production ticket, verifies
it, creates one independent learner exercise and stops. Practice follows
[learning/README.md](learning/README.md); learner completion does not gate a
new explicit production request. Local bootstrap commands are below.

| Path | Purpose |
| --- | --- |
| `app/` | Django project (`config`) and registered task app skeleton (`tasks`) |
| `docs/TICKETS.md` | Separate production and learner status |
| `docs/PROGRESS.md` | Observed verification evidence |
| `docs/architecture/` | Space for future detailed decisions; current architecture is above |
| `docs/operations/` | Future operations runbook |
| `docs/reference/` | Read-only historical sources |
| `learning/tasks/` | One independent task per verified production ticket |

## Local Python and Django setup

Supported bootstrap environment: **Python 3.14.x on macOS/Linux**, with `venv`
and pip available. `.python-version` selects the 3.14 series for compatible
version managers; it does not install Python. Use a maintained patch release
in that series. Django 5.2 supports Python 3.14 from 5.2.8 onward; this project
pins Django 5.2.19 and its current runtime dependencies in `requirements.txt`.
No PostgreSQL driver or deployment packages are installed yet (TSK-006 and later).

From a clean checkout, run these commands at the repository root:

```sh
python3.14 --version
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip check
python -m django --version
cp .env.example .env
# Generate a private local key and write it into the blank DJANGO_SECRET_KEY in .env:
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
# Quote the key with single quotes in .env, then export the file:
set -a
source .env
set +a
python app/manage.py check
python app/manage.py migrate
python app/manage.py runserver 127.0.0.1:8000
```

The Django version should be `5.2.19`, pip should report no broken requirements,
and Django's system check should report no issues. Open
[the local server](http://127.0.0.1:8000/) to see Django's default installation
success page (HTTP 200). Stop it with Ctrl-C; use `deactivate` to leave the
virtual environment. Activation is optional if you invoke `.venv/bin/python`
explicitly. Recreate the environment and reinstall from the requirements file
on each new checkout; never copy or commit a virtual environment.

`app/manage.py` is the command entry point; `app/config/` holds project settings,
URLs and WSGI/ASGI entry points. `app/tasks/` is registered but has no task
models or views yet. The generated admin route remains; no accounts are
provisioned. The root page is Django's built-in debug welcome screen, not a
health endpoint. Settings regression tests are available below; routing tests
arrive with TSK-005.

This bootstrap is **local development only**. SQLite at `app/db.sqlite3` is
still temporary disposable storage; PostgreSQL connection verification arrives
in TSK-006. `.venv/`, `.env`, caches and SQLite files are ignored. Run migrations
before startup. Do not expose the development server publicly.

## Environment configuration

Settings read the process environment using Python's standard library; no new
dependency or automatic `.env` loader is used. The shell commands above export
your private `.env` for the current terminal. Source only a local file you trust:
`source` executes shell code. Keep secret values quoted, never paste them into
tracked files or validation evidence, and reuse your local key across restarts.
The committed example files contain empty secrets and illustrative values only;
they intentionally cannot start Django until populated. Existing exported values
persist in a terminal: open a fresh shell when switching configurations.

| Variable | Behavior |
| --- | --- |
| `DJANGO_ENV` | `production` by default; only `development` or `production` accepted. Development must be explicit. |
| `DJANGO_SECRET_KEY` | Required and nonblank in every mode; no stored or randomly generated fallback. Supply a private, large random value. |
| `DJANGO_DEBUG` | Defaults to `false`; accepts only `true`/`false`, ignoring case and surrounding whitespace. `true` is rejected in production. |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated hostnames/IPs, trimmed with empty entries removed. Production requires a nonempty list without `*`. Use hosts without scheme or port; Django enforces host matching on requests. |
| `DB_ENGINE` | `postgresql` by default in production, `sqlite3` in development. SQLite is rejected in production. |
| `DB_NAME` | Required for PostgreSQL; SQLite defaults to `app/db.sqlite3` when omitted/blank. A relative SQLite path is relative to the process working directory. |
| `DB_USER`, `DB_PASSWORD`, `DB_HOST` | Required and nonblank for PostgreSQL in either mode; ignored for SQLite. |
| `DB_PORT` | PostgreSQL port; defaults to `5432`, must be an integer from 1 to 65535. Ignored for SQLite. |

Use [.env.example](.env.example) for local setup and
[.env.production.example](.env.production.example) as a production variable
inventory. Supply actual production values privately via the deployment
environment. An unset/blank secret raises `ImproperlyConfigured` naming the
variable without printing its value. Typoed modes/debug values fail instead of
silently weakening settings. Django's built-in CSRF/authentication middleware
and template escaping remain enabled.

TSK-004 prepares the PostgreSQL settings dictionary only. The driver, database
service, migrations against PostgreSQL and persistence verification belong to
TSK-006. These templates do not constitute a deployable production service;
HTTPS, cookies, proxy configuration and deployment checks remain later tickets.

Run configuration tests from the repository root without loading your `.env`:

```sh
.venv/bin/python -m unittest discover -s app/config -p 'test_*.py' -v
```

Tests isolate environment values and use synthetic credentials, never a database
connection. With your local development environment exported, also run
`python app/manage.py check` and `(cd app && python manage.py test)`
(the app directory is the test discovery root).

Configuration references: [Django 5.2 deployment checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/),
[Django 5.2 database settings](https://docs.djangoproject.com/en/5.2/ref/settings/#databases),
and [Twelve-Factor configuration](https://12factor.net/config).

References: [Python 3.14 virtual environments](https://docs.python.org/3.14/library/venv.html),
[Django 5.2 Python compatibility](https://docs.djangoproject.com/en/5.2/faq/install/),
and [Django project/app setup and development server](https://docs.djangoproject.com/en/5.2/intro/tutorial01/).

## Version control and local files

The existing Git repository uses `main` and the GitHub remote
[`Steranko96/task_forge`](https://github.com/Steranko96/task_forge).
Its initial commit is `ba8fd3a` (`first commit`). Reuse this repository and
history; a fresh checkout should be cloned rather than initialized again.

For an explicitly requested ticket, use a focused branch such as
`codex/tsk-002-repository-hygiene`. Before editing, inspect `git status --short`
and preserve unrelated changes. Keep each commit limited to the requested
ticket and describe the result, for example
`TSK-002: document repository hygiene`. Before an authorized commit:

1. Run the ticket's relevant checks and `git diff --check`.
2. Inspect `git diff` and `git status --short`, including untracked files.
3. Stage intended paths explicitly with `git add <path> ...`.
4. Review `git diff --cached --stat` and `git diff --cached` for scope and secrets.
5. Commit only after that review. Push or open a PR only when requested.

These are workflow instructions, not a record that those actions occurred.
Codex creates commits, pushes, PRs or publishes only with authorization for
the current ticket. Verification and learner handoff do not require committing
the pending changes.

`.gitignore` excludes local `.env` variants, private key files (`*.pem`,
`*.key`), `secrets/`, virtual environments (`.venv/`, `venv/`, `env/`), Python
caches/build output, collected static files (`staticfiles/`), uploaded media,
local databases and their journals, logs and backups. Authored static source
and Django migrations belong in Git. `.env.example` and `.env.*.example`
remain trackable, but must contain placeholders only. See the environment
configuration section above for variable names and safe example templates.

Use `git check-ignore -v --no-index <path>` to identify a matching rule;
`git ls-files` shows what is already tracked. Ignore rules do not remove
previously tracked data and cannot recognize arbitrary credentials in source
files. Never put tokens in remote URLs or commit real credentials, sessions,
data or backups. If a real secret enters Git, stop sharing it, revoke/rotate
the credential, and coordinate any cleanup; adding an ignore rule alone
does not remove it from history.

References: [Git ignore rules](https://git-scm.com/docs/gitignore),
[reviewing and recording changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository),
and [GitHub sensitive-data response](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).
