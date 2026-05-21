Now I have all the information I need. Let me compose the final consolidated review.

## Summary

PI-CCA proposes a replay-free continual learning method for vision-language models that preserves cross-modal alignment by explicitly constraining the canonical correlation spectrum and subspaces via a compact sketched certificate (CCA certificate). The key idea is to treat forgetting as alignment-geometry drift rather than matching proxy quantities (similarities, logits, weights). The method also incorporates prompt-invariant certificate averaging for robustness to phrasing variation. Across four VL-CL benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL), PI-CCA achieves state-of-the-art performance among replay-free methods and even surpasses a synthetic-replay method without storing or generating data.

---

## Strengths

1. **Novel and principled geometry-first approach to replay-free VL-CL.** The paper reframes forgetting as drift in the alignment geometry of the whitened cross-modal covariance (CCA spectrum and subspaces), which is conceptually well-motivated and contrasts with prior methods that regularize proxy signals (similarities, logits, parameters). The CCA certificate compresses this alignment skeleton into constant memory via random orthonormal sketches (Eq. 4), which is technically clean.

2. **State-of-the-art empirical results across four benchmarks.** Tables 1 and 2 show consistent improvements: MTIL Avg 76.8 (vs. 75.2 next best), X-TAIL Avg 68.1 (vs. 67.4), VLCL I2T R@1 48.6±1.0 (vs. 47.3±1.2), ConStruct-VL FA 75.2±1.3 (vs. 73.9±1.5). Notably, PI-CCA surpasses GIFT (a synthetic-replay method) without storing or generating data.

3. **Strong ablations and robustness analyses.** Table 3 systematically ablates each component—removing the spectral or subspace term causes the largest drops (2.5 and 2.2 pp on MTIL Avg), confirming both are necessary. Figure 5 shows narrow interquartile ranges across 20 random task orders, demonstrating that performance is not an artifact of a particular sequence. The certificate capacity Pareto analysis (Figure 2) provides practical guidance for choosing (k, h).

4. **Prompt-invariance mechanism is well-designed and empirically validated.** The projector averaging over M perturbation samples (Eq. 5–6, 11) is a thoughtful solution to an often-overlooked problem. Figure 4 shows consistent flattening of degradation slopes: at perturbation strength s=1.0, R@1 improves by +2.44 pp (ID) and +2.51 pp (OOD) over the ablated model.

---

## Weaknesses

### Fatal
None.

### Major

1. **Suspiciously high correlation values in Figure 3 require clarification.** The paper reports Pearson r = 1.00 and Spearman ρ = 1.00 for two of four panels, and r = 0.99 / ρ = 1.00 for the other two. Spearman ρ = 1.00 in all four panels means the rank ordering between drift measures and performance drops is *perfectly* preserved across diverse perturbations (certificate size, EMAs, invariance strength, LoRA capacity/LR, sketch type). This is unusual for real data with any scatter, and the paper itself describes "realistic scatter" in the caption. Two issues arise:

   - **Precision.** Values are given to only 2 decimal places. With "realistic scatter," values like 0.998→1.00 or even 0.95→1.00 could occur depending on precision conventions. The authors should report these to at least 3 decimal places and clarify the number of data points in each panel.
   - **Interpretation.** A Spearman ρ of 1.00 across qualitatively different perturbations (changing a hyperparameter vs. changing the sketch type) implies the drift measures perfectly rank-order performance. Even if mathematically possible for an intrinsic property of the method, this deserves explicit discussion rather than a bare caption number.

   This does **not** invalidate the method's empirical results, but it undermines the paper's strongest conceptual evidence. A correlation of 0.7–0.9 with clear, interpretable scatter would be more convincing than numbers that strain credibility at first glance. The paper's core contribution—the method and its SOTA results—stands independently; the correlation analysis should be fixed for the archival version.

### Minor

2. **Missing confidence intervals on classification benchmarks.** Table 1 (MTIL and X-TAIL) reports point estimates without variance, while Table 2 (VLCL and ConStruct-VL) includes ± intervals. This inconsistency makes it impossible to assess whether the +1.6 gain over C-CLIP on MTIL or the +0.7 gain on X-TAIL is statistically significant. The authors should report CIs (or at least standard deviations across seeds) for all main tables.

