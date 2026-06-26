# brainstorm-room orchestration

This file governs how a brainstorm-room session runs. It is the **only** orchestration file in this repo — there is no second `CLAUDE.md` at the root. `skills/` below is the machinery this file drives; `dist/` is where every session's output lands. Never write into `skills/` during a normal session — only `meta/skill-forge` and a human editing the stack do that.

## 1. Classify

Every session opens by deciding which problem class this is:

- **Class A — formatted-document skill.** The user already knows the shape of the desired *output* — a document in a fixed template — and wants it produced consistently from structured input. The session's deliverable is a skill that produces the document, not the document itself.
- **Class B — exploratory.** The user is still figuring out what the right answer even is: architecture, scaling, connectivity, debugging, new-solution ideation. The deliverable is `plan.md`; a skill is optional and only if the thinking generalizes.

If it's genuinely ambiguous after a glance, ask directly: "Are we designing a repeatable document template, or exploring an open problem?" Classification can be revised once grilling reveals more — don't force an early guess to stick.

## 2. Grill

Run [`engineering/grill-me`](../skills/engineering/grill-me/SKILL.md) before anything else, regardless of class. Don't proceed to a lens until the problem is sharp: a one-paragraph restatement the user has explicitly confirmed, with no constraints left unstated.

Once the problem is sharp, derive `<problem-name>` as its kebab-case slug and create `dist/<problem-name>/plan.md` with just the `## Problem` section filled in (template in §5). Writing it now, not at the end, means nothing is lost if the session runs long.

## 3. Apply the right lens

**Class A** → clarify three things, then go straight to step 4 (skip Design Thinking, SRE lens, domain-modeling — they're for open problems, not fixed templates):

- The **input contract** — what structured input the future skill will receive.
- The **target template** — the exact shape of the document it must produce.
- The **invariants** — what must always hold true of the output, no matter the input.

**Class B** → run [`frameworks/design-thinking`](../skills/frameworks/design-thinking/SKILL.md) (Discover/Define/Develop/Deliver) as the spine of the session. Inside Develop, reach for additional lenses only when the problem's shape calls for them:

- Operational, scaling, reliability shape → [`frameworks/sre-lens`](../skills/frameworks/sre-lens/SKILL.md).
- Structural, architectural shape → [`engineering/domain-modeling`](../skills/engineering/domain-modeling/SKILL.md) and/or [`engineering/improve-codebase-architecture`](../skills/engineering/improve-codebase-architecture/SKILL.md).

These aren't mutually exclusive — a scaling problem can also be structural. Apply as many as the problem's shape actually calls for, and none it doesn't.

## 4. Record decisions

Whenever a decision is hard to reverse, surprising without context, and the result of a real trade-off — all three — record it via [`frameworks/adr`](../skills/frameworks/adr/SKILL.md) inline in `plan.md`'s `## Decisions` section. Flag provisional ones with `**Confidence: low —** {why}`. Most small choices fail at least one of the three tests; don't record those.

## 5. Produce `plan.md`

Keep `dist/<problem-name>/plan.md` current as the session proceeds rather than writing it all at the end:

```md
# {Problem title}

## Problem
{The confirmed, sharp problem statement from grilling.}

## Class
Class A — document skill | Class B — exploratory

## Approach
{Class A: the input contract, target template, and invariants from step 3.}
{Class B: which lens(es) were applied and why.}

## Decisions
{Inline ADRs from step 4 — Context / Decision / Consequences. Low-confidence ones flagged.}

## Plan
{The concrete, actionable plan — what to actually do, in enough detail to act on without this conversation.}
```

The plan must stand alone: usable by pasting into any project, with no dependency on the skill below even existing.

## 6. Ask about a skill

Once `plan.md` is complete, ask explicitly: **"Generate a skill from this?"**

- **No** → done. Export is just `plan.md`.
- **Yes** → run [`meta/skill-forge`](../skills/meta/skill-forge/SKILL.md), which writes `dist/<problem-name>/<skill-name>/SKILL.md` (and any bundled files) and validates it against the Anthropic spec before calling it done.

For Class A sessions, the answer is usually yes by construction — the whole session was scoped around producing a skill — but still ask; don't assume.

## 7. Export

Final state for every session:

```
dist/<problem-name>/
├── plan.md                 # always
└── <skill-name>/            # only if step 6 was a yes
    └── SKILL.md
```

## Skill index

| Skill | Invoked |
|---|---|
| [`engineering/grill-me`](../skills/engineering/grill-me/SKILL.md) | Always, first, after classification. |
| [`frameworks/design-thinking`](../skills/frameworks/design-thinking/SKILL.md) | Class B sessions, as the main spine. |
| [`frameworks/sre-lens`](../skills/frameworks/sre-lens/SKILL.md) | Class B, inside Develop, only if the problem is operational/scaling/reliability-shaped. |
| [`engineering/domain-modeling`](../skills/engineering/domain-modeling/SKILL.md) | Class B, inside Develop, only if the problem is structural — also whenever terminology needs sharpening, in either class. |
| [`engineering/improve-codebase-architecture`](../skills/engineering/improve-codebase-architecture/SKILL.md) | Class B, inside Develop, only if the problem is about an existing codebase's structure. |
| [`frameworks/adr`](../skills/frameworks/adr/SKILL.md) | Whenever a decision passes the three-part test in step 4. |
| [`meta/skill-forge`](../skills/meta/skill-forge/SKILL.md) | Step 6, only on explicit "yes." |
| [`engineering/to-issues`](../skills/engineering/to-issues/SKILL.md) | **Not** part of the automatic flow. On request only, after `plan.md` exists, when the user wants it broken into tickets. |

## Standing constraints

- `skills/` (machinery) and `dist/` (output) never overlap. Nothing a session produces belongs in `skills/`.
- A session can end at `plan.md` — skill generation is always opt-in, never automatic.
- If the curated skill stack itself is ever extended, adapt from a real, cited source. Don't invent a skill's content from scratch.
