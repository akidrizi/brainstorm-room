# SRE frameworks — SLIs, SLOs, error budgets, toil, blameless postmortems

**Source:** Google, [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/) and the [*SRE Workbook*](https://sre.google/workbook/table-of-contents/) — specifically the [Service Level Objectives](https://sre.google/sre-book/service-level-objectives/), [Eliminating Toil](https://sre.google/sre-book/eliminating-toil/), [Postmortem Culture](https://sre.google/sre-book/postmortem-culture/), and [Error Budget Policy](https://sre.google/workbook/error-budget-policy/) chapters. Disclosed reference for [`skills/frameworks/sre-lens`](../skills/frameworks/sre-lens/SKILL.md).

## SLI — Service Level Indicator

A carefully defined *quantitative measure* of some aspect of the level of service provided. Almost always a ratio: good events ÷ total events (e.g., requests served under 300ms ÷ all requests). An SLI is a measurement, not a target — it's the speedometer, not the speed limit.

## SLO — Service Level Objective

A target value or range for an SLI, over a defined window. "99.9% of requests complete in under 300ms, measured over a rolling 28 days" is an SLO. SLOs are how a team makes reliability a deliberate, negotiated choice instead of an accident — and how they make data-driven decisions about *how much* reliability a thing actually needs (more reliability than the SLO requires is wasted engineering effort, not free safety margin).

## Error budget

`error budget = 100% − SLO`. A 99.9% SLO leaves a 0.1% error budget. Over 3 million requests in a four-week window, that's a 3,000-request budget to spend on outages, risky launches, planned maintenance, or experiments — not a number to defend at all costs. Spending the whole budget on one bad rollout is fine; spending it on toil-driven manual changes is not.

**What the error budget is for, mechanically:** it converts the SLO from a scolding metric into a shared resource both product and reliability work draw from. Budget remaining → ship faster, take more risk. Budget exhausted → an [error budget policy](https://sre.google/workbook/error-budget-policy/) kicks in (typically: freeze risky launches, redirect engineering toward reliability work) until the budget recovers. The policy is what gives the budget teeth — without a pre-agreed policy, "we're out of budget" is just an observation, not a constraint on behavior.

## Toil

> "Toil is the kind of work tied to running a production service that tends to be manual, repetitive, automatable, tactical, devoid of enduring value, and that scales linearly as a service grows." — *SRE book*, [Eliminating Toil](https://sre.google/sre-book/eliminating-toil/)

A task is more likely toil the more of these it exhibits:

- **Manual** — needs hands-on human time, including babysitting a script rather than letting it run unattended.
- **Repetitive** — done over and over, not novel problem-solving.
- **Automatable** — a machine could do it as well, or the need could be designed away entirely.
- **Tactical** — interrupt-driven and reactive, not strategic and proactive.
- **No enduring value** — the system is unchanged after the task completes.
- **Scales linearly** — effort grows in lockstep with traffic, users, or service count instead of sub-linearly.

Not every toil task needs all six traits; the more present, the more confidently it's toil. The lens matters operationally: toil that scales linearly with growth is a standing claim on future headcount, even when each individual instance looks cheap.

## Blameless postmortems

A postmortem after an incident that focuses on *contributing causes*, never on indicting a person or team. It assumes everyone involved had good intentions and acted reasonably given the information they had at the time. The blame is structural: a system that lets one human mistake cause an outage is the bug, not the human. This is what makes incident retrospectives a source of real signal instead of a reason to hide failures — punishing the reporter guarantees the next near-miss goes unreported.

## Using this as a lens on a Class B brainstorm

These aren't a checklist to run start-to-finish — they're questions to ask when a brainstorm's shape is operational, scaling, or reliability-flavored:

- **Framing the problem at all?** → Is there an SLI here, even an informal one? What would "good enough" (the SLO) actually be, and who'd be hurt by less?
- **Trading off speed vs. safety?** → Frame it as error budget: how much failure can this system absorb before the cost outweighs the benefit of moving fast?
- **Proposing a manual process, runbook, or recurring on-call task?** → Run it against the toil checklist. A linearly-scaling manual step proposed today is a hiring problem in a year.
- **Reasoning about a past or hypothetical incident?** → Stay blameless. Ask "what made it possible for this to happen," never "who caused this."
