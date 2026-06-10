Now I have all the information needed to write the final consolidated review. Let me compile it.

**Calibration Summary:**

**Round 1 (Bracketing):**
- Low band (<3.5): PowerGPT (3.00, Reject) — domain-specific "foundation model" with narrow pre-training, similar overclaim to SigMap
- Middle band (3.5–7.5): Wireless Geometric Transformers (7.00, Accept), NextLocLLM (5.25, Reject), G2PTL (6.33, Reject), MapLearn (4.75, Reject)
- High band (>7.5): Multiple 8.0 papers (Accept) — strong theoretical/methods papers

**Bracket estimate: 4.0–5.5** (SigMap is better executed than PowerGPT at 3.0 but has more serious reproducibility issues than NextLocLLM at 5.25)

**Round 2 (Narrowing):**
- Presto (4.75, Reject) — self-supervised pre-trained transformer, similar domain-specific framing, concerns about baseline comparisons. SigMap has more substantial accuracy gains but a more severe reproducibility gap.
- MLO-MAE (4.40, Reject) — learned masking for MAE, method fully specified. SigMap's cycle-adaptive masking is less well-specified.
- RedMotion (5.33, Reject) — self-supervised motion prediction.

**Final score: 4.5** — SigMap has genuine strengths (well-specified geographic prompt mechanism, parameter efficiency) but the core masking method is underspecified, numerical inconsistencies undermine confidence, and key SSL baselines are absent. Below the ICLR acceptance bar.

---

## Summary

SigMap proposes a self-supervised pre-training + prompt-based fine-tuning framework for wireless localization. The two key innovations are (1) a cycle-adaptive masking strategy that dynamically adjusts mask patterns based on CSI periodicity to prevent shortcut learning, and (2) a "map-as-prompt" framework that encodes 3D geographic information via GNNs into soft prompts for parameter-efficient fine-tuning. The model is evaluated on simulated ray-tracing data (DeepMIMO, WAIR-D) and shows improvements over OMP, CNN, SWiT, and LWLM on single-BS and multi-BS localization tasks.

## Strengths

1. **Geographic prompt mechanism is well-specified and shows consistent, measurable gains.** Tables 1, 2, and 4 demonstrate that incorporating 3D map information via GNN-based prompts improves accuracy across all settings (single-BS MAE: 1.564 m with map vs 2.275 m without; multi-BS MAE: 0.673 m vs 0.789 m). The progressive degradation from 3-D → 2-D → no-map in Table 4 provides clear evidence that the mechanism actually leverages spatial structure, and the 2-D variant retaining most of the benefit (1.692 m vs 1.564 m) is an informative finding with practical implications.

2. **Parameter efficiency is concretely demonstrated with resource figures.** Table 5 reports only 0.085 M trainable parameters (0.7% of 11.73 M total) during fine-tuning, with the full process taking 30 minutes and inference at 0.83 ms/sample. This is a genuine practical advantage for deployment and is backed by specific numbers.

3. **Cycle-adaptive masking improves MAE and CDF@1m over fixed strategies.** Table 3 shows adaptive masking achieves 0.673 m MAE and 84.5% CDF@1m vs. grid-masking (0.770 m, 80.3%) and strip-masking (0.753 m, 75.3%), supporting the claim that disrupting periodic shortcuts is beneficial for representation learning.

## Weaknesses

### Major

1. **Core method (cycle-adaptive masking) is underspecified to the point of irreproducibility.** The cycle-adaptive masking is the paper's headline contribution, yet the derivation of `d_final` (the detected periodicity shift in Eq. 6) is never explained. The paper states only that "we compute shift patterns using cross-correlation analysis" (line 133), without providing: (a) the formula for the cross-correlation, (b) what dimensions of the CSI tensor it operates on, (c) how the periodicity shift is extracted from the cross-correlation output, or (d) how `j_0` and `w` in Eq. 6 are determined. Without this information, the central claimed contribution cannot be reproduced, and it is impossible to verify whether the adaptive masking is doing something substantively different from standard random or structured masking. This is the most serious weakness — a method paper at a top conference must disclose its algorithms.

2. **Multiple numerical and factual inconsistencies undermine confidence in the reported results.** Several claims in the text disagree with the tables or are internally inconsistent:
   - **1.580 m vs 1.880 m**: The text (line 340) states "1.580 m on WAIR-D Scenario-2" but the generalization table (line 336) shows **1.880 m**. One of these is wrong.
   - **0.4% vs 0.7%**: Section 4.5 claims "updating only 0.4% of parameters" while Section 4.6 states "0.7% of the total parameters" (confirmed by Table 5: 0.085 M / 11.73 M = 0.72%). These are inconsistent.
   - **"Zero-shot" vs few-shot**: The abstract and contributions claim "strong zero-shot generalization," but the generalization experiments (Section 4.5) fine-tune on "approximately 100 instances per scenario." This is few-shot, not zero-shot — a factual overclaim.
   
   These errors, taken together, suggest insufficient rigor in data reporting.

