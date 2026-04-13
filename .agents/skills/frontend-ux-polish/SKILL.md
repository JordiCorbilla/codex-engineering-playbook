# frontend-ux-polish

Description: Improve frontend quality beyond raw functionality by tightening information hierarchy, interaction clarity, state handling, and consistency without redesigning the entire product.

## When To Use

- polishing an existing React or web UI after the core feature works
- improving spacing, labels, empty states, loading behavior, affordances, and visual coherence
- making pragmatic UX improvements that should stay aligned with the current design language

See [conventions/react-typescript.md](../../../conventions/react-typescript.md).

## When Not To Use

- initial feature implementation where structure is the primary problem
- full visual redesign requests
- backend or API-only changes

## Workflow

1. Inspect the current screen or component states, especially loading, error, and empty paths.
2. Identify friction in hierarchy, labels, affordances, spacing, and interaction feedback.
3. Improve clarity before adding decoration.
4. Preserve established UI patterns unless inconsistency is the problem itself.
5. Keep accessibility intact while refining wording, control grouping, and visual emphasis.
6. Explain the practical reason for each notable polish change in UX terms.

## Expected Outputs

- improved labels, layout, affordances, and state handling
- minimal code changes with visible UX impact
- short explanation tied to usability, not aesthetics alone

## Boundaries

- avoid gratuitous animation or complexity
- do not introduce a new design system for a local polish task
- do not re-architect data flow unless the UX problem clearly comes from state structure
