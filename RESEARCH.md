# User brief and comparison

## Intended user and painful task

Engineers handing exported LFS pointer files and an object folder to an offline team. Pointer text alone does not prove that the handed-over object bytes exist, match their size or hash. A standalone directory receipt is useful without Git metadata or a Git LFS client.

Current alternatives: git-lfs fsck, history rewriting with git-filter-repo and repository sizing with git-sizer.

Evidence and limits: Git LFS specification establishes the pointer/object contract. The standalone export workflow need is inferred; git-lfs already supports integrity checks in its own workflow. No fabricated customers, requests, adoption, testimonials or growth promise.

## Smallest useful capability and acceptance criteria

Parse strict basic v1 pointers, find missing/corrupt local objects, reject symlink objects and preserve inputs.

Runnable acceptance fixtures are `test_lfs_handoff.py` and `demo.py`. Invalid inputs must return an explicit failure, and diagnostics must preserve source files where the contract is read-only. See README for supported subsets and bounds. Plausible discovery path: git-lfs and data-integrity topics; corruption demo with a portable JSON receipt.

## Live leader research on 5 October 2026

Queries `git lfs` were requested from live GitHub sorted by stars descending. Search receipts include exact query URLs, observation times and top-ten metadata in [research-evidence.json](research-evidence.json). Irrelevant broad matches were rejected: map fonts/geospatial tools are not JavaScript source-map comparables, browser redirect extensions are not site migration analysis, and unrelated notebook/diffusion matches are not notebook hygiene tools.

Highest-star relevant comparable found among the researched set: [git-lfs/git-lfs](https://github.com/git-lfs/git-lfs) with 14529 stars. Some established comparables were added outside the narrow search query. This is bounded search coverage, not an exhaustive global ranking. Stars are a discovery signal, not a performance/reliability result.

| Comparable | Stars | Last observed push UTC | License metadata | Workflow, install, docs and tradeoff |
| --- | ---: | --- | --- | --- |
| [git-lfs/git-lfs](https://github.com/git-lfs/git-lfs) | 14529 | 2026-10-01T04:52:14Z | unresolved metadata; inspect license before reuse | Full Git LFS client and protocol, platform packages, Git integration and integrity checking. Our input is an exported directory subset; no remote or history functionality. |
| [newren/git-filter-repo](https://github.com/newren/git-filter-repo) | 13352 | 2026-07-09T22:09:49Z | unresolved metadata; inspect license before reuse | Repository history rewriting and migration tool with extensive rationale/docs. It mutates history for a different task; no superiority comparison. |
| [github/git-sizer](https://github.com/github/git-sizer) | 4080 | 2026-09-10T21:27:35Z | MIT | Git object graph/size statistics and JSON reports. Checks reachable Git repository dimensions, not a portable exported asset handoff. |

Current READMEs and the returned recent issue/PR samples were inspected. Samples may be maintainer PRs, not genuine user requests. Support channels and examples are visible; support responsiveness, actual installation reliability and time to first useful result of comparables were not measured. License metadata marked unresolved/unavailable is not a permission to reuse. No competitor code or prose is incorporated.

## Distinctness and rejected directions

Compared with all 133 owned repository names, descriptions/READMEs for overlapping tools and yesterday's five launch briefs. The five new products handle saved notebook state, planned redirect graphs, exported LFS bytes, content-bound JSONL record references, and generated-code source positions respectively. They share packaging, not one subdivided product.

Existing json-differ/log-parser/traceweave analyze different JSON or agent-trace semantics; urlnorm normalizes URLs; syncplan plans filesystem synchronization; wheel-sentinel validates Python wheel archives; portable-tree audits names. This candidate's user contract is separate. Environment checking was rejected because envdiff/env-vault/dotenv-mini already cover it; another archive checker was rejected as overlapping Wheel Sentinel.

## Fairness and limitations

Audits exported pointer files, not Git history or attribute rules. Smudged working trees may contain no pointers. No network, fetch, push, server existence claim or repair. Extensions unsupported; symlink input files/directories skipped. Stable trusted local trees only, no protection from concurrent file replacement. Hash work grows with object bytes; 100,000 input file bound.

There is no measured competitor benchmark or superiority claim. Local examples establish our behavior only. No claim is made that a competitor lacks this capability. Broader established tools can be better choices when their workflow/dependencies fit. Evidence dates, installed behavior and untested limits remain separate.
