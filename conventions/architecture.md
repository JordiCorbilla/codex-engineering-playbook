# Architecture Conventions

This playbook assumes production-style application code should be easy to reason about, easy to change, and explicit about where responsibilities live. The goal is not maximal abstraction. The goal is predictable structure.

## Separation Of Concerns

- Entry points handle transport concerns: HTTP parsing, authentication context, status codes, and response shaping.
- Services handle application behavior: orchestration, business rules, transactions, and coordination across dependencies.
- Persistence and infrastructure code handle storage, external APIs, queues, files, and framework-specific mechanics.
- Domain logic belongs in domain-focused types or service modules, not in controllers, routes, repositories, or React render branches.

## Layering

Use a simple directional flow:

`API/UI -> Service/Application -> Domain -> Infrastructure`

- Higher layers may depend on lower layers through explicit interfaces or concrete collaborators when abstraction would be ceremony.
- Lower layers should not reach upward into transport or UI concerns.
- Shared helpers should stay small and focused; do not create a generic utilities layer that becomes a dumping ground.

## Boundary Definitions

- DTOs and request models represent contracts at boundaries.
- Domain models represent business concepts and invariants.
- Persistence models represent storage concerns.
- Do not reuse one model everywhere unless the application is small enough that the distinction adds no value.

Prefer explicit mapping when:

- external contracts are stable and need versioning discipline
- persistence shape differs from API shape
- domain rules require stronger invariants than storage records provide

Prefer fewer model types when:

- the feature is small
- the data shape is genuinely stable across layers
- extra mapping would be noise without adding protection

## API, Service, And Persistence Concerns

- API handlers should validate input, call a service, and translate known failures into contract-level responses.
- Services should own business decisions, workflow sequencing, and transaction boundaries.
- Repositories or data-access modules should encapsulate query details and storage-specific behavior.
- External clients should have clear adapters rather than leaking HTTP or SDK details into business logic.

## DTOs, Models, Domain Logic, And Infrastructure

- DTOs should be versionable, narrow, and safe to expose.
- Domain logic should not depend on controller types, ORM entities, or frontend view models.
- Infrastructure should implement interfaces only when that indirection helps testing, swapping implementations, or keeping boundaries clear.
- Avoid interface-per-class habits when there is only one obvious implementation and no boundary value.

## Testing Philosophy

- Favor tests around behavior and contracts over tests that mirror implementation details.
- Unit test pure or mostly pure business logic when it carries meaningful rules.
- Use integration-style tests for persistence behavior, HTTP contracts, and dependency wiring where failure risk is higher.
- Keep test pyramids pragmatic; a few useful integration tests are better than many brittle mock-heavy unit tests.

## Error Handling Philosophy

- Validate early at boundaries.
- Distinguish expected business failures from unexpected system failures.
- Return explicit error contracts where callers need stable behavior.
- Log unexpected failures with enough context to debug, but avoid double-logging the same exception path.
- Do not hide exceptions with catch-all blocks that downgrade useful failures into vague responses.

## Simplicity Versus Abstraction

Prefer simplicity when:

- one implementation is likely to remain one implementation
- the workflow is straightforward
- abstraction would force more files, naming, and indirection than the feature warrants

Prefer abstraction when:

- the boundary is real and changes independently
- the dependency is expensive to mock or awkward to replace
- multiple features rely on the same variation point

If the code is small, let it stay small. If the code is growing, introduce structure where the pressure is real.
