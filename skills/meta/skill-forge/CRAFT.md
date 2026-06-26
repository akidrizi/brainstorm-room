# Craft — sharpening a skill beyond bare validity

Condensed from mattpocock/skills' `productivity/writing-great-skills` and its `GLOSSARY.md` (full source has the complete vocabulary; this is the actionable subset). Disclosed reference for [SKILL.md](SKILL.md) — read this when a draft passes validation but still feels bloated, vague, or unreliable.

## The root virtue: predictability

A skill exists to make the agent take the same *process* every run — not produce the same output. A brainstorming skill should predictably diverge: its tokens vary, its behavior doesn't. Every lever below serves this one thing.

## The information hierarchy

Rank content by how immediately it's needed, and push everything else down:

1. **Steps** — the ordered actions in `SKILL.md` itself. The primary tier.
2. **In-file reference** — definitions and rules consulted on demand, still in `SKILL.md`.
3. **Disclosed reference** — a separate file (like this one), reached by a link, loaded only when the link fires.

Inline what every run needs; disclose what only some runs reach. A skill with no steps (pure reference) still has this hierarchy — it just uses rungs 2 and 3.

## Completion criteria

Every step should end on a condition the agent can check against, not a feeling. Two properties make a criterion strong:

- **Checkable** — can the agent actually tell done from not-done, or is it a vibe ("understanding reached")?
- **Exhaustive**, where it matters — "every modified field accounted for" forces real legwork; "produce a change list" doesn't.

A vague criterion invites **premature completion**: the agent's attention slips to *being done* rather than to the work, especially when it can see the steps still ahead. Fix the criterion first — it's cheap and local. Only split the skill into a hand-off (hiding the later steps) if sharpening the criterion doesn't fix it.

## Leading words

A leading word is a compact, already-pretrained concept the agent thinks with — *tracer bullet*, *deep module*, *blameless* — repeated as a token, not re-explained as a sentence each time. It does double duty: in the body it anchors consistent execution; in the description it anchors reliable triggering, especially when the same word also lives in the user's own vocabulary for the problem. Coining a new one works only if you define it once, clearly — a pretrained word is free; a made-up one costs definition tokens. Reach for an existing word before inventing one.

## Failure modes to hunt for in a draft

- **Duplication** — the same meaning stated in two places. Costs maintenance and inflates that meaning's apparent importance. Keep one source of truth; link to it instead of restating it.
- **Sprawl** — the skill is simply too long, even if every line is live and unique. Cure: push reference down the hierarchy, split by branch.
- **Sediment** — stale layers nobody removes because adding feels safe and removing feels risky. Cure: when editing, actively ask whether each existing line still bears on what the skill does.
- **No-op** — an instruction that changes nothing because the model already does it by default ("be thorough"). The test: does this line change behavior versus the default? If not, delete it or replace it with a real leading word ("be *relentless*").

## Degrees of freedom

Match instruction specificity to how fragile the task is:

- **High freedom** (prose, heuristics) — when multiple approaches are valid and judgment matters. Most Class B forged skills.
- **Medium freedom** (a template with parameters) — when a preferred pattern exists but some variation is fine.
- **Low freedom** (an exact template or script, no room to improvise) — when consistency is the whole point and deviation is a bug, not a feature. Every Class A forged skill.
