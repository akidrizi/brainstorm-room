# brainstorm-room

A reusable thinking environment for software problems. Open this repo, brainstorm inside it, walk out with a plan, and sometimes with a reusable Claude Code skill.

Think of it as a factory: the repo is the machine, [`dist/`](dist/) is the warehouse of finished products, and [`skills/`](skills/) is the tooling on the factory floor. Nothing in `skills/` is ever a finished product, and nothing in `dist/` is ever tooling — the two never mix.

## Two kinds of problem

**Class A — formatted-document skills (deterministic).** You already know the shape of the output; you want it produced the same way every time. *Example: a skill that generates arc42 architecture documents in your company's house style from a structured brief.* The session's deliverable is a skill that produces the document — not the document itself.

**Class B — exploratory problem-solving.** You don't yet know what the right answer is. Architecture, scaling, connectivity, debugging, new-solution ideation. *Example: "should this service split into two, and if so, along which seam?"* The deliverable is a `plan.md`. If the thinking generalizes, you can ask for a skill on top of it — but a session can end at the plan, every time.

## Starting a session

Open Claude Code in this repo and describe the problem. [`.claude/CLAUDE.md`](.claude/CLAUDE.md) takes it from there: classifies which class you're in, interrogates the request until it's sharp, applies the right thinking framework, and writes a plan as it goes — not just at the end. See that file for the exact flow if you want the mechanics.

## Where things land

```
dist/<problem-name>/
├── plan.md            # always produced
└── <skill-name>/       # only if you ask for a skill
    └── SKILL.md
```

- **`plan.md`** stands alone. Paste it into any project; it doesn't need the skill to make sense.
- **A generated skill** also stands alone. Copy its folder into any project's `.claude/skills/` and it's invocable there, independent of brainstorm-room.

You're asked explicitly — "Generate a skill from this?" — before one is ever produced. It's never automatic.

## The skill stack

`skills/` holds the frameworks and engineering practices brainstorm-room thinks with. Each is adapted from a cited source, not invented from scratch.

| Skill | Contributes |
|---|---|
| `frameworks/design-thinking` | The Double Diamond (Discover → Define → Develop → Deliver) — structures divergent/convergent thinking, drives every Class B session. |
| `frameworks/adr` | Records *why* a decision was made — Context / Decision / Consequences — feeding every plan. |
| `frameworks/sre-lens` | SLOs, error budgets, toil, blameless postmortems — the operational lens for scaling/reliability problems. |
| `engineering/grill-me` | Interrogates assumptions and surfaces blind spots before any planning starts. |
| `engineering/improve-codebase-architecture` | Finds and ranks architectural friction in an existing codebase. |
| `engineering/domain-modeling` | Builds and sharpens the domain glossary before the solution gets designed. |
| `engineering/to-issues` | Breaks a finished plan into vertical-slice tickets, on request. |
| `meta/skill-forge` | Converts a brainstorm into a valid, reusable `SKILL.md` — the skill that generates skills. |

## Citations

| Skill | Source(s) |
|---|---|
| `frameworks/design-thinking` | UK Design Council, [*Framework for Innovation*](https://www.designcouncil.org.uk/resources/framework-for-innovation/) |
| `frameworks/adr` | [MADR](https://github.com/adr/madr); Michael Nygard, [*Documenting Architecture Decisions*](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (2011) |
| `frameworks/sre-lens` | Google, [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/) and the [*SRE Workbook*](https://sre.google/workbook/table-of-contents/) |
| `engineering/grill-me` | [mattpocock/skills](https://github.com/mattpocock/skills), `productivity/grilling` + `productivity/grill-me` (merged into one) |
| `engineering/improve-codebase-architecture` | [mattpocock/skills](https://github.com/mattpocock/skills), `engineering/improve-codebase-architecture` |
| `engineering/domain-modeling` | [mattpocock/skills](https://github.com/mattpocock/skills), `engineering/domain-modeling` |
| `engineering/to-issues` | [mattpocock/skills](https://github.com/mattpocock/skills), `engineering/to-issues` |
| `meta/skill-forge` | Anthropic's [Agent Skills spec](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) and [authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices); [mattpocock/skills](https://github.com/mattpocock/skills), `productivity/writing-great-skills` |

None of the above is copied verbatim — each `SKILL.md`'s own header explains exactly what was adapted and why. Full adaptation notes live there and in [`docs/`](docs/).
