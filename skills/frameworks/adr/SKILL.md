---
name: adr
description: Records an architectural decision as a short, durable Context/Decision/Consequences note, using MADR or Nygard's format. Use whenever a brainstorm-room session reaches a hard-to-reverse, non-obvious decision with a real trade-off, to capture it inline in plan.md, or to write a standalone numbered ADR into a target project's docs/adr/.
---

# ADR — Architectural Decision Records

Sources: [MADR](https://github.com/adr/madr) and Michael Nygard, [*Documenting Architecture Decisions*](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (2011); the offer-sparingly test below is adapted from mattpocock/skills' `domain-modeling`. Full templates: [docs/adr-templates.md](../../../docs/adr-templates.md).

An ADR records *that* a decision was made and *why* — not a design doc, not a spec, not a place to re-litigate things already decided. The value is almost entirely in the Context and the Decision; everything else is optional weight.

## When to offer one

Offer an ADR only when **all three** are true:

1. **Hard to reverse** — the cost of changing your mind later is real.
2. **Surprising without context** — a future reader would look at the outcome and wonder "why on earth did they do it this way?"
3. **The result of a real trade-off** — genuine alternatives existed and one was picked for specific reasons.

If any one is missing, skip it — recording "we did the obvious thing" or something you'll reverse next week isn't worth a durable note. Don't ask the user every time; when it's a clear yes on all three, record it and say you're doing so.

## Format — pick the lightest that fits

Don't default to the heaviest template. See [docs/adr-templates.md](../../../docs/adr-templates.md) for the full text of each.

- **Nygard** (Title, Status, Context, Decision, Consequences) — the default for most brainstorm-room decisions.
- **MADR minimal** (adds Considered Options before the outcome) — reach for this when naming the rejected alternatives matters.
- **MADR full** (adds Decision Drivers, per-option Pros/Cons, Confirmation, frontmatter) — only when there are several stakeholders or several real options each with non-obvious trade-offs worth recording individually.

## Where it lands

**Default — inline in `plan.md`.** Brainstorm-room sessions record decisions inline under a `## Decisions` section in the plan being produced, using the Nygard shape compressed to 1-3 sentences per field:

```md
### {short title}

**Context:** {what's the issue, in 1-2 sentences}
**Decision:** {what we're going with, and why, in 1-2 sentences}
**Consequences:** {what becomes easier or harder — only if non-obvious}
```

Number them locally within the plan (`Decision 1`, `Decision 2`, ...) — this is a one-shot artifact, not a project with its own decision history to maintain.

**Flag low-confidence decisions explicitly.** If a decision is made provisionally — to keep momentum rather than because the alternatives were actually resolved — prefix it with `**Confidence: low —** {why}` so the reader knows to revisit it before treating it as settled.

**Standalone — numbered file in a target project.** If the user is working inside a real project that already has (or wants) a `docs/adr/` directory, write a normal sequential `NNNN-slug.md` file there instead, using MADR or Nygard format directly. Scan `docs/adr/` for the highest existing number and increment.
