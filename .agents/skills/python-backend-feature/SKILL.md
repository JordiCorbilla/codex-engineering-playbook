# python-backend-feature

Description: Implement or extend a Python backend feature with thin request handling, explicit service logic, typed boundaries, and restrained abstraction.

## When To Use

- adding API behavior in a Python backend
- extending service logic, schemas, validation, or data-access modules
- refining a Python backend toward a clearer service-oriented structure

See [conventions/architecture.md](../../../conventions/architecture.md) and [conventions/python.md](../../../conventions/python.md).

## When Not To Use

- reviewing Python changes rather than implementing them
- frontend work
- large repository reconnaissance where the structure is not yet understood

## Workflow

1. Inspect the existing route, service, schema, and data-access layout before changing anything.
2. Keep request handling thin: parse input, call a service, translate expected failures.
3. Put business rules in service functions or classes, depending on the existing dependency shape.
4. Keep IO concerns in repository, data-access, or client modules rather than mixing them into route handlers.
5. Add or refine typed request/response models and explicit function signatures.
6. Use async only when the framework and dependencies justify it.
7. Add or update tests for route contracts, service behavior, and known failure paths where practical.
8. Explain any trade-off where simplicity won over a heavier abstraction, or the reverse.

## Expected Outputs

- feature code placed in the correct boundary
- updated models, services, and tests where needed
- explicit typing at public module boundaries
- short trade-off notes when structure changes matter

## Boundaries

- do not introduce classes when plain functions are clearer
- do not mix transport, business logic, and persistence in one module without a clear reason
- avoid clever framework usage that hides control flow or validation behavior
