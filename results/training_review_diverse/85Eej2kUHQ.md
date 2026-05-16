Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the consolidated review.

## Summary

This paper proposes **Dynamic Smoothing (DSmooth)**, a certified defense that extends randomized smoothing to anisotropic Gaussian noise, where the covariance matrix Σ is estimated from adversarial perturbation statistics. The goal is to handle complex multi-attacks (e.g., Square+FGSM) that standard isotropic smoothing cannot certify. The paper claims theoretical guarantees in Mahalanobis distance and ℓ₂ norm, and reports large certified accuracy improvements over baselines on CIFAR-10 and ImageNet.

## Strengths

1. **Generalizes randomized smoothing to anisotropic noise via push-forward measure (Theorem 4.3).** The paper proves a general certification guarantee for smoothing distributions that are push-forwards of isotropic Gaussians under deterministic invertible functions. Theorem 4.3 captures Cohen et al. (2019a) as a special case when the push-forward is the identity, and provides a principled template for handling more complex noise distributions. This is a clean theoretical contribution.

2. **First certified defense framework explicitly targeting multi-attacks.** The paper formalizes white-box multi-attacks (Definition 3.1) and constructs a smoothing distribution whose covariance is derived from the statistical structure of adversarial perturbations (Equation 2). This dynamical adaptation is a novel approach for defending against combined attack strategies that prior randomized smoothing methods (ℓ₂, ℓ₁) cannot handle.

3. **Practical scalability via PCA approximation with demonstrated robustness.** The paper addresses the computational infeasibility of a full d×d covariance matrix by proposing a rank-k PCA approximation (Section 4.1). The ablation study (Figure 3) shows that certified accuracy remains nearly identical across k ∈ {10, 100, 1000, 10000}, indicating the method is practical for high-dimensional data like ImageNet.

4. **Consistent large-magnitude improvement across multiple base classifiers and datasets.** The results in Figures 1–2 show DSmooth achieving substantially higher certified accuracy than RandSmooth and LSmooth on both CIFAR-10 and ImageNet across several base classifiers (ResNet, RepVGG, MobileNet, etc.), with baselines hovering near random accuracy while DSmooth reaches 0.4–0.6 on CIFAR-10.

## Weaknesses

### Fatal

None.

### Major

1. **Bound in Lemma 4.5 contains a likely dimensional/notational error.** The bound states:

   `MAHL(̂x|x) ≤ σ/(2·√det(Σ)) · (Φ⁻¹(p_A)−Φ⁻¹(p_B))`

   The denominator contains √det(Σ) (the square root of the determinant). However, tracing the derivation through Theorem 4.4 and the scaled covariance of equation (3), the smoothing distribution has covariance `C = σ²/∛det(Σ)·Σ`. The correct Cholesky-based push-forward gives a bound of the form `σ/(2·(det(Σ))^(1/(2d)))`, i.e., the 2d-th root of the determinant. The paper's expression with the 2nd (square) root is dimensionally inconsistent unless d=1. Since the proof is deferred to the stripped appendix, this cannot be verified from the main text, but the mismatch is a serious concern that could affect the validity of the claimed guarantees. **This requires verification against the full proof; if the bound is wrong, the paper's central theoretical claim is unsupported.**

2. **Experimental comparison is not apples-to-apples.** The paper compares DSmooth's certified accuracy in **Mahalanobis distance** against RandSmooth's **ℓ₂** certification and LSmooth's **ℓ₁** certification on the same multi-attack. These are different metrics, and the radii are not aligned or converted. A Mahalanobis radius R and an ℓ₂ radius R are not comparable quantities. The paper does not attempt to (a) convert Mahalanobis radii to equivalent ℓ₂ radii via the whitening transformation (which Corollary 4.6 provides the tools for), (b) measure robust accuracy directly (fraction of points where the attack does not change the prediction), or (c) report the ℓ₂ norm of the actual attack perturbations to verify whether baselines would be expected to fail. The reported near-random baseline accuracy (0.1 on 10 classes) is consistent with the attack having ℓ₂/ℓ₁ norms that exceed the baselines' certified radii, but this does not demonstrate that DSmooth is better—it demonstrates that DSmooth uses a different metric. A proper comparison requires aligning the evaluation.

3. **Estimation of Σ is underspecified.** The paper states that Σ is the covariance of δ̂ treated as a random variable over natural examples (Equation 2), and that it is approximated by "gathering sample perturbations δ̂ in simulation" and computing the sample covariance, optionally with PCA. Critical details are missing: Is Σ computed once globally from the training set, or per-instance? How many perturbations are collected per image? Are multiple attack restarts used? How is the "distribution over natural examples" defined? The method as described cannot be reproduced, and the theoretical guarantees' applicability to individual test points depends on how Σ is estimated.

4. **The relationship between Theorem 4.4 and Lemma 4.5 is not clearly demonstrated in the main text.** Theorem 4.4 gives p(x) = (1/σ)Lx+μ where L is the Cholesky factor of the *target* covariance. In Lemma 4.5, the target covariance is the scaled version cΣ (c = σ²/∛det(Σ)), not Σ itself. The paper does not explicitly construct p for the scaled covariance or show how the push-forward guarantee translates to the bound on MAHL(̂x|x). The appendix presumably contains the full derivation, but the main text's sketch leaves this connection ambiguous, which undermines trust in the theoretical claims.

