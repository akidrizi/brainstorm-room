---
name: sre-lens
description: Applies Google SRE's operational vocabulary — SLIs, SLOs, error budgets, toil, blameless postmortems — to a brainstorm. Use when a brainstorm-room Class B problem is operational, about scaling, on-call load, incident response, or a speed-vs-safety trade-off, to ask the right reliability questions before converging on a solution.
---

# SRE Lens

Source: Google, [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/) and the [*SRE Workbook*](https://sre.google/workbook/table-of-contents/). Full reference: [docs/sre-frameworks.md](../../../docs/sre-frameworks.md).

This is a lens, not a phase — reach for it during [`design-thinking`](../design-thinking/SKILL.md)'s Develop/Deliver when the problem's shape is operational, not on every Class B session.

## Questions to ask

Match the question to what the brainstorm is actually about:

- **Framing the problem itself?** Is there an SLI here, even an informal one — a ratio of good events to total events? What target (SLO) would actually be "good enough," and who is hurt by less?
- **Trading off speed vs. safety?** Frame it as an error budget: `100% − SLO`. How much failure can this absorb before the cost outweighs the benefit of moving fast — and what happens automatically (a freeze, a redirect to reliability work) once that budget is spent?
- **Proposing a manual process, runbook, or recurring on-call task?** Check it against toil's six traits: manual, repetitive, automatable, tactical, no enduring value, scales linearly with growth. A task proposed today that scales linearly is a hiring problem in a year — flag it even if it looks cheap right now.
- **Reasoning about a past or hypothetical incident?** Stay blameless: ask what made the failure *possible*, never who caused it. A system that lets one human mistake cause an outage is the bug.

## Output

Don't produce a separate report — fold the answers directly into the candidate solutions being compared in Develop/Deliver, as the operational consequences of each. If a question above surfaces a hard-to-reverse trade-off (e.g., "we accept a lower SLO to ship faster"), offer an ADR via [`adr`](../adr/SKILL.md).
