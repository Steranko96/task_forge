# Title and source ticket

Seed Library configuration rehearsal — independent practice for
[TSK-004](../../../BACKLOG.md#tsk-004--configure-environment-dependent-settings).
Status: READY. Submission: `learning/tasks/TSK-004/workspace/`.

## Objective

Build one offline Python configuration validator for a fictional community seed
library. Suggested timebox: 45–60 minutes. It loads configuration, validates it,
and reports readiness without running a web server or connecting to a database.

## Concepts

Environment variables separate deployment choices from source code. Strings
need explicit parsing before they can safely control behavior. Secure defaults
and startup errors prevent incomplete configuration from silently becoming an
unsafe service. Examples document variable names without supplying credentials.

## Prerequisites and setup

Use Python 3.14.x and its standard library, an editor and a terminal. Start in
this task's empty workspace. No Django, database, network access, paid service,
production import or prior learner submission is required. Use only synthetic
values in tests. Do not source TaskForge's `.env` or reuse its database/key.

## Scenario and requirements

A volunteer wants to validate the seed library's future service configuration
before it starts. Create `seed_config.py` with a command-line entry point and
an importable configuration-loading function. Define the following inputs:

| Variable | Required behavior |
| --- | --- |
| `SEED_MODE` | Default `production`; accept only `development` or `production`. |
| `SEED_SIGNING_KEY` | Required and nonblank in every mode. No generated or hardcoded fallback. |
| `SEED_DEBUG` | Default `false`; accept `true`/`false` ignoring case and surrounding whitespace; reject other values and reject true in production. |
| `SEED_HOSTS` | Split comma-separated hosts and trim/discard empty entries. Production requires at least one host and rejects `*`. |
| `SEED_DB_NAME`, `SEED_DB_USER`, `SEED_DB_PASSWORD`, `SEED_DB_HOST` | All required and nonblank in production. Development may leave them unset, yielding no database configuration. If any is provided in development, require all four. |

Return the parsed configuration to callers, including secret values needed by
an eventual service, but never print those secrets. The CLI must exit 0 for
valid configuration and print a short readiness message; invalid configuration
must exit nonzero and identify the invalid/missing variable without its value.
Do not implement a server, database connection, real signing operation or host
header validation. This exercise concerns loading and validating configuration.

Supply one `seed.env.example` containing all names and only empty secrets plus
illustrative values, a `README.md` explaining how to export variables and run
the validator, and automated standard-library tests in `test_seed_config.py`.
Never include private environment files or a completed deployment setup.

## Acceptance criteria

- [ ] All authored files are in this workspace and use only the standard library, with no TaskForge imports or resources.
- [ ] The loader returns correctly parsed values and the CLI exits 0 for complete synthetic production configuration with debug disabled.
- [ ] Missing/blank signing keys and every missing/blank production database field cause nonzero CLI exit and identify the variable without exposing either secret.
- [ ] Omitted mode selects production, unknown modes fail, and omitted debug is false; production debug true fails and invalid boolean strings fail.
- [ ] Host lists are trimmed and split; empty lists and wildcard hosts fail in production.
- [ ] Development accepts no database configuration, rejects partially supplied database configuration, and accepts all four fields together.
- [ ] The example contains every variable, empty secret fields and no usable credentials; README describes setup, defaults, validation and secret handling.
- [ ] Automated tests cover valid configurations and the failure cases above, isolate ambient environment variables and pass without accessing any service.

## Validation

From your workspace run `python3.14 -m unittest discover -v`; expect all tests
to pass. Exercise the CLI in separate processes with synthetic environment
values and capture exit codes. Check a complete production case, a minimal
development case, each missing/blank secret, a partial development database
configuration, an unknown mode, malformed debug input (including `false` versus
`true`), production debug true, and empty/wildcard production hosts.

Run a production case with `SEED_MODE` omitted to verify that omission cannot
enable development conveniences. For failure cases, inspect stdout and stderr
and assert that the synthetic signing key/password never appear. Also check
successful output for leaks. Clear or replace environment values between cases;
your shell's existing configuration must not make a failing case pass. Record
actual commands and outcomes, using synthetic values only. No real database
or deployed service should be contacted.

## Official documentation

- [Python 3.14 process environment](https://docs.python.org/3.14/library/os.html#os.environ)
- [Python 3.14 unittest and discovery](https://docs.python.org/3.14/library/unittest.html)
- [Twelve-Factor configuration](https://12factor.net/config)
- [Django 5.2 deployment checklist: secret keys, debug and hosts](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/) — conceptual context; Django is not needed for this exercise.

## Submission and help

Submit `seed_config.py`, `test_seed_config.py`, `seed.env.example`, `README.md`
and sanitized `EVIDENCE.md` in `workspace/`. Evidence should include the Python
version, working directory, actual test/CLI commands, exit codes and results.
Do not submit real keys/passwords, generated environments or database files.

Ask for a hint about boolean parsing, fail-safe defaults, environment isolation
or redacting output, or request a review against these criteria. A full solution
is available only on explicit request.