### Minor

1. **Definition 3.1 has circular notation.** The perturbation set is written as C(δ), but δ is the variable being optimized over. This should be C (a fixed set). This does not affect the paper's substance but is sloppy.

2. **Numerical stability of the determinant factor is not discussed.** The scaling factor 1/∛det(Σ) in equation (3) involves the d-th root of the determinant of a potentially very large matrix. For ImageNet-scale inputs (d ≈ 150k), det(Σ) could be extremely large or small, leading to numerical overflow/underflow, especially since Σ is only estimated from samples. The PCA approximation mitigates this but the paper provides no analysis.

3. **The ablation study on rank-k does not report variance captured.** Figure 3 shows certified accuracy is insensitive to k, but the paper does not report how much variance is captured by k=1000 relative to the full Σ (or even what the effective rank of Σ is). If Σ is intrinsically low-rank, this insensitivity is expected and not informative about the robustness of the approximation.

### Trivial

None that survive filtering.

## Nice-to-Haves

- Report robust accuracy (not just certified accuracy) for all methods on the same attack budget, to provide a complementary apples-to-apples comparison.
- Convert Mahalanobis certified radii to equivalent ℓ₂ radii using the relationship in equation (4) to enable a common x-axis for comparison figures.
- Provide a concrete algorithm box for computing Σ from sample perturbations (how many, from which distribution, PCA truncation rule).
- Discuss numerical strategies for computing the determinant scaling factor at high dimensions (e.g., using log-determinants or working in PCA space).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Theorem 4.4 covariance calculation error** (Critic: "Cov(p(X)) = Σ/σ², not Σ"): **Removed.** The critic's math is wrong. Cov(p(X)) = (1/σ)L · σ²I · (1/σ)Lᵀ = LLᵀ = Σ. The derivation is correct as written.
- **Theorem 4.3 omits that p must be invertible/deterministic**: **Removed.** The paper states "let p be a deterministic invertible function" (line 95) explicitly.
- **Attack parameters not stated**: **Removed.** The paper states "Square Attack with maximum perturbation 0.5 and 5000 queries. The FGSM attack uses maximum perturbation parameter 0.5" (line 194), along with specifying ℓ∞ and ℓ₂ norms.
- **Corollary 4.6 whitening should use cΣ not Σ**: **Removed.** The critic misunderstands. The Mahalanobis distance in Lemma 4.5 is defined w.r.t. Σ (Definition 4.1), not cΣ. Corollary 4.6 correctly follows from Lemma 4.5 via the relationship MAHL = ||W⁻¹(̂x−x)||₂ where Σ = WWᵀ.
- **Missing appendix tables (Table 3-5 etc.)** : **Removed.** The appendix is stripped by the parsing pipeline; these tables exist in the original submission.
- **Figures lack axis labels/scales**: **Removed.** The figures are embedded images whose labels cannot be verified from the parsed text.
- **NVidia GV102 model name**: **Removed.** Pure formatting/style nitpick irrelevant to scientific content.
- **Missing reference list details**: **Removed.** Parser artifact.
- **Generic/unsupported strengths from Strength Finder** (e.g., "addresses important problem"): **Removed** as generic.

## Novel Insights

The key insight that emerges from the reviews is that the paper's core contribution—extending randomized smoothing to anisotropic noise whose covariance is informed by attack statistics—is interesting and underexplored in the certified robustness literature. However, the main challenge the paper fails to fully address is the **evaluation gap**: comparing certified radii in different norms (Mahalanobis vs ℓ₂ vs ℓ₁) is fundamentally difficult, and the paper's dramatic gains may partly reflect this metric mismatch rather than genuine robustness improvement. A second novel observation is that the push-forward framework (Theorem 4.3) is general enough to be of independent interest but the specialization to anisotropic Gaussians has subtle mathematical pitfalls (the scaling factor and determinant root) that require careful handling.

## Suggestions

1. **Fix the bound in Lemma 4.5.** Verify whether the denominator should be √det(Σ) or (det(Σ))^(1/(2d)) (the 2d-th root). Provide the full derivation in the main text or supplementary material. This is the most critical issue.

2. **Redesign the experiments for fair comparison.** Either: (a) report robust accuracy for all methods on the same fixed attack budget, or (b) convert Mahalanobis radii to equivalent ℓ₂ radii using the whitening transformation (equation 4) so that all methods can be compared on a common x-axis, or (c) at minimum, report the ℓ₂/ℓ₁ norm distributions of the actual attack perturbations to contextualize the baseline results.

3. **Provide a concrete algorithm for estimating Σ.** Specify: number of perturbations per image, whether multiple attack restarts are used, whether Σ is global or per-instance, and how the PCA rank k is chosen in practice.

4. **Clarify the mapping from Theorem 4.4 to Lemma 4.5.** Explicitly construct the push-forward function p for the scaled covariance cΣ = σ²/∛det(Σ)·Σ, and show how the bound on ||p⁻¹(δ)||₂ translates to the Mahalanobis distance bound.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>