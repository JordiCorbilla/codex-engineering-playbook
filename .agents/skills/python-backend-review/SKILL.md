# python-backend-review

Description: Review Python backend changes for module boundaries, typing discipline, exception handling, clarity, and overengineering risk.

## When To Use

- reviewing Python backend diffs
- checking service-oriented structure in API code
- looking for validation, typing, and exception-flow issues

See [conventions/architecture.md](../../../conventions/architecture.md) and [conventions/python.md](../../../conventions/python.md).

## When Not To Use

- implementing features
- reviewing C# or frontend work
- broad architectural mapping before the feature boundaries are known

## Workflow

1. Inspect touched modules and reconstruct the route-to-service-to-IO path.
2. Look for mixed responsibilities, unclear ownership, or hidden side effects.
3. Check public function signatures and models for missing or weak typing.
4. Review validation placement and error translation at boundary points.
5. Identify unnecessary classes, abstract base layers, or framework-heavy patterns that add ceremony.
6. Check tests for meaningful coverage of business rules and contract failures.
7. Produce a concise review summary with practical findings.

## Expected Outputs

- concise findings with severity or importance implied by ordering
- short explanation of why a pattern is risky or overbuilt
- explicit note when the diff is structurally sound

## Boundaries

- avoid generic style commentary
- do not insist on more layers unless the code already shows the pressure for them
- keep feedback anchored to maintainability, correctness, and production failure modes
