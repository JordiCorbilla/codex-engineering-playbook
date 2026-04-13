# Codex Engineering Playbook

This repository teaches Codex how to implement and review production-style application code across three areas:

- C# backend development
- Python backend development
- React + TypeScript frontend development

Use this file for durable repository-wide guidance. For recurring work, prefer the relevant skill under `.agents/skills`. When a template or script fits the task, use it instead of re-describing deterministic steps in prose.

## Working Approach

- Inspect the existing project structure before adding code.
- Keep changes minimal, coherent, and consistent with this playbook.
- Preserve clear boundaries between API, application/service, domain, and infrastructure layers.
- Keep controllers, routes, and UI rendering thin; move business logic into services or domain-focused modules.
- Explain trade-offs when making architecture decisions, especially when choosing simplicity over abstraction or vice versa.
- For non-trivial multi-file tasks, create a short execution plan before editing.

## Definition Of Done

A task is done when:

- code is placed in the correct layer and follows the relevant convention document
- templates or scripts are used where they reduce ambiguity or repeated effort
- tests, linting, and build checks are updated or run where available
- error handling and validation are consistent with the surrounding code
- public contracts and boundaries remain explicit
- the final change is small enough to review and clearly explained

## Validation

- Run the most relevant validation available for the touched area
- Prefer targeted checks first, then broader project checks when practical
- If full validation is not possible, state what was validated and what remains manual
