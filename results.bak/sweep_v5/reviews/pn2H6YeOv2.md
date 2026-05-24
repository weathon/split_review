Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes PI-CCA, a replay-free continual learning framework for vision-language models that preserves cross-modal alignment by directly constraining the canonical correlation spectrum and subspaces (the "CCA certificate") of image-text embeddings. The certificate is stored compactly via random sketches, and training enforces spectral/subspace consistency plus prompt invariance through a perturbation-averaging mechanism. Across MTIL, X-TAIL, VLCL, and ConStruct-VL, PI-CCA achieves state-of-the-art results among replay-free methods and even surpasses a synthetic-replay baseline.

## Strengths

- **Novel and principled approach to VL-CL.** The framing of forgetting as alignment-geometry drift (rather than proxy-signal decay) and the use of CCA invariants as the consolidation target is conceptually clean and moves beyond distillation, logit-matching, or prompt-based methods. The paper directly targets the whitened cross-covariance that underpins CLIP's zero-shot retrieval, which is a well-motivated first-class object to preserve.

- **Strong empirical results across four distinct VL-CL benchmarks.** Tables 1 and 2 show PI-CCA achieving the highest Avg/Last/Transfer on MTIL (76.8/75.5/73.2) and X-TAIL (68.1/66.9/64.7), best retrieval on VLCL (I2T R@1 48.6), and best FA/AF on ConStruct-VL (75.2/2.7). Crucially, it outperforms the synthetic-replay method GIFT (Table 2) without storing or generating any past data — directly delivering on the paper's core claim of replay-free, generator-free consolidation.

- **Component-wise ablation validates each loss term independently.** Table 3 shows that removing the spectral term (λ₁=0) drops MTIL Avg by 2.5 points, removing the subspace term (λ₂=0) drops it by 2.2, removing prompt invariance (λ₃=0) drops it by 1.5, and disabling covariance EMA (β=0) drops it by 2.7. These controlled degradations empirically confirm that both spectral and directional components of the certificate are necessary, and that the prompt-invariance mechanism provides a distinct benefit.

- **Certificate capacity Pareto analysis (Figure 2) demonstrates practical efficiency.** The sweep over (k, h) reveals a broad Pareto ridge with a stable knee at (64, 256), confirming that the certificate can be "small yet sufficient" with constant memory relative to feature dimension — a key practical strength for deployment.

- **Low task-order sensitivity (Figure 5).** Boxplots over 20 random MTIL orders show narrow IQRs (Avg range ~1.4 p.p.), confirming that PI-CCA's retention is robust to ordering, not reliant on a favorable sequence.

## Weaknesses

### Major

- **Implausible perfect correlation values in Figure 3 without explanation.** The paper reports Pearson r=1.00 and Spearman ρ=1.00 for two of the four panels in Figure 3 (angle drift vs. ΔAvg and ΔR@1), and r=0.99 / ρ=1.00 for the spectral drift panels. With "realistic perturbations" sweeping certificate size, EMAs, invariance strength, whitening, pairing, LoRA capacity/LR, and sketch type (line 235), perfect or near-perfect rank correlation across all these independent axes is practically impossible unless the number of distinct data points is trivially small or the relationship is mathematically deterministic — neither of which is discussed. The paper simultaneously describes "realistic scatter" and shows a "95% confidence interval," which is inconsistent with r=1.00 (zero residual variance). This figure is presented as core evidence that "preserving CCA geometry predicts retention" (line 245). While the qualitative trend (strong positive correlation) is almost certainly real, the specific rounded-to-exact-1.00 values raise a serious rigor concern that the authors must address: (a) how many distinct (drift, drop) pairs are plotted? (b) are these values rounded from e.g., 0.9996? (c) could some of these drifts and drops be deterministically linked? This does not invalidate the paper's central claim — the trend is independently supported by the ablation study (Table 3) — but it undermines the evidential weight of Figure 3 as presented.

### Minor

