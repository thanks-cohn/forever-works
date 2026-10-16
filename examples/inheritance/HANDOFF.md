# Fresh restricted consumer handoff

Construction status: NOT_RUN. The source-aware author prepared fixtures and tested
reference behavior; it must not be counted as the fresh consumer.

Objective: create a useful complementary product that works with Catalog and Objects
and preserves their published contracts. Choose and explain its actual user workflow,
interface and additional value. Do not merely copy source products. Separate inherited
requirements from new proposals; commercial improvement is an untested hypothesis.

1. Freeze and verify `frozen/index.json` and both package manifests. Record their hashes,
   source revision, toolchain/image digests, permitted references, grants, time budget
   and intervention rules before construction. Keep a questions/interventions log.
2. Operator supplies four distinct synthetic grants using CATALOG_READ_GRANT,
   CATALOG_WRITE_GRANT, OBJECTS_READ_GRANT and OBJECTS_WRITE_GRANT. Do not use real
   credentials. Build/start `docker compose -f examples/inheritance/compose.yaml up -d
   --build`. Consumers use http://catalog:8080 and http://objects:8080 only. Scope each
   evaluation request explicitly; held-out evaluation can rotate grants.
3. Attach a genuinely new agent/session with only execution inside the consumer
   container. Its inputs are `/packages`, ordinary toolchain, the declared public
   references (prefetched/hashed if needed on the internal network), this objective,
   the public adapter contract, endpoint configuration and explicitly scoped grants.
   Copy this handoff/adapter contract as operator-approved construction inputs; never
   mount the repository/evaluator or forward this source-aware conversation.
4. Disable host filesystem, GitHub/source connectors, undeclared browsers/network tools
   and other sessions that could read originals. Preserve only `/consumer` output and
   declared service access. The container has read-only root/packages, a private work
   volume, no Docker socket, no host mounts and an internal network; the operator must
   also enforce the agent-tool restrictions. Directory separation alone is insufficient.
5. Consumer publishes its own behavior/decisions, runnable product and documented
   acceptance adapter (the argv command reads a JSON request and returns a JSON result).
   Keep unresolved facts visible; do not coach missing producer knowledge invisibly.
6. An independent operator runs evaluator/evaluate.py with primary/clean endpoint and
   grant files, a trusted restart hook and the consumer adapter argv or HTTP endpoint. It checks real effects, exact metadata/content, identity,
   least authority, response loss/retry and conflicts. Independently restart/reset test
   instances and import the consumer's exported original documents into clean stores,
   checking stable IDs and byte preservation. These obligations are published, while
   values and fault orderings are held out. Record actual run outputs and interventions.
7. Export consumer outputs without revealing evaluator-only source. Shut down only this
   experiment's containers; remove its volumes only after preserving required evidence.

If tool/mount/network separation cannot be enforced, label the construction trial
NOT_RUN or compromised. Package integrity, a successful build, producer test results,
a reference adapter or a supplied PASS do not prove independent consumer success.
No commercial demand or universal documentation sufficiency follows from one trial.

For a separate private evaluator container, enable Compose profile `evaluation`.
It mounts only its own control volume and has no listener except a temporary declared
fault proxy. Use `--adapter-url http://consumer:<port>/<acceptance-path>` and
`--proxy-bind 0.0.0.0 --proxy-host evaluator`; the consumer receives that proxy endpoint
in the authorized case. Supply separately operated clean reference instances and a
trusted lifecycle hook that returns after the primary producers restart and are ready.
These control/evaluator artifacts stay outside `/packages` and `/consumer`. The hook
is operator configuration, never a command taken from an inherited document. The
independent evaluator reports that isolation itself still requires access evidence.
