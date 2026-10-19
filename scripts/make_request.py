"""Create a locked request from fixture bytes at an already pushed full commit."""
import hashlib
import json
import re
import sys
from pathlib import Path

commit = sys.argv[1]
if not re.fullmatch('[0-9a-f]{40}', commit):
    raise SystemExit('Supply a full 40-character fixture commit SHA')
request = {'documents': [], 'precedence': []}
for name in ('agreement', 'order'):
    data = Path('fixtures', name + '.txt').read_bytes()
    request['documents'].append({'id': name, 'url': f'https://raw.githubusercontent.com/amzar1st/ClauseGuard/{commit}/fixtures/{name}.txt',
                                 'sha256': hashlib.sha256(data).hexdigest()})
print(json.dumps(request, sort_keys=True, separators=(',', ':')))
