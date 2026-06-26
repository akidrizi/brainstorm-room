---
name: improve-codebase-architecture
description: Scans a codebase for deepening opportunities — refactors that turn shallow modules into deep ones — and presents them as ranked candidates, then grills through whichever one is picked. Use when a brainstorm-room Class B problem is structural or architectural, or the user wants to find what's causing friction in a codebase before committing to a redesign.
---

# Improve Codebase Architecture

Source: mattpocock/skills, `engineering/improve-codebase-architecture` — adapted to drop the dependency on a local `codebase-design` skill (not part of brainstorm-room's curated stack; its essential vocabulary is inlined below) and the standalone HTML-report step (replaced with a markdown candidates section, since every brainstorm-room session converges on `plan.md`, not a side artifact).

Surface architectural friction and propose **deepening opportunities**. The aim is testability and navigability, not aesthetics.

## Which codebase

This operates on whatever project the brainstorm is about — which may not be brainstorm-room itself. If it's an external project, make sure it's accessible (open its directory, or `--add-dir` it) before exploring. If you can't get filesystem access, work from what the user pastes in or describes, and say so.

## Vocabulary

Use these terms exactly — don't drift into "component," "service," "API," or "boundary":

- **Module** — anything with an interface and an implementation: a function, class, package, or tier-spanning slice.
- **Interface** — everything a caller must know to use the module correctly: signature, invariants, ordering constraints, error modes, performance characteristics. Broader than the type signature alone.
- **Depth** *(Ousterhout,* A Philosophy of Software Design*)* — leverage at the interface: how much behavior a caller can exercise per unit of interface they learn. **Deep** = small interface, lots of implementation behind it. **Shallow** = interface nearly as complex as the implementation — a near pass-through.
- **Seam** *(Michael Feathers)* — the place where a module's interface lives; where you can alter behavior without editing in that spot.
- **The deletion test.** Imagine deleting the module. If complexity vanishes, it was a pass-through. If complexity reappears across every caller, it was earning its keep — that's the deep-module signal.

## Process

### 1. Explore

Read the project's `CONTEXT.md` (if any — see [domain-modeling](../domain-modeling/SKILL.md)) and any ADRs in the area first, so suggestions use the project's own vocabulary and don't re-litigate settled decisions.

Use the Agent tool with `subagent_type=Explore` to walk the codebase organically — don't follow a rigid checklist. Note where you feel friction:

- Where does understanding one concept require bouncing between many small modules?
- Where is a module shallow — interface nearly as complex as what's behind it?
- Where have pure functions been extracted for testability while the real bugs hide in *how they're called*?
- Where do tightly-coupled modules leak across their seams?
- What's untested, or hard to test through its current interface?

Apply the deletion test to anything suspected shallow.

### 2. Present candidates

Write the candidates directly into the working plan as a `## Architecture candidates` section — not a separate file. For each:

- **Files** — which modules are involved.
- **Problem** — why the current shape causes friction, in deep/shallow terms.
- **Solution** — plain-English description of the change.
- **Benefits** — in terms of leverage (callers) and locality (maintainers) — concentrating change, bugs, and verification in one place instead of spreading them.
- **Recommendation strength** — `Strong`, `Worth exploring`, or `Speculative`.

End with a **Top recommendation** — which candidate to tackle first, and why.

**ADR conflicts.** If a candidate contradicts an existing ADR, surface it only when the friction is real enough to warrant reopening that ADR — name it explicitly ("contradicts ADR-0007 — worth reopening because…"). Don't list every theoretical refactor an ADR already forbids.

Do not design the new interface yet. After presenting candidates, ask: "Which of these would you like to explore?"

### 3. Grilling loop

Once a candidate is picked, run [`grill-me`](../grill-me/SKILL.md) to walk its design tree — constraints, dependencies, the shape of the deepened module, what sits behind the seam, what tests survive.

As decisions crystallize:

- **Naming a deepened module after a concept not yet in `CONTEXT.md`?** Run [`domain-modeling`](../domain-modeling/SKILL.md) to add it.
- **User rejects the candidate for a load-bearing reason?** Offer an ADR via [`adr`](../../frameworks/adr/SKILL.md) — only when a future explorer would actually need the reason to avoid re-suggesting the same thing.
