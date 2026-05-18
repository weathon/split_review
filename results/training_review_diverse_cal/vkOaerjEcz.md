Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper proposes MTMC (Maximum Token Manifold Capacity), a simple regularizer for Generalized Category Discovery (GCD) that maximizes the nuclear norm of class tokens from unlabeled samples. The core idea is that existing GCD losses overly compress intra-class representations, causing dimensional collapse, and that maximizing the nuclear norm — interpreted as manifold capacity — preserves representation richness and improves clustering. MTMC adds ~3 lines of code to any GCD pipeline and yields consistent accuracy improvements across six benchmarks (CIFAR100, ImageNet100, CUB, Stanford Cars, FGVC Aircraft, Herbarium19), with notable gains on ImageNet100 (+4.7%).

## Strengths

- **Simple, practical, and widely applicable.** MTMC is a three-line addition to any GCD loss (SimGCD or CMS), with a single hyperparameter λ. The code snippet and loss definition make the implementation straightforward. This is a genuine practical contribution — the method could be adopted easily by practitioners.

- **Consistent empirical gains across all six benchmarks.** Table 1 shows that MTMC improves clustering accuracy on every dataset for both SimGCD and CMS backbones, under both the ground-truth K and estimated-K settings. The gain on ImageNet100 (+4.7% all categories, +4.7% novel categories under SimGCD) is particularly compelling.

- **Robust hyperparameter sensitivity.** Figure 3 demonstrates that MTMC improves accuracy across a range of λ values (0.01–1.0) and feature dimensions D, indicating the method does not require careful tuning and is stable across different configurations.

- **Effective mitigation of dimensional collapse.** Figure 5 and the analysis in Section 4.3 show that MTMC produces a flatter singular value distribution and higher von Neumann entropy compared to baselines. This directly supports the claim that the method prevents collapse into a low-dimensional subspace, which is a measurable and desirable property.

- **Improved estimation of the number of categories.** Table 2 shows CMS+MTMC achieves near-perfect or perfect K estimation on several datasets (100% on ImageNet100), reinforcing that richer representations lead to better inter-class separation and more accurate cluster count prediction.

## Weaknesses

### Fatal
None. The core empirical claim — that adding MTMC improves GCD — is supported by consistent results. No weakness invalidates this.

### Major

1. **Notational ambiguity about the loss definition.** The paper writes `L_MTMC = -||[cls]^u||_*` where `[cls]^u` notationally appears to be a single class token vector. For a single L2-normalized vector, the nuclear norm equals its L2 norm (i.e., 1), which is constant and useless as an optimization target. The loss only makes sense if `[cls]^u` is a matrix stacking class tokens across the batch. The paper never explicitly states this matrix construction or its dimensions. An experienced reader can infer the batch-level interpretation from context ("centroid matrix" on line 101, SVD computation, rank summation), but the ambiguity will confuse many readers and impedes reproducibility. The paper must state explicitly: "Stack the N unlabeled class tokens into a D×N matrix and maximize its nuclear norm."

2. **Disconnect between the claimed mechanism (intra-class completeness) and the actual objective (mixed-batch nuclear norm).** The paper motivates MTMC by arguing that existing GCD methods produce overly compact intra-class representations, and that MTMC enriches *within-class* representation. However, the MTMC loss operates on the full unlabeled batch, which contains a mixture of known and novel classes from different categories. Maximizing the nuclear norm of this mixed-class matrix will spread out *all* class tokens regardless of class membership. The paper does not establish why this batch-level objective should specifically improve intra-class completeness rather than simply increasing the overall feature dispersion. The claimed geometric intuition about "[cls] minimizing each [vis] manifold" is about patches within a single sample, not about samples within a class — there is a level mismatch between the per-sample patch argument and the across-sample intra-class claim. This gap between the stated motivation and the actual mechanism undermines the theoretical framing.

3. **Unsubstantiated theoretical connection to intra-class representation.** Section 3.3 shows that MTMC increases von Neumann entropy and effective rank of the feature autocorrelation matrix. These are global properties of the entire feature space. The paper asserts (without derivation) that this specifically corresponds to richer *intra-class* representation. Nothing in the analysis conditions on class membership — the entropy and rank are computed over the entire test set. The argument is correlational: MTMC increases rank/entropy and also improves accuracy, but the causal link to intra-class completeness specifically (as distinct from better global feature dispersion) is not demonstrated.

### Minor

