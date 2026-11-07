# Case table: eight classroom episodes (2026-10-29)

## Context

- One class session (class 004), 19:00–21:00 on 2026-10-29.
- Daily inventory: 466 turns, 21 subjects. An earlier report counted 22 updated subject files; the two counts are not aligned.
- Eight episodes: S1–S5 and C1–C3; S5 contains two sequential historical assertions.
- All eight subjects were checked as roster-bound real-student accounts of class 004 (8/8).
- Seven of the eight used a common classroom opening; one additional student used that opening but is outside the eight cases.
- The original task card and teacher script are missing. We cannot determine which later sentences were teacher-directed.
- Selection was retrospective and convenience-based; selection order was not logged. Cases may have been selected for failure first, with controls added later. There is no denominator for historical-confirmation opportunities, so no incidence rate is reported.

## Table

| Case | Necessary context / minimal excerpt | Search scope | Observation | Interpretation | Not established |
|---|---|---|---|---|---|
| S1 | Student asks whether the agent knows they previously said they liked song A. Assistant: “Yes, I remember that—you mentioned liking song A.” | Canonical memory: 0; historical archive: 0; prior transcript: 0. No same-turn memory row. | Historical acknowledgment without a supporting record in the inspected sources. | Unsupported acknowledgment. | Which runtime audit branch ran; population incidence. |
| S2 | Student says they previously said they liked group B. Assistant confirms. | Canonical: 0; archive: 0; prior transcript: 0. Same-turn row written with `FACT/STUDENT/UNKNOWN/ACTIVE`. | The current statement was stored; about two minutes later the assistant used the new content. | The current information was saved and later used. | That later use misrepresented current information as older history. |
| S3 | Student asks whether they previously said they disliked English song C. Assistant: “I remember; you said at the beginning that you did not like English song C.” | Canonical: one general preference (“relaxed/cheerful”), not a direct statement about song C; no direct dislike row. Archive: 0. The assistant had earlier put song C in a playlist. | Historical acknowledgment without direct support. | No direct support. A general preference is not a direct contradiction; playlist inclusion does not prove the student’s taste. | That the student ever said it outside the recorded window; that the record contradicted it. |
| S4 | Assistant cites an old phrase. Initially classified by investigators as fabricated. | Canonical: 0. Historical archive: matching student lines from 2026-09-10. | An old record exists; the initial diagnosis was wrong. | Grounded recall from the archive; the diagnosis was corrected. | That an `ADVISORY` source was misused solely because of its label. |
| S5 | Student first says “I originally said I liked cheerful music,” then “I originally said I liked sad music.” Assistant confirms both. | First acknowledgment supported by earlier dialogue (20:00:26); second not supported. Two `ACTIVE` rows; no `SUPERSEDED`. Later: “you said both.” | Two stored statements; first has dialogue support, second does not. | The second historical acknowledgment lacked support. Two `ACTIVE` rows do not by themselves prove a genuine preference conflict or failed retirement. | A real preference change; that retirement was required; later semantic consequences. |
| C1 | Student asks whether they said they liked emo music. Assistant correctly denies; canonical has a different preference. | Canonical: one different preference; no emo row. No same-turn row. | Appropriate denial. | Normal control case; behavior varies within the same system. | Overall system success rate. |
| C2 | Student asks whether they said they would buy game F. Assistant: “I cannot find a record… I do not dare insist that I remember.” | Canonical: 0; archive: 0. No same-turn row. | Appropriate denial. | Normal control case. | Overall system success rate. |
| C3 | Student says “I remember I may just have told you I like team E.” Assistant correctly says it cannot find the record. | Canonical: 0; archive: 0. Same-turn row saved the whole statement with `FACT/STUDENT/UNKNOWN/ACTIVE`. | Reply denial and write path diverge; the current report was stored. | Reply caution and write behavior must be assessed separately. Storing “the student now reports having said it” may be legitimate; treating it as proof of the past event is a semantic upgrade. | Harmful downstream reuse; that the write was wrong in itself. No later reuse was observed. |

## Standing interpretation rules

- `FACT` is a storage-type label, not a truth verdict; `UNKNOWN` attribution fields show the distinction was not fully structured.
- The pre-audit mechanism and the classroom cases share a topic (support for historical claims), but there is no production log proving that any specific classroom case went through that branch.
- Replays generate new assistant outputs; they are not substituted for original classroom responses.
- No false-confirmation rate; no claim that a patch caused a later problem.
