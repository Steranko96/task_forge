# TaskForge

## 1. Project Overview

TaskForge is a full-stack, multi-user task management application
built with Django.

The purpose of this project is to develop practical software
engineering skills by studying verified production changes made by Codex,
then independently implementing a related learner task for each ticket.
The production application is still designed, tested, deployed, and operated
against the requirements below.

## 2. Learning Objectives

By completing this project, I should understand:

- HTTP request/response lifecycle
- Django project architecture
- URL routing, views, and templates
- Relational database modelling
- Django ORM and migrations
- Authentication and authorisation
- HTML forms and validation
- Automated testing
- Environment configuration
- Docker and Docker Compose
- Linux server administration
- Reverse proxies and HTTPS
- CI/CD pipelines
- Application logging and monitoring
- Basic application security

## 3. Technology Stack

- Python
- Django
- HTML/CSS
- Django Templates
- PostgreSQL
- Django TestCase
- Git and GitHub
- Docker and Docker Compose
- Gunicorn
- Caddy
- GitHub Actions
- DigitalOcean VPS

Avoid unnecessary frameworks and dependencies.

## 4. Functional Requirements

The application must support:

### Authentication
- User login
- User logout
- Session-based authentication
- Protected routes

### Task Management
- Create tasks
- View tasks
- Update tasks
- Complete/uncomplete tasks
- Delete tasks

### User Isolation
- Every task belongs to a user.
- Users can only access their own tasks.
- Unauthorised access must be prevented server-side.

### Database
- PostgreSQL persistence
- Django ORM
- Database migrations

## 5. Engineering Requirements

### Development
- Reproducible local environment
- Environment variables
- Git version control

### Testing
- Automated Django tests
- Authentication tests
- CRUD tests
- Authorisation tests

### Deployment
- Docker containerisation
- Docker Compose
- Linux VPS
- Gunicorn
- Caddy
- HTTPS

### CI/CD
- Automated linting
- Automated tests
- Deployment workflow

### Operations
- Application logging
- Health endpoint
- Basic monitoring
- Database backup and recovery

## 6. Constraints

- Target completion: 5 days
- Approximately 50 focused hours
- Keep the application deliberately simple
- Prioritise functionality and understanding
- Use official documentation
- Avoid unnecessary abstractions
- Codex implements exactly one explicitly requested production ticket at a time
- The learner independently implements one related task per completed production ticket

## 7. Delivery Milestones

### Milestone 1: Foundations
Working Django application and health endpoint.

### Milestone 2: Database
Task model, relationships, migrations, and persistence.

### Milestone 3: Authentication
Login, logout, and protected views.

### Milestone 4: Application
Task CRUD, templates, and user isolation.

### Milestone 5: Testing
Core automated test suite.

### Milestone 6: Containerisation
Docker and PostgreSQL running through Compose.

### Milestone 7: Deployment
Application accessible over HTTPS on a VPS.

### Milestone 8: Operations
CI/CD, logging, monitoring, and recovery.

## 8. Definition of Done

The project is complete when:

- Two separate users can authenticate.
- Users can independently manage their tasks.
- Data persists in PostgreSQL.
- Users cannot access another user's tasks.
- Core automated tests pass.
- The application runs using Docker.
- Production is accessible over HTTPS.
- CI runs successfully.
- Application logs can be inspected.
- Database backup and restoration have been verified.

## 9. Learning Rules

The user explicitly requests each production ticket by ID. Codex implements
that ticket, including its relevant tests and verification, without requiring
the learner to write the production implementation.

After the production ticket meets its acceptance criteria, Codex creates
exactly one independent learner task at `learning/tasks/TSK-XXX/TASK.md`.
The task applies the ticket's core concepts to a small separate problem.
The learner writes that solution in `learning/tasks/TSK-XXX/workspace/`,
without changing or depending on the production application.

Do not generate the complete application, batch tickets, pre-create learner
tasks, or start another production ticket automatically. Stop after the
requested ticket and its single learner task are complete.

Tutoring is on demand. Explain concepts, give progressively stronger hints,
and review learner work when asked. Do not require quizzes, explanations,
or learner completion before accepting an explicit request for another ticket.
Do not provide learner solutions unless explicitly requested.

See `AGENTS.md`, `learning/README.md`, and `docs/TICKETS.md` for workflow,
learner task requirements, tracking, and verification rules.
