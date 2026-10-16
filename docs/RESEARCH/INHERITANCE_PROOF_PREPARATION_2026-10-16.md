# Bounded independent inheritance proof preparation

Status: implemented reference preparation, not a core edition or independent consumer
result. Stage A passed hosted run 38897739593 before producer implementation began.
Runnable producers, exporter/validator, frozen packages and a separated evaluator now
live in examples/inheritance. The source-aware author must not act as the cold consumer;
construction remains NOT_RUN. The original bounded design below remains contextual;
use examples/inheritance/HANDOFF.md for the delivered operator setup.

## Proposed bounded producers

A local catalog owns stable item identities, titles, tags, opaque metadata and revision
conflicts. A separate local object store owns immutable bytes and content identity.
They run independently, persist state and use distinct synthetic authorization grants.
Neither infers permission from model provenance or metadata. No paid service, real
credential, personal data or source-product network fetch is needed.

Use existing intent/capability/invariant/decision/implementation/evidence records to
explain each producer, backed by exact public JSON/HTTP contracts and examples. Link
rationale to replaceable SQLite/HTTP mechanisms. Make partial cross-product failure
explicit: storing content and updating a catalog are not one atomic transaction.

Freeze only allowlisted public documentation, core schemas, model records and portable
acceptance examples. The manifest records package version, every file's SHA-256,
allowed references/dependencies and known unknowns. Do not export service source,
private state, checkout paths, environment files or evaluator-only cases. Package
integrity and cross-link checks cannot establish semantic sufficiency.

## Fresh-session objective

Create a useful complementary product that works with both documented systems and
preserves their contracts. Choose its user workflow and interface; explain the inherited
requirements and new decisions. Provide a documented acceptance adapter so an evaluator
can exercise your workflow without inspecting the original producers' source.

Inputs: frozen documentation packages, declared public platform references, ordinary
toolchain, explicitly permitted test services and synthetic scoped grants. No original
repositories, this source-aware conversation, hidden coaching or evaluator artifacts.
Record all questions, interventions, missing facts and failures.

## Access and evaluation

The machine-readable access plan is `evidence/inheritance-access.json`. Enforce it in
a separate disposable container/VM/session: mount only frozen packages read-only and
consumer work output writable; do not mount the host or checkout; deny additional
filesystem access; allow only the two reference service endpoints and declared public
references. Keep original source/state and evaluator files outside that mount namespace.
A separate directory in this unrestricted workspace is not isolation.

The evaluator uses published obligations but held-out values/orderings: interact with
both originals, preserve IDs/tags/opaque metadata and exact numeric values, respect
distinct read/write grants, retry after an unknown commit outcome, detect conflicting
updates, restart producers and round-trip exported state. Test actual effects through
the running services. A consumer build, valid package or supplied PASS is insufficient.

Producer startup/reset/seed scripts, frozen exports, clean package-consumption smoke,
separate evaluator and container launch configuration have been implemented and
reference-tested after hardening passed. A genuinely fresh restricted consumer has
not run; construction is NOT_RUN. If restrictions cannot be enforced, downgrade the trial rather than count
this source-aware preparation as success. No commercial-demand claim follows.
