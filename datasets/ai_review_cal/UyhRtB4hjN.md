- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 5, 6
Now I have all the information needed. Let me construct the final consolidated review.

## Summary

The paper proposes LLEGO, a genetic programming method for decision tree induction that uses LLM-based semantic priors to define fitness-guided crossover and diversity-guided mutation operators. The core idea is to represent trees in natural language and query an LLM to generate offspring conditioned on desired fitness (crossover) or inversely-weighted-by-likelihood candidates (mutation), with hyperparameters α and τ controlling exploration vs. exploitation. Empirical results across 12 classification/regression datasets show LLEGO outperforming greedy (CART, C4.5), exact optimal (GOSDT, DL8.5), and GP (GATree) baselines, with a systematic ablation study confirming each component's contribution.

## Strengths

- **Comprehensive empirical demonstration of superior generalization**: Tables 1 and 2 show LLEGO achieving the best balanced accuracy across 11 of 14 classification settings and lowest MSE across all 10 regression settings, against a diverse set of baselines spanning greedy, exact, and GP approaches. The advantage is more pronounced at depth 4, a substantially larger search space — exactly where the method claims to excel.

- **Novel, controllable variation operators grounded in clear reasoning**: Sections 3.2–3.3 introduce fitness-guided crossover (conditioning on a target fitness f* derived from parent fitness with extrapolation parameter α) and diversity-guided mutation (using inverse-likelihood weighting with temperature τ to favor unlikely offspring). Figures 5–6 demonstrate that these hyperparameters systematically tune the exploration–exploitation trade-off, a level of control absent from conventional subtree crossover and point mutation.

- **Systematic ablation isolating each component (Figure 7)**: The ablation compares the full LLEGO against versions that remove the semantic prior (LLEGO_no_prior), remove crossover, remove mutation, or restrict arity to 2. Full LLEGO outperforms all ablations, confirming that both guided operators and higher-arity context are individually necessary — not just collectively sufficient — for best search performance.

- **Search efficiency advantage over conventional GP**: Figure 4 shows LLEGO achieving higher median population fitness with faster convergence across 25 generations on all classification datasets, while diversity decreases as search focuses on semantically promising regions — consistent with the claimed efficiency gains.

## Weaknesses

### Fatal
None.

### Major

1. **Wall-clock time comparison confounds search efficiency with inference cost.** The paper imposes a uniform 10‑minute wall‑clock limit per run (Section 5). LLEGO relies on LLM API calls that are substantially slower per evaluation than greedy methods (CART, C4.5) or even conventional GP (GATree). Under equal wall time, LLEGO necessarily explores fewer candidate trees — yet the paper also claims LLEGO "requires fewer evaluations" (Section 5.1) without reporting the actual number of evaluations each method performed. The direction of this confound works *against* LLEGO (it wins despite fewer evaluations), which could make the results *stronger* evidence of genuine search efficiency. But without reporting evaluation counts or an auxiliary comparison under equal evaluation budgets, the reader cannot distinguish whether LLEGO's advantage comes from the LLM's semantic priors or simply from the baselines being unable to search enough under the time constraint. This gap undermines the precision of the headline claim that LLEGO "consistently outperforms."

2. **No statistical significance testing is reported.** The paper reports means and standard deviations over 5 runs and uses average rank, but no paired statistical test (e.g., Wilcoxon signed-rank, corrected Friedman, or Bayesian signed-rank test) is applied across datasets. With only 5 runs per setting and 12 datasets, the observed superiority may not be reliable. For example, Table 1 appears to show that on some datasets (Blood depth 3, Electrical depth 3) LLEGO is tied with or worse than GATree; in regression, on Yacht, LLEGO's MSE is worse than GATree's. Without formal testing, the claim of *consistent* superiority is overstated. The paper should include across‑dataset significance tests to support this central claim.

### Minor

3. **The intuitive explanation of the mutation operator's diversity signal is factually inverted (Section 3.3).** The text states: "s(õⱼ) reflects the likelihood of the candidate offspring given the set of parents, with smaller values indicating that the candidate offspring has low probability under the current population distribution." Since s is defined as the *negative log probability* (s = −log p), smaller s corresponds to *higher* probability, not lower. The actual sampling formula (weights ∝ exp(s/τ)) is correctly designed to favor low-probability candidates for diversity, so only the textual intuition is wrong. This should be corrected to avoid confusing readers about the mechanism.

4. **Fairness‑regularized experiments are mentioned but no results are presented (Section 5.4).** The paper states "we investigated LLEGO's ability to mitigate negative bias by optimizing fairness-regularized objectives" but provides no data, figure, or analysis. This dangling reference either should be removed (if the experiment is not central to the paper) or expanded with results.

5. **The claim that LLEGO "requires fewer evaluations" is made without supporting data.** Line 133 states "LLEGO achieves this superior performance while requiring fewer evaluations," but no table or figure in the main text reports evaluation counts per method per run. This unsubstantiated claim should either cite evaluation counts or be softened.

### Trivial
None.

## Nice-to-Haves

- Run an auxiliary experiment under equal evaluation budgets (same number of candidate trees evaluated) to disentangle search efficiency from LLM inference cost.
- Provide a wall-clock breakdown (LLM inference time vs. fitness evaluation time) for LLEGO to clarify the computational trade-off already acknowledged in the limitations.
- Report or ablate the effect of the λ′/λ candidate generation ratio in the mutation operator.
- A brief example of the prompt template in the main text would improve readability.

## Removed Points

- *"Semantic prior framing is inflated"*: The paper clearly defines its use of "semantic prior" as the LLM's pretrained knowledge, and the ablation (LLEGO_no_prior) explicitly investigates the impact of removing explicit feature semantics. The paper is transparent about what the term means in this context.
- *"Crossover target fitness form not justified"*: The paper provides an intuitive explanation for the linear extrapolation form (f* = f_max + α(f_max − f_min)) and its relationship to α controlling exploration. This is a reasonable design choice; not every design decision requires exhaustive justification.
- *"Baselines may not have been tuned within 10‑minute budget"*: The paper explicitly states "each method is allowed 10 minutes of wall clock time per seeded run, which includes time spent on hyperparameter tuning" (line 129). This criticism assumes the opposite of what the paper says.
- *"Validation fitness not clearly defined"*: The paper states that training-set fitness is used during evolution and validation fitness is used for final selection (Section 3.4, line 101), which is standard practice.
- Various formatting/style nitpicks and requests for material that would only be in the appendix (which the parser stripped).

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the authors themselves do not make. The key insight — that LLM-based variation operators with fitness/diversity guidance can outperform both conventional GP and exact decision tree methods — is the paper's own.

## Suggestions

1. **Report evaluation counts** for each method per run (or the number of generations × population size explored) to support the efficiency claim and clarify the wall-clock confound. Even better, add an auxiliary experiment with equal evaluation budgets.
2. **Add statistical significance tests** across datasets (e.g., Wilcoxon signed-rank test or Bayesian signed-rank test on the paired per-dataset results) to formally support the claim of consistent superiority.
3. **Fix the inverted intuition** in Section 3.3: smaller s (negative log probability) corresponds to *higher* probability, not lower. The formula is correct; the text is not.
4. **Either remove or flesh out** the fairness-regularized results mention in Section 5.4 — dangling references to experiments without data weaken the paper.
