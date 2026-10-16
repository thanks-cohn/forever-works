# Optional experimental acceptance adapter

This is construction input, not evaluator source or a prescribed third product UI.
The fresh consumer chooses a useful complementary product and publishes its workflow,
new decisions and limitations. To test it repeatably, provide a command (argv array)
reading one JSON request from stdin and writing one JSON result to stdout. Diagnostics
go to stderr; network operations use only the supplied endpoints and scoped grants.

Request fields: `objectEndpoint`, `catalogEndpoint`, `objectGrant`, `catalogGrant`,
`objectDocument` and `itemDocument` (exact JSON text strings), and `catalogETag`.
The requested observable outcome is to preserve the object then catalog item through
the product's documented workflow, respecting immutable object identity, conditional
catalog updates and recovery obligations. No hidden requirement dictates screens,
implementation, business model or further useful functions. An insufficient grant
must not be substituted/guessed; partial effects must be disclosed. A lost response
is UNKNOWN until resolved by a safe retry/read, not a reason to invent success.

Result: `{outcome:"complete"|"partial"|"denied"|"conflict"|"unknown", detail?:string}`.
The evaluator does not trust this declaration: it checks reference-service state,
content, metadata, identity and revisions independently. Adapter code is the new
consumer's code and is never supplied as an original producer implementation.
Published service obligations are the oracle. Values/orderings/fault points may be
held out, but obligations are not invented after construction. Log interventions.

An HTTP acceptance endpoint is an equivalent optional transport: POST the same JSON
request and return the same JSON result. The evaluator accepts `--adapter-url` instead
of a local argv command, so a private evaluator container can test a consumer over the
reference network without mounting producer/evaluator source or a Docker socket into
the consumer. A declared fault proxy may be supplied as a reference endpoint during a
case; use the supplied endpoint rather than hardcoded hosts. No extra privilege follows.
