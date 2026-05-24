Now let me write the consolidated review.

## Summary

This paper proposes STNAdam, a stochastic optimizer for "nonconvex + weakly-convex" composite optimization that combines a two-track iteration framework (an extrapolation track via Nesterov momentum and a regular update track via Adam-style adaptivity) with variance-reduced gradient estimation. The authors provide convergence analysis under the Kurdyka-Łojasiewicz property and demonstrate empirical results on low-light image enhancement (LIE) tasks.

## Strengths

- **Novel two-track algorithmic architecture**: The two-track coupled iteration (Algorithm 1, Figure 1(d)) maintains two intertwined trajectories — an extrapolation point $\bar{x}^{k+1}$ and a regular update $x^{k+1}$ — governed by separate momentum estimates ($\hat{\varpi}^{k+1}$ and $\tilde{\varpi}^{k+1}$). This is a genuine architectural departure from single-track methods like NAdam and SNAdam, and the idea of enlarging the update neighborhood through dual trajectories is conceptually interesting.

- **General convergence framework accommodating arbitrary variance-reduced estimators**: Theorem 1 establishes the finite-length property and Theorem 2 provides explicit convergence rates depending on the KL exponent. Crucially, Lemma 1 defines the variance-reduced gradient estimator condition generically, and the paper shows that SGD, SAGA, and SARAH all fit within this framework (Section 2). This level of generality — covering SVRG, SAGA, SARAH, and SPIDER under a unified analysis — is a technically ambitious theoretical contribution.

- **Strong empirical performance on LIE**: In Table 2, STNAdam-SARAH achieves PSNR 22.26 / SSIM 0.906 / LPIPS 0.050, substantially outperforming all baselines. Notably, even STNAdam-SGD (using plain SGD, no variance reduction) achieves 18.06 PSNR vs. SNAdam's 17.14 and SGD's 14.80, suggesting the two-track structure itself provides a benefit beyond variance reduction. Table 3 further shows STNAdam-SARAH dominating LIME, LR3M, and Retinex-Net on denoising tasks.

## Weaknesses

### Fatal
None.

### Major

- **Adaptive parameter intervals lack practical guidance, undercutting the "removing hand-tuning" claim**: The update intervals in equations (6)–(8) depend on constants $L$ (Lipschitz modulus), $\tau$ (weak convexity modulus), $V_1, V_\Upsilon, \rho$ (estimator-dependent), and critically on $M, s$ — which are themselves theoretical analysis parameters from the energy function (9) described only as "within some certain intervals." The abstract and Section 1.2 claim this "removes hand-tuning," but a practitioner has no concrete mechanism to compute these bounds without estimating problem-dependent constants or resolving the circular dependency on $M$ and $s$ (which are part of the proof structure, not independently known). The bounds are mathematically valid existence claims, but the paper overstates their practical utility by suggesting they make the algorithm hyperparameter-free.

- **Experimental evaluation does not fully isolate the two-track contribution**: While STNAdam-SGD vs. SNAdam (Table 2) partially controls for gradient estimator (both use SGD-like estimators), the paper lacks a critical ablation: comparing STNAdam-SARAH against a single-track optimizer that also uses SARAH (e.g., SNAdam with SARAH, or a SARAH-Adam hybrid). Without this, the large performance gap between STNAdam-SARAH and SNAdam (22.26 vs. 17.14 PSNR) cannot be cleanly attributed to the two-track framework vs. the variance reduction from SARAH. Additionally, the baselines do not include NAdam (which is the closest single-track analog to the proposed architecture), and no standard deep learning benchmarks (CIFAR, ImageNet, language modeling) are provided to demonstrate generalizability beyond LIE.

- **Citation inconsistency for a baseline**: The paper states "SAdam (Kingma & Ba, 2014)" in the experiment section (line 285), but Kingma & Ba (2014) is the original Adam paper, not SAdam. The related work section (line 37) correctly attributes SAdam to Le-Duc et al. (2024). This inconsistency calls into question which algorithm was actually used as the SAdam baseline and whether it was implemented faithfully.

### Minor

- **Vague "randomly select" in Algorithm 1 Step 3**: The algorithm says "Randomly select weighted parameters $\gamma_{k+1}, \alpha_{k+1}, \lambda_{k+1}$ within some updated intervals" but does not specify the distribution (uniform? arbitrary?). This matters for reproducibility since different distributions could affect empirical behavior.

- **Evaluation limited to a single application domain**: All experiments are on LIE. While the results are strong, the paper would benefit from at least one additional task (e.g., classification, denoising) to establish broader relevance of the two-track framework.

- **No convergence curves or training dynamics**: Only final metrics are reported (Tables 2, 3) with no loss trajectories, residual plots, or convergence behavior over iterations, making it impossible to assess optimization dynamics.

### Trivial
None.

## Nice-to-Haves

