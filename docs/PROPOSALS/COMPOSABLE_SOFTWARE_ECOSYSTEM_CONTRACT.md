# Composable Software Ecosystems: A Forever Works Contract Evolution Proposal

**Status:** non-normative research proposal, not Standard 0.1 or an implemented Public API operation. **Scope:** arbitrary software compositions, not just pairs of applications or any current operating system/toolkit. **Motivation:** long-lived reconstruction and generation of one or many products that interact through changing arrangements.

## 1. Problem

Forever Works Standard 0.1 already has durable intent, capability, invariant, constraint, dependency, compatibility, implementation, decision, migration, and evidence records connected by stable IDs and a directed graph. That is a strong source-neutral foundation, but it does not yet define **first-class semantics and conformance checks for multi-product ecosystems**. Generic record references alone do not specify typed participants, directional interactions, product configurations, multi-party coordination, authority propagation limits, state ownership, cross-product behavior, or a verified suite release.

The objective is not to canonize Chrome extensions, Avalonia, Android, React Native, Python or C++. These are only interchangeable implementation examples. The contract must remain language, OS, transport, vendor, agent and GUI neutral.

## 2. Ecosystems are arbitrary arrangements, not pairs

Represent an ecosystem as a typed, versioned **directed labeled multigraph or suitable hypergraph equivalent**. Participants may be products, modules, services, libraries, processes, interfaces, agents, users, external systems, data stores, or other nested ecosystems. Edges may be many-to-many, conditional, asynchronous, bidirectional (as two directions with explicit semantics), or multi-party coordination events. Repeated relationships between the same participants must be distinguishable.

Support:
- a mobile application interacting with multiple browser/desktop products;
- browser extension + Python helper + C++ service + Android client + shared data store;
- one producer with several consumers and independent authorization;
- intermediary brokers, fan-out, fan-in, replication, sync, offline operation, optional and dynamic participants;
- different deployments/topologies of one conceptual suite, with partial rollouts and fallback modes;
- a specification that asks for a completely new suite, a faithful reconstruction, selected capabilities or complementary components.

A participant's **identity/purpose/capabilities** must be separate from its chosen implementation technology. A relationship's **meaning** must be separate from its chosen transport or operating-system IPC/API. A suite need not have one central product, one coordinator or a fixed number of parts.

## 3. Proposed semantic entities (candidate vocabulary, not new Standard 0.1 kinds)

1. **Ecosystem / composition:** boundary, purpose, participants, configurations, collective obligations, ownership and evidence.
2. **Participant:** stable ID, role(s), provided and required capabilities, version/identity, independently replaceable implementation(s).
3. **Interface / port:** interaction capability, input/output types, errors, protocol-independent preconditions and postconditions.
4. **Interaction / relationship:** uniquely identified participants and endpoints; direction(s); trigger; exchange and permitted effects; semantics such as command, event, stream, query, data replication, shared storage or coordination.
5. **Coordination policy:** sequencing/ordering, concurrency, atomicity or compensations, retries, idempotency, timeouts, consistency, convergence and eventual failure behavior where relevant.
6. **Authority / trust contract:** per-participant permissions, consent, source and destination trust zones, data minimization, authentication/authorization and explicit prohibition of implicit privilege inheritance.
7. **Data and state stewardship:** authoritative owner/source of truth, schema and migration, synchronization and reconciliation, retention and deletion, conflict resolution.
8. **Topology / deployment profile:** one of potentially many valid mappings from conceptual participants/relationships to processes, hosts, networks, platforms, languages and toolchains.
9. **Derivation relationship:** preserve, transform, exclude, add; distinguish clone/port/adapt from assistant/companion/integrate/new-product generation.
10. **Acceptance / ecosystem evidence:** individual participant tests, every claimed interaction, emergent suite-level invariants and failure/recovery tests, independently tied to versions and deployment profile.

Represent shared capabilities once but require explicit evidence before considering a **shared implementation** safe for multiple participants or platforms.

## 4. Example neutral ecosystem (illustrative, not a current schema)

```json
{
  "profileVersion": "proposal-0.1",
  "ecosystemId": "example-suite",
  "participants": [
    {"id":"mobile-client","role":"user-interface"},
    {"id":"browser-extension","role":"context-capture"},
    {"id":"desktop-helper","role":"local-service"},
    {"id":"sync-store","role":"state-authority"}
  ],
  "interactions": [
    {
      "id":"capture-to-helper",
      "from":[{"participant":"browser-extension","port":"captured-items"}],
      "to":[{"participant":"desktop-helper","port":"intake"}],
      "semantics":"authorized-data-transfer",
      "authority":"explicit-consent-required"
    },
    {
      "id":"multi-client-sync",
      "from":[{"participant":"desktop-helper","port":"changes"},{"participant":"mobile-client","port":"changes"}],
      "to":[{"participant":"sync-store","port":"reconcile"}],
      "semantics":"state-convergence",
      "authority":"scoped-writes"
    }
  ],
  "configurations":[
    {"id":"desktop-only","participants":["browser-extension","desktop-helper","sync-store"]},
    {"id":"full-suite","participants":["mobile-client","browser-extension","desktop-helper","sync-store"]}
  ]
}
```

