Now I have sufficient calibration data. Let me synthesize everything.

---

## Summary

This paper introduces *Continuous Online Action Detection* (COAD), a task formulation where online action detection models learn on-the-fly from streaming egocentric video without storing data, using single-pass training with state continuity, orthogonal gradient projection, and non-uniform loss weighting. The authors also curate Ego-OAD, a benchmark of 87 classes and 22,991 instances over 263 hours of video derived from the Ego4D Moment Queries split. Experiments demonstrate that COAD improves out-of-stream generalization by up to 6.9% Top-5 Recall and in-stream adaptation by up to 20% over a pretrained-only baseline, with thorough ablation validating each component.

## Strengths

- **Novel, well-motivated task formulation**: COAD bridges the gap between offline OAD training and real-world deployment on wearable devices, where models must adapt continuously without storing data. The motivation is clear and the problem is timely given the push toward on-device training and personalized egocentric AI.

- **Well-curated benchmark (Ego-OAD)**: The dataset provides 87 action classes, 22,991 temporally-grounded multi-label instances across 263h of egocentric video, filling a gap for large-scale egocentric OAD benchmarks. The merging of multiple annotation passes and manual semantic grouping of free-form labels produces a realistic testbed with genuine label ambiguity (36% overlapping actions). Table 1 shows that egocentric pretraining substantially outperforms exocentric, validating that the benchmark captures domain-specific challenges.

- **Thorough experimental analysis**: The paper goes beyond reporting final numbers. Figure 3 provides a nuanced trade-off analysis between in-stream adaptation and out-of-stream generalization across stride and learning rate values. Figure 4 demonstrates progressive improvement toward the IID upper bound as more stream data is processed. Table 3 offers a detailed component ablation isolating the contribution of each strategy (non-uniform loss boosts out-of-stream mAP by 4.2%, orthogonal gradient improves out-of-stream recall by 4.5%).

- **Effective training strategies with strong ablation**: The three proposed components (state continuity, orthogonal gradient, non-uniform loss) are well-motivated by the constraints of streaming video. The full COAD configuration achieves the best out-of-stream generalization, and the ablation reveals interesting interactions — e.g., non-uniform loss proves essential (removing it drops out-of-stream mAP by 4.2% and Recall by 8.3%), while orthogonal gradient is critical for recall.

- **Transparent about limitations**: The paper honestly reports mixed EPIC-KITCHENS results and acknowledges that the baseline sometimes outperforms COAD on in-stream mAP, interpreting this as a deliberate adaptation-generalization trade-off rather than hiding it.

## Weaknesses

### Major

- **Generalization claims limited by dataset provenance**: All splits (pretraining, in-stream, out-of-stream) are drawn exclusively from the Ego4D MQ validation split. While the paper is transparent about this (line 154) and follows the protocol from Carreira et al. (2024a), the claim of evaluating "generalization to unseen environments" should be tempered. The out-of-stream videos share the same collection conditions, annotation pipeline, and broad distribution as the in-stream data; this is held-out generalization within a single distribution, not generalization to truly novel environments. The small pretraining set (186 videos, explicitly designed for "weak initialization") also inflates the relative gain of COAD over the pretrained-only baseline — a larger, more realistic pretraining set would likely narrow these margins. This does not invalidate the core contribution (COAD training strategies improve over no adaptation), but it does weaken the strength of the generalization claims as stated.

### Minor

- **Missing ablation configuration in Table 3**: The ablation omits the "state continuity only" row (State Cont: ✓, Orth. Grad: ✗, Non-uniform: ✗, Adapt: ✓). While the effect can be partially inferred by comparing rows 3 (✓ ✗ ✓ ✓) and 5 (✗ ✗ ✗ ✓), the missing configuration prevents clean isolation of state continuity's independent contribution to both in-stream and out-of-stream performance.

- **Unbacked label efficiency claim**: Section 4.5 states that non-uniform loss "allows training with sparse instead of dense frame-level annotations," but no experiment varies annotation sparsity to verify this benefit. All experiments use supervision at fixed-stride window boundaries; the claim about label efficiency is asserted but not tested.

- **EPIC-KITCHENS results are mixed and under-analyzed**: COAD improves out-of-stream metrics on EPIC-KITCHENS but degrades in-stream action mAP from 9.6 to 7.9 (Table 2). The paper attributes this to "fine-grained nature of the actions and annotations" but offers no deeper investigation — no per-class breakdown, no analysis of which action types benefit vs. suffer, no exploration of whether hyperparameters tuned on Ego-OAD transfer poorly. This limits the evidence that COAD is a general solution beyond the Ego-OAD benchmark.

### Trivial

- The abstract and introduction refer to "top-5 accuracy" while the actual metric reported is Top-5 Recall (as correctly stated in Section 5.1). These should be consistent.

## Nice-to-Haves

- Including comparisons against simple streaming-compatible continual learning baselines (e.g., experience replay with a small buffer, EWC) would strengthen the claim that the orthogonal gradient and non-uniform loss provide benefits beyond generic continual learning strategies.

- A per-class analysis of EPIC-KITCHENS results would illuminate when COAD succeeds or fails and provide actionable guidance for practitioners.

