- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
I have now read the full paper and verified all claims. Let me construct the consolidated review.

## Summary

This paper frames continuous disparity prediction in stereo matching as risk minimization. The authors show that the commonly used disparity expectation is a special case of L² risk, and advocate for L¹ risk minimization to achieve more robust predictions, particularly under multi-modal disparity distributions. They enable end-to-end training by using implicit differentiation to backpropagate through the non-differentiable L¹ optimization. The method is evaluated extensively across SceneFlow, KITTI 2012/2015, Middlebury, and ETH3D, demonstrating state-of-the-art in-domain results and notably strong cross-domain generalization.

## Strengths

- **Theoretical unification of prior work**: The paper formally shows (Section 3.2) that the standard disparity expectation is a special case of their risk formulation under the L² error function. This provides a principled framework that connects and generalizes existing practice.

- **End-to-end trainable L¹ risk minimization**: By applying the Implicit Function Theorem (Section 3.3, Eq. 6–7), the authors derive a differentiable backward pass for the L¹ risk minimization. This technical enabler was lacking in prior approaches to L¹-style disparity prediction.

- **Strong in-domain results**: On SceneFlow, the method reduces >1 px error from 5.00 to 4.22 relative to the next best method (Section 4.1). It ranks first on KITTI 2012 non-occluded regions and achieves top results on KITTI 2015.

- **Superior cross-domain generalization**: When trained only on SceneFlow and tested on real-world datasets without fine-tuning, the method achieves first or second best across all four benchmarks (Tables 4–7). On ETH3D, >1 px error drops from 4.05 to 2.71 (Section 4.2). These are substantial absolute improvements over strong baselines.

- **Plug-and-play applicability**: The ablation (Section 4.3, Table 8) shows that replacing expectation with L¹ risk minimization at test time in ACVNet and PCWNet consistently improves accuracy without retraining, demonstrating that the formulation benefits stereo matching beyond the authors' own architecture.

- **Efficient inference**: The risk module adds no learnable parameters and increases runtime by only ~0.5 ms (Section 4.4), with an O(log N) binary search procedure.

## Weaknesses

### Fatal
None.

### Major

- **SMD-Net omitted from experimental comparisons**: The paper cites SMD-Net (Tosi et al., 2021) in Section 2.2 as a method that "exploit[s] bimodal mixture densities as output representation for disparities" — directly addressing the same multi-modal distribution problem that this paper targets. Yet SMD-Net does not appear in any performance table (Tables 1–7). Without this comparison, the reader cannot assess whether the risk-minimization approach outperforms the existing explicit multi-modal solution, which weakens the claim of "superior performance over current state-of-the-art methods" for the specific problem the paper frames as central.

- **No sensitivity analysis for kernel bandwidth σ**: The Laplacian kernel interpolation (Eq. 1) uses σ = 1.1 (line 115) without any justification or ablation. σ controls the shape of the interpolated probability density, which directly affects the risk function and its gradient (Eq. 7). The paper does not report whether results are stable across different σ values (e.g., σ ∈ {0.5, 1.0, 2.0}), nor does it discuss how to choose σ for new domains where disparity ranges differ substantially from SceneFlow's distribution. This is a methodological gap that affects reproducibility and trust in the reported results.

### Minor

- **No discussion of limitations**: The paper does not acknowledge that the Laplacian kernel is a crude density model, that the denominator clipping in Eq. 7 (threshold 0.1) may bias training gradients in certain numerical regimes, or that the binary search adds computational overhead (beyond noting it is small). A brief limitations section would strengthen the paper.

- **No analysis of failure cases**: The paper presents one qualitative success (Fig. 1) but does not show cases where both the proposed method and baselines fail similarly, or where the L¹ risk minimization introduces artifacts. An analysis of failure modes would improve understanding of the method's boundaries.

- **No performance variance reported**: The paper reports single-run results without variance estimates (standard deviations or confidence intervals). For the small absolute differences on some metrics (e.g., ~0.10–0.20 percentage points on KITTI), the reader cannot assess whether these differences are statistically reliable.

- **Kernel choice not discussed**: The paper uses a Laplacian kernel for density interpolation but does not discuss why it is preferred over a Gaussian or other kernel. While this does not invalidate the method, a brief rationale would improve methodological completeness (relevant to Section 3.1).

### Trivial

- The loss weighting (0.1 for coarse, 1.0 for refined, Section 3.5) is stated without any justification or ablation. A brief note or reference would help.
- The text "as shown in Alg." (line 115) is truncated — the algorithm reference is incomplete due to parser stripping. (This is a formatting artifact, not an author error.)

## Nice-to-Haves

- **Sensitivity analysis for σ and kernel choice ablation**: Adding experiments varying σ (e.g., 0.5, 1.0, 2.0) and comparing Laplacian vs. Gaussian kernels would directly test whether the robustness gains are inherent to the L¹ formulation or tied to the specific interpolation scheme.

- **End-to-end training for ACVNet/PCWNet with L¹ risk**: While the test-only plug-in results (Table 8) are already valuable, training these networks from scratch with the L¹ risk objective would strengthen the claim that the approach is broadly beneficial.

- **Failure case visualization**: A figure showing a case where the L¹ risk avoids an expectation-induced failure, alongside a case where both methods perform similarly, would improve qualitative understanding.

## Removed Points

The following points from the reviewer inputs were removed per the filtering rules:

1. *"The binary search algorithm is referenced but its text was stripped by the parser"* (Harsh Critic, "Missing Parts") — **Removed per Hard Rule**: Parser-stripped content (appendix, algorithms) is not an author error and exists in the original submission.
2. *"The paper does not discuss variance estimates"* from the "Strengthening the Paper on Its Own Terms" list about confidence intervals for test-set errors — Placed in Minor rather than inflated into a central weakness. The paper reports standard benchmarks where single-run evaluation is the norm in this field.
3. *"No ablation of the coarse/refined loss weighting (0.1 vs 1.0)"* (Harsh Critic, Section 3.5 note) — Moved from a standalone weakness to a Trivial note, as this is a minor design detail that does not threaten the paper's claims.
4. *Strengths about "important problem" or generic praise* from Strength Finder — The six strengths listed in the final review above are the only ones that are concrete, specific to the paper, and grounded in evidence. Generic praise (e.g., "this paper addressed an important problem") was removed.

## Novel Insights

None beyond the paper's own contributions. The Harsh Critic's observation that the L¹ risk minimization can serve as a test-time plug-in for other architectures (ACVNet, PCWNet) without retraining is already reported by the paper itself. The key insight — that the common expectation operation is equivalent to L² risk minimization, and switching to L¹ yields robustness gains — is the paper's own contribution and is well articulated.

## Suggestions

1. **Add SMD-Net to the cross-domain comparison tables** (Tables 4–7) to directly compare against the prior explicit multi-modal solution. Even if the authors cannot reproduce SMD-Net's results themselves, citing the best published numbers from the original paper would be informative.

2. **Include an ablation study for σ** — report the cross-domain metrics (at least on Middlebury and ETH3D) for σ ∈ {0.5, 1.0, 1.5, 2.0} to demonstrate that the L¹ robustness does not hinge on a finely tuned bandwidth.

3. **Add a limitations paragraph** in the conclusion or a separate section acknowledging: (a) the Laplacian kernel's limited capacity as a density model, (b) the potential training signal bias from the denominator clipping threshold (0.1), and (c) any failure modes observed during experimentation.

4. **Report run-to-run variance** for at least the main cross-domain results. This would help distinguish reliable improvements from noise on metrics with small absolute differences.