4. **No error bars or multi-run statistics.** All results in Table 1 are reported as single numbers without standard deviations or confidence intervals. The gains on most datasets are 1–2 percentage points (CIFAR100: +0.7, CUB: +2.3, Stanford Cars: +1.7, FGVC Aircraft: +2.1). Without multiple seeds, it is impossible to assess whether these small differences are statistically significant or reflect random variation. Given the simplicity of the regularizer, this is a meaningful gap.

5. **No ablation comparing against other anti-collapse regularizers.** The paper shows that MTMC prevents dimensional collapse, but does not compare against alternative collapse-prevention techniques (e.g., a Barlow Twins-style decorrelation loss on class tokens, a spectral regularization term, or a direct rank penalty). Without such baselines, it is unclear whether the nuclear norm objective is specifically beneficial or whether any mechanism that increases feature rank would produce similar gains.

6. **Modest gains on CIFAR100 and Herbarium19 are attributed to "low embedding quality" without quantitative support.** The paper provides a qualitative explanation (small image size for CIFAR100, out-of-distribution for Herbarium19) but does not present feature-space overlap metrics, embedding quality scores, or any quantitative evidence to support this post-hoc explanation.

### Trivial
None beyond what can be attributed to parser artifacts.

## Nice-to-Haves

- A clear pseudocode block with explicit matrix dimensions (batch_size × feature_dim) for the MTMC loss computation.
- Class-conditioned analysis: compute the effective rank or nuclear norm separately on per-class subsets to directly demonstrate that MTMC enriches intra-class representation, not just global feature dispersion.
- Comparison against at least one alternative collapse-prevention regularizer (e.g., feature decorrelation, Frobenius norm penalty on the covariance matrix) to isolate the effect of the nuclear norm.
- Multiple random seed experiments with standard deviations, particularly for the small-gain datasets.

## Removed Points

- **Harsh Critic's claim that the loss definition "undermines the paper's core claim" as fatal.** The paper's text at line 101 explicitly refers to the "centroid matrix," and the loss involves SVD and rank summation — together these make clear that a batch-level matrix is intended. The notation is sloppy but not fatally ambiguous. The point is kept as Major (not Fatal) above.
- **Criticism about only applying MTMC to unlabeled samples being "unexplained."** The paper does explain this choice (Section 3.2: labeled samples are "sufficiently accurate and unbiased"). An argument can be made against this choice, but the rationale is stated. The related concern about mixed-class batches (which is valid) is folded into Major weakness #2.
- **Strength Finder's strength 4 about "novel focus on intra-class completeness."** This conflicts with Major weakness #2/3 showing the mechanism is not well-supported. The paper's *claim* of novelty is noted, but the strength is removed because it is contradicted by verified weaknesses about the mechanism not being demonstrated.
- **Strength Finder's strength about "theoretical connection to manifold capacity and von Neumann entropy."** This strength overstates the theoretical grounding — Section 3.3 shows correlation, not causation, and does not specifically connect to *intra-class* completeness. The entropy analysis is interesting but not a "strength" in supporting the core claim as argued. The empirical evidence (Figure 2) is valid but the theoretical weight the Finder assigns to it is disproportionate.

## Novel Insights

None beyond the paper's own contributions. The reviewers identify a genuine disconnect between the paper's intra-class motivation and its mixed-batch mechanism, but this is a critique of the paper's framing, not a novel synthesis.

## Suggestions

1. **Explicitly define the loss matrix.** Replace the ambiguous notation `[cls]^u` with an explicit matrix: let `C ∈ ℝ^{D×N}` be the matrix of class token embeddings from N unlabeled samples, and define `L_MTMC = -‖C‖_*`. Provide a pseudocode block with explicit dimensions.

2. **Add intra-class analysis.** Compute the effective rank or average singular values on class-conditioned subsets of the test features to show that MTMC specifically enriches within-class representation, not just global feature dispersion.

3. **Run at least 3 seeds and report standard deviations.** This is especially important for datasets where gains are <2%, to demonstrate the improvement is stable.

4. **Add an anti-collapse baseline.** Compare against a simple feature decorrelation or covariance regularization term (e.g., a penalty on off-diagonal elements of the feature covariance matrix) to show the nuclear norm is specifically beneficial.

5. **Clarify the theoretical story.** Acknowledge the gap between the per-sample patch-level geometry argument and the across-sample class-level claim. Either reframe the contribution as "preventing dimensional collapse" (which is well-supported) rather than "improving intra-class completeness" (which is not directly demonstrated), or provide explicit class-conditioned evidence for the latter.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>