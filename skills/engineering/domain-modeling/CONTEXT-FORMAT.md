# CONTEXT.md Format

Adapted from mattpocock/skills, `engineering/domain-modeling/CONTEXT-FORMAT.md`. Disclosed reference for [domain-modeling](SKILL.md).

## Structure

```md
# {Context Name}

{One or two sentence description of what this context is and why it exists.}

## Language

**Order**:
{A one or two sentence description of the term}
_Avoid_: Purchase, transaction

**Invoice**:
A request for payment sent to a customer after delivery.
_Avoid_: Bill, payment request
```

## Rules

- **Be opinionated.** When multiple words exist for the same concept, pick the best one and list the others under `_Avoid_`.
- **Keep definitions tight.** One or two sentences max. Define what it IS, not what it does.
- **Only include terms specific to this context.** General programming concepts (timeouts, error types, utility patterns) don't belong even if heavily used. Ask: is this unique to this domain, or a general programming concept? Only the former belongs.
- **Group under subheadings** when natural clusters emerge; a flat list is fine if everything belongs to one cohesive area.

## Single vs multi-context

**Single context (most projects):** one `CONTEXT.md` at the root.

**Multiple contexts:** a `CONTEXT-MAP.md` at the root lists each context, where it lives, and how they relate:

```md
# Context Map

## Contexts

- [Ordering](./src/ordering/CONTEXT.md) — receives and tracks customer orders
- [Billing](./src/billing/CONTEXT.md) — generates invoices and processes payments

## Relationships

- **Ordering → Billing**: Ordering emits `OrderPlaced` events; Billing consumes them to generate invoices
```

Infer which structure applies: `CONTEXT-MAP.md` present → multi-context; only a root `CONTEXT.md` → single context; neither → create a root `CONTEXT.md` lazily when the first term resolves. When multiple contexts exist, infer which one the current topic belongs to; if unclear, ask.
