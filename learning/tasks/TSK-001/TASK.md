# Design a private reading journal

## Title and source ticket

One independent architecture exercise derived from
[TSK-001](../../../BACKLOG.md#tsk-001--record-architecture-and-scope-decisions).
Status: READY. Submit your work in `learning/tasks/TSK-001/workspace/`.

## Objective

Write one concise design document for a private reading journal that another
person could review before implementation. Suggested timebox: 30–45 minutes.
No application code or running services are required.

## Concepts

Components divide responsibilities. A request path explains how those
components cooperate to produce a response. Authentication identifies the
reader; authorization determines which entries they may access. Explicit
scope boundaries keep the design achievable, and a verification plan makes
its promises checkable.

## Prerequisites and setup

Use a text editor to create Markdown; no particular editor version is required.
A browser is useful for the documentation below. You do not need Python,
Django installed, a database, cloud access or credentials. Use fictional
readers and journal entries only. Work entirely inside this exercise's
workspace, without importing or changing TaskForge.

## Scenario and requirements

Two members of a small book club each want a private reading journal. Each
member can sign in, sign out, list their own entries, add an entry, edit it
and delete it. Each entry records a book title and a short private reflection.
Members must never read or change one another's entries, even by changing an
entry identifier in a request.

Produce `workspace/DESIGN.md` describing the smallest viable design. Choose
Django server-rendered pages and PostgreSQL, with ordinary HTML forms and
session authentication. State the responsibilities of the browser,
application and storage, the ownership relationship, and where access rules
are enforced. Describe a hypothetical HTTPS deployment boundary, including
which services may be reached publicly. This is a written design only.

Trace both reading the entry list and submitting an edit, including a rejected
edit of another member's entry. Choose at least three features to exclude or
defer and give a brief reason for each. Include a two-member verification
matrix with actions and observable expected outcomes. Finish with a short
self-review record of the validation below. Keep all of this in one document;
do not implement the journal or supply real account details.

## Acceptance criteria

- [ ] `workspace/DESIGN.md` identifies each component's responsibility and the public/private deployment boundary.
- [ ] It defines one required owner per journal entry, permits multiple entries per member, and places access enforcement on the server.
- [ ] It traces the list GET and edit POST from browser to storage and back, including session identification, validation, CSRF and the successful response.
- [ ] It explains how an attempted foreign-entry edit is denied without exposing the reflection or changing stored data.
- [ ] It explicitly excludes or defers at least three features, with a reason for each.
- [ ] Its verification matrix includes successful workflows for both fictional members, list isolation, direct foreign-entry reads and edits, logged-out access, invalid form input, missing CSRF and logout. Each row states an action and a pass/fail outcome.
- [ ] A self-review records whether each criterion above passes or needs revision; no code, real secrets, paid resources or production data are used.

## Validation

Read your document as someone who has not seen TaskForge. Manually check each
criterion and record the outcome in the self-review. Follow both request
traces end to end: every handoff should name a responsible component and
explain what returns to the browser. Check that the successful and rejected
edit paths cannot contradict the ownership rule.

For each verification row, ask whether a second person could tell pass from
fail using the expected outcome alone. Explicitly examine a guessed entry
identifier, forged ownership input, invalid reflection/title input and a
missing CSRF token. Correct contradictions before submission. These are
paper checks of a design; do not report runtime tests as passed.

## Official documentation

Read these Django 5.2 references for the concepts; no installation is needed.
Links verified on 2026-11-10.

- [Django overview](https://docs.djangoproject.com/en/5.2/intro/overview/)
- [Django security](https://docs.djangoproject.com/en/5.2/topics/security/)

## Submission and help

Submit `learning/tasks/TSK-001/workspace/DESIGN.md`, including the verification
matrix and self-review evidence. The workspace is intentionally empty except
for `.gitkeep`. Ask for a concept explanation, a hint about a specific
criterion, or a review against this task when ready. A worked solution is
available only if you explicitly request one.