- **"Constant-memory" claim is imprecise.** The abstract and introduction describe PI-CCA as a "constant-memory path" (line 20) and "constant-memory consolidation mechanism" (line 38). The *certificate* storage is indeed O(hk) and constant w.r.t. d, which the paper correctly explains (line 88). However, the streaming estimation (Section 3.4) maintains EMA copies of the full covariance matrices Σ_vv, Σ_tt, Σ_vt, each of size O(d²) — for CLIP ViT-B/16 (d=512), this is about 0.75M entries. While modest in absolute terms (~3 MB float32), this contradicts the literal reading of "constant-memory." The authors should either clarify that the claim refers to the stored certificate alone (not the full training footprint) or acknowledge this O(d²) component explicitly.

- **Computational cost of the prompt-invariance term ℒ_pi is not analyzed.** As described in lines 128-130, each of M prompt perturbations requires computing a separate top-k SVD of the whitened cross-covariance (M=4 in the stress test), multiplying the per-step SVD cost by roughly 5×. The paper never reports wall-clock time with and without ℒ_pi, nor ablates the overhead across different M or λ₃ values. The Pareto analysis in Figure 2 measures the full method's step time but does not isolate the cost of ℒ_pi, making it impossible for readers to assess the trade-off between the +2.44 p.p. R@1 gain (Figure 4) and the added computation.

- **No results on larger backbones.** All experiments use CLIP ViT-B/16 (d_v=d_t=512). The CCA computation involves SVD of d×d matrices (Eq. 2), which for ViT-L (d=768) would be about 2.25× larger. The paper does not discuss scalability to larger backbones or whether the d×d matrix inversion/SVD would become a bottleneck.

- **Missing sensitivity analysis on EMA rates β and α.** Table 3 ablates α=0 and β=0 as on/off, but does not sweep these hyperparameters over plausible ranges (e.g., 0.01, 0.05, 0.1, 0.5) to characterize the stability–plasticity trade-off they control.

### Trivial

- The figure caption for Figure 2 mentions "color encodes AF" in the 3D plot but does not describe the color bar values in the caption text (though this may be visible in the figure image itself).

## Nice-to-Haves

- An experiment comparing against a simpler alignment regularizer (e.g., Frobenius norm of the cross-covariance matrix without CCA whitening) would help isolate the benefit of the CCA-specific invariants.
- Testing with different pre-training checkpoints for the initial certificate would reveal sensitivity to the quality of the starting alignment.
- An analysis of how quickly the streaming CCA estimates (EMA of covariances) deviate from the true joint distribution as tasks accumulate would inform practical deployment.

## Removed Points

**From the Harsh Critic:**
- "Suspicious perfect correlations ... If the correlation is fabricated or misleading, the central claim of the paper collapses" — The accusation of fabrication is speculative and unsupported. The concern about the r=1.00 reporting is real and kept as a Major weakness, but the framing as deliberate fabrication is removed.
- "The paper provides no explanation for why these correlations are perfect, and no confidence intervals or raw data are shown" — The paper states "95% confidence interval shaded area" is shown (line 241), so the CI claim is factually wrong. Kept the core objection about unexplained perfect values; removed the false CI claim.
- "Constant-memory claim is false (Structural)" — Downgraded from Structural to Minor. The certificate storage is indeed constant-memory; the O(d²) EMA covariances are training state, not stored as the certificate. The claim is slightly imprecise but not false.
- "Computational cost of prompt-invariance term is not analyzed (Methodological gap)" — Kept as Minor (real concern), downgraded from the harsh critic's "structural/methodological gap" framing.
- "The 'stable whitening' subsection ... does not state explicitly whether gradients flow through the SVD" — The paper says on line 144: "gradients are propagated to Ẑ (and hence to Σ), not through the certificate." This is stated explicitly. Removed.
- "Figure 3 lack of raw data" — The figure shows scatter plots with 95% CI, which is standard. Removed.
- "3 seeds per order, more seeds would strengthen" — 3 seeds per order with 20 orders (60 runs total) is reasonable. Removed as generic.
- Missing experiments about varying pre-training certificate, comparing to simpler regularizer, scalability — These are nice-to-haves, moved to that section.
- "Ablation study with no confidence intervals or significance tests" — Standard in this subfield; single-factor ablations on benchmarks are typically reported as point comparisons. Removed.

