# Independent learning track

For each explicitly requested, verified production ticket, Codex generates
exactly one task at `learning/tasks/TSK-XXX/TASK.md`. There are no tasks yet.
You implement that task yourself, independently of TaskForge's production app.

## Your workflow

1. Read the generated task and its acceptance criteria.
2. Put your work in `learning/tasks/TSK-XXX/workspace/`. The exercise defines
   its own small inputs and setup; it does not require production services.
3. Validate your result and keep useful evidence alongside your solution.
4. Ask for explanations, hints, or a review whenever useful. For example:
   “Explain the concept behind TSK-008 without solving my learner task” or
   “Review my TSK-008 learner workspace against TASK.md.”

You can ask for the next production ticket before finishing practice. Codex
never starts it automatically. Production DONE and learner COMPLETE are
separate claims. A full solution is available on explicit request; the default
is help that leaves the implementation to you.

## Required TASK.md structure (for Codex)

Create these sections only after the matching production ticket is verified:

- **Title and source ticket:** One learner exercise linked to TSK-XXX; task
  status and intended submission path.
- **Objective:** One concrete result, with a manageable suggested timebox.
- **Concepts:** The ticket's core transferable ideas, explained briefly.
- **Prerequisites and setup:** Explicit local tools/versions if needed; local
  or disposable resources only. Include enough context to stand alone without
  reading/copying the production solution. No future-ticket dependencies.
- **Scenario and requirements:** A distinct small problem applying those ideas,
  with clear inputs, boundaries, expected behavior, and deliverables. For an
  operational concept, use a safe local simulation or written rehearsal.
- **Acceptance criteria:** Observable pass/fail checks for this one exercise.
- **Validation:** Commands or manual checks the learner can use, expected
  outcomes, and relevant failure/security cases; never a completed solution.
- **Official documentation:** A few focused links relevant to the actual
  versions/concepts. Verify them when creating the task.
- **Submission and help:** Files to place in `workspace/`, evidence to capture,
  and how to ask for tutoring or review.

Create `workspace/.gitkeep` alongside the task if the workspace is empty.
Do not include a worked answer, generate a second task, create separate TASK.md
files for substeps, or pre-create tasks for unimplemented tickets. Any reusable
format is this section, not a set of pre-generated ticket assignments.

## Independence and review

The exercise must run or be assessable without importing `app/`, altering
TaskForge, accessing production data, using real secrets, or paying for cloud
services. Avoid simply retyping the production implementation. Documentation
and infrastructure tickets still get one concept-matched independent exercise.

Use READY → IN_PROGRESS → COMPLETE for learner status in `docs/TICKETS.md`.
Record actual review/validation evidence in `docs/PROGRESS.md` before marking
COMPLETE. Leave the human's solution intact; provide feedback first unless
asked to edit. Revisions use the same TASK.md and workspace.
