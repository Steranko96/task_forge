# TaskForge — Engineering Backlog

> Roadmap version: 1.0 · Source: `PROJECT.md` · Status: planning only · Mode: GUIDED

## 1. Project overview

TaskForge is a full-stack, server-rendered, multi-user Django task application using PostgreSQL. Users log in through Django sessions and can create, list, edit, complete/uncomplete, and delete only their own tasks. The delivery stack is Django templates, Docker Compose, Gunicorn, Caddy HTTPS, GitHub Actions and a DigitalOcean Linux VPS. This roadmap preserves the eight delivery milestones in `PROJECT.md` and its **5-day / approximately 50-focused-hour** constraint.

**Scope decisions (proposed for this backlog; not additions to PROJECT.md):** Django built-in User, authentication views, forms and templates; one Task entity with a required owner; no registration requirement (two accounts can be provisioned by admin command), no REST API/SPA, no Celery/Redis, no Kubernetes, no third-party observability stack. Use Django TestCase; choose one small Python linter. Public HTTPS needs a domain and DNS access. Prefer Docker Compose for consistent development and production.

**Effort accounting:** Tickets use estimates of 30–60 minutes (focused implementation plus ticket-level verification). MUST-HAVE total **37h 30m**, leaving **12h 30m** within the 50-hour budget for debugging, infra provisioning, CI delays and learning. STRETCH: **4h 00m** extra, not included in the deadline. These are planning estimates, not guarantees. The word “weekend” is treated as the **5 focused days specified by PROJECT.md**, not a 2-day/16-hour sprint.

## 2. Milestones and estimated effort

| Milestone | Tickets | MUST-HAVE | STRETCH | Exit gate |
|---|---|---:|---:|---|
| Foundations | TSK-001–TSK-005 | 4h 00m | 0h 00m | Django runs locally; health route responds |
| Database | TSK-006–TSK-009 | 3h 30m | 0h 00m | Task persists in PostgreSQL; owner required |
| Authentication | TSK-010–TSK-014 | 4h 15m | 0h 00m | Login/logout, session and protected views tested |
| Application and user isolation | TSK-015–TSK-024 | 8h 45m | 0h 00m | CRUD works; cross-user requests denied |
| Testing and hardening | TSK-025–TSK-026 | 1h 45m | 0h 00m | Regression matrix and production settings checked |
| Containerisation | TSK-027–TSK-030 | 4h 00m | 0h 00m | Reproducible Compose stack persists data |
| Linux deployment and HTTPS | TSK-031–TSK-034 | 4h 00m | 0h 00m | HTTPS live site with verified user isolation |
| CI/CD and operations | TSK-035–TSK-042 | 7h 15m | 0h 00m | CI/CD, logs, monitoring and tested restore evidenced |
| Optional extensions | TSK-043–TSK-046 | 0h 00m | 4h 00m | Optional UX/operational enhancements |

**Total mandatory:** 37h 30m; **unallocated contingency:** 12h 30m; **stretch add-on:** 4h 00m.

## 3. Complete ordered engineering backlog

Every ticket is one primary learning task. Its acceptance criteria are binary checks; preserve evidence such as test output, screenshots or commands in commit/PR notes. Links target official product or standards documentation.

### Milestone: Foundations

