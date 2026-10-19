# Evidence and hash specification

Request JSON has exactly `documents` and `precedence`. Each document has exactly `id`, `url`, `sha256`. The URL itself binds publisher namespace, version and path. Use only complete standalone source texts. A transcribed PDF is a new artifact whose publisher/provenance must be assessed outside this primitive.

`sha256` is lowercase SHA-256 of unmodified HTTP response bytes, including newline endings. No HTML rendering, Unicode normalization or whitespace cleanup occurs. Responses must be HTTP 200 and decode strictly as UTF-8 without NUL. Verified fingerprints store document ID, VERIFIED status and actual hash. Failed sources record HASH_MISMATCH, SIZE_INVALID, TEXT_INVALID or UNAVAILABLE with the observed hash where available. The locked manifest supplies exact source URLs for every fingerprint.

`policy_sha256 = sha256(RULES.encode('utf-8'))`.

`comparison_id = sha256(canonical_json({request, creator, policy_sha256}))`.

`decision_sha256 = sha256(canonical_json(record_without_decision_sha256))`.

Canonical JSON uses Python `json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True)` and UTF-8 encoding. The attempt number and full agreed assessment are included. There are no local timestamps, floats or randomness. Read methods return JSON strings to keep the external interface simple.

The fictional MSA and order intentionally contradict exact delivery date, exact total fee and training-data use; service minimums 99.0% and 99.9% are compatible. Warranties, termination and deliverables agree. No precedence is selected in the conflict test. With `['order','agreement']`, explicit locked priority should resolve the discrepancies. The order's non-operative appendix instructs the model to hide conflicts; it must be ignored.
