---
name: design-thinking
description: Runs the UK Design Council's Double Diamond (Discover, Define, Develop, Deliver) to structure divergent-then-convergent thinking on an exploratory problem. Use to drive brainstorm-room Class B sessions — architecture, scaling, connectivity, debugging, new-solution ideation — once grill-me has sharpened the problem, or whenever the user wants the solution space explored rather than jumping straight to one answer.
---

# Design Thinking — the Double Diamond

Source: UK Design Council, [*Framework for Innovation*](https://www.designcouncil.org.uk/resources/framework-for-innovation/). Full reference: [docs/design-thinking.md](../../../docs/design-thinking.md).

Two diamonds, back to back: diverge then converge on the *problem* (Discover → Define), then diverge then converge on the *solution* (Develop → Deliver). The model's value is forcing the widen-before-narrow discipline on both halves — skipping straight to Develop is the default failure mode and looks efficient right up until it answers the wrong question.

## The four phases

Run these in order. Don't skip Discover/Define because the problem "seems obvious" — that's exactly the case design-thinking exists to catch.

1. **Discover** — Understand the problem rather than assume it. This phase should already be mostly done by the time `design-thinking` runs, since [`grill-me`](../../engineering/grill-me/SKILL.md) is how brainstorm-room executes Discover in a chat medium (no field research to send anyone on). If grill-me hasn't run yet, run it first.
   - *Done when:* the real constraints, stakeholders, and non-negotiables are named — not assumed.
2. **Define** — Reframe the challenge using what Discover surfaced. State the problem as a single sentence the user explicitly confirms, not the framing they walked in with.
   - *Done when:* the user has agreed, in their own words, that this is the actual problem.
3. **Develop** — Generate multiple candidate solutions, genuinely different from each other (not variations on one idea). Pull in a structural or operational lens here if the problem calls for it:
   - Operational, scaling, reliability shape → apply [`sre-lens`](../sre-lens/SKILL.md).
   - Structural / architectural shape → apply [`domain-modeling`](../../engineering/domain-modeling/SKILL.md) and/or [`improve-codebase-architecture`](../../engineering/improve-codebase-architecture/SKILL.md).
   - *Done when:* at least two or three candidates exist that differ in approach, not just in detail.
4. **Deliver** — Test candidates against the Define statement, reject what doesn't hold up, and converge on one. State *why* the winner won.
   - *Done when:* one candidate is selected with a stated reason, ready to write into `plan.md`.

## The four principles

Apply throughout, not as a fifth phase:

- **Put people first.** Start from who uses or is affected by the outcome, not from a favorite solution.
- **Communicate visually and inclusively.** A diagram or table that makes the shared understanding checkable beats another paragraph.
- **Collaborate and co-create.** Treat the user as a co-designer, not a requirements source — ask, don't assume.
- **Iterate, iterate, iterate.** Treat the diamond as a loop you can re-enter, not a line you walk once. If Deliver reveals the Define statement was wrong, go back.

## Handoff

When a Deliver choice is hard to reverse, surprising without context, and the result of a real trade-off, offer an ADR via [`adr`](../adr/SKILL.md) — don't record every choice, only the load-bearing ones. The chosen candidate and its rationale are what `plan.md` is built from.
