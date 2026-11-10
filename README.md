# TaskForge

TaskForge will be a multi-user task manager built with Python, Django,
server-rendered HTML/CSS and PostgreSQL. This README records the architecture
and scope decisions for TSK-001. The repository is still a documentation and
folder skeleton: there is no runnable application, database or deployment yet.
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

The backlog's Django 5.2 documentation provides the design reference; runtime
compatibility and dependency pins will be established in TSK-003.

- [Django overview: models, routing, views and templates](https://docs.djangoproject.com/en/5.2/intro/overview/)
- [Django security: escaping, CSRF and deployment protections](https://docs.djangoproject.com/en/5.2/topics/security/)

## Working in this repository

Read [PROJECT.md](PROJECT.md), [BACKLOG.md](BACKLOG.md) and
[AGENTS.md](AGENTS.md) for scope, ticket requirements and execution rules.
Codex implements exactly one explicitly requested production ticket, verifies
it, creates one independent learner exercise and stops. Practice follows
[learning/README.md](learning/README.md); learner completion does not gate a
new explicit production request. Installation and runtime test commands will
be added when the corresponding tickets provide a runnable application.

| Path | Purpose |
| --- | --- |
| `app/` | Future production Django application; currently a placeholder |
| `docs/TICKETS.md` | Separate production and learner status |
| `docs/PROGRESS.md` | Observed verification evidence |
| `docs/architecture/` | Space for future detailed decisions; current architecture is above |
| `docs/operations/` | Future operations runbook |
| `docs/reference/` | Read-only historical sources |
| `learning/tasks/` | One independent task per verified production ticket |

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
remain trackable, but must contain placeholders only. Environment variable
names and sample settings will be defined in TSK-004.

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
