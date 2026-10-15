# Contractual Fixity, Implementation Fluidity
## Linux ABI Inheritance, Cross-Language Reconstitution, and Regenerative Software

**Status:** research proposal and architectural principle, **not normative Standard 0.1**, not a proof of full Linux compatibility. **Research subject:** Linux-compatible userspace behavior, illustrated by the Zig-based Morphic/Alpz experiment in `thanks-cohn/zig-reference`. **Applicability:** deliberately general to every kind of software; Linux is a demanding illustrative case, not a special case baked into Forever Works.

## Central thesis

A software system can retain its **identity and required external promises** while its implementation language, algorithms, internal topology, framework, hardware accommodations and component boundaries change. Forever Works should preserve the *necessary invariants* and accepted compatibility contracts, along with purpose, relationships, evidence, historical decisions and explicit replacement freedom. A cold agent should be able to consume that inheritance and construct a different implementation, including one in a different language, without having to transliterate or import original code.

**Contractual fixity, implementation fluidity:** preserve what must remain true; permit everything else to evolve subject to declared constraints and independent proof.

The bold working hypothesis is that **once a sufficiently precise Linux ABI compatibility envelope and its behavioral obligations are understood and preserved, the implementation behind it becomes a design choice, rather than a binding inheritance**. “Just a choice and a step” expresses architectural freedom, **not** that choosing and engineering a safe kernel are trivial. Re-creating compatible scheduling, memory, synchronization, filesystems, process semantics, devices and error behavior remains a formidable undertaking. A syscall number table alone is not a complete ABI contract.

## 1. The three-layer separation

1. **Purpose and identity:** WHY the system exists, which workloads and people it serves, what usable capabilities the system promises, and the meaning of its connections to other software.
2. **Compatibility envelope and invariants:** WHAT *must* endure under an explicitly chosen target (e.g. Linux userspace ABI on RV64 under a specified release/userspace workload), including application-observable behaviors, security boundaries, state transitions, error codes, concurrency and resource lifetimes, and independently measurable acceptance obligations.
3. **Replaceable realization:** HOW the system is implemented in one generation: Zig, Rust, C, other future languages; monolithic vs microkernel composition; virtual memory internals; scheduler structures; internal object layouts; source organization; toolchains; deployment topology. These choices can change where a required invariant does not constrain them.

The same element may be fixed in one **compatibility envelope** and variable in another. No global “Linux forever means one historical version, architecture or syscall catalog” assumption is acceptable. Pin ABI architecture, word sizes, calling conventions, syscall semantics, userspace assumptions, versions, profiles and known exceptions. Expose multiple simultaneous or alternative compatibility envelopes.

## 2. The variation contract

Each accepted property receives a carefully scoped disposition:

| Classification | Semantics | Example |
| --- | --- | --- |
| **Fixed invariant** | MUST endure for the selected environment and target consumers | Architecture-specific syscall calling convention; specified results/errors; protection against userspace violating kernel memory |
| **Constrained variation** | MAY change only while the declared behavioral, security, performance or interoperability bounds remain satisfied | Scheduler implementation may differ, but exposed scheduling semantics and fairness/priority obligations must still hold |
| **Free mechanism** | MAY be reinvented or replaced; no equivalence claim for the internal mechanism is needed | Zig-specific data structures, internal allocator strategy, repository layout or build language unless separately constrained |
| **Explicitly changed obligation** | A change to a former invariant requires a new/reviewed compatibility envelope, migration rationale and evidence; never silently relabel it “fluid” | Removing a formerly supported syscall or changing a persistent ABI behavior |

Every classification must include provenance, rationale, owners of the claim, affected dependents and an evidence strategy. Unknown or disputed properties remain **UNKNOWN**, not implicitly free. Environmental assumptions and timing/concurrency nondeterminism must be recorded, not swept into “same output.”

## 3. Linux compatibility as a stringent inheritance experiment

Linux is an unusually revealing reference because enormous bodies of userspace code depend upon its ABI. The goal is not simply “convert C into Zig” or “rewrite Zig into Rust.” Rather, extract and preserve the commitments that make Linux-compatible userspace function and let future generations implement those commitments differently.

