---
name: skill-forge
description: Converts a finished brainstorm-room session into a valid, reusable SKILL.md — a low-freedom template-filler for Class A document skills, or a high-freedom heuristic-capturer for an opt-in Class B skill. Use when the user says yes to "generate a skill from this?", or asks directly to turn a brainstorm or plan into a Claude Code skill.
---

# Skill Forge

Sources: the official [Anthropic Agent Skills spec](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) and [authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) (frontmatter rules, naming, progressive disclosure); mattpocock/skills' `productivity/writing-great-skills` (the craft vocabulary — see [CRAFT.md](CRAFT.md)).

This is the last step of a session, and the only one that writes outside `dist/<problem-name>/`'s `plan.md`. Never run it unasked — skill generation is always opt-in.

## 1. Gather inputs — branch on class

**Class A (document skill, low/medium freedom):** pull from the session's clarified input contract, target template, and invariants. The forged skill's job is to reproduce that template *precisely* every time — determinism is the entire point, so write low-freedom instructions: a bundled template file the skill fills in, not prose the model improvises from.

**Class B (opt-in, high freedom):** pull from the finished `plan.md` — the decisions, the lens(es) applied, the shape of the solution. The forged skill's job is to make the *reusable pattern* in that thinking available next time, not to reproduce this session's specific output. Write high-freedom, heuristic instructions: questions to ask, signals to watch for, not a fill-in-the-blanks template.

If it's unclear which artifact (template vs. heuristic) the skill should produce, ask — don't guess silently.

## 2. Name it

Prefer gerund form (`processing-pdfs`) or a clear noun/action phrase (`pdf-processing`, `process-pdfs`). Avoid vague (`helper`, `utils`) or generic (`tools`, `data`) names. Hard constraints, checked mechanically in step 4: lowercase letters, numbers, and hyphens only; ≤64 characters; no XML tags; must not contain "anthropic" or "claude".

## 3. Draft the frontmatter and body

`name` and `description` are the only required fields. Write `description` in **third person**, stating both what the skill does and when to use it — this is what the consuming agent matches against, so front-load the trigger phrasing:

```yaml
---
name: {gerund-or-noun-phrase}
description: {What it does}. Use when {the trigger conditions/phrases}.
---
```

Ask the user whether the forged skill should fire automatically when relevant, or only when manually invoked:

- **Fires automatically** (default) → leave frontmatter as above.
- **Manual-only**, e.g. it has side effects or the user wants to control timing → add `disable-model-invocation: true`.

Write the body to match the freedom level from step 1:

- **Low freedom** (Class A): "Use this template and fill in exactly these fields" — bundle the actual template as a separate file (e.g. `TEMPLATE.md`) next to `SKILL.md` and point to it, rather than describing the template in prose.
- **High freedom** (Class B): numbered heuristics or questions, the way [docs/sre-frameworks.md](../../../docs/sre-frameworks.md)'s "lens" questions are written — guidance the model adapts, not a script it fills in.

Keep the body under 500 lines. If reference material (a glossary, an API surface, a long template) would push past that, split it into a same-folder file and link to it once, directly from `SKILL.md` — never nest a reference behind another reference.

## 4. Validate, then fix, then re-validate

Run the bundled validator against the draft and treat its output as a gate, not a suggestion:

```
python scripts/validate_skill.py <path-to-drafted-SKILL.md>
```

`FAIL` lines are hard spec violations — fix and re-run before continuing. `WARN` lines (e.g. first/second-person description) are worth fixing but won't fail validation on their own. Only consider the skill done once the script prints `PASS`.

## 5. Write the output

Place the result at `dist/<problem-name>/<skill-name>/SKILL.md`, alongside any bundled files (`TEMPLATE.md`, `scripts/`, etc.) from step 3. Tell the user the skill is standalone: copying that folder into any project's `.claude/skills/` makes it invocable there.

For a sharper draft beyond bare validity — leading words, avoiding duplication/sprawl, picking the right information hierarchy — see [CRAFT.md](CRAFT.md).
