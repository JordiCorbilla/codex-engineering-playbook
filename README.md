# Codex Engineering Playbook

`codex-engineering-playbook` is a reusable repository for teaching Codex how to implement and review production-style application code across three common areas:

- C# backend development
- Python backend development
- React + TypeScript frontend development

This is not a prompt dump. The repository is structured as an engineering playbook: stable repo-wide guidance in [AGENTS.md](AGENTS.md), reusable workflow instructions in [.agents/skills](.agents/skills), deterministic implementation support in [templates](templates) and [scripts](scripts), and small example applications under [examples](examples).

## Why Separate AGENTS.md And Skills

`AGENTS.md` should stay compact, durable, and repository-wide. It defines the operating model:

- inspect structure before changing code
- preserve clear boundaries
- validate work before calling it done
- explain trade-offs when architecture changes

Skills handle recurring workflows that are too specific or too detailed for the top-level file. For example, [csharp-backend-feature](.agents/skills/csharp-backend-feature/SKILL.md) and [python-backend-review](.agents/skills/python-backend-review/SKILL.md) tell Codex how to route implementation and review work without turning `AGENTS.md` into a giant style blob.

This separation matters because durable guidance and workflow guidance change at different rates. `AGENTS.md` should survive most repository evolution. Skills can become more specific as patterns repeat.

## Repository Layout

```text
.
|-- AGENTS.md
|-- README.md
|-- .agents/skills/
|-- blog/
|-- conventions/
|-- examples/
|-- scripts/
`-- templates/
```

- [conventions](conventions) explains the engineering opinions behind the playbook.
- [.agents/skills](.agents/skills) contains focused implementation, review, contract, and reconnaissance workflows.
- [templates](templates) contains implementation starting points when structure is deterministic enough to be templated.
- [scripts](scripts) contains lightweight helper utilities for scanning repositories, discovering tests, finding likely insertion points, summarizing changed files, and validating repository coherence.
- [examples](examples) contains small but credible projects that make the playbook concrete.
- [blog](blog) contains the technical write-up of what the repository is trying to achieve.

## Conventions And Intentional Opinions

The convention documents are concise on purpose:

- [architecture.md](conventions/architecture.md) defines layering, boundaries, testing expectations, error-handling philosophy, and when simplicity should beat abstraction.
- [csharp.md](conventions/csharp.md) covers controllers versus services versus repositories, DI, async discipline, DTO boundaries, logging, and minimal APIs versus controllers.
- [python.md](conventions/python.md) focuses on service-oriented structure, typed boundaries, validation, async restraint, module organization, and explicitness over cleverness.
- [react-typescript.md](conventions/react-typescript.md) covers component structure, hook discipline, state management, API client separation, typing, async UI states, accessibility, and keeping rendering logic readable.

These are intentionally opinionated. They are optimized for repeatability and maintainability, not for encoding every valid architecture choice. When a trade-off is real, the playbook says so.

## Example Applications

The examples are deliberately small, but they are not throwaway snippets:

- [examples/csharp-api](examples/csharp-api) shows controller/service/repository layering, async flows, DTOs, middleware-based exception translation, and unit tests.
- [examples/python-api](examples/python-api) shows route/service/data-access separation, typed Pydantic models, explicit request and response contracts, and route-level tests.
- [examples/react-app](examples/react-app) shows typed components, API client separation, a dedicated state hook, explicit loading/error/empty states, and a small test.

These apps exist so the skills and conventions have something concrete to anchor to. They also serve as reference points when Codex needs to infer where new code should go.

## How To Use This Repo With Codex

1. Keep [AGENTS.md](AGENTS.md) small and durable. Do not move detailed workflow logic into it unless the rule truly applies repo-wide.
2. Route recurring work to the relevant skill under [.agents/skills](.agents/skills).
3. Use the conventions docs during implementation and review, especially when deciding whether a new abstraction is justified.
4. Prefer [templates](templates) and [scripts](scripts) when the task is repetitive or deterministic.
5. Use the examples to ground judgments about layering, contracts, testing, and UI state handling.
6. Validate the touched area before declaring the work done.

## What This Repo Does Not Try To Solve

- It does not encode every framework pattern for .NET, Python, or React.
- It does not replace project-specific architecture judgment.
- It does not attempt to define one universal style guide for all teams.
- It does not turn Codex into an autonomous architect that should ignore existing repository patterns.

The repository is strongest when a team wants consistent production-minded defaults without over-specifying every implementation detail.

## Extending The Playbook

When you extend this repository:

- keep `AGENTS.md` small
- add or refine skills for recurring workflows
- add templates only when they remove ambiguity rather than add ceremony
- prefer small example changes over abstract advice
- update conventions only when the repository's engineering stance actually changes
- add validation that is lightweight enough to run routinely

If you add a new domain, follow the same pattern: durable top-level guidance, focused skills, deterministic helpers, and small concrete examples.

## Validation

The repository includes lightweight validation support in [scripts/validate_playbook.py](scripts/validate_playbook.py). During this build, the following checks were run:

- `dotnet test` for the C# example
- `python -m pytest` for the Python example
- `npm.cmd run build` and `npm.cmd run test -- --run` for the React example
- `python scripts/validate_playbook.py` for required paths and internal markdown links

If you adapt the examples or add new skills, rerun the relevant checks rather than relying on the playbook text alone.
