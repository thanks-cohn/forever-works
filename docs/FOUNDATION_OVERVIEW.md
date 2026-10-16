# Where to start

Forever Works exists to preserve software's purpose and reasoning while mechanisms
change. Begin with [the small newcomer path](GETTING_STARTED.md): one intent, a few
invariants, one dependency rationale and evidence links are useful without exhaustive
modeling.

| Question | Entry point |
| --- | --- |
| Why does the project exist? | [Foundational proposal](FOUNDATIONAL_PROPOSAL.md), `forever/project.intent.json` |
| What must survive? | [Standard](STANDARD.md), invariants and compatibility records |
| How do the parts relate? | [Exact reference map](API/CORE_INPUT_AND_NORMALIZATION.md), model trace |
| What implements it now? | [Binding/operation inventory](API/OPERATION_COVERAGE.md), implementation records |
| How are numbers preserved? | [Optional exact interchange](API/LOSSLESS_JSON.md), separately from legacy host values |
| What is actually verified? | Latest research evidence report and exact linked runs; declarations alone are not proof |
| How do I maintain this knowledge? | [Worked bug-fix example](MAINTENANCE_EXAMPLE.md), bounded artifact checks |

Project-specific requirements, actual target behavior and authoritative acceptance
still need to be supplied. No agent, cloud, SDK or service is required by the model.
