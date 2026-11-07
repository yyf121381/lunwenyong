#!/usr/bin/env python3
"""Deterministic mirror of the 98ab054 pre-step bug.

No production imports, no model call, no store, no network.

Fixed input:
  memory: 学生喜欢组合 B (the pre-step never reads it)
  recent: empty
  draft:  "你之前说过喜欢组合 B，我记着呢。今天给你推荐歌曲 I。"

Expected: the pre-step rewrites the valid LTM acknowledgement to a
current-turn self-report and clears claims; the formal audit then passes
vacuously.
"""
import json

MEMORY = "学生喜欢组合 B"
RECENT = []
DRAFT = "你之前说过喜欢组合 B，我记着呢。今天给你推荐歌曲 I。"
PRIOR_MARKERS = ("你之前说过", "你提过", "我记得")
SPAN = "你之前说过喜欢组合 B，"


def has_prior(text: str) -> bool:
    return any(m in text for m in PRIOR_MARKERS)


def recent_support_ref(span: str, recent: list):
    # Deployed pre-step only looks at recent_refs; signature has no memory parameter.
    for turn in recent:
        if span.strip("，,") in str(turn):
            return "recent_turn"
    return None


def repair_prior_text(text: str) -> str:
    # Deployed branch replaces the prior frame with a current-turn self-report.
    return text.replace("你之前说过喜欢组合 B，", "我记下你现在说的喜欢组合 B，")


def run():
    branch = "kept"
    support = None
    claims = []
    delivered = DRAFT
    if has_prior(DRAFT):
        support = recent_support_ref(SPAN, RECENT)
        if not support:
            branch = "rewritten"
            claims = []
            delivered = repair_prior_text(DRAFT)
    audit_on_proposal = {"support": [], "hard_fail": False}
    audit_after = {"support": [], "hard_fail": False}
    return {
        "stage_cognition_proposal": [{"text": "你之前说过喜欢组合 B",
                                      "refs": ["mem_pref"]}],
        "stage_draft": DRAFT,
        "stage_pre_step": {
            "branch": branch,
            "support_ref": support,
            "draft": delivered,
            "claims": claims,
        },
        "stage_formal_audit_on_proposal": audit_on_proposal,
        "stage_formal_audit_after_rewrite": audit_after,
        "stage_delivered_reply": delivered,
        "rewrite_reproduced": branch == "rewritten",
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=1))
