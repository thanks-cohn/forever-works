# Forever Works
## Vision and Adoption Proposal: Becoming the Durable Software-Longevity Standard

**Status:** Strategic proposal  
**Project:** Forever Works  
**Scope:** Long-term positioning, interoperability, adoption, competitive differentiation, and standards strategy  
**Primary objective:** Make Forever Works the smallest, most trustworthy, most portable standard for preserving software intent across languages, tools, agents, vendors, and technological eras.

---

# 1. Executive Summary

Forever Works should aim higher than becoming a useful coding-agent memory tool.

Its long-term goal should be to become the **default durable architectural-memory and software-longevity standard**: the layer a project carries so that humans and future agents can understand what the software is trying to preserve, what may change, why dependencies exist, which invariants matter, and what evidence is required before a modernization can be considered safe.

The project cannot guarantee universal adoption. It can, however, deliberately optimize for the properties that make durable standards difficult to replace:

- a small and stable semantic core,
- open and boring interchange formats,
- language and vendor neutrality,
- independent conformance implementations,
- excellent import and export paths,
- extremely low adoption cost,
- conservative treatment of unknowns,
- explicit provenance,
- trustworthy migration and replacement verification,
- compatibility across versions,
- and usefulness even when no AI agent is present.

The strategic principle is:

> **Forever Works should survive the tools that use Forever Works.**

A coding agent, model provider, IDE, runtime, package manager, framework, or programming language may disappear. The project should still be able to explain itself.

This proposal also reviews important adjacent projects and standards. They validate the problem space. Forever Works should not dismiss or imitate them. It should interoperate with them while occupying a broader and more durable layer.

---

# 2. The Goal

The goal is not simply:

> Give today's coding agents better memory.

The goal is:

> **Give software a durable, portable memory of what must remain true across time.**

A successful Forever Works project should remain intelligible when:

- the original authors are gone,
- the current framework is obsolete,
- dependencies are unavailable,
- the original agent vendor no longer exists,
- the implementation language is no longer common,
- the build system has changed,
- the hosting environment has changed,
- and a future maintainer must decide what can be replaced without destroying the project's purpose.

## 2.1 Autonomous Inheritance Design Goal

A central design goal for Forever Works is:

> **A sufficiently capable agent should be able to inherit the repository cold, understand it, repair it, modernize it, verify the repair, and leave it in a better documented state without needing the original developers.**

This is not merely an aspirational slogan. It should function as a design test for the standard itself.

Whenever Forever Works adds a concept, schema, command, evidence model, recovery mechanism, or interoperability feature, the project should ask whether that addition improves the ability of a capable future agent to inherit a repository with no prior conversation, no institutional memory, and no access to the original authors.

The repository should contain enough durable intent, executable verification, provenance, compatibility information, recovery knowledge, dependency purpose, and implementation boundaries that a capable agent can reconstruct what matters without depending on undocumented human memory.

This does not imply that every possible failure can be repaired autonomously. Missing external credentials, unavailable proprietary services, lost data, physical hardware dependencies, or genuinely new product decisions may still require human judgment or outside resources. The design objective is to eliminate avoidable dependence on the original developers wherever the repository itself can preserve the knowledge required for safe continuation.

This goal turns Forever Works from a documentation format into an **inheritance substrate for autonomous maintenance**.

Forever Works should therefore sit **beneath** individual agents and tools.

```text
                    SOFTWARE PROJECT
                           │
                  Forever Works model
                           │
          ┌────────────────┼────────────────┐
          │                │                │
       humans          current agents    future agents
          │                │                │
       IDEs/CI          Codex/etc.      unknown systems
          │                │                │
          └────────────────┼────────────────┘
                           │
                preserved architectural meaning
```

The agent should be replaceable.

The model of the project's enduring meaning should not be.

---

# 3. What Forever Works Must Become

Forever Works should become the layer that can answer, in a stable machine-readable way:

- Why does this project exist?
- What capabilities define it?
- Which invariants may not be broken?
- Which constraints are intentional?
- Which compatibility obligations remain active?
- Why was a dependency selected?
- Is that dependency itself essential, or only the capability it supplies?
- What implementation choices are replaceable?
- What evidence supports a claimed architectural fact?
- What is known, inferred, proposed, historical, or still unknown?
- What would a replacement have to prove?
- Did a migration preserve the protected requirements?
- Which assumptions may now be retired?
- What has changed, and what must still survive?

