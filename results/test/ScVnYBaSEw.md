Now I have a thorough understanding of the paper and the reviews. Let me produce the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper introduces UNSURE, a self-supervised learning framework for image reconstruction that bridges the gap between SURE (requires full noise-distribution knowledge but is expressive) and cross-validation methods (requires minimal noise knowledge but is overly constrained). The key insight is to relax the zero-derivative constraint of cross-validation to a zero-expected-divergence (ZED) constraint, which yields a family of estimators that can be trained via a saddle-point optimization without knowing the noise level, yet approach supervised performance. The framework is extended to correlated Gaussian noise, Poisson-Gaussian noise, and linear inverse problems.

## Strengths
- **Principled theoretical framework for the expressivity-robustness trade-off**: The paper characterizes self-supervised estimators by the constraints they impose on derivatives, formalizing a hierarchy: CV (zero per-pixel derivatives) ⊂ ZED (zero expected divergence) ⊂ SURE (no constraints). Propositions 1 and 2 provide closed-form solutions and MSE formulas for the optimal ZED estimator, giving a rigorous foundation (Section 3, Eqs. UNSURE, Prop. 1, Prop. 2).

- **Novel method that removes the need to know the noise level**: The UNSURE loss (Eq. UNSURE) uses a Lagrange multiplier to enforce the ZED constraint, and Algorithm 1 provides a practical training procedure. The multiplier converges to a value slightly above the true noise level (Fig. 2, left panel), showing implicit noise-level estimation during training. This is a clear advance over standard SURE, which requires the noise level as input.

- **Strong empirical results across multiple imaging modalities with unknown noise**: On correlated Gaussian denoising (DIV2K), UNSURE achieves 28.72 dB PSNR, outperforming Noise2Void (19.09 dB) and Neighbor2Neighbor (23.61 dB), and coming within ~1 dB of SURE with known covariance (29.77 dB) (Table 1). On accelerated MRI with unknown noise (Table 3), UNSURE+EI achieves 35.73 dB, outperforming CV+EI (33.25 dB). On CT with Poisson-Gaussian noise (Table 2), PG-UNSURE achieves 33.31 dB, close to PG-SURE with known parameters (33.76 dB).

- **Robustness to noise-level misspecification**: The paper demonstrates that SURE and R2R suffer large PSNR drops when the assumed noise level is wrong (Fig. 2, right panel), while UNSURE maintains high performance across all tested σ values — a key practical advantage.

- **Generalization to correlated noise, Poisson-Gaussian, and inverse problems**: The framework extends to unknown noise covariance (C-UNSURE, Theorem 1), Poisson-Gaussian noise (PG-UNSURE, Eq. PG-UNSURE), and incomplete measurements via a combined loss with equivariant imaging (Eq. General UNSURE), backed by experiments on all three settings.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison with two-stage baselines for non-Gaussian settings**: For the MNIST Gaussian denoising experiment, the paper does compare with Noise2Score (Kim 2022), which estimates the noise level from the learned score — this is a version of a two-stage approach. However, for the correlated-noise (DIV2K) and Poisson-Gaussian (CT) experiments, the paper compares only with cross-validation methods and SURE with *known* parameters. The reader cannot tell whether the single-stage saddle-point formulation provides a meaningful advantage over a simpler plug-in approach that first estimates the noise parameters (covariance matrix for correlated noise; σ, γ for Poisson-Gaussian) from data and then applies standard SURE. Without this comparison, the claim that the saddle-point formulation is the reason for the strong performance is unsubstantiated for these settings.

### Minor

- **Theory-practice gap not fully analyzed for learned networks**: Proposition 2 gives the MSE of the optimal ZED estimator, and Figure 1 validates this formula by post-hoc adjusting a *pretrained* MMSE denoiser via the convex combination in Eq. (8). However, this analysis is not extended to networks trained from scratch with the UNSURE loss. The paper does not examine whether the learned networks empirically satisfy the ZED constraint (i.e., whether E_y[div f(y)] ≈ 0 after training) or how close their performance is to the theoretical ZED optimum. While the theory is validated on a pretrained MMSE denoiser, connecting it to the end-to-end trained networks would strengthen the paper.

