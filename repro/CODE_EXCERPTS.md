# 关键代码摘录（98ab054）

来源：`l6_postdeploy_audit_20261030/AUDIT.md`、`l7_ltm_ack_fix_20261101/REPORT.md`、`audit_code.md`。
行号按部署版本；公开版只保留机制所需片段。

## 1. pre-step 只看 recent，不看 LTM

`lingyao_next/chain/link_a.py:295-297`

```python
def _text_has_prior(text: str) -> bool:
    return any(m in text for m in PRIOR_MARKERS) and not any(d in text for d in DENIAL_MARKERS)
```

`lingyao_next/chain/link_a.py:1319-1325`（故障版本）

```python
elif _text_has_prior(draft.text):
    span = _prior_span(draft.text)
    ref = _recent_support_ref(span, world.recent_refs)
    if not ref:
        draft = _repair_prior_text(draft)
        claims = ()
```

`lingyao_next/chain/link_a.py:417-430`

```python
def _recent_support_ref(span, recent_refs):
    # 只在 recent_refs 里找；签名没有 memory/memos 参数
```

`lingyao_next/chain/link_a.py:328-342`

```python
def _repair_prior_text(draft):
    # 把 prior frame 替换成“我记下你现在说的”
```

`link_a.py:1299-1303` 已构造 `prior_refs = memos + recent_student_refs`，但只在 1345 行传给后面的 `audit_claims`；改写已经把 claims 清空，后面的审计没有东西可拒。

## 2. 审计的豁免与字面支持

`lingyao_next/claim_audit.py:198-208`

```python
def _asserts_prior(text: str) -> bool:
    return any(m in text for m in PRIOR_MARKERS)  # 包含裸“我记得”
```

`claim_audit.py:209-235` 的范围豁免（问句、计划、建议、假设、对话元陈述）在 prior 分支**之后**才检查，所以救不了“我记得……”。

`claim_audit.py:143-170`：support 只做 bigram 交集；没有声明成 claim 的句子不进入审计。

## 3. 修复方向（不是本复现的运行代码）

- pre-step 只声明带 support ref 的 span，不改写文本、不清空 claims。
- 支持来源 = recent 学生轮 **或** `memos`。
- 按语法主语判断“记得的对象是不是学生”；support 用精确 clause 匹配与否定极性。
- material 层拆 `display_text` 与 `citation_text`。

补丁：`l7_ltm_ack_fix_20261101/patch/l7_ltm_ack_fix.patch`；候选 `3f67db0`。
