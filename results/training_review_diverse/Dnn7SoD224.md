Now I have all the information needed. Let me cross-reference the claims against the paper and write the final review.

---

## Summary

This paper introduces a novel formulation for continuous disparity prediction in stereo matching by replacing the standard expectation over a discrete probability distribution with L1 risk minimization. The authors show that expectation is a special case of L2 risk in their framework, interpolate the discrete distribution using a Laplacian kernel to obtain a continuous density, find the L1 risk minimizer via binary search during forward inference, and compute gradients through this non-differentiable operation using the implicit function theorem for end-to-end training. Experiments across SceneFlow, KITTI 2012/2015, Middlebury, and ETH3D show strong in-domain performance and particularly notable cross-domain generalization improvements.

## Strengths

- **Novel and theoretically grounded formulation**: The paper reframes disparity prediction as risk minimization over an interpolated continuous density, formally showing that the standard expectation is an L2 special case. Switching to L1 risk is motivated by well-known robustness properties against multi-modal distributions (Section 3.2, Figure 2). This is a clean, principled departure from existing practice.

- **Strong empirical results, especially in cross-domain generalization**: When trained only on SceneFlow and tested on unseen real datasets, the method achieves best or near-best error rates across all four benchmarks (Tables 4–7). On ETH3D the >1px error drops substantially (from 4.05 to 2.71) and on Middlebury the >1px error drops from 13.76 to 12.63. These are large relative improvements that indicate genuinely better robustness.

- **Ablation cleanly isolates the contribution**: Table 8 compares three conditions within the same network — expectation (train+test), L1 risk at test only, and L1 risk at train+test — showing that the full gain requires end-to-end training (EPE 2.03 → 1.88 → 1.73). This provides clear evidence that the proposed training scheme, not just the post-hoc change, is responsible for the improvement.

- **Practical plug-and-play utility**: L1 risk minimization applied at test time to existing networks (ACVNet, PCWNet) improves accuracy without retraining (Table 8), demonstrating that the benefit is not architecture-specific and can be adopted incrementally.

- **Efficient with no extra parameters**: The binary search forward pass has O(log N) complexity, the backward gradient (Eq. 7) avoids unrolling iterative loops, and the module introduces only marginal runtime overhead with zero additional learnable parameters (Table 8, Section 4.4).

## Weaknesses

### Fatal
None.

### Major

- **Backward gradient implementation is not validated, weakening the causal claim about training.** The paper derives the backward gradient via the implicit function theorem (Eq. 7), but there is no empirical validation that this gradient correctly minimizes L1 risk during training rather than acting as an approximate or regularizing signal. Three specific concerns are unaddressed: (1) the forward pass uses binary search with tolerance τ=0.1, but there is no analysis of gradient error introduced by this approximate solution; (2) the denominator clipping (≥0.1) is a heuristic to avoid large gradients but could introduce bias, and its impact on training is not analyzed; (3) the sign function in Eq. 5 is non-differentiable at y=d_i, and the implicit function theorem requires a continuously differentiable optimality condition — the paper glosses over this. Because the loss function (Eq. 8, smooth L1) is identical for both expectation and L1 risk training, the backward gradient through the risk module is the *only* difference during training. Without validation that this gradient faithfully implements L1 risk minimization, the observed improvement from end-to-end training (Table 8) could stem from the gradient approximation acting as a useful auxiliary signal rather than from the theoretically argued robustness of the L1 median. **This is the paper's most significant evidential gap.**

### Minor

- **No discussion of limitations or failure cases.** The paper does not discuss when the method might underperform — e.g., when the discrete distribution is near-uniform (making the interpolated density flat and L1 risk similar to expectation), or when the Laplacian bandwidth σ is poorly calibrated for the disparity range. A brief limitations paragraph would improve credibility and guide future work.

### Trivial

- The second-order derivative condition ∂²F/∂²y ≥ 0 is stated but strict positivity (required for the implicit function theorem to apply) is not guaranteed; for regions where the density is constant, ∂²F/∂²y = 0 and the binary search may find a valid point but backward propagation would be ill-defined. In practice this is unlikely to occur, but noting it would be precise.
- The hyperparameter σ=1.1 appears without justification or sensitivity analysis.

## Nice-to-Haves

- **Validate the backward gradient on a small synthetic example** where the true gradient can be computed via finite differences or enumeration on a fine grid. This would directly address the core training concern.
- **Report whether the test-time L1 risk swap benefits ACVNet/PCWNet on other cross-domain datasets** (ETH3D, KITTI) beyond Middlebury, to strengthen the generality claim.
- **Analyze sensitivity to σ and the clipping threshold** over a reasonable range.

## Removed Points

These points are flagged for removal from the main evaluation; treat with caution.

- **"The binary search algorithm (Alg. 1) is not provided in the main text"** — Algorithm pseudocode was in the appendix, which is a standard place for it; the parser strips appendix content. Not an author error.
- **"The paper does not compare to offset-based regression methods like Garg et al. or SMD-Net"** — The paper compares to IGEV and DLNR, which are among the most relevant and recent SOTA methods in this space. SMD-Net (2021) and Garg et al. are discussed in Related Work. Demanding every possible baseline is scope creep.
- **"The relationship to the implicit function theorem is under-explained"** — The derivation from dG=0 to Eq. 7 is standard and sufficiently clear for the target audience.
- **"No confidence intervals / significance tests"** — Single-run evaluation without CI is standard practice on stereo matching leaderboards; this is not a weakness unique to this paper.
- **"The paper should report whether improvements hold on other cross-domain datasets for ACVNet/PCWNet"** — This is moved to Nice-to-Haves as a suggestion, not a flaw.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a useful observation: the framing of disparity prediction as risk minimization creates a unified view in which expectation (L2) and median (L1) are two points on a continuum defined by the choice of error function. The practical gap identified — that the backward gradient may only approximately implement L1 minimization — suggests a broader methodological point: many end-to-end learning pipelines that differentiate through optimization procedures (e.g., implicit differentiation, unrolled optimization) would benefit from explicit validation of the backward pass against ground-truth gradients, especially when the forward pass involves non-differentiable operations or approximation tolerances.

## Suggestions

- Add an experiment comparing the implicit-differentiation gradient to a finite-difference approximation on a small synthetic distribution (e.g., a two-spike mixture) to validate that the backward pass correctly minimizes L1 risk during training.
- Include a brief limitations paragraph discussing when the L1 risk minimizer may behave similarly to expectation (e.g., near-uniform distributions) and the role of the Laplacian bandwidth σ.
- Report the sensitivity of results to the binary search tolerance τ and the denominator clipping threshold.

## Score and Decision

This paper presents a novel, well-motivated formulation for continuous disparity prediction. The core idea — replacing expectation with L1 risk minimization — is clean and principled, and the empirical results (especially in cross-domain generalization) are strong and consistently positive across multiple benchmarks. The ablation study cleanly isolates the contribution of end-to-end L1 training.

The paper's main weakness is the lack of validation for the backward gradient. This is a genuine evidential gap: because the training loss is identical for both L1 and expectation training, the gradient through the risk module is the sole differentiating factor during training, and its correctness is not verified. However, this is a fixable issue — the paper's contribution does not depend on a perfect gradient, only on a demonstrably correct one — and the test-time-only improvements already demonstrate practical value independent of the gradient question.

The paper offers real novelty (the risk minimization framing is new to stereo matching), strong experimental support for its claims, and practical utility (test-time plug-and-play). The weaknesses are significant but addressable and do not invalidate the core contribution.

**Score**: 7.0

**Decision**: Accept

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>