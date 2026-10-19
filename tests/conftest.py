"""Reuse the exact official artifact already downloaded by genvm-lint.

genlayer-test 0.29.2 otherwise requests an obsolete release asset filename.
Run genvm-lint check first on a fresh machine; never patch the contract SDK.
"""
from pathlib import Path
import shutil

version = 'v0.3.0-rc7'
name = f'genvm-universal-{version}.tar.xz'
source = Path.home() / '.cache' / 'genvm-linter' / name
target = Path.home() / '.cache' / 'gltest-direct' / name
if source.exists() and not target.exists():
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
