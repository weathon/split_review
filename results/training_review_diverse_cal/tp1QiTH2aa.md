Now I have all the information needed. Let me produce the final consolidated review.

## Summary

The paper introduces QWICK (Question-Wise model pICK), a method for cost-effective synthetic data generation (SDG) that frames per-question model selection under a budget constraint as a budget-limited multi-armed bandit problem. The algorithm tracks reward-cost ratios across models per question, uses a cost-aware selection rule with exploration, and progressively converges to cost-effective model assignments. On three benchmarks (GSM8K, MATH, MBPP), QWICK achieves 33–50% cost reductions at matched quality and up to 2.1× more valid synthetic data at the same budget compared to baselines.

## Strengths

- **Novel per-question formulation of cost-effective SDG as a budget-limited bandit.** The paper formalizes a problem that prior work treated at the dataset level — dynamic model selection at the *question* level, motivated by Table 1 showing different models excel on different questions. This is a principled departure from dataset-level selection.

- **Significant and quantified cost reductions with matched or improved data quality.** On MBPP, QWICK achieves 50% cost reduction while maintaining comparable fine-tuned accuracy; on GSM8K and MATH, reductions are 40% and 33% respectively (Figure 4, first row). These numbers are concrete, reported across multiple budgets and datasets.

- **Up to 2.1× more valid synthetic data at the same cost.** Under identical budgets, QWICK generates up to 112% more valid samples on MATH and 106% more on MBPP compared to UCB1 (Figure 4, second row). This directly demonstrates higher total reward (valid sample count).

- **Demonstration of flexible utility metric with an Outcome Reward Model.** Section 4.3 shows QWICK works with a non-binary reward (ORM), achieving up to 2.2× higher reward than UCB1. This shows the method is not limited to ground-truth comparisons.

- **Convergence analysis validates algorithm behavior.** Figure 5a visualizes how QWICK progressively switches from cheap models to larger models on questions where the cheap model underperforms, converging per-question selections after few iterations. This provides interpretable evidence that the algorithm works as designed.

## Weaknesses

### Fatal
None.

### Major

- **Missing dataset-level cost-aware baseline conflates two sources of improvement.** QWICK is both *cost-aware* and *per-question*; the baselines (random selection and dataset-wise UCB1) are neither cost-aware nor per-question (UCB1), or per-question but random. The observed gains of 50% cost reduction and 2.1× more valid data could reflect the benefit of cost-awareness, per-question adaptation, or both. A dataset-level cost-aware baseline (e.g., a fractional KUBE applied at the dataset level, selecting one model for all questions based on empirical reward-cost ratio) would isolate the per-question benefit. Without it, the paper's central claim — that per-question selection is superior — is not as cleanly supported as it should be. The discussion in Section 4.2 gestures at this comparison but does not provide quantitative results from an actual implemented baseline.

### Minor

- **Uniform generation length assumption acknowledged but unexamined empirically.** The algorithm's stopping criterion (Algorithm 1, line 16) and initial reward-to-cost ratio estimates use per-token cost *aᵢ* only, assuming uniform generation lengths across models. However, the experiments track actual costs as token count × per-token price (line 182), and different models can generate systematically different output lengths (e.g., a verbose large model vs. a concise small one). When actual token counts differ meaningfully, the algorithm's internal utility estimates may misalign with the true cost objective. The paper acknowledges this assumption (line 158) but provides no empirical evidence about its impact in the tested model pools.

- **Hyperparameter sensitivity unexplored.** The parameters α=16 (scaling exploration term) and β=0.5 (mixing question-level and dataset-level reward) are set with no sensitivity analysis or empirical justification. The exploration term is scaled by 1/α, and α=16 makes exploration quite small. Without ablations across reasonable ranges (e.g., α∈{8,16,32}, β∈{0.25,0.5,0.75}), it is unclear whether the reported results depend on careful tuning or are robust across choices.

- **Coverage and diversity metrics are referenced but not defined.** The paper attributes accuracy gains to increased coverage and diversity (Section 4.1, Figure 3) and reports these as metrics (Figure 4, third row), but never defines how coverage and diversity are computed. The reader cannot evaluate these claims without a definition or at minimum a precise reference to a known metric.

### Trivial

- **Cost normalization (ĉ) is introduced but not explained.** The empirical normalized cost ĉ_{i,t,j} appears in the selection rule (lines 20, 23) and is described as "used to estimate the cost" (line 160), but the paper never specifies how ĉ is computed from observed costs, nor why the min-over-pool normalization is needed. This makes the selection rule harder to interpret than necessary.

- **Stopping condition is abstract in the algorithm but concrete in experiments.** Algorithm 1 takes `Stop(xⱼ)` as an opaque input condition. The experiments use "a maximum number of valid responses per question" (line 178), but the algorithm description never connects this concrete rule to the abstract stopping condition.

## Nice-to-Haves

- A brief discussion of how the per-question variant inherits (or modifies) the regret bounds of fractional KUBE would strengthen the theoretical grounding.
- The algorithm's internal utility (r̂/aᵢ) could be extended to use expected token counts per model rather than assuming uniform generation length, which would eliminate the mismatch.

## Removed Points

- **"Hyperparameter robustness with fixed defaults" (claimed Strength Finder strength).** This conflicts with the verified weakness that hyperparameter sensitivity is unexplored. Using fixed defaults across experiments does not demonstrate robustness without an ablation study. Removed per the rule that when a strength and verified weakness disagree, the weakness wins.

- **"QWICK is both cost-aware AND per-question; UCB1 is neither" (Harsh Critic).** Random selection is per-question (picks per question, just not based on signal). The characterization oversimplifies. However, the core concern about missing a cost-aware dataset-level baseline is valid and retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a dataset-level cost-aware baseline.** Implement a dataset-level fractional KUBE (or dataset-level budgeted UCB): select one model for all questions based on the same reward-cost ratio criterion, without question-wise differentiation. This would directly isolate the benefit of per-question adaptation and strengthen the paper's central claim.

2. **Validate or address the uniform generation length assumption.** Report the distribution of generated token counts per question across models in at least one setting (e.g., MATH with Gemma models). If the assumption holds approximately, note it; if not, discuss the expected impact on algorithm decisions.

3. **Add a hyperparameter sensitivity study.** On one dataset (e.g., MATH with Gemma models), vary α∈{8,16,32} and β∈{0.25,0.5,0.75} and show that the relative ordering over baselines is preserved.

4. **Define coverage and diversity metrics explicitly** or cite a specific existing metric with a short description of how they are computed in this paper.

5. **Explain ĉ computation.** Clarify how the empirical normalized cost ĉ_{i,t,j} is derived from observed costs (c_{i,t,j}) and why the min-over-pool normalization is included.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>