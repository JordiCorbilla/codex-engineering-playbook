# React + TypeScript Conventions

This playbook favors React applications that keep rendering code readable, state transitions explicit, and API concerns separate from UI composition.

## Component Structure

- Keep components focused on one level of responsibility.
- Separate page composition, feature widgets, and primitive UI elements when the distinction adds clarity.
- Move non-trivial transformations and side-effectful behavior out of JSX.

Split a component when:

- it handles unrelated concerns
- rendering branches hide the main intent
- state and effects become difficult to reason about

## Hooks Discipline

- Use hooks to model state, effects, and reusable behavior, not to hide ordinary helper functions.
- Keep effects narrowly scoped and driven by real external synchronization.
- Avoid effect chains that simulate imperative workflows.
- Derive UI from props and state where possible instead of copying data into local state.

## State Management

- Start with local component state.
- Lift state to feature or page level when multiple components truly share it.
- Introduce a state library only when server state, caching, or cross-cutting complexity justifies it.
- Keep server state concerns separate from local UI concerns.

## API Client Separation

- Put fetch and serialization logic in API client modules, not directly in components.
- Return typed results from client functions.
- Normalize error handling enough that components can render useful states without parsing transport details.

## Typing Standards

- Type props, async results, and public utility functions explicitly.
- Prefer specific interfaces or type aliases over `any`.
- Keep types close to the code that owns them unless they are true shared contracts.
- Model optionality honestly; do not use non-null assertions to escape design problems.

## Loading, Error, And Empty States

- Every data-driven screen should handle loading, error, and empty states deliberately.
- Keep those states visible in component structure, not hidden behind clever helpers.
- Use clear messaging and stable layout to avoid jarring UI shifts.

## Accessibility

- Use semantic HTML first.
- Label form fields and interactive controls explicitly.
- Keep keyboard interaction and focus behavior intact.
- Communicate errors and status changes in accessible ways.

## UI Consistency

- Reuse patterns for spacing, typography, buttons, and feedback states.
- Keep formatting and naming consistent across components.
- Avoid one-off styling decisions that make similar flows behave differently.

## Form Handling

- Keep simple forms simple.
- Use controlled or library-managed forms deliberately, based on complexity.
- Separate validation rules, submission logic, and rendering enough that each remains readable.

## Avoid Logic-Heavy Rendering

- Compute view models before `return` when branching gets dense.
- Extract subcomponents or helper functions when JSX becomes a place for business logic.
- Keep API calls, retries, and response shaping out of rendering code.
