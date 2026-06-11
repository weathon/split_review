Here is the final consolidated review:

---

## Summary

This paper introduces Constrained Mass Transport (CMT), a variational framework that constructs annealing paths for sampling from unnormalized densities by imposing simultaneous constraints on both the KL divergence (trust-region) and entropy decay between successive intermediate distributions. The method derives closed-form optimal densities under these constraints and instantiates the framework with normalizing flows for molecular Boltzmann generators. Evaluation on molecular benchmarks including a new ELIL tetrapeptide (d=219) shows consistent improvements over existing annealing-based methods (FAB, TA-BG), particularly on larger systems.

## Strengths

1. **Well-motivated combination of two constraints with compelling ablation evidence.** The ablation study (Figures 2-3) cleanly isolates the contribution of each constraint on alanine hexapeptide, showing that the trust-region constraint maintains overlap between successive densities (high ESS between intermediates) while the entropy constraint prevents mode collapse, and only the combined variant achieves both objectives. This directly validates the paper's central design claim.

2. **Consistent empirical gains on the largest systems with statistical support.** On ELIL tetrapeptide (d=219), CMT achieves ESS of 26.06% vs. TA-BG's 13.75% (1.90×) and FAB's 7.21% (3.61×) with non-overlapping standard errors across independent runs. On alanine hexapeptide (d=180), CMT achieves ESS of 29.63% vs. TA-BG's 18.22% (1.63×) and FAB's 14.55% (2.04×). These improvements use the same or fewer target evaluations, which is practically important for expensive energy evaluations.

3. **Negligible computational overhead from dual optimization.** The Lagrangian multiplier optimization accounts for only ~0.01% of training time (stated for alanine dipeptide), meaning the improved sample quality comes at essentially no additional computational cost.

4. **Introduction of the ELIL tetrapeptide benchmark (d=219).** This is a useful contribution to the community as a challenging benchmark for variational sampling, with more complex side-chain interactions than existing benchmarks.

## Weaknesses

### Fatal

None.

### Major

1. **Exponent error in Propositions 2.1 and 2.3.** The Lagrangian (3) is $\mathcal{L} = D_{\text{KL}}(q\|p) + \lambda(D_{\text{KL}}(q\|q_i) - \varepsilon_u)$. Solving this variational problem (calculus of variations on (3) with normalization constraint $\int q = 1$) yields $q_{i+1}(x) \propto \tilde{p}(x)^{1/(1+\lambda)} \, q_i(x)^{\lambda/(1+\lambda)}$, but Proposition 2.1 states $q_{i+1} \propto q_i^{1/(1+\lambda)} \tilde{p}^{1/(1+\lambda)}$ — the exponent on $q_i$ is $\lambda/(1+\lambda)$, not $1/(1+\lambda)$. The same error carries to Proposition 2.3 (combined constraints), where the correct exponent on $q_i$ would be $\lambda/(1+\lambda+\eta)$ rather than $1/(1+\lambda+\eta)$. Notably, equation (16) — the Monte Carlo estimator for $\mathcal{Z}_{i+1}$ — uses the form $\mathbb{E}[(\tilde{p}/q_i^{1+\eta})^{1/(1+\lambda+\eta)}]$, which is consistent with the *correct* derivation where the exponent on $q_i$ is $\lambda/(1+\lambda+\eta)$, *not* with the paper's own Proposition 2.3. This indicates an internal inconsistency: the implementation likely uses the right formula, but the theoretical characterization in the main text is wrong. Since the analytical solution is the paper's primary theoretical contribution, this error undermines the theoretical foundation. **Why it matters:** The closed-form solution is the paper's headline theoretical result. An incorrect derivation requires correction, and the paper must reconcile the propositions with the actual expressions used in the algorithm.

2. **Overclaimed and internally inconsistent ESS improvement.** The abstract and conclusion both claim "more than 2.5× higher effective sample size" while the results section says "approximately twice the ESS of competing approaches." Neither matches Table 1 cleanly. Against TA-BG (the strongest energy-based baseline), the maximum ratio is 1.90× (ELIL); on hexapeptide it is 1.63×. Against FAB, the ratios are 2.04× (hexapeptide) and 3.61× (ELIL). The "2.5×" figure is not attributable to any specific comparison in the table. This factual inconsistency between sections is a credibility problem.

