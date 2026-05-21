Now I have enough calibration data to write a well-anchored review. Let me finalize.

## Summary

This paper tackles Wasserstein Geodesic Principal Component Analysis (GPCA) — finding geodesic curves in the Wasserstein space that best capture variation in a dataset of probability measures. It makes two algorithmic contributions: (1) for centered Gaussian distributions, it lifts the GPCA problem to the flat space $GL_d$ via the Bures-Wasserstein geometry (Proposition 3), enabling exact (non-linearized) computation; (2) for general absolutely continuous measures (GPCAGEN), it parametrizes geodesics using MLPs through Otto's formulation, with orthogonality and intersection constraints enforced via regularization. The paper also quantifies distortion between TPCA and GPCA (Proposition 4) and proves that univariate Gaussian GPCA stays within the Gaussian family (Proposition 5).

## Strengths

- **Exact lift of Gaussian GPCA to $GL_d$ (Proposition 3).** Replacing the geodesic search in curved $S_d^{++}$ with a constrained optimization over horizontal lines in $GL_d$ (incorporating rotation variables $Q_i$ and a clipping operator) is a nontrivial theoretical reformulation that makes exact GPCA tractable for Gaussians.

- **Analytical quantification of TPCA vs. GPCA distortion (Proposition 4, Equation 14).** The closed-form expression for the ratio of Bures-Wasserstein distance to its linearized counterpart in terms of eigenvalue spread $(a-b)/(a+b)$ and orientation $\theta$ gives a concrete measure of when linearization fails, backed by numerical experiments showing up to 35% cost improvement (Figure 4, right).

- **Proof that univariate Gaussian GPCA stays Gaussian (Proposition 5).** Resolves a natural theoretical question and justifies restricting to the Gaussian submanifold in 1D.

- **Avoidance of input-convex neural networks in GPCAGEN.** By using Otto's parametrization with general MLPs for $\varphi_\theta$ and $f_\psi$, the method avoids the convexity constraint typical of ICNN-based approaches, with the trade-off (monitoring Hessian eigenvalues) stated clearly.

- **Gaussian GPCA experiments include quantitative comparison to TPCA.** The random-matrices test reports numerical cost improvement (<1% on average across 100 trials), and Figure 4 (right) quantifies cost improvement over TPCA as a function of eigenvalue spread.

## Weaknesses

### Major

- **No quantitative evaluation of GPCAGEN on real data.** The general-case experiments (3D point clouds, landscape images, MNIST) are entirely qualitative. The paper explicitly declines numerical comparison to TPCA, stating "a direct numerical comparison between the two methods is therefore not meaningful" (Section 5.2). Yet the paper's central motivation is that GPCA improves upon TPCA. Without any quantitative metric — reconstruction error, variance explained (Equation 1 evaluated as a number), projection residual, Sinkhorn divergence between projected and original distributions — the reader cannot judge whether GPCAGEN offers a practical advantage. The Gaussian experiments are quantitative, but the general-case method is the paper's headline contribution. This is the single most important evidential gap.

- **Missing quantitative constraint validation for GPCAGEN.** The paper does not report final values of the regularization terms $\mathcal{I}$ and $\mathcal{O}$ after training. Without this, the reader cannot verify that the learned components actually intersect orthogonally — a core requirement of the GPCA definition. The paper mentions $\lambda_I = \lambda_O = 1.0$ "ensures the algorithm works as expected in all experiments" but offers no numerical evidence.

### Minor

- **Optimization procedure for Gaussian GPCA underspecified.** Proposition 3 involves optimizing over $SO(d)$ rotation matrices $(Q_i)$ jointly with $A_1$ and $X_1$. The paper does not describe how this is done — Riemannian gradient descent on $SO(d)$, alternating minimization, axis-angle parameterization? The clipping operator $p_{A,X}$ is introduced but its effect on gradients is not discussed.

- **No sensitivity analysis for $\lambda_I$, $\lambda_O$.** These are fixed to 1.0 across all experiments with no ablation or robustness study. For a method whose constraints are critical to the definition of GPCA, this is a notable omission.

- **Choice of reference measure $\rho$ is fixed to standard Gaussian.** The paper claims the approach is "independent of the chosen reference measure" (abstract), but this independence is not empirically verified.

- **Computational cost and scaling are not discussed.** No information on training iterations, wall-clock time, scaling with dimension $d$ or number of samples $n$, or batch size $m$ is provided in the main paper (deferred to the stripped appendix).

### Trivial

- The captions for Figures 1 and 2 include repeated boilerplate text that appears to be a parser artifact.

## Removed Points

These points were flagged for removal; treat them with caution.

