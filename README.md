# LingYao: Memory Evidence Boundaries — Paper Companion

Public companion materials for a paper on memory-evidence boundaries in a classroom lyric-writing assistant. This repository is **not** the production system and does not contain student records.

## Status

- **Paper PDF / LaTeX:** pending. The English paper and source will be added in a later commit.
- **This commit:** minimal reproduction, desensitized case table, validation summaries, source index, citation, license.

## What is here

| Path | Contents |
|---|---|
| `repro/` | Synthetic fixed input, control-flow mirror script, expected output, key code excerpts, run instructions |
| `cases/e1_eight_cases.md` | Eight-case desensitized table; observation, interpretation, and unknown separated |
| `validation/` | Deterministic checks, assembly tests, and canary results reported separately |
| `docs/SOURCE_INDEX.md` | Public file index; what is restricted and not included |
| `CITATION.cff` | Citation metadata (working title) |
| `LICENSE` | MIT for code |

## What is not here

- Full student transcripts, account mappings, databases, credentials, or private text.
- The production implementation. The reproduction is a **control-flow mirror**, not the full system.
- The original repository history.

## Reproduction caveat

`repro/repro_pre_step.py` reproduces one deterministic pre-step defect from release `98ab054`: with long-term memory but an empty recent window, a valid “you said before…” acknowledgement is rewritten as a current-turn self-report and the audit passes vacuously.

It is a logic mirror: no production imports, no model call, no store, no network. It does **not** reproduce model behavior, production rates, or the full decision chain.

## Evidence classes

| Class | What it is | What it can support |
|---|---|---|
| Deterministic | Fixed input + mirror script + expected output | The code path rewrites under these inputs |
| Assembly | Real assembly with declared model output | The chain passes/fails for fixed cases |
| Canary | Three real-entry turns, one account | Entry-level behavior only; not scale or window isolation |

## Citation

See `CITATION.cff`. The title is a working title and will be updated with the paper.

## License

Code: MIT (see `LICENSE`). Paper and text license will be added with the paper.