**From the Strength Finder:**
- Strength 3 (geometry-performance correlation) — Kept but note the correlation reporting concern. The qualitative trend is real.
- None of the strengths were generic enough to warrant removal — all are concrete and evidence-backed.

## Novel Insights

Beyond the paper's own contributions, the most interesting emergent observation is that the ablation study reveals nearly equal importance of the spectral term (λ₁) and the subspace term (λ₂) — removing either causes 2.2–2.5 p.p. drops on MTIL. This suggests that both *what* canonical correlation strength is retained and *which* direction the canonical subspaces point matter independently, rather than one being derivative of the other. This is a nontrivial finding: a practitioner might expect that preserving the spectrum implicitly preserves the subspace, but the ablation shows they are complementary constraints. Separately, the fact that the prompt-invariance mechanism works through projector averaging (which eliminates sign/rotation ambiguity without Procrustes alignment, line 102) is a neat technical trick worth noting.

## Suggestions

1. **Clarify Figure 3.** Report correlations to 3-4 decimal places, state the number of data points, and explain whether any of the drift/performance-drop pairs are deterministically linked. If the r=1.00 values are artifacts of rounding from e.g., 0.9996, say so explicitly. If the number of points is small, a non-parametric visualization (e.g., a table of the configurations) may be more informative than scatter plots with suspect fit lines.

2. **Reconcile "constant-memory" language.** Either qualify that the claim applies to the stored certificate (not the full training state) in the abstract and contributions, or show that the EMA covariances can themselves be sketched without loss.

3. **Report wall-clock time ablation for ℒ_pi.** Measure per-step time with M=0, M=4 across a few (k,h) configurations to let readers assess the overhead.

4. **Add a brief sensitivity sweep for β and α** (e.g., β ∈ {0.01, 0.05, 0.1, 0.5}) in the appendix to confirm the stability–plasticity trade-off is well-behaved.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/sb7qHFYwBc.md` (C-CLIP) | 6.50 | Also VL-CL; less novel methodologically (LoRA+CKC) but cleaner presentation. PI-CCA has a more principled approach but a more significant reporting concern (Figure 3). Comparable overall quality. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/k9NYnsC4Mq.md` (PROOF) | 5.67 | Similar VL-CL domain, rejected. PI-CCA has stronger empirical validation (4 benchmarks vs 9 classification datasets) and more novel method. PI-CCA is clearly stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bqv7M0wc4x.md` (ICL-TSVD) | 5.50 | CL with pre-trained models, accepted. Similar level of presentation issues (some unclear theoretical claims). PI-CCA has more diverse empirical validation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ScI7IlKGdI.md` (Spurious Forgetting) | 6.33 | Conceptual CL paper, accepted. Stronger on conceptual novelty but weaker on empirical breadth. PI-CCA comparable. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/JIlIYIHMuv.md` (LVLM-CL) | 2.50 | Weak VL CL paper, rejected. PI-CCA is far stronger in every dimension. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6Mg7pjG7Sw.md` (CSA) | 6.00 | CCA-based multimodal method, accepted. Similar use of CCA concepts; CSA has cleaner story but less challenging problem setting. Comparable. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/04TRw4pYSV.md` (ModalPrompt) | 3.50 | Multimodal CL, rejected. Weaker method and experiments. PI-CCA is substantially stronger. |

The paper is solid: novel methodology, SOTA results across multiple benchmarks, and clean ablations. The main concern is the unqualified r=1.00 reporting in Figure 3, which needs clarification but is not fatal — the trend is independently corroborated by the ablation study. Relative to the accepted anchors (C-CLIP at 6.50, CSA at 6.00, Spurious Forgetting at 6.33), PI-CCA sits in a similar band: strong contributions with some presentation issues that warrant attention but not rejection.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>