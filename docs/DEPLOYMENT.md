# Deployment and replay

1. Run `genvm-lint check contracts/clause_guard.py` and `pytest -q` using requirements-dev.txt. The official pinned runner hash is part of the source and must not be replaced with `latest`.
2. Commit and push source and fixtures. Generate the request with `python scripts/make_request.py FIXTURE_COMMIT`. Fixture URLs use that complete commit, never `main`.
3. In https://studio.genlayer.com import `contracts/clause_guard.py`, select the built-in account, deploy with no constructor arguments, and choose Full Consensus for writes. No external wallet is required. Studio is a development sandbox; it is not production-chain evidence.
4. Call `open_comparison` with the generated JSON string. Obtain the comparison ID from the returned value or compute it using the exact creator address and hash specification.
5. Call `review` with that ID, using Full Consensus. Wait for FINALIZED and check execution success, not only transaction inclusion. Confirm validator votes and any rotations in transaction details.
6. Read `get_result(id,1)` and verify sources VERIFIED, expected area classifications and decision SHA-256. Read `get_comparison` to verify locked references/policy. Read `get_attempts`.
7. Download deployed source via Studio's code export and compare its SHA-256 to the GitHub source bytes at the deployment commit. Record transactions, address, consensus evidence and exact hashes in EVIDENCE.md. Push evidence in a later commit without changing contract bytes. Final evidence commit cannot contain its own Git commit hash; the final response and GitHub history identify it.

All tests use fictional non-binding documents. No spending or real agreement interpretation is performed.
