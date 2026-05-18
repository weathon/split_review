Here is my final consolidated review.

---

## Summary

This paper introduces a method for inverse decision-making that amortizes Bayesian actor models using neural networks trained in an unsupervised fashion directly from the cost function. The pre-trained neural network serves as a fast, differentiable stand-in for the optimal action computation, enabling efficient gradient-based Bayesian inference (NUTS) of perceptual, motor, and cost parameters from continuous behavioral data. The method is validated against analytical solutions where they exist, used to investigate identifiability between priors and costs, and applied to real human throwing data.

## Strengths

- **Unsupervised training eliminates the need for expensive numerical solutions.** The neural network is trained on the cost function directly via a reparameterized stochastic objective (Section 4.1.1), without requiring pre-computed optimal actions — a clear advance over the supervised approach of Neupärtl et al. (2021) that required numerical optimization for each training example.

- **Efficient gradient-based Bayesian inference.** By providing a differentiable approximation of the Bayesian actor, the method enables Hamiltonian Monte Carlo (NUTS) to draw 20,000 posterior samples in 10 seconds for a 60-trial dataset on a standard laptop (Section 4.3). This is orders of magnitude faster than approaches requiring a numerical solve per likelihood evaluation.

- **Validation against analytical gold standards for two of three cost functions.** For the quadratic cost (Section 5.2), the neural-network-based posteriors closely match the analytical solution on shape, mean recovery, and MSE over 100 simulated datasets (Figure 2B–C). For the quadratic cost with quadratic effort (Section 5.3), the paper derives an analytical solution and shows that the neural-network posteriors match it, including 94% HDI contours (Figure 3B). These comparisons provide strong evidence that the method works correctly when verification is possible.

- **Systematic investigation of identifiability between priors and costs.** The method reveals that prior mean \(\mu_0\) and effort cost \(\beta\) are correlated in the posterior, and demonstrates that fixing one parameter substantially improves inference of the other (Section 5.3, Figure 3C,F). This analysis is a novel and useful contribution enabled by the amortized approach.

- **Application to real human data.** Applied to a bean-bag throwing experiment (Willey & Liu, 2018), the method recovers cost functions that capture systematic undershooting in one participant and unbiased behavior with higher variability in another (Section 5.4, Figure 4), demonstrating practical utility.

## Weaknesses

### Fatal
None.

### Major

- **Posterior calibration not assessed for the asymmetric quadratic cost function — the only case without an analytical solution.** The paper validates against analytical solutions for the quadratic cost (Section 5.2) and the quadratic-with-effort cost (Section 5.3, Figure 3B). For the asymmetric quadratic cost, no analytical solution is known, and the validation rests entirely on MSE between posterior mean and ground truth across 100 datasets (Figure 3E–F). MSE of the posterior mean is a point-estimation diagnostic; it does not assess whether the posterior width is well-calibrated. A Bayesian inference method should also report whether uncertainty quantification is reliable — for example, what fraction of ground-truth parameters fall within the 94% HDI. Without this, the reader cannot evaluate whether the method produces well-calibrated posteriors or merely accurate point estimates for this cost function. This is the most consequential gap in the paper's validation.

- **No quantitative comparison against existing inference methods.** The paper positions itself as overcoming limitations of previous bespoke tools and numerical methods, but provides no quantitative comparison against any alternative approach (e.g., Acerbi & Ma 2014's mixture-of-Gaussians framework, Neupärtl et al. 2021's supervised approach, or a likelihood-free method such as SNPE). For a methods paper, the absence of any baseline comparison makes it difficult to assess the claimed computational and statistical advantages relative to the existing toolbox. A single comparison — even a grid-based numerical approach on a small number of datasets — would substantially strengthen the contribution.

### Minor

- **Neural network approximation error not directly characterized for the asymmetric quadratic cost.** For the quadratic cost (and quadratic-with-effort, where an analytical solution was derived), the approximation quality is implicitly validated by the match to the analytical posteriors. For the asymmetric quadratic cost, the approximation error between the neural network's output and a brute-force numerical optimizer's solution is not reported. Characterizing this error (e.g., mean absolute error on a holdout grid) would strengthen confidence that the training objective yields a near-optimal policy for this case.

