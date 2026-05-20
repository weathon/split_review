Now I have a clear picture of the calibration landscape. Let me write the final review.

## Summary

The paper proposes a sparsification loss for hyperspectral band selection that enforces exactly-\(k\) sparse importance weights. The key idea is a combinatorial loss \(L_{sp} = -\log E_{(k,B)}\) derived from summing probabilities over all \(k\)-subsets, computed via dynamic programming, with theoretical guarantees (global optimum only at sparse configurations, no local maxima inside the open interval). The method is evaluated on three standard hyperspectral benchmarks (KSC, HT2013, HT2018) with two downstream classifiers, consistently achieving the highest OA/AA/Kappa among competing methods.

## Strengths

1. **Principled combinatorial sparsification with theoretical guarantees.** Theorems 1 and 2 (Section 3.4) are genuinely useful: they prove that \(E_{(k,B)}\) reaches its maximum iff exactly \(k\) bands have importance 1 and the rest 0, and that inside \((0,1)\) there are no local maxima — only a saddle point at uniform importance. This explains why the optimization reliably converges to a sparse configuration, a property absent from L1/L2 sparsification.

2. **Consistent state-of-the-art classification results.** On KSC with 5 selected bands and SSDGL classifier, Ours(CLS) achieves 96.1% OA vs. 95.3% for the prior best (Yao et al., 2024). On HT2013 (5 bands, SSDGL), 95.6% vs. 95.1%. On HT2018 (5 bands, SSDGL), 98.2% vs. 97.5%. The improvements hold across 3 datasets, 2 classifiers, and both 5- and 10-band settings (Tables 1, 2, 4). The method also works in both supervised (CLS) and unsupervised (REC) variants, demonstrating flexibility.

3. **Clean, efficient dynamic programming solution.** The forward-backward DP (Section 3.5) computes the loss and its gradient in \(O(B \times (2k+1))\) time, which the paper correctly notes is minimal — lower than a \(1\times1\) convolution. This makes the approach practical for deployment.

4. **Sharper sparsity than alternatives.** Figure 2 directly compares the final importance distributions: the proposed loss produces sharp peaks at 1.0 for selected bands and near-0 for the rest, while L1 and L2 yield more distributed values. This is visually compelling evidence that the method achieves its design goal.

## Weaknesses

### Major

1. **Classification results reported without variance or significance testing.** Tables 1, 2, and 4 present single-run numbers. Differences between the proposed method and the best competitor are often small (e.g., 95.6% vs. 95.1% on HT2013 with 5 bands, 0.5 pp; 96.1% vs. 95.3% on KSC, 0.8 pp). Without error bars, confidence intervals, or multi-trial statistics, the reader cannot assess whether these improvements are statistically robust or reflect random variation in training or data splits. This is the single issue that most weakens confidence in the paper's headline claims. *Note: this is a real gap — the paper should report at least mean ± std over multiple random seeds.*

2. **The claim that the method "depicts inter-band relationships" is only validated on synthetic data.** Section 4.6 constructs a random binary weight matrix and tests whether the EM loss recovers high-weight subsets better than alternatives. While the t-test shows statistical significance (Table 6), this only demonstrates that the method can optimize a known linear objective on a toy problem — it does not constitute evidence that the method captures meaningful spectral interactions (e.g., NDVI, NDWI) in real hyperspectral data. The paper's introduction and Section 3.6 emphasize this relationship-modeling advantage as a key contribution, but no real-data validation is provided. This is a significant gap between the claims made and the evidence supplied.

### Minor

3. **The selection rule for converting learned importance weights into a discrete band subset is never specified.** The paper says "selected bands are assigned an importance level of 1, and unselected bands as 0" (Section 3.1), and Table 3 reports discrete band indices. But the explicit rule — threshold at 0.5? take the top-\(k\) weights? — is not stated. While one can infer top-\(k\) from context, this should be unambiguous for reproducibility.

4. **The "EM algorithm" framing is a terminological stretch.** The method computes a marginal probability \(E_{(k,B)}\) (not a posterior over latent variables) and then minimizes \(-\log E_{(k,B)}\) via standard gradient descent (not an M-step that maximizes a Q-function). Calling the forward pass an "E-step" and the gradient update an "M-step" conflates the method with the well-defined EM algorithm. The technical contribution — a combinatorial sparsification loss with exact DP computation — stands on its own and does not need this framing. Dropping or significantly softening the EM claim would strengthen the paper.

5. **Hyperparameter analysis is thin.** The analysis of \(\alpha\) (Section 4.7) uses only the KSC dataset with 5 bands. The finding that \(\alpha<0.03\) fails to produce sparsity is plausible, but it is unclear whether this threshold generalizes to other datasets or selection sizes.

### Trivial

6. **The "sequential sparsification" claim in Section 4.4 is a qualitative observation.** The paper states that "bands selected earlier may influence the selection of subsequent bands" based on Figure 3, but provides no quantitative measure of ordering or causality. This should be acknowledged as a qualitative observation rather than a finding.

## Nice-to-Haves

- Include all-bands accuracy as a reference in Table 5 (sparsity strategies comparison).
- Add a limitations paragraph (e.g., the need to pre-specify \(k\), dependence on classifier architecture).
- Consider using realistic band correlation matrices (derived from real HSI data) rather than random matrices in Section 4.6.
- Report training time / FLOPs for the band selection phase to complement the complexity analysis.

