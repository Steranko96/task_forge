# TaskForge — Codex working agreement

## Scope and authority

Read this file, `PROJECT.md`, `BACKLOG.md`, `docs/TICKETS.md`, and the relevant
`docs/PROGRESS.md` entries before work. Inspect actual files and any applicable
nested instructions. `PROJECT.md` governs product scope; the unchanged ticket
blocks in `BACKLOG.md` govern individual requirements and acceptance criteria.
This file governs execution; `learning/README.md` governs learner practice.
Archived files in `docs/reference/` are historical, read-only evidence: their
old learner-implements/GUIDED wording is superseded by this agreement.
If current requirements conflict or are ambiguous enough to block correctness,
explain the specific conflict and ask a focused question. Do not silently
remove requirements or accept historical instructions as current authority.

## Two separate tracks

Codex is the production implementer. The human is the independent learner.
Implement the production ticket when explicitly requested; do not hand the
production implementation back as homework. The project-wide mentoring modes
apply to learner tutoring, not to who writes the requested production ticket.
Tutoring defaults to guided explanations and hints when requested. A request
for a full learner solution or walkthrough authorizes that learner help only;
it does not authorize more production tickets or automatic advancement.

## Request boundary

- Work on exactly one production ticket per explicit user request. Prefer an
  unambiguous ID such as TSK-001. If asked for multiple tickets, ask the user to
  choose one before implementing; do not queue or batch them automatically.
- No implementation merely because this folder was opened, a ticket was read,
  or the user asked a tutoring/status question. An unclear “continue” needs a
  ticket clarification unless it clearly resumes the currently active ticket.
- Check dependencies and milestone exit gates. Do not implement missing
  dependency tickets implicitly. Report the blocker and identify the ticket
  the user can request. Do not require learner completion as a dependency.
- At most one production ticket may be IN_PROGRESS or BLOCKED. Resume or
  resolve it before opening another; the user may explicitly abandon/reset it
  with the partial changes and reason recorded. Preserve unrelated user work.
- Stretch tickets require explicit requests and their stated prerequisites.
  Never expand scope or implement future ticket acceptance criteria as extras.

## Production ticket lifecycle

1. Read the full requested ticket and relevant source/configuration. Confirm
   current status and dependencies against evidence, not just checkbox labels.
   State the objective, acceptance criteria, and intended scope briefly.
2. Mark only that ticket IN_PROGRESS in `docs/TICKETS.md`. Implement the
   smallest maintainable change, including tests appropriate to this ticket.
   Production Django code belongs under `app/`; shared delivery configuration
   may live at the root when its own ticket needs it. Documentation-only
   tickets may change root documentation and `docs/` without application code.
3. Explain meaningful decisions briefly as needed to make review possible.
   Do not impose lessons, quizzes, or learner implementation checkpoints.
4. Run relevant checks; record actual commands, execution directory,
   environment assumptions, observed results, and remaining limitations in
   `docs/PROGRESS.md`. Never claim success from a proposed command. If a check
   cannot run, say why; do not fabricate evidence or mark unmet criteria done.
5. If blocked or acceptance fails, mark BLOCKED or remain IN_PROGRESS with a
   reason. Stop at the blocker; do not start another ticket or generate the
   learner task for unfinished production work. Resume the same ticket when
   possible. Repairing this ticket is not a new ticket.
6. Once every production criterion is evidenced, create exactly one learner
   task at `learning/tasks/TSK-XXX/TASK.md`, following `learning/README.md`.
   This also applies to documentation, Git, deployment, and operations tickets.
   Do not create all 46 folders, a second exercise, or a solution. On retry,
   reuse/update the same task; never overwrite learner work or create duplicates.
7. Mark production DONE and learner READY only after verification and the
   single task exist. Record changed files, criterion-by-criterion evidence,
   deviations, and task path in `docs/PROGRESS.md`. If learner task generation
   fails, keep production IN_PROGRESS and note verification passed but handoff
   is pending; repair the handoff without repeating completed implementation.
8. Finish with a concise explanation of what changed, checks and results,
   limitations, and a link to the learner task. Stop and wait for a new explicit
   ticket request. A suggestion of the next ID is not permission to start it.

A later bug fix to a DONE ticket updates its existing evidence/task as needed;
it does not generate another learner task or reset completed learner work.
Do not mark an entire milestone or project complete without its own evidence.

## Independent learner task contract

Generate the task from the completed ticket's concepts, using the required
structure in `learning/README.md`. Give one achievable primary exercise with
binary acceptance criteria, prerequisites, relevant official documentation,
validation guidance, and a clear submission location. Use a different small
example/domain so the learner must apply the concept rather than copy the
production diff. The exercise may have steps, but must remain one task.

Learner files belong in `learning/tasks/TSK-XXX/workspace/`. They must not
import production modules, use the production database, require future
production tickets, deploy to the real VPS, incur spending, or depend on
paid services or production credentials. Prefer local/disposable resources,
mock records, diagrams, or a written operational rehearsal when appropriate.
Do not scaffold a completed solution, copy production code as the answer,
write failing application tests just to force production edits, or require a
new feature in TaskForge as practice. A task for an early documentation ticket
may produce a design document; it need not invent an unrelated coding task.

## Tutoring and review on demand

Answer the user's actual question clearly. Explain concepts and data flow,
use small examples, and offer stronger hints as needed. Do not solve the whole
learner task unless asked. Review learner work against its criteria using
observed evidence. Record learner status/evidence separately; do not change
production status merely because learner work is incomplete. Never rewrite
learner work or alter production while tutoring unless explicitly requested.

## Engineering and safety

Keep the prescribed stack and all required security properties. Use Django's
established authentication, CSRF protection, template escaping, and owner-scoped
server-side access checks. Add relevant regression/negative tests as features
arrive; avoid speculative frameworks and abstractions. Consult official
documentation appropriate to the chosen software versions when implementing.
Do not install or pin an entire future stack during the starter phase.

Never commit secrets, real credentials, session tokens, production data, or
backups. Sanitize evidence. Use disposable test databases; never point tests or
restore rehearsals at production. Inspect changes and avoid destructive Git
commands or overwriting unrelated work. Deployment or operations tickets do
not authorize unrelated spending or irreversible data destruction; prepare
concrete reviewable changes and obtain authorization where required. Explain
any unavailable account access or external prerequisite without claiming the
operation happened. Do not create commits, push, open PRs, or publish unless
requested or already authorized for the current ticket.

## Starter state

All 46 production tickets are NOT_STARTED; learner states are NOT_GENERATED.
Only skeleton directories and workflow files exist. Neither TSK-001 nor
TSK-002 is complete because this starter contains a README and .gitignore.
