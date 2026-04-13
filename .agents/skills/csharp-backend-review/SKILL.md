# csharp-backend-review

Description: Review C# backend changes for layering, async correctness, contract discipline, error handling, and maintainability.

## When To Use

- reviewing a C# backend diff or pull request
- checking whether new code respects controller/service/repository boundaries
- looking for correctness and maintainability risks in ASP.NET Core feature work

See [conventions/architecture.md](../../../conventions/architecture.md) and [conventions/csharp.md](../../../conventions/csharp.md).

## When Not To Use

- implementing a feature
- reviewing frontend-specific UX or React component work
- deep repository mapping where architecture is still unknown

## Workflow

1. Inspect the touched files and identify the request path through controller, service, and persistence layers.
2. Check for fat controllers, misplaced orchestration, or infrastructure details leaking upward.
3. Review async usage for blocking calls, missing awaits, and inconsistent cancellation or error flow.
4. Inspect DTO, entity, and model boundaries for leakage or accidental coupling.
5. Check validation placement, exception handling strategy, and logging behavior.
6. Note missing or weak tests around business failures, contracts, or persistence behavior.
7. Produce a concise review summary ordered by severity.

## Expected Outputs

- findings with severity and confidence
- file-level references where possible
- explicit statement when no major findings are present
- short residual-risk note about testing or contract exposure

## Boundaries

- focus on real risks, not style trivia
- do not recommend extra abstractions without a concrete maintenance benefit
- keep the summary concise and review-oriented rather than rewriting the feature plan
