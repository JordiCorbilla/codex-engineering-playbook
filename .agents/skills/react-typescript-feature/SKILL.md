# react-typescript-feature

Description: Implement or extend a React + TypeScript feature with focused components, explicit types, separated API access, and deliberate UI state handling.

## When To Use

- adding or changing a React + TypeScript feature
- building pages, components, hooks, or client-side API integrations
- improving frontend code structure while preserving established UI patterns

See [conventions/react-typescript.md](../../../conventions/react-typescript.md) and [conventions/architecture.md](../../../conventions/architecture.md).

## When Not To Use

- pure UX polish without feature or structure work
- backend-only changes
- review-only tasks

## Workflow

1. Inspect the existing component tree, API client layout, and styling conventions.
2. Decide where the feature belongs: page, feature component, shared component, hook, or API client.
3. Keep transport concerns in API modules and rendering concerns in components.
4. Type props, client responses, and local state explicitly.
5. Handle loading, error, and empty states deliberately in the UI flow.
6. Keep rendering code readable by moving heavy logic out of JSX.
7. Preserve accessibility, keyboard behavior, and visual consistency with the existing app.
8. Add or update tests where the repo already supports them or where the behavior is easy to validate.

## Expected Outputs

- focused component and API client changes
- explicit state and typing updates
- deliberate empty, loading, and error handling
- concise explanation of any component split or state-management trade-off

## Boundaries

- do not fetch directly inside deeply nested presentation components unless the app already centers that pattern
- do not hide complex business logic inside render branches or effects
- do not add a state-management library for a local problem