- **Convergence diagnostics for neural network training on non-analytical costs are referenced to the (stripped) appendix.** The main text states that convergence was assessed "using an evaluation set of analytically or numerically solved optimal actions" (line 128). For the non-analytical cost functions, it would be helpful to clarify in the main text how this evaluation set was generated, and what the accuracy of the numerical optimizer used to construct it was.

### Trivial
None.

## Nice-to-Haves

- **Coverage diagnostics for the asymmetric quadratic cost:** Reporting the empirical coverage of the 94% HDI for each parameter across the 100 simulated datasets would directly address the major calibration concern above.
- **A brief comparison to a simple baseline:** Even a single figure comparing recovery accuracy or computation time against a grid-based numerical inference approach for the asymmetric quadratic cost would significantly strengthen the paper's claims.
- **A remark on comparing across cost families:** The paper assumes the cost function form is known up to parameters. A brief discussion of how one might compare different cost families (e.g., via model comparison or posterior predictive checks) would be helpful for practitioners.

## Removed Points

- **"No analytical solution exists for quadratic-with-effort cost."** This is factually wrong. The paper explicitly states (lines 224–225): "we derived an analytical solution for the quadratic cost with quadratic effort" and validates the neural network against it, showing matching 94% HDI contours in Figure 3B. The critic's central claim about incomplete validation rests on this error and applies only to the asymmetric quadratic cost.
- **"No discussion of convergence diagnostics for neural network training."** The paper states (line 128) that convergence was assessed using an evaluation set, referenced to the appendix. The appendix was stripped by the parser; this is an infrastructure artifact, not an author omission.
- **"The method should be extended to circular stimuli / other domains."** The paper explicitly acknowledges this as a limitation in the Discussion (line 271) and suggests future work. This is scope-appropriate self-awareness, not a weakness.
- **"The paper does not address model comparison across cost families."** The critic acknowledges this "is appropriate for the scope." This is a nice-to-have, not a weakness.

## Novel Insights

Beyond the paper's own contributions, the reviews highlight a genuine tension in amortized inference for scientific models: the cost functions that most need the method (those without analytical solutions) are precisely the ones where validating the surrogate's accuracy is hardest, because no gold standard exists. The paper's validation strategy — showing the surrogate matches an analytical solution for a closely related cost function (quadratic-with-effort), then relying on MSE for the truly intractable case — is reasonable but incomplete. This points to a broader methodological question: what should constitute sufficient validation for amortized surrogates in scientific inference, where ground truth is often unavailable?

## Suggestions

1. **Add coverage diagnostics for the asymmetric quadratic cost.** For each of the 100 simulated datasets, compute whether the ground-truth parameter falls within the posterior 94% HDI and report the fraction across datasets. This directly addresses the most significant validation gap.
2. **Include at least one baseline comparison.** A simple grid-based numerical inference on a few datasets for the asymmetric quadratic cost would suffice to benchmark accuracy and speed against an alternative.
3. **Characterize the neural network approximation error directly for the asymmetric quadratic cost.** On a holdout grid of parameters and observations, compare the network's output to a high-quality numerical optimizer and report mean absolute error.
4. **Clarify in the main text how the evaluation set for convergence was generated for non-analytical cost functions** (i.e., what numerical optimizer was used, and with what accuracy).

## Score and Decision

The paper presents a clever and practically useful method that addresses a real bottleneck in behavioral modeling. The unsupervised training scheme, the validation against analytical solutions for two of three cost functions, the identifiability analysis, and the real-data application all constitute genuine contributions. The main weaknesses — incomplete calibration assessment for the asymmetric quadratic case and lack of baseline comparison — are real but addressable and do not invalidate the core contribution. The paper is clearly written, the method is well-motivated, and the software implementation (JAX-based, publicly usable) enhances reproducibility and impact.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>