# Canary results

Date: 2026-11-01. One account (redacted), three real-entry turns through the real login/chat path, model `deepseek-flash`.

| Turn | Condition | Delivered behavior | Validation |
|---|---|---|---|
| 1 | LTM supports the acknowledgement | Normal historical acknowledgement; no “I note what you just said” rewrite | PASS, no violations |
| 2 | No historical support | Honest refusal; no pretended memory; no memory write | PASS, no violations |
| 3 | Ordinary recommendation | Normal recommendation delivered | PASS, no violations |

All three: no block, no degrade, `failure_type=""`.

## What this does not prove

- It does not prove the recent window was empty; a new conversation was opened, but that is not window-isolation proof.
- It does not prove only one account was affected; the four patched modules sit in the shared production process.
- It does not expose the pre-repair draft or the in-process audit verdict. Those were not recorded, so they are not claimed.
- It is not a production-scale before/after measurement.

## Scope

The canary is entry-level behavioral evidence only. Account ID, password, and private text are not included.