A Linux ABI envelope can include, as applicable:
- target architecture, calling convention and syscall IDs, arguments, structures, alignment and data layouts;
- process creation, exec, termination, parent/child relations, signals and threading;
- user/kernel memory boundary, address-space behavior, mmap and atomic user copy;
- file descriptors, open/read/write/close/dup, offsets, pipes, blocking, ownership, EOF and errors;
- filesystem path resolution, namespaces, permissions and persistence;
- synchronization, scheduling-visible promises, memory ordering, wakeup and interruption;
- dynamic ELF loading, auxiliary vectors, userspace entry stack, libc/runtime expectations;
- device, terminal, networking and observable `/proc`/`/sys` behavior when required by the chosen workloads;
- concurrency, failure, resource exhaustion and security invariants;
- explicitly known implementation-specific quirks relied upon by consumers.

Do not assume that running one BusyBox command proves all Linux semantics. Coverage should be indexed by interfaces, scenarios, negative cases and confidence, so a cold agent can distinguish **demonstrated**, **specified**, **inferred**, **unknown** and **not implemented**.

## 4. Real reference: Morphic / Alpz in Zig

The project `https://github.com/thanks-cohn/zig-reference` provides a real experimental candidate and historical progression. Its README reports a **Playable Alpine** acceptance milestone for Alpine v3.22.0 RV64 under QEMU 8.2.2, including persistent dynamic musl/BusyBox shell, real external execution, file read/write/read-back, a pipeline carrying bytes between processes, and parent-shell continuation. The repository explicitly says this is research rather than a production-complete Linux implementation. These claims were inspected in its public documentation and **have not been independently rerun as part of this proposal**.

This offers evidence that selected Linux userspace-facing behavior can be implemented by markedly different internal machinery. It does **not** yet prove:
- full Linux ABI equivalence;
- portability of the complete design to Rust or any other language;
- that a Forever Works inheritance package already contains all required meaning;
- that a cold agent has reconstructed that subsystem from the inheritance package; or
- that reconstructing an entire kernel would be rapid or inexpensive.

The precise research opportunity is to turn real iterative evidence—WHY each syscall or subsystem mattered, WHAT observable behavior was earned, which invariants survived each repair, and HOW another implementation could achieve it—into a reusable, implementation-independent inheritance corpus.

## 5. Granularity: total-system knowledge without a bloated core

The ambition is to **semantically inherit an entire Linux-compatible system**: recursively from whole-system purpose to subsystems, interfaces, state transitions, error branches and hardware constraints. Complete semantic coverage is a target, not a factual assertion. Represent it as a modular, content-addressed graph with cross-layer links, stable identifiers, revisions and uncertainty reports.

A cold agent should be able to ask at any scale:
- What is this responsible for and why?
- What behavior is promised to callers?
- Which aspects are fixed, conditionally variable or free?
- What other participants/subsystems rely on these promises?
- Which proof demonstrates each claim and under what environment?
- Which source observations conflict with accepted intent or other evidence?
- What remains undiscovered?
- What changes are safe, and which require a new compatibility profile?

The core Forever Works standard must remain small and general. Detailed ABI/syscall machinery belongs in an **optional versioned compatibility-envelope profile**, not as mandatory kernel fields in every application record. The same profile principles should serve browser APIs, desktop app data formats, interservice protocols, CLI behavior and whole-product suites.

## 6. Cold-agent reconstruction protocol

1. **Fix the target envelope:** pin a Linux ABI architecture/workload and a reproducible reference kernel/userspace environment; specify scope and exceptions.
2. **Extract:** analyze source, documentation, design/history and actual reference execution; isolate claims by provenance, confidence and revision. Extract not just code structure but causal purpose and external semantics.
3. **Review:** distinguish observation, inference and accepted obligation; identify what must endure, what is constrained and what is genuinely replaceable.
4. **Package:** emit an agent-neutral modular Forever Works inheritance corpus with ABI profile, precise subsystem/interface records, topology, proof requirements, accepted decisions and unresolved gaps. Keep original Zig/C implementations as archived evidence but do not require the reconstructing agent to read them in the blinded experiment.
5. **Reconstitute:** give a cold agent the package and a specification requesting a different language or architecture (e.g., Rust); permit first-principles replacement choices behind the envelope.
6. **Independently evaluate:** run held-out ABI, negative/error, concurrency, security, integration, real QEMU and userspace workload tests; do not count compilation as functional equivalence.
7. **Compare controls:** run source-only, ordinary-documentation and Forever Works inheritance conditions at comparable budgets; measure missing information, corrections, cost/time, compatibility coverage and new defects.
8. **Evolve:** archive new implementations, decisions, regressions and newly discovered obligations as additive historical evidence; retain the accepted compatibility baseline while allowing explicit profile revisions.

