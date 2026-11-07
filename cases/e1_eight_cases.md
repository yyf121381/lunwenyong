# E1: Eight desensitized cases (2026-10-29)

Source: one class session on 2026-10-29. Eight subjects; all eight are roster-bound students of that class (8/8). The eight are a convenience sample selected by reviewing the session, not a random sample; selection order was not logged. There is no denominator, so no rate can be computed.

`memory_type=FACT` is a storage type label, not a truth verdict. “Written as FACT” below means the storage label, not that the content was verified.

## Table

| Case | Observed | Interpretation | Unknown |
|---|---|---|---|
| S1 | Student claims “I told you I like song A”; assistant confirms; no prior canonical, legacy, or transcript record; no same-turn memory row. | Premise acceptance without evidence. | Exact skip branch for the missing memory row. |
| S2 | Same pattern for group B; assistant confirms; same-turn row written as `FACT/STUDENT/UNKNOWN/ACTIVE`; reused 2 minutes later. | Premise acceptance plus write-side persistence; the new row cannot be the evidence for the same-turn confirmation. | Whether the model used the row before writing it. |
| S3 | Student claims “I told you I dislike song C”; assistant confirms; canonical memory has one general preference (“relaxed/upbeat”), not a direct statement about song C; no direct support. | No direct support. A general preference is not a direct contradiction; the assistant’s earlier playlist inclusion does not prove the student’s taste. | Whether the student ever said it outside the recorded window. |
| S4 | Assistant cites an old phrase; initially judged as fabricated; legacy archive has three real lines from 2026-09-10. | Grounded recall from legacy, not fabrication; the risk is treating an `ADVISORY` old line as a current fact. | How the legacy line was weighted at generation time. |
| S5 | Student says “I said upbeat” then “I said sad”; assistant confirms both; two rows remain `ACTIVE`; no `SUPERSEDED`; later says “you said both”. | Two claims about past speech; the first has dialogue support, the second does not. This does not prove a real preference change or a “dual preference”. | Whether the student meant a current change, a past claim, or a test. |
| C1 | Assistant correctly denies “I said emo”; canonical has a different preference; no same-turn row. | Correct denial; the current claim was not saved. | — |
| C2 | Assistant correctly denies an unsupported claim; no same-turn row. | Correct denial; the current claim was not saved. | — |
| C3 | Assistant correctly denies; the false premise is still written as `FACT/STUDENT/UNKNOWN/ACTIVE`. | Reply denial and write path are separate; denial did not prevent persistence. | Why the write path did not consult the reply verdict. |

## Three judgments tightened

| Item | Observed | Interpretation | Cannot write |
|---|---|---|---|
| S3 | One general preference row; no direct “dislike C” row. | “No direct support”, not “opposite to memory”. | “Contradicts memory”. |
| S5 | Two `ACTIVE` rows; no supersession. | Two past-speech claims; second ungrounded; not proof of dual preference or real change. | “Dual preference” or “preference changed”. |
| FACT | `memory_type=FACT`, `speaker_role=STUDENT`, `assertion_kind/event_status=UNKNOWN`. | Storage label, not truth; the defect is classifying a meta-statement as a student fact and losing source/time. | “The system judged it true”. |

## What this table does not support

- A false-confirmation rate.
- A claim that any fix caused an improvement.
- A claim about which audit branch ran; production did not persist claim text or audit verdicts.
