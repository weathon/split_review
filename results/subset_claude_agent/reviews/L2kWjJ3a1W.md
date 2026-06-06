Now I have enough context. Let me draft the review and then calibrate.Round 1 bracket: **4.5 – 6.5**. LaMo (6.25, accepted) is the closest topical anchor — stronger novelty and results, but similar domain. TEDUO (4.25, rejected) is weaker due to single benchmark. TG-DT sits between them. Now narrowing.Now I have enough calibration. Let me compare:

- **TCMRL (5.67, rejected)**: Very similar domain (offline meta-RL + contrastive contexts), but had unclear technical justification and fundamental design questions. TG-DT is more clearly motivated and has cleaner ablations.
- **ECET (5.75, accepted)**: Online meta-RL on same benchmarks, stronger SOTA results. TG-DT is harder setting (offline) with a novel language angle, but "on par" rather than clearly better results.
- **LaMo (6.25, accepted)**: Actual LLM weights in offline RL — more impactful use of language, stronger results. TG-DT is more limited.

TG-DT is comparable to ECET and somewhat stronger than TCMRL. Final placement: **5.5**, borderline accept. The contribution is novel (language-grounded zero-shot offline meta-RL), results are competitive, ablations are sound, and the main weaknesses are the unclear evaluation protocol in Table 1 and the overstated free-form language claim (acknowledged in limitations).

---

## Summary
TG-DT proposes an offline meta-RL framework that replaces test-time task demonstrations with natural language descriptions for zero-shot generalization. It introduces a dual alignment mechanism — a contrastive objective (TBC) for cross-task separation and a matching objective (TBM) for within-task quality differentiation — to ground behavioral trajectories in a shared text-behavior embedding space, which then conditions a Decision Transformer-style policy decoder. Experiments on MuJoCo (Cheetah-dir/vel, Ant-dir) and MetaWorld (ML10, ML45) show competitive performance against baselines that require test-time demonstrations, while TG-DT requires only a text description.

## Strengths

- **Zero-shot competitive with demonstration-aided baselines**: Table 1 shows TG-DT (549.9 Cheetah-dir, -93.0 Cheetah-vel, 361.1 ML10) matches or exceeds baselines like Meta-DT (539.6, -102.7, 335.2) and PDT (548.9, -150.6, 289.2) across most environments without requiring any test-time demonstrations, while those baselines do. The ability to match information-privileged baselines without demonstrations is the paper's central claim and is empirically supported.

- **Dual alignment ablation validates complementarity**: Table 3 shows a clear hierarchy — full TG-DT (958.4, -21.4, 383.4 on Expert) > w/o TBC (936.8, -24.6, 322.1) > w/o TBM (875.2, -46.6, 298.7) > w/o both (859.4, -55.7, 133.6). Removing TBM causes the steeper drop on Ant-dir, while removing TBC causes more degradation on Cheetah-vel. This establishes both components as necessary.

- **Robustness across dataset qualities**: Table 4 shows TG-DT is competitive across Expert, Mixed, and Medium datasets. Notably on Mixed Ant-dir (344.9), TG-DT outperforms DPDT (342.6) and Meta-DT (327.0), suggesting the alignment mechanism is not brittle to suboptimal training data.

- **Trajectory-level pairing is a clean methodological insight**: Rather than assigning one description to all trajectories of a task, TG-DT uses trajectory-level pairing where each trajectory gets a description reflecting its own return and episode length (Section 3.1). This design enables within-task quality discrimination, which is essential for the TBM matching objective and uncommon in language-conditioned RL.

- **Comprehensive evaluation scope**: Five environments, three dataset quality levels (Expert/Mixed/Medium), zero-shot and few-shot settings, 5 independent runs each, with an ablation and a description-guided data-sharing analysis.

## Weaknesses

### Fatal
None.

### Major

- **Table 1 evaluation protocol is underdescribed**: Table 1 is captioned "Zero-shot test returns" and includes baselines (PDT, MDT, HDT, DPDT) marked with † for "requiring test-time interaction to obtain adaptation demonstrations." The paper does not specify whether these methods were run *with* their full test-time demonstrations (their intended setting) or *without* (a disabled variant). The plausible interpretation — that † methods are given their demonstrations and TG-DT is shown to match them without demonstrations — would make TG-DT's zero-shot result more impressive. But without explicit confirmation in the paper, the reader cannot verify this. One sentence in Section 5.2 clarifying the evaluation protocol would resolve this entirely.

