- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6
Now I have a thorough understanding of the paper and both reviews. Let me construct the final consolidated review.

---

## Summary

This paper introduces a method that amortizes Bayesian actor models using neural networks trained *unsupervisedly* on the decision problem's cost function. Once trained, the differentiable neural network surrogate enables efficient gradient-based Bayesian inference (via NUTS/HMC) over interpretable model parameters — priors, perceptual/motor uncertainty, and cost parameters — from continuous behavioral data. The method is validated on synthetic data against analytical solutions (where available) and applied to human bean-bag throwing data.

## Strengths

- **Unsupervised training scheme for amortizing Bayesian decision-making (Sec. 4.1.1).** The network is trained using only the cost function as a stochastic objective with the reparameterization trick, requiring no precomputed optimal actions. This is a clear advance over the supervised approach of Neupertl et al. (2021), which required expensive numerical solutions per training example.

- **Efficient gradient-based inference.** Using the differentiable neural network as a stand-in for the optimal action enables NUTS sampling of 20,000 posterior samples in ~10 seconds for a 60-trial dataset on a laptop CPU (Sec. 4.3). This is a major computational improvement over methods that must solve the decision problem at each likelihood evaluation.

- **Quantitative validation against analytical solutions (Sec. 5.2, Fig. 2).** For quadratic costs, posteriors inferred via the neural network closely match those obtained with the exact analytical solution. The evaluation across 100 random parameter draws shows comparable MSEs for both approaches, establishing that the approximation does not meaningfully degrade inference quality.

- **Identifiability analysis of priors vs. costs (Sec. 5.3, Fig. 3).** The method reveals that prior mean μ₀ and effort cost β are strongly correlated in the posterior for the quadratic+effort cost function, and that this is a model property rather than an inference artifact (fixing one parameter substantially improves recovery of the other). This analysis would be difficult to conduct without the efficient inference the method provides.

- **Application to empirical human data (Sec. 5.4, Fig. 4).** The method is demonstrated on real bean-bag throwing data, producing interpretable posterior distributions that distinguish qualitatively different behavioral patterns (undershooter vs. accurate but variable) and yield visualizable cost functions in stimulus–response space.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Limited cost-function diversity in experiments.** All three tested cost functions are quadratic variants (symmetric quadratic, quadratic + quadratic effort, asymmetric quadratic). The paper claims the framework "allows for arbitrary parametric families of cost functions" (Sec. 2, Sec. 4), yet no qualitatively different cost family (e.g., hinge, log-cosh, piecewise linear, or asymmetric non-quadratic) is tested. While there is no fundamental barrier in the method's design, the empirical evidence for generality across cost families is narrower than the scope claimed.

- **Inductive bias in the network architecture.** The final layer uses `softplus(y₁·obs^{y₂} + y₃)`, explicitly motivated by the form of the quadratic analytical solution (Sec. 4.1.2). The paper references an appendix discussion, but the potential degradation for cost functions with very different functional forms (e.g., cost functions whose optimal actions are not a power-law of the observation) is not empirically assessed. This matters because users adopting the method for non-quadratic-like costs may need to redesign the architecture.

- **Real-data analysis is light.** Only two participants are analyzed (Sec. 5.4), and the evaluation is restricted to visual inspection of posterior distributions and posterior predictives. No quantitative model-fit assessment (e.g., posterior predictive p-values, coverage of posterior predictive intervals, comparison against a null or simpler model) is provided. This is acceptable for a methods demonstration but weakens the empirical claim relative to the analyses on synthetic data.

- **No timing comparison against alternatives.** The paper reports that inference takes ~10 seconds for 60 trials (Sec. 4.3), which is fast, but does not quantify the speedup relative to a baseline (e.g., MCMC with numerical optimization per likelihood evaluation). The efficiency advantage is asserted but not benchmarked.

- **Posterior coverage/calibration not checked.** The evaluation assesses MSE of the posterior mean (parameter recovery) but does not test whether the posterior credible intervals are well-calibrated (e.g., coverage rates on the 100 synthetic datasets). This would strengthen confidence that the neural network does not systematically over- or under-estimate uncertainty, especially for cost functions without an analytical check.

### Trivial
None.

## Nice-to-Haves

- A brief experiment with a single qualitatively different cost function (e.g., hinge or asymmetric non-quadratic) would substantially broaden the empirical support for the "arbitrary cost functions" claim.
- A calibration check (coverage of 94% HDI intervals on synthetic data) would be a simple addition that increases trust in the posterior uncertainty estimates.
- A timing comparison against a reasonable baseline (e.g., numerical optimization + MCMC) would make the efficiency claim concrete.

## Removed Points

These points from the inputs were flagged to be removed; treat them with caution:

- **From Strength Finder — "Log-normal perceptual-motor model grounded in psychophysics" (as a paper strength).** This describes the model setup's motivation rather than a strength of the proposed method itself. The method is evaluated using this model, but the strength of the paper is the inference method, not the psychophysical grounding of the specific model choice.
- **From Strength Finder — Generic/importance-based strengths.** General statements about the problem being "important" or the method having "broad applicability" are removed as generic per instructions.
- **From Harsh Critic — "Section 4.1.1" / "Section 4.3" / specific section numbering.** These are presentational labeling differences; the content referenced is correctly identified in the paper.

## Novel Insights

None beyond the paper's own contributions. The key observation that prior and cost parameters can be confounded in Bayesian actor models with non-trivial cost functions, and that this is a structural property rather than an inference artifact, is already the paper's own contribution (Sec. 5.3). The reviewers did not surface additional novel insights beyond what the paper itself provides.

## Suggestions

1. **Add one non-quadratic cost function** to the synthetic evaluation (e.g., a piecewise linear cost or hinge loss) to broaden the empirical support for the claim that the method handles arbitrary parametric cost functions.
2. **Report posterior coverage** for the synthetic recovery experiments (the fraction of ground-truth parameters falling within the 94% posterior credible interval) to validate uncertainty calibration.
3. **Include a timing baseline** — briefly compare inference runtime against a conceptually sensible alternative (e.g., grid-based numerical optimization + MCMC) to substantiate the efficiency claim.
4. **Discuss the architecture's inductive bias** more explicitly in the main text: under what cost function families would the current `softplus(y₁·obs^{y₂}+y₃)` final layer be a poor choice, and how should users modify it?

---
