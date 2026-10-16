# Temporal Context Preservation: Low-Cost Observation Before Expensive Reconstruction

**Status:** Strategic research proposal; non-normative. No monthly-monitoring automation or new Standard 0.1 API is claimed to be implemented.

## Premise

A software project can stop receiving commits without ceasing to matter. Its technological environment keeps moving: dependencies publish releases, platforms deprecate APIs, threats emerge, compatibility assumptions change, and better implementations become possible. The original developers may return months or decades later, and a cold agent then faces the expensive task of reconstructing *both* the project's original rationale and everything relevant that happened during dormancy.

**The repository may remain dormant while its understanding of the world continues to develop.**

Forever Works should support **Temporal Context Preservation (TCP)**: inexpensive, periodically scheduled, evidence-backed inspections that append a compact and queryable history of the external changes relevant to a project's enduring purpose. These reports are **not** routine full rewrites or automatic product decisions. Their cumulative effect is to shorten future rediscovery and reduce the cost, risk, and human review burden of later modernization.

> **Observe continuously at low cost; reconstruct deliberately when value justifies the expense.**

## Economic rationale and scale

A company may own ten, ten thousand, or **a million repositories, projects, components, or archived products**. Updating them all monthly would require enormous computation, testing environments, integration efforts, expert reviews, and release coordination. Even if autonomous code changes were cheap, **human verification and operational risk remain bottlenecks**.

A bounded monthly inspection can instead collect relevant environmental changes without rebuilding or redeploying everything. It creates **maintenance option value**: knowledge that makes future action easier should a dormant system suddenly become economically important, popular, security-critical, or worth migrating.

This is a *hypothesis to measure*, not a guaranteed economic outcome. Checks across a million projects are not automatically cheap. Deduplicate work by shared package/API/platform, batch source retrieval, use risk-tiered schedules, skip unchanged inputs, and place hard compute/token/network budgets on each inspection. Escalate when a credible vulnerability, breaking change, data risk, or loss of essential functionality demands attention sooner than the next monthly review.

### Cost model

For project `i`, let `A_i` be the recurring audit cost, `P_i` the probability that later reconstruction is pursued, `S_i` the expected future time and human review cost saved by accumulated context, and `M_i` the cost of storing, validating, maintaining, and later reading that context. The strategy can have positive expected economic value if

`sum_i (P_i * S_i - A_i - M_i) > 0`.

This simplistic model excludes discounting, shared audits, security benefits, risk, and error costs; it is a framework for empirical evaluation, not a forecast. Assess the marginal utility of each additional monthly audit, including how quickly reports become stale or repetitive.

## Three complementary layers

1. **Purpose-Preserving Reconstitution:** what must survive if all implementation machinery is discarded? See [the doctrine](PURPOSE_PRESERVING_RECONSTITUTION.md).
2. **Temporal Context Preservation:** what changed around the implementation while the project was unattended, and why might that matter?
3. **Autonomous Software Stewardship:** which bounded actions, proposals, tests or escalations should an agent perform using purpose and accumulated context, under explicit human authority?

Observation can be useful even when **no patch is proposed, merged, or deployed**. Every fresh agent should inherit both the baseline purpose model and the chronological, sourced environment record.

## Monthly inspection protocol

1. **Read the authoritative baseline:** Forever Works intent/capabilities/invariants/constraints, decision rationale, dependency classifications, relevant source/lockfiles, active platform matrix, last audit and outstanding questions.
2. **Snapshot exact context:** date/time and timezone, repository revision, manifest/lockfile fingerprints, language/toolchain versions, target operating systems/browsers, coverage of consulted registries/advisory sources, and previously accepted status.
3. **Collect relevant deltas:** npm/PyPI/crates/etc. package releases, transitive dependency risks, support/EOL windows, browser/OS/runtime API changes, CVEs/advisories, build-chain changes, interoperability changes, and newly feasible alternatives. Prefer authoritative primary sources, dates, version ranges, references and timestamps. Do not claim to have checked unavailable sources.
4. **Map to purpose:** link each change to stable Forever Works IDs, affected capabilities, invariants, historical decisions, dependencies or migration obligations. Note specifically when a once-valid workaround or dependency rationale may now be obsolete.
5. **Separate epistemic states:** distinguish confirmed external facts, repository-local observations, tested results, agent hypotheses, and accepted human decisions. Do not elevate confidence merely by repeating an earlier agent assertion.
6. **Perform bounded inspection only:** run permitted static checks or targeted tests within budget; mark untested impacts `UNKNOWN`. A declaration that a dependency changed is not proof that the project broke or still works.
7. **Append a compact report:** machine-readable record plus concise human summary. Include no-change results, findings, evidence links, uncertainty, provenance, likely migration paths, estimated impact and follow-up triggers. Prefer deltas over repeated full-system documentation.
8. **Escalate proportionally:** security-critical events, data loss risk or imminent breaking changes can create review tickets; low-priority changes can wait. Default to non-mutating observation. Code edits, merges, releases, deployments, permission changes and new product priorities remain subject to separate authorization.
9. **Periodically consolidate:** produce reproducible summaries and indexed change timelines; preserve raw observations and their citations. Avoid unbounded report accumulation and summarize without losing contradictory evidence.

