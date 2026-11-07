# Deterministic checks

No model, no store, no network. Fixed inputs only.

## Minimal pre-step reproduction

```bash
python ../repro/repro_pre_step.py
```

Expected output: `../repro/expected_output.json`.

Result: the valid long-term-memory acknowledgement is rewritten to a current-turn self-report; `claims=[]`; both formal audits report `support=[]` and `hard_fail=false`; `rewrite_reproduced=true`.

## Six chain cases

All PASS with fixed/declared model output:

1. LTM support present → acknowledgement kept verbatim.
2. No historical support → only the unsupported span removed.
3. One assertion fails → practice plan kept.
4. Benign opinion (`我记得 song I is suitable`) → kept, not treated as a historical assertion.
5. Mixed acknowledgements → supported one kept; unsupported one removed.
6. Recent-window support only → kept, claim ref points to the current student turn.

## Unit checks (10/10)

Includes student-object vs assistant-opinion cases, unsupported duty memory, and negation-polarity cases. All pass.

Source: `l7_ltm_ack_fix_20261101` evidence (`assertions.json`, `outcomes_after.json`), summarized here. Raw evidence remains in the restricted working location.