- Include training curves and convergence trajectories for at least the LOL dataset experiments.
- Add an ablation comparing STNAdam-SARAH against a single-track optimizer with SARAH gradient estimation.
- Benchmark on standard deep learning tasks (CIFAR-10/100 classification) to demonstrate generalizability.

## Removed Points

These points were flagged by reviewers but are removed with justification:

- **"Convergence analysis is critically incomplete in the main paper" (Harsh Critic #3)**: This criticism targets the absence of proofs that were deferred to an appendix. The parser strips appendix content from all papers; the proofs exist in the original submission per the paper's note ("The detailed proofs... are provided in the appendix"). Per hard rules, this criticism is invalid.

- **"Algorithm randomness not reconciled with convergence proof" (Harsh Critic #4)**: The convergence analysis uses worst-case lower bounds ($\underline{\gamma}, \underline{\lambda}, \underline{\alpha}$) which guarantee descent for any draw within the intervals. This is standard Lyapunov analysis technique. The critic's concern about unaccounted variance from parameter randomness misunderstands the proof structure — the gradient noise, not parameter selection within feasible bounds, is the source of variance.

- **"Time values unrealistic"**: Table 2 reports per-iteration times in seconds. Values like $2.85 \times 10^{-5}$s (28.5 μs) are plausible per-iteration times for image-level optimization; the paper does not claim these are end-to-end processing times.

- **"Second-time ME correction never explained"**: It is explained as "$\tilde{m}^{k+1} = \gamma_{k+1} \hat{m}^{k+1} + (1 - \gamma_{k+1}) \nabla f(x^k)$" (Table 1) — a convex combination of bias-corrected momentum and the current gradient, analogous to NAdam's Nesterov correction.

- **"Two-track not sufficiently distinguished from Nesterov acceleration"**: Figure 1(d) explicitly illustrates the difference from single-track NAG, Adam, and NAdam. The two-track maintains two separate points ($x^k$ and $\bar{x}^{k+1}$) with separate momentum estimates, which is structurally distinct.

- **Miscellaneous nitpicks about formatting, missing training curves (as fatal)**: These are either parser artifacts or minor issues that do not threaten the core claims.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension: the paper makes a strong "removing hand-tuning" claim about its adaptive parameter intervals, but the intervals depend on problem-dependent and analysis-internal constants whose practical estimation is not addressed. This disconnect between theoretical ambition and practical specification is the central unresolved issue.

## Suggestions

1. Provide a practical default or estimation procedure for the constants $L$, $\tau$, $M$, $s$ in equations (6)–(8). Without this, the adaptive parameter update scheme is not actionable and the "removing hand-tuning" claim should be softened.
2. Add an ablation: STNAdam-SARAH vs. a single-track Adam/NAdam variant that also uses SARAH gradient estimation. This is the cleanest way to isolate the two-track effect.
3. Fix the SAdam citation (currently attributed to Kingma & Ba 2014 instead of Le-Duc et al. 2024).
4. Specify the random selection distribution in Algorithm 1 Step 3.
5. Include at least training curves (loss vs. iteration) for the main comparison, and ideally one additional benchmark task beyond LIE.
6. Add standard convergence plots (e.g., $\|x^{k+1} - x^k\|$ or $\Phi(x^k)$ over iterations) to support the theoretical convergence results visually.

---

**Calibration Anchors (list of all returned anchors):**

| Path | Avg Score | Comparison to this paper |
|------|-----------|-------------------------|
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/jj7b3p5kLY.md (AdEMAMix) | 6.60 | Stronger practical contribution with thorough ablations on standard benchmarks; less theoretical ambition. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/CtM5xjRSfm.md (AlgoPerf) | 7.00 | Large-scale empirical study, not directly comparable. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/zCZnEXF3bN.md (Double Momentum) | 6.00 | Stronger convergence theory with practical claims; cleaner experiment design. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/r4Q86nBQka.md (INNAprop) | 5.00 | Less novel extension but more thorough benchmarks. This paper has more algorithmic novelty but narrower experiments. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/mEBSeSk49H.md (Convergence of Adam) | 4.25 | Theory paper with proof issues and unrealistic assumptions; comparable quality concerns. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/YGWGhdik6O.md (Optimizer Search) | 3.00 | Incomplete experiments, limited contributions. This paper is stronger. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/aF1jasJeRy.md (Torque-Aware Momentum) | 4.67 | Comparable optimizer paper with modest experiments but cleaner ablations. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/2KWZjdFwmh.md (StEVE) | 4.25 | Similar story: new optimizer, theory in appendix, experiments on limited domains. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/gBT6rAEqvx.md (Adaptive Second-Order) | 3.80 | Theoretical paper with unclear practical value; comparable quality level. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/DIAaRdL2Ra.md (Adafactor Convergence) | 5.00 | Cleaner convergence analysis for a known optimizer. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/PVHoELf5UN.md (LIE Denoising) | 6.40 | Stronger LIE-specific contribution with more complete experiments. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/sUywd7UhFT.md (Multi-Objective HH) | 2.50 | Less rigorous; this paper is substantially stronger. |

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>