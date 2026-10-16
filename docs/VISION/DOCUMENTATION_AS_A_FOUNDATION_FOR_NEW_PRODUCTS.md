# Documentation as a Foundation for New Products

## From preserving software to extending an ecosystem through understanding

**Status:** Non-normative vision and research proposal, recording explicit owner direction and proposed evaluation methods.  
**Date:** 2026-10-15 (America/Chicago).  
**Scope:** Agent-, language-, runtime-, framework-, platform- and vendor-neutral.  
**Relationship to the standard:** This document changes neither Standard 0.1 nor Public API v0.1. It proposes a demanding use and evaluation of documented intent, capabilities, rationale, implementations, compatibility and evidence. It does not declare universal autonomous product generation implemented or proven.

Related work: [Inheritable Software Ecosystem](INHERITABLE_SOFTWARE_ECOSYSTEM.md), [Any-Shape research](../RESEARCH/FIFTY_APP_INHERITANCE_AND_ANY_SHAPE.md), [Composable Software Ecosystems](../PROPOSALS/COMPOSABLE_SOFTWARE_ECOSYSTEM_CONTRACT.md), [optional ecosystem composition profile](../../spec/profiles/ecosystem-composition/v0.1/README.md), and [Selective Reconstitution](../PROPOSALS/SELECTIVE_RECONSTITUTION_CAPABILITY_EXTRACTION.md).

## 1. The owner's requirement

A sufficiently capable agent should be able to receive a broad request such as:

> Build an Android app that complements Atlas and Redown, makes their ecosystem more complete, and improves its revenue potential. Use their Forever Works documentation. You should not need access to their source repositories.

The short request supplies the assignment. The inherited documentation supplies the depth: what the products exist to accomplish, how their concepts fit together, what currently works, what is missing, why important decisions were made, what can change, and how a new participant can communicate correctly with them.

This extends the preservation mission. The desired agent should be able to reason about an unfamiliar ecosystem and propose a useful new product, rather than require the owner to dictate every screen, workflow and implementation detail. It should recognize opportunities the owner has not exhaustively specified, while keeping proposed opportunities distinct from accepted requirements.

The owner envisages Avalonia or React with an appropriate Android runtime as possible implementation choices; no choice has been made. They illustrate implementation freedom, not dependencies of Forever Works. Any-Shape is a possible consumer of this knowledge and a research vehicle; the standard must work without it.

## 2. What "documentation alone" means

The requirement is to succeed without needing the original products' source repositories, hidden institutional memory or private coaching. It is not a prohibition on programming tools, public target-platform references, compilers, test devices or documented services.

A versioned inheritance package should be exportable independently from the repositories. It contains the project models, explanatory documentation, relevant schemas, examples, portable fixtures and evidence needed for the task. Links to source locations can preserve provenance, but following those links must not be necessary to discover a missing protocol, state transition or acceptance rule.

Running APIs or independently operated test instances may be needed to prove integration. Authorizing those instances and supplying test credentials is an environment requirement, not permission to inspect the source. A strict trial can additionally disallow source-product binaries during construction and reserve an independently operated reference receiver for final evaluation. State the boundary precisely for every trial.

A future trial might allow only a locally exported package plus standard toolchains; another may allow public Android documentation. Report those access conditions instead of applying one ambiguous "documentation-only PASS" label.

The ambitious outcome is **enough preserved understanding to make and verify new decisions**. Documentation is not a substitute for access to an unavailable external service or authority to incur charges.

## 3. The knowledge that must survive

| Knowledge layer | Questions the package must answer |
| --- | --- |
| Purpose and users | What problems matter? What should the experience feel like? Which outcomes take priority? |
| Concepts and boundaries | What are resources, groupings, relationships, boards and publications? Which meanings must remain distinct? |
| Accepted behavior | What does a successful action do, including state changes, errors, cancellation and recovery? |
| Reasoning | Why were decisions made? Which alternatives were rejected, under which assumptions, and when should they be reconsidered? |
| Current implementation | Which mechanisms presently realize the behavior, how do they interact, and which defects or platform assumptions remain? |
| Interoperability | What exact formats, identifiers, APIs, authentication, authority and compatibility rules let another product participate? |
| Product economics | Which capabilities are Free or Premium? What limits, ownership promises, service costs and entitlement rules apply? |
| Evidence | Which claims were observed or tested, on which versions and environments? What is unverified? |
| Freedom to innovate | Which requirements are fixed, constrained or fluid, and what decisions may an agent propose independently? |

These layers need explicit links. A rationale separated from the behavior it protects is difficult to apply; an implementation description without its protected intent encourages accidental copying of obsolete constraints.

Current mechanisms belong in the documentation at sufficient depth: algorithms or pseudocode where necessary, component boundaries, state machines, sequencing, storage layouts, transaction assumptions, dependencies, wire examples, error codes and known failure paths. A source filename and a sentence saying "uses the API" are not an adequate substitute. Conversely, a line-by-line transcription of a repository does not automatically produce useful understanding.

