# If We Had to Start Again

**Status:** Owner-requested vision and non-normative research proposal.  
**Date:** 2026-10-15  
**Scope:** Software continuity, agent-assisted reconstruction, and infrastructure recovery.  
**Evidence boundary:** The reconstruction and speed claims below are hypotheses to test, not capabilities already demonstrated by this repository. Standard 0.1 and Public API v0.1 are unchanged.

## The premise

Imagine that most of the software world disappeared.

Public servers have gone silent. Package registries, hosted development platforms, cloud APIs, certificate services, and documentation sites are unavailable. Many original developers and institutions are no longer reachable. Only a few computers, storage copies, technical archives, and sufficiently capable agents remain.

What would we wish we had preserved?

The ambition of **Forever Works**, together with implementations attempted through **Any-Shape**, is that surviving agents could recover useful capabilities extraordinarily quickly compared with rediscovering their purposes and engineering history from fragments. In the strongest version of the hypothesis, a carefully selected inheritance corpus could become a starting point for reconstructing much of modern digital life and the tools used to rebuild physical infrastructure.

**We propose preserving the ability to build again, even when the original implementation and its surrounding ecosystem can no longer operate.**

“Recreate everything in record time” expresses the owner's ambition. The research claim is more precise: accepted semantic contracts, executable evidence, dependency knowledge, offline resources, and explicit replacement freedom may sharply reduce reconstruction time and lost functionality. Neither universal reconstruction nor a speedup has yet been established.

This is peaceful reconstruction and service restoration. “Rebuild the world” refers to recovering useful capabilities for people and their institutions.

## 1. Why the format matters

A source archive can preserve a historical mechanism while losing the circumstances that made it usable. A surviving agent may still have to discover what the program was meant to do, which defects were accidental, which relationships mattered, and how to replace unavailable dependencies.

Forever Works should carry the answers across generations:

- Why the capability exists and who it serves.
- Which outcomes, state transitions, constraints, and external effects are required.
- Which invariants and compatibility promises must survive.
- Which mechanisms may change, and under what conditions.
- Why each dependency exists and how its role could be replaced.
- How to evaluate a new implementation and migrate surviving information.
- What is accepted intent, observed evidence, inference, or unresolved uncertainty.

The proposed reconstruction loop is:

1. Inspect the surviving environment and inherited capability graph.
2. Select an achievable recovery target and compatibility envelope.
3. Restore a working reference where possible, or implement a replacement.
4. Adapt interfaces and deployment through appropriate target tools.
5. Independently verify behavior, data recovery, resource use, and real effects.
6. Preserve the new evidence and implementation for the next generation.

The source language, framework, service provider, and internal architecture can change when the accepted contract permits it. An old mechanism need not become a permanent dependency merely because it was once used.

## 2. Forever Works and Any-Shape have different responsibilities

| Layer | Proposed responsibility |
| --- | --- |
| **Forever Works** | Preserve accepted meaning, requirements, relationships, provenance, permitted variation, migration obligations, and evidence. |
| **Any-Shape** | Attempt requested realizations using source/target adapters, implementation tools, and verification workflows. |
| **Recovery archive** | Supply source, bootstrap tools, dependencies, data, offline knowledge, and legal records that cannot be recovered from a semantic description alone. |
| **Independent evaluation** | Determine what actually works in the declared environment and report failures or unknowns. |

Any-Shape is one implementation pathway, not a mandatory dependency of the Forever Works standard. No universal target support is asserted. Hardware design, kernel recovery, and browser reconstruction require specialized tools and proof beyond interface generation.

A shared inventory capability might appear as a browser dashboard, a small-screen form, an accessible keyboard interface, a terminal workflow, or an agent API. Across those forms, accepted stock-accounting rules, authorization, persistence, and transaction behavior must survive. Presentation can vary without silently changing the operation.

Interfaces must remain usable by people as well as agents. Adaptation should preserve accessibility, error recovery, understandable navigation, and meaningful control.

## 3. The assumed operating-system foundation

This proposal assumes the owner's projects and a recoverable operating-system foundation are already in the archive.

Alpine is a Linux distribution, not a distinct kernel. Two different recovery paths must be distinguished:

- Preserve and rebuild Linux and the chosen Alpine userspace, with their respective licenses and dependencies.
- Preserve an explicitly scoped Linux-compatible ABI contract and implement it through alternative machinery, such as the experimental Zig Morphic/Alpz direction.