3. **Baseline number provenance is not specified.** The paper does not state whether baseline results are taken from original papers or re-run under identical conditions. If taken from original papers, differences in backbone, LoRA configuration, batch size, and evaluation protocols could contribute to gaps. If re-run, the configuration should be documented. This is a standard reporting requirement.

4. **No fully-ablated ("task loss only") baseline.** The ablation study (Table 3) removes one component at a time, but no row removes *all* regularization terms simultaneously (λ₁=λ₂=λ₃=0, α=β=0). Such a baseline would cleanly establish the lower bound for the method and quantify the total contribution of the CCA losses relative to naive LoRA fine-tuning. The closest ablations (w/o spectral term at 74.3, w/o covariance EMA at 74.1) still retain other regularization components.

5. **Computational cost of prompt perturbations not discussed.** The ℒ_pi loss requires computing M top-k SVDs per batch (M=4 by default). Even with sketching (h=256) and block power iteration, this incurs non-trivial overhead. The paper should report per-step wall-clock time for the full model vs. ablated models (with and without ℒ_pi) to help practitioners assess the trade-off.

### Trivial

6. **Stop-gradient on Σ^{-1/2} is mentioned but not explained.** The paper states that the inverse square root is followed by stop-gradient "if needed" (Section 3.4), but does not discuss whether gradients actually flow through the whitening or why it is beneficial to stop them. This is a minor technical omission.

7. **Ridge coefficients γ_v, γ_t appear in Eq. 1 but are not discussed in the main text.** The paper defers this to the appendix (which is stripped by the parser). These coefficients affect the whitening and thus the CCA estimate; their impact should be acknowledged briefly in the main text.

---

## Nice-to-Haves

