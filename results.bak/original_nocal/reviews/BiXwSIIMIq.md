Now I have a thorough understanding of the paper and can verify the reviewers' claims against the actual content. Let me produce the final review.

## Summary

This paper introduces the AC-DC denoiser, a three-stage score-based denoiser (auto-correction via additive Gaussian noise, directional correction via conditional Langevin dynamics, and Tweedie/ODE denoising) designed to mitigate the mismatch between ADMM iterates and the noisy data manifolds on which diffusion score functions are trained. The method is embedded in ADMM for plug-and-play inverse problem solving. The paper provides convergence analysis (fixed-point ball convergence under strong convexity, and high-probability convergence under an adaptive step-size schedule without convexity) and evaluates on six inverse problems across FFHQ and ImageNet against eight baselines.

## Strengths

- **AC-DC denoiser design with explicit manifold alignment rationale**: The three-stage structure (Algorithm 1) provides a clear conceptual framework for addressing the geometry mismatch between ADMM iterates and score-trained manifolds. The AC stage injects noise to bring iterates closer to noisy manifolds, while the DC stage uses conditional Langevin dynamics to refine alignment. This goes beyond the simpler noise-injection strategies used in prior work (e.g., DiffPIR, RED-diff). The ablation in Figure 5 directly demonstrates the effect of the DC stage: increasing J from 0 (AC only) to 20 progressively removes artifacts on the phase retrieval problem.

