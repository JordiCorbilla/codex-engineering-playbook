# Python Backend Conventions

This playbook favors explicit service-oriented Python code with typed boundaries, restrained abstraction, and clear separation between request handling, business logic, and IO.

## Default Structure

- Routes or handlers own HTTP concerns.
- Services own business rules and orchestration.
- Data-access modules or repositories own persistence and external system access.
- Schemas or models define request/response contracts.

Not every feature needs every layer, but the responsibilities should still stay distinct.

## Typed Boundaries

- Add type hints to public functions, service methods, and DTO-like models.
- Use typed request/response models where framework support makes that natural.
- Keep internal helper typing practical; do not turn small scripts into annotation exercises.

## Classes Versus Functions

Prefer functions when:

- behavior is stateless
- the workflow is small
- dependency injection would be artificial

Prefer classes when:

- stateful collaborators need to be configured once
- a service coordinates multiple dependencies
- lifecycle or interface boundaries matter

Do not create classes just to mimic enterprise patterns from other languages.

## Exception Handling

- Validate input at the boundary.
- Raise explicit domain or application exceptions for expected business failures.
- Translate expected failures into HTTP responses near the route layer.
- Let unexpected failures surface to centralized error handling so stack traces and logs remain useful.

## Async Usage

- Use async only when the framework and dependencies benefit from it.
- Keep async flows consistent end-to-end for IO-bound paths.
- Do not mix sync and async casually or wrap sync storage calls in async handlers without reason.

## Validation

- Prefer declarative request/response validation where the framework supports it.
- Keep schema validation separate from business-rule validation.
- Use explicit response models for outward-facing contracts when the API matters beyond a toy example.

## Module Organization

- Group by feature or boundary, not by vague technical buckets.
- Keep modules small enough to scan quickly.
- Avoid circular imports by keeping models and contracts in stable locations.
- Shared helpers should stay narrow and justified.

## Testing

- Test service behavior directly where business logic is meaningful.
- Add route-level tests for contract behavior, validation, and error handling.
- Prefer readable fixtures over heavy mocking.
- Cover failure paths that are likely in production: validation failures, missing records, dependency failures, and idempotency concerns where relevant.

## Simplicity And Explicitness

- Prefer straightforward code over clever metaprogramming.
- Avoid hidden control flow, magic registries, and over-generalized base classes.
- Make data movement, validation, and side effects obvious in the code.
