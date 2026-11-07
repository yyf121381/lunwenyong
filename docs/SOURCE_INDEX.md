# Source index

This repository contains public, desensitized companion materials only.

## Included

| Path | Contents | Evidence class |
|---|---|---|
| `repro/` | Fixed synthetic input, control-flow mirror script, expected output, key code excerpts, run instructions | Deterministic |
| `cases/e1_eight_cases.md` | Eight desensitized cases; observation / interpretation / unknown separated | Contemporaneous transcript, later review |
| `validation/deterministic/` | Six chain cases + ten unit checks | Deterministic |
| `validation/assembly/` | Six real-assembly cases | Assembly with declared model output |
| `validation/canary/` | Three real-entry turns, one redacted account | Canary |
| `paper/` | Placeholder; English PDF and LaTeX to be added | — |

## Not included (restricted)

- Full student transcripts, private text, account mappings.
- Databases, memory stores, request indexes.
- Credentials, server configuration, billing records.
- The production implementation and the original repository history.

These remain in the restricted working environment and are not part of this repository.

## Version anchors

| Anchor | Value |
|---|---|
| Release | `98ab054` |
| Service SHA256 | `088c96dc0a169676e2b974f4acdcdbf01027ba6d46665b845e84189133980247` |
| LTM-ack candidate | `3f67db0` |
| Defect | Pre-step consults only the recent window; on miss it rewrites the acknowledgement and clears claims, so the formal audit passes vacuously |

## Reproduction

```bash
cd repro
python repro_pre_step.py
```

Compare with `repro/expected_output.json`. The script is a logic mirror, not the full production implementation.

## Evidence boundary

- **Deterministic:** fixed input; proves the code path rewrites, not the production rate.
- **Assembly:** real chain with declared model output; proves the chain passes for fixed cases, not live-model behavior.
- **Canary:** three real-entry turns; entry-level behavior only, not window isolation or scale.
