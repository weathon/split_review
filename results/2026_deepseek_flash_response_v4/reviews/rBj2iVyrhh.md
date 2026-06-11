## Summary

CCAT proposes a two-stage framework for modality imbalance in multimodal learning. Stage 1 pre-trains a shared classifier with bidirectional cross-attention and a contribution-regularization term that penalizes disparities between modalities' mutual-information-based contribution scores. Stage 2 freezes this classifier during modality-alternating training, adds modality-specific LoRA adapters to handle the distribution mismatch between fused and unimodal features, and applies sample-level secondary updates to severely imbalanced samples. Results are reported on CREMA-D, Kinetic-Sound, and MVSA.

## Strengths

1. **Classifier freezing as a targeted fix for a real limitation of alternating training (Section 1, paragraph 2; Section 3.3; Table 2).** The paper correctly identifies that encoder-level alternating training (e.g., MLA) leaves the shared classifier biased toward the dominant modality. CCAT's solution — pre-training a classifier with contribution regularization and freezing it during alternating training — directly addresses this. The ablation (Table 2) shows removing classifier freezing drops CREMA-D multimodal accuracy from 85.89% to 82.80%, confirming this component matters.

2. **Creative use of LoRA adapters to bridge the fused-feature vs. unimodal-feature distribution mismatch (Section 3.3, Equations 9-10).** The paper recognizes a non-trivial technical challenge: a classifier pre-trained on fused features (P(f|y)) must process unimodal features (P(z^m|y)) during alternating training. The modality-specific LoRA modules as additive corrections to the frozen classifier's logits are a clean architectural fix. The ablation shows LoRA contributes +1.21% on CREMA-D.

3. **Consistent gains across three diverse benchmarks (Table 1).** CCAT achieves 85.89% on CREMA-D (+2.27% over LFM), 79.29% on Kinetic-Sound (+6.76% over LFM), and 80.73% on MVSA (+1.92% over MMPareto). The improvements hold across audio-visual (CREMA-D, KS) and text-image (MVSA) modality pairs.

4. **Thorough hyperparameter documentation (Table 3, Figure 4).** The paper conducts separate grid searches for LoRA rank r and imbalance threshold β on each dataset, finding dataset-specific optima (e.g., r=2 for CREMA-D/KS, r=8 for MVSA). This suggests the framework adapts to different imbalance patterns rather than being tuned to a single configuration.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaimed theoretical novelty in Section 3.1.** The paper states it provides "a new theoretical framework" (line 26), a "profound theoretical isomorphism" (line 87), and a "unified theoretical framework" (line 59) connecting class and modality imbalance. In reality, Section 3.1 presents standard cross-entropy gradient equations (Eq. 1-3) that are definitional consequences of what class/modality imbalance *is* — the paper correctly observes the parallel but does not prove a theorem, derive a bound, or establish any non-trivial result. The connection is a useful intuition that motivates the frozen-classifier design, but claiming "a new theoretical framework" overstates what is delivered. This overclaiming could undermine reviewer trust in the rest of the paper.

2. **No standard deviations or confidence intervals for any main result (Table 1).** The paper reports "average test accuracy (%) of three random seeds" but omits variance entirely. For improvements of moderate size (+1.35% on CREMA-D, +1.92% on MVSA), the reader cannot evaluate whether these reflect a genuine advance or noise. This is a standard expectation for experimental ML papers.

3. **Clustering metrics computed on t-SNE embeddings are not meaningful (Section 4.4).** t-SNE is a nonlinear dimensionality reduction that systematically distorts distances. Computing Calinski-Harabasz, Silhouette, and Davies-Bouldin scores on t-SNE projections measures the quality of the *visualization*, not the quality of the original feature space. These metrics should have been computed on the original penultimate-layer representations, not on t-SNE embeddings.

### Minor

4. **The ablation conflates pretrained initialization with freezing (Table 2, row 1).** Removing "classifier freezing" (Fix=✗) removes both the frozen state and the pretrained initialization simultaneously. The paper does not ablate: (a) using the pretrained classifier but not freezing it, or (b) freezing a randomly initialized classifier. Without these controls, it is unclear whether the benefit comes from the pretrained initialization, the freezing, or both. This matters because the paper's central argument is about the *freezing* preventing structural classifier bias.

5. **The +6.76% gain on Kinetic-Sound (72.53% → 79.29%) is large by the standards of this literature and receives limited explanation.** The paper attributes it to "liberating weak modalities' representational potential" but does not provide per-class accuracy breakdowns, representation similarity analysis, or ablations that isolate which component primarily drives this dataset-specific gain. While the result is not inherently suspicious, deeper analysis would strengthen confidence.

6. **The mutual information estimator (Eq. 5) is cited from Zhou et al. (2025b) but the notation (f̄ᵢ, z̄ᵢ^m) is not defined in the main text, and the formula is not explained.** The expression involves a log-sum-exp structure that does not match a standard MI estimator. Clarifying this would help reproducibility.

7. **Missing comparison with PMR (Fan et al., 2023) and CML (Ma et al., 2023),** which are mentioned in Related Work but absent from the main comparison table (Table 1). While the baseline set is already substantial, including these would strengthen the comparison.

### Trivial

