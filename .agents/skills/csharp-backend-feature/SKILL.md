# csharp-backend-feature

Description: Implement or extend a C# backend feature in a layered ASP.NET Core style with thin controllers, service-led business logic, explicit contracts, and practical validation.

## When To Use

- adding or changing an API endpoint in a C# backend
- implementing service logic, DTOs, repository behavior, or validation in an existing ASP.NET Core codebase
- extending a feature that should preserve controller/service/repository boundaries

See [conventions/architecture.md](../../../conventions/architecture.md) and [conventions/csharp.md](../../../conventions/csharp.md).

## When Not To Use

- reviewing code rather than implementing it
- broad architecture discovery across an unfamiliar repository
- one-off infrastructure changes with no feature-layer implications

## Workflow

1. Inspect the existing project structure, registration patterns, and naming conventions before editing.
2. Locate the transport layer, service layer, and persistence layer for the feature area.
3. Add or update request/response DTOs at the API boundary instead of leaking entities directly.
4. Keep controllers or endpoints thin: validate, delegate, translate the result.
5. Put business rules, orchestration, and workflow sequencing in services.
6. Isolate storage concerns in repositories or data-access code when that boundary already exists or clearly helps.
7. Use async end-to-end for IO-bound paths. Do not introduce sync-over-async behavior.
8. Add or update tests around service behavior, endpoint contracts, and known failure paths where practical.
9. Run the most relevant build and test checks available.

## Expected Outputs

- minimal, coherent code changes in the correct layer
- updated DTOs, services, and persistence code where needed
- targeted tests or validation updates
- a short explanation of key trade-offs if structure changed

## Boundaries

- do not move business logic into controllers
- do not create repository or interface layers by habit when the feature does not need them
- do not expose persistence entities as external contracts unless the codebase already does so intentionally
- keep changes consistent with the surrounding ASP.NET Core style instead of imposing a new pattern
