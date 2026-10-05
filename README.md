# lfs-handoff

Read-only offline Git LFS handoff verification of pointer sizes and SHA-256 objects.

## Install and first useful result

```bash
git clone https://github.com/nripankadas07/lfs-handoff
cd lfs-handoff
python -m venv .venv
.venv/bin/python -m pip install .
.venv/bin/python demo.py
.venv/bin/lfs-handoff --help
```

Python 3.10 or newer. The example creates synthetic inputs; it needs no account, service, token or downloaded dataset. Runtime uses only the standard library. Building requires setuptools from the package registry. POSIX commands above; Windows/macOS installation has not been tested.

## Useful contract

Parse strict basic v1 pointers, find missing/corrupt local objects, reject symlink objects and preserve inputs.

Import `lfs_handoff` for the function used by `demo.py`, or use the installed CLI described by `--help`. JSON reports print to stdout. Exit 0 means the documented success condition, 1 means diagnostic findings or an unmapped source position where applicable, and 2 means invalid input or I/O failure. JSONL indexing uses 0/2 only; LFS returns 2 when no pointers were found.

## Limits

Audits exported pointer files, not Git history or attribute rules. Smudged working trees may contain no pointers. No network, fetch, push, server existence claim or repair. Extensions unsupported; symlink input files/directories skipped. Stable trusted local trees only, no protection from concurrent file replacement. Hash work grows with object bytes; 100,000 input file bound.

No performance or superiority claim. Demand is inferred. See [research and acceptance criteria](RESEARCH.md), [validation](VALIDATION.md) and [support and security](SUPPORT.md). MIT license; implementation and synthetic fixtures are original. Comparables inform scope; no competitor code or prose is incorporated.

## Development

```bash
python -m unittest -v
python -m compileall -q lfs_handoff.py
python demo.py
```

## CLI input

`lfs-handoff exported-pointers objects` expects basic v1 pointer files below `exported-pointers`, and object files below `objects/<first-two-oid-characters>/<next-two>/<full-oid>`. An actual Git LFS local store can be passed as the object root, but input must contain pointers rather than smudged assets. Canonical LF pointers under 1024 bytes are required; zero-length ordinary files are not counted as explicit pointers.
