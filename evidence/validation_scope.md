# Validation scope

Four checks are reported separately. Their counts are not added as independent samples.

| Check | Reported result | What it establishes | What it does not establish |
|---|---|---|---|
| Fixed-input mechanism reproduction + six-case checks | Specified checks passed | For the supplied inputs, the mirrored pre-step rewrites the historical frame, clears claims, and the audit receives an empty claim set; the patched behavior passes the six specified cases | Free-generation behavior; production incidence; that the mirror equals the full production implementation |
| Declared-output staging assembly | 6/6 | The real assembly path (decision core → audit → repair → validation) passes six fixed cases with declared cognition/expression outputs | Six real student successes; live-model behavior |
| Unit tests | 10/10 | Tested clause, polarity, and support branches | Overall interaction reliability |
| Live-model entry-point canary | One account, three normal turns | Login/chat entry and delivery worked for three turns; no block or degrade | Long-term or cross-class improvement; window isolation; a model-call count; production-scale before/after |

## Reproduction package

`repro/repro_pre_step.py` is a self-contained control-flow mirror. It does not import production modules and does not execute the full audit algorithm. The two `stage_formal_audit` returns are explicit illustrative stubs. Running it shows the mirror’s behavior for the fixed input; it does not prove equivalence with the deployed version or substitute for the original deployment-function reproduction.

## Patch scope

The patch covered four modules in a shared production process. The single-account canary describes the observation scope, not deployment isolation. No component-by-component ablation or large-scale before/after comparison was completed.

## Regenerated materials

Replays and probes generate new assistant outputs from historical inputs. They are reported as replay observations, not as original classroom outputs, and they do not increase the classroom-incident count.
