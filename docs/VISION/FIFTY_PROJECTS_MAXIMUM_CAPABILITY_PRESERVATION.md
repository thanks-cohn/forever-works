# Fifty Projects to Preserve the Widest Possible Capability

## If We Could Carry Only Fifty

**Status:** Owner-requested non-normative vision and research portfolio.  
**Date:** 2026-10-15  
**Companion:** [If We Had to Start Again](IF_WE_HAD_TO_START_AGAIN.md)  
**Authority:** [Standard 0.1](../STANDARD.md) remains normative. This document adds no schema, command, adapter, or API requirement.

> If only fifty major projects could receive deep preservation, which fifty would leave future people and agents the greatest practical capacity to recover, understand, create, and build again?

This document proposes an explicit selection of **exactly fifty primary project subjects**. It retains all twenty recovery candidates from the companion document and expands across additional domains. It replaces the earlier commercially oriented fifty-project list **for this particular maximum-coverage thought experiment**; that earlier list remains a useful product catalogue.

The ambition is larger than keeping fifty applications alive. Through Forever Works, we would preserve their purposes, causal explanations, accepted capabilities, relationships, constraints, permitted variation, and verification evidence. Through Any-Shape and other implementation pathways, humans and agents could attempt new realizations, interfaces, combinations, and successors.

**Source preserves a realization. Purpose, context, and evidence can help preserve the ability to realize it differently.**

This is a reasoned candidate portfolio, not a proven global optimum. “Greatest possible capture” is the selection objective. Establishing superiority over other portfolios would require a defined coverage model, archive budget, and comparative recovery experiments.

## 1. What the fifty-project limit means

The thought experiment assumes that the owner's applications, Forever Works, Any-Shape, and a recoverable operating-system foundation are already available. They are not counted again.

Alpine is a distribution. Its Linux kernel/userspace path or an alternative kernel's explicitly scoped Linux-compatible ABI path must have an actual recovery package. Neither is assumed complete merely because a shell once ran.

The fifty are **primary preservation subjects**, each with a complete, openly recorded dependency closure. That closure includes runtimes, build tools, libraries, firmware where lawful and needed, formats, datasets, models, and bootstrap seeds.

This distinction is essential: fifty projects do not mean fifty repositories can rebuild everything without other software. If the limit literally prohibited every additional software component, this list would not be operational. A stricter archive would need radical scope reduction and a different selection.

Preservation targets should be versioned upstream scopes, not vendor accounts or hosted subscriptions. Preserve a useful capability even when optional enterprise features are excluded. No project has already been extracted or reconstructed merely through inclusion here.

## 2. Selection principles

We favor:

1. **Generative leverage:** capabilities that enable rebuilding other capabilities.
2. **Breadth:** scientific, industrial, institutional, creative, educational, and everyday work.
3. **Complementarity:** additions that cover a missing domain rather than repeat the same product.
4. **Recoverability:** useful offline operation and realistic restoration on declared surviving hardware.
5. **Understandable contracts:** behavior that can be specified, tested, and explained.
6. **Interoperability:** durable formats, protocols, migration paths, and explicit units.
7. **Human and agent access:** both people and software can understand and operate the recovered capability.
8. **Lawful continuity:** preservation and adaptation rights remain documented across generations.

Some redundancy is deliberate. SQLite and PostgreSQL address local and shared transactional storage. Kiwix and MediaWiki address reading an offline corpus and collaboratively revising knowledge. NATS and MQTT address different messaging environments.

A concrete deployment would weight these priorities differently. A rural recovery site might prioritize maps, communications, repair, and water-system models; a surviving university might prioritize scientific computation and education.

## 3. The selected fifty

Each row identifies a project, its contribution, and one example of meaning that must be captured beyond source code. Examples are proposed extraction questions, not accepted statements of upstream author intent. They require observation, provenance, review, and scope-specific tests.

### A. Rebuild the machinery that builds software

