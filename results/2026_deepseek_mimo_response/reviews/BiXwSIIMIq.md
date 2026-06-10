## Summary
This paper proposes the AC-DC denoiser, a three-stage score-based denoiser (Auto-Correction via noise injection, Directional Correction via conditional Langevin dynamics, and final score-based denoising) designed for the ADMM framework for inverse problems. The paper provides convergence analysis under both fixed and adaptive step-size regimes and validates across 7 inverse problems on FFHQ and ImageNet datasets.

## Strengths
- **Well-motivated DC stage with principled mechanism**: The DC stage runs conditional Langevin dynamics targeting p(z_σ|z_ac), whose support is contained in M_σ by construction (Section 3, Eq. 10). This provides a principled way to align iterates with score-trained manifolds, absent in prior work like DiffPIR or SNORE. The ablation in Figure 5 directly demonstrates that increasing DC steps J from 0 to 20 progressively removes artifacts in phase retrieval.
- **Layered convergence analysis extending ADMM-PnP theory**: Theorem 1 extends Ryu et al. (2019) by replacing strict contractiveness with weak nonexpansiveness (δ-ball convergence). Theorems 2-3 prove the AC-DC denoiser satisfies this assumption with high probability, and Theorem 3 removes the convexity assumption on ℓ via an adaptive step-size scheme. This three-theorem framework covers both convex and non-convex settings—a concrete advance over prior work.
- **Broad and strong experimental validation**: Table 1 presents results on 7 inverse problems (super-resolution, Gaussian/motion deblurring, random/box inpainting, phase retrieval, HDR) across FFHQ and ImageNet, compared against 8 baselines. The method achieves best or second-best in nearly all configurations, with particularly large margins on challenging tasks (e.g., phase retrieval: 27.94 vs. 26.71 next-best PSNR on FFHQ).
- **Honest limitations discussion**: Section 7 explicitly acknowledges the theory-practice gap, the need for recoverability analysis, heuristic noise schedules, and computational cost concerns—an unusually candid treatment.

## Weaknesses

### Fatal
None.

### Major
- **Theory-practice gap on noise schedule**: The convergence theorems (Theorems 2b, 3b) require σ^(k) → 0 as k → ∞, but the experimental noise schedule σ^(k) = max(0.1, 10 − (10 − 0.1)·k/W) plateaus at σ = 0.1 (line 297). This means experiments run under conditions not covered by any theorem. The δ-ball convergence radius r depends on the limiting noise level, so with σ never reaching zero, iterates are only guaranteed to stay *near*—not converge *to*—a fixed point. While the authors are honest about this in Section 7, the theoretical results do not directly explain the experimental success.

- **No computational cost analysis**: The AC-DC denoiser requires J+1 = 11 score function evaluations per ADMM iteration (Algorithm 1, lines 100-111), plus iterative Adam optimization for the x-subproblem (up to 1000 inner iterations, line 297), across K = W+10 outer iterations. Improvements over the strongest baseline DAPS are moderate—typically 0.4–1.2 dB PSNR (Table 1). Without any runtime, wall-clock time, or NFE comparison, it is impossible to judge whether these improvements justify the computational overhead. This is a material omission for a method paper proposing a multi-stage iterative procedure.

### Minor
- **Hyperparameter W never specified**: The decay window W determines total iterations (K = W+10) and the entire noise schedule trajectory (line 297 defines the schedule using W but never states its numerical value), making the experimental setup incomplete.
- **HDR and nonlinear deblurring claimed in abstract but absent from main results**: The abstract (line 28) claims validation on HDR and the task description (line 293) mentions nonlinear deblurring, but neither appears in Table 1. Either include them or remove from abstract.
- **Table 1 has incomplete/empty PMC entries**: PMC appears with empty cells in several rows (lines 334, 355-356, 365-366) and duplicate PMC rows in others (lines 324-325, 339-340), suggesting incomplete evaluation.
- **δ-ball convergence is a relatively weak guarantee**: Definition 2 establishes convergence to a neighborhood of a fixed point, not to the point itself. When σ plateaus at 0.1, the neighborhood radius does not shrink to zero.

### Trivial
- **Missing confidence intervals**: With 100 test images and improvements of 0.5–1.5 dB, reporting standard deviations would strengthen the quantitative claims and clarify whether gains are consistent or outlier-driven.

## Nice-to-Haves
- Report per-image computational cost (even a rough NFE count per image compared to baselines like DAPS and DiffPIR) so readers can contextualize quality improvements.
- Quantify the manifold alignment effect directly (e.g., distribution of ||z_ac − z_σ|| or distance from z_dc to M_σ) to validate the stated mechanism of *why* DC helps.
- Include a "no correction" ablation (direct score denoising, no AC or DC) alongside the J=0/J=10/J=20 ablation in Figure 5 to isolate the contribution of each stage individually.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Harsh critic's concern about Gaussian approximation quality for the likelihood (line 135) — the paper does discuss this approximation and the Var(s) ≪ σ condition under which it holds.
- Strawman weakness about fairness of comparison — improvements favor the authors' method; no asymmetry issue exists.
- Claims about missing appendix content — the parser strips appendices; they exist in the original submission.

