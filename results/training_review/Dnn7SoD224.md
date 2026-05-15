I have now thoroughly verified the paper content against all reviewer claims. Let me produce the consolidated review.

---

## Summary

This paper proposes a novel formulation for continuous disparity prediction in stereo matching by reframing it as a risk minimization problem. The authors show that the standard expectation-based prediction (used by most classification-based stereo networks) corresponds to L² risk minimization, and advocate for L¹ risk minimization to improve robustness to multi-modal disparity distributions. To make L¹ optimization differentiable, they leverage the implicit function theorem, enabling end-to-end training. Experiments on SceneFlow, KITTI 2012/2015, Middlebury, and ETH3D demonstrate improvements over many state-of-the-art methods, particularly in cross-domain generalization.

## Strengths

- **Novel risk-minimization formulation for disparity prediction.** The paper rigorously derives that the standard expectation is an L² special case of the proposed risk framework (Section 3.2, Eqs. 2–4), and motivates L¹ risk as a principled alternative. Figure 2 provides a clear illustration of why L² expectation fails at object boundaries while L¹ risk is more robust. This reframing is conceptually clean and underexplored in the stereo matching literature.

- **Differentiable L¹ optimization via the implicit function theorem.** The non-differentiability of the L¹ minimizer is a genuine challenge, and the authors provide a technically sound solution: a binary-search forward pass (Algorithm 1) plus an analytical gradient via the implicit function theorem (Eq. 7). This enables end-to-end training with L¹ disparity selection, which prior work did not achieve. The gradient derivation (Eq. 7) is correct and efficient, adding no extra parameters.

- **Substantial and consistent cross-domain generalization improvements.** The method achieves its largest gains on datasets unseen during training, which is the strongest evidence for its core claim of improved robustness. On ETH3D, >1px error drops from 4.05 (second-best) to 2.71 (Table 5); on Middlebury, from 13.76 to 12.63 (Table 4). These are meaningful differences that suggest genuine robustness benefits under domain shift.

- **Clean ablation study isolating the L¹ effect.** Table 8 convincingly demonstrates three results within the same architecture: (i) test-time switching from expectation to L¹ already improves accuracy; (ii) training with L¹ further improves results; (iii) plugging L¹ risk into existing networks (ACVNet, PCWNet) at test time improves all metrics without retraining. This provides direct evidence for the method's effectiveness independent of architecture.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparisons against the most directly relevant methods.** The paper's central motivation is handling multi-modal disparity distributions. Section 2.2 discusses three families of methods that explicitly target this same problem — SMD-Net (Tosi et al., 2021) using bimodal mixture densities, Garg et al. (2020) using offset-based regression with Wasserstein supervision, and Yang et al. (2022) using top-K hypotheses. Not a single one appears in the experimental comparisons (Tables 1–7). The paper compares against IGEV, DLNR, PSMNet, and others, all of which use either expectation or iterative regression — i.e., methods that do not specifically address multi-modality. Without comparisons to the methods that are most directly competing with its stated contribution, the claim that L¹ risk minimization is superior for multi-modal robustness is unsubstantiated. This is a gap in experimental design, not a minor omission.

- **No hyperparameter sensitivity analysis for the key parameter σ.** The Laplacian kernel bandwidth σ=1.1 (set in line 115) controls the shape of the interpolated probability density, which directly determines the L¹ optimum. If σ is too large, the density becomes nearly uniform and the L¹ solution converges to the median of a vague distribution; if σ is too small, the interpolation peaks at discrete hypotheses and L¹ approximates a mode. The paper provides zero ablation or sensitivity analysis for σ (or for the convergence threshold τ=0.1 or the gradient denominator clipping threshold 0.1). Without this, it is unclear whether the reported gains are robust to σ or depend on careful tuning.

### Minor

- **Architecture and risk formulation contributions are conflated in the main results.** Tables 1–7 compare the authors' full pipeline (cascade architecture + L¹ risk) against methods with completely different architectures (IGEV, DLNR, RAFT-Stereo). This makes it impossible to attribute improvements to the risk formulation vs. the cascade design. The ablation (Table 8) partially addresses this by isolating the L¹ effect within a fixed architecture, which is commendable, but the main benchmark tables should ideally report both the full method and the baseline architecture with expectation. The paper would benefit from training the identical cascade architecture with expectation and reporting those numbers alongside the L¹ results on all benchmarks.

- **No error bars or statistical significance.** Tables 1–7 report single numbers. On KITTI 2012, the >2px non-occluded improvement is 0.11 percentage points (1.17 → 1.06) — well within potential noise given only 194 training images. While single-submission norms for KITTI leaderboards mitigate this concern for the test set results, the ablation study (Table 8) could easily report variance over multiple runs. This is especially important for the small in-domain improvements.