#### TSK-001 — Record architecture and scope decisions
- **Priority:** MUST-HAVE · **Estimate:** 45 minutes · **Dependencies:** None
- **Objective:** Define the smallest production-capable TaskForge.
- **Learning objectives:** Request flow; scope trade-offs.
- **Functional and technical requirements:** Document Django server-rendered architecture, ownership model, PostgreSQL, and deployment boundary; defer registration, API, JS SPA and styling extras.
- **Acceptance criteria:** README describes components, request path, excluded features, and two-user verification plan.
- **Official documentation:** [Django overview](https://docs.djangoproject.com/en/5.2/intro/overview/); [Django security](https://docs.djangoproject.com/en/5.2/topics/security/).

#### TSK-002 — Initialize repository and ignore rules
- **Priority:** MUST-HAVE · **Estimate:** 30 minutes · **Dependencies:** TSK-001
- **Objective:** Establish version-controlled development.
- **Learning objectives:** Git hygiene; secret handling.
- **Functional and technical requirements:** Initialize Git/GitHub repository; ignore environment files, virtual environments and generated assets; document branches/commits.
- **Acceptance criteria:** Repository has initial commit; ignores local secrets; no credentials tracked.
- **Official documentation:** [Git book](https://git-scm.com/book/en/v2); [GitHub docs](https://docs.github.com/en).

#### TSK-003 — Establish Python and Django environment
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-002
- **Objective:** Make local application start repeatably.
- **Learning objectives:** Virtual environments; dependencies.
- **Functional and technical requirements:** Pin Python compatibility and direct dependencies; create Django project/app; record installation/run commands.
- **Acceptance criteria:** Clean checkout can install dependencies and start Django development server.
- **Official documentation:** [Python venv](https://docs.python.org/3/library/venv.html); [Django overview](https://docs.djangoproject.com/en/5.2/intro/overview/).

#### TSK-004 — Configure environment-dependent settings
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-003
- **Objective:** Separate settings from secrets.
- **Learning objectives:** Twelve-factor configuration; fail-safe defaults.
- **Functional and technical requirements:** Read secret key, DB connection, debug mode and allowed hosts from environment; supply safe example variables; no production secrets in repository.
- **Acceptance criteria:** Missing production secrets fail clearly; DEBUG is disabled in production configuration; sample contains placeholders only.
- **Official documentation:** [Django deployment checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/); [Twelve-Factor config](https://12factor.net/config).

#### TSK-005 — Implement health endpoint and smoke check
- **Priority:** MUST-HAVE · **Estimate:** 45 minutes · **Dependencies:** TSK-003
- **Objective:** Prove routing works and expose liveness.
- **Learning objectives:** HTTP status; routing; tests.
- **Functional and technical requirements:** Add lightweight route that reports application liveness without secrets; add basic Django test.
- **Acceptance criteria:** Health route returns HTTP 200 when running; test passes; no credentials exposed.
- **Official documentation:** [Django URL dispatcher](https://docs.djangoproject.com/en/5.2/topics/http/urls/); [Django testing](https://docs.djangoproject.com/en/5.2/topics/testing/overview/).

### Milestone: Database

#### TSK-006 — Connect PostgreSQL in development
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-004
- **Objective:** Replace temporary storage with PostgreSQL.
- **Learning objectives:** DB connections; persistence.
- **Functional and technical requirements:** Use environment-configured PostgreSQL; document initial DB setup; verify connection without hard-coded passwords.
- **Acceptance criteria:** Django checks and migrations run against PostgreSQL; restart preserves data.
- **Official documentation:** [Django databases](https://docs.djangoproject.com/en/5.2/ref/databases/); [PostgreSQL docs](https://www.postgresql.org/docs/current/).

#### TSK-007 — Design Task schema and ownership
- **Priority:** MUST-HAVE · **Estimate:** 45 minutes · **Dependencies:** TSK-006
- **Objective:** Specify minimal Task data and relation.
- **Learning objectives:** Keys; constraints; data modelling.
- **Functional and technical requirements:** Choose task title, optional description, completion status, timestamps as appropriate, and required user foreign key; record deletion behaviour.
- **Acceptance criteria:** Task model spec includes non-null owner and field/validation choices; one owner can own many tasks.
- **Official documentation:** [Django models](https://docs.djangoproject.com/en/5.2/topics/db/models/).

#### TSK-008 — Create and verify Task migrations
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-007
- **Objective:** Persist task records through ORM.
- **Learning objectives:** Migrations; ORM; integrity.
- **Functional and technical requirements:** Implement model, generate and apply versioned migrations; validate required fields and relation.
- **Acceptance criteria:** Migration applies to fresh DB; ORM creates and retrieves task; owner is required.
- **Official documentation:** [Django migrations](https://docs.djangoproject.com/en/5.2/topics/migrations/); [Django models](https://docs.djangoproject.com/en/5.2/topics/db/models/).

#### TSK-009 — Add model and persistence tests
- **Priority:** MUST-HAVE · **Estimate:** 45 minutes · **Dependencies:** TSK-008
- **Objective:** Catch schema/persistence regressions.
- **Learning objectives:** Test isolation; DB fixtures.
- **Functional and technical requirements:** Test Task defaults, required ownership and persisted fields in Django TestCase.
- **Acceptance criteria:** Tests pass against configured test PostgreSQL DB; invalid ownerless task is rejected by DB or explicit validation.
- **Official documentation:** [Django testing](https://docs.djangoproject.com/en/5.2/topics/testing/overview/); [Django models](https://docs.djangoproject.com/en/5.2/topics/db/models/).

### Milestone: Authentication

#### TSK-010 — Configure two demo users securely
- **Priority:** MUST-HAVE · **Estimate:** 45 minutes · **Dependencies:** TSK-008
- **Objective:** Enable multi-user acceptance tests without registration.
- **Learning objectives:** Password hashing; user fixtures.
- **Functional and technical requirements:** Use Django user model and account creation procedure; provision two non-identical test accounts without hardcoded production passwords.
- **Acceptance criteria:** Two users exist for testing; credentials not committed; passwords hashed by Django.
- **Official documentation:** [Django auth](https://docs.djangoproject.com/en/5.2/topics/auth/default/); [Django management commands](https://docs.djangoproject.com/en/5.2/ref/django-admin/).

#### TSK-011 — Implement session login
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-010
- **Objective:** Let users authenticate through Django.
- **Learning objectives:** Sessions; authentication forms.
- **Functional and technical requirements:** Use Django built-in login view/form, GET page and POST credentials; handle invalid login with non-revealing errors.
- **Acceptance criteria:** Valid login establishes session and redirect; invalid credentials do not authenticate; browser receives session cookie.
- **Official documentation:** [Django auth](https://docs.djangoproject.com/en/5.2/topics/auth/default/); [Django forms](https://docs.djangoproject.com/en/5.2/topics/forms/).

#### TSK-012 — Implement logout safely
- **Priority:** MUST-HAVE · **Estimate:** 45 minutes · **Dependencies:** TSK-011
- **Objective:** End authenticated sessions.
- **Learning objectives:** POST semantics; CSRF.
- **Functional and technical requirements:** Use Django logout mechanism and non-GET action; render logout control in authenticated UI.
- **Acceptance criteria:** Authenticated POST logs user out; subsequent protected request redirects; GET does not mutate session.
- **Official documentation:** [Django auth](https://docs.djangoproject.com/en/5.2/topics/auth/default/); [Django CSRF protection](https://docs.djangoproject.com/en/5.2/howto/csrf/).

#### TSK-013 — Protect authenticated application routes
- **Priority:** MUST-HAVE · **Estimate:** 45 minutes · **Dependencies:** TSK-011
- **Objective:** Reject anonymous task access.
- **Learning objectives:** Authentication vs authorisation.
- **Functional and technical requirements:** Require login on task screens; implement safe return URL behaviour.
- **Acceptance criteria:** Anonymous request to each task screen redirects to login; logged-in request proceeds; unsafe redirects rejected.
- **Official documentation:** [Django auth](https://docs.djangoproject.com/en/5.2/topics/auth/default/); [Django web security](https://docs.djangoproject.com/en/5.2/topics/security/).

#### TSK-014 — Test login, logout and route protection
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-012, TSK-013
- **Objective:** Prove core access transitions.
- **Learning objectives:** Client tests; HTTP redirects.
- **Functional and technical requirements:** Cover successful/failed login, session termination and anonymous protection.
- **Acceptance criteria:** Automated tests verify each stated case; no task data leaked to anonymous clients.
- **Official documentation:** [Django testing](https://docs.djangoproject.com/en/5.2/topics/testing/overview/); [Django auth](https://docs.djangoproject.com/en/5.2/topics/auth/default/).

### Milestone: Application and user isolation

#### TSK-015 — Build shared layout and navigation
- **Priority:** MUST-HAVE · **Estimate:** 45 minutes · **Dependencies:** TSK-013
- **Objective:** Create usable template foundations.
- **Learning objectives:** Templates; accessible HTML.
- **Functional and technical requirements:** Create base layout, messages, login/logout navigation, semantic headings; minimal CSS only.
- **Acceptance criteria:** Templates render without errors; navigation matches auth state; form labels and headings present.
- **Official documentation:** [Django templates](https://docs.djangoproject.com/en/5.2/topics/templates/); [MDN HTML](https://developer.mozilla.org/en-US/docs/Web/HTML).

#### TSK-016 — List only current user's tasks
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-008, TSK-013, TSK-015
- **Objective:** Display scoped task list.
- **Learning objectives:** ORM filtering; IDOR threat.
- **Functional and technical requirements:** Query by authenticated owner; show empty state and completion state.
- **Acceptance criteria:** User A sees only A's tasks and not B's; anonymous requests blocked; list supports empty result.
- **Official documentation:** [Django queries](https://docs.djangoproject.com/en/5.2/topics/db/queries/); [Django web security](https://docs.djangoproject.com/en/5.2/topics/security/).

#### TSK-017 — Create tasks with validated form
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-016
- **Objective:** Create owned tasks securely.
- **Learning objectives:** ModelForm; validation; CSRF.
- **Functional and technical requirements:** Implement GET form/POST submit; set owner from request.user, never client input; validate title.
- **Acceptance criteria:** Valid submission creates exactly one owned task; empty title rejected; CSRF protected; owner field not editable.
- **Official documentation:** [Django forms](https://docs.djangoproject.com/en/5.2/topics/forms/); [Django CSRF protection](https://docs.djangoproject.com/en/5.2/howto/csrf/).

#### TSK-018 — Edit tasks with ownership checks
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-017
- **Objective:** Update tasks without crossing user boundaries.
- **Learning objectives:** Object-level access control.
- **Functional and technical requirements:** Resolve task by owner and identifier; validate form; preserve owner.
- **Acceptance criteria:** Owner edits title/description; nonowner direct URL returns 404 or 403 and leaves record unchanged.
- **Official documentation:** [Django queries](https://docs.djangoproject.com/en/5.2/topics/db/queries/); [Django forms](https://docs.djangoproject.com/en/5.2/topics/forms/).

#### TSK-019 — Toggle task completion
- **Priority:** MUST-HAVE · **Estimate:** 45 minutes · **Dependencies:** TSK-018
- **Objective:** Mark and unmark a task.
- **Learning objectives:** HTTP methods; state transitions.
- **Functional and technical requirements:** Use POST-only mutation, CSRF and owner-filtered task lookup.
- **Acceptance criteria:** Owner can complete and uncomplete; GET causes no change; nonowner cannot toggle.
- **Official documentation:** [Django CSRF protection](https://docs.djangoproject.com/en/5.2/howto/csrf/); [Django views](https://docs.djangoproject.com/en/5.2/topics/http/views/).

#### TSK-020 — Delete task with confirmation
- **Priority:** MUST-HAVE · **Estimate:** 45 minutes · **Dependencies:** TSK-018
- **Objective:** Remove only user-owned tasks.
- **Learning objectives:** Destructive actions; confirmation.
- **Functional and technical requirements:** Provide confirmation page; POST-only deletion; owner scoped lookup.
- **Acceptance criteria:** Owner can confirm deletion; GET does not delete; other user cannot delete.
- **Official documentation:** [Django views](https://docs.djangoproject.com/en/5.2/topics/http/views/); [Django CSRF protection](https://docs.djangoproject.com/en/5.2/howto/csrf/).

#### TSK-021 — Test task CRUD behaviours
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-017, TSK-018, TSK-019, TSK-020
- **Objective:** Prove normal workflows and invalid input.
- **Learning objectives:** Integration tests; form assertions.
- **Functional and technical requirements:** Test list, create, edit, toggle, delete, title validation, and persistence.
- **Acceptance criteria:** Tests cover success, errors, and POST/GET semantics; test suite green.
- **Official documentation:** [Django testing](https://docs.djangoproject.com/en/5.2/topics/testing/overview/); [Django forms](https://docs.djangoproject.com/en/5.2/topics/forms/).

#### TSK-022 — Test cross-user isolation comprehensively
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-016, TSK-018, TSK-019, TSK-020
- **Objective:** Block insecure direct object references.
- **Learning objectives:** Authorization matrices; negative testing.
- **Functional and technical requirements:** Exercise A/B users against list/detail (if used), edit, toggle, delete, and crafted owner field submissions.
- **Acceptance criteria:** For every entry point, B cannot read/change/delete A's tasks; forbidden operations leave DB unchanged.
- **Official documentation:** [Django testing](https://docs.djangoproject.com/en/5.2/topics/testing/overview/); [Django web security](https://docs.djangoproject.com/en/5.2/topics/security/).

#### TSK-023 — Review forms, templates and session security
- **Priority:** MUST-HAVE · **Estimate:** 45 minutes · **Dependencies:** TSK-021, TSK-022
- **Objective:** Eliminate obvious app-layer vulnerabilities.
- **Learning objectives:** CSRF; escaping; sessions.
- **Functional and technical requirements:** Check CSRF on mutating forms, default template autoescaping, safe redirects, owner filtering and method constraints.
- **Acceptance criteria:** Security checklist recorded; missing CSRF rejected; user-entered HTML renders as text; no task owner impersonation.
- **Official documentation:** [Django CSRF protection](https://docs.djangoproject.com/en/5.2/howto/csrf/); [Django web security](https://docs.djangoproject.com/en/5.2/topics/security/).

#### TSK-024 — Improve usability and error handling
- **Priority:** MUST-HAVE · **Estimate:** 45 minutes · **Dependencies:** TSK-021
- **Objective:** Make core features usable without polish work.
- **Learning objectives:** Feedback; validation UX.
- **Functional and technical requirements:** Add clear field errors, success messages, missing-task handling, and basic mobile-readable layout.
- **Acceptance criteria:** User can finish entire workflow without raw tracebacks; validation errors visible; 404 for missing task.
- **Official documentation:** [Django forms](https://docs.djangoproject.com/en/5.2/topics/forms/); [Django templates](https://docs.djangoproject.com/en/5.2/topics/templates/).

### Milestone: Testing and hardening

#### TSK-025 — Create test matrix and regression instructions
- **Priority:** MUST-HAVE · **Estimate:** 45 minutes · **Dependencies:** TSK-014, TSK-021, TSK-022
- **Objective:** Make system behaviour independently verifiable.
- **Learning objectives:** Test strategy; reproducibility.
- **Functional and technical requirements:** Document cases for authentication, user isolation, database, HTTP mutations, and smoke tests.
- **Acceptance criteria:** README lists commands and cases mapped to requirements; tests runnable locally.
- **Official documentation:** [Django testing](https://docs.djangoproject.com/en/5.2/topics/testing/overview/).

#### TSK-026 — Test production-like settings and failure modes
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-023, TSK-025
- **Objective:** Catch configuration risks before deployment.
- **Learning objectives:** Deployment checks; debugging.
- **Functional and technical requirements:** Exercise DEBUG off, required secrets, static files and allowed hosts; run Django deployment checks.
- **Acceptance criteria:** Checks report no unaddressed critical issues; known production variables documented.
- **Official documentation:** [Django deployment checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/); [Django static files](https://docs.djangoproject.com/en/5.2/howto/static-files/deployment/).

### Milestone: Containerisation

#### TSK-027 — Package Django with Docker
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-026
- **Objective:** Build reproducible runtime image.
- **Learning objectives:** Images; processes; build contexts.
- **Functional and technical requirements:** Create lean Dockerfile with pinned deps, non-root app execution where practical, .dockerignore and Gunicorn startup.
- **Acceptance criteria:** Image builds cleanly; starts under Gunicorn; secrets absent from image; health responds.
- **Official documentation:** [Docker Dockerfile](https://docs.docker.com/build/concepts/dockerfile/); [Django deployment checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/); [Gunicorn deployment](https://docs.gunicorn.org/en/stable/deploy.html).

#### TSK-028 — Run application and PostgreSQL with Compose
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-027, TSK-006
- **Objective:** Run services together locally.
- **Learning objectives:** Networks; service dependencies; volumes.
- **Functional and technical requirements:** Compose app and PostgreSQL; persist DB in named volume; inject variables without committing secrets.
- **Acceptance criteria:** One documented command starts stack; browser can log in; container recreation retains DB data.
- **Official documentation:** [Docker Compose](https://docs.docker.com/compose/); [Docker volumes](https://docs.docker.com/engine/storage/volumes/).

#### TSK-029 — Handle migrations and static assets in containers
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-028
- **Objective:** Make container startup/deploy predictable.
- **Learning objectives:** One-off jobs; static serving.
- **Functional and technical requirements:** Document deliberate migration execution; collect static assets for Caddy or appropriate serving configuration; avoid concurrent migration race.
- **Acceptance criteria:** Fresh stack migrates successfully; login CSS and assets load; migrations are explicit and repeatable.
- **Official documentation:** [Django migrations](https://docs.djangoproject.com/en/5.2/topics/migrations/); [Django static files](https://docs.djangoproject.com/en/5.2/howto/static-files/deployment/); [Docker Compose](https://docs.docker.com/compose/).

#### TSK-030 — Test container startup and persistence
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-029
- **Objective:** Prove reproduction rather than trusting build success.
- **Learning objectives:** Smoke tests; volume durability.
- **Functional and technical requirements:** Run documented clean-start sequence; create task; restart/recreate app and DB containers without deleting volume.
- **Acceptance criteria:** Health OK; task remains after normal recreation; test commands run against Compose services.
- **Official documentation:** [Docker Compose](https://docs.docker.com/compose/); [Django testing](https://docs.djangoproject.com/en/5.2/topics/testing/overview/).

### Milestone: Linux deployment and HTTPS

#### TSK-031 — Provision and harden Linux VPS
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-030
- **Objective:** Prepare minimal public host.
- **Learning objectives:** SSH keys; firewall; OS patches.
- **Functional and technical requirements:** Provision DigitalOcean VPS; non-root sudo account, SSH key auth, essential updates, inbound SSH/HTTP/HTTPS only; note access recovery.
- **Acceptance criteria:** SSH works as non-root; password SSH disabled after verifying key login; unnecessary ports blocked.
- **Official documentation:** [DigitalOcean documentation](https://docs.digitalocean.com/products/droplets/); [Ubuntu server guide](https://documentation.ubuntu.com/server/); [OpenSSH documentation](https://www.openssh.com/manual.html).

#### TSK-032 — Configure domain/DNS and Caddy HTTPS
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-031
- **Objective:** Provide reverse proxy and valid TLS.
- **Learning objectives:** DNS; HTTPS termination; proxies.
- **Functional and technical requirements:** Point domain to VPS, configure Caddy to proxy Gunicorn, expose only proxy publicly.
- **Acceptance criteria:** Public domain resolves; HTTPS certificate valid; HTTP redirects to HTTPS; Gunicorn not exposed publicly.
- **Official documentation:** [Caddy reverse proxy](https://caddyserver.com/docs/caddyfile/directives/reverse_proxy); [Caddy automatic HTTPS](https://caddyserver.com/docs/automatic-https); [DigitalOcean documentation](https://docs.digitalocean.com/products/droplets/).

#### TSK-033 — Deploy production Compose stack
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-029, TSK-031, TSK-032
- **Objective:** Run TaskForge on real host.
- **Learning objectives:** Production env; volumes; releases.
- **Functional and technical requirements:** Install Docker/Compose; provision secret env outside Git; run app/Postgres behind Caddy with persistent DB storage and migrations.
- **Acceptance criteria:** Authenticated task CRUD works via HTTPS; DEBUG=false; app survives service restart.
- **Official documentation:** [Docker Dockerfile](https://docs.docker.com/build/concepts/dockerfile/); [Docker Compose](https://docs.docker.com/compose/); [Django deployment checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/).

#### TSK-034 — Verify production security configuration
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-033, TSK-023
- **Objective:** Validate internet-facing access controls.
- **Learning objectives:** Secure cookies; CSRF origins; host validation.
- **Functional and technical requirements:** Configure hosts, trusted origins, HTTPS proxy headers, secure session/CSRF cookies; recheck firewall and owner isolation.
- **Acceptance criteria:** Deployment checks pass or exceptions documented; cross-account attack denied on live site; browser uses HTTPS cookies.
- **Official documentation:** [Django deployment checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/); [Django CSRF protection](https://docs.djangoproject.com/en/5.2/howto/csrf/); [Django web security](https://docs.djangoproject.com/en/5.2/topics/security/).

### Milestone: CI/CD and operations

#### TSK-035 — Add CI for checks, lint and tests
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-025, TSK-028
- **Objective:** Prevent broken changes reaching deployment.
- **Learning objectives:** CI jobs; branch gates.
- **Functional and technical requirements:** GitHub Actions triggers on pushes/PRs; installs deps, uses PostgreSQL test service, runs selected linter and Django tests.
- **Acceptance criteria:** Deliberately failing test/lint yields red workflow; clean branch green; CI needs no production secrets.
- **Official documentation:** [GitHub Actions](https://docs.github.com/en/actions); [GitHub Actions PostgreSQL service](https://docs.github.com/en/actions/tutorials/use-containerized-services/create-postgresql-service-containers); [Django testing](https://docs.djangoproject.com/en/5.2/topics/testing/overview/).

#### TSK-036 — Create gated deployment workflow
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-033, TSK-035
- **Objective:** Make deployment repeatable and controlled.
- **Learning objectives:** CD credentials; least privilege.
- **Functional and technical requirements:** GitHub Actions deployment trigger from protected main or manual approval; securely connect to VPS, update release, run migrations and restart; document rollback.
- **Acceptance criteria:** Manual or protected trigger deploys known commit; secrets in GitHub Secrets; failed health check visible; rollback steps documented.
- **Official documentation:** [GitHub Actions](https://docs.github.com/en/actions); [GitHub Actions secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions); [Docker Compose](https://docs.docker.com/compose/).

#### TSK-037 — Configure structured-enough application logs
- **Priority:** MUST-HAVE · **Estimate:** 45 minutes · **Dependencies:** TSK-033
- **Objective:** Make failures diagnosable.
- **Learning objectives:** stdout/stderr; log severity.
- **Functional and technical requirements:** Send Django/Gunicorn operational errors to container logs with timestamps; avoid logging cookies, passwords or secret values.
- **Acceptance criteria:** Can identify request/server failure by time; logs survive via host/container logging policy; no secret data in sample.
- **Official documentation:** [Django logging](https://docs.djangoproject.com/en/5.2/topics/logging/); [Docker logs](https://docs.docker.com/reference/cli/docker/container/logs/).

#### TSK-038 — Add basic uptime and health monitoring
- **Priority:** MUST-HAVE · **Estimate:** 45 minutes · **Dependencies:** TSK-005, TSK-033
- **Objective:** Detect outage without full observability stack.
- **Learning objectives:** Liveness vs readiness; alerts.
- **Functional and technical requirements:** Use external HTTP(S) probe or host scheduler with notification; document health endpoint limits; set minimum alert path.
- **Acceptance criteria:** HTTPS health status checked regularly; demonstrated failure is visible; named response action documented.
- **Official documentation:** [DigitalOcean documentation](https://docs.digitalocean.com/products/droplets/); [GitHub docs](https://docs.github.com/en).

#### TSK-039 — Define database backup procedure
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-033
- **Objective:** Preserve task data off the running DB volume.
- **Learning objectives:** RPO; dump consistency; retention.
- **Functional and technical requirements:** Create documented PostgreSQL dump command/schedule, secure storage off VPS and retention policy; protect backup credentials.
- **Acceptance criteria:** Fresh backup produced, encrypted/restricted off-host, timestamped; schedule and ownership recorded.
- **Official documentation:** [pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html); [pg_restore](https://www.postgresql.org/docs/current/app-pgrestore.html).

#### TSK-040 — Prove database restoration
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-039
- **Objective:** Demonstrate disaster recovery.
- **Learning objectives:** RTO; data verification.
- **Functional and technical requirements:** Restore latest backup into isolated PostgreSQL database/container; verify known task and owner relation; document restart/recovery procedure.
- **Acceptance criteria:** Restore completes without overwriting live DB; known rows match; timestamp/duration/evidence recorded.
- **Official documentation:** [pg_restore](https://www.postgresql.org/docs/current/app-pgrestore.html); [Docker Compose](https://docs.docker.com/compose/).

#### TSK-041 — Perform end-to-end release acceptance
- **Priority:** MUST-HAVE · **Estimate:** 60 minutes · **Dependencies:** TSK-034, TSK-036, TSK-037, TSK-038, TSK-040
- **Objective:** Validate whole deployed system.
- **Learning objectives:** Release checks; evidence collection.
- **Functional and technical requirements:** Run two-user workflow, negative ownership checks, CI status, Docker restart, HTTPS, logs, monitoring, recovery evidence.
- **Acceptance criteria:** All PROJECT.md DoD items checked with dated evidence; outstanding failures tracked, not marked done.
- **Official documentation:** [Django testing](https://docs.djangoproject.com/en/5.2/topics/testing/overview/); [Django deployment checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/).

#### TSK-042 — Consolidate operations runbook and handoff
- **Priority:** MUST-HAVE · **Estimate:** 45 minutes · **Dependencies:** TSK-041
- **Objective:** Enable repeatable operation by future self.
- **Learning objectives:** Operational documentation.
- **Functional and technical requirements:** Record setup, env names, deployment/rollback, log inspection, uptime check, backup/restore, security updates and known limitations.
- **Acceptance criteria:** Another reader can locate commands, secrets locations (not secret values) and recovery instructions; README links runbook.
- **Official documentation:** [Docker logs](https://docs.docker.com/reference/cli/docker/container/logs/); [pg_restore](https://www.postgresql.org/docs/current/app-pgrestore.html).

### Milestone: Optional extensions

#### TSK-043 — Add self-service registration
- **Priority:** STRETCH · **Estimate:** 60 minutes · **Dependencies:** TSK-041
- **Objective:** Allow users to create accounts themselves.
- **Learning objectives:** User lifecycle; abuse protection.
- **Functional and technical requirements:** Add registration only after core release; keep server-side validation and password handling.
- **Acceptance criteria:** New user registers without staff assistance; duplicate/invalid inputs rejected; authenticated session works.
- **Official documentation:** [Django auth](https://docs.djangoproject.com/en/5.2/topics/auth/default/); [Django forms](https://docs.djangoproject.com/en/5.2/topics/forms/).

#### TSK-044 — Add task ordering and filters
- **Priority:** STRETCH · **Estimate:** 60 minutes · **Dependencies:** TSK-041
- **Objective:** Improve list navigation.
- **Learning objectives:** ORM ordering; query parameters.
- **Functional and technical requirements:** Add completion filter and deterministic ordering; preserve owner restriction.
- **Acceptance criteria:** Filters show only matching owned tasks; invalid filters safe; tests pass.
- **Official documentation:** [Django queries](https://docs.djangoproject.com/en/5.2/topics/db/queries/); [Django testing](https://docs.djangoproject.com/en/5.2/topics/testing/overview/).

#### TSK-045 — Automate backup scheduling and alerts
- **Priority:** STRETCH · **Estimate:** 60 minutes · **Dependencies:** TSK-040
- **Objective:** Reduce manual backup dependency.
- **Learning objectives:** Scheduling; failure alarms.
- **Functional and technical requirements:** Automate scheduled off-host dump and alert on failure; preserve tested manual restore.
- **Acceptance criteria:** Scheduled run creates restorable dump; simulated failure alerts; retention enforced.
- **Official documentation:** [pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html); [Ubuntu server guide](https://documentation.ubuntu.com/server/).

#### TSK-046 — Add lightweight error-rate visibility
- **Priority:** STRETCH · **Estimate:** 60 minutes · **Dependencies:** TSK-037, TSK-038
- **Objective:** Spot recurring server faults.
- **Learning objectives:** Metrics; thresholds.
- **Functional and technical requirements:** Add simple host-based log summary/alert without new monitoring platform.
- **Acceptance criteria:** Repeated 5xx errors become apparent from documented report or alert.
- **Official documentation:** [Django logging](https://docs.djangoproject.com/en/5.2/topics/logging/); [Docker logs](https://docs.docker.com/reference/cli/docker/container/logs/).

## 4. Ticket dependency map

**Ordering:** Ticket IDs are the recommended sequence; the dependency field above is authoritative. Tickets not connected by dependencies may be done in parallel or rearranged after the relevant prerequisite exists. Do not advance into a later phase while its exit gate is unmet.

**Main chains:**

- Repository → config → PostgreSQL → schema: **001 → 002 → 003 → 004 → 006 → 007 → 008**.
- Database → users → authentication → routes: **008 → 010 → 011 → 013 → 016** (logout and auth tests branch from 011).
- Task list → forms → edits → mutations → negative tests: **016 → 017 → 018 → 019/020 → 021/022 → 023**.
- Security/test review → Docker → Compose → VPS → live deployment: **023/026 → 027 → 028 → 029 → 030 → 031 → 033 → 034** (DNS/TLS 032 also precedes 033).
- CI and deployment automation: **025/028 → 035 → 036**, with **033** also preceding 036.
- Recovery: **033 → 039 → 040**; monitoring and logging: **033 → 037/038**.
- Final release gate: **034 + 036 + 037 + 038 + 040 → 041 → 042**.

## 5. Critical path and five-day plan

| Day | Focus | Key deliverable | Planned MUST-HAVE |
|---|---|---|---:|
| Day 1 | TSK-001–TSK-009 | Foundation, health and PostgreSQL model | 7h 30m |
| Day 2 | TSK-010–TSK-020 | Authentication and complete task workflow | 9h 30m |
| Day 3 | TSK-021–TSK-030 | Isolation tests, security review and Compose | 9h 15m |
| Day 4 | TSK-031–TSK-036 | VPS, HTTPS, CI and controlled deployment | 6h 00m |
| Day 5 | TSK-037–TSK-042 | Logging, health monitoring, verified restore, acceptance | 5h 15m |

**Schedule note:** The plan aims to finish MUST-HAVEs within 50 focused hours, retaining a contingency block for first-time VPS/DNS, TLS, container and restore troubleshooting. Use the contingency before any stretch ticket. If a two-day weekend is the actual time available, 50 focused hours is infeasible; split delivery across five days or renegotiate scope/deadline.

**Scope reduction ladder if time slips (requires explicit agreement because these affect PROJECT.md):** First drop all STRETCH items, decorative UI, optional fields and any nonessential refactor (no required feature lost). Next simplify monitoring to one scheduled HTTPS probe/alert, CI/CD to a manual approved deployment workflow, and documentation to one concise README/runbook—while retaining functional proof. Do **not** claim PROJECT.md complete if HTTPS, cross-user isolation, CI, backup **and verified restore** are missing. If overrun remains, extend the deadline rather than silently removing these acceptance requirements.

## 6. Overall definition of done

- [ ] Two separate users can log in and log out using session-based authentication; anonymous users cannot access task screens.
- [ ] Both users can independently list/create/edit/complete/uncomplete/delete their own tasks; server-side checks prevent reading or mutating another user’s tasks, including direct object URLs.
- [ ] Tasks have required user ownership and survive PostgreSQL and container restarts; migrations work from a clean database.
- [ ] Django automated authentication, CRUD, validation and authorisation tests pass locally and in GitHub Actions; lint is green.
- [ ] Docker image and Compose app/PostgreSQL stack build and start with documented environment variables and persistent storage.
- [ ] The production service runs on a Linux/DigitalOcean VPS with Gunicorn behind Caddy, HTTPS works, secure settings are checked, and deployment workflow can publish an identified commit.
- [ ] Health endpoint responds; logs can be inspected; a monitoring check/notification is configured and exercised.
- [ ] PostgreSQL backup is captured securely off host, and restoration into an isolated environment is **actually tested and evidenced**.
- [ ] README/runbook contains installation, tests, configuration variable names, deploying, rollback, logging, monitoring, backup, restore, and known limitations—without revealing secrets.
- [ ] End-to-end evidence is recorded in TSK-041; all MUST-HAVE tickets satisfy their own acceptance criteria.

## 7. Scope, risk and completeness review

**Coverage audit:** The tickets map the eight specification milestones to tangible exit gates. Authentication (010–014), full CRUD and isolation (016–023), PostgreSQL and migrations (006–009), testing (005, 009, 014, 021–026), environment/Git (002–004), Docker/Gunicorn/Compose (027–030), Linux/Caddy/HTTPS (031–034), CI/CD (035–036), and logging/health/monitoring/backup/restore (005, 037–040) are all MUST-HAVE.

**Primary risks:** First-time DNS/HTTPS setup or no domain access; VPS billing/access/SSH security; deployment secrets and CI permissions; test PostgreSQL/Compose differences; imperfect estimate accuracy for incident/debugging work; backup restoration taking longer than anticipated. Mitigate by securing accounts/domain/VPS access early, validating each milestone gate, and reserving contingency. Never commit secrets or put production credentials into CI logs.

**Estimate realism:** This is an ambitious five-day cap for a learner: infrastructure and debugging time can be very variable. All tickets are intentionally small, but an individual task can exceed its estimate. The plan is flexible: revise sequencing/estimates and log changes after a ticket while keeping mandatory requirements explicit. The learner owns all application implementation; this backlog does not start TSK-001 or provide implementation code.

## 8. Source and planning authority

- `PROJECT.md` (TaskForge specification, sections 1–9): functional, engineering, technology, time and completion criteria. This backlog **does not modify** the specification.
- Where the spec leaves choices open (registration, exact schema fields, linter, monitoring mechanism, domain), the simplest viable option is proposed—not represented as an original requirement.
