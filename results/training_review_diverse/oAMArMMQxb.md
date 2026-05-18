Now I have a thorough understanding of the paper and all the reviewer claims. Let me construct the final consolidated review.

## Summary

This paper proves that vanilla score matching *can* successfully sample multimodal distributions (mixtures of strongly log-concave components) when combined with two ingredients: (1) data-based initialization (initializing Langevin dynamics from the empirical distribution of training samples) and (2) early stopping (running the dynamics for a finite, carefully chosen time rather than to stationarity). Theorem 1 provides explicit bounds on the required running time, step size, number of samples, and score estimation accuracy needed to achieve a target total variation distance. The proof introduces a novel log-Sobolev bound for mixtures (Theorem 2) based on an overlap graph, and uses a careful case analysis separating high-overlap components (where LSI drives mixing) from low-overlap components (where the score is close to that of a single component). Simulations in 1D and 32D illustrate the predicted behavior.

## Strengths

- **First theoretical guarantee for vanilla score matching on multimodal distributions.** Theorem 1 proves that Langevin dynamics with data-based initialization and early stopping succeeds on mixtures of log-concave distributions, directly addressing the known failure mode of vanilla score matching (Koehler et al. 2022). The result is new even for the unimodal case (Remark after Theorem 1), improving over prior warm-start analyses that required exponentially many samples in high dimensions.

- **Novel log-Sobolev bound for mixtures (Theorem 2).** Establishes a bound on the LSI constant of a mixture in terms of the overlap graph's connectivity and the minimum component weight, using assumptions strictly milder than prior work (e.g., no bounded chi-square divergence requirement as in Chen 2021). The bound for more than two components is new, and the comparison to existing results (Schlichting 2019, Madras 2002) is clearly stated.

- **Clean proof architecture.** The high-level strategy — decompose components by overlap, apply LSI in high-overlap regimes and component-wise comparison in low-overlap regimes — is well-motivated and clearly described. The inductive argument over the sequence of overlap thresholds $\delta_r$ (reducing the number of connected components by at most one per iteration) is elegant.

- **Handling of realistic $L_2$-accurate score estimates.** The analysis extends from exact scores to $L_2$-approximate scores (Definition 1) via a "bad set" argument, ensuring the result applies when scores are learned from data. This connects the theory to practical usage.

- **Honest about limitations.** The paper explicitly acknowledges the exponential dependence on $K$ (Remark after Theorem 1), discusses it as an open question (Section 1.3: "it is an open question if the dependence on the number of components is optimal"), and clearly scopes the contribution.

## Weaknesses

### Fatal

None.

### Major

- **Exponential dependence on $K$ severely limits the regime of applicability.** Theorem 1's running time $T$ and step size $h$ scale as $\exp(K)$ with the number of mixture components, and the $\epsilon_{\text{score}}$ requirement inherits this dependence. This restricts the main result to $K = O(1)$. While the paper acknowledges this limitation, the title and abstract discuss "multimodal distributions" generally, and a reader might reasonably expect a result that handles many modes gracefully. The inductive argument over the overlap graph iterates at most $K$ times, but the constants compound multiplicatively through the recursion $\delta_{r+1} = \Theta((\alpha\delta_r)^{3/2}/(\beta R)^3)$, which drives the exponential blowup. The paper would be strengthened by a discussion of whether this dependence is an artifact of the proof technique or reflects a genuine barrier.

- **The score accuracy requirement is extremely stringent.** The bound $\epsilon_{\text{score}} \leq \tilde{\Theta}(p_*^{1/2} \epsilon_{TV}^4 / ((\beta \kappa^2 K e^K)^2 d^{3/2} T^{3/2}))$ involves very small constants and, through its dependence on $T$, inherits the exponential-in-$K$ factors. The paper references the connection to Rademacher complexity bounds from Koehler et al. (2022) as evidence that this is achievable, but does not work out an explicit example (e.g., a finite mixture of well-separated Gaussians) where the required sample complexity is polynomially bounded. Without such a concrete demonstration, a reader may question whether the theorem establishes feasibility or merely logical possibility.

### Minor