The core product is therefore not a particular CLI, SDK, agent plugin, or language binding.

The core product is the **portable semantic contract**.

---

# 4. Competitive Thesis

Forever Works should not attempt to win by trapping users in a proprietary runtime or by duplicating every feature of every adjacent tool.

It should win by becoming the **interoperability layer they can all safely support**.

The desired future reaction from another tool maker is:

> "We do not need to invent another format for durable software intent. We can read and write Forever Works."

This suggests a moat based on:

1. semantic stability,
2. conformance,
3. trust,
4. portability,
5. compatibility,
6. integration breadth,
7. migration evidence,
8. and very low adoption friction.

The project should make it easier to integrate Forever Works than to invent a competing private representation.

---

# 5. Adjacent Projects and How Forever Works Should Differentiate

The following projects are important because they show that the broader field is real. Some are direct competitors in part of the problem; others are complementary systems that overlap with one layer of Forever Works.

The comparison below describes **Forever Works' intended differentiation**, not a claim that every competing project is inferior in its own chosen scope.

## 5.1 AGENTS.md

AGENTS.md is a simple open convention for giving coding agents repository-specific instructions. It is deliberately analogous to a README for agents: build commands, testing instructions, conventions, and working rules.

That simplicity is a major strength. Forever Works should support AGENTS.md rather than attempting to replace it.

### Where Forever Works should go further

AGENTS.md principally answers:

> How should an agent work in this repository?

Forever Works is intended to answer a different and more durable set of questions:

> Why is the software this way? What must survive? What may change? What evidence makes a replacement acceptable?

Forever Works should be stronger for long-term inheritance because its model is structured around enduring intent, capabilities, invariants, dependency purpose, compatibility, provenance, and migration verification rather than primarily operational instructions.

**Strategic response:** import useful AGENTS.md facts where appropriate, reference AGENTS.md as an agent-operational companion, and never force users to choose between the two.

Source reviewed: https://agents.md/

---

## 5.2 Project Canon

Project Canon describes itself as durable architectural memory for coding agents. It preserves caps, contracts, invariants, and decisions so agents do not quietly rewrite architectural intent.

This is one of the closest conceptual neighbors to Forever Works and validates the need for durable repository-native architectural memory.

### Where Forever Works should aim to be stronger

Forever Works should distinguish itself by making **software longevity and modernization** the organizing problem, not only preservation of current architectural decisions.

Its durable model should explicitly connect:

```text
intent
  ↓
capability
  ↓
invariant / constraint
  ↓
dependency purpose
  ↓
current implementation
  ↓
candidate replacement
  ↓
evidence
  ↓
migration verification
```

That replacement and migration chain is central. A dependency can disappear without the project losing the reason the dependency existed.

Forever Works should also insist on language-neutral canonical interchange, cross-language conformance, explicit provenance classes, backward-aware versioning, and pass/fail/unknown replacement evaluation.

**Strategic response:** interoperate with Canon-style invariants and decisions where possible, while keeping Forever Works focused on preserving meaning across implementation replacement and technological eras.

Source reviewed: https://agentcanon.dev/

---

## 5.3 Cairn

Cairn is architecture memory that agents can write, reconcile against code, gate at commit time, and query. Its blueprint → reconcile → gate → query loop is powerful because it attempts to keep declared architecture synchronized with implementation.

This is valuable territory and Forever Works should learn from its emphasis on checking declarations against reality.

### Where Forever Works should aim to be stronger

Forever Works should make a narrower foundational promise at the semantic layer:

> Preserve architectural meaning independently of the mechanism used to verify it.

A Forever Works invariant might be verified by Cairn, a test suite, static analysis, a benchmark, a human review, future tooling, or an evidence artifact that does not yet exist.

That makes Forever Works suitable as a **long-lived interchange and inheritance layer** even if today's scanner, graph engine, or enforcement mechanism is replaced.

Forever Works should also model why a dependency or implementation exists and how a successor can prove equivalence. Its goal is not only to detect drift from today's blueprint, but to enable a future system to replace today's blueprint implementation while preserving the reasons behind it.