3. **Missing comparison against directly relevant SSL baselines.** The introduction (lines 26–27) critically discusses CrowdBERT (Han et al., 2024), signal-guided masked autoencoders (Wang et al., 2025), and WirelessGPT (Yang et al., 2025) as prior SSL-based localization methods, specifically arguing they are "confined to specific configurations" and have "limited generalizability." Yet none of these appear in the experimental comparison. Without evaluating against the methods the paper claims to improve upon, the reader cannot assess the actual contribution. (SWiT = Salihi et al., 2024 is included, partially mitigating this, but the gap is still substantial.)

### Minor

1. **Unexplained "NLoS-aware attention mechanism" appears mid-results.** Equation (11) in Section 4.2 introduces an attention mechanism with notation (`phi`, `o_s`, `W_NLoS`) that is never defined, and this component is not described anywhere in the Methodology section (Section 3). It is unclear whether this is part of SigMap's architecture or a separate post-hoc analysis. If it is part of the method, its absence from Section 3 is a serious omission; if it is not, its placement in the results discussion is misleading.

2. **"Foundation model" framing is significantly overstated.** Pre-training is conducted on a single simulated scenario (DeepMIMO O1_3p5) and evaluated on only two localization tasks. A foundation model — in the sense the term has acquired in the literature — implies pre-training on diverse, large-scale data yielding general-purpose representations transferable to many tasks. A single-environment, single-task-family method is a domain-specific pre-trained model, not a foundation model. This overclaim sets expectations the paper cannot meet.

3. **Generalization evaluation is thin.** For cross-scenario generalization (Section 4.5), only LWLM is compared. CNN, SWiT, and OMP are dropped without explanation. If these were evaluated and performed worse, reporting them would strengthen the claims; if not evaluated, the comparison is incomplete. Additionally, no error bars are reported despite claiming "5 independent runs" — statistical significance cannot be assessed.

4. **Figure reference error.** Section 4.4 refers to "Figure 1" for map ablations, but Figure 1 is the wireless propagation paths figure from the preliminaries, not the ablation visualization.

### Trivial

1. The RMSE result in the masking ablation (Table 3) shows strip-masking achieving the best RMSE (0.972 m vs adaptive's 1.099 m) — the adaptive strategy has worse outlier performance — but the text selectively reports MAE and CDF@1m without discussing this.

## Nice-to-Haves

- Include at least one real-world CSI dataset or explicitly acknowledge the sim-to-real gap as a limitation
- Ablate the pooling strategy for the geographic prompt (global mean pooling over potentially hundreds of vertices is a severe information bottleneck)
- Analyze what the learned prompt tokens capture via visualization or probing
- Justify or ablate the 1000-epoch fine-tuning schedule (unusually long for prompt tuning)

## Removed Points

1. **Criticism about OMP being a "classical method" comparison** — OMP is included as a classical reference baseline, not a primary competitor. SWiT and LWLM are the main learned baselines. Removed.

2. **Criticism about "foundation model" framing being "fatal"** — demoted to Minor. It is an overclaim, but the paper's results stand on their own regardless of the label; the technical contribution is not invalidated by the framing.

3. **Criticism about RMSE in masking ablation being "contradictory"** — partially removed from significance. The paper claims "best trade-off" considering MAE and CDF@1m (on which adaptive wins), but should discuss the RMSE degradation. Retained as Trivial rather than Major.

4. **Criticism about CrowdBERT/WirelessGPT not being "available" or "released"** — the hard rules forbid questioning existence of cited references. However, the criticism that they are not evaluated remains valid and is kept as Major weakness #3.

5. **Criticism about needing "larger dataset" or "more model comparisons" generically** — weakened. The current dataset size is sufficient for the paper's stated scope. The specific missing baselines (CrowdBERT, etc.) are retained.

6. **Strength Finder's "strong zero-shot generalization"** — weakened because it's actually few-shot. The numerical results are still strong, but the framing is wrong.

7. **Strength Finder's generic/problem-importance strengths** — removed as they lack specific evidence.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Fully specify the periodicity detection algorithm: provide the cross-correlation formula, state which CSI dimensions are correlated, describe how `d_final` is extracted from the correlation output, and specify how `j_0` and `w` are determined.
2. Add at least CrowdBERT or signal-guided MAE as experimental baselines, or explicitly explain why comparison is infeasible (e.g., different input modalities, incompatible settings).
3. Correct the numerical inconsistencies: reconcile 1.580 → 1.880, 0.4% → 0.7%, and replace "zero-shot" with "few-shot" throughout.
4. Move the NLoS-aware attention mechanism (Eq. 11) to the Methodology section with full definitions, or remove it from the results discussion.
5. Fix the Figure 1 reference in Section 4.4.
6. Add error bars or confidence intervals for all main results.
7. Tone down the "foundation model" framing to match the actual pre-training scope (single scenario, two tasks).


MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>