1. **"'Exact' GPCA claim is misleading."** — The paper explicitly defines "exact" (end of Section 1): "Our methods are exact in the sense that they do not rely on a linearization of the Wasserstein space, and the components are true geodesics that minimize the cost in equation 1." This is a reasonable and well-defined usage. The harsh critic's complaint conflates "exact objective" with "global optimality," which the paper does not claim.

2. **"Pathological example (Figure 4) undermines the paper's own motivation."** — The paper honestly reports a case where GPCA behaves differently from TPCA and describes this as "worse-behaved." This is a valid finding, not a flaw. The paper does not claim GPCA is universally superior to TPCA; it transparently documents a limitation and the conditions under which it arises. Full credit for intellectual honesty.

3. **"Missing comparison to Seguy & Cuturi (2015)."** — Removed per rules (do not mention missing related works, as you lack external sources to confirm their relevance).

4. **"Missing appendix content / reproducibility details."** — The appendix is stripped by the parser; the paper explicitly states hyperparameters and details are in Appendix E. Criticizing their absence from the parsed version is invalid.

5. **"The paper's central empirical claim is unsubstantiated."** — This was kept and reformulated as a Major weakness above (quantitative evaluation missing). The Gaussian experiments *do* provide quantitative comparison, so the "central claim" framing was too broad.

6. **Strength Finder's "pathological case" strength.** — Removed because it conflicts with the paper's own characterization of the finding as potentially "worse-behaved."

7. **Strength Finder's generic strengths** — Removed generic statements about problem importance that lacked specific evidence.

## Nice-to-Haves

- A quantitative comparison framework for GPCAGEN vs. TPCA could be constructed by sampling from learned geodesics and computing Sinkhorn divergences between projected distributions and original data, even if the two methods operate on different representations (continuous vs. discrete).
- Sensitivity analysis for $\lambda_I$, $\lambda_O$ on a controlled synthetic dataset would strengthen confidence in the constraint enforcement.
- An ablation study of the intersection constraint (the stronger Diff($\Omega$) version vs. a softer Prob($\Omega$) version) would clarify whether the current design over-constrains the problem.
- Reporting projection residuals explicitly (sum in Equation 1) for each dataset would directly validate that GPCAGEN solves its stated objective.

## Novel Insights

None beyond the paper's own contributions. The reviews do surface that the paper's honest reporting of GPCA's limitations (the pathological example where GPCA is "worse-behaved" than TPCA) is actually a novel form of evidence — it delineates the regime where the method is and is not advantageous, which is more informative than a paper that only shows favorable cases. The reviewers do not add new technical insights beyond what the authors already provide.

## Suggestions

1. **Add quantitative evaluation for GPCAGEN.** Compute the sum of squared projection residuals (Equation 1) for the learned components and compare to the TPCA approximation (e.g., by approximating continuous distributions as fine-grained discrete measures for TPCA, or by comparing Sinkhorn divergences). Even an approximate numerical comparison would be far more informative than purely qualitative results.

2. **Report final constraint values.** After training the second component, report $\mathcal{I}$ and $\mathcal{O}$ to verify that the intersection and orthogonality constraints are satisfied.

3. **Describe the Gaussian GPCA optimization explicitly.** State how $SO(d)$ rotation variables are handled (Riemannian optimization? Parameterization via axis-angle? Alternating minimization?) and how the clipping operator affects gradient computation.

4. **Add a sensitivity study for $\lambda_I$, $\lambda_O$.** At minimum, show results on the MNIST synthetic experiment with varying regularization strengths.

## Score and Decision

**Calibration details.** Round 1 bracketing: weak anchors (avg 3.0) were clear rejects; strong anchors (avg 7.6–8.0) were top-tier papers. The paper sits in the middle band. Round 2 anchoring: the closest comparables are *Wasserstein Flow Matching* (6.33, Reject), which had a similar structure (Wasserstein geometry + neural nets) but was rejected for insufficient experimental validation on general measures; *Probabilistic Geometric PCA* (7.33, Accept), which had quantitative experiments; and *What Secrets Do Your Manifolds Hold?* (6.50, Accept), which had broad (though qualitative) experiments. Our paper has stronger theoretical contributions than WFM but weaker experimental validation than PGPCA or "What Secrets." The critical gap — purely qualitative evaluation of the general-case method — is the deciding factor.

**Score:** 5.5. The theoretical framework is elegant and the Gaussian GPCA derivation is a genuine contribution. However, the GPCAGEN experiments lack any quantitative validation, which is a decisive weakness for a method paper. The comparison to TPCA on real data is explicitly declined, leaving the central claim unsubstantiated.

**Decision:** Reject. The paper needs substantial additional experimental work (quantitative metrics for GPCAGEN, constraint validation, sensitivity analysis, optimization details) before it can be accepted.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>