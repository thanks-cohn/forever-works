# Agent query protocol

The query contract is transport-independent: `getProjectIntent`, list operations, `getEntity`, `traceEntity`, `explainDependency`, dependency classification filters, `validateModel`, `evaluateReplacement`, and `verifyMigration`. CLI JSON is the lowest-common-denominator adapter: stdout contains one JSON value; diagnostics and nonzero status indicate errors. Understanding, planning, verification, and mutation are separate authorities. No transport is canonical.