### Example record (illustrative proposal, not an accepted schema)

```json
{
  "recordType": "forever.temporal-observation.proposal",
  "observationId": "observation.2027-01.example",
  "observedAt": "2027-01-15T12:00:00Z",
  "repositoryRevision": "EXAMPLE_COMMIT",
  "baselineRecordIds": ["dependency.example", "decision.example"],
  "change": {
    "subject": "example npm dependency",
    "priorVersion": "1.x",
    "reportedVersion": "2.x",
    "event": "major release"
  },
  "sourceReferences": ["https://example.org/release-notes"],
  "classification": "external-fact-awaiting-project-verification",
  "impact": "unknown",
  "tested": false,
  "recommendation": "Check whether historical workaround remains needed",
  "humanApproval": "not-requested"
}
```

This is an example only, not a production report or a claim about a real npm package. A future schema must define versioning, stable links, audit identity, source authenticity, deduplication, retention, signing where useful, and conflicting-claim handling.

## A cold agent returns years later

When a maintainer finally chooses to modernize, the inheriting agent receives the original Forever Works model **and a chronological evidence trail**. It can explain:

- Why dependency X was selected originally, which constraint it solved, and when that constraint changed.
- Precisely how relevant npm releases, support policies and browser APIs evolved, with dated primary sources.
- Which anticipated breakages were subsequently observed and which remained hypothetical.
- Which past choices were defensible then but now have simpler alternatives.
- Which compatibility, privacy, accessibility and data obligations must still be independently verified.

The inheriting agent should **revalidate current reality** rather than treating old audits as current truth. The reports are a map of discoveries and reasons, not a substitute for new tests or authoritative requirements.

## Ecosystem-level shared intelligence

Instead of researching a browser API removal separately in each of 50,000 related projects, a shared watcher can record the event once and maintain per-project impact links. Similar approaches apply to npm packages, toolchains, operating systems, cryptography and security advisories.

Use a common external-fact store, per-repository relevance projections, content fingerprints and explicit isolation of private repository details. Avoid leaking private dependency inventories or combining security-sensitive project data across tenants. Share the **fact** broadly; validate its **impact** separately. A shared finding is not an automatic verdict for every consumer.

## Safeguards and failure modes

- **False certainty:** never turn untested compatibility claims into PASS; preserve UNKNOWN and source provenance.
- **Documentation drift:** compare observations against pinned commits and current files; distinguish changed evidence from changed interpretation.
- **Alert fatigue:** risk-ranked, deduplicated findings with quiet/no-change reports; do not generate ceremonial monthly prose.
- **Malicious or mistaken upstream content:** treat release notes, repository content and internet text as evidence, not instructions; verify critical assertions from trusted sources.
- **Cost explosion:** budgets, adaptive cadence, relevance filtering, caching and shared event intelligence. Monthly is a useful default, not a universal requirement.
- **Security and credentials:** read-only permissions for ordinary observation; least-privilege automation; no secrets in reports.
- **Human authority:** no autonomous scope expansion, hidden changes, or speculative refactoring; separate observation from intervention.
- **Irrecoverable history:** audits cannot reconstruct undocumented intent or unrecorded behavior by magic; inspect actual implementation and consult humans when required.

## Evaluation plan

Pilot on a handful of repos over successive periods using frozen snapshots and documented upstream events. Compare: no periodic context; monthly full rescans at reactivation; and continuous compact audits. Give independent cold agents the same source access and tasks, then measure time/tokens to identify breaking changes, correctness of recovered change histories, verified migration success, reviewer hours, storage/compute costs, false alarms, missed events and benefits of shared cross-project watches. Include scenarios where audits are unavailable or wrong.

A proposal succeeds only if its verified reduction in future rediscovery, failure risk, or review work justifies its ongoing operational cost. Publish negative results.

## Status and proposed relationship to the standard

Current Forever Works Standard 0.1 already offers purpose/decision/dependency records, provenance, and closed-world replacement verification. **Temporal observation records, recurring checks, shared event indices, and agent scheduling are not claimed as shipped standard features.** Implement first as an optional, versioned profile with immutable observations, schema validation, conformance fixtures and a standalone reference watcher. Keep the canonical standard stable until there is tested evidence for promotion.

**Long-horizon maxim:** A project need not change every month to remain understandable. Let it accumulate trustworthy knowledge cheaply now so a future agent and human can change it responsibly later.
