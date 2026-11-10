# Ticket tracking

One row per original production ticket. The backlog holds requirements; this
file holds status. No ticket is complete at starter creation.

Production: NOT_STARTED → IN_PROGRESS → DONE; use BLOCKED with a reason in
`PROGRESS.md` when progress cannot continue. At most one IN_PROGRESS/BLOCKED
production ticket. DONE means all criteria have observed verification evidence
and exactly one learner TASK.md exists, not that learner practice is finished.

Learner: NOT_GENERATED → READY → IN_PROGRESS → COMPLETE. READY means TASK.md
exists; COMPLETE requires learner validation/review evidence. Learner status
does not gate a new explicitly requested production ticket.

In the evidence column, link to the matching entry in `PROGRESS.md` once work
starts. Use a heading `## TSK-XXX` there and append dated updates on retries.
Optional tickets remain NOT_STARTED unless explicitly requested.

| Ticket | Title | Production | Learner | Evidence |
| --- | --- | --- | --- | --- |
| TSK-001 | Record architecture and scope decisions | NOT_STARTED | NOT_GENERATED | — |
| TSK-002 | Initialize repository and ignore rules | NOT_STARTED | NOT_GENERATED | — |
| TSK-003 | Establish Python and Django environment | NOT_STARTED | NOT_GENERATED | — |
| TSK-004 | Configure environment-dependent settings | NOT_STARTED | NOT_GENERATED | — |
| TSK-005 | Implement health endpoint and smoke check | NOT_STARTED | NOT_GENERATED | — |
| TSK-006 | Connect PostgreSQL in development | NOT_STARTED | NOT_GENERATED | — |
| TSK-007 | Design Task schema and ownership | NOT_STARTED | NOT_GENERATED | — |
| TSK-008 | Create and verify Task migrations | NOT_STARTED | NOT_GENERATED | — |
| TSK-009 | Add model and persistence tests | NOT_STARTED | NOT_GENERATED | — |
| TSK-010 | Configure two demo users securely | NOT_STARTED | NOT_GENERATED | — |
| TSK-011 | Implement session login | NOT_STARTED | NOT_GENERATED | — |
| TSK-012 | Implement logout safely | NOT_STARTED | NOT_GENERATED | — |
| TSK-013 | Protect authenticated application routes | NOT_STARTED | NOT_GENERATED | — |
| TSK-014 | Test login, logout and route protection | NOT_STARTED | NOT_GENERATED | — |
| TSK-015 | Build shared layout and navigation | NOT_STARTED | NOT_GENERATED | — |
| TSK-016 | List only current user's tasks | NOT_STARTED | NOT_GENERATED | — |
| TSK-017 | Create tasks with validated form | NOT_STARTED | NOT_GENERATED | — |
| TSK-018 | Edit tasks with ownership checks | NOT_STARTED | NOT_GENERATED | — |
| TSK-019 | Toggle task completion | NOT_STARTED | NOT_GENERATED | — |
| TSK-020 | Delete task with confirmation | NOT_STARTED | NOT_GENERATED | — |
| TSK-021 | Test task CRUD behaviours | NOT_STARTED | NOT_GENERATED | — |
| TSK-022 | Test cross-user isolation comprehensively | NOT_STARTED | NOT_GENERATED | — |
| TSK-023 | Review forms, templates and session security | NOT_STARTED | NOT_GENERATED | — |
| TSK-024 | Improve usability and error handling | NOT_STARTED | NOT_GENERATED | — |
| TSK-025 | Create test matrix and regression instructions | NOT_STARTED | NOT_GENERATED | — |
| TSK-026 | Test production-like settings and failure modes | NOT_STARTED | NOT_GENERATED | — |
| TSK-027 | Package Django with Docker | NOT_STARTED | NOT_GENERATED | — |
| TSK-028 | Run application and PostgreSQL with Compose | NOT_STARTED | NOT_GENERATED | — |
| TSK-029 | Handle migrations and static assets in containers | NOT_STARTED | NOT_GENERATED | — |
| TSK-030 | Test container startup and persistence | NOT_STARTED | NOT_GENERATED | — |
| TSK-031 | Provision and harden Linux VPS | NOT_STARTED | NOT_GENERATED | — |
| TSK-032 | Configure domain/DNS and Caddy HTTPS | NOT_STARTED | NOT_GENERATED | — |
| TSK-033 | Deploy production Compose stack | NOT_STARTED | NOT_GENERATED | — |
| TSK-034 | Verify production security configuration | NOT_STARTED | NOT_GENERATED | — |
| TSK-035 | Add CI for checks, lint and tests | NOT_STARTED | NOT_GENERATED | — |
| TSK-036 | Create gated deployment workflow | NOT_STARTED | NOT_GENERATED | — |
| TSK-037 | Configure structured-enough application logs | NOT_STARTED | NOT_GENERATED | — |
| TSK-038 | Add basic uptime and health monitoring | NOT_STARTED | NOT_GENERATED | — |
| TSK-039 | Define database backup procedure | NOT_STARTED | NOT_GENERATED | — |
| TSK-040 | Prove database restoration | NOT_STARTED | NOT_GENERATED | — |
| TSK-041 | Perform end-to-end release acceptance | NOT_STARTED | NOT_GENERATED | — |
| TSK-042 | Consolidate operations runbook and handoff | NOT_STARTED | NOT_GENERATED | — |
| TSK-043 | Add self-service registration | NOT_STARTED | NOT_GENERATED | — |
| TSK-044 | Add task ordering and filters | NOT_STARTED | NOT_GENERATED | — |
| TSK-045 | Automate backup scheduling and alerts | NOT_STARTED | NOT_GENERATED | — |
| TSK-046 | Add lightweight error-rate visibility | NOT_STARTED | NOT_GENERATED | — |
