# Title and source ticket

Museum Cabinet bootstrap — independent practice for
[TSK-003](../../../BACKLOG.md#tsk-003--establish-python-and-django-environment).
Status: READY. Submit only in `learning/tasks/TSK-003/workspace/`.

## Objective

Create a repeatable local Django environment for a fictional museum catalogue.
Suggested timebox: 45–60 minutes. This is one bootstrap exercise; no catalogue
features, models, accounts or custom routes are required.

## Concepts

A virtual environment isolates installed packages from other projects.
A dependency pin makes an installation version explicit. Python compatibility
is a separate choice from the Django version. A Django project owns global
configuration; a registered app is a component within it. Setup notes let
another person reproduce the environment without copying generated files.

## Prerequisites and setup

Use a working Python 3.14.x installation on macOS/Linux with `venv` and pip,
a terminal, an editor, and internet access to PyPI. Use Django 5.2.19.
All work is local and free. Begin in this task's empty `workspace/`, using a
separate virtual environment there. Do not reuse TaskForge's `.venv`, import
its `app/`, access its database, or change production files. No earlier learner
submission or future production ticket is needed.

## Scenario and requirements

A small museum needs a starter repository that another curator can run locally.
Create a Django project named `cabinet` and an empty app named `exhibits`;
register the app in the project. Keep the standard development welcome page.

Choose and record the supported Python series, pin Django and its resolved
runtime dependencies in a requirements file, and create `SETUP.md` with commands
for creating an isolated environment, installing dependencies, checking Django,
applying built-in migrations to disposable local SQLite and starting/stopping
the server on loopback. State which files are source and which are generated.
Do not store a real credential; clearly identify these as development settings.
No exhibit records, custom endpoints, deployment or PostgreSQL are needed.

## Acceptance criteria

- [ ] All authored files and evidence are inside this task's workspace, with no production imports or database references.
- [ ] The supported Python series is recorded as 3.14; Django is pinned to 5.2.19 and every installed runtime dependency is pinned to an exact version.
- [ ] The `cabinet` project loads and the `exhibits` app is registered with Django.
- [ ] A fresh separate virtual environment installs from the authored requirements file and `pip check` reports no broken requirements.
- [ ] Django's system check reports no issues and built-in migrations apply to a new disposable SQLite database.
- [ ] The development server binds to loopback and returns HTTP 200 with the standard Django installation success page at `/`.
- [ ] `SETUP.md` includes working setup/run/stop commands, the development-only limitation and generated-file boundaries; no real secrets or generated environments/databases are submitted as source.

## Validation

Use your new environment's Python to run `python -m pip check` and
`python -m django --version`; expect no broken requirements and `5.2.19`.
Run `python manage.py check` and `python manage.py migrate` from the directory
containing your management script; expect no system-check issues and successful
migrations. Use `python manage.py shell` to inspect Django's app registry for
`exhibits` (a directory alone does not register an app).

Start your server on `127.0.0.1:8001`, then use a browser or
`curl -i http://127.0.0.1:8001/` to inspect the status and welcome content.
Stop it when finished. Repeat installation and startup in a temporary copy
containing only your source files and a new virtual environment/database.
Do not reuse the first environment as proof of a clean install. An import
error, dependency mismatch, missing app registration, migration failure or
non-200 response fails the corresponding criterion. Keep all tests on local,
disposable resources; never bind publicly or use real credentials.

## Official documentation

- [Python 3.14 venv](https://docs.python.org/3.14/library/venv.html)
- [Django 5.2 project/app structure and runserver](https://docs.djangoproject.com/en/5.2/intro/tutorial01/)
- [Django 5.2 installation and Python compatibility](https://docs.djangoproject.com/en/5.2/faq/install/)

## Submission and help

Put the project, empty app, requirements file, Python compatibility record,
`SETUP.md`, and sanitized validation evidence in `workspace/`. Record working
directories, versions, actual commands and observed results in `EVIDENCE.md`.
Virtual environments, caches and SQLite databases are disposable and must stay
out of source submissions. Leave the production application unchanged.

Ask for a hint about environment isolation, dependency pinning or app
registration, or request a review against these criteria. A full solution is
available only if you explicitly ask for one.
