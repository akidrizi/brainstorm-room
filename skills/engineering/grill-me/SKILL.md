---
name: grill-me
description: Interrogates a request relentlessly, one question at a time, to surface real constraints and kill ambiguity before any planning happens. Use at the start of every brainstorm-room session, right after classifying the problem, and again whenever a candidate solution needs stress-testing before it's locked in.
---

# Grill Me

Source: mattpocock/skills, `productivity/grilling` + `productivity/grill-me` — merged into one skill here since brainstorm-room has no separate model-invoked/user-invoked split to preserve; both invocation surfaces collapse into this one.

Interview relentlessly about whatever is currently on the table — the raw request if nothing else exists yet, or a specific candidate solution once Develop has produced one. Walk down each branch of the problem, resolving dependencies between answers one by one. The goal is a problem statement sharp enough that no two people would describe it differently.

## Rules

- **One question at a time.** Wait for the answer before asking the next. Asking several at once is bewildering and the answers bleed into each other.
- **Always propose your own recommended answer** alongside the question — don't just ask open-ended; give the user something to react to or correct.
- **Explore before asking.** If a question can be answered by reading the codebase, the repo, or material already in context, do that instead of asking the user. Only ask what you genuinely can't discover yourself.
- **Chase the branch.** When an answer reveals a new ambiguity, follow it immediately rather than queuing it — depth over breadth.

## Done when

You can restate the problem back to the user in a single paragraph, and they confirm it's accurate with no additions. If they add a new constraint after hearing your restatement, you're not done — fold it in and restate again.
