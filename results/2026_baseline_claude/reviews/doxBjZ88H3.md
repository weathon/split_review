Now I have a comprehensive understanding of the paper. Let me write the review.

---

## Summary

This paper introduces an information-theoretic framework for designing neural recording experiments to distinguish between two competing hypotheses about how uncertainty is encoded in early sensory populations: likelihood coding (probabilistic population codes, PPC) and posterior coding (neural sampling codes, NSC). The central contribution is the **information gap** Δ^info — analytically derived as the expected KL divergence between the true posterior and a "task-marginalized surrogate posterior" — which quantifies how distinguishable the two hypotheses are under a given stimulus distribution design. The authors validate that the information gap accurately predicts empirical decoder performance differences in simulations, demonstrate that maximizing the gap yields interpretable optimal experimental designs, and confirm via the Allen Brain Observatory Neuropixels dataset that conventional single-context designs yield zero distinguishing power.

---

## Strengths

- **Genuine theoretical contribution.** The derivation of Δ_L^info (Eq. 1–2) and Δ_P^info (Eqs. 3–5) as KL divergences between true posteriors and task-marginalized surrogate posteriors is non-trivial and elegant. In particular, the fixed-point equation (Eq. 5) for the Bayes-optimal likelihood estimator applied to a posterior-coding population is a non-obvious result, and the derivation of the constraint (Eq. 4) characterizing which observation pairs contribute to Δ_P^info is insightful.

- **Thorough empirical validation.** The paper validates the information gap against DNN-decoder empirical performance differences across two neural models (Poisson + Gaussian tuning, gain-modulated Poisson), three contrast levels, and >10 parameter settings each, finding tight agreement with the y = x diagonal (Fig. 4). Convergence with number of trials and neurons (Fig. 3) is carefully analyzed with multiple random seeds.

- **Concrete, actionable experimental guidance.** The 2D information gap landscape over context prior separation d and standard deviation σ (Fig. 5) provides experimenters with directly usable "sweet spots" (e.g., low contrast: d ≈ 30°, σ ≈ 20°), transforming the design problem from heuristic guessing to principled optimization.

- **Real-data validation of null result.** Applying the framework to 169 sessions of Allen Brain Observatory Neuropixels data — a single-context, uniform-prior design — yields a decoder performance difference of 0.0024 ± 0.064 (p = 0.63), exactly matching the theoretical prediction of Δ^info = 0. This convincingly confirms that current experimental designs cannot adjudicate between the two hypotheses and motivates the framework.