**Strategic response:** treat systems such as Cairn as excellent potential evidence and enforcement providers for Forever Works rather than forcing Forever Works to own every code-analysis technique itself.

Source reviewed: https://github.com/cairn-framework/cairn

---

## 5.4 AsDecided

AsDecided provides repository-native decision infrastructure for coding agents. It keeps human-reviewed engineering decisions in validated Markdown, retrieves applicable decisions deterministically, serves them to agents, and can connect machine-checkable consequences to CI.

Its insistence that deterministic checks prove only what they can actually prove is closely aligned with Forever Works' conservative evidence philosophy.

### Where Forever Works should aim to be stronger

Forever Works should cover a wider longevity graph than decisions alone.

A decision is one kind of durable architectural knowledge. Forever Works also needs first-class representations of:

- project intent,
- capabilities,
- invariants,
- constraints,
- dependencies and their purpose,
- implementations,
- compatibility contracts,
- migrations,
- and evidence.

Its key differentiation should be the ability to ask:

> If we replace this implementation or dependency, which enduring requirements must the replacement satisfy, and what is the current evidence state for each one?

Forever Works should also be usable without MCP, Markdown processing, or any particular retrieval engine. Plain UTF-8 JSON plus a minimal CLI should remain enough for a future environment to reconstruct the model.

**Strategic response:** support decision import/export and treat deterministic decision systems as peers or evidence sources, while retaining the broader software-longevity model.

Sources reviewed:
- https://asdecided.com/
- https://github.com/asdecided/core

---

## 5.5 projectmem

projectmem focuses on persistent coding-agent memory across sessions. It records typed events such as issues, attempts, fixes, decisions, and notes, and can warn before an agent repeats an approach that previously failed.

That solves an immediate and important agent-continuity problem.

### Where Forever Works should aim to be stronger

Forever Works should distinguish **project history** from **enduring architectural truth**.

An event log can tell a future agent:

> We tried approach X and it failed.

Forever Works should be able to say:

> Requirement Y exists because of invariant Z. Approach X failed under evidence E. Any future replacement must still satisfy Y and Z.

This lets historical events contribute evidence without making every event part of the permanent semantic core.

Forever Works should also remain useful if the project has no session-memory system at all. Its model should describe the architecture and preservation contract, not depend on reconstructing meaning from chronological agent activity.

**Strategic response:** allow project-memory systems to contribute historical evidence and provenance while Forever Works owns the durable requirement graph.

Sources reviewed:
- https://projectmem.dev/
- https://github.com/riponcm/projectmem

---

## 5.6 ProductSpec

ProductSpec defines a portable layer for product intent before implementation. It includes structured product specs, acceptance criteria, evals, Agent Run receipts, Decision Traces, conformance fixtures, and mechanisms for reconciling agent execution with a spec revision.

This is especially important because it treats intent and evidence as portable artifacts rather than merely chat context.

### Where Forever Works should aim to be stronger

Product intent and architectural longevity overlap, but they are not identical.

ProductSpec is concerned with questions such as:

> What are we building? What is in or out of scope? How do we know this implementation run satisfied the current product contract?

Forever Works should specialize in:

> What must this software continue to preserve over years or decades, even when the implementation technology changes?

Forever Works should therefore be stronger at dependency intent, implementation replaceability, protected invariants, compatibility obligations, migration verification, and long-term inheritance across languages and runtimes.

The two systems should be able to complement each other. A ProductSpec acceptance criterion or decision trace could become evidence or provenance for a Forever Works capability, constraint, or architectural decision without either standard swallowing the other.

**Strategic response:** build import/reference interoperability rather than a competing product-management format.

Sources reviewed:
- https://github.com/gokulrajaram/ProductSpec
- https://github.com/gokulrajaram/ProductSpec/blob/main/docs/agent-run.md
- https://github.com/gokulrajaram/ProductSpec/blob/main/docs/vision.md

---

# 6. Predecessors We Should Respect, Not Replace

Architecture Decision Records, design documents, READMEs, test suites, API schemas, package manifests, lockfiles, CI configuration, comments, issue history, and version control already preserve valuable pieces of project knowledge.

Forever Works should not require a project to abandon them.

Instead:

```text
README / ADR / AGENTS.md / ProductSpec / tests / CI / manifests
                            │
                            ↓
                    forever discover
                            │
                            ↓
                     draft Forever Model
                            │
                    explicit human review
                            │
                            ↓
                  accepted durable meaning
```

