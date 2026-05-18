Now I have all the information needed. Let me compile the final review.

---

## Summary

This paper proposes reformulating disparity prediction in stereo matching as risk minimization under an L1 loss, rather than the standard expectation (L2) over a discretized distribution. The authors interpolate the discrete categorical distribution using a Laplacian kernel to obtain a continuous density, solve the L1 minimization via binary search on the forward pass, and derive gradients through the implicit function theorem for end-to-end training. Extensive experiments on SceneFlow, KITTI, Middlebury, and ETH3D show consistent in-domain improvements and substantially stronger cross-domain generalization compared to prior state-of-the-art methods, while requiring no additional learnable parameters.

## Strengths

1. **Novel risk-minimization formulation that generalizes expectation-based disparity**: The paper reframes the standard weighted-average (expectation) prediction as a special case of L2 risk minimization, and introduces L1 risk minimization which demonstrably handles multi-modal distributions more robustly (Section 3.2, Fig. 2). This is a conceptually clean shift that directly addresses a known weakness of classification-based stereo matching.

2. **Differentiable L1 risk optimization via the implicit function theorem**: Because the L1 risk has no closed-form solution, the paper derives a closed-form gradient dy/dp^m (Eq. 7) using the implicit function theorem, enabling end-to-end training despite the non-differentiable forward binary search. This theoretical contribution makes the practical deployment of L1 formulation feasible.

3. **State-of-the-art cross-domain generalization**: The method demonstrates clear and substantial improvements in generalization from synthetic (SceneFlow) to real-world datasets without fine-tuning. For example, on ETH3D the >1px error drops from 4.05 to 2.71 (Table 5), and on Middlebury from 13.76 to 12.63 (Table 4). This is a critical practical strength, as cross-domain robustness is a known bottleneck for stereo matching.

4. **Competitive or best in-domain results**: On SceneFlow the method achieves the lowest EPE, >1px error, and >0.5px error among all published methods (Table 1). On KITTI 2012 and 2015 it ranks first in non-occluded regions for >2px error (Tables 2–3), confirming that L1 risk does not sacrifice accuracy on in-domain benchmarks.

5. **Ablations verify the core mechanism and transferability**: Table 8 shows that switching from expectation to L1 risk at test time (without retraining) already improves accuracy, and training with L1 risk yields further gains. Plugging L1 risk into existing networks (ACVNet, PCWNet) also improves their cross-domain accuracy, demonstrating generality independent of the backbone.

6. **Efficient inference with negligible parameter overhead**: The risk-minimization module adds no learnable parameters and only slightly increases running time (Table 8). The overall network has fewer parameters than competing methods like IGEV and DLNR (Section 4.4).

## Weaknesses

### Fatal
None.

### Major
None. The core claims are well-supported by the experimental results, and no identified issue invalidates the central contribution.

### Minor

1. **Imprecise time complexity claim (Section 3.2)**: The paper states "the binary search algorithm can find the optimal solution with time complexity of O(log N)" (line 115). This is incorrect. Each binary search iteration evaluates G(y, p^m) which sums over all N disparity hypotheses, costing O(N). The number of iterations depends on the tolerance τ (set to 0.1), not N. The correct complexity is O(N log(1/τ)). For N=192 and τ=0.1 this is O(192 × ~3.3) ≈ 634 operations, which is negligible in practice, but the claim as stated is technically wrong and should be corrected.

2. **Missing baseline: discrete L1 minimizer (median) without interpolation**: The paper argues that L1 risk minimization is more robust than L2 expectation, but the ablation study (Table 8) compares only interpolated L1 vs expectation. It does not compare against the discrete L1 minimizer — i.e., the median of the discrete PMF, computed as argmin_y Σ |y-d_i| p_i without interpolation. Such a comparison would disentangle how much of the gain comes from the switch from L2 to L1 versus from the continuous interpolation itself. Without it, the attribution of the improvement is partially confounded.

3. **Laplacian kernel choice not justified or ablated**: The paper uses a Laplacian kernel for interpolation (Eq. 1) without discussing why this choice was made over alternatives (e.g., Gaussian). The kernel choice affects both the shape of the interpolated density and the analytic form of G(y, p^m). An ablation comparing Laplacian vs. Gaussian (or other kernels) on the downstream disparity accuracy would strengthen the paper.