- **Non-Gaussian prior analysis.** The finding that heavy-tailed priors (Student's t, Cauchy) yield near-zero Δ_P^info throughout parameter space — because almost no observation pairs satisfy the constraint in Eq. 4 — is a practically important negative result, ruling out a class of seemingly reasonable experimental designs.

- **Important asymmetry revealed.** The order-of-magnitude difference between Δ_L^info and Δ_P^info (likelihood populations are more easily discriminated than posterior populations) is a genuinely non-trivial insight with immediate practical implications for power analysis and experimental design.

---

## Weaknesses

### Fatal
None.

### Major

1. **Continuous-observation regime not adequately addressed.** The entire framework, particularly Δ_P^info, is defined over a discrete observation space {x_i}. The constraint (Eq. 4) — that p^A(θ)·p(x_j|θ) ∝ p^B(θ)·p(x_k|θ) for all θ — selects specific observation pairs (x_j, x_k) that produce identical posteriors under the two contexts. In a continuous observation domain, this condition holds on a set of measure zero, making Δ_P^info = 0 identically. While this is implicitly handled by the discretization used in simulations, the paper does not explicitly acknowledge this issue, does not discuss the effect of bin size on the computed information gap, and does not provide guidance for experimentalists who must discretize continuous stimulus variables in practice. The robustness of the information gap estimates to discretization resolution is not evaluated.

2. **Practical trial-count requirements not quantified.** The framework provides an ideal-observer upper bound. In Fig. 3, convergence is shown up to 500 trials and 500 neurons, but real electrophysiology experiments typically have far fewer (30–100 trials per condition, 100–300 neurons). The paper shows that DNN decoders converge toward the theoretical information gap, but does not characterize whether the "sweet spots" identified in Fig. 5 remain statistically identifiable at realistic experimental scale (e.g., 50 trials/condition). Without this characterization, experimentalists cannot use the framework to design adequately powered experiments.

3. **The framework requires accurate prior knowledge of the generative model.** Computing the information gap requires specifying p(x|θ), p^A(θ), p^B(θ), and the neural population model a priori. In practice, the generative model must be estimated from preliminary data, introducing uncertainty. While the paper mentions incorporating biased priors (Appendix A.4), it does not analyze how misspecification of p(x|θ) or tuning curve parameters affects the accuracy of the information gap or the optimality of the resulting experimental designs. This is a non-trivial concern for practical deployment.

### Minor

1. **Two-context design only.** The framework is developed for exactly two contexts c ∈ {A, B}. Multi-context designs (K > 2) are natural extensions — for instance, using multiple priors to trace out a fuller discrimination curve — but are not analyzed. The benefit of additional contexts for Δ_P^info (which suffers from sparsity of qualifying pairs) might be substantial.

2. **Asymmetry implications under-analyzed.** The order-of-magnitude difference between Δ_L^info and Δ_P^info is mentioned but not fully explored. In particular, if the true neural code is posterior coding, the expected effect size is very small; this has direct implications for the statistical tests one would use to adjudicate between the hypotheses in a real experiment, which is not addressed.

### Trivial
None worth noting.

---

## Nice-to-Haves

- A figure showing the effect of bin size on Δ_P^info (addressing the discretization concern) would strengthen confidence in the framework's continuous-space applicability.
- A worked example with approximate realistic trial counts (e.g., N = 50 trials, 150 neurons) and the expected statistical power to detect the information gap at the identified "sweet spots" would make the framework directly usable by experimentalists.

---

## Novel Insights

The most genuinely novel insight is the construction and characterization of the **task-marginalized surrogate posterior**: the fact that a Bayes-optimal posterior decoder applied to a likelihood-coding population can do no better than marginalize over context priors (Eq. 2), and conversely that a Bayes-optimal likelihood decoder on a posterior-coding population is constrained to a fixed-point implicit equation (Eq. 5) restricted to isoposterior observation pairs (Eq. 4). The emergent consequence — that the information gap for posterior coding is sparse by construction, making posterior populations intrinsically harder to distinguish and requiring specifically engineered prior configurations — is a non-trivial theoretical result that could guide broader thinking about experimental separability in probabilistic neuroscience. The revelation that heavy-tailed priors yield near-zero Δ_P^info (because the sparsity of qualifying pairs is compounded by heavy-tail geometry) is an unexpected corollary of this analysis.

---

## Suggestions

- Analyze the robustness of information gap estimates to discretization bin size and provide guidelines for choosing resolution when applying the framework to continuous observations.
- Provide a power analysis relating information gap magnitude to the number of trials and neurons needed to achieve statistical significance in a realistic experiment.
- Analyze sensitivity of the optimal design to misspecification of the generative model parameters (e.g., tuning width, noise level), even briefly.
- Consider extending the visualization in Fig. 5 to include at least a three-context design to illustrate whether adding contexts helps recover Δ_P^info sensitivity.

---

## Score and Decision

The paper addresses a fundamental question in computational neuroscience with a technically sound and novel theoretical framework. The derivations are clean, the empirical validation is thorough, the real-data null result is compelling, and the practical guidance (information gap landscape, "sweet spots") is directly actionable. The major concerns — treatment of the continuous-observation case, practical power analysis, and sensitivity to model misspecification — are real gaps that should be addressed but do not invalidate the core theoretical contribution. This is a solid, well-scoped contribution that advances the field meaningfully.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>