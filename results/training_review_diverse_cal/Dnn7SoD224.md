Now I have a thorough understanding of the paper. Let me produce the consolidated review.

---

## Summary

This paper reformulates continuous disparity prediction in stereo matching as risk minimization. It shows that the widely-used expectation (soft-argmin) corresponds to L2 risk minimization, then replaces it with L1 risk minimization whose optimal solution (a median-like estimate under the interpolated density) is more robust to multi-modal disparity distributions. The key technical contribution is making this differentiable via the implicit function theorem, enabling end-to-end training through the binary-search-based L1 solver. Strong cross-domain generalization results on ETH3D, Middlebury, and KITTI provide the most compelling evidence for the method's robustness.

## Strengths

- **End-to-end differentiable L1 risk minimization via implicit differentiation**: The use of the implicit function theorem (Eq. 6–7) to backpropagate through a non-differentiable binary-search optimization loop is a technically non-trivial contribution. It enables gradient flow from the final disparity prediction back to the discrete distribution, which is what allows the network to learn distributions tailored to the L1 decoder.

- **Consistent and large-margin cross-domain generalization**: Without any fine-tuning on target domains, the method achieves the lowest error rates on multiple real-world benchmarks. On ETH3D (Table 5), the >1px error drops from 4.05 (next best) to 2.71; on Middlebury (Table 4), from 13.76 to 12.63. These margins are well beyond what could be noise.

- **Plug-and-play improvement across architectures**: Simply replacing the expectation layer with the L1 risk module *at test time only* improves accuracy for ACVNet and PCWNet across all metrics (Table 8), without retraining. This cleanly separates the benefit of the L1 decoder from the specific network architecture.

- **In-domain SOTA on SceneFlow and KITTI 2012**: The method achieves the best published results on SceneFlow (e.g., >1px error 4.22 vs. 5.00 for the next best) and ranks first in non-occluded regions on KITTI 2012, with competitive inference time and fewer parameters than several compared models.

- **Theoretical grounding**: The paper proves convexity of the L1 risk function and monotonicity of its derivative (Section 3.2), guaranteeing global optimality of the binary search solution and providing the foundation for the implicit differentiation.

## Weaknesses

### Major

None. The core claims are supported by the experiments, and no methodological error invalidates the results.

### Minor

1. **Missing sensitivity analysis for the kernel bandwidth and no justification for the Laplacian kernel**: The entire continuous density interpolation relies on the Laplacian kernel with σ=1.1, yet the paper provides no ablation over σ (e.g., 0.5, 1.0, 1.5, 2.0) and no comparison with a Gaussian kernel. Since σ controls the smoothness of the density — too large blurs the distribution and shifts the L1 minimizer, too small collapses gradient signals — the claimed robustness is partially contingent on an unexamined hyperparameter choice. An ablation on the cross-domain evaluations (where the strongest gains appear) is the natural fix.

2. **Gradient clipping in Eq. (7) is used without analysis**: The denominator in the implicit gradient is clipped to ≥0.1 to prevent large gradients, introducing a bias whose impact is never characterized. How often does this clipping activate during training? Under what configurations of the discrete distribution? If it fires frequently near the optimum, the training signal is distorted, potentially harming convergence. The paper does not report clipping rates or validate that the clipped gradient remains a descent direction.

3. **No discussion of limitations or failure cases**: The paper does not address when the L1 approach might not help (e.g., symmetric unimodal distributions where L1 and L2 coincide, or when the interpolated density is flat near the minimizer and the gradient denominator becomes small). A frank limitations paragraph would strengthen the paper.

4. **Ablation finding left unexplained**: Table 8 shows that switching from expectation to L1 *at test time only* (with expectation-based training) still improves accuracy. This is interesting and somewhat surprising — it suggests the network trained with expectation loss produces distributions where the L1 decoder happens to recover a better point estimate. The paper reports this but does not analyze *why*, which would deepen the contribution.

