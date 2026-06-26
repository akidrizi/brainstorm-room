---
name: to-issues
description: Breaks a finished plan into independently-grabbable issues using tracer-bullet vertical slices, written into plan.md by default or published to a connected issue tracker on request. Use when the user wants a plan broken into tickets, tasks, or issues — typically after plan.md already exists.
---

# To Issues

Source: mattpocock/skills, `engineering/to-issues` — adapted to write into `plan.md` by default instead of requiring an issue-tracker integration, since brainstorm-room's export contract is plan.md, not a connected tracker.

Break a plan into independently-grabbable issues using **tracer bullets**: vertical slices, not horizontal layers.

## Process

### 1. Gather context

Work from the plan already in the conversation, or read `plan.md` if pointed at one.

### 2. Explore the codebase (optional)

If the target project is accessible, explore it to ground issue descriptions in its real domain vocabulary (`CONTEXT.md`, if any) and respect existing ADRs. Look for prefactoring opportunities — "make the change easy, then make the easy change."

### 3. Draft vertical slices

Each issue is a thin slice that cuts through every integration layer end-to-end (schema, API, UI, tests) — not one layer split across many issues.

- Each slice is independently demoable or verifiable.
- Any prefactoring becomes its own first slice.

### 4. Quiz the user

Present the breakdown as a numbered list. For each slice: **Title**, **Blocked by** (which other slices, if any), **Covers** (which part of the plan it addresses). Ask whether the granularity is right, whether dependencies are correct, and whether anything should merge or split. Iterate until approved.

### 5. Write the issues

**Default — append to `plan.md`.** Add a `## Issues` section with one entry per approved slice, in dependency order:

```md
### {N}. {Title}

**What to build:** {end-to-end behavior, not layer-by-layer implementation}

**Acceptance criteria:**
- [ ] {criterion}

**Blocked by:** {issue N, or "None — can start immediately"}
```

Avoid specific file paths or code snippets that go stale fast — except a snippet from an earlier prototype that encodes a decision more precisely than prose can (a state machine, a schema shape); trim it to the decision-rich part.

**On request — publish to a connected tracker.** If the user has a real issue tracker available for the target project (e.g. `gh` is authenticated against it) and asks to publish, create one issue per slice there instead, in dependency order so later issues can reference real identifiers in "Blocked by." Don't publish unprompted — `plan.md` is the default, durable artifact.