## Removed Points

- *"Missing related works"* — removed; I lack external sources to verify.
- *"Missing appendix proofs" and "hyperparameters not disclosed in main text"* — removed; parser strips appendix, and such details are standard to relegate.
- *"L1/L2 comparison is unfair"* — weakened to a minor point in nice-to-haves; the paper includes Gumbel (the more relevant baseline) and the L1/L2 comparison serves as a useful lower-bound demonstration of the sparsity advantage.
- *"Should include error bars"* — kept as Major weakness; it is verifiable from the paper that no variance is reported. However, it should be noted that none of the baseline methods in the tables report variance either — this is a field-wide issue, but the paper should still lead by example.
- *Strength Finder generic strengths* — removed strengths like "addressed an important problem" or "targeted an interesting question" as they are superficial.
- *"The method is the first to implement sparsity based on EM"* — this specific strength claim is removed because the EM framing is overstated; the technical merit of the loss function is retained as a strength.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a new angle that the paper itself does not already articulate.

## Suggestions

1. **Add multi-run statistics** — Report mean ± std over at least 5-10 random seeds for the main classification tables. This is the single highest-impact improvement.
2. **Validate relationship mining on real data** — Show that conditional probabilities \(P(b_j=1|b_i=1,S)\) from the computation graph align with known band interactions (e.g., NDVI band pairs) on a real dataset. Even a qualitative example would be far more convincing than the synthetic experiment alone.
3. **Specify the selection rule explicitly** — State clearly: "after training, we select the \(k\) bands with the highest \(c_i\) values" (or whatever rule is actually used).
4. **Reframe the EM connection** — Describe the loss as a "combinatorial sparsification loss" rather than an EM algorithm. The contribution is strong enough without the terminological stretch.
5. **Extend hyperparameter analysis** — Show \(\alpha\) sensitivity on at least one additional dataset and one additional \(k\) value.

## Score and Decision

**Bracket (Round 1):** The paper's topic (hyperspectral band selection with sparsity) returned anchors at avg scores 2.2–3.0 (weak band), 4.0–4.75 (middle band), and 7.75–8.5 (strong band). The paper is clearly above the weak band and well below the strong band, placing it in the 4–7 range.

**Narrowing (Round 2):** The most directly comparable anchor — "Supervised Band Selection with a Concrete Layer for Hyperspectral Imagery" (avg 4.0, scores 5,5,3,3) — addresses the same problem with a Gumbel-Softmax approach but lacks theoretical guarantees, has fewer experimental settings (different classifiers/datasets), and received reviews citing limited novelty and excessive hyperparameter tuning. The current paper is stronger on all these dimensions (theoretical backing, cleaner sparsity mechanism, both supervised/unsupervised variants, more datasets), placing it above 4.0. At the same time, evaluation gaps (no variance, synthetic-only relationship validation) prevent it from reaching the level of papers at 6+ with rigorous statistical reporting. Comparing against "Mask in the Mirror: Implicit Sparsification" (avg 5.75, accepted poster) — which had stronger theoretical analysis of implicit regularization dynamics — the current paper's evaluation is less rigorous but its practical contribution (band selection) is more concrete. I place it between these anchors.

**All anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| py3RTHNT6J.md | 2.20 | R1 | Weaker — scaling law study on remote sensing, not band selection |
| lt6xKGGWov.md | 2.33 | R1 | Weaker — feature selection via MI estimation, synthetic-only experiments |
| zgHamUBuuO.md | 3.00 | R1 | Weaker — sparsity for latent representations, different domain |
| XMaPp8CIXq.md | 3.00 | R1 | Weaker — always-sparse training, different domain |
| **PauyrluLud.md** | **4.00** | **R1/R2** | **Weaker — same topic (band selection), fewer guarantees, more tuning issues** |
| Ai4L058yoO.md | 4.50 | R1 | Similar — dynamic feature selection, unclear methodology |
| tGsumqfOUk.md | 4.75 | R1 | Similar — parameter sharing sparsity, limited comparison |
| lnVPfgRnIV.md | 4.75 | R1 | Similar — incremental segmentation, different task |
| saFH7zTtQs.md | 5.17 | R2 | Similar — EM + sparsity for LDS, different domain |
| rYTlmSlxia.md | 4.75 | R3 | Different domain — GPR anomaly detection |
| 7dmsy2Vd5h.md | 4.75 | R3 | Different domain — weather prediction |
| **U47ymTS3ut.md** | **5.75** | **R2** | **Stronger — Mask in the Mirror, implicit sparsification theory** |
| 2ET561DyPe.md | 5.75 | R3 | Stronger — Few-Class Arena, cleaner evaluation |
| 4VgBjsOC8k.md | 6.25 | R3 | Stronger — Conv kernel clustering, thorough analysis |

**Final score: 5.5.** The paper has a genuine technical contribution (combinatorial sparsification loss with theoretical guarantees) and demonstrates consistent SOTA results, but is held back by the absence of variance/statistical significance in its core experimental claims and the gap between claimed relationship-modeling advantages and the synthetic-only validation provided.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>