A discovered implementation defect is not automatically an invariant. Record whether to preserve, correct or intentionally exclude it, with authority and evidence.

## 4. Efficient depth, rather than either vagueness or a context dump

Use a small entry document and exact identifiers to navigate detailed knowledge. Organize retrieval by task, capability, participant, interaction and target platform. Keep normative facts in their authoritative records and link narrative reasoning to them instead of copying inconsistent summaries into many files.

An efficient inheritance package can provide:

- A compact orientation and vocabulary explaining the ecosystem's purpose and participant roles.
- Capability-to-contract-to-implementation-to-evidence traces.
- Versioned detailed contracts, examples and failure cases retrieved when relevant.
- A compatibility and implementation inventory with dates, digests and supported environments.
- A gap ledger that identifies unknowns, proposals and unverified claims.

The overview is a navigation aid, not a replacement for required detail. Context selection must not hide a relevant permission boundary or acceptance obligation. Measure whether agents find the necessary information, not merely whether the package is short.

## 5. The concrete example: an Atlas/Redown Android companion

The envisioned ecosystem includes collection and organization in Atlas, remote acquisition/transfer workflows in Redown, shared collection semantics and optional customer-owned cloud storage. Some of this is planned rather than implemented. In particular, product vision, a generated interface and a successful build do not prove working cross-product integration.

Given adequate packages for both products, an agent could investigate mobile needs such as receiving a shared link or image, browsing a collection away from the desktop, adding notes and relationships, preparing a board on a phone, continuing the same work on desktop, or transferring authorized content through shared storage. These are candidate complementary workflows, not an instruction to copy every desktop feature into a phone app.

The reasoning chain should be visible: documented need → mobile opportunity → proposed workflow → affected contracts → implementation choice → independent acceptance evidence. Compare alternatives and justify the chosen first slice. Record which part of the solution is inherited and which is newly proposed.

The collection format must distinguish resource identity from its current location. It must preserve notes, tags, group membership and typed relationships across products. Availability through membership, semantic relationships, visual presentation and publication remain distinct. A new app must not silently publish a private collection merely because it can read it.

Android adapters must respect actual mobile file-access, sharing and background-execution rules. Desktop Chrome extension APIs and native filesystem grants cannot be assumed available on a phone. Data saved by desktop Atlas may be usable through an explicitly synchronized/exported collection even where direct access to a browser's private bookmark store is unavailable. Compatibility requires correct behavior through supported interfaces, not fictional platform parity.

Avalonia or a React-based implementation can be evaluated against these same contracts. Neither a shared framework nor shared source is required for shared meaning. The package should let the agent choose or evaluate mechanisms while preserving accepted constraints, including the owner's interest in modest hardware.

## 6. Economic reasoning is part of product understanding

"Improve revenue potential" is a broad objective to analyze under constraints. It does not mean a package can reveal the globally maximum possible revenue, which depends on future customer behavior, competition, distribution, pricing and operating costs.

An agent should be able to propose a credible commercial hypothesis: which mobile workflow adds value, which existing users might pay for it, how it complements existing subscriptions, what costs it creates, and how to measure adoption, conversion, retention and contribution. Distinguish a modeled forecast, a pricing hypothesis and observed paid results. An operationally successful integration does not independently prove demand or profitability.

Design the complete product vision and Free/Premium boundaries early. Document capability eligibility, quotas and execution boundaries before shipping the corresponding features, so alternate interfaces or imports cannot accidentally expose paid capabilities. Shared core functionality and paid operations need coherent policy across the ecosystem; hiding a button is not sufficient enforcement.

A mobile app could extend an existing subscription or motivate an optional suite bundle. That is a hypothesis to evaluate, not a license to invent new charges or change existing customer rights. Test production entitlements through documented interfaces; provide synthetic grants for isolated experiments. Keep permission to access files/accounts separate from payment status.

Preserve user ownership as part of the inherited product purpose: documented exports, readable collections after cancellation and honest provider dependencies. Commercial success should come from useful capability and reduced effort. A collection that remains recoverable can still support a valuable paid ecosystem of editors, integrations, automation and ongoing maintenance.

## 7. Opportunities opened by this approach

If these packages are sufficiently complete and agents sufficiently capable, several opportunities become plausible:

1. **New platforms from existing understanding.** Desktop, browser and mobile participants can be designed around their own input methods and constraints while exchanging the same meaningful state.
2. **Complementary products, not only replacements.** An agent can identify a workflow between existing products and implement the missing participant or adapter.
3. **Faster experiments.** Teams can evaluate a small candidate product against established contracts instead of rediscovering each integration from source.
4. **Renewable product families.** A change of language, UI framework, storage service or deployment topology need not destroy the ecosystem's conceptual identity.
5. **Human understanding and onboarding.** People can learn why a system works and make better decisions without first mastering every implementation detail.
6. **Independent implementations.** Multiple teams or agents can build compatible participants from the same published contracts and compare results.
7. **Cross-domain composition.** With many well-described projects, agents can explore combinations of capabilities that no original author enumerated.
8. **Durable economic assets.** Preserved reasoning, formats, interfaces and verification reduce the cost of future maintenance and may expand the number of useful products that can be attempted.

