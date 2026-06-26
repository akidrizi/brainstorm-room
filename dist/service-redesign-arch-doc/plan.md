# Simplified-arc42 Architecture Doc Skill for Service Redesigns

## Problem

We need a repeatable **skill** that produces a lightweight, arc42-inspired architecture
document for a **proposed service redesign (the to-be design)**. The author hands the skill
a rough brief; the skill **interviews them section-by-section** and assembles a **single
Markdown file targeted at Confluence (with the Mermaid plugin installed)**. Four sections are
**always present, in fixed order with fixed headings** — *Introduction & Goals*, *Context &
Scope*, *Building Block View*, *Architectural Decisions*. The other seven arc42 sections appear
**only when the interview confirms the redesign actually touches them**. The doc is written to
be consumed by **both humans and AI agents**: concise, structured, every diagram captioned, and
predictable enough that an agent always knows where to look.

## Class

**Class A — formatted-document skill.** The output shape is fixed (a trimmed arc42 template);
the deliverable is the skill that produces it consistently, not any one document.

## Approach

Per the Class A lens, the three things that define this skill:

### Input contract
- A **rough brief / RFC / ticket** describing the redesign (free text), plus a **live author**
  to answer follow-up questions.
- The skill does **not** read the current service's codebase — the design is to-be and lives in
  the author's head, so the brief + interview is the sole source.
- **Agent-run fallback:** if invoked with a rich brief but no human to answer, the skill infers
  from the brief and marks each inference rather than stalling (see invariants).

### Target template
Canonical arc42 numbering is preserved so docs are mappable across services. A metadata header
sits above section 1.

| # | Section | Status | Required diagram |
|---|---------|--------|------------------|
| — | **Metadata header** | always | — |
| 1 | **Introduction & Goals** | **mandatory** | — |
| 2 | Constraints | gated | — |
| 3 | **Context & Scope** | **mandatory** | Mermaid `flowchart` |
| 4 | Solution Strategy | gated | — |
| 5 | **Building Block View** | **mandatory** | Mermaid `flowchart` |
| 6 | Runtime View | gated | Mermaid `sequenceDiagram` |
| 7 | Deployment View | gated | Mermaid `flowchart` |
| 8 | Crosscutting Concepts | gated | optional |
| 9 | **Architectural Decisions** | **mandatory** | — |
| 10 | Quality Requirements | gated | — |
| 11 | Risks & Technical Debt | gated | — |

**Metadata header** (always, complete): Service/Component · Owner (team) · Status (Proposed /
Accepted / Superseded) · Last updated · Related links (Jira/RFC/repo/runbook).

Per-section content:
- **§1 Introduction & Goals** — 2–4 sentence summary of the redesign and the problem it solves;
  a **Quality Goals** table (top 3–5: attribute · concrete scenario · priority); a
  **Stakeholders** table (role · concern). The quality goals seed §10 if it's included.
- **§2 Constraints** — *gate: "Any org/tech/regulatory constraints binding this design?"* —
  bullets grouped technical / organizational / regulatory.
- **§3 Context & Scope** — system-boundary prose + a **Mermaid `flowchart`** showing the service
  as one box surrounded by external systems/users with labelled interfaces (business + technical).
  Optional external-interface table.
- **§4 Solution Strategy** — *gate: "Top-level strategy worth summarizing (tech stack,
  decomposition approach, key patterns)?"* — short bullets mapping each top quality goal → approach.
- **§5 Building Block View** — white-box decomposition as a **Mermaid `flowchart`** (level 1;
  drill to level 2 only for blocks the redesign changes). Each block: name + one-line responsibility.
- **§6 Runtime View** — *gate: "Does a key scenario need a sequence to be understood?"* — one
  **Mermaid `sequenceDiagram`** per important scenario + 1–2 line narrative; include an error path
  where it matters.
- **§7 Deployment View** — *gate: "Does the redesign change infra / topology / environments?"* —
  **Mermaid `flowchart`** mapping building blocks → infra nodes / environments.
- **§8 Crosscutting Concepts** — *gate: "Any concern spanning multiple components — auth, logging,
  error handling, data model, config?"* — a short subsection per concept.
- **§9 Architectural Decisions** — ADR-lite entries (Nygard compressed): Title · Status · Context ·
  Decision · Consequences. Capture every decision that makes the redesign non-obvious.
- **§10 Quality Requirements** — *gate: "Need quality scenarios beyond §1's goals?"* — scenario
  table (stimulus → response → measure).
- **§11 Risks & Technical Debt** — *gate: "Known risks or debt the team worries about?"* — table
  (risk/debt · impact · mitigation/plan).

### Invariants (must always hold of the output)
1. The **4 mandatory sections** always appear, in **fixed arc42 order with their canonical
   numbered headings**, even in the smallest doc.