- A controlled experiment isolating the "geometry vs. proxy" claim (e.g., adding PI-CCA's spectral/subspace losses to a strong proxy-based baseline and measuring improvement) would strengthen the conceptual narrative but is not required for the method's validity.
- Discussion of EMA bias under distribution shift—the streaming covariance estimates use EMA on non-stationary data, which will be biased toward recent tasks. The momentum β balances stability and plasticity; acknowledging this trade-off would improve the paper.

---

## Removed Points

These points from the reviewers were removed with justification:

- **Code availability criticism** ("Due to ongoing commercial use, we cannot release the code during review"): Removed per hard rule—criticisms questioning the release status of cited entities are not permitted. The paper promises release upon acceptance.
- **Missing related works**: Removed per hard rule—cannot confirm existence of un-cited works.
- **"The method is not causally shown to be better because it targets invariants"** (from the conceptual overclaiming argument, the strongest version): This point was weakened. The paper provides correlational evidence and ablations linking geometry preservation to performance; while a controlled swap experiment would strengthen the claim, the available evidence supports the interpretive lens. The remaining concern is captured in the Major weakness about Figure 3's precision.
- **Speculation about orth() dynamics accumulating drift**: Removed—this is pure speculation without evidence of a problem.
- **"Could be overfitting to perturbation distribution in Figure 4"**: Removed—the paper uses ID and OOD templates, and the test-time perturbations differ from those used in training (which is the standard setup).
- **"Prompt-invariance mechanism is computationally heavy"** (overstated): The M=4 SVDs on h=256 sketched matrices is not prohibitive; the computational cost point is retained as Minor (item 5 above) rather than a major concern.
- **"Figures 4 stress test: modest gains"**: The gains are consistent and shown across two settings; "modest" is a subjective framing that the paper's own numbers support as meaningful.

---

## Novel Insights

Beyond the paper's own contributions, the reviewer synthesis surfaces a subtle tension: the near-perfect correlation values in Figure 3, if taken at face value, would be the strongest empirical confirmation of the "geometry drift hypothesis" in the VL-CL literature, but they are also *too perfect* to be persuasive as reported. This creates a credibility gap between what the paper claims and what a critical reader will accept—a gap that is fully fixable by reporting more precise coefficients and discussing the data. Additionally, the ablation table reveals an asymmetry worth noting: disabling the streaming EMA (β=0) hurts more than disabling the certificate EMA (α=0), suggesting that noisy cross-modal covariance estimates are a larger bottleneck than stale certificate references. This finding is not highlighted in the paper and could guide future work on streaming CCA estimation.

---

## Suggestions

1. **Fix Figure 3's correlation reporting.** Report values to 3+ decimal places, state the number of data points, and provide a table or caption that explains which perturbations were swept and how many configurations each sweep produced. If the values are genuinely 0.998+, briefly explain why the relationship is so tight (e.g., because all perturbations are of the same base method and the drift measures directly capture the loss terms being optimized).

2. **Add confidence intervals to Table 1** (MTIL and X-TAIL) for consistency with Table 2. Run at least 3 seeds and report standard deviations or bootstrapped intervals.

3. **Specify baseline number sources** explicitly in Section 4.1 (e.g., "C-CLIP, Mod-X, ZSCL numbers are from the original papers; ZAF numbers are re-run under our protocol with configuration in Appendix §A.2").

4. **Add a fully ablative baseline** (λ₁=λ₂=λ₃=0, α=β=0) to Table 3 to establish the unregularized lower bound.

5. **Report wall-clock overhead** of the prompt-invariance module to help practitioners understand the computational cost of the M=4 default.

6. **Clarify the stop-gradient design choice**—why gradients are stopped through Σ^{-1/2} and what effect this has on learning.

---

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak band (<3.5): LVLM-CL (2.50), Stabilize continual learning hyperspherical replay (3.00), Multimodal Class-Incremental Learning benchmark (2.33), Maintaining Adversarial Robustness (3.25). PI-CCA is clearly above all of these—it has a well-engineered method with SOTA results, unlike these which are position/benchmark papers with limited novelty or incomplete results.
- Middle band (3.5–7.5): **C-CLIP (6.50)**—a direct baseline that PI-CCA outperforms across all benchmarks. C-CLIP was accepted as a poster with scores 6,6,8,6. Its reviews noted missing code, presentation issues, and incomplete baselines. PI-CCA has stronger method novelty, cleaner writing, and more thorough analysis, placing it above C-CLIP. Other middle-band anchors: Language Guided Representation Learning (4.20, reject), TIPS (4.50, withdrawn), Vision and Language Synergy (5.00, poster with split 3,3,6,8).
- Strong band (>7.5): Compositional Entailment Learning (8.00, oral), Modality Gap analysis (8.00, oral), Function Vectors for CF (9.00, oral), Meta-CL (8.67, oral). These papers have broader impact, more rigorous theoretical/narrative framing, or address larger questions. PI-CCA does not reach this tier.

**Round 2 (Narrowing, bracket 5.5–7.5):**
- C-CLIP (6.50): As above, PI-CCA is clearly stronger. Better method, better results, better writing.
- TTA with CLIP Reward (6.67, accepted poster): A well-written paper with a simple, broadly applicable idea across three tasks. PI-CCA has deeper technical novelty and more thorough evaluation on domain-specific benchmarks.
- Demystifying CLIP Data (6.75, spotlight): A data-centric analysis paper with high impact. PI-CCA is a different type of contribution but comparably rigorous.
- Towards flexible perception with visual memory (5.75, reject): Thin novelty and mixed reviews. PI-CCA is substantially stronger.

**Final calibration:** The round-2 anchors suggest a score of approximately 7.0. PI-CCA is better than the C-CLIP baseline (6.5) and the TTA paper (6.67) in terms of technical novelty, evaluation thoroughness, and writing quality. However, the correlation analysis concern in Figure 3 and the missing CIs on classification benchmarks prevent it from reaching the 8+ tier of the strong-band papers. A score of 7.0 reflects a solid paper with a genuine methodological contribution, SOTA results, and mostly thorough analysis, but with non-trivial reporting issues that need fixing.

### Score

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>