- Reporting variance (e.g., standard deviation over multiple runs) would help assess whether the 1–2% absolute differences in out-of-stream mAP are statistically meaningful.

## Removed Points

*These points were flagged by reviewers but are not valid concerns and should be treated with caution.*

1. **Feature extraction specification**: The harsh critic claimed the mapping from TimeSformer clip features to per-frame features $z_t$ is unclear and irreproducible. This is standard practice in the OAD literature (used in An et al. 2023, Zhao & Krähenbühl 2022, etc.): clip-based backbones process sliding windows and assign the resulting feature to the corresponding temporal position. The paper states features are extracted with a stride of 2 yielding 1.87 FPS, which is sufficient for reproducibility by anyone familiar with video OAD.

2. **Demand for continual learning baselines (EWC, experience replay)**: The critic argued the paper must compare against generic continual learning methods. This is scope creep — the paper proposes OAD-specific training strategies and ablates them thoroughly. Comparing against generic CL methods would be a nice addition (moved to Nice-to-Haves) but is not essential for validating the paper's core contribution.

3. **"w/o COAD baseline is not a plausible streaming scheme"**: The critic claimed any streaming system should keep its recurrent state. The paper acknowledges this explicitly — "w/o COAD" is an ablation baseline that strips all proposed strategies, not a proposed competitive streaming method. The effect of state continuity is studied in Table 3.

4. **Claim that Figure 3 shows COAD yields no net positive**: The critic interpreted the trade-off curve as evidence that "less frequent updating is better for generalization, which undercuts the message." In fact, all COAD configurations in Figure 3 lie above and to the right of the pretrained-only baseline on both axes — COAD improves both in-stream and out-of-stream performance. The trade-off exists *within* COAD variants but does not undermine the net improvement over no adaptation.

5. **"No variance estimates or statistical significance"**: This is a generic criticism that applies to virtually all papers in the video OAD and large-scale benchmark literature. Single-run evaluation is standard practice; this is noted as a nice-to-have.

## Novel Insights

The paper's most interesting finding is the interaction between the three COAD components revealed in Table 3: non-uniform loss and orthogonal gradient serve complementary roles. Uniform loss combined with other components actually *underperforms* (row 2: 21.8 out-of-stream mAP vs. 25.5 for the no-components baseline), suggesting that uniform loss creates harmful gradient interference in the streaming setting that both the non-uniform weighting and orthogonal projection independently help resolve. This is a genuinely non-obvious interaction that goes beyond the simple "each component helps" narrative and suggests the strategies are not merely additive but address interrelated failure modes in streaming OAD training.

## Suggestions

- **Temper generalization language**: Replace "generalization to unseen environments" with "generalization to held-out videos" or similar, and explicitly discuss the limitation that all data comes from the same MQ validation split.

- **Add the missing ablation row**: Including the state-continuity-only configuration (✓ ✗ ✗ ✓) would complete Table 3 and cost little experimentally.

- **Either support or remove the label efficiency claim**: Either run an experiment varying annotation sparsity (e.g., supervision every K seconds for different K), or remove the sentence claiming this benefit.

- **Expand EPIC-KITCHENS analysis**: A brief per-class breakdown or analysis of action duration vs. COAD effectiveness would add substantial insight and help readers understand when COAD applies.

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| M8gXSFGkn2 (EgoHOIBench) | 7.00 | R1 | COAD is weaker — less extensive cross-model generalization evidence, less polished benchmark |
| P6G1Z6jkf3 (Hand-Object Dynamics) | 6.00 | R1 | COAD is comparable — similar scope, similar evaluation concerns |
| Y7jJN0VQ4y (Anomaly Streaming CL) | 5.71 | R2 | COAD is stronger — clearer setting, better ablations, more thorough analysis |
| qnAZqlMGTB (StreamingBench) | 5.75 | R2 | COAD is stronger — has both benchmark AND method contribution, deeper experimental validation |
| JbPb6RieNC (StreamChat) | 5.80 | R2 | COAD is comparable or slightly stronger in experimental depth |
| 67sSPPAZiG (MMEgo) | 6.00 | R2 | COAD is comparable — similar benchmark+method scope, stronger ablation but similar evaluation limitations |
| 1L52bHEL5d (Test-Time Adaptation Ego) | 6.00 | R2 | COAD is comparable — more thorough ablation and analysis, similar evaluation scope concerns |
| C53FwQZigu (IPSeg) | 6.50 | R2 | COAD is weaker (different topic, hard to compare directly) |

**Round 1 bracket**: 3.5–7.5 (anchored by weak papers at ~3.0 and strong egocentric papers at 6.0–7.0).

**Round 2 narrowing**: The paper sits at approximately 6.0. It is clearly stronger than the 5.71–5.80 streaming/continual learning papers (which had more significant setting concerns or thinner experimental validation) but below the 7.00 EgoHOIBench paper (which had broader cross-model generalization evidence). It is comparable to the 6.00 anchors — MMEgo and the test-time adaptation paper — sharing their profile of a solid contribution with addressable evaluation limitations. The paper's thorough ablation analysis and trade-off characterization are stronger than typical 6.0 papers, but the dataset limitation (single MQ split) and under-analyzed EPIC-KITCHENS results pull it back from 6.5–7.0 territory.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>