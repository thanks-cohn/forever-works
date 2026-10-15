# Codex implementation request — ecosystem composition profile (30-minute session)

**Location:** operational Codex instructions only. **Repository:** `thanks-cohn/forever-works`, `main`. **Status:** bounded implementation request; NOT normative standard text. **Time budget:** approximately 30 minutes. The permanent schemas, validators and API must remain agent-, toolkit-, platform-, transport- and language-neutral.

## Read before editing
1. `AGENTS.md`, `README.md`, `docs/STANDARD.md`, `docs/CONFORMANCE.md`, `docs/API/PUBLIC_API_V0_1.md`.
2. `docs/PROPOSALS/COMPOSABLE_SOFTWARE_ECOSYSTEM_CONTRACT.md` (the architectural proposal).
3. Current `spec/schemas/`, `spec/conformance/` or the actual conformance fixture directories, public API implementation/tests and adapters; locate existing patterns before choosing new paths.
4. The independent adoption context: `thanks-cohn/any-shape/forever-works/DECISION_RECORD_SOURCE_NEUTRAL_ECOSYSTEM_ROADMAP.md`. No direct dependency on Any-Shape is permitted.

## Mission
**Implement a versioned, OPTIONAL composition profile for arbitrary software ecosystems**, not just pairs of applications. A suite may include zero/one/many products, services, libraries, processes, interfaces, data stores, external systems, people, agents and nested ecosystems. Relationships may form directed multigraphs and many-to-many coordination with fan-in, fan-out, cycles, shared services, alternate deployment configurations and independently replaceable participants.

Preserve meaning and proof independently of any current platform or toolkit. Android, Windows, Linux, browser extension, Avalonia, React Native, Python, C++, C# and JavaScript are **examples only**, never enum limits in the abstract profile. Compositions must represent the system's collective purpose as well as individual participants and interactions. Interactions have first-class semantics and independent acceptance obligations.

## Session priorities, in order

### A. Build executable optional profile and JSON Schema
- Choose a clear versioned neutral package/directory location consistent with existing layout (e.g. `spec/profiles/ecosystem-composition/v0.1/`); document exact profile identity, version, authority and relationship to normative Standard 0.1.
- Define stable ecosystem, participant, endpoint/port, interaction, configuration/topology and evidence references. Support multiple edges between same participants, one-to-many and many-to-many interactions, nested suites and varying active participants. Avoid any two-product assumption.
- Distinguish *provided/required capabilities*, semantic contracts, data/state ownership, ordering/concurrency, retry/idempotency, consistency, offline/failure/recovery obligations, authority/trust/data access, version compatibility, and topology-specific obligations. Favor expandable typed structures over a huge mandatory field inventory; unknown semantics must remain visible and cannot silently confer authority.
- Keep framework, language, OS, transport and process deployment as replaceable implementation bindings; these do not define the ecosystem's semantic identity.
- Profile should reference existing Forever Works record IDs (intent, capability, invariant, compatibility, etc.) where applicable; no parallel authoritative source of intent.
- Add bounded validation: IDs/references, port existence, duplicate IDs, configurations, nested suite cycles where forbidden, references with safe paths, authority boundary and state owner declarations, contract/evidence scope. Distinguish structural errors from warnings/undetermined runtime behavior.
- Version and document migrations/forward-extensions. Avoid changing `foreverVersion` 0.1 or breaking canonical schemas.

### B. Conformance fixtures and executable validator
- Add independently runnable valid fixtures: single component; 4+ participant fan-in/fan-out; bidirectional multi-edge interactions; many-to-many sync/shared service; nested suite; two valid deployment alternatives.
- Invalid fixtures: dangling port/participant, duplicate interaction ID, inappropriate implicit privilege inheritance, contradictory state authority, invalid topology references, unexpected schema fields, missing or forged evidence being treated as PASS.
- Deliver a reference loader/validator with stable issue codes and deterministic normalization/output. Follow existing repository language/testing conventions, no gratuitous dependencies.
- Add negative tests for unsupported or unknown semantics, preserving optional-profile behavior for legacy projects.
- Do not mistake structurally valid JSON for working runtime interoperability; suite-level verification must remain `UNKNOWN`/`NOT_RUN` until actual independent evidence.

### C. Minimal optional API discovery
- Prefer a profile-specific, versioned neutral API wrapper exposing a small subset (such as `listEcosystems`, `getEcosystem`, `listParticipants`, `listInteractions`, `resolveConfiguration`, `validateComposition`).
- Only advertise operations actually implemented, with compatible error codes and deterministic ordering. Keep `describe()` discovery; **do not silently add unsupported calls to Public API v0.1 or alter its semantics**.
- If session time is insufficient, prioritize schema + validator + tests; leave public API proposals documented without claims of implementation.

### D. Documentation, neutral examples, continuity
- A concise adopter guide explaining why the profile exists, how it differs from basic dependency links, how it maps to canonical Forever Works records, how to replace the implementation and how to independently verify a suite.
- Additive dated historical/decision note: prior single-project model still valid; new profile expresses meaning *between* components and configurations. Make explicit what remains proposed or unverified.
- Demonstrate an illustrative browser extension + helper + mobile app + shared service suite **only as a technology-neutral example**, with a second structurally different example to prevent hardcoding. No coupling to Any-Shape.
- Preserve provenance; don't elevate imported/inferred/agent-proposed to owner-approved merely because validation passed.

## Preserve all existing compatibility
- Keep Standard 0.1, canonical model schemas, existing record fixtures and Public API v0.1 working and unchanged unless a true bug fix is unavoidable and justified with tests.
- New profile opt-in: old models remain valid with no new required fields.
- Keep existing JavaScript implementation conformance; do not claim C/C++/Python adapters support new features unless they actually do.
- No destructive rewrites, undocumented changes to record normalization or invented migrations.
- Never mark a composed system verified because its parts compile.

## Acceptance for this 30-minute session
1. At least one executable JSON Schema + loader/validator for the profile.
2. Real passing tests on representative **4+ participant** and intentionally invalid arrangements.
3. Deterministic results and explicit `UNKNOWN`/unsupported evidence status.
4. Backward compatibility suite executed (or precise environment blockers recorded).
5. README/adopter instructions and historical reasoning committed.
6. A useful updated handoff in `codex/HANDOFF_LATEST.md`, including commits, exact commands/results, unresolved issues and a copy-ready continuation prompt.

## Time and handoff discipline
- By about minute 20, assess achievable remaining work.
- At about minute 25, transition to test execution, commits and handoff preparation.
- By about minute 28, commit/push `codex/HANDOFF_LATEST.md`, with a precise next-session plan.
- Deliver the final summary by around minute 30.
- If less can be completed, preserve a working minimal validator plus conformance tests before expanding API breadth. The repository must always distinguish implemented functionality from design proposals.

## Forward sequence
After this bounded Forever Works proof: independently map a synthetic multi-product Any-Shape `specifications.json` job to the new profile; confirm the same relationships/authority/evidence survive; then build two functional interacting outputs and evolve the profile against observed gaps. Avoid rewriting the standard based solely on one application.
