# Small real inheritance proof fixtures

Experimental optional examples, not new core requirements. Catalog owns mutable
metadata/revisions; Objects owns immutable content identities. Two processes, two
SQLite databases and distinct grants make partial effects/authority observable. They
share a reference runtime implementation; they are not independent semantic bindings.

From the repository root, using Python standard library plus the local core binding:

```sh
python3 examples/inheritance/run.py start --state work/inheritance-state --ready work/inheritance-ready.json
# In a second terminal:
python3 examples/inheritance/run.py seed --ready work/inheritance-ready.json
# Stop the first command before resetting:
python3 examples/inheritance/run.py reset --state work/inheritance-state
PYTHONPATH=bindings/python python3 examples/inheritance/test_producers.py
```

Each producer can also run independently with its documented `server.py --state ...
--port ...` entry point and `PYTHONPATH=bindings/python`. Only synthetic state/grants;
no paid infrastructure, personal data or production credentials. Default bind is
loopback. Reset refuses unmarked directories and only removes named fixture databases.

## Documentation packages

`public/catalog` and `public/objects` contain allowlisted public contracts, examples,
source-aware reference observations and standard model graphs. After a coherent producer
commit, export a new immutable destination:

```sh
python3 examples/inheritance/export_packages.py --out work/inheritance-export
python3 examples/inheritance/export_packages.py --validate work/inheritance-export/catalog
python3 examples/inheritance/export_packages.py --validate work/inheritance-export/objects
```

`frozen/` is the delivered snapshot, with per-file hashes, package manifest hashes,
source revision and explicit references/dependencies. No original producer `.py` source,
private state, host paths or evaluator cases are exported. Validation detects integrity,
model/reference and documentation link problems; semantic sufficiency remains UNKNOWN.
Do not overwrite a frozen package or regenerate expected outputs to hide a failure.

## Evaluation and separation

`evaluator/evaluate.py` contains held-out published-obligation cases. Source-aware
reference tests cover both stores, opaque metadata/precision, distinct/read-only grants,
a lost committed response, retries, conflicts, restart and clean-store round trips.
They are not an independently constructed third product. The public acceptance adapter
contract is `evaluator/adapter-contract.md`; it specifies observable obligations while
leaving the consumer's useful product/workflow/interface to the fresh agent.

See HANDOFF.md for a fresh restricted session. `compose.yaml` separates producer source
and state from a consumer image containing only ordinary Python, read-only frozen
packages and its own writable output volume. The network is internal; no host socket,
source checkout or evaluator files are mounted into the consumer. Disable all other
agent tools/connectors to original sources. A container alone does not restrict an
agent that also retains host tools. No fresh-agent construction is claimed here.
