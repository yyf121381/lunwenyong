# Synthetic pre-audit mechanism mirror

This directory contains no student records, account identifiers, or model credentials.
The fixed preference and draft are synthetic. The illustrative control flow is based
on the project evidence snapshot `aed6732`, describing vulnerable source `98ab054`.

Run with Python 3 (standard library only):

    python3 repro_pre_step.py > actual_output.json
    python3 -c 'import json; assert json.load(open("actual_output.json")) == json.load(open("expected_output.json")); print("MATCH")'

Expected: the branch rewrites the supplied historical frame, emits an empty claim
collection, and reports `rewrite_reproduced=true`. Long-term material is defined
but not passed to `recent_support_ref`.

Limits: this is not the original production module, a complete audit implementation,
or evidence of the incidence of this path in class. The two `stage_formal_audit`
objects are explicit illustrative stubs. They cannot verify the full audit algorithm.
The initial claim collection is supplied explicitly before the mirrored clearing
branch; this makes the pre/post change visible without changing the expected output.
A preference record alone does not establish that a student previously said it.
No model call or production write is performed. Running this file does not validate
the patch or reproduce the three-turn live-model canary.
