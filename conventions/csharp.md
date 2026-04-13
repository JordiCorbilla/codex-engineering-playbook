# C# Backend Conventions

This playbook favors a layered ASP.NET Core style with explicit request/response models, thin transport handlers, and service-led business logic.

## Default Structure

- `Controllers` or endpoint definitions own HTTP concerns.
- `Services` own business workflows and coordination.
- `Repositories` or data-access implementations own persistence queries and storage behavior.
- `Models` or `Contracts` contain DTOs and request/response shapes.

## Layered Classes

- Controllers should parse input, delegate to a service, and translate results into HTTP responses.
- Services should own business rules, sequencing, authorization checks that depend on application state, and transaction boundaries.
- Repositories should encapsulate EF Core or storage-specific queries.

If a repository abstraction does nothing except forward `DbContext` calls for a trivial feature, skip it. If persistence logic is reused, complex, or likely to vary, the abstraction earns its keep.

## Dependency Injection

- Register services and infrastructure explicitly.
- Depend on interfaces when the boundary matters; do not generate interfaces for every class by habit.
- Constructor injection is the default.

## Async/Await

- Use async end-to-end for IO-bound flows.
- Do not block on `Task.Result` or `.Wait()`.
- Avoid fake async wrappers around purely synchronous work.
- Return `Task` or `Task<T>` from asynchronous APIs; prefer cancellation tokens in application and persistence boundaries when the surrounding code already supports them.

## Exception Handling

- Validate request models before business logic runs.
- Use domain-meaningful exceptions or result objects for expected failures.
- Let unexpected exceptions bubble to centralized middleware or filters.
- Controllers should not contain large try/catch trees unless they are translating one specific failure into one specific contract.

## Validation And DTOs

- Use request/response DTOs at HTTP boundaries.
- Do not expose EF entities directly from controllers.
- Keep validation close to the boundary using data annotations, validators, or explicit service checks.
- Map DTOs to domain or persistence shapes explicitly when it protects boundaries.

## Logging

- Log at service or infrastructure boundaries where the context is meaningful.
- Avoid noisy informational logs for obvious request flow.
- Log unexpected failures once, with identifiers and key business context rather than dumping entire payloads.

## Naming

- One public class per file.
- File names should match class names.
- Use clear suffixes where they add signal: `Controller`, `Service`, `Repository`, `Request`, `Response`.

## Minimal APIs Versus Controllers

Prefer minimal APIs when:

- the service is small
- route organization is straightforward
- endpoint grouping is enough structure

Prefer controllers when:

- the surface area is growing
- filters, versioning, or richer conventions matter
- multiple related endpoints benefit from a stronger organizational unit

Choose one style deliberately. Do not mix patterns randomly.

## Testing

- Unit test service logic with focused dependency seams.
- Add integration tests for controllers or endpoints when routing, model binding, or error translation matters.
- Test async flows as async.
- Cover unhappy paths for validation and known business failures, not only the happy path.