### Minor

- **Motivation-mechanism gap for free-form language**: The introduction motivates the method with examples like "setting the table for dinner" as free-form task instructions (Section 1), but the actual descriptions are rigid templates: "This is the [task_name], which targets [task_intent]… yield an expected return of [expected_return]." The paper's own Limitation section correctly acknowledges "reduces robustness to free-form natural language," but this constraint should be stated more prominently up front rather than only in limitations, since the motivating examples imply a broader capability than what is implemented.

- **No ablation of semantic content vs. numeric identifiers**: The description template contains both structured numeric fields (expected return, episode length, which effectively serve as task IDs) and semantic language content (task intent, environment description). There is no experiment that replaces the full description with only the numeric fields, holding all else constant. Without this, it cannot be determined whether the linguistic semantics or the numeric identifiers are driving the alignment and task disambiguation. This would be the most direct test of the "natural language grounding" claim.

- **Sensitivity to test-prompt quality unaddressed**: Section 4 notes that at test time, expected return and episode length are "replaced by approximate statistics inferred from the training distribution," but provides no analysis of how sensitive performance is to errors in these approximations. For the claimed zero-shot use case (new tasks with no interaction), the accuracy of these estimates may vary substantially.

### Trivial

- **Table 3 dataset split not stated in caption**: The ablation numbers exactly match the Expert dataset results in Table 4, but the Table 3 caption does not specify "Expert dataset." Minor presentation issue.

- **BLIP initialization not ablated**: The paper states BLIP's cross-modal attention patterns "transfer effectively to trajectory-text alignment" (Section 3.2) without comparing to BERT-initialized or randomly initialized alternatives.

## Nice-to-Haves

- Add an ablation replacing the full description with a stripped version containing only task name + numeric statistics (return, episode length). If performance is unchanged, the "natural language" framing should be toned down; if performance drops, the semantic content is doing real work and this finding would significantly strengthen the paper's contribution.
- Evaluate text conditioning at inference: does providing a null/generic text description (while keeping RTG conditioning) degrade performance? This would test whether the policy decoder relies on language or primarily on the RTG signal.
- Confidence intervals in main tables (rather than only in Appendix C), particularly for cases with narrow margins (e.g., Cheetah-dir: 549.9 TG-DT vs. 548.9 PDT; ML45 few-shot: 499.2 vs. 498.6 DPDT).
- tSNE visualizations under ablation conditions (w/o TBC, w/o TBM) to visually confirm what each alignment component contributes to the embedding structure.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"TG-DT is not zero-shot when K > 0" (Harsh Critic Issue 3)**: The paper distinguishes description-guided data sharing (using semantically similar *training* task trajectories) from few-shot (using *target task* data). While the zero-shot label for K > 0 is debatable, the paper is transparent that K > 0 uses training-distribution data, not target-task data. The distinction is defensible and the paper doesn't definitively mislabel K > 0 as zero-shot. Reduced to a minor presentation point already incorporated above.

- **"0.3 cosine similarity means text conditioning is ignored"** (Harsh Critic, Section 3.2): Speculative. The paper demonstrates that this alignment level yields strong performance outcomes and cites prior work supporting that moderate alignment suffices. No evidence in the paper supports the hypothesis that the decoder ignores text; this would require an ablation that is not present, making the weakness speculative-fatal. Removed per hard rules.

- **Criticisms about reproducibility of imputed test-prompt statistics**: The paper notes test prompts are detailed in Appendix E. Per hard rules, criticism about missing appendix content is removed.

- **Strength: "semantic task-behavior alignment filters task-irrelevant patterns on Mixed data"** (Strength Finder): The paper states this as the *explanatory mechanism* in Section 5.5, but no ablation isolates this mechanism from other factors. Removed as a concrete claimed strength; retained only as a performance result (TG-DT competitive on Mixed data).

## Novel Insights

