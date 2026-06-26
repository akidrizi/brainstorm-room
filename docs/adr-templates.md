# Architectural Decision Records — templates

**Sources:**
- MADR — [`github.com/adr/madr`](https://github.com/adr/madr), `template/adr-template.md` and `template/adr-template-minimal.md` (MIT/CC0 dual-licensed, designed for reuse).
- Michael Nygard, [*Documenting Architecture Decisions*](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (2011) — the original ADR format: Title, Status, Context, Decision, Consequences.

Disclosed reference for [`skills/frameworks/adr`](../skills/frameworks/adr/SKILL.md).

An ADR records *that* a decision was made and *why* — not a design doc, not a spec. Three formats below, ordered by weight. Pick the lightest one that captures the decision; don't default to the heaviest.

## Nygard (lightest, five fields)

The original 2011 format. Five sections, no frontmatter:

```md
# {short title}

## Status
{proposed | accepted | superseded by ADR-NNNN}

## Context
{What is the issue we're seeing that motivates this decision?}

## Decision
{What is the change we're actually proposing or have agreed to?}

## Consequences
{What becomes easier or harder as a result of this change?}
```

## MADR minimal

`adr-template-minimal.md` — adds Considered Options between Context and Decision, drops Status as its own section:

```md
# {short title, representative of solved problem and found solution}

## Context and Problem Statement

{Describe the context and problem statement, e.g., in free form using two to
three sentences or in the form of an illustrative story. You may want to
articulate the problem in form of a question.}

## Considered Options

* {title of option 1}
* {title of option 2}
* {title of option 3}

## Decision Outcome

Chosen option: "{title of option 1}", because {justification}.

### Consequences

* Good, because {positive consequence}
* Bad, because {negative consequence}
```

## MADR full

`adr-template.md` — adds YAML frontmatter (status/date/decision-makers/consulted/informed), Decision Drivers, per-option Pros and Cons, Confirmation, and More Information. Every section below Context and Problem Statement / Decision Outcome is explicitly optional in the source template — MADR's own convention is "feel free to remove":

```md
---
status: "{proposed | rejected | accepted | deprecated | … | superseded by ADR-0123}"
date: {YYYY-MM-DD when the decision was last updated}
decision-makers: {list everyone involved in the decision}
consulted: {list everyone whose opinions are sought; two-way communication}
informed: {list everyone kept up to date; one-way communication}
---

# {short title, representative of solved problem and found solution}

## Context and Problem Statement

{Free-form, two to three sentences, or an illustrative story. Make the scope
of the decision explicit.}

## Decision Drivers

* {decision driver 1, e.g. a desired quality, constraint, or force}
* {decision driver 2}

## Considered Options

* {title of option 1}
* {title of option 2}

## Decision Outcome

Chosen option: "{title of option 1}", because {justification — e.g. only
option that meets a k.o. criterion, or comes out best on balance}.

### Consequences

* Good, because {positive consequence}
* Bad, because {negative consequence}

### Confirmation

{How will compliance be confirmed? A design/code review, an architecture
fitness function, a test?}

## Pros and Cons of the Options

### {title of option 1}

* Good, because {argument a}
* Neutral, because {argument b}
* Bad, because {argument c}

## More Information

{Additional evidence, team agreement, or when/how this decision should be
revisited.}
```

## Which one to reach for

| Situation | Template |
|---|---|
| Quick, low-ceremony decision; one obvious alternative | Nygard |
| Real alternatives worth naming, but the trade-off is simple | MADR minimal |
| Multiple stakeholders, multiple options each with real pros/cons, or compliance needs to be checkable later | MADR full |

`status` and `decision-makers` frontmatter only earns its place when decisions are actually revisited or contested later — most brainstorm-room ADRs are accepted-on-write and never revisit, so skip the frontmatter by default and add it only when the session's discussion shows the decision is genuinely live (e.g., explicitly "proposed" pending someone else's sign-off).

## Numbering and location

ADRs are sequential: `0001-slug.md`, `0002-slug.md`, … in a `docs/adr/` directory. Scan for the highest existing number and increment. Create the directory lazily — only when the first ADR is needed.
