# layered-architecture-recon

Description: Explore an unfamiliar codebase and map its architecture against this playbook's layering, boundary, and maintainability conventions.

## When To Use

- first-pass exploration of an unfamiliar repository
- mapping entry points, layers, and likely feature boundaries before implementation or review
- identifying where a codebase aligns with or diverges from this playbook

See [conventions/architecture.md](../../../conventions/architecture.md) plus the language-specific convention relevant to the project.

## When Not To Use

- narrow feature implementation once the target area is already clear
- line-by-line code review of a small diff
- single-file tasks that do not need architecture context

## Workflow

1. Find the main entry points, application startup files, and feature directories.
2. Trace representative request or UI flows through handlers, services, and persistence or client layers.
3. Map where domain logic, contracts, and infrastructure concerns currently live.
4. Note boundary violations, layering shortcuts, and areas where the structure is simpler than the playbook on purpose.
5. Summarize the architecture in playbook terms so later feature or review work can route correctly.

## Expected Outputs

- concise architecture map
- identified entry points and major layers
- notable violations, risks, or pragmatic deviations
- suggested starting points for feature or review work

## Boundaries

- do not propose broad rewrites during reconnaissance
- keep the output diagnostic and actionable
- distinguish between intentional simplicity and genuine architectural drift
