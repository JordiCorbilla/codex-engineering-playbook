# api-contract-review

Description: Review backend and frontend contract changes for DTO shape integrity, client/server alignment, error semantics, and breaking-change risk.

## When To Use

- request or response shapes changed across backend and frontend
- reviewing DTOs, API client code, validation models, or error contracts
- checking for mismatches and compatibility risks during refactors

See [conventions/architecture.md](../../../conventions/architecture.md), [conventions/csharp.md](../../../conventions/csharp.md), [conventions/python.md](../../../conventions/python.md), and [conventions/react-typescript.md](../../../conventions/react-typescript.md).

## When Not To Use

- purely internal refactors with no contract impact
- single-layer review where transport contracts are unchanged
- UX-only review work

## Workflow

1. Inspect request and response DTOs, schema models, and API client usage.
2. Compare field names, nullability, enum or literal assumptions, and collection shapes across both sides.
3. Review validation behavior and error response shapes for stability and caller expectations.
4. Identify implicit migrations, default-value assumptions, and backward-compatibility risks.
5. Highlight breaking changes, silent behavior changes, and versioning concerns.
6. Summarize the contract risk in concise review language.

## Expected Outputs

- clear contract mismatches or confirmation that contracts align
- notes on breaking changes, migration needs, or rollout risk
- emphasis on caller-visible behavior, not just type shape

## Boundaries

- focus on contract integrity rather than full feature quality
- do not recommend speculative versioning complexity unless the compatibility risk is real