Running a BusyBox shell is valuable bounded evidence; it does not establish complete Linux compatibility. The system must declare supported architectures, workloads, syscall behavior, device assumptions, security boundaries, resource limits, and exceptions.

Kernel implementation language and internal structure may vary behind a verified compatibility boundary. Behavior becomes fixed only within the accepted envelope. Linux-derived code retains applicable licensing obligations; format extraction or language translation does not erase them.

See [Contractual Fixity, Implementation Fluidity](../PROPOSALS/CONTRACTUAL_FIXITY_IMPLEMENTATION_FLUIDITY_LINUX_ABI.md) for the existing research and evidence boundaries.

## 4. Twenty projects selected for reconstruction leverage

This is a proposed portfolio, not a mathematically optimal set or twenty self-contained dependency-free archives. Selection favors breadth and the ability to enable other capabilities. Projects can overlap deliberately: local storage and shared storage, for example, serve different recovery conditions.

Every project would need a separate accepted extraction scope, pinned revision, license review, complete dependency inventory, and recovery experiment.

| # | Candidate | Capability to inherit | Reconstruction leverage and required companions |
| --- | --- | --- | --- |
| 1 | [LLVM / Clang / LLD](https://github.com/llvm/llvm-project) | Compilation and linking for selected processor targets | Builds software; requires a surviving bootstrap compiler/toolchain, runtime libraries, headers, and build tools. |
| 2 | [QEMU](https://www.qemu.org/) | Emulation of selected machines and devices | Keeps historical environments executable on different hosts; needs compatible images, firmware where applicable, and sufficient resources. |
| 3 | [CPython](https://github.com/python/cpython) | General scripting, automation, and data processing | Connects recovery operations and scientific workflows; preserve required modules and native dependencies. |
| 4 | [Git](https://git-scm.com/) | Distributed version history and collaboration | Surviving full clones can carry project history without a central server; separately preserve LFS objects, submodules, and external artifacts. |
| 5 | [PostgreSQL](https://www.postgresql.org/) | Shared transactions and structured records | Supports institutional and business data; preserve logical exports, schemas, extension requirements, and recovery procedures. |
| 6 | [SQLite](https://www.sqlite.org/) | Embedded transactional storage | Supports small offline installations and portable local records; preserve application schemas and format expectations. |
| 7 | [restic](https://github.com/restic/restic) | Encrypted backups and restoration | Protects repeated recovery attempts; archives need repository contents and recoverable keys/passwords, not just backup software. |
| 8 | [OpenSSL](https://github.com/openssl/openssl) | Cryptography and secure transport primitives | Supports protected communications; entropy, key management, trusted implementations, and trustworthy time remain operational concerns. |
| 9 | [BIND 9](https://gitlab.isc.org/isc-projects/bind9) | DNS service and naming | Enables locally administered namespaces without surviving public DNS; preserve zone configuration and relevant keys. |
| 10 | [Caddy](https://github.com/caddyserver/caddy) | HTTP services and application delivery | Distributes local services; public certificate issuance cannot be assumed, so local trust and certificate recovery require explicit plans. |
| 11 | [Chromium](https://chromium.googlesource.com/chromium/src/) | Web rendering and interactive application execution | Provides a common target for adapted interfaces; a large build closure, graphics stack, fonts, and resource budgets must be accounted for. |
| 12 | [LibreOffice](https://www.libreoffice.org/) | Documents, spreadsheets, and presentations | Restores practical knowledge work and document exchange; preserve fonts, import/export expectations, and representative files. |
| 13 | [llama.cpp](https://github.com/ggml-org/llama.cpp) | Local inference for compatible models | Provides one route to local agents; weights, tokenizers, model formats, licenses, and adequate hardware must also survive. The runtime alone is not an AI. |
| 14 | [SciPy](https://github.com/scipy/scipy) | Numerical algorithms, optimization, and scientific computation | Supports calculation and simulation; preserve NumPy, numerical libraries, units, tolerances, and validated reference problems. |
| 15 | [QGIS](https://github.com/qgis/QGIS) | Geographic inspection, mapping, and analysis | Supports resource, settlement, transport, and utility planning; needs GDAL/PROJ and suitable maps, coordinate definitions, and local observations. |
| 16 | [FreeCAD](https://github.com/FreeCAD/FreeCAD) | Parametric mechanical design | Supports replacement parts and equipment design; manufacturing tools, materials, tolerances, and validation remain necessary. |
| 17 | [KiCad](https://www.kicad.org/) | Circuit schematics and PCB design | Supports replacement electronics; preserve component libraries, footprints, datasheets, and fabrication knowledge. |
| 18 | [Yosys](https://github.com/YosysHQ/yosys) | Digital logic synthesis | Transforms hardware descriptions into implementable logic; requires supported target descriptions and verification. |
| 19 | [nextpnr](https://github.com/YosysHQ/nextpnr) | Place and route for supported FPGAs | Complements Yosys where suitable hardware and device databases survive; does not manufacture chips. |
| 20 | [ERPNext](https://github.com/frappe/erpnext) | Inventory, purchasing, production, maintenance, and accounting | Coordinates organized reconstruction; needs its framework/runtime/database closure and locally appropriate business rules. |

The generative value of this set comes from its connections: compile software, emulate historical machines, restore records, communicate locally, run analysis, design parts and electronics, and coordinate production.

Several candidates carry copyleft or mixed-component obligations. QEMU and Git, for example, are not permissively licensed substitutes for MIT libraries. Their inclusion reflects reconstruction value and lawful open-source use, not a claim that every derivative may be distributed under arbitrary proprietary terms.

## 5. The larger fifty-project portfolio

**Dedicated maximum-coverage selection:** [Fifty Projects to Preserve the Widest Possible Capability](FIFTY_PROJECTS_MAXIMUM_CAPABILITY_PRESERVATION.md) now provides a separate, explicitly selected fifty-project portfolio for the recovery thought experiment. It retains all twenty recovery candidates above and expands scientific, physical, institutional, creative, and knowledge coverage. The historical list below remains the earlier commercially oriented catalogue; the dedicated document is the proposed selection when only fifty primary projects can receive deep preservation.

The earlier fifty-project discussion addressed broader economic and institutional coverage. It remains a complementary candidate catalogue, distinct from the twenty-project recovery selection above.

| Original catalogue range | Candidate projects | Coverage |
| --- | --- | --- |
| 1–5 | Frappe Framework; ERPNext; SuiteCRM; Medusa core; Puck | Business applications, production, customer management, commerce, visual builders |
| 6–10 | Form.io JavaScript library; Payload; Chatwoot community; Apache Superset; Temporal | Intake, publishing, support, reporting, durable workflows |
| 11–15 | Keycloak; OpenSearch; Qdrant; Node-RED; Jitsi Meet | Identity, search, semantic retrieval, automation, conferencing |
| 16–20 | Excalidraw; Tiptap core; Tesseract; OpenMRS; Moodle | Planning, editing, OCR, clinical information, education |
| 21–25 | LLVM; musl; CPython; Node.js; Git | Compilation, runtime foundations, programming, development history |
| 26–30 | CMake; llama.cpp; SQLite; PostgreSQL; Valkey | Builds, inference, local/shared storage, caching |
| 31–35 | NATS Server; Caddy; BIND 9; OpenSSL; OpenSSH | Messaging, service delivery, naming, protected communications, administration |
| 36–40 | curl; restic; Prometheus; OpenTelemetry Collector; Chromium | Transfers, recovery, monitoring, diagnostics, application execution |
| 41–45 | LibreOffice; JupyterLab; NumPy; SciPy; GDAL | Office work, reproducible computation, numerical and geographic processing |
| 46–50 | QGIS; FreeCAD; KiCad; Yosys; nextpnr | Spatial planning, mechanical/electronic design, programmable digital logic |

QEMU is an additional recovery-focused selection rather than a member of that original fifty. Counts are portfolio planning aids; the complete dependency closure will include many more projects.

The twenty commercial starting points are the first twenty entries of this broader catalogue. They offer possible products through specialized hosting, implementation, integrations, support, and complete industry workflows. Demand and profitability require separate validation. The reconstruction portfolio optimizes a different question: which capabilities enable the recovery of others?

## 6. What survives and what may change

| Must survive within an accepted recovery profile | May change when the contract permits |
| --- | --- |
| Intended outcomes and authorized effects | Programming language and source organization |
| Data meaning, integrity, and migration obligations | Framework, runtime, and deployment topology |
| Declared protocol, format, API, and ABI compatibility | Internal algorithms and component boundaries |
| Security and authorization boundaries | Storage mechanism behind verified semantics |
| Error, concurrency, and recovery behavior | UI layout, input medium, and presentation |
| Accepted numerical tolerances and resource budgets | Hardware accommodation behind the selected envelope |
| Provenance, licenses, and evidence history | Optional features explicitly outside the recovery scope |

Unknown behavior remains unknown. Observed bugs do not automatically become intended invariants. Changing an accepted obligation requires a reviewed profile revision and migration rationale rather than quietly labeling it replaceable.

For a database, “stores records” is inadequate: transaction isolation, crash recovery, supported queries, and data migration matter. For CAD, a file that opens is inadequate: units, geometry, tolerances, and exported manufacturing outputs matter. For a kernel, syscall numbers alone are inadequate: process, memory, filesystem, device, and failure semantics matter.

## 7. The recovery package

A semantic model reduces rediscovery but cannot supply missing physical resources or information it never contained. Each preserved capability therefore needs an offline recovery package.

| Package element | Minimum useful content |
| --- | --- |
| Accepted meaning | Intent, capabilities, invariants, constraints, compatibility scope, decisions, and explicit uncertainty |
| Implementation evidence | Pinned source, history where available, observed behavior, known defects, representative reference outputs |
| Build closure | Transitive dependencies, compilers, linkers, generators, headers, scripts, patches, and local package sources |
| Bootstrap seed | Known-working executables/images for declared surviving hosts, plus a documented path to rebuild tools and runtime components |
| Verification | Functional, negative, concurrency, resource, security, integration, migration, and held-out acceptance cases as appropriate |
| Surviving state | Logical data exports, schemas, format descriptions, backup recovery material, and migration tools |
| Operational knowledge | Offline manuals, diagnostics, repair procedures, resource requirements, and recovery order |
| Legal provenance | Exact licenses, notices, component/edition boundaries, source obligations, data/model rights, and revision identifiers |
| Archive integrity | Manifests, hashes, replicated copies, readable formats, and periodically exercised restoration procedures |

Do not assume a package cache is complete because one build succeeded online. Exercise a build with network access disabled. Break circular dependencies by documenting trusted bootstrap seeds and the limitations of that trust.

Hashes help detect changes relative to a trusted manifest; they do not establish the origin or safety of an untrusted archive. Encrypted copies need surviving decryption material and an appropriate custody plan.

## 8. The knowledge archive beyond software

A useful reconstruction corpus also needs lawful offline knowledge and data covering:

- Agriculture, food preservation, water treatment, and sanitation.
- Clinical reference information and public-health procedures.
- Electricity generation, distribution, storage, and equipment repair.
- Materials, machining, joining, measurement, and manufacturing.
- Component datasheets, machine manuals, and supported hardware designs.
- Geography, surveying, transport, and local resource observations.
- Educational resources, languages, units, standards, and scientific reference data.

These are separate preservation obligations. Clinical records software is not medical knowledge; PCB design software is not a fabrication plant; an inference runtime is not model weights.

This proposal assumes some usable computation, energy, storage, and agency survive. Recovery from literally no hardware or knowledge is outside its scope. Semiconductor production and industrial supply chains remain major physical bottlenecks.

## 9. Test the speed claim

“Record time” should be measured as **time to independently verified useful capability**, not time to generated code.

### Proposed offline cold-agent experiment

1. Choose one small application and freeze its accepted behavior and reference data.
2. Prepare matched survival environments with declared hardware, energy/resource budgets, and no public services.
3. Compare source-only, ordinary-documentation, and Forever Works recovery-package conditions at comparable resource budgets.
4. Give reconstruction agents the same target request and permitted tools. Keep the evaluation independent; do not provide undocumented coaching.
5. Remove or replace one dependency, then attempt a different interface/runtime where supported by the experiment.
6. Evaluate against held-out behavior, failure, data-recovery, resource, and real-effect tests.
7. Record time, cost, interventions, missing knowledge, compatibility coverage, regressions, and unknowns.
8. Repeat with an interconnected application pair, a bounded kernel subsystem, and a larger service stack.

Separate two questions: does semantic inheritance improve reconstruction, and does retaining additional offline material improve survival? Use controls with matched archive contents when isolating the format's contribution. Measure package preparation and maintenance costs as well as recovery gains.

Suggested outcomes include first successful boot, first verified transaction, first restored document, first compatible target implementation, and full completion of the declared recovery profile. Report failed attempts and partial results. No unknown requirement becomes a pass.

A clean rebuild alone does not prove behavioral continuity. Passing a finite test suite supports a bounded claim rather than universal equivalence.

## 10. A staged reconstruction program

| Stage | Target | Example acceptance evidence |
| --- | --- | --- |
| Survival seed | Bootable environment, readable archive, working local agent or manual tooling | Boot and inspect data without external services |
| Software production | Compiler/runtime, version history, reproducible local builds | Rebuild a selected program from preserved inputs |
| Local services | Naming, web delivery, databases, backups, local trust | Perform a transaction, interrupt execution, recover state |
| Human work | Adapted interfaces, documents, knowledge access | Complete useful tasks through accessible interfaces |
| Scientific and physical design | Numerical work, maps, CAD, PCB and supported FPGA workflows | Reproduce validated calculations and inspectable design outputs |
| Organized production | Inventory, procurement, maintenance, coordination | Track materials and authorized operations through an end-to-end scenario |
| Successive renewal | Replacement language/platform and renewed archive | Independent successor implementation preserves accepted obligations |

These are proposed stages, not a claim of a completed dependency graph. Extracting the real build/runtime graph is part of the work.

## 11. Commercial value and continuity value

The same engineering can support ordinary businesses before any catastrophe: recoverable deployments, portable workflows, maintainable applications, vendor exit, offline operation, and verified migration.

A possible commercial route is a narrow industry application assembled from forms, records, permissions, interfaces, and durable workflows. Any-Shape could help realize it in different environments; Forever Works could preserve why it works and what a successor must retain.

Economic opportunity does not prove demand. Preserving capabilities does not automatically create a market, and a successful business does not prove disaster recovery.

The legal foundation must travel too. MIT, BSD, and Apache-licensed cores are useful commercial candidates, while GPL, AGPL, MPL, LGPL, and project-specific terms impose different obligations. Preserve exact license text and review the actual extracted scope, dependencies, assets, models, and enterprise boundaries. A rewrite or format conversion does not automatically remove upstream obligations.

## 12. The claim we want to earn

**A sufficiently capable future agent, inheriting a sufficiently complete and independently tested corpus, could recover useful software and engineering capabilities far faster than reconstructing their meaning from scattered remnants.**

If repeated experiments support this, Forever Works could help turn fragile software inheritance into a renewable engineering resource. Any-Shape and other implementation pathways could let that resource take forms its original authors never anticipated.

The intended achievement is continuity of capability across generations of implementations. Each generation can leave a clearer, more recoverable inheritance.

We should aim to preserve more than what once ran.

**We should preserve enough understanding, evidence, and practical means that someone can build again.**

## Related repository documents

- [Foundational proposal](../FOUNDATIONAL_PROPOSAL.md)
- [Forever Works Standard 0.1](../STANDARD.md) — normative authority
- [Inheritable software ecosystem](INHERITABLE_SOFTWARE_ECOSYSTEM.md)
- [Fifty-App Inheritance, SUBSTRATE Mini, and Any-Shape](../RESEARCH/FIFTY_APP_INHERITANCE_AND_ANY_SHAPE.md)
- [Selective Reconstitution](../PROPOSALS/SELECTIVE_RECONSTITUTION_CAPABILITY_EXTRACTION.md)
- [Contractual Fixity, Implementation Fluidity: Linux ABI](../PROPOSALS/CONTRACTUAL_FIXITY_IMPLEMENTATION_FLUIDITY_LINUX_ABI.md)
- [Composable software ecosystems](../PROPOSALS/COMPOSABLE_SOFTWARE_ECOSYSTEM_CONTRACT.md)

## Primary project and licensing references

Candidate names in the selection table link to upstream projects. Before adoption, record the exact source revision and applicable terms rather than relying on this planning document.

- [Linux kernel licensing rules](https://docs.kernel.org/process/license-rules.html)
- [Alpine Linux](https://alpinelinux.org/)
- [LLVM licensing](https://llvm.org/docs/DeveloperPolicy.html#licensing)
- [QEMU licensing](https://www.qemu.org/docs/master/about/license.html)
- [PostgreSQL license](https://www.postgresql.org/about/licence/)
- [SQLite copyright](https://www.sqlite.org/copyright.html)
- [LibreOffice licenses](https://www.libreoffice.org/licenses/)
- [QGIS license](https://qgis.org/license/)
- [KiCad licenses](https://www.kicad.org/about/licenses/)
- [ERPNext license and trademark](https://docs.frappe.io/legal/others/license-and-trademark)
