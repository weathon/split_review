---

## Summary

ScaPre (Scalable-Precise Concept Unlearning) is a closed-form framework for large-scale machine unlearning in text-to-image diffusion models. It jointly addresses three persistent challenges: conflicting weight updates across many concepts, collateral damage to semantically similar non-target concepts, and the computational burden of auxiliary modules or extra data. Its core contributions are (1) a *Conflict-Aware Stable Design* combining a spectral trace regularizer (built from concept second-order statistics and SVD-gated inter-concept overlap) with Bures-distance geometry alignment, and (2) an *Informax Decoupler* that uses channel-level mutual information to selectively weight parameter updates. Together these yield a training-free, Sylvester-equation-based closed-form update that scales to 50 concepts in 120 seconds and outperforms eight baselines across object, style, and explicit-content unlearning benchmarks.

---

## Strengths

- **Technically principled conflict suppression.** The decomposition of the regularizer into an empirical second-order structure term **S** and an SVD-gated inter-concept overlap term **R** is well-motivated: **S** targets directions that are individually noisy under large-scale aggregation, while **R** separately suppresses directions where concepts highly overlap. The sigmoid gating on singular values is an elegant soft alternative to hard truncation.

- **Replacing ℓ₂ weight-norm with Bures-distance geometry alignment is genuinely novel in this context.** Matching covariance structures **WW**ᵀ and **W₀W₀**ᵀ via the Bures geodesic preserves higher-order feature correlations that element-wise Frobenius penalties miss; this is a stronger structural anchor during large-scale edits.

- **Strong and multi-dimensional empirical results.** ScaPre achieves 0.8% residual accuracy on Imagenette (vs. 4.9% for the best prior closed-form method, RECE) while holding CLIP-COCO at 30.43 (vs. 29.27 for RECE). On the harder 50-concept ImageNet-Diversi50, it reaches 3.9% vs. 19.6% for ESD (the next best method that does not collapse). The visually similar concept benchmark (ImageNet-Confuse5) shows an 84.3% harmonic overall accuracy vs. ≤50.3% for all baselines—a compelling precision result.

- **Efficiency profile is competitive.** 120 seconds / ∼5 GB for 50 concepts matches UCE/RECE resource costs while dramatically outperforming them in unlearning quality; fine-tuning-based methods (FMN, SPM, ESD) require far more compute.

- **New evaluation benchmarks (ImageNet-Diversi50 and ImageNet-Confuse5)** are methodologically well-designed contributions: Diversi50 tests scalability with diverse categories, while Confuse5 tests precision with intentionally confusable near-neighbors.

---

## Weaknesses

### Fatal
None.

### Major

1. **The proposed UQ metric is internally normalized and potentially self-referential.** UQ is computed as a sigmoid-normalized, harmonic-mean combination of unlearning accuracy and CLIP score, where the normalization constants (μ, σ) are computed *over the set of evaluated methods*. Adding or removing a baseline could change every method's UQ score. Since the paper uses UQ as a primary headline result (e.g., Table 1, Table 3, Table 4), and ScaPre is the paper's own method, the metric is structurally designed in a way that benefits whichever method achieves simultaneously strong unlearning and quality—but the sigmoid scaling amplifies differences near the mean, which may inflate separation. The individual constituent metrics (Avg Acc, CLIP) unambiguously favor ScaPre, so this does not undermine the conclusions, but the metric design deserves rigorous justification that is currently absent.

2. **The Bures geometry alignment term is handled via an approximation (post-hoc proximal refinement) rather than optimizing Eq. 8 directly.** The matrix square root in Eq. 5 breaks the quadratic structure, so the paper solves the quadratic part analytically and then applies a separate Procrustes-style refinement. The derivation is deferred to Appendix B.2. While this two-stage approach works empirically, the paper does not bound the approximation error or analyze how much the refinement changes the unlearning direction. The contribution of geometry alignment vs. the other components is therefore harder to isolate.