- **First convergence analysis for score-based denoisers in ADMM-PnP**: Theorems 1–3 extend prior ADMM-PnP fixed-point convergence theory (Ryu et al., 2019; Chan et al., 2016) to diffusion score-based denoisers. Theorem 1 relaxes the strict contractivity requirement to weak nonexpansiveness (Assumption 1), and Theorem 2 shows that the AC-DC denoiser satisfies this property with high probability under Assumptions 2–3. Theorem 3 further relaxes the strong convexity requirement on the data fidelity term. While the guarantees are (by the paper's own acknowledgment) limited to fixed-point convergence, this is the first theoretical treatment of score-based denoisers within a primal–dual PnP framework.

- **Broad and competitive empirical evaluation**: The method is tested on six tasks (super-resolution, random inpainting, box inpainting, Gaussian/motion deblurring, phase retrieval) across two standard datasets (FFHQ 256×256, ImageNet 256×256) with 100 test images each. In Table 1, both Ours-tweedie and Ours-ode achieve the best or second-best results on nearly all metric-task combinations against eight strong baselines (DPS, DAPS, DDRM, DiffPIR, RED-diff, DPIR, DCDP, PMC). The qualitative results (Figures 2–4) support the quantitative findings.

## Weaknesses

### Fatal
None. The paper's core claims—a novel three-stage denoiser, convergence analysis in an idealized setting, and competitive empirical results—are supported by the presented evidence. The weaknesses below are substantive but do not invalidate the paper.

### Major

- **Gap between theoretical assumptions and practical implementation regarding the DC Langevin dynamics**: Theorems 2 and 3 assume "the DC step reaches the stationary distribution for each k," while the practical algorithm uses only J=10 Langevin steps. This is a significant gap because 10 steps in a high-dimensional space (e.g., 256×256×3 images) are orders of magnitude short of mixing. The paper notes in a footnote that "counterparts removing this assumption" exist in Appendix E.2. *However*, even if the stationarity assumption can be removed, the practical question remains: do J=10 steps suffice for the DC correction to be effective in the sense required by the theory? The paper provides no empirical diagnostics (e.g., convergence of the Langevin chain, distance from stationary distribution) to bridge this gap. As presented, the theoretical guarantees and the implemented algorithm operate under different conditions, and the relationship between them is not quantified.

### Minor

- **Theory requires vanishing noise schedule, practice uses non-vanishing noise**: Theorem 3(b) requires lim_{k→∞} σ^{(k)} = 0 and lim_{k→∞} σ_{s^{(k)}} = 0 for convergence to a fixed point. The empirical schedule uses σ^{(k)} = max(0.1, 10 - (10-0.1)·k/W), which plateaus at a noise floor of 0.1. The paper does not discuss whether this mismatch affects the applicability of the convergence guarantee or whether the 0.1 floor is practically negligible.

- **Missing hyperparameter values for the decay window W**: The σ^{(k)} schedule is defined over a "W decay window," and the total iterations are K = W+10, but the numerical value of W is not reported in the main text. This makes it difficult to assess the computational budget or reproduce the schedule precisely. (If W is specified in the appendix, a cross-reference would be helpful.)

- **No variance or confidence intervals reported**: All metrics in Table 1 are reported as point estimates averaged over 100 images, with no standard deviations, confidence intervals, or statistical significance tests. While this is common in the field, the absence is notable given the paper's claim of "consistently improves solution quality." Some of the observed advantages over second-best methods are small (e.g., 0.3–0.5 dB PSNR), and without variance information it is hard to assess robustness.

- **No runtime or NFE comparison**: The AC-DC denoiser requires multiple score evaluations per ADMM iteration (J=10 Langevin steps plus Tweedie/ODE denoising), which is computationally more expensive than methods like DiffPIR or DPS. The paper acknowledges this in the Limitations section but does not quantify the overhead. A comparison of wall-clock time or total NFEs would help readers assess the cost of the performance improvement.

- **One inverse problem (Box Inpainting on FFHQ) shows DCDP outperforming Ours-tweedie on PSNR (25.230 vs. 24.025)**: Ours-tweedie is still best on SSIM and LPIPS for this task, so the claim of "best or second-best in terms of all metrics" holds. However, the claim of "consistently improves solution quality" should be read with the nuance that the improvement is not universal across every metric-task combination.

### Trivial

- The baseline label "DiPIR" in Table 1 appears to be a typo for "DiffPIR" (which is correctly spelled elsewhere in the paper). The parsed table also shows "DDPM" under Gaussian Blur instead of "DDRM" (listed in the baselines). These are minor labeling inconsistencies.

## Nice-to-Haves

- An ablation that tests the full pipeline without the AC stage (i.e., DC + Tweedie directly on the raw ADMM iterate) to further isolate the contribution of the AC step. The current ablation (Figure 5) varies only the DC steps J, comparing AC-only (J=0) to AC-DC (J>0).
- A plot of convergence behavior (PSNR or objective vs. ADMM iteration) for AC-DC vs. baselines, to show whether the fixed-point ball convergence translates to practical stability.
- Empirical diagnostics checking whether J=10 Langevin steps yield iterates plausibly close to the stationary distribution of the Langevin SDE.

## Removed Points

- **"Convergence guarantees do not apply to practical algorithm because Appendix E.2 is not provided"**: Removed per the rule that the parser strips appendices from all papers; the appendix exists in the original submission. The footnote referencing Appendix E.2 indicates the authors are aware of and claim to address this concern.
- **"Table formatting errors (double PMC rows, empty cells)"**: Removed per the rule about formatting artifacts being parser issues. The original PDF may have proper formatting (e.g., merged cells).
- **"The paper overlooks DiffPIR and other PnP-ADMM works"**: Removed as factually incorrect — Section 2 explicitly discusses DiffPIR, and the paper frames its novelty as the AC-DC denoiser design and convergence analysis, not ADMM integration per se.
- **"Convergence notion is too weak to support the paper's claims"**: Weakened and moved to minor/nice-to-have. The paper explicitly acknowledges this limitation ("all theoretical results in this section focus on fixed-point convergence, which is not the strongest form") and situates it within the existing PnP convergence literature, which faces the same challenge.
- **"Missing ablation separating all three stages"**: Weakened. Figure 5 tests AC-only (J=0) vs. AC-DC (J=10, 20), which isolates the DC stage. The baselines (DiffPIR, DPS, DDRM, etc.) serve as comparisons against "direct score-based denoising without AC-DC." A complete ablation of all combinations would be nice-to-have but is not missing.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the standard tension between idealized theoretical assumptions and practical implementation, which the paper partially addresses (via Appendix E.2) and partially leaves open. No reviewer identified a hidden flaw or unclaimed strength that changes the overall assessment of the paper.

## Suggestions

1. In the main text or a visible table, provide the numerical value of W and other key hyperparameters (e.g., total score evaluations per experiment) to improve reproducibility.
2. Add standard deviations or confidence bands to Table 1, at least for the primary metric (PSNR), to allow readers to judge the significance of observed improvements.
3. Discuss the relationship between the theoretical requirement lim σ^{(k)} → 0 and the practical noise floor of 0.1 explicitly, and note whether the theory can accommodate this or whether the gap is practically negligible.
4. Add a brief empirical note on how many Langevin steps would be needed to approach the stationary distribution (e.g., monitoring the KL divergence or energy distance) for a representative ADMM iterate. If this is infeasible, state so explicitly.
5. Include a runtime or NFE table to help readers understand the computational cost of the AC-DC denoiser relative to baselines.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>