### Minor

3. **RAM TV claim is overstated on ELIL.** The results section states CMT "provides superior mode coverage and resolution of metastable high-energy regions (RAM TV)" as a general claim, but on ELIL tetrapeptide, TA-BG achieves RAM TV = 2.54×10⁻² vs. CMT's 3.13×10⁻² — CMT is clearly worse on this metric for the largest system. While CMT is best on 3 of 4 systems, this blanket claim should be qualified.

4. **Unaddressed EUBO anomaly on ELIL.** CMT (trained without any MD samples) achieves EUBO = -277.83, outperforming Forward KL (trained on MD samples) at -276.76. Since EUBO corresponds to forward KL (up to an additive constant), the method trained to minimize forward KL on MD data should in principle be optimal. This surprising result requires explanation — it could indicate suboptimal MD training, limitations of the flow family, or a subtlety in EUBO computation — but the paper does not discuss it.

5. **Finite termination claim lacks justification.** Theorem 2.4 states there exists $I$ such that $q_I = p$, but this finite-termination property of a KL-constrained iterative process is not obvious and depends on the schedule of $\varepsilon$ values. No proof sketch or reference is provided.

### Trivial

6. The results section states CMT "provides superior mode coverage ... (RAM TV)" — on alanine dipeptide the RAM TV improvement is marginal (9.43×10⁻³ vs. TA-BG's 1.24×10⁻², with overlapping scales).

## Nice-to-Haves
- A discussion of hyperparameter sensitivity ($\varepsilon_{\text{tr}}, \varepsilon_{\text{ent}}$) in the main text rather than deferred entirely to the appendix.
- Clarification on how the number of annealing steps $\tilde{T}$ was chosen and how performance varies with it.
- Discussion of why the Forward KL baseline's substantially higher compute budget (4.2×10⁹ target evaluations on larger systems) does not translate to better EUBO on ELIL.

## Removed Points
- **"Tempered-only induces collapse"** (from harsh critic): The paper already discusses this — both constraints are needed, and the tempered-only variant avoids visible mode collapse in Figure 3 despite lower ESS. The asymmetry between constraints is part of the paper's stated finding.
- **Strength Finder generic strengths** (e.g., "the paper addresses an important problem"): Removed as superficial.
- **Missing related works**: Removed per rules — no external sources to verify.
- **Speculative criticisms about method soundness without concrete anchor in the paper**: Removed per filtering discipline.
- **Formatting/style nitpicks and requests for appendix details**: Removed as parser artifacts or standard deferrals.

## Novel Insights

The reviewer identified an internal inconsistency in the paper between the claimed exponents in Propositions 2.1/2.3 and the Monte Carlo estimator in equation (16). Equation (16) matches the correct derivation (where the exponent on $q_i$ is $\lambda/(1+\lambda+\eta)$), while the propositions claim $1/(1+\lambda+\eta)$. This suggests the practical algorithm uses the correct formula but the theoretical characterization in the main text is wrong — a useful finding that the authors should address. Beyond this, no novel insight emerges beyond the paper's own contributions.

## Suggestions

1. **Correct the exponents** in Propositions 2.1 and 2.3 to $\lambda/(1+\lambda)$ and $\lambda/(1+\lambda+\eta)$ respectively, and verify all downstream expressions (importance weights, dual functions) are consistent throughout the paper.
2. **Align ESS claims in abstract/conclusion** with Table 1 — either report specific comparison baselines or use a more conservative statement (e.g., "up to 1.9× over the strongest energy-based baseline, and up to 3.6× over FAB").
3. **Discuss the EUBO anomaly** on ELIL where CMT beats Forward KL training — this surprising result needs explanation.
4. **Qualify the RAM TV claim** to acknowledge TA-BG's superior performance on this metric for ELIL.
5. **Provide justification or a reference** for the finite-iteration convergence claim.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>