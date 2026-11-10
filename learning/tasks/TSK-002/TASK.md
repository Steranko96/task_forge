# Keep a weather notebook repository clean

## Title and source ticket

One independent Git hygiene exercise derived from
[TSK-002](../../../BACKLOG.md#tsk-002--initialize-repository-and-ignore-rules).
Status: READY. Submission location: `learning/tasks/TSK-002/workspace/`.

## Objective

Create one local weather notebook repository that tracks its useful inputs
and instructions while keeping local configuration and generated output out
of commits. Suggested timebox: 30–45 minutes.

## Concepts

Git records staged snapshots. Ignore rules filter untracked files; they do
not remove files already tracked or detect secrets inside ordinary documents.
A focused branch, explicit staging and a reviewed diff make changes easier
to assess. Safe example configuration explains setup without sharing secrets.

## Prerequisites and setup

Use Git 2.23 or later, a shell and a text editor; no Python, Django or online
account is needed. Git 2.54.0 was available when this task was created.
Create `workspace/weather-notebook/` as a separate local Git repository.
Run its Git commands from that directory and confirm `git rev-parse
--show-toplevel` points there before any staging or commits. Do not stage or
commit the outer TaskForge repository. Keep the exercise repository local:
no remote, pushes, deployments, paid services or real credentials.
Use a fictional local commit identity if necessary; avoid changing global
Git configuration.

## Scenario and requirements

A community garden keeps a small weather notebook. Create these synthetic
inputs yourself inside the exercise repository:

- `observations.csv`: a header and two fictional weather observations.
- `README.md`: the notebook's purpose and your branch/commit workflow.
- `config/example.ini`: an example sensor configuration using placeholders.
- `config/local.ini`: local sensor configuration using an obviously fake token.
- `reports/daily.txt`: a pretend generated summary.
- `.cache/sensor.tmp`: pretend cached sensor data.

Write your own `.gitignore`. Keep observations, instructions and example
configuration trackable; ignore local configuration, all generated reports
and cache contents. Make an initial commit of intended files, then use a
separate `practice/describe-observations` branch for a small README improvement
and a second focused commit. Do not implement a weather application.

Create `workspace/REVIEW.md` with the checks you actually ran and their
observed results, plus a short written response to this hypothetical incident:
someone committed a real sensor token before adding an ignore rule. Explain
what the ignore rule can and cannot fix and what actions are needed. Do not
create or commit a real token to rehearse the incident.

## Acceptance criteria

- [ ] `weather-notebook/` is an independent local Git repository with no remote and at least two commits: an initial snapshot and one focused README change on `practice/describe-observations`.
- [ ] `git ls-files` includes `.gitignore`, `README.md`, `observations.csv` and `config/example.ini` and excludes local configuration, reports and caches.
- [ ] Local configuration, report and cache files exist with synthetic content; their ignore checks succeed. Example configuration and observations remain trackable.
- [ ] The README documents branch naming, focused commits, explicit staging and review of the staged diff before committing.
- [ ] The exercise repository has a clean working tree after commits, with ignored files still present locally.
- [ ] `REVIEW.md` records actual commands/results and explains both the tracked-file limitation and credential revocation/rotation after exposure; it makes no claim to have rehearsed real credential cleanup.
- [ ] All content is fictional or placeholder-only; no TaskForge files, production services or credentials were used or modified.

## Validation

From `workspace/weather-notebook/`, inspect `git log --oneline --all`,
`git branch --show-current`, `git remote -v` and `git ls-files`. Check that the
history, branch and tracked inventory meet the criteria; remote output should
be empty. Inspect `git show --stat` and the latest diff to confirm the second
commit contains only the intended README change.

Use `git check-ignore -v --no-index <path>` for each local/generated file and
for the example configuration and observations. Ignored files should identify
an excluding rule; trackable files must have no effective excluding rule
(a matching `!` rule means inclusion). Use the quiet form
`git check-ignore -q --no-index <path>` if checking exit codes: 0 means ignored,
1 means not ignored. Test an additional path beneath each ignored directory
to ensure your rules cover future output too.

Inspect `git status --short` for a clean tree and `git status --short --ignored`
to confirm ignored local files still exist. Review committed content for
accidentally staged fake local configuration as well as real secrets. Record
failures honestly and repair them before declaring a criterion passed. This
task intentionally provides requirements and checks without an ignore-rule
solution or a sequence of implementation commands.

## Official documentation

Links verified on 2026-11-10. These Git concepts apply to the version above.

- [Git ignore pattern rules and tracked-file limitations](https://git-scm.com/docs/gitignore)
- [Git book: reviewing, staging and committing changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
- [GitHub: responding to committed sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)

## Submission and help

Leave the local repository, including its local history, in
`learning/tasks/TSK-002/workspace/weather-notebook/` and your evidence in
`learning/tasks/TSK-002/workspace/REVIEW.md`. Do not add the nested repository
to TaskForge's Git index. The provided workspace contains only `.gitkeep`;
there is no solution. Ask for a concept explanation, a hint or a review
against these criteria when ready.