These possibilities can compound across a portfolio: each well-described project becomes another body of usable architectural knowledge. An inventory of fifty projects is not automatically fifty interoperable products, nor a guarantee of exponential commercial returns. Their contracts, rights, actual compatibility and independent evidence determine which combinations are feasible.

The most consequential possibility is that valuable software understanding becomes transferable independently of its original authors and machinery. That understanding can support original work, not merely keep old code alive.

## 8. Construction protocol for a broad request

A proposed agent workflow:

1. Verify the inherited package's versions, scope, provenance and evidence. Identify accepted intent separately from speculative roadmaps.
2. Build an ecosystem map: participant responsibilities, interaction contracts, state ownership, permission boundaries and missing capabilities. Consult the optional composition profile where appropriate without assuming static validation proves interoperability.
3. Infer candidate opportunities from the broad request. Explain each candidate's user value, economic rationale, cost and affected obligations.
4. Select a bounded first workflow within the task's authority. Declare inherited fixed/constrained/fluid aspects and record proposed new decisions. Ask about material ambiguity instead of silently altering accepted intent.
5. Implement through target-specific adapters using the documented contracts. Keep user consent and external deployment or billing authority explicit.
6. Verify real effects and failure recovery, then assess usability and performance on the target. Report remaining unknowns.
7. Package the new product's own Forever Works documentation and evidence, including discovered documentation gaps and any accepted contract evolution.

The broad assignment reduces unnecessary micromanagement. It does not grant unlimited filesystem access, production credentials, spending authority or permission to publish private data.

## 9. A source-restricted experiment that can falsify the claim

Create a frozen, checksummed documentation package for unfamiliar source products. Use a fresh construction agent with no prior project conversation or repository access. Record permitted tools, reference material, credentials and intervention rules before work begins.

Give the broad Android-complement request. Let the agent decide the proposed product workflow rather than supply a prewritten target implementation. Reserve representative interoperability cases and independently operated reference instances for evaluation; use documented behavior as the oracle, not hidden requirements invented after construction.

Evaluate separately:

| Evaluation | Evidence sought |
| --- | --- |
| Understanding | Accurate explanation of purpose, concepts, tradeoffs and cross-product obligations |
| Product judgment | A defensible complementary workflow and explicit economic hypothesis |
| Compatibility | Real exchange of collections and supported effects with both products; no metadata loss |
| Authority and plans | Correct grants, privacy, entitlements and quota behavior through every entry point |
| Recovery | Network interruption, revoked access, conflicts, partial operations and restart handled according to contract |
| Target experience | Working touch interaction, accessibility, resource use and performance on declared Android devices |
| Independence | No repository reads, hidden coaching or dependency on undocumented original code |
| Commercial evidence | Costs and adoption assumptions recorded; actual conversion/retention measured later if released |

Record time, compute, tool use, interventions, missing facts, defects and unresolved questions. A build is not an integration test. Two individually passing products do not prove a passing interaction. No actual commercial experiment means revenue improvement remains UNKNOWN.

Compare documentation-only, source-only and combined-input conditions on similar tasks and budgets. Include a concise ordinary-documentation baseline. Repeat with different agents, unfamiliar products and dissimilar platforms so one specially prepared example cannot establish universality.

A missing fact is evidence of a package gap when it concerns information the package was supposed to supply. Some unanswered questions instead concern genuinely new owner preferences, external permissions or unknown market outcomes. Classify the cause rather than blaming every clarification on incomplete documentation.

## 10. Continuity without freezing creativity

An agent-generated complementary app adds new decisions to the ecosystem. New features should acquire their own accepted intent, contracts, implementation descriptions and evidence. Do not promote the agent's guesses into original owner requirements or overwrite the provenance of inherited decisions.

Existing Standard 0.1 record kinds can describe intent, capability, constraints, compatibility, implementations and evidence. The experimental ecosystem composition profile can describe participant relationships within its declared scope. This document does not add a canonical record kind, invent a Public API operation or establish a new conformance badge. New machine-readable semantics require normal reviewed evolution with schemas, fixtures and independent proof bindings.

The research objective is ambitious and measurable:

> Can an unfamiliar agent receive a broad new-product objective and a portable body of documented software understanding, then create a useful, compatible, independently verified addition to the ecosystem without reading its source repositories?

Technical success would establish a foundation for further commercial trials. Broad success across different products and agents would support a much larger claim: preserving software understanding can enable continual invention as well as continual repair.