- **Saddle-point optimization convergence analysis is limited**: The paper states that the Lagrange multiplier η converges in a few epochs for MNIST, but provides no convergence plots or analysis for the harder problems (correlated noise on DIV2K, Poisson-Gaussian on CT, accelerated MRI). The primal-dual algorithm is applied to a non-convex objective, and it would be helpful to show that η (or η) stabilizes sensibly in these more complex settings.

### Trivial
- The abstract could more precisely convey that while the noise *level* (σ²) is unknown, the *structural form* of the noise distribution (Gaussian, correlated Gaussian with known basis, Poisson-Gaussian with known parametric form) must be specified. The paper is precise about this in Section 3.2, but a reader scanning only the abstract could overestimate the method's generality.

## Nice-to-Haves
- Overlay the predicted optimal ZED MSE (from Proposition 2) on the test PSNR curves of Figure 3 (MNIST experiment) to directly visualize the gap between theory and practice.
- Provide convergence plots for the Lagrange multiplier(s) in the correlated-noise and MRI experiments.
- Add a synthetic-data experiment where the signal dimension k can be tuned (e.g., a sparse linear model) to empirically verify the geometric-series formula in Eq. (9).
- The high-entropy failure case (Gaussian signal prior) is correctly identified; a brief discussion of how to detect or guard against such degenerate cases in practice would be welcome.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Criticism about notation/readability of divergence and Jacobian** — This is a formatting/presentation nitpick that does not affect the paper's substance. Removed per formatting nitpick rule.
- **Criticism about the inverse-problem UNSURE loss (Eq. 12) being "sketched very briefly"** — The paper explicitly references the appendix for more details ("please see Appendix for more details"). The appendix was stripped by the parser, so this criticism reflects a parser artifact, not an author error. Removed per missing-appendix rule.
- **Criticism about lacking pseudocode for the inverse-problem case** — The paper focuses on denoising for the main pseudocode and references the appendix for inverse-problem details, which was stripped by the parser.
- **Criticism about the Noise2Score baseline comparison being insufficient** — For the Gaussian denoising experiment, the paper compares with Noise2Score (Kim 2022), which *does* estimate the noise level from the score. This partially addresses the critic's demand for a two-stage baseline. The criticism is factually incomplete and is removed from the main weaknesses, though the broader concern about non-Gaussian settings remains in Major.

## Novel Insights
The key insight that emerges from synthesizing the reviews is that the paper's theoretical contribution (the ZED framework and its closed-form solution) is its strongest element, but the empirical validation has a systematic edge that the authors could sharpen: the theory predicts the performance of the optimal ZED estimator in terms of the MMSE and noise level, yet the experiments evaluate the trained networks' performance without directly measuring whether the networks actually satisfy the ZED constraint or how close they are to the theoretical prediction. Connecting these dots would not only strengthen the paper but also provide a diagnostic tool for practitioners deploying UNSURE in new settings.

## Suggestions
1. Add a controlled comparison with a two-stage baseline for the correlated-noise and Poisson-Gaussian experiments: first estimate the noise parameters (covariance basis coefficients, or γ and σ for PG) using a simple estimator (e.g., moment-based), then train the same network with standard SURE using the estimated parameters. This would isolate the benefit of the joint saddle-point formulation.
2. After training with the UNSURE loss, compute the empirical expected divergence on a held-out set and report it alongside the test PSNR, to directly verify that the ZED constraint is approximately satisfied.
3. Provide convergence trajectories of the Lagrange multiplier(s) for the DIV2K correlated-noise and CT experiments, as done for MNIST in Figure 2.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>