## Novel Insights
The core novel insight is identifying the "manifold mismatch" problem specifically in ADMM-PnP with score-based denoisers—where dual variables further distort iterate geometry beyond what noise injection alone can address—and providing a principled solution via conditional Langevin dynamics (DC stage) to project iterates onto the correct noisy manifold. The conditional score decomposition in Eq. (10) and the connection between DC and conditional Langevin dynamics targeting p(z_σ|z_ac) is a genuinely new idea that extends PnP literature's understanding of score-based optimization integration.

## Suggestions
- Specify the value of W in the main paper to make experiments reproducible.
- Add a runtime/NFE comparison table for at least one task, comparing AC-DC against DAPS, DiffPIR, and DPS.
- Either include HDR and nonlinear deblurring results in Table 1 or remove these claims from the abstract.
- Clean up Table 1 to resolve duplicate/empty PMC entries.

---

## Calibration Report

**All anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| dAavOuxZvo.md (VIPaint) | 3.00 | 1 | Much weaker — no convergence theory, limited experiments |
| W4djmqKZC6.md (Pixel-Aware) | 3.00 | 1 | Much weaker — heuristic method, poor results |
| mHkbi3XM58.md (Conditional density) | 3.25 | 1 | Much weaker — different domain, limited scope |
| vK8C37eHXM.md (Sample what you can't compress) | 3.20 | 1 | Much weaker — preliminary autoencoder work |
| Z9Odi09Rv9.md (Fast Diffusion Solvers) | 4.75 | 1 | Weaker — experimental concerns, no convergence theory |
| nHESwXvxWK.md (Monte Carlo SGM) | 4.00 | 1 | Weaker — less complete evaluation |
| 1YO4EE3SPB.md (RED-diff) | 5.50 | 1,2 | Paper under review is stronger: has convergence theory RED-diff lacks, and outperforms it in experiments |
| bEDTZxwJjT.md (DiracDiffusion) | 5.50 | 1,2 | Paper under review is stronger: more complete theory and broader experiments |
| HXjXPQU3yJ.md (Prior Mismatch PnP-ADMM) | 6.25 | 2 | Similar scope but paper under review has broader experiments (7 vs 2 tasks), more novel mechanism (AC-DC vs domain adaptation) |
| x7d1qXEn1e.md (Restoration Network Implicit Prior) | 6.25 | 2 | Less directly relevant — focuses on general restoration networks |
| kRBQwlkFSP.md (DiffStateGrad) | 6.75 | 2 | Most comparable anchor: similar experimental setup, both address manifold alignment. Paper under review has convergence theory that DiffStateGrad lacks, but also has theory-practice gap |
| U3PBITXNG6.md (InverseBench) | 7.50 | 2 | Stronger — benchmark paper with different contribution type |
| TtUh0TOlGX.md (TReg) | 7.33 | 2 | Stronger — cleaner experimental setup, text regularization novelty |
| j8hdRqOUhN.md (ReSample) | 7.50 | 2 | Stronger — cleaner method, no theory-practice gap |
| 6EUtjXAvmj.md (Variational Diffusion Posterior) | 8.00 | 1 | Stronger — high-impact method with broad validation |
| 6O3Q6AFUTu.md (NoiseDiffusion) | 8.00 | 1 | Not directly comparable — image interpolation |
| I5lcjmFmlc.md (Robust Diffusion Classifier) | 8.00 | 1 | Not directly comparable — classification |
| fV0t65OBUu.md (Optimal Covariance) | 8.00 | 1 | Not directly comparable — covariance learning |

**Round 1 bracket**: Between 5.0 and 7.5. The paper is clearly better than the 4.75 rejected paper and the 5.50 anchors (RED-diff accepted, DiracDiffusion rejected), and comparable to DiffStateGrad (6.75, accepted).

**Round 2 narrowing**: The paper sits between Prior Mismatch PnP-ADMM (6.25, rejected — weaker experiments, less novel mechanism) and DiffStateGrad (6.75, accepted — no convergence theory but no theory-practice gap either). The paper has stronger theoretical contribution than DiffStateGrad but the theory-practice gap and missing cost analysis hold it back from 7+.

**Final score positioning**: 6.5 — the paper is a solid contribution with genuinely novel mechanism and convergence theory, outperforming 5.5 anchors but held back by the theory-practice gap and missing computational analysis relative to the 6.75 anchor.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>