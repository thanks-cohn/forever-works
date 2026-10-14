# Forever Works — Long-Horizon Vision: The Inheritable Software Ecosystem

**Status:** Owner vision and research charter; aspirational, non-normative.  
**Date:** 2026-10-14  
**Companions:** [Foundational Proposal](../FOUNDATIONAL_PROPOSAL.md), [Selective Reconstitution](../PROPOSALS/SELECTIVE_RECONSTITUTION_CAPABILITY_EXTRACTION.md), [50-App / Any-Shape Research Program](../RESEARCH/FIFTY_APP_INHERITANCE_AND_ANY_SHAPE.md)

## The purpose that must not be lost

**Forever Works is intended to become an enduring, openly implementable software-continuity standard, not merely a documentation generator, debugging utility, or project-specific framework.** The owner envisions a family of approximately **50 browser applications** forming an ecosystem. Every application should carry a sufficiently deep, precise, portable inheritance package that an unfamiliar capable agent, in a future decade, can take possession of the code, understand its purpose and functional identity, and **upgrade, renew, reform, recover, or reconstruct** it for whatever browser, desktop environment, programming language, framework, and platform exist then.

These are **research goals and acceptance targets**, not claims of capabilities already delivered or guarantees that all future agents will succeed. Their ambitious depth must guide standard design today.

> **Build once. Understand forever. Reconstruct whenever necessary.**

> **Preserve purpose, not obsolete machinery. The form may change; the intended meaning, authorized effects, and verifiable identity must survive.**

The standard should allow software to outlive its original implementation language, libraries, dependencies, development environment, creators, and initial distribution model. A future agent should inherit *knowledge and proof*, not simply code and anecdotes.

## The 50-application inheritance challenge

The 50 apps are not a marketing count; they are the flagship **diverse longitudinal conformance research corpus**. Ideally they represent varied real capabilities, data formats, state lifecycles, local and remote effects, interface paradigms, performance demands, and failure conditions. An app should be reconstructible **cold**, without a conversation with its author. Ordinary developer and user documentation is not by itself sufficient.

For each app, maintain a portable inheritance dossier containing at minimum:

1. **Owner-accepted mission and product identity:** what the app exists to accomplish, whom it serves, deliberate non-goals and scope.
2. **Capabilities and behavioral contracts:** named operations, inputs, outputs, invariants, constraints and edge cases, with stable IDs and versioning.
3. **User interactions and presentation semantics:** navigation, discoverability, accessibility, stateful flows, responsive behavior, visual orientation and quality; adaptation across mediums may change layout without changing what actions mean.
4. **State and persistence:** durable/ephemeral data, formats, migrations, undo, concurrency and recovery.
5. **Real-world effects:** exact HTTP/file/network/permission consequences, authorized effects, partial failures, retry behavior, error semantics, security and privacy.
6. **Implementation evidence:** actual call/data/dependency graphs, lifecycle, environment assumptions, startup conditions, undocumented side effects, limits and known defects.
7. **Replacement and transference instructions:** explicit seams, dependencies that can change, necessary compatibility boundaries, platform-specific adapters and migration plans.
8. **Verifiable evidence:** golden fixtures, independent replay tests, integration tests, runtime traces, benchmarks, accessibility checks, provenance and clear unresolved gaps.
9. **Continuity history:** which capabilities and contracts changed, why, who approved modifications and how earlier versions remain interpretable.

An agent should discover capabilities rather than guess from file names, then make changes under bounded conditions and produce evidence that the new implementation honors the intended contracts. **Undocumented behavior is an incomplete inheritance package, not tacit permission for an agent to guess.**

## Agent actions Forever Works must eventually enable

- **Upgrade:** adapt original apps to a newer browser, runtime, operating system or API.
- **Renew:** repair, replace obsolete dependencies, remove brittle coupling and stabilize previously working functionality.
- **Reform:** change architecture, presentation framework, or packaging while preserving required semantics.
- **Recover:** isolate a chosen slice of a tangled application into a reusable independent capability.
- **Reconstruct:** build an independently maintainable implementation in a different language or platform.
- **Verify:** audit the observable actions, authorized effects, presentation meaning, state, security and performance against accepted fixtures.

All are judged by evidence, not a successful build alone. An agent must be allowed to report **not verified / requires human confirmation** rather than invent compliance.

## Standard before implementation

Forever Works should strive to become a foundation upon which unrelated teams can build tooling and products, comparable **in ecosystem ambition** (not API purpose) to how interface ecosystems build around React or Flutter. Those frameworks build interfaces; Forever Works would standardize portable knowledge needed to *inherit* software across changing implementations.

Maintain three clearly separated layers:

| Layer | Role |
| --- | --- |
| **The Forever Works standard** | Vendor-, agent-, runtime-, language-, platform-, and framework-neutral semantics, UTF-8 JSON interchange, stable versioned schema, normative conformance behavior, provenance and governance |
| **SDKs, analyzers and research tools** | Independent competing implementations: CLI, extraction tools, agent adapters, legacy archaeology, dependency maps, diagnostic harnesses, migration and reconstruction utilities |
| **Adopter applications and demonstrations** | SUBSTRATE, SUBSTRATE Mini, Any-Shape and the 50-app browser ecosystem; users of the standard, never dependencies of its core |

The standard's authority should flow from the normative specification and conformance fixtures to bindings, not vice versa. An application must not require Any-Shape, SUBSTRATE, a proprietary cloud, a specific AI model, or the original authors to interpret its inheritance package. No single implementation should determine what compliance means.

Make improvements through public proposals, compatibility-preserving migrations, explicit versioning and independent tests. Research output should feed reviewed proposals back into the standard; do not rewrite normative rules solely because one demonstration needed a workaround.

## Definition of durable success

Imagine an agent in 2045 handed a 2026 application and its Forever Works package after the original developers and frameworks are gone. It can discover accepted intent, instantiate representative inputs, understand why dependencies existed, obtain or recreate equivalent capabilities in contemporary technology, verify actual effects and leave a fully documented successor. This remains an ambitious *experiment* until repeatedly observed.

The flagship **Cold Inheritance Test** is: give an independent capable agent an unfamiliar app, its inherited contracts and a target technology; forbid project-specific recipes and reliance on original-author guidance; evaluate implementation against independent behavior/state/effect/UX tests and record all assistance and failures. Run across increasingly diverse members of the 50-app corpus, repeat over time and compare other approaches.

Do not assert that all 50 apps, all technologies or every future agent are presently supported. The purpose of the program is to discover what the standard must contain to make that outcome progressively more attainable.

## The enduring criterion

> **Forever Works succeeds when people who never built our applications can independently understand, preserve, modernize, divide, reunite, and reconstruct them—and can build entirely new tools upon the standard without relying on us.**

SUBSTRATE demonstrates **selective rescue and structural clarity**. Any-Shape demonstrates **cross-medium transference**. The fifty applications demonstrate **generality and inheritance at scale**. None of them defines the limits of the standard.