This example is **non-normative**, its syntax and property names are not accepted Standard 0.1 fields, and it makes no statement that the integrations are currently supported.

## 5. Compatibility-first evolution path

**Step A: versioned optional profile.** Propose a namespaced extension on existing records and a profile-level validator in a separate package. Existing Standard 0.1 files stay valid and existing bindings need not change. Link original capability, compatibility, evidence and dependency record IDs; do not create a second competing source of authoritative intent.

**Step B: conformance fixtures.** Add valid graphs for one participant, pairwise, three-way fan-in, fan-out, cyclic interactions, many-to-many coordination, multiple topologies and nested suites. Add invalid fixtures for dangling participant/port IDs, unintended privilege escalation, incompatible state ownership, duplicate IDs, forbidden platform coupling, missing integration evidence, and silent target-status reuse. Clarify that structural validity != behavioral validity.

**Step C: API proposal.** Candidate neutral operations, only after semantics are accepted and independently implemented: `listEcosystems`, `getEcosystem`, `listParticipants`, `listInteractions`, `traceInteraction`, `resolveConfiguration`, `assessComposition`, `evaluateEcosystem`, `compareDeploymentProfiles`. Preserve existing `describe()` capability discovery. These are **not v0.1 operations**. The API version may evolve independently of the model/profile version, and implementations must advertise exactly which operations are real.

**Step D: adoption evidence.** Build at least two independent proof bindings and execute the same shared conformance fixtures; produce agent-neutral examples and mapping guidance from user specifications (such as an Any-Shape job manifest) to accepted ecosystem records. Do not add an unverified new canonical record kind just because one application wants it.

**Step E: promotion.** Only consider a normative revision if the profile demonstrates clear interoperability/necessity; preserve historical v0.1 fixtures and migrations. Avoid forcing the entire standard into a specific ontology or central orchestration runtime.

## 6. Safeguards against cross-target contamination and conceptual drift

- Shared **meaning** is not shared source code, transport or UI.
- Product and configuration IDs are separate; a component can serve many products without borrowing their authorization or release status.
- Each interaction contract is explicit about direction, source of truth, data class, possible effects, permissions, platform and failure conditions.
- A desktop implementation cannot become a mobile requirement by proximity; host-specific assumptions require applicability/ownership metadata and independently tested adapters.
- Agent context should be retrieved by participant, topology, target and task while keeping an immutable accepted global contract. Selective context does not weaken completeness of suite evaluation.
- Every claimed pass is scoped to a specific component, interaction, deployment arrangement, requirement, artifact digest and environment.
- Ecosystem-level PASS cannot be inferred from all individual component builds passing: cross-product communication and end-to-end effects must be independently exercised.
- Drift/negative transfer/context interference are research hypotheses with measurable defect definitions. The format alone cannot guarantee their prevention.

## 7. Long-horizon replaceability

A future agent should be able to reconstruct participants and relationships in a **new configuration**, potentially splitting one old service into several new services or consolidating several old products into one, so long as accepted capabilities, authority constraints, state semantics and externally observable contracts are preserved or reviewed for change.

Always retain WHY the suite exists, WHAT each part and relationship must achieve, HOW it could be replaced with different technologies and topology, and PROOF that the composed result is faithful to its accepted requirements. No present framework, language, platform, transport or agent is permanent.

## 8. Research questions

- Can formal ecosystem relationships reduce wrong assumptions during one-run multi-product generation?
- Can a single accepted suite contract generate independently functional desktop, browser and mobile participants and validate their real interoperability?
- Does a structured ecosystem profile outperform plain documentation on held-out composition tasks at comparable time/compute?
- Can unfamiliar future agents redesign a suite topology while preserving its emergent behavior and security boundaries?
- What are the representational limits, cost and ergonomic burden of detailed relationship contracts, especially at hundreds of participants?

## 9. Why this belongs in Forever Works

Forever Works defines enduring purpose and compatibility independent of machinery. Multi-product compositions introduce *requirements that exist only in the relationships*—not in any one participating application. Without first-class, portable descriptions of those relationships and whole-ecosystem evidence, the standard can preserve each component yet lose the intended suite.

This proposal extends the standard's **subject matter**, not its dependency on Any-Shape. Any-Shape is one potential adopter and experimental testbed; other projects, agents, languages, and runtimes must be able to apply the same concepts.
