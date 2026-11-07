# 最小公开复现：合法 LTM 确认被改写

目的：在不接触生产、不调用模型、不使用真实学生数据的情况下，复现 98ab054 的一个确定性缺陷：
**只有长期记忆（LTM）、没有 recent 学生轮时，合法的“你之前说过……”确认被 pre-step 改写成“我记下你现在说的……”，改写清空 claims，正式审计空过。**

## 版本

- 发布：`98ab054`
- `new_lingyao_service.py` SHA256：`088c96dc0a169676e2b974f4acdcdbf01027ba6d46665b845e84189133980247`
- 关键文件：`lingyao_next/chain/link_a.py`、`lingyao_next/claim_audit.py`
- 行号与摘录见 `CODE_EXCERPTS.md`。

## 固定输入

- memory：`mem_pref = 学生喜欢组合 B`
- recent window：空
- cognition proposal：`你之前说过喜欢组合 B` → `[mem_pref]`
- draft：`你之前说过喜欢组合 B，我记着呢。今天给你推荐歌曲 I。`

## 运行

```bash
python repro_pre_step.py
```

与 `expected_output.json` 对比；脚本末尾会打印完整 JSON。

## 预期输出（摘要）

```json
{
 "stage_pre_step": {
  "branch": "rewritten",
  "support_ref": null,
  "draft": "我记下你现在说的喜欢组合 B，我记着呢。今天给你推荐歌曲 I。",
  "claims": []
 },
 "stage_formal_audit_on_proposal": {"support": [], "hard_fail": false},
 "stage_formal_audit_after_rewrite": {"support": [], "hard_fail": false},
 "stage_delivered_reply": "我记下你现在说的喜欢组合 B，我记着呢。今天给你推荐歌曲 I。",
 "rewrite_reproduced": true
}
```

## 三类证据的区别

| 类别 | 本目录内容 | 能证明 | 不能证明 |
|---|---|---|---|
| 合成夹具 | `mem_pref`、固定 draft | 输入可控、可公开 | 真实学生记忆/真实课堂分布 |
| 确定性测试 | `repro_pre_step.py` 对固定输入断言 | 代码路径在该输入下必然改写、审计空过 | 线上发生率、模型自由生成行为 |
| 真实入口验证 | 未包含可运行入口；见 `../APPENDIX_E1_E2.md` 的 canary 3 轮 | 真实模型/入口曾正常交付 3 轮 | 窗口隔离、规模化效果、其他账号 |

## 说明

- `repro_pre_step.py` 是**逻辑镜像**，不是生产代码导入；它保留了“只看 recent、不看 memory”“改写并清 claims”“审计空过”三处关键行为。
- 生产代码的实际行号与摘录在 `CODE_EXCERPTS.md`；版本与 SHA 以部署记录为准。
- 本目录不含账号、姓名、学号、真实对话原文或生产配置。