The project should **browse reality first and extend reality when necessary**: discover existing truth, preserve provenance, and ask users to author only what cannot safely be inferred.

---

# 7. The Adoption Strategy

## 7.1 Make adoption almost embarrassingly easy

The long-term experience should approach:

```sh
forever init
forever audit
```

`forever init` should inspect the repository and produce useful **draft** records from existing sources without fabricating architectural truth.

Automatically discovered information must remain visibly imported, inferred, or agent-proposed until accepted.

A user should not need to manually author dozens of files before receiving value.

## 7.2 Import before asking users to rewrite

Forever Works should eventually understand or reference:

- AGENTS.md,
- ADR formats,
- ProductSpec,
- package manifests,
- lockfiles,
- API schemas,
- test metadata,
- CI workflows,
- build files,
- dependency manifests,
- source annotations,
- architecture documents,
- and compatible decision/memory systems.

The standard should become a common semantic destination for knowledge projects already possess.

## 7.3 Export everywhere

Canonical JSON should remain boring and durable.

From it, tooling should be able to generate:

- human Markdown,
- dependency explanations,
- diagrams,
- architecture maps,
- agent context bundles,
- migration plans,
- audit reports,
- CI-readable verification,
- compact summaries,
- and adapter-specific formats.

The canonical model should not depend on those renderings.

## 7.4 Become the easiest format for other tools to support

Publish:

- JSON Schemas,
- conformance fixtures,
- golden outputs,
- small reference parsers,
- clear versioning rules,
- compatibility tests,
- and adapter guidance.

A third-party implementation should be able to determine objectively whether it implements Forever Works correctly.

---

# 8. Conformance as a Strategic Advantage

Forever Works should make conformance unusually serious.

JavaScript, TypeScript, C, Python, C++, and future bindings should interpret the same canonical fixtures consistently.

Over time, likely additional proofs include:

- Rust,
- Go,
- Java,
- C#,
- and external CLI-only consumers.

The goal is not to accumulate SDKs for marketing.

The goal is to demonstrate:

> **The semantics do not belong to any one implementation language.**

The specification, schemas, fixtures, normalization rules, and observable behavior should remain more authoritative than any binding.

When implementations disagree, the disagreement should improve the standard rather than silently create dialects.

---

# 9. Replacement Verification as the Killer Capability

Many systems can record:

> We chose dependency X.

Forever Works should be able to preserve:

```text
Why X exists.
Which capability X supplies.
Which invariant X protects.
Which compatibility obligation X participates in.
Whether X itself is replaceable.
What a successor must prove.
Which evidence exists.
Which evidence is missing.
Whether the migration currently passes, fails, or remains partial.
```

This should become one of the project's defining capabilities.

Example:

```text
dependency.old-streamer
  purpose: streaming remote files
  required:
    capability.streaming
    capability.resumability
    invariant.bounded-memory
    compatibility.configuration-v1

candidate.wasm-streamer
  streaming: pass
  resumability: pass
  configuration-v1: pass
  bounded-memory: unknown

result: partial
```

The key trust property is:

> **Absent evidence is never silently converted into success.**

If a protected requirement has not been demonstrated, Forever Works should say so.

---

# 10. Provenance Must Be Sacred

Forever Works should preserve the difference between:

- explicit,
- inferred,
- imported,
- historical,
- agent-proposed,
- and verified evidence.

An agent's confidence must never become architectural authority merely because it was serialized.

This is not only a correctness rule. It can become a major reason people trust the standard.

The system should make it easy for automation to help without making it easy for automation to rewrite project truth accidentally.

---

# 11. Compatibility Is Part of the Product

A longevity standard that repeatedly strands its own earlier users has failed its central purpose.

Forever Works should therefore treat compatibility as a first-class product property.

The project should maintain:

- explicit format versions,
- preserved old conformance fixtures,
- predictable schema evolution,
- unknown-field preservation where safe,
- non-destructive migrations,
- documented deprecation periods,
- machine-readable migration paths,
- and the ability for future implementations to understand historical models.

A Forever Works 0.x repository should become evidence that the standard itself practices long-term stewardship.

---

# 12. Self-Hosting as Proof

Forever Works should describe Forever Works.

