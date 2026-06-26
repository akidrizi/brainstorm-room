---
name: redesign-arch-doc
description: Produces a lightweight arc42-style architecture document for a proposed service redesign by interviewing the author section-by-section and assembling a single Confluence-ready Markdown file with Mermaid diagrams. Use when documenting the to-be design of a service or feature redesign so humans and AI agents can understand how it works and why. Invoke via redesign-arch-doc.
disable-model-invocation: true
---

# Redesign Architecture Doc

Produces a lightweight, arc42-inspired architecture document for a *proposed service redesign*
(the to-be design) by interviewing the author section-by-section and assembling one
Confluence-ready Markdown file with Mermaid diagrams. The output is written for both human
readers and AI agents: concise, predictably structured, every diagram captioned.

The source material is the author's brief plus their answers — never the current codebase. The
design being documented does not exist yet.

## Process

1. **Read the brief.** Treat the author's rough brief / RFC / ticket as source material.
   Pre-fill the metadata header and a draft of section 1 from it.
2. **Open [TEMPLATE.md](TEMPLATE.md).** It is the exact skeleton — copy it verbatim and fill the
   placeholders. Never reorder, rename, or renumber headings.
3. **Walk sections 1 → 11 in order.**
   - **Mandatory — 1, 3, 5, 9** — always filled, never deleted.
   - **Gated — 2, 4, 6, 7, 8, 10, 11** — each carries its gate question as an HTML comment in the
     template. Ask that question first; on *yes*, fill the section; on *no*, delete the entire
     section, heading included.
4. **One question at a time.** Never dump a list of open questions. With each question, propose a
   recommended answer inferred from the brief for the author to confirm or correct.
5. **Diagrams.** Sections 3 and 5 always carry a Mermaid diagram; add diagrams to 6 and 7 when
   those sections are included. Follow the conventions below, and caption every diagram with one
   line directly beneath it.
6. **Self-check, then output.** Verify the done-checklist below, then emit the single Markdown
   file and the Confluence usage note.

## Diagram conventions

| View | Mermaid type | Shows |
|---|---|---|
| §3 Context | `flowchart LR` | the service as one node; external users/systems around it; edges labelled with the interface |
| §5 Building Block | `flowchart TB` + `subgraph` | level-1 internal decomposition; drill to level 2 only for blocks the redesign changes |
| §6 Runtime | `sequenceDiagram` | one important scenario; include an error / alt path where it matters |
| §7 Deployment | `flowchart` | environment / host nodes containing the building blocks they run |

## Done-checklist

Do not finish until all of these hold:

- [ ] Metadata header present, every field filled.
- [ ] Sections 1, 3, 5, 9 present, with canonical numbered headings.
- [ ] Every included section keeps its canonical arc42 number and name, in numeric order.
- [ ] §3 and §5 each contain a Mermaid diagram; every Mermaid block has a one-line caption.
- [ ] No gated section is present unless its gate returned yes; no mandatory section is missing.
- [ ] Each ADR has at least Context and Decision filled.
- [ ] Output is one self-contained Markdown file — no external image references.
- [ ] Sections are concise and bullet-first, not pages of prose.

## Honest gaps

When an answer is unknown, do not invent a value:

- **Inferable from the brief** → write the inference and flag it: `> ⚠️ Assumption: {what was assumed}`.
- **Not inferable** → leave `_TODO: {what's needed}_` in place.

This also lets the skill run when no human is available to answer: infer what the brief supports,
mark everything else, and hand back a draft with its gaps made explicit.

## Getting it into Confluence

Paste the Markdown into the Confluence page, then drop each ` ```mermaid ` block into a Mermaid
macro so the plugin renders it (or use the space's Markdown import if available). The Mermaid
source stays the single source of truth for each diagram.