- **The compact support assumption in the proof sketch and its interaction with dimension dependence.** The sketch assumes the distribution is supported on a ball of radius $R$, with the claim that this is handled via concentration in the appendix. Since $R$ appears in the sketch's bounds (e.g., $\beta R$ terms) and the natural high-probability radius scales as $\sqrt{d/\alpha}$ for strongly log-concave components, it is not immediately clear whether the final $d$-dependence in Theorem 1 (where $d$ appears only linearly in the numerator of $h$) properly accounts for this substitution without introducing additional dimension factors. The commented-out text in the paper itself uses $R = \theta(\sqrt{d})$, suggesting the full proof does handle this, but the main text could clarify the final $d$-dependence that results from the concentration argument.

- **The proof sketch relies on several unquantified steps.** Phrases like "we can argue" and "with high probability" appear without specifying the failure probabilities or constants (e.g., the Girsanov bound used in the low-overlap case, or the explicit log-Sobolev bound from Theorem 4). While this is typical for a proof sketch with deferred details, the sketch could be tightened by stating a few key inequalities explicitly, particularly the bound that controls the probability of hitting the "bad set" $B_{\text{score}}$ and how this translates to the $\epsilon_{\text{score}}$ requirement. The paper states that all proofs are in the appendices, which is standard, but the sketch is the only content available to verify the architecture of the argument.

- **Minimal simulations.** The experiments consist of one 1D example (40 samples, two Gaussians) and one 32D example (15 samples, two Gaussians). While they illustrate the phenomenon, they do not probe the theory's predictions about dependence on $K$, $d$, $\kappa$, or the required $\epsilon_{\text{score}}$. The 32D example uses only 15 samples for initialization — this is too small to convincingly demonstrate that the empirical distribution captures the correct component weights. An ablation varying $K$ or the number of samples would strengthen the empirical support.

### Trivial

None.

## Nice-to-Haves

- **Concrete example with explicit sample complexity.** Working out a simple parametric case (e.g., a balanced mixture of two isotropic Gaussians with known parameters) and computing the sample size $N$ needed to achieve the $\epsilon_{\text{score}}$ condition would ground the abstract bounds and help readers assess whether the result is practically meaningful.
- **Numerical comparison of predicted vs. observed optimal early-stopping time.** Showing that the theoretical $T$ from Theorem 1 is in the right ballpark for the simulated examples would strengthen the connection between theory and experiments.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that "the main text should bear more of the verification burden" because the appendix is not available for review.** This is a review-process artifact — the appendices exist in the original submission and are stripped by the parser. The paper clearly states "We leave complete proofs of all results to the appendices," which is standard practice.
- **Suggestion to move the two-Gaussian example to the introduction/discussion.** This is a presentational preference, not a weakness. The example already appears in a Remark within the proof sketch, which is a reasonable placement.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an unexpected implication or connection that the paper itself does not already identify.

## Suggestions

- Add a brief discussion in Section 2 or after Theorem 1 clarifying how the compact-support-to-concentration step affects the final $d$-dependence, showing that the linear-in-$d$ dependence in Theorem 1 is what results from the full proof.
- State explicitly whether the $\exp(K)$ dependence is known to be improvable or is conjectured to be necessary, providing a sharper characterization of the open problem raised in Section 1.3.
- Expand the simulations to include at least one experiment varying $K$ (e.g., $K=1,2,3,4$) in a low-dimensional setting to demonstrate that the method works for multiple components, and one experiment varying the number of initialization samples to verify the $M$ dependence.
- In the proof sketch, replace one or two of the "we can argue" steps with explicit inequality statements (even with placeholder constants) to make the logical flow more self-contained.

## Score and Decision

This paper makes a genuine theoretical contribution — it provides the first rigorous guarantee that vanilla score matching, when equipped with data-based initialization and early stopping, can successfully sample from multimodal distributions. The technical machinery (the log-Sobolev bound for mixtures via overlap graphs, the inductive argument over decreasing overlap thresholds, the Girsanov-based comparison for $L_2$-approximate scores) is novel and significant. The paper is transparent about its limitations, particularly the exponential dependence on $K$, and identifies concrete open problems.

The main weaknesses — the $\exp(K)$ dependence restricting the result to $K=O(1)$ and the stringent $\epsilon_{\text{score}}$ requirement — are real but do not invalidate the core contribution. The paper delivers on its central claim: it proves that the approach works, establishes the first such guarantee, and provides a reusable analytical framework. The simulations, while minimal, are consistent with the theory.

**Score:** 7.5

**Decision:** Accept

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>