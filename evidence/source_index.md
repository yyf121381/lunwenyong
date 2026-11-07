# Source index

The index separates public files from restricted materials. It does not assume that a reader can access the restricted snapshots.

## Public files

| Path | Contents | Evidence class |
|---|---|---|
| `paper/main.tex` | LaTeX source of the English manuscript | Author-provided manuscript |
| `paper/LingYao_arXiv_English.pdf` | English manuscript PDF | Author-provided manuscript |
| `repro/repro_pre_step.py` | Self-contained control-flow mirror | Synthetic reproduction |
| `repro/expected_output.json` | Expected mirror output | Synthetic reproduction |
| `repro/README.txt` | Run notes and limits | Synthetic reproduction |
| `repro/CODE_EXCERPTS.txt` | Indexed source excerpt, not an execution trace | Restricted source snapshot, excerpted |
| `evidence/case_table.md` | Eight classroom cases; observation / interpretation / not established | Contemporaneous records, later review |
| `evidence/validation_scope.md` | Fixed-input, assembly, unit, canary scope | Mixed; separated |
| `evidence/data_inventory.md` | Aggregate containers and counting limits | Contemporaneous records, inventory |
| `evidence/source_index.md` | This file | Author retrospective |
| `README.md`, `CITATION.cff`, `RIGHTS.md`, `CHANGELOG.md` | Project description, citation, rights, change record | Author-provided |

## Restricted materials (not in this repository)

- Full student conversations and private text.
- Historical exports, frozen transcripts, databases, memory stores, and request indexes.
- Account mappings, names, student IDs, subject hashes, and small-cell identifying details.
- Credentials, API keys, server configuration, and operational addresses.
- Signed consent documents, signatures, and class rosters.
- The production implementation and the original repository history.

These remain in the restricted working environment. No private repository link is offered as a substitute for access.

## Internal snapshots

| Snapshot | Use |
|---|---|
| `a4d6874` | Restricted research materials: data inventory, incident evolution, architecture timeline, E1/E2 appendix |
| `aed6732` | Restricted paper-material supplement and original reproduction working copy |

The public materials were assembled from these snapshots and the author-provided manuscript. The snapshots themselves are not public.

## Provenance categories

- **Contemporaneous project documents:** architecture reports and stage documents.
- **Production records:** transcripts, memory rows, expression attempts, request indexes.
- **Later investigation:** code inspection, controlled reproductions, repair reports.
- **Synthetic reproduction:** fixed-input mirror, no model, no store, no network.
- **Author retrospective:** purpose, funding, maintenance decision, and consent-scope confirmation.

## Version anchors

| Anchor | Value |
|---|---|
| Vulnerable release | `98ab054` |
| Service SHA256 | `088c96dc0a169676e2b974f4acdcdbf01027ba6d46665b845e84189133980247` |
| LTM-ack candidate | `3f67db0` |

## Reproduce

```bash
cd repro
python3 repro_pre_step.py > actual_output.json
python3 -c 'import json; assert json.load(open("actual_output.json")) == json.load(open("expected_output.json")); print("MATCH")'
```

The script is a logic mirror, not an import of production modules or a complete audit implementation.