8. Minor internal inconsistency: the paper describes LoRA as a "low-rank residual correction applied to the features" (line 167), but Eq. 10 shows the LoRA output is added to the classifier output *before* softmax — i.e., at the logit level. The math is correct either way; the description and equations should match.

## Nice-to-Haves

- An analysis of whether the contribution regularization (Eq. 7) forces equal contributions at the cost of representation quality. The classification loss (L_cls) in Eq. 8 mitigates this concern, but explicitly checking that the pretrained fused features remain discriminative would strengthen validation.
- A simple baseline training the full model (no alternating training, no frozen classifier) with the same LoRA modules would help isolate the contribution of the alternating+freezing mechanism.
- An analysis of why β thresholds vary so much across datasets (0.05 for MVSA vs. 0.30 for KS) and whether performance degrades gracefully when β is misspecified.

## Removed Points

These points were flagged for removal but are retained here for reference:

- **"Contribution regularization is circular" (harsh critic's Issue 2):** Removed because the regularization is *by design* targeting the measured imbalance — this is how all regularization works. The concern about "equally uninformative" features is addressed by the classification loss term (L_cls) in the total loss (Eq. 8).

- **"Large KS gains are suspicious / could be configuration mismatch" (harsh critic's Issue 3):** Removed because raising the need for more analysis is reasonable (kept as Minor #5), but speculating about "configuration mismatch" without evidence is not supported.

- **"Unimodal evaluation heterogeneity across baselines" (harsh critic):** Removed because the paper explicitly describes (lines 224-229) that different baseline architectures require different evaluation protocols. This is standard practice.

- **"LoRA α=1 analysis is missing" (harsh critic):** Removed because the paper notes that α is insensitive due to "classifier's limited parameter scale" (lines 244-245). This is a minor empirical observation, not a missing analysis.

- **"No theorem, lemma, or formal result" (harsh critic):** Subsumed by Major #1 (overclaimed theoretical novelty). The section already delivers useful intuition; the problem is the overclaiming, not the absence of formal results.

## Novel Insights

The critic's observation that the ablation conflates pretrained initialization with freezing (Minor #4) is the most actionable finding: it identifies a genuine experimental gap that directly relates to the paper's central claim about freezing preventing structural classifier bias. The critic's note about t-SNE clustering metrics (Major #3) is also a technically correct concern that many papers overlook. Beyond these, no genuinely novel synthesis emerges beyond the paper's own contributions.

## Suggestions

1. Reframe Section 3.1 as motivation/intuition rather than a "theoretical framework" — this will improve reviewer trust and accurately represent what the section delivers.
2. Add standard deviations or 95% confidence intervals to all main results (Table 1).
3. Replace t-SNE-based clustering metrics with metrics computed on the original feature space.
4. Add controlled ablations separating pretrained initialization from freezing (random init + freezing, pretrained + unfrozen).
5. Provide per-class accuracy or representation similarity analysis to explain the large KS gain.
6. Define all notation in Eq. 5 and explain the MI estimator.
7. Consider comparing with PMR and CML, or explain their omission.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- `/a4O528mek9.md` — 3.00 — Incomplete multimodal data; weaker empirical validation and writing quality. CCAT is stronger.
- `/ul1cjLB98Y.md` — 5.25 — "A Theory of Unimodal Bias in Multimodal Learning" (Reject). Stronger theory but limited experiments. CCAT has stronger empirical contributions but overclaims theory. CCAT is slightly stronger overall.
- `/5BXWhVbHAK.md` — 6.33 — "Can One Modality Model Synergize Training of Other Modality Models?" (Accept). Has formal theoretical proofs and broad experiments. CCAT has weaker theory but comparable experiments. CCAT is slightly weaker.
- `/TPZRq4FALB.md` — 8.00 — "Test-time Adaptation against Multi-modal Reliability Bias" (Accept). Strong motivation, extensive experiments, novel problem. CCAT does not match this level.

**Round 2 (Narrowing within bracket):**
- `/1L52bHEL5d.md` — 6.00 — "Test-Time Adaptation for Combating Missing Modalities" (Accept). Solid problem framing, comprehensive experiments. CCAT is slightly weaker due to overclaimed theory and missing std devs.
- `/rObkvzJxTG.md` — 5.50 — "Smoothing the Shift" (Accept). Comparable quality — both have clear contributions and notable weaknesses. CCAT's empirical validation across more diverse modality pairs gives it a slight edge.
- `/BZWssJoYEv.md` — 5.50 — "Towards Holistic Multimodal Interaction" (Reject). Confusing theoretical presentation. CCAT has clearer practical contributions.

**Initial bracket:** 5.0–6.5 based on comparison with Round 1 anchors.

**Narrowing rationale:** CCAT is clearly stronger than the "Unimodal Bias" paper (5.25) due to stronger experiments and practical contributions, but weaker than the "Synergize" paper (6.33) which had formal theoretical proofs. CCAT is comparable to "Test-Time Adaptation for Combating Missing Modalities" (6.00) but with more fixable weaknesses, and comparable to "Smoothing the Shift" (5.50, Accept) with a slight empirical edge. The final score of 5.5 reflects a borderline-accept paper: a practically sound method with consistent empirical results, but marred by overclaimed theoretical novelty and missing experimental details (std devs, t-SNE metrics) that are fixable in revision.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>