5. **Overclaimed framing**: The introduction presents this as "a radically different perspective" (line 19) when the core statistical idea — that the median (L1 minimizer) is more robust than the mean (L2 minimizer) for multi-modal distributions — is a standard result in estimation theory. The paper's genuine novelty lies in the differentiable implementation and its application to stereo matching. The framing should be adjusted to match the actual scope of the contribution.

### Trivial

- τ=0.1 is given as the binary search convergence threshold, but its role is never explicitly stated (it appears only in "we set the σ and τ as 1.1 and 0.1 respectively").

## Nice-to-Haves

- **Comparison with a differentiable Huber risk minimizer**: Since the paper frames the choice as L1 vs. L2, a natural middle ground is Huber risk. Comparing against it using the same implicit differentiation approach would clarify whether L1's specific robustness properties matter or whether any robust loss would do.
- **Runtime breakdown**: The paper says the module "slightly increased" running time (Table 8 caption) but does not give absolute numbers for the binary search + gradient computation vs. the rest of the network. Given the per-pixel O(log N) operations, this would be useful for practitioners.
- **Analysis of the test-time-only L1 improvement**: Investigating *why* the expectation-trained network's distributions favor L1 decoding could yield insights beyond the paper's current scope.

## Removed Points

- **Criticism that "Alg. 1 is not shown" / "binary search algorithm is referenced but never shown"**: The algorithm was in the appendix, which the PDF parser strips from all submissions. The main text already describes the binary search procedure (convexity → zero-derivative condition → binary search with O(log N) complexity), and τ=0.1 is given as the convergence threshold.
- **Criticism about architectural borrowing**: The paper transparently acknowledges its architectural debts ("our network structure is inspired by CasMVSNet," line 39). The paper's contribution is the risk minimization module, not the full pipeline architecture, and this is clear.
- **Criticism that "in-domain gains are small"**: This is an observation, not a weakness. Gains on saturated benchmarks are inherently incremental, and the paper's strongest evidence is cross-domain anyway. The in-domain results are consistently positive.
- **Criticism about missing comparison with other failures of L1**: Already captured in the limitations point above (weakness #3), which I kept.

## Novel Insights

The most striking finding across the reviews is the test-time-only L1 improvement (Table 8): a network trained with expectation loss produces distributions that are better decoded by the L1 minimizer. This suggests that the training loss (smooth L1 on the final disparity) implicitly biases the learned distribution in a way that makes the L1 decoder outperform the expectation decoder even though the latter was used during training. This decoupling of training objective from inference decoder is interesting and worth deeper investigation — it may imply that smooth L1 training encourages distributions whose expectation is off-center but whose median remains accurate.

## Suggestions

1. Add an ablation over σ values (0.5, 1.0, 1.5, 2.0) on one cross-domain benchmark (e.g., ETH3D or Middlebury) and compare Laplacian vs. Gaussian kernels.
2. Report the fraction of pixels where the gradient denominator falls below 0.1 during training, and show that removing the clipping (or using a softer regularization like adding a small ε) does not degrade results.
3. Add a limitations paragraph acknowledging when the L1 approach may not help.
4. Tone down the "radically different perspective" framing and more accurately describe the contribution as a differentiable L1 risk minimizer for stereo matching.
5. Analyze why test-time-only L1 switching works, even briefly.

## Score and Decision

**Originality**: 6/10 — The core statistical idea is well-known, but the differentiable implementation in the context of stereo matching is novel and non-trivial.

**Importance**: 7/10 — Improving cross-domain generalization in stereo matching is practically important, and the method is simple enough to be adopted by other architectures.

**Claims supported**: 7/10 — The cross-domain results convincingly support the main claim. The missing σ sensitivity analysis partially weakens the robustness claim.

**Soundness**: 7/10 — The math is correct and the experiments are comprehensive. The unanalyzed gradient clipping and missing σ ablation are the main gaps.

**Clarity**: 6/10 — The paper is generally well-structured but the overclaimed framing and missing limitations section detract.

**Value to community**: 7/10 — The plug-and-play nature means it can be dropped into existing stereo networks. The implicit differentiation trick may also be useful outside stereo matching.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>