2. Included optional sections keep their **canonical number + name** and stay in numeric order, so
   a doc containing only §1, §3, §5, §9 still reads in that order — an agent can map any doc to the
   same skeleton.
3. The **metadata header** is always present and fully filled.
4. **§3 and §5 always carry a Mermaid diagram**; **every** Mermaid block has a **one-line caption**
   directly beneath it.
5. The skill **never silently drops a mandatory section** and **never pads an optional one** — an
   optional section exists iff its gate returned yes.
6. Decisions are ADR-lite with **at minimum Context + Decision** populated.
7. Output is a **single self-contained Markdown file**; diagrams are fenced ` ```mermaid ` blocks
   with **no external image dependencies**.
8. **Tone:** concise, bullet-first, agent-readable; each section is a few short paragraphs/bullets,
   not pages.
9. **Honest gaps:** when an answer is unknown but inferable from the brief, the skill writes the
   inference and flags it `> ⚠️ Assumption: …`; when not inferable, it writes `_TODO: <what's
   needed>_` instead of inventing.

## Decisions

### Decision 1 — Document the to-be redesign only
**Context:** "How it works and why it was built that way" could mean the existing service (as-is),
the new design (to-be), a living doc, or a side-by-side delta.
**Decision:** Scope each doc to the **proposed redesign (to-be)** only; the skill does not read or
describe the current implementation.
**Consequences:** No codebase ingestion needed and decisions are forward-looking and crisp; the
trade-off is the doc carries no as-is baseline, so a reader wanting "what exists today" must look
elsewhere. Revisit if teams find they need the contrast.

### Decision 2 — Core-subset-mandatory template (4 fixed + 7 gated), not all 11
**Context:** arc42 has 11 sections; the user wants "standard but simpler, not overkill," yet
agents benefit from predictable structure.
**Decision:** Make **4 sections mandatory** (1, 3, 5, 9) and **gate the other 7** behind a yes/no
interview question, while preserving canonical numbering/order whenever a section appears.
**Consequences:** Small redesigns produce short docs without empty ceremony, and structure stays
mappable across docs. The trade-off vs. "all 11 present with N/A": section *presence* now varies
between docs, so a missing §7 means "not relevant," not "forgotten" — the gate log makes that
distinction, and the fixed numbering keeps cross-doc navigation intact.

### Decision 3 — Mermaid source as the diagram format for a Confluence target
**Context:** Destination is Confluence, which doesn't render Mermaid natively; options were
draw.io/Gliffy macros, exported PNG/SVG images, PlantUML, or Mermaid via the installed plugin.
**Decision:** Emit diagrams as **fenced ` ```mermaid ` blocks** and rely on the Confluence Mermaid
plugin to render them.
**Consequences:** Diagrams are **text — diff-able, agent-editable, single-source with the doc** and
need no binary attachments. The trade-off is a **hard dependency on the Mermaid plugin** being
installed; if a space lacks it, the diagram shows as code until the source is dropped into a Mermaid
macro (captured as a usage note). Switching to images later is possible but loses agent-editability.

## Plan

**Runtime behavior the skill must implement:**
1. **Ingest** the brief; pre-fill the metadata header and a draft of §1 from it.
2. **Walk sections 1→11 in order.** For each **mandatory** section, interview to fill it. For each
   **gated** section, ask its **gate question first**; on *yes*, interview and include it; on *no*,
   omit it entirely.
3. **One question at a time**, each accompanied by a **recommended answer drawn from the brief**
   (mirrors the grill-me ethos) — never a wall of open-ended prompts.
4. **Assemble** the single Markdown file: metadata header, then only the sections that survived,
   in canonical numbered order, with Mermaid blocks + captions.
5. **Self-check against the invariants** (mandatory sections present, §3/§5 diagrams + captions,
   header complete, gaps flagged not invented). Fix or flag before finishing.
6. **Emit a Confluence usage note**: paste the Markdown into the page; each ` ```mermaid ` block
   goes into a Mermaid macro (or via Markdown import if the space supports it).

**Diagram conventions to bundle as examples in the skill:**
- Context → `flowchart LR`: the service as one node, external actors/systems around it, edges
  labelled with the interface (e.g. `REST`, `Kafka topic`, `nightly batch`).
- Building Block → `flowchart TB` with `subgraph`s for hierarchy; drill down only on changed blocks.
- Runtime → `sequenceDiagram` per scenario, including at least one error/alt path where relevant.
- Deployment → `flowchart` with environment/host nodes containing the building blocks they run.

**Authoring rules to encode:**
- Keep every section short and bullet-first; prose only where a diagram can't carry the meaning.
- Caption every diagram in one line.
- Use `> ⚠️ Assumption:` for inferred answers and `_TODO:_` for genuine unknowns.
- Preserve arc42 numbering and heading text exactly, so docs are interchangeable to an agent.

This plan is self-contained: a person could produce a conforming document by hand from the template,
invariants, and conventions above, without the skill existing.
