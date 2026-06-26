---
name: domain-modeling
description: Builds and sharpens a project's domain glossary during design — challenging vague terms, inventing edge cases, writing CONTEXT.md down the moment a term crystallises. Use when a brainstorm-room Class B problem is structural, when the user's terminology is fuzzy or conflicts with an existing glossary, or when another brainstorm-room skill needs the domain model kept current.
---

# Domain Modeling

Source: mattpocock/skills, `engineering/domain-modeling` (adapted — ADR format delegated to brainstorm-room's own [`adr`](../../frameworks/adr/SKILL.md) skill instead of a duplicate local format).

This is the *active* discipline of building the model — challenging terms, inventing edge-case scenarios, writing the glossary down the moment it crystallizes. Merely reading an existing `CONTEXT.md` for vocabulary is not this skill; that's a one-line habit any skill can do. Reach for this when the model is actually changing.

## Which project's glossary

This operates on whatever project the brainstorm is about. If that's an external project, make sure it's accessible (open its directory, or `--add-dir` it) before reading or writing `CONTEXT.md`. If the brainstorm is pure greenfield with no repo yet, keep the glossary in conversation and fold it into `plan.md`'s vocabulary section — let `CONTEXT.md` materialize later, once there's an actual repo to put it in.

## File structure

Most projects have a single context: a root `CONTEXT.md`. If a `CONTEXT-MAP.md` exists at the root instead, the project has multiple contexts, and the map points to where each one's own `CONTEXT.md` lives (e.g. `src/ordering/CONTEXT.md`). Infer which applies; if neither exists, create a root `CONTEXT.md` lazily, only once the first term is resolved. See [CONTEXT-FORMAT.md](CONTEXT-FORMAT.md) for the exact structure and the multi-context map format.

## During the session

- **Challenge against the glossary.** When the user's term conflicts with `CONTEXT.md`, call it out immediately: "Your glossary defines 'cancellation' as X, but you mean Y here — which is it?"
- **Sharpen fuzzy language.** When a term is vague or overloaded, propose a precise canonical one: "You're saying 'account' — do you mean the Customer or the User? Those are different things."
- **Stress-test with scenarios.** Invent concrete edge cases that force precision about where one concept's boundary ends and another's begins.
- **Cross-reference with code.** If the user's description of behavior and the actual code disagree, surface the contradiction rather than silently picking one.
- **Update `CONTEXT.md` inline, the moment a term resolves.** Don't batch edits for later — capture them as they happen.

`CONTEXT.md` is a glossary and nothing else — never a spec, a scratchpad, or a place for implementation decisions.

## Offering an ADR

When the modeling surfaces a decision that is hard to reverse, surprising without context, *and* the result of a real trade-off — all three — offer to record it via [`adr`](../../frameworks/adr/SKILL.md). Most terminology choices are none of these; don't offer reflexively.
