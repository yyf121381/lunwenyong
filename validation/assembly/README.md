# Assembly tests

Real service assembly, fixed/declared model output, no live model, no network, no store.

Chain exercised:

```
DecisionWorld (ingress → evidence → understanding → retrieval → persona)
  → link_a.run_decision_core
  → material registry / authority / expression emit
  → prior-ack gate → audit → repair → validate
```

Result: **6/6 PASS**.

| Case | Result |
|---|---|
| 1 LTM supports the acknowledgement | PASS — kept verbatim |
| 2 no historical support | PASS — only the unsupported clause removed |
| 3 one assertion fails | PASS — plan kept |
| 4 `我记得 song I is suitable` | PASS — kept as assistant opinion |
| 5 mixed support / no support | PASS — supported kept, unsupported removed |
| 6 recent-window support | PASS — kept, ref points to current turn |

Limit: this is an assembly test with declared outputs, not a live-model or production-rate test.

Source: `l7_ltm_ack_fix_20261101/staging/STAGING.md`, summarized and desensitized here. Raw evidence remains restricted.
