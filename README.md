# LingYao Field Study — Public Companion Materials

Paper: **From Companionship Goals to Maintenance Limits: A Case Study of a Classroom Conversational Agent**
Author: Liuqing Yang (杨柳青), Jiangxi Institute of Applied Science and Technology

Status: preprint prepared; not submitted; no arXiv identifier yet.

## Research questions

- **RQ1:** What obstacles to sustained dialogue are visible in the available records, and which can be connected to internal system evidence?
- **RQ2:** What did patches and architectural changes actually alter, and which effects remain limited to controlled tests?
- **RQ3:** How did unresolved problems, maintenance work, and resource conditions influence the decision to stop maintaining this architecture?

## Contents

| Path | Contents |
|---|---|
| `paper/main.tex` | LaTeX source of the English paper |
| `paper/LingYao_arXiv_English.pdf` | English paper PDF |
| `repro/` | Synthetic fixed input, control-flow mirror, expected output, code excerpts, run notes |
| `evidence/case_table.md` | Eight classroom cases; observation, interpretation, not established |
| `evidence/validation_scope.md` | Fixed-input, assembly, unit, and canary results reported separately |
| `evidence/data_inventory.md` | Aggregate containers; units and overlap limits |
| `evidence/source_index.md` | Public files and restricted-material boundary |
| `CITATION.cff` | Citation metadata |
| `LICENSE-CODE` | MIT for code |
| `RIGHTS.md` | Paper, code, and evidence rights |

## Reproduce

```bash
cd repro
python3 repro_pre_step.py > actual_output.json
python3 -c 'import json; assert json.load(open("actual_output.json")) == json.load(open("expected_output.json")); print("MATCH")'
```

Python 3 standard library only; no network, model, store, or student data. The script is a **control-flow mirror**, not the production module or a complete audit implementation. Its two formal-audit returns are explicit illustrative stubs.

## Evidence boundary

- **Deterministic:** fixed input; shows the mirrored path rewrites and clears claims under those inputs.
- **Assembly:** real assembly with declared model output; 6/6 fixed cases; not live-model behavior.
- **Canary:** three real-entry turns on one account; entry behavior only; not window isolation, scale, or production improvement.
- **Classroom cases:** eight convenience-selected episodes; no incidence denominator; selection order not logged.
- **Replays/probes:** regenerated outputs, not original classroom responses; undeployed changes are not counted as production improvements.

## Not included

Full student conversations, historical exports, databases, memory stores, account mappings, subject hashes, names, credentials, server configuration, signed consent documents, and the original repository history remain restricted.

## Citation and rights

See `CITATION.cff` and `RIGHTS.md`. Code is MIT. The paper license is to be chosen by the author in the arXiv submission interface; this repository does not default it to CC BY.
