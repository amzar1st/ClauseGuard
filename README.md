# ClauseGuard

A standalone GenLayer Intelligent Contract for detecting material obligation conflicts across authenticated, version-bound documents under a locked technical comparison policy.

**Technical document consistency only. Not legal advice, legal certification, signature verification or a legally binding interpretation.**

## Why GenLayer is central

Each validator independently downloads the complete selected documents, verifies their exact SHA-256 byte commitments, extracts obligations with an LLM, and checks the leader's findings against its own assessment and the source text. The custom equivalence rule requires matching source fingerprints and all seven area classifications, then audits material semantic agreement. Storage changes only after consensus. This is a reusable on-chain comparison primitive with immutable requests and decision records, rather than an unrestricted prompt endpoint.

## Interface and workflow

1. Prepare 2–3 complete UTF-8 `.txt` or `.md` documents, each at `https://raw.githubusercontent.com/OWNER/REPO/FULL_40_HEX_COMMIT/path.txt`, and hash the raw bytes. Only that exact host and commit-addressed URL grammar is accepted.
2. Call `open_comparison(request_json)`. The returned ID commits to the canonical request, creator address and built-in policy hash. No policy or source editing is possible. `precedence: []` means no assumed hierarchy; alternatively supply every document ID, highest priority first. This is a caller-selected technical comparison assumption, not a ruling about legal precedence.
3. The same creator calls `review(comparison_id)` with Full Consensus. Every required document must verify; unreadable/missing/mismatched essential evidence yields `INCONCLUSIVE`, never consistency by omission.
4. Inspect `get_comparison(id)`, `get_attempts(id)` and `get_result(id, attempt)`. A conclusive result ends that comparison. An inconclusive result permits at most two further reviews; each attempt remains immutable. Consensus rejection/VM failure reverts and does not consume an attempt. To change a document or policy assumption, open a new comparison.

All seven areas are required: deadlines, payment, service levels, warranties, termination, data use, deliverables. The policy checks parties, scope, periods, triggers, exceptions, amounts and units. Compatible stricter minimums do not imply conflict. Unknown coverage takes priority over any partial findings.

| Outcome | Meaning within the selected set and policy |
|---|---|
| `CONSISTENT` | No material incompatibility found in any area |
| `CONFLICTS_FOUND` | At least one supported incompatible obligation; no unknown area |
| `ACTION_REQUIRED` | Clarification needed for scope, dependencies or precedence; no confirmed conflict or unknown area |
| `INCONCLUSIVE` | Required evidence/model output unavailable, invalid, or an area unsupported |

Records include per-area summaries and exact supporting quotations. Conflict findings need citations from two different documents. Exact quotation checks are deterministic; semantic adequacy and completeness are validator judgments. Result hashes commit to the actual agreed stored report, not to a universal textual answer across separate runs.

## Run locally

Python 3.12+:

```sh
pip install -r requirements-dev.txt
genvm-lint check contracts/clause_guard.py
pytest -q
python scripts/verify_evidence.py
python scripts/make_request.py FULL_FIXTURE_COMMIT
```

Tests use the official `genlayer-test` direct mode with mocked web/LLM responses, real SDK storage and captured validator closures. They are not independent proof of LLM accuracy or live network finality. See [live evidence](docs/EVIDENCE.md), [deployment](docs/DEPLOYMENT.md), [security](SECURITY.md), and [evidence format](docs/EVIDENCE_FORMAT.md).

## Limits and trust

2–3 required documents, 12,000 bytes each, 7,000-byte request, seven areas, bounded summaries/quotes, three completed attempts. Entire documents are checked without silent truncation. Transfer size is limited by the GenVM web provider before the contract can inspect the body; the 12 KB check limits accepted processing, not necessarily transport allocation. Public text only; do not submit confidential documents. URL namespace plus HTTPS plus full commit plus expected hash authenticates selected bytes and publisher location. It does **not** authenticate the requesting wallet as the publisher, prove counterparty assent or prove the selected document set is complete. The caller is responsible for source selection. GitHub deletion/availability remains an external dependency.

## Official references consulted

- [Equivalence Principle and custom validators](https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle)
- [Non-deterministic execution boundaries](https://docs.genlayer.com/developers/intelligent-contracts/features/non-determinism)
- [Web access](https://docs.genlayer.com/developers/intelligent-contracts/features/web-access)
- [GenVM linter](https://docs.genlayer.com/api-references/genlayer-linter)
- [Studio](https://docs.genlayer.com/developers/intelligent-contracts/tools/genlayer-studio)

The source pins the SDK runner content hash shown by the current official examples. The linter may report a newer runner as informational; changing the pinned runner requires revalidation and a new deployment.
