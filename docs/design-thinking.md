# Design Thinking — the Double Diamond

**Source:** UK Design Council, [*Framework for Innovation*](https://www.designcouncil.org.uk/resources/framework-for-innovation/) (2019 update to the original 2005 Double Diamond). Disclosed reference for [`skills/frameworks/design-thinking`](../skills/frameworks/design-thinking/SKILL.md).

The Double Diamond names two cycles of divergent-then-convergent thinking, back to back: the first diamond explores the *problem* space wide before narrowing it; the second explores the *solution* space wide before narrowing it. Most teams jump straight to the second diamond — picking a solution before the problem is actually understood. The model's whole value is forcing the first diamond to happen on purpose.

```
   DISCOVER          DEFINE           DEVELOP          DELIVER
  (diverge)        (converge)        (diverge)        (converge)
      ╲                ╱  ╲                ╱  ╲                ╱
       ╲              ╱    ╲              ╱    ╲              ╱
        ╲            ╱      ╲            ╱      ╲            ╱
         ╲          ╱        ╲          ╱        ╲          ╱
          ╲________╱          ╲________╱          ╲________╱
            problem    diamond 1         solution    diamond 2
            space      "the right        space       "the thing
                       problem"                       right"
```

## The four phases

1. **Discover** — Understand the problem rather than assume it. Talk to and spend time with the people affected by the issue before forming a hypothesis.
2. **Define** — Use what Discover surfaced to reframe the challenge — often differently than how it first showed up.
3. **Develop** — Generate multiple candidate answers to the now-sharp problem. Seek inspiration from elsewhere; co-design with different people; breadth before commitment.
4. **Deliver** — Test candidate solutions at small scale, kill the ones that don't work, and improve the ones that do.

The diamond shape itself is the discipline: widen before you narrow, in both halves. Narrowing without first widening is the most common failure — it looks efficient and produces an answer to the wrong question.

## The four principles (2019 update)

These govern *how* you move through the four phases, not what phase you're in:

1. **Put people first.** Start from an understanding of the people using a service — their needs, strengths, and aspirations — not from the solution you already have in mind.
2. **Communicate visually and inclusively.** Help everyone involved reach a shared understanding of the problem and the ideas in play; words alone under-communicate.
3. **Collaborate and co-create.** Work with others and get inspired by what others are already doing, rather than designing in isolation.
4. **Iterate, iterate, iterate.** Repeat the cycle. Iteration catches mistakes early, mitigates risk, and builds confidence in the eventual answer — treat the model as a loop you re-enter, not a line you walk once.

## Why brainstorm-room uses this for Class B

Class B problems (architecture, scaling, connectivity, debugging, new-solution ideation) fail most often by skipping Discover/Define and jumping straight to Develop — i.e., solutioning before the problem is sharp. Pairing the Double Diamond with [`grill-me`](../skills/engineering/grill-me/SKILL.md) gives Discover/Define teeth: grilling *is* how the first diamond gets executed in a chat-based medium, since there's no field research to send anyone on. The SRE lens and domain-modeling lens are tools you reach for *inside* Develop/Deliver when the candidate solutions are operational or structural in nature, respectively.