The most genuinely novel contribution is the adaptation of BLIP-style dual alignment (contrastive + binary matching) from vision-language learning to the offline sequential decision-making setting, with trajectory-level text pairing that encodes per-trajectory quality variation. The key insight — that within-task quality differentiation (TBM) and cross-task semantic separation (TBC) are complementary objectives requiring both to achieve strong zero-shot generalization — is supported by the ablation (Table 3) and is non-obvious from prior work in language-conditioned RL, which typically uses a single contrastive objective or no alignment at all.

## Suggestions

1. **Clarify Table 1 baseline evaluation protocol** (one sentence in Section 5.2): state whether demonstration-requiring baselines are evaluated with or without their demonstrations in the zero-shot table.
2. **Add numeric-only description ablation**: this experiment would either validate or appropriately scope the "natural language grounding" claim and would be the most impactful single addition to the paper.
3. **Temper the introduction's free-form language framing** to match the actual structured-template mechanism; or move the free-form limitation caveat from the conclusion to the introduction.

---

## Score and Decision

### Calibration anchor summary

**Round 1 anchors:**
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/INzc851YaM.md` — avg 3.00, rejected; multi-objective offline RL with DT. Much weaker contribution and narrower evaluation than TG-DT.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/It4KL6XnPq.md` — avg 3.00, rejected; foundation policies with memory. Generic integration paper, weaker than TG-DT.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/AY6aM13gGF.md` — avg 6.25, accepted (LaMo); LMs for offline RL. More impactful language use, stronger results, but also has evaluation issues. TG-DT is weaker on novelty but similar in quality tier.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/zAzzMOaisF.md` — avg 4.25, rejected (TEDUO); language-conditioned offline policy. Single benchmark (BabyAI), narrower evaluation. TG-DT is clearly stronger.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/9pW2J49flQ.md` — avg 8.00, accepted (DeepLTL); LTL-conditioned RL. Theoretically grounded, tight results. Much stronger than TG-DT.

**Round 1 bracket: 4.5 – 6.5**

**Round 2 anchors:**
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/5GauLpaNGC.md` — avg 5.67, rejected (TCMRL); offline meta-RL with contrastive contexts on same benchmarks. Very divided (8, 3, 6). Weaker technical justification than TG-DT; unclear mechanism design. TG-DT is better motivated and more comprehensive.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/UENQuayzr1.md` — avg 5.75, accepted (ECET); online meta-RL on MuJoCo + MetaWorld + ManiSkill. Cleaner SOTA claims, stronger results. TG-DT's setting is harder (offline) and language angle is more novel, but results are only "on par" vs. clearly SOTA.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/XMOaOigOQo.md` — avg 5.67, accepted (ContraDiff); contrastive learning for offline RL. Uses contrastive diffusion, different approach, somewhat comparable contribution scope.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/upV91V0Big.md` — avg 4.75, rejected; continual offline RL. Less novel than TG-DT.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/FhbZ1PQCaG.md` — avg 5.75, rejected; DT with internal memory. Rejected despite 5.75 avg.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/ZtOnddFVT3.md` — avg 4.67, rejected; self-alignment for offline safe RL. Less novel, narrower.

**Narrowing analysis:** TG-DT sits above TCMRL (5.67, rejected) by virtue of cleaner motivation, stronger ablations, and more comprehensive evaluation. It is comparable to ECET (5.75, accepted) in overall quality — the offline/language angle is novel but results are "on par" rather than SOTA. The evaluation protocol issue in Table 1 and the structured-template limitation are the primary negatives, but neither is fundamental. Placement: **5.5**, at the lower end of the 5.5–6.0 range.

**Originality**: Moderate-high. Adapting BLIP-style dual alignment to offline meta-RL trajectories is genuinely novel. Trajectory-level quality pairing is a clean design insight.

**Importance of research question**: High. Zero-shot offline meta-RL without test-time demonstrations is practically relevant.

**Claims supported by evidence**: Partially. Core claim (competitive zero-shot without demos) is supported, but language grounding claim is overstated relative to structured templates.

**Soundness of experiments**: Adequate. Multi-environment, multi-dataset, ablation included. Key protocol gap in Table 1.

**Clarity of writing**: Good. Method is clearly described; limitation acknowledged.

**Value to community**: Moderate-high for offline meta-RL practitioners. Introduces a concrete direction (language descriptions as task specification).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>