4. **Gradient clipping threshold not analyzed**: The denominator in Eq. (7) is clipped to be no less than 0.1 (line 129) to avoid large gradients. Since this denominator equals ∂G/∂y, clipping introduces a biased gradient. The paper does not discuss the sensitivity of results to this threshold, alternatives (e.g., adding a small epsilon), or the impact on training stability. While common practice, this omission is worth noting.

5. **Overstated theoretical framing**: The paper invokes Vapnik's principle of risk minimization (lines 19, 256), but the risk is defined over the network's estimated posterior p(x; p^m), not the true data-generating distribution. This is a standard minimum-Bayes-risk / plugin decision rule (Berger, 1983; Lehmann & Casella, 1998). The framing is somewhat misleading; the paper would benefit from acknowledging this explicitly to avoid overclaiming the theoretical connection to statistical learning theory.

### Trivial
- The paper does not explicitly state the convergence guarantee of binary search (G is monotonic because ∂²F/∂²y ≥ 0, so a unique root exists and binary search is guaranteed to find it). Including this would improve clarity.
- The derivation from Eq. (4) to Eq. (5) could include an intermediate step showing the Leibniz rule application under the Laplacian kernel; the final result is correct but the reader must infer the intermediate calculus.

## Nice-to-Haves
- **Code release**: The gradient computation via implicit differentiation is non-trivial; releasing code would aid reproducibility and adoption.
- **Discrete median baseline** (elaborated above as a minor weakness; even a quick experiment would strengthen the ablation).
- **Multi-modal distribution analysis**: Quantify how often multi-modal distributions occur and how much L1 risk improves on such pixels, beyond the single qualitative example in Fig. 2.
- **Visualization of the derivative-based gradient** (∂y/∂p^m) compared to the trivial gradient of expectation (dy/dp_i = d_i), to illustrate why implicit differentiation matters during training.
- **Kernel ablation**: Compare Laplacian vs. Gaussian interpolation to assess sensitivity to this choice.
- **Gradient clipping sensitivity**: Ablate the 0.1 threshold to validate the choice.

## Removed Points
These points were flagged by reviewers or the strength finder but are removed or downgraded for the reasons given:
- **"Network architecture heavily borrowed from CasMVSNet/PSMNet"** → The paper explicitly states its architecture is "inspired by CasMVSNet" (Section 2.1) and describes all components transparently. The novelty is correctly identified as the risk-minimization head. This is a neutral observation, not a weakness.
- **"No code release mentioned"** → This is a practical suggestion, not a weakness of the submission. Moved to Nice-to-Haves.
- **Strengths about addressing an important problem / targeted an interesting question** → These generic phrasings from the strength finder are not included; only specific, citation-backed strengths are retained.

## Novel Insights
None beyond the paper's own contributions. The reviews surface several constructive suggestions (discrete median baseline, kernel ablation, gradient clipping analysis) that would strengthen the ablation story, but do not contribute new scientific insights beyond what the paper already provides.

## Suggestions
1. Correct the time complexity claim in Section 3.2 to O(N log(1/τ)).
2. Add a discrete L1 minimizer (median) baseline to Table 8 to disentangle the effect of interpolation from the L1 switch.
3. Include a brief justification for the Laplacian kernel choice, or an ablation comparing Laplacian vs. Gaussian.
4. Acknowledge that the risk is defined over the estimated posterior (minimum Bayes risk) rather than the true data distribution, to align the theoretical framing with standard decision theory terminology.
5. Add a sentence noting that G(y, p^m) is monotonic, guaranteeing that binary search converges to the unique root.

## Score and Decision

This paper makes a genuine contribution — a well-motivated reformulation of disparity prediction as L1 risk minimization, backed by a clean theoretical apparatus (implicit differentiation) and strong empirical results across five benchmarks. The weaknesses are bounded: the complexity claim is wrong but inconsequential for practice, the missing discrete median baseline is a genuine gap but does not invalidate the overall finding, and the remaining issues are presentation/analysis depth. The paper delivers on its central claims.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>