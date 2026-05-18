Now I have a thorough understanding of the paper and all the review claims. Let me produce the final consolidated review.

## Summary

This paper presents a method for inverse decision-making — Bayesian inference over the parameters of Bayesian actor models. The key idea is to amortize the forward computation of optimal actions using a neural network trained in an unsupervised fashion (using the cost function itself as the training objective), then leverage the network's differentiability for efficient gradient-based Bayesian inference (NUTS) of the actor's parameters from behavioral data. The method is validated on synthetic data (matching analytical posteriors for quadratic costs, recovering ground truth for non-analytical costs), used to investigate identifiability between prior and cost parameters, and demonstrated on human data from a bean-bag throwing task.

## Strengths

- **Unsupervised amortization eliminates expensive numerical optimization.** The neural network is trained using the cost function as a stochastic objective with reparameterized Monte Carlo sampling (Section 3.1.1), requiring no precomputed optimal actions. Training takes 10 minutes on a standard laptop (Section 3.3), which is a significant efficiency gain over the supervised approach of Neupertl et al. (2021).

- **Efficient gradient-based inference at scale.** Because the neural network is differentiable w.r.t. all model parameters and the sensory input, the method draws 20,000 NUTS posterior samples in 10 seconds for a 60-trial dataset (Section 3.3). This would be orders of magnitude slower without amortization, as each likelihood evaluation would require solving a complete decision-making problem numerically.

- **Posterior recovery matches the analytical gold standard.** For quadratic costs (where the optimal action has a closed form), posterior distributions obtained using the neural network are virtually indistinguishable from those using the analytical optimal action (Figure 2B). Mean squared errors to ground truth are nearly identical across 100 synthetic datasets (Figure 2C, Table 2), providing strong quantitative validation of the approximation.

- **Handles non-analytical cost functions accurately.** For the asymmetric quadratic cost (no known analytical solution), the method still recovers ground truth parameters (Figure 3E) and reveals the same identifiability pattern between prior and cost as in the analytically solvable case (Figure 3F).

- **Enables systematic identifiability analysis.** The method makes it feasible to investigate confounds between prior and cost parameters in Bayesian actor models (Figure 3B–F), demonstrating, for example, the strong posterior correlation between prior mean μ₀ and effort cost β, and showing that fixing one resolves the confound. This type of analysis would be difficult without an efficient forward and inverse solver.

## Weaknesses

### Fatal

None.

### Major

- **The handling of the latent sensory measurement m during inference is underspecified.** The paper's generative model (Figure 1B) includes an unobserved sensory measurement m per trial. During inference of p(θ | D), the likelihood p(r | s, θ) requires marginalizing over m: ∫ p(r | a*(m, θ)) p(m | s, θ) dm. The paper states the neural network is "differentiable with respect to the parameters θ and sensory input m" and that NUTS is used, but never explicitly describes how the marginalization is accomplished — whether m is treated as a latent variable sampled jointly with θ during MCMC, or whether some other approximation is used. While the empirical match to the analytical posterior (Figure 2) strongly suggests the implementation is correct, the omission undermines reproducibility and pedagogical clarity. This is the most important issue to address in revision.

- **Limited human data analysis.** The paper states that 20 participants performed the bean-bag throwing task, yet only 2 participants' data are analyzed and shown (Figure 4). The abstract's claim that the method "explains systematic individual differences" is weakly supported by this sample. While a methods paper does not need a full-scale empirical study, including a brief summary of posteriors across all 20 participants (e.g., a figure of posterior means or a table of R-hat values) would substantially strengthen the real-data demonstration.

### Minor

- **No direct wall-clock or accuracy comparison against non-amortized baselines.** The paper demonstrates that the NN-based posteriors match analytical ones (where available), but does not provide a direct comparison to a standard alternative inference procedure (e.g., a Metropolis-Hastings sampler that numerically solves the decision problem at each likelihood evaluation). Showing that amortization reduces inference time from hours to seconds would make the computational contribution more concrete. The paper already compares posterior shapes; adding a runtime comparison would be straightforward and valuable.

- **The analytical-vs-NN comparison could be misinterpreted.** The paper repeatedly says "using the analytical solution for the optimal action" vs "using the neural network" to compute a*, but a reader could mistakenly think the comparison is against a fully analytical posterior (which does not exist for this model). Clarifying that both approaches use the same NUTS inference procedure and differ only in how a* is computed (closed-form formula vs neural network) would prevent confusion.

### Trivial

- None (the formatting issues are parser artifacts, not author errors).

## Nice-to-Haves

- A brief discussion of potential limitations of the softplus power-law output nonlinearity for cost functions with very different functional forms (e.g., logarithmic costs). The paper touches on this in the Limitations paragraph but could warn users more explicitly.
- An explicit mention in the main text of the prior families and hyperparameters used during training and inference (currently deferred to appendix).
- Expanding the human data analysis to more than 2 of the 20 available participants.

## Removed Points

- **"Analytical marginal likelihood derivation is missing"** — The critic claims the paper must derive a closed-form marginal p(r | s, θ) for the analytical comparison. This misreads the paper: the analytical solution is for the *optimal action* a*(m, θ) (equation after line 184), not for the full marginal likelihood. The comparison is between posteriors obtained using the analytical a* vs the NN a*, both using the same inference procedure. The derivation exists in the appendix (app:derivation-quadratic) which was stripped by the parser.
- **"Prior distributions only mentioned in appendix"** — The paper references app:param-priors; this is standard practice and the appendix was stripped by the parser.
- **"Inductive bias may not generalize"** — The paper itself acknowledges the architecture choice and its limitations. This is a known design consideration, not a hidden flaw.
- **"Identifiability finding is not novel"** — The paper does not claim the finding itself is novel; the value is demonstrating that the amortized method reproduces the same confound as the analytical solution, validating the approximation. This is a legitimate strength, not a weakness.
- **"Missing comparison to grid-based approach"** — This is a nice-to-have suggestion, not a core weakness. The paper already validates against the strongest possible baseline (the analytical solution).

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel observation about the work that the paper itself does not already make.

## Suggestions

1. **Clarify the inference procedure.** Explicitly specify how the latent sensory measurement m is handled during NUTS sampling. If m is treated as a latent variable (one per trial, sampled jointly with θ), state this clearly. Provide the joint log-posterior or pseudo-code in the main text (beyond what is in the algorithm in the appendix). This is the single highest-leverage improvement.

2. **Add a runtime/accuracy comparison against a non-amortized baseline.** Even for a small problem, showing that inference takes hours without amortization vs seconds with it would make the computational contribution tangible.

3. **Expand the human data presentation.** Include a supplementary figure or table summarizing posteriors across all 20 participants (e.g., posterior means and credible intervals per participant). This would substantiate the claim about systematic individual differences without requiring a full re-analysis.

4. **Clarify the "analytical solution" comparison.** Add a sentence noting that both procedures use the same NUTS inference; only the computation of a* differs (analytical formula vs neural network).

## Score and Decision

This paper makes a solid contribution to the cognitive science / computational neuroscience community by providing a practical, amortized method for inverse decision-making that handles general parametric cost functions and produces full Bayesian posteriors efficiently. The synthetic validation is rigorous, the match to analytical solutions is convincing, and the identifiability analysis is a useful demonstration. The core technical approach is sound, and the computational gains are substantial.

The primary weakness is the underspecified treatment of the latent sensory measurement during inference — a genuine clarity gap, but one that can be resolved with an explicit description in the main text. The limited human data presentation is a secondary concern appropriate for a methods paper. Neither issue undermines the core contribution.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>