Now I have a thorough understanding of the paper and can cross-check every claim. Let me produce the final consolidated review.

---

## Summary

This paper proposes UCB-C and UCB-D, constrained Bayesian optimization algorithms with provable no-regret guarantees. UCB-C handles the coupled setting (all functions evaluated at the same input), while UCB-D extends to the decoupled setting where the objective function and constraints can be evaluated independently at different inputs. The key technical innovation is a self-tuning "horizontal exploration" mechanism that adaptively decides whether to query the objective or a constraint by tying the constraint-relaxation parameter to the vertical exploration bonus. The paper provides theoretical regret bounds (Theorem 3.3), connects the function-query selection to uncertainty sampling in active learning, and evaluates the methods on synthetic and real-world optimization problems.

## Strengths

1. **First provable no-regret guarantee for decoupled constrained BO.** Theorem 3.3 bounds the cumulative regret of UCB-D sublinearly (via max-information gain γ_{h,T}) for commonly used kernels. Prior theoretical work (Lu & Paulson 2022, Xu et al. 2023) only covered the coupled setting. This is a genuine theoretical contribution.

2. **Clean regret definition that avoids penalty parameters.** The instantaneous regret is defined as a max over function-specific regrets (Eq. 3), and the analysis requires no tunable penalty parameter — unlike Lu & Paulson (2022), which leaves automated penalty tuning as future work. This is a meaningful simplification.

3. **Self-tuning horizontal exploration mechanism.** The constraint-relaxation parameter ν_t is automatically set to 2β_t^{1/2}σ_{f,t-1}(x_t), tying the decision of which function to query to the current uncertainty about the objective. The feedback intuition (Section 3.2) is clearly explained, and the mechanism resolves the dilemma of excessive constraint vs. objective queries without manual tuning.

4. **Principled connection to active learning / uncertainty sampling.** Section 3.3 shows that the function-query selection in UCB-D can be framed as uncertainty sampling (Eq. 18), and that the "uncertainty" being reduced is epistemic (resolvable with more data) rather than aleatoric. This yields a natural cost-aware extension (Remark 3.4).

5. **Theoretically grounded estimator for the optimal solution.** Lemma 3.5 provides a sublinear bound on the sum of instantaneous regrets at the recommended design point x̃_t*, directly connecting the suggested solution to the algorithm's theoretical performance.

6. **Empirical evaluation on diverse problems.** Three synthetic problems (with varying numbers of active constraints at the optimum) and three real-world problems (gas compressor design, CNN hyperparameter tuning, quantum chip design) provide a reasonable breadth of evaluation, with visualizations of query allocation that corroborate the algorithm's intended behavior.

## Weaknesses

### Fatal
None.

### Major

1. **Finite-domain theory vs. continuous-domain experiments.** The theoretical analysis (Section 3) explicitly assumes a *finite* input domain 𝒳, which is essential for the union bound in Lemma 3.1. Yet every experiment uses continuous domains (2D synthetic, 4D, 5D, 11D real-world). The paper never discusses how the algorithm is applied in practice (e.g., via a continuous optimizer over the acquisition function) nor provides a discretization argument (as in Srinivas et al. 2010) showing how the regret bound carries over to continuous domains. This creates a gap between the theory and the evidence used to support it. The gap is common in BO papers and addressable (a discretization argument with a chosen grid density would suffice), but as presented, the theoretical guarantee does not transparently cover the experimental setting.

### Minor

2. **ADMMBO may have been configured suboptimally.** The paper notes that ADMMBO "requires tuning the number of evaluations of f and c at each BO iteration" and that it was run with a fixed budget of one evaluation per function per iteration, consistent with the other baselines. ADMMBO's native design may allow multiple evaluations per iteration, and constraining it to a single evaluation likely handicaps its performance. While the authors acknowledge this, the claim of superior performance over ADMMBO is weakened by this asymmetry.

3. **Uncertainty about "true" optimal values for real-world problems.** Regret computation requires f(x*) and the true feasible set. The paper explicitly states that ground-truth functions are created for [QChip] (393 simulation data points). For [Gas] and [CNN], the problems are adopted from prior work but it is not clarified whether the true optima are known or estimated. If they are estimates, the regret values themselves are approximations. This does not invalidate the results but the paper should clarify how regret is computed for these cases.

4. **No ablation on the key hyperparameter β_t.** The theoretical β_t (Lemma 3.1) depends on |𝒳|, which for continuous domains is not defined. In practice, some heuristic must be used, and the self-tuning ν_t is tied to β_t. A brief sensitivity study (e.g., scaling β_t by a constant factor) would strengthen confidence in the algorithm's robustness. Without it, one cannot assess how sensitive performance is to this choice.