- **No limitations or failure case analysis.** The paper never acknowledges that for truly multi-modal distributions at occlusion boundaries (where both foreground and background disparities are valid), no single-valued prediction — L¹, L², or median — can be correct. The framing implies L¹ "solves" multi-modality, but it really selects one mode, which is sometimes the correct one and sometimes not. A discussion of when and why L¹ might fail (e.g., textureless regions, nearly uniform distributions) would strengthen the paper.

### Trivial

- **The claim of a "radically different perspective" (line 19) is overstated.** Showing that L² expectation is a special case of risk minimization is a straightforward mathematical observation. The real contribution is in making L¹ minimization differentiable, which should be the focus of the novelty claim.

- **The Laplacian kernel is chosen without justification** (Section 3.1). A Gaussian kernel would produce different gradient expressions and different L¹ optima. The paper should briefly justify the choice or note that the framework is agnostic to the kernel choice.

- **The broad applicability claim** (Abstract: "holds promise for... robotics and control engineering") is unsupported hyperbole. The paper presents a stereo matching technique; extrapolating to control theory is speculative.

## Nice-to-Haves

- An analysis of where L¹ helps vs. hurts: failure cases or visualization of disparity distributions where L¹ performs worse than expectation, which would help characterize the method's scope of applicability.
- A brief discussion of whether other loss functions (e.g., Huber) could be integrated into the risk minimization framework and why L¹ was specifically chosen.
- Runtime numbers specifically isolating the L¹ risk module overhead in absolute terms (the paper notes it "adds minimal overhead" but the Table 8 runtime increase of 0.08s for a 1024×768 image is mentioned without discussing whether this matters in practice).

## Removed Points

- **Criticism about "cannot be independently verified" regarding reproducibility**: No such criticism was made. All removed points below are from the harsh critic's review that fail the verification rules.
- **"Methods missing — need comparison to SMD-Net, Garg et al., Yang et al."**: KEPT (see Major weaknesses above). However, note that the reviewer's framing that this is a "direct failure to test the proposed solution against existing solutions" is slightly over-broad — the paper does demonstrate L¹ > expectation cleanly in the ablation. The gap is specifically about comparing against multi-modal handling methods, not a total failure of evaluation.
- **"The integral claim is correct... but the density shape depends on σ"**: KEPT as part of the hyperparameter sensitivity weakness.
- **"Network architecture is separable from L¹ risk contribution"**: KEPT as a minor weakness (architecture conflation).
- **"No limitations section"**: KEPT as a minor weakness.
- **General observation about L¹ not truly solving multi-modality**: KEPT as part of the limitations weakness.
- **Generic nitpick about "radically different perspective" being overstated**: KEPT as a trivial weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation about the method that the authors themselves did not articulate.

## Suggestions

1. **Add comparisons to SMD-Net, Garg et al. (2020), and Yang et al. (2022)** on the cross-domain benchmarks (Middlebury, ETH3D) where your method shows the largest gains. If these methods cannot be reproduced, clearly state why and provide whatever comparison is feasible (e.g., cite published results on the same benchmarks). This is essential to substantiate the claim that L¹ risk minimization advances multi-modal handling.
2. **Ablate σ** over a range (e.g., 0.1 to 5.0) on a validation set and report EPE and >1px error. Show that the gains are not brittle to this choice. Similarly, discuss the sensitivity to the gradient clipping threshold.
3. **Report the cascade architecture baseline with expectation** on all benchmarks (not just in the ablation), so readers can attribute improvements to the risk formulation vs. the network design.
4. **Add a limitations section** discussing failure cases — e.g., textureless regions, near-uniform distributions, occlusion boundaries where no single prediction is correct.
5. **Temper the novelty claims.** The paper's real contribution is the differentiable L¹ risk minimization, not the "radically different perspective" of risk minimization itself. Frame the contribution accordingly.
6. **Add variance reporting** for the ablation study (Table 8) over multiple training runs, even if the benchmark results follow single-submission norms.

## Score and Decision

The paper presents a technically sound contribution — differentiable L¹ risk minimization for stereo matching — with compelling cross-domain evidence. However, the experimental evaluation has significant gaps: the paper does not compare against the methods that most directly address its stated problem (multi-modal handling), provides no hyperparameter sensitivity analysis for the key parameter σ, and conflates architecture and risk contributions in the main results. These gaps are addressable but require substantial revision. The core idea is solid; the evaluation does not yet fully support the claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>