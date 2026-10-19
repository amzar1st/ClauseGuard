"""Offline integrity verification for the recorded deployment and decision."""
import hashlib
import json
from pathlib import Path


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()

root = Path(__file__).resolve().parents[1]
source = (root / 'contracts/clause_guard.py').read_bytes()
deployed = (root / 'evidence/final-deployed-source.py').read_bytes()
assert source == deployed, 'deployed source differs'
print('Source SHA-256:', hashlib.sha256(source).hexdigest())
record = json.loads((root / 'evidence/final-result.json').read_text())
expected = record.pop('decision_sha256')
assert hashlib.sha256(canonical(record)).hexdigest() == expected, 'decision hash differs'
manifest = json.loads((root / 'evidence/live-request.json').read_text())
envelope = json.loads((root / 'evidence/final-comparison.json').read_text())
assert envelope['request'] == manifest
assert hashlib.sha256(canonical(envelope)).hexdigest() == record['comparison_id']
assert envelope['policy_sha256'] == record['policy_sha256']
for doc in manifest['documents']:
    filename = doc['url'].rsplit('/',1)[-1]
    assert hashlib.sha256((root / 'fixtures' / filename).read_bytes()).hexdigest() == doc['sha256']
    fingerprint = next(f for f in record['assessment']['fingerprints'] if f['id'] == doc['id'])
    assert fingerprint['status'] == 'VERIFIED' and fingerprint['sha256'] == doc['sha256']
    for area in record['assessment']['report'].values():
        for citation in area['citations']:
            if citation['document'] == doc['id']:
                assert citation['quote'] in (root / 'fixtures' / filename).read_text()
assert record['outcome'] == 'CONFLICTS_FOUND'
assert {k for k,v in record['assessment']['report'].items() if v['status']=='CONFLICT'} == {'deadlines','payment','data_use'}
print('Decision hash, source hashes, citations and three expected conflict areas verified.')