| # | Project | Why carry it? | Meaning and evidence to preserve |
| --- | --- | --- | --- |
| 1 | [LLVM / Clang / LLD](https://github.com/llvm/llvm-project) | Compile and link software for selected architectures. | Target ABI, language semantics, optimization assumptions, compiler correctness cases, and bootstrap trust. |
| 2 | [musl](https://musl.libc.org/) | Supply a compact C runtime and userspace interface foundation. | Calling conventions, supported interfaces, allocation/thread behavior, errors, and kernel assumptions. |
| 3 | [CMake](https://github.com/Kitware/CMake) | Describe and regenerate builds across environments. | Which build inputs and generated artifacts matter, target configuration, reproducibility limits, and toolchain discovery. |
| 4 | [QEMU](https://www.qemu.org/) | Run selected historical machine environments on surviving hosts. | Guest-visible hardware behavior, machine profiles, firmware/image requirements, timing limits, and emulation acceptance tests. |
| 5 | [Git](https://git-scm.com/) | Preserve development history and support distributed renewal. | Object integrity, history relationships, merge/conflict behavior, and separate recovery of LFS/submodule contents. |

### B. Execute programs, agents, and scientific reasoning

| # | Project | Why carry it? | Meaning and evidence to preserve |
| --- | --- | --- | --- |
| 6 | [CPython](https://github.com/python/cpython) | Provide accessible automation and general computation. | Language behavior, interpreter/runtime assumptions, module closure, and reference workloads. |
| 7 | [Node.js](https://github.com/nodejs/node) | Run JavaScript services and existing application logic. | Event-loop behavior, streams, cancellation, module compatibility, and observable filesystem/network effects. |
| 8 | [Chromium](https://chromium.googlesource.com/chromium/src/) | Provide a broad interactive web application target. | Rendering, input, accessibility, storage, sandboxing, browser APIs, and bounded application compatibility profiles. |
| 9 | [llama.cpp](https://github.com/ggml-org/llama.cpp) | Execute compatible local language models. | Model architecture/format, tokenizer behavior, inference configuration, resource needs, weights, and evaluation tasks. |
| 10 | [SciPy](https://github.com/scipy/scipy) | Preserve numerical algorithms for science and engineering. | Mathematical assumptions, units, tolerances, convergence/failure conditions, and validated reference problems; include NumPy and numerical dependencies. |

### C. Keep records and knowledge recoverable

| # | Project | Why carry it? | Meaning and evidence to preserve |
| --- | --- | --- | --- |
| 11 | [SQLite](https://www.sqlite.org/) | Support durable records on small offline installations. | Transactions, file-format behavior, corruption boundaries, schema meaning, and recovery/migration cases. |
| 12 | [PostgreSQL](https://www.postgresql.org/) | Support shared institutional and business data. | Isolation, constraints, query semantics, extension needs, logical exports, and crash recovery. |
| 13 | [restic](https://github.com/restic/restic) | Restore data after storage loss and failed reconstruction attempts. | Snapshot meaning, repository integrity, restore procedures, encryption keys, and actual restoration evidence. |
| 14 | [OpenSearch](https://github.com/opensearch-project/OpenSearch) | Make large surviving records and archives searchable. | Index mappings, analyzers, query/ranking expectations, update behavior, and ways to rebuild indexes from original data. |
| 15 | [Kiwix tools](https://github.com/kiwix/kiwix-tools) | Serve and manage packaged knowledge offline. | Archive formats, navigation/search, provenance, content rights, and coverage of the actual preserved corpus. |

### D. Reconnect computers without old public services

| # | Project | Why carry it? | Meaning and evidence to preserve |
| --- | --- | --- | --- |
| 16 | [BIND 9](https://gitlab.isc.org/isc-projects/bind9) | Reestablish locally administered naming. | Zone ownership, resolution/caching behavior, delegation, expiry, and local-root recovery assumptions. |
| 17 | [OpenSSL](https://github.com/openssl/openssl) | Supply cryptographic and secure-transport primitives. | Protocol profiles, key lifecycle, entropy/time assumptions, reference vectors, and security maintenance requirements. |
| 18 | [OpenSSH](https://www.openssh.com/) | Administer and transfer between recovered machines securely. | Authentication, host identity, permissions, sessions, and recovery of trust without former identity services. |
| 19 | [Caddy](https://github.com/caddyserver/caddy) | Deliver local web applications and APIs. | Routing, service boundaries, failure handling, certificate lifecycle, and explicit local-trust plans. |
| 20 | [curl](https://github.com/curl/curl) | Transfer information across supported protocols. | Protocol behavior, retries, streaming, authentication, error reporting, and data-integrity checks. |

### E. Coordinate services and explain failures

| # | Project | Why carry it? | Meaning and evidence to preserve |
| --- | --- | --- | --- |
| 21 | [Keycloak](https://github.com/keycloak/keycloak) | Rebuild organizational identity and access management. | Identity ownership, authentication, authorization, recovery, revocation, and offline trust assumptions. |
| 22 | [NATS Server](https://github.com/nats-io/nats-server) | Connect distributed services through messaging. | Delivery/ordering profiles, persistence configuration, consumer recovery, and duplication/loss behavior. |
| 23 | [Temporal](https://github.com/temporalio/temporal) | Coordinate workflows that survive interruptions. | Replay, retry policy, idempotency, time assumptions, versioning, and external-side-effect boundaries. |
| 24 | [Prometheus](https://github.com/prometheus/prometheus) | Observe resource use and service health. | Metric definitions, units, sampling, retention, alert meaning, and misleading/missing data cases. |
| 25 | [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector) | Collect and transport diagnostic evidence. | Trace/metric/log meaning, context propagation, processing, sampling, and evidence loss under pressure. |

### F. Connect computation to signals and physical systems

| # | Project | Why carry it? | Meaning and evidence to preserve |
| --- | --- | --- | --- |
| 26 | [GNU Radio](https://github.com/gnuradio/gnuradio) | Preserve programmable signal processing and radio experimentation. | Signal units, sample rates, modulation/DSP assumptions, hardware interfaces, and validated reference signals. |
| 27 | [Eclipse Mosquitto](https://mosquitto.org/) | Exchange sensor and device messages using MQTT. | Topic meaning, QoS behavior, retained messages, device identity, reconnect behavior, and broker configuration. |
| 28 | [Node-RED](https://github.com/node-red/node-red) | Assemble event-driven integrations and monitoring workflows. | Event meaning, state ownership, device adapters, failures, and authorization for real-world effects. |
| 29 | [OpenModelica](https://github.com/OpenModelica/OpenModelica) | Model interacting physical systems for analysis and simulation. | Equations, units, initial/boundary conditions, solver settings, model validity, and experimental comparisons. |
| 30 | [ngspice](https://ngspice.sourceforge.io/) | Simulate analog and mixed-signal circuits. | Component models, operating limits, netlist interpretation, convergence, tolerances, and measured comparisons. |

### G. Design physical and digital artifacts

| # | Project | Why carry it? | Meaning and evidence to preserve |
| --- | --- | --- | --- |
| 31 | [FreeCAD](https://github.com/FreeCAD/FreeCAD) | Design parametric mechanical parts and assemblies. | Design intent, units, constraints, tolerances, dependencies, and manufacturing/export acceptance. |
| 32 | [KiCad](https://www.kicad.org/) | Design circuit schematics and printed circuit boards. | Electrical intent, nets, footprints, component substitutions, fabrication rules, and design-review evidence. |
| 33 | [Yosys](https://github.com/YosysHQ/yosys) | Synthesize implementable digital logic. | HDL semantics, timing/reset assumptions, target mapping, and equivalence tests. |
| 34 | [nextpnr](https://github.com/YosysHQ/nextpnr) | Place and route logic for supported FPGAs. | Device databases, pin/timing constraints, routing validity, and target-specific programming requirements. |
| 35 | [Blender](https://www.blender.org/) | Create 3D assets, visualizations, animation, and explanatory media. | Scene meaning, geometry, materials, animation, interchange formats, and bounded visual/interaction expectations. |

### H. Understand territory and organize institutions

| # | Project | Why carry it? | Meaning and evidence to preserve |
| --- | --- | --- | --- |
| 36 | [GDAL](https://github.com/OSGeo/gdal) | Read, transform, and exchange geographic information. | Coordinates, projections, raster/vector interpretation, units, nodata handling, and transformation accuracy. |
| 37 | [QGIS](https://github.com/qgis/QGIS) | Plan using maps, spatial analysis, and local observations. | Layer provenance, analysis assumptions, coordinate systems, map interpretation, and reproducible workflows. |
| 38 | [ERPNext](https://github.com/frappe/erpnext) | Coordinate materials, maintenance, production, and accounting. | Stock/cost meaning, transaction rules, units, roles, production dependencies, and local institutional policies. |
| 39 | [OpenMRS](https://github.com/openmrs/openmrs-core) | Preserve clinical-record and care-workflow infrastructure. | Clinical concepts, identity, record provenance, access control, auditability, and locally validated workflow scope. |
| 40 | [DHIS2 core](https://github.com/dhis2/dhis2-core) | Support population-level information and health reporting. | Indicator definitions, aggregation, provenance, missingness, privacy boundaries, and interpretation limits. |

### I. Teach, document, and recover information

| # | Project | Why carry it? | Meaning and evidence to preserve |
| --- | --- | --- | --- |
| 41 | [LibreOffice](https://www.libreoffice.org/) | Recover office documents, spreadsheets, and presentations. | Document meaning, formulas, layout expectations, fonts, compatibility profiles, and export fidelity. |
| 42 | [MediaWiki](https://www.mediawiki.org/) | Build and revise shared institutional knowledge. | Authorship, revision history, references, dispute/approval practices, permissions, and export/recovery. |
| 43 | [Moodle](https://github.com/moodle/moodle) | Organize courses, assessment, and learning records. | Learning objectives, prerequisites, grading meaning, accessibility, and content/learner-data portability. |
| 44 | [Tesseract](https://github.com/tesseract-ocr/tesseract) | Recover searchable text from scanned material. | Language/model requirements, confidence, layout, known recognition failures, and correction workflows. |
| 45 | [FFmpeg](https://ffmpeg.org/) | Decode, convert, and process audiovisual records. | Codec/container profiles, timing, metadata, quality/loss expectations, build configuration, and rights. |

### J. Communicate, create, and adapt interfaces

| # | Project | Why carry it? | Meaning and evidence to preserve |
| --- | --- | --- | --- |
| 46 | [Inkscape](https://inkscape.org/) | Create vector diagrams, signage, illustration, and precise layouts. | Geometry, text/font assumptions, scale, SVG interpretation, and output requirements. |
| 47 | [GIMP](https://www.gimp.org/) | Edit and restore raster images. | Color management, layers, transformations, metadata, and fidelity limits. |
| 48 | [Jitsi Meet](https://github.com/jitsi/jitsi-meet) | Support local or regional real-time conferencing. | Session identity, media behavior, consent/access boundaries, network limits, and failure recovery. |
| 49 | [Matrix Synapse](https://github.com/element-hq/synapse) | Support persistent messaging and federated collaboration. | Identity, room/event semantics, synchronization, federation, encryption boundaries, and state recovery. |
| 50 | [Puck](https://github.com/puckeditor/puck) | Provide an editable visual composition foundation for interfaces. | Component meaning, allowed configuration, serialized state, accessibility, and real effect bindings. |

These fifty include developer infrastructure, user applications, libraries, and domain tools. “Project” is the consistent selection unit; calling all fifty browser apps would misdescribe the scope.

## 4. Preserve the questions, not merely the answers

For every selected capability, preserve the following questions and the current accepted answers. An unanswered question is useful when it exposes a recovery gap.

| Question | Required kind of understanding | Example |
| --- | --- | --- |
| **Why?** | Purpose, beneficiaries, rejected alternatives, tradeoffs, and causal rationale. | Why is a transfer streamed? Because the target machine cannot buffer the entire file. |
| **What?** | Observable capability, inputs/outputs, state, invariants, effects, and exclusions. | What counts as a completed inventory transaction, and what must remain consistent? |
| **When?** | Preconditions, triggers, ordering, lifetimes, deadlines, versions, and historical assumptions. | When may a retry occur, and when could it duplicate an irreversible effect? |
| **Where?** | Environment, hardware, locality, deployment, ownership, trust and jurisdictional boundaries. | Where does clinical data reside, and which participant is authorized to read it? |
| **How?** | Current mechanism, dependency roles, protocols, procedures, verification, and recovery. | How does the implementation meet the invariant, and how would a replacement prove it? |

Include **who** as well: owners, users, maintainers, authorities, affected people, and sources of accepted intent.

Capture the reasoning at several scales: whole project, subsystem, interface, critical state transition, and important failure path. Do not describe every incidental implementation detail as a permanent requirement.

A useful record says both “this is how it worked” and “this is why that mechanism existed.” It links to observations and tests. It distinguishes an author's explicit requirement from a future agent's inference.

This semantic corpus is proposed domain content built using the standard's existing distinctions and optional reviewed extensions. The six questions do not silently introduce new mandatory Standard 0.1 fields.

## 5. Possibilities opened by semantic inheritance

### A. Replacement without accidental loss of purpose

A future agent could replace an unavailable runtime, service, or library after finding its capability role and checking a new implementation against its obligations.

For humans, the same records explain which changes are safe and why an apparently unnecessary constraint matters.

### B. Adaptation beyond the original application shape

Any-Shape could attempt different realizations for browser, desktop, mobile, terminal, accessible assistive interfaces, or agent APIs as adapters and evidence permit.

A rendering that looks correct does not establish correct effects. A newly shaped application must still preserve accepted state, permissions, calculations, error handling, and recovery.

### C. Selective rebuilding under scarcity

If only a small machine survives, an agent could identify a narrow essential slice instead of recreating every feature of a large product. It might recover document reading before editing, local records before federation, or a specific engineering calculation before a complete GUI.

Excluded capabilities must remain explicit. A reduced profile must not advertise full historical compatibility.

### D. New combinations across old project boundaries

| Proposed combination | Newly possible workflow | Additional proof needed |
| --- | --- | --- |
| QGIS + GDAL + ERPNext | Plan resource locations and coordinate materials/maintenance. | Coordinate and inventory units, authoritative records, synchronization, and access. |
| KiCad + ngspice + FreeCAD | Design an electrical assembly with a mechanical enclosure. | Electrical performance, physical fit, component availability, and manufacturing checks. |
| GNU Radio + Mosquitto + Node-RED + local records | Observe equipment or environmental sensors and record events. | Calibrated signals, device identity, timing, loss handling, and controlled effects. |
| Kiwix + Tesseract + MediaWiki + Moodle | Recover manuals, curate knowledge, and teach repair skills. | Source fidelity, correction, content rights, versioning, and instructional review. |
| OpenMRS + DHIS2 | Connect scoped clinical information to population reporting. | Clinical meaning, privacy, indicator validity, authorization, and independent domain review. |
| SciPy + OpenModelica + FreeCAD | Analyze a physical system and develop a proposed component. | Valid models, units, tolerances, measured evidence, and physical validation. |
| Chromium + Puck + inherited business capabilities | Deliver an editable interface adapted to surviving devices. | State/effect equivalence, accessibility, security, and resource budgets. |

These are research opportunities, not implemented integrations or evidence that arbitrary systems compose automatically. Interface matching alone does not reconcile incompatible concepts.

### E. More than one valid successor

A preserved purpose may admit many implementations. One successor could favor energy efficiency; another clarity and repairability; another compatibility with surviving hardware.

The invariant is the accepted promise within its chosen profile. Diversity is legitimate where the contract allows it. Changed requirements need explicit decisions and migration evidence.

### F. Knowledge transfer between people and agents

A person can study why a design exists, challenge its assumptions, learn from its failures, and propose a better successor. Agents can trace the same evidence mechanically.

The inheritance must remain readable without a proprietary model or vendor. Canonical plain UTF-8 JSON, narrative explanations, examples, and independent fixtures support both audiences.

### G. Repeated renewal across generations

A recovered implementation can add discoveries, verified fixes, new constraints, and migration evidence to the archive. Later generations inherit a clearer corpus.

Newer records must retain provenance and contradictions. A successful successor does not retroactively make every decision it took authoritative.

The possibilities are open-ended because purposes can be recombined and realized differently. They are bounded by information, evidence, resources, rights, physical reality, and the completeness of the inherited contracts.

## 6. A worked example: preserve the reason for a retry

Suppose an old application uploads an inspection report and retries after a network interruption.

Source may show a loop. A superficial extraction may record “supports retry.”

A useful inheritance records:

- **Why:** field workers face unreliable connections.
- **What:** one logical submission must create one accepted report.
- **When:** retry only under defined conditions; completion and cancellation have explicit meanings.
- **Where:** the device and receiver may be offline independently.
- **How:** stable submission identity, server deduplication, durable local state, and recovery tests.
- **Who:** the worker may submit; the receiving organization owns acceptance policy.

An agent can then invent another mechanism while preserving the actual purpose. Reproducing the loop without understanding duplication could produce a functioning interface that corrupts institutional records.

This illustrates why behavioral, contextual, and causal inheritance expands useful freedom: it tells a successor both what must remain and where invention is allowed.

## 7. The archive around the fifty

Each subject needs source, history, known-working binaries, toolchains, transitive dependencies, accepted contracts, executable fixtures, offline documentation, data formats, migration procedures, legal provenance, and a tested bootstrap path.

Also preserve:

- Model weights and tokenizers where inference is required.
- Maps, coordinate definitions, observations, and scientific reference data.
- Component libraries, datasheets, device databases, and fabrication knowledge.
- Fonts, language resources, curricula, medical concepts, and manuals.
- Cryptographic recovery material under appropriate custody.
- Hardware descriptions, drivers, firmware rights, and energy/resource assumptions.

The selected projects do not produce missing information automatically. Kiwix without content is not an encyclopedia; a simulator without a valid model is not reliable physical knowledge.

There are major uncovered areas: full semiconductor fabrication, complete industrial process design, specialized civil/structural engineering, agriculture, modern telecommunications operations, and many scientific disciplines. Domain libraries and knowledge archives improve reach, but this document does not count that as complete capture.

## 8. Legal and economic continuity

This is a continuity portfolio, not an all-permissive proprietary-product list. The selection includes permissive, copyleft, and mixed-license projects. Preserve the exact revision's applicable licenses and obligations before extraction or distribution.

Language conversion and semantic reimplementation do not automatically remove rights in adapted code. Separately assess code, data, documentation, model weights, assets, patents where relevant, trademarks, enterprise modules, and distribution mode. FFmpeg's build configuration and enabled components, for example, affect its licensing situation.

Free and lawful commercial use is possible under many open-source licenses; the conditions differ. The document does not certify every combination or promise zero legal risk.

Commercial possibilities include supported recovery packages, industry systems, migration services, offline installations, maintained adapters, and verified integration. Profitability remains a hypothesis. No one should mistake preservation breadth for demonstrated demand.

## 9. How to test whether these fifty were good choices

Define a weighted capability matrix before comparison: software production, communication, storage, knowledge, human access, science, engineering, health, education, logistics, media, and observability.

For each candidate, record marginal coverage, dependency cost, archive size, hardware requirements, legal obligations, recovery difficulty, and overlap. Compare alternatives under the same archive and compute budget. Include package preparation/maintenance costs.

Run independent offline cold-agent and human-assisted trials:

1. Recover one useful capability on a declared surviving machine.
2. Remove a historical dependency and reconstruct its role.
3. Change one language, runtime, interface, or deployment where the target permits it.
4. Restore real data and test negative/failure cases.
5. Combine two projects and test their cross-boundary behavior.
6. Compare source-only, ordinary documentation, and semantic-inheritance conditions with matched underlying resources.
7. Measure time to verified capability, intervention count, fidelity, data survival, resources, and unresolved unknowns.
8. Publish failures and revise the portfolio from evidence.

Use held-out acceptance cases and independent evaluation. No amount of descriptive completeness makes a missing test pass. A fifty-project manifest is a research plan; a validated recovery corpus must earn its coverage claims.

## 10. The proposition

**If we could preserve only fifty major projects deeply, we would choose these fifty as a broad starting portfolio for recovering modern digital capabilities and the engineering tools that help sustain them.**

Their lasting value would arise from preserving not only implementations, but purpose, context, causal understanding, permissible change, relationships, and proof.

Forever Works should let future humans and agents understand what must survive and why. Any-Shape and other tools could help them construct forms suited to their circumstances.

The goal is an inheritance from which many futures remain possible.

## Related work and upstream evidence

- [If We Had to Start Again](IF_WE_HAD_TO_START_AGAIN.md)
- [Inheritable Software Ecosystem](INHERITABLE_SOFTWARE_ECOSYSTEM.md)
- [Fifty-App Inheritance and Any-Shape Research](../RESEARCH/FIFTY_APP_INHERITANCE_AND_ANY_SHAPE.md)
- [Selective Reconstitution](../PROPOSALS/SELECTIVE_RECONSTITUTION_CAPABILITY_EXTRACTION.md)
- [Contractual Fixity, Implementation Fluidity](../PROPOSALS/CONTRACTUAL_FIXITY_IMPLEMENTATION_FLUIDITY_LINUX_ABI.md)
- [Composable Software Ecosystems](../PROPOSALS/COMPOSABLE_SOFTWARE_ECOSYSTEM_CONTRACT.md)

Project links in the tables identify upstream discovery sources, not preserved snapshots. Supporting descriptions include [OpenModelica's stated modeling/simulation scope](https://openmodelica.org/), [ngspice's simulation documentation](https://ngspice.sourceforge.io/docs.html), [Mosquitto's MQTT scope](https://mosquitto.org/), [DHIS2's source and licensing information](https://github.com/dhis2/dhis2-core), and [MediaWiki's purpose](https://www.mediawiki.org/wiki/Manual:What_is_MediaWiki%3F). Extraction must retain versioned local copies of the evidence actually relied on.