Its own `forever/` model should eventually explain:

- why the project exists,
- why JSON is canonical,
- why language neutrality is protected,
- why JavaScript and TypeScript are separate proof targets,
- why C exists as a portability stress test,
- why provenance cannot be silently promoted,
- why unknown evidence does not pass,
- why conformance fixtures are authoritative,
- why specific dependencies exist,
- which dependencies may be replaced,
- and how Forever Works itself may be modernized.

This creates a uniquely strong demonstration:

> A future agent should be able to inherit Forever Works using Forever Works.

---

# 13. The Project Should Not Become an Agent

Forever Works should not attempt to own reasoning, coding, code search, chat, IDE interaction, or every verification engine.

Those are replaceable consumers and providers.

Forever Works should instead define the durable layer they exchange.

```text
                   Forever Works
                 durable semantics
                        │
        ┌───────────────┼───────────────┐
        │               │               │
      agents        analyzers       human tools
        │               │               │
      Codex           Cairn          documentation
      others          tests          architecture UI
      future AI       CI             review systems
```

This keeps Forever Works small enough to survive.

---

# 14. What We Should Optimize For

When design choices conflict, prefer:

1. **Durability over novelty.**
2. **Interoperability over lock-in.**
3. **Explicit semantics over clever inference.**
4. **Evidence over confidence.**
5. **Small stable primitives over a giant ontology.**
6. **Backward compatibility over needless format churn.**
7. **Plain files over mandatory infrastructure.**
8. **Independent conformance over one privileged implementation.**
9. **Easy adoption over ceremony.**
10. **Replaceable tooling over permanent runtime assumptions.**
11. **Human authority over automatic promotion of inferred intent.**
12. **Preserving purpose over preserving obsolete machinery.**

---

# 15. What "Winning" Should Mean

Forever Works should not define success as eliminating neighboring projects.

Success should mean that the ecosystem increasingly treats Forever Works as a dependable common layer.

Strong signs of success would include:

- coding agents natively reading Forever Works,
- IDEs and CI systems understanding it,
- architecture tools exporting to it,
- memory systems referencing it,
- spec systems linking evidence into it,
- package managers or dependency tools using dependency-intent records,
- multiple independent language implementations passing the same conformance suite,
- major projects keeping a `forever/` model beside their source,
- and future maintainers being able to modernize old projects without reconstructing their purpose from archaeology.

The strongest possible outcome is not:

> Everybody must use our implementation.

It is:

> **Everybody can rely on the standard.**

---

# 16. North Star

Forever Works should become:

> **The smallest durable standard that lets software explain what must survive when everything around it changes.**

Its most important strategic promise is:

> **Preserve purpose, not obsolete machinery.**

And its architectural promise is:

> **Preserve the upper graph. Replace the leaves.**

If Forever Works can make those principles concrete, easy to adopt, rigorously testable, independently implementable, and trustworthy across time, it has a credible path to becoming infrastructure rather than another temporary agent tool.

---

# 17. Immediate Strategic Work Suggested by This Proposal

The next generations of Forever Works should progressively add:

- first-class import/reference adapters for adjacent standards,
- a provenance-preserving discovery workflow,
- excellent `forever init` and `forever audit` experiences,
- a formal adapter/conformance profile,
- replacement and migration evaluation golden suites,
- compatibility guarantees for historical model versions,
- more independent language implementations,
- generated human documentation and diagrams,
- compact agent context export,
- a fully self-hosted `forever/` model,
- and documented integration paths for tools that want to consume or emit Forever Works.

Each addition should be judged by the same question:

> Does this make Forever Works more useful as a durable common standard without making the standard dependent on today's tools?

---

# 18. Current Reference Set

The competitive discussion in this proposal was based on publicly available project descriptions reviewed in October 2026:

- AGENTS.md: https://agents.md/
- Project Canon: https://agentcanon.dev/
- Cairn: https://github.com/cairn-framework/cairn
- AsDecided: https://asdecided.com/ and https://github.com/asdecided/core
- projectmem: https://projectmem.dev/ and https://github.com/riponcm/projectmem
- ProductSpec: https://github.com/gokulrajaram/ProductSpec

These projects are evolving quickly. Forever Works documentation should describe them factually, avoid stale caricatures, and periodically revisit this comparison as the field matures.
