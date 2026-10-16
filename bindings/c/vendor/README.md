# Parser dependency

cJSON 1.7.19, from https://github.com/DaveGamble/cJSON/tree/v1.7.19.
Upstream `cJSON.c`, `cJSON.h`, and MIT `LICENSE` are vendored so builds work offline.
There is no new system library or language-runtime dependency. cJSON is a maintained
portable C parser; the previous fragment scanner could not establish JSON syntax.
A system JSON library would add platform-specific build requirements. Replacing
cJSON is permitted when shared parsing/validation/preservation fixtures pass.

Local patch: parsed strings and object names carry explicit lengths; string printing
uses those lengths. This lets our adapter distinguish embedded NUL from termination
in IDs, enum values, duplicate names and extension keys. The adapter retains source
record and manifest JSON for lossless serialization, rather than relying on cJSON's
floating-point reprinting or duplication helpers. Do not replace these raw documents
with a cJSON print/duplicate round trip. Other cJSON mutation/creation APIs are not
part of the public adapter and their length fields are not generally maintained.

The adapter adds strict UTF-8 and JSON lexical preflight (including JSON number and
unescaped-control syntax), decoded duplicate-member checks, nesting and byte limits,
and real-target containment. Compile with `CJSON_NESTING_LIMIT=64`. Keep the local
length patch and rerun malformed inputs, sanitizer checks and common fixtures when
updating upstream. This is bounded validation, not hostile-filesystem race protection.