Begin with one well-bounded completed subsystem, e.g. pipe/file-descriptor lifetime semantics from the Zig project, then test two interdependent subsystems, then progressively wider userspace compatibility. A userspace mock cannot prove a bootable kernel.

## 7. Compositional and cross-generation continuity

The contract is not restricted to a single binary or a direct translation. One historical subsystem may be split into multiple services, several components consolidated, or entirely new hardware abstractions introduced. Whole-system invariants and **relationships between parts** (authority, state ownership, error propagation, synchronization, lifecycles) must remain preserved, explicitly altered, or declared unsupported. The independent composable-ecosystem profile should provide these semantics without imposing a central coordinator or a particular topology.

Possible lineage:

`Linux C reference → accepted semantic corpus → Zig-compatible implementation → renewed corpus → Rust-compatible implementation → future implementation`

No particular generation is canonical merely because it was most recently built. Newer implementations may reveal more accurate understanding of prior behavior and expose new deviations; record the evidence and review rather than silently rewriting history.

## 8. Relationship to Any-Shape and specifications.json

**Forever Works** preserves accepted engineering meaning, claims, provenance, constraints, permitted variation and proof across implementation generations.

**Any-Shape** accepts evidence and `specifications.json` requests, uses source/target adapters to plan and attempt the desired realization, and verifies artifacts. A job could request: “Using this Linux/RV64 ABI compatibility envelope, implement a Rust kernel subsystem; preserve these user-visible behaviors, allow all other mechanisms to change, and evaluate against these held-out tests.” The request file is not the immutable inheritance itself, and importing a project does not make its spec authoritative.

This is one application of the larger universal premise: extension→desktop, desktop→mobile, Python helper→browser extension, arbitrary multi-participant suite, or C/Zig kernel→new-language kernel all obey the **same separation of meaning, permissible transformation and proof**.

## 9. What would count as strong evidence?

- One new-language implementation of a selected Zig subsystem passes independent held-out real-behavior tests **without consulting the original Zig implementation during reconstruction**.
- Several interoperating subsystems collectively pass tests whose correctness depends on their interactions.
- Clear per-requirement explanation and negative evidence; no inferred PASS.
- Better or comparable fidelity with reduced time/human corrections in controlled experiments using the inheritance corpus.
- Demonstrated ability to change internal architecture or implementation language while preserving the accepted ABI envelope.

Anything less is useful preliminary evidence, not a claim of technological immortality. “Regenerative software” or “technological immortality” names the **long-term aspiration**: successive implementations can perish or become obsolete without necessarily extinguishing the preserved ability to reconstruct functionality.

## 10. Research principle and next actions

**Preserve what must survive. Allow everything else to evolve. Prove that the replacement still fulfills the accepted purpose.**

Next actions: (1) develop an optional compatibility-envelope and permitted-variation profile with JSON Schema and conformance examples; (2) include this among the small, heterogeneous Forever Works teaching cases; (3) select a bounded `zig-reference` capability with verifiable QEMU evidence; (4) test cold-agent reconstruction into a different implementation language; (5) revisit generic profile semantics in response to observed gaps. Avoid bloating normative Standard 0.1 or confusing the Linux example with the general mission.

### Related records

- `docs/STANDARD.md` (normative Forever Works 0.1)
- `docs/PROPOSALS/COMPOSABLE_SOFTWARE_ECOSYSTEM_CONTRACT.md`
- `docs/PROPOSALS/SMALL_REFERENCE_CORPUS_AND_COLD_AGENT_LEARNING.md`
- `https://github.com/thanks-cohn/zig-reference`
- `https://github.com/thanks-cohn/any-shape`

**Bottom line:** The Linux ABI is a possible *stable boundary*, and the kernel behind it can be a *fluid implementation*. A sufficiently precise, independently checked inheritance corpus could make changing programming languages or internal designs a repeatable engineering decision rather than a loss of identity; constructing and proving the implementation nevertheless remains real engineering work.