3. **Scalability to 50 concepts is tested, but the abstract's claim of "×5 more concepts than the best baseline" lacks a crisp definition of "acceptable generative quality."** MACE is described in the related work as scaling to "hundreds of concepts." No experiment tests ScaPre beyond 50 concepts or directly compares against MACE at the hundreds-of-concepts regime. The scalability advantage may be real within the tested range, but the claim of large-scale coverage relative to all prior work is partially unsubstantiated.

### Minor

1. **The Informax Decoupler's MI estimation uses a binary-thresholded activation and an empirical joint distribution over what may be a small sample.** For 50 concepts with d_out ∈ {768, 1024}, the per-channel MI estimates from Eq. 6 are computed from few co-activation pairs per concept. The sensitivity to the adaptive threshold τᵢ and sample count K is not analyzed; noisy MI estimates would propagate directly into the α weights.

2. **The closed-form Sylvester solve (Eq. 10) involves a Kronecker product of size (d_in × d_out)², i.e., roughly 590K × 590K for d=768.** For the numbers claimed (50 concepts, 120 s), this must be handled efficiently (e.g., via vectorized Lyapunov/Sylvester solvers). The paper does not detail which solver is used or its computational complexity, making the efficiency comparison incomplete.

3. **The unlearn accuracy baseline for SD v1.5 on Imagenette (89.9%) is somewhat low for a ResNet-50 classifier on a well-matched class set,** suggesting the classifier or generated-image quality creates a ceiling that partially masks differences between methods (e.g., MACE at 78.5% already underperforms the pretrained model by only ∼11 pp).

### Trivial
None worth listing.

---

## Nice-to-Haves

- An ablation in the main paper (even a compact table) for the three key components (spectral trace regularizer, Bures alignment, Informax Decoupler) would strengthen the methodological claims.
- Evaluation at 100 or 200 concepts would directly address the comparison with MACE's claimed scale.
- The sensitivity of MI estimation to threshold τᵢ and sample count K deserves at least a brief analysis.
- Clarifying exactly which non-target concept embeddings are used in Eq. 2 (since the method claims it needs no additional data) would help practitioners reproduce the work.

---

## Novel Insights

The most genuinely novel insight is the decomposition of the regularization matrix into two distinct second-order terms—**S** capturing intra-concept token-level statistics and **R** capturing inter-concept overlap via SVD with a smooth sigmoid gating—rather than relying on a single isotropic or Frobenius regularizer. This reflects a meaningful conceptual advance: different failure modes of large-scale closed-form editing (directional noise vs. concept aliasing) require structurally different suppression mechanisms. The pairing with Bures-distance geometry alignment (instead of Frobenius weight-space distance) to protect non-target feature covariances during large-scale edits is an orthogonal and complementary insight, drawing from optimal-transport geometry in a setting where it had not previously been applied. The channel-level binary MI decoupler is less surprising in isolation but is well-integrated with the closed-form paradigm.

---

## Suggestions

- Formally define "acceptable generative quality threshold" used to support the "×5 more concepts" claim, or replace it with a concrete curve showing CLIP score vs. number of concepts across methods.
- Provide complexity analysis of the Sylvester solve (Eq. 10) as a function of d_in, d_out, and number of concepts m, and note which solver is used (e.g., scipy.linalg.solve_sylvester).
- Consider a fixed-distribution version of UQ (e.g., normalizing against the pretrained SD baseline and the null model) so that the metric is stable with respect to the evaluation set of methods.
- Add a direct test at 100+ concepts to compare against MACE's claimed scale, even if on a subset of categories.

---

## Score and Decision

ScaPre makes a technically well-grounded contribution to an important and practically relevant problem. The method is novel in its combination of structured spectral regularization, Bures-geodesic alignment, and information-theoretic channel weighting within a closed-form framework. The empirical improvements over strong baselines are large and consistent across multiple benchmarks and dimensions (unlearn accuracy, preservation, efficiency, precision). The weaknesses—primarily around metric justification, the Bures approximation analysis, and the scalability ceiling—are real but do not undermine the core contribution. The paper advances the state of the art meaningfully.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>