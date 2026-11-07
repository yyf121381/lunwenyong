# Data inventory (aggregate only)

Units differ. Messages, turns, accounts, and subjects are not interchangeable. The containers overlap; do not add them into one total.

| Container | Inventory | Date range | Limits on interpretation |
|---|---|---|---|
| Account history files | 251 accounts; 14,191 messages (7,096 user, 7,095 assistant) | June–November; classroom use from September | Includes test and unclassified accounts; not all accounts are students; 113 files contain exactly 100 messages, indicating possible truncation or export limits, but the configuration is unconfirmed |
| Historical archive | 108 subject identifiers; 27,484 messages | 2026-09-01 to 2026-10-25 | Overlaps other containers; not fully deduplicated; PII/restricted flags indicate handling requirements, not that every message was individually checked |
| Frozen transcripts | 108 subject identifiers; 4,477 turns | 2026-10-24 to 2026-11-04 | Real and synthetic subjects are not completely classified; a turn is not an independent experiment |
| Frozen memory | 1,321 rows | October | 1,320 ACTIVE, 1 SUPERSEDED; storage state does not establish content correctness |
| Expression attempts | 17,634 attempts | 2026-10-24 to 2026-11-04 | 14,160 parsed, 3,474 unparsed; attempts are not independent model calls or request failures |

## Counting rules

- Four-class account allocations total 148, but the number of distinct real students has not been confirmed.
- A file ending in September does not prove the student had no later records elsewhere.
- An export containing only role, content, and time does not prove the running system had only flat history.
- Internal adequacy labels (FULL, PARTIAL, FAIL) were not independently calibrated; 689 FAIL labels are not 689 conversational or service failures.
- Replays, probes, and synthetic runs are separate from classroom incidents and do not increase the classroom count.

No raw conversations, account mappings, databases, or memory stores are included in this repository.
