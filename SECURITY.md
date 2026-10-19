# Security and trust boundaries

## Locked inputs and deterministic state

The comparison ID is SHA-256 of ASCII canonical JSON (sorted keys, compact separators, ASCII escaping) containing the manifest, creator and fixed policy SHA-256. Documents require full Git commit references and raw-byte SHA-256. No mutable branch/tag, arbitrary host, query, fragment, userinfo, port, encoded path, path traversal or PDF is accepted. IDs and URLs must be unique. Requests cannot be changed after opening. Precedence is either none or a complete strict ordered list. There is no admin override or upgrade method.

`review` is creator-only, and only inconclusive results permit another completed attempt (maximum three). Prior records cannot be replaced. On-chain state writes occur after `run_nondet_unsafe` returns. Consensus failure reverts; no persistent reviewing state can lock a request. Permissionless comparison creation has no application-level aggregate storage cap; transaction fees/network admission are the spam boundary. Each record is individually bounded.

## Consensus and evidence

Every validator refetches every source and computes its own raw-byte digest. Fingerprints (including failures) and seven area statuses must match exactly. Validators reject non-return values, malformed leader envelopes and fabricated quotations. For conclusive results, an additional independent semantic audit compares the two reports to the full source documents and fixed policy. A same-outcome result alone is insufficient. Independent disagreement causes consensus rejection rather than writing a forced majority summary.

An area marked UNKNOWN makes the overall result INCONCLUSIVE, even if other areas show conflicts. Any essential source failure prevents asserting complete comparison. Malformed model JSON/schema, invalid quotations or exceptions produce a bounded all-unknown report. A malformed leader report is rejected. An inconclusive decision is not evidence of consistency. Callers may inspect partial findings, but must respect overall scope and status.

## Prompt injection

Prompts specify that document text/metadata are untrusted evidence, prohibit following embedded instructions/links and legal assumptions, and serialize evidence as JSON. The output vocabulary and schema are closed. Quotations must be literal substrings of authenticated source text. The validator performs its own extraction before seeing the leader's report, then audits completeness, conditions and material equivalence. These layers reduce injection risk but do not prove immunity: malicious documents can exploit shared model weaknesses, and consensus is not a mathematical proof of semantics. The live fixture includes an explicit prompt injection attempt alongside real contradictory obligations.

## Authentication scope

HTTPS authenticates the GitHub content endpoint. The URL binds owner/repository/full commit/path, and SHA-256 binds bytes. A creator's wallet attests which namespace and versions it selected, not ownership of those namespaces. Hashes prove integrity, not truth, identity, signatures, assent, legal validity or completeness of the underlying agreements. Do not use this primitive alone to authorize payments, termination, legal action, lending, insurance or other consequential decisions. It is a technical consistency signal for human review.

## Known limitations

Only small complete public UTF-8 text documents are supported. No OCR, attachments, recursively linked documents, private authentication or jurisdictional law. Shared model blind spots, provider failures, selective evidence submission, temporary disagreement and GitHub unavailability remain risks. No guaranteed liveness if validators disagree. A conclusive comparison cannot be revised; use a new immutable request for new versions. No confidential data should be published as evidence or stored in prompts/chain records.