5. **Statistical significance is limited to standard errors.** Results are shown with standard errors over 10 runs. Given the variability visible in some plots (e.g., Fig. 3c), paired significance tests or confidence intervals at the final iteration would strengthen the claims of superiority, particularly when comparing to the state-of-the-art CMES-IBO.

### Trivial

6. **The remark about equality constraints is slightly misleading.** The paper mentions that equality constraints can be transformed into two inequality constraints, but then says the baseline estimator "may be undefined" for equality constraints and notes they are not considered. Since the experiments involve only inequality constraints, this is a non-issue for the presented results; it should simply be stated as a scope limitation rather than raised as a potential problem.

## Nice-to-Haves

- **Additional plot against BO iterations.** Beyond the plots against total queries, an additional plot against BO iterations (rounds of algorithm decision) would help separate the benefit of decoupling (fewer queries per iteration) from the per-iteration decision quality. This would make the comparison with coupled baselines more interpretable.
- **Discretization discussion in the main text.** A paragraph (or a sentence in Section 3) noting that continuous domains can be handled via a standard discretization argument (as in Srinivas et al., 2010), with reference to the appendix, would resolve the theory-experiment tension cleanly.
- **Cost-aware extension experiment.** Remark 3.4 sketches a cost-aware variant. A brief experimental demonstration (even on one problem) would strengthen the practical appeal.
- **Synthetic experiments on a discrete grid.** Running UCB-D on a moderately fine discrete grid for the synthetic problems would directly align the experiments with the finite-domain theory, even as a supplementary figure.

## Removed Points

These points were raised by reviewers but are removed or downgraded after cross-checking against the paper:

- **"Unfair comparison with coupled baselines"** — The critic argues that comparing UCB-D against coupled methods (EIC, CMES-IBO) on total queries is biased because coupled methods use |ℱ| queries per iteration while UCB-D uses 1. This is not a structural flaw: the *entire point* of decoupling is to be more query-efficient by not wasting evaluations on unnecessary functions. Plotting against total queries is the correct and standard way to demonstrate query efficiency. The paper's claim is that UCB-D is more query-efficient, which is appropriately evidenced by converging faster in terms of total queries. The suggestion to also plot against iterations is a nice-to-have, not a weakness. **Moved to Nice-to-Haves.**

- **"PESC complexity claim is subjective"** — The paper's statement that PESC is "fairly complex, making it less accessible" is an opinion, not a factual claim requiring evidence. This is not a weakness.

- **"Regret definition could affect intuition"** — The critic notes that the max-type regret (Eq. 3) treats a small constraint violation the same as a large one. The paper acknowledges this and provides the sum regret s(x) as an alternative (Remark 2.1), showing they are equivalent up to a constant factor. This is adequately addressed and not a weakness.

- **"The estimator may be undefined for equality constraints"** — The paper explicitly states that equality constraints are not considered in the experiments. This is a scope clarification, not a gap. The critic's concern about a "logical gap" is based on a misreading: the paper mentions this as a limitation of the *baseline* estimator, not of UCB-D.

## Novel Insights

The most incisive observation from the reviews is that the paper's theoretical guarantee (finite-domain) and experimental evaluation (continuous-domain) operate under different assumptions without a bridging argument. This is a real gap, but it is the standard gap present in most GP-UCB-style analyses (including Srinivas et al. 2010, which the paper builds on). The paper would be strengthened by explicitly adopting the discretization framework from Srinivas et al. and noting how the regret bound degrades with grid fineness. Beyond this, no genuinely novel insight emerges from the reviews that is not already contained in the paper's own contributions.

## Suggestions

1. Add a discretization argument to the main text (or a clear forward-reference to the appendix) that bridges the finite-domain theory and continuous-domain experiments, following Srinivas et al. (2010).
2. Clarify how the "true" optimal values are determined for the [Gas] and [CNN] benchmarks, and whether the regret values are exact or approximate.
3. Run ADMMBO with its native multi-evaluation-per-iteration configuration as a supplementary comparison, or explicitly state that the reported comparison uses the fixed-budget configuration and discuss how this may affect results.
4. Add a brief hyperparameter sensitivity study for β_t (e.g., scaling by 0.5× and 2×) on at least one synthetic problem.
5. Include statistical significance tests (e.g., Mann-Whitney U or paired t-test at the final iteration) comparing UCB-D against the best baseline.

## Score and Decision

The paper makes a solid theoretical contribution (first no-regret bound for decoupled constrained BO) and couples it with a clean algorithmic design. The main weakness — the finite-domain theory / continuous-domain experiment gap — is real but standard and fixable. No weakness is fatal. The experimental comparison is appropriate for demonstrating query efficiency (the core claim), and the missing ablations and clarifications are addressable. The paper merits acceptance after addressing the finite-domain/continuous-domain gap and the minor experimental clarifications.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>