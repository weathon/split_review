Now I have all the information needed. Let me synthesize the final review.

---

## Summary

This paper tackles test-time adaptation (TTA) for regression, an underexplored problem where existing TTA methods designed for classification (entropy minimization, full-dimensional feature alignment) are ineffective. The authors propose Significant-subspace Alignment (SAL), which detects the low-rank feature subspace of the source regression model via PCA, then aligns only the target features within that subspace using a weighted KL divergence. The method is simple, principled, and demonstrated across four diverse regression tasks (SVHN→MNIST, UTKFace under corruption, Biwi Kinect gender shift, California Housing coastal/non-coastal split) with consistent R² improvements over adapted classification TTA baselines.

---

## Strengths

1. **Well-motivated and principled core idea.** The paper identifies a genuine property of regression features — that they occupy a very small subspace of the feature space (Table 1: e.g., 102 valid dims out of 2048 for ResNet-50 on UTKFace) — and builds a method that directly addresses this. Subspace detection via PCA is a clean solution to the instability caused by aligning degenerated dimensions. The reconstruction error analysis (Figure 3) directly validates the mechanism: SAL preserves the source subspace structure while baselines break it.

2. **Consistent empirical superiority across diverse settings.** SAL outperforms all baselines on four datasets spanning image-to-image domain shift (SVHN→MNIST), image corruption (UTKFace with 13 corruption types), demographic shift (Biwi Kinect by gender), and tabular distribution shift (California Housing). The gains are non-trivial — e.g., on UTKFace with Gaussian noise, SAL achieves 0.717 R² vs. Source 0.589 and best baseline (FR) 0.603. This covers a broader range of regression TTA settings than typical classification TTA papers.

3. **Thorough ablation isolating the contribution of each component.** The ablation (Table 4) clearly separates the effect of subspace detection from dimension weighting. Subspace detection provides the dominant gain (e.g., MNIST: from 0.398 without to 0.754 with subspace detection), while dimension weighting provides a smaller but consistent additional improvement (0.754 → 0.820). The K-ablation (varying subspace dimensions from 10 to 2048) is informative and supports the claim that using the source subspace rank as a guideline for K is reasonable.

4. **Mechanistic evidence beyond performance numbers.** The reconstruction error analysis (Figure 3) and feature distribution visualization (Figure 4) go beyond simple accuracy tables to explain *why* SAL works — it preserves the source subspace and makes projected features more Gaussian, which validates the use of Gaussian KL divergence. This strengthens the paper's internal coherence.

---

## Weaknesses

### Fatal

None.

### Major

1. **Missing variance/reliability estimates for all main results.** The paper reports all R² scores as single point estimates with no standard deviations, confidence intervals, or mention of how many random seeds/runs were used. Many reported improvements are modest (e.g., SAL 0.554 vs. Source 0.506 on California Housing; SAL 0.678 vs. Source 0.651 on Biwi Kinect female→male yaw). Without variance estimates, it is impossible for the reader to judge whether these gains are statistically reliable or could be reversed by a different initialization or data split. This is a significant evidential gap for an empirical paper. **The authors should report means and standard deviations over multiple runs for all main result tables.**

2. **Baseline fairness concerns for RSD and Prototype.** RSD (a regression-specific UDA method) and Prototype are included as baselines, but their failures on certain datasets are reported without adequate context. RSD "did not work on California Housing because of numerical instability of SVD performed on every target feature batch" (line 238) — the batch-wise SVD is an artifact of applying a UDA method in a TTA streaming setting, not a fundamental failure of the method. Similarly, Prototype is reported as "diverging" on Biwi Kinect (line 244). The paper would be stronger if it either (a) adapted these baselines to a setting where they function as designed (e.g., full-dataset rather than batch-wise computation when feasible), or (b) explicitly framed them as *inapplicable* to TTA for regression rather than presenting them as *failed baselines* that inflate SAL's relative performance. The current presentation undersells the difficulty of adapting regression UDA methods to the TTA setting.

### Minor

3. **No limitations or failure-case discussion.** The paper does not discuss when SAL might perform poorly — e.g., severe shifts that change the subspace orientation, settings where the source subspace dimension is very large (making PCA-based detection less useful), or cases where the Gaussian assumption on projected features is violated. Adding a limitations paragraph would improve credibility.

4. **Dimension-weighting form is under-explored.** The weighting function α_d = 1 + |w^⊤ v^s_d| is introduced without justification of the linear form over alternatives (e.g., quadratic, exponential). The ablation already shows that dimension weighting contributes a smaller gain than subspace detection, and the correlation table (mentioned but not visible) shows strong correlation between λ^s_d and α_d, suggesting partial redundancy. The paper would benefit from explicitly noting that the linear form is a simple default and that the main contribution (subspace detection) is robust to the exact weighting choice.

5. **Gaussian-convergence argument (Eq. 5 / line 344–350) is heuristic.** The CLT-based argument that projected features become Gaussian assumes independence across feature dimensions, which is not justified (the terms a_{i,d} share the same input x_i and are functions of the network's weights). The paper implicitly presents this as intuition, which is fine, but should state more clearly that this is a heuristic rather than a formal justification.

6. **Missing reference R² on clean data.** For UTKFace (which uses severity-5 corruption), the paper does not report the Source model's R² on clean UTKFace images. This makes it difficult to assess how severe the corruption shift is relative to the model's base capability.

### Trivial

7. Minor notational inconsistency: The paper uses both tilde notation (σ̃_d^t²) and λ^s_d to describe variances in the projected space and eigenvalues, respectively, without always clarifying that they represent the same quantity (variance along a principal direction). This is clear on re-reading but could be streamlined.

---

## Nice-to-Haves

- An additional error metric (e.g., MAE for UTKFace age prediction) would help verify that R² improvements translate to practically meaningful reductions in absolute error.
- A simple practical guideline stating explicitly that K should be set to the rank of the source covariance matrix would be helpful (this is already done implicitly).
- A comment on which specific normalization layers' parameters are adapted in each architecture (ResNet-26, ResNet-50, MLP) would aid reproducibility, though the paper's reference to Tent makes this largely inferable.

---

## Removed Points

*"Missing related works"* — removed per instructions (cannot verify existence of missing citations).
*"No code or reproducibility statement"* — removed per instructions (criticism about artifacts not standard/accommodatable in reviews).
*"Section 3 notations cleaner" / "Section 1 could add forward reference"* — removed as pure presentation/polish nitpicks that are not substantive weaknesses.
*"Strengthening the Paper on Its Own Terms" suggestions* — some of these are merged into weaknesses above; the rest are moved to Nice-to-Haves since they are constructive suggestions, not weaknesses.
*Several generic Strength Finder entries* (e.g., "the paper addresses an important problem") — removed as generic/superficial. Only specific, evidence-grounded strengths are retained.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation that the paper itself does not already articulate, though they collectively identify that the dimension-weighting component is considerably weaker than subspace detection (a point the paper partially acknowledges but could emphasize more).

---

## Suggestions

1. **Add variance estimates:** Run each experiment with at least 3–5 random seeds/initializations and report mean ± std for all main tables (SVHN, California Housing, UTKFace, Biwi Kinect).
2. **Address baseline fairness:** Either fix RSD to use full-dataset SVD (non-streaming setting) and report those results, or explicitly remove it from the main comparison with a clear statement that RSD is a UDA method, not a TTA method, and is included only for reference.
3. **Add a limitations paragraph** discussing plausible failure modes (e.g., extreme shifts that reorient the subspace, datasets where the source subspace dimension is large relative to the full feature dimension).
4. **Report Source R² on clean UTKFace** as a reference point for the corruption severity.

---

## Score and Decision

The paper addresses a genuinely underexplored problem with a principled, simple method, supported by consistent empirical evidence across diverse regression tasks and informative mechanistic analysis. The main evidential gap is the absence of variance estimates, which is addressable, and the baseline fairness concern is real but does not invalidate the core contribution. The method's strengths (subspace detection, reconstruction validation, consistent gains) clearly outweigh the weaknesses.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>