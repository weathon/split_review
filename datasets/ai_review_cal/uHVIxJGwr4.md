- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 8, 3, 3, 5
Now I have a thorough understanding of the paper and can proceed to synthesize the final consolidated review.

---

## Summary

This paper proposes Ranking-Constrained Actor-Critic (RCAC), the first offline reinforcement learning method for learning branching heuristics in MILP solvers. RCAC trains a reward-weighted scoring function to rank candidate branching actions, then constrains the policy to only consider top-*k* candidates during offline actor-critic training, mitigating distributional shift while still allowing high-quality out-of-distribution actions. The method is evaluated on six benchmarks (four easy, two hard) against hand-crafted heuristics, imitation learning (GGCN), and online RL (tMDP), using both exact-solving and time-constrained settings.

## Strengths

1. **First principled offline RL approach for MILP branching.** The paper correctly distinguishes itself from Huang et al. (2023) and Qu et al. (2022), which claim to be offline RL but still assume cheap access to near-optimal expert demonstrations. RCAC is the first to tackle the full offline RL problem (sub-optimal behavior policy, small dataset, OOD action handling) for branching. This is a genuinely novel contribution.

2. **Consistent and clear outperformance on exact solving across four easy benchmarks.** On Set Covering, Maximal Independent Set, Combinatorial Auction, and Capacitated Facility Location, RCAC trained on either sub-optimal (VHB) or small (5k FSB) data consistently beats GGCN trained on the same data, in both solving time and search tree size (Tables 2 and 3). The results are reported as mean ± std over 5 seeds. For example, on Set Covering with sub-optimal data, RCAC achieves 271.0s vs GGCN's 380.3s; on CA with small FSB data, RCAC reduces nodes from 3,721 to 2,369. These are clean, reproducible improvements.

3. **Dramatic reduction in data collection cost.** Table 1 shows that the sub-optimal VHB dataset takes 0.2–1.8 hours per problem, versus 128.7–465.7 hours for the standard FSB dataset. Despite this 100–1000× reduction, RCAC still outperforms methods trained on expensive data. This directly supports the paper's main practical motivation and is the strongest evidence for the method's value.

4. **Ablation confirms RL-driven improvement beyond the scoring function.** Table 5 shows RCAC further improves over its own ranking model G_ω (e.g., on CA, reducing nodes from 4,084 to 3,965). Figure 3 shows that increasing *k* (allowing more candidates) monotonically improves performance, ruling out the concern that RCAC merely distills the scoring function.

## Weaknesses

### Fatal

None.

### Major

1. **Hard-problem evaluation reports only "best results," not mean ± std, making the claims uninterpretable.** For Workload Apportionment and Anonymous Problem (Table 4, Figure 2), the paper states: "We evaluate each model on 20 testing instances from the official split and report the best results for each model" (line 178). No standard deviations, no per-seed breakdown, no confidence intervals. The text then claims RCAC "shows some promising signals" and "takes the lead" — but with only best-case reporting, the reader cannot assess whether this advantage is meaningful or just noise in the metric. The easy-problem experiments (Tables 2-3) properly report mean ± std over 5 seeds, so the inconsistency here is striking. This is the most significant weakness in the paper's experimental evidence.

2. **No comparison to a standard unconstrained offline RL method (e.g., CQL, IQL).** The paper's key methodological contribution is the ranking constraint — yet there is no ablation or baseline that removes this constraint and applies a standard conservative offline RL method instead. The ablation on *k* (Figure 3) shows that larger *k* (weaker constraint) improves performance, which is consistent with the possibility that removing the constraint entirely might work at least as well. Without this comparison, the paper cannot substantiate that the ranking constraint is beneficial rather than an unnecessary complication. This is the central methodological gap.

3. **tMDP comparison is incomplete and selectively reported.** The paper excludes tMDP from the hard-problem evaluation (WA, AP) with the justification "due to its long training time and bad performance on easy problems" (line 178). Even on the easy problems where tMDP is included, the results are described qualitatively ("tMDP could sometimes achieve a good performance such as on CA") without the full numerical results in the tables. Since tMDP is one of only three neural baselines, this selective reporting weakens the overall comparison. The paper should either provide the full tMDP numbers (even if poor) or clearly state when training was infeasible.

### Minor

1. **Missing the GGCN baseline trained on the full 100k FSB dataset.** The paper trains GGCN only on the same limited data (VHB or 5k FSB) as RCAC. Showing that RCAC beats GGCN on the same poor data is expected behavior. The more informative comparison would be GGCN trained on the standard large FSB dataset (as in Gasse et al., 2019), which would show how much of the gap between limited-data and abundant-data performance RCAC actually closes. This is not a fatal omission (the paper's core claim is about learning from limited data, not matching full-data methods), but it would significantly strengthen the results.

2. **Several training hyperparameters are not specified.** The paper does not report the values of λ (the reward-weighting factor in Eq. 6), γ (discount factor), learning rates, batch size, the value of *k* used in main experiments (only ablation varies it), or the negative penalty δ for OOD actions. The GNN architecture is referenced to Gasse et al. (2019), which is acceptable, but the RL-specific hyperparameters are missing. This hinders reproducibility.

3. **No statistical significance tests for the main comparisons.** Although means and standard deviations are reported for the easy problems (Tables 2-3), the paper does not perform any significance test (e.g., paired t-test, Wilcoxon) to confirm that the observed differences between RCAC and GGCN are statistically reliable.

### Trivial

- The paper uses "PRB" as an abbreviation in the baseline description (line 142) but likely means "RPB" (reliability pseudocost branching), as RPB is the standard term used elsewhere in the paper.

## Nice-to-Haves

- An ablation on λ (the reward-weighting factor) to show its sensitivity.
- A brief analysis of behavior policy quality — reporting the average dual-bound improvement per step for VHB vs FSB on representative instances would help contextualize the dataset quality.
- Reporting the *k* value used for the main experiments.

## Removed Points

- **"GNN architecture details omitted"**: The paper explicitly states "We use the same features and GNN architecture from Gasse et al. (2019)" (line 130). This is standard practice for referencing established architectures. Removed.
- **"Number of MILP instances for generating transitions is not given"**: The paper specifies "generate 10,000 MILP instances for training, 2,000 instances for validation, and 20 instances for testing on each problem" (lines 146-147) for easy problems. For hard problems, the official ML4CO split is used. Removed.
- **"VHB with prob 0.05 lacks sensitivity analysis"**: Pure scope creep; requesting a sensitivity analysis for every design choice is unreasonable. Removed.
- **"Ranking constraint uses a short-sighted proxy"**: This is essentially the same concern as the missing unconstrained baseline comparison (already listed as Major #2). The paper acknowledges the G_ω is a heuristic ranking and the Q-learning is supposed to correct for short-sightedness. The specific implied criticism that "larger k works better → removing k might work better" is exactly the ablation gap already captured. Merged into Major #2 rather than listed separately.
- **"tMDP excluded from hard problems"**: The paper provides a justification (long training time + poor easy-problem performance). This is a reasonable scoping decision. The real issue is the incomplete reporting where tMDP is included. Removed as separate point; retained as part of Major #3.
- **"Metric for hard problems is not clearly defined"**: The paper clearly states "we directly report the score from the ML4CO evaluation script, which is a negated unshifted version of the dual integral intended to be maximized" (lines 146-147). The metric is standard and well-defined. Removed.

## Novel Insights

The most interesting observation emerging from the review is the tension in the ablation results: Figure 3 shows that RCAC monotonically improves as *k* increases (weaker constraint), yet the paper's core contribution is precisely this constraint. This dynamic — where the supposedly beneficial constraint degrades performance as it is relaxed — is never directly examined by testing a completely unconstrained (or CQL-style) offline RL baseline. The paper's interpretation (that increasing *k* shows RCAC "learns to evaluate Q-values rather than distilling G_ω") is reasonable but incomplete: it could also mean the constraint is a net negative and the Q-learning is doing all the work. Resolving this ambiguity would substantially strengthen the paper.

## Suggestions

1. **Report mean ± std (or per-instance scores) for WA and AP.** This is the single most actionable fix. Even 3-5 seeds with one standard deviation would make the hard-problem results interpretable.
2. **Add a comparison to a standard unconstrained offline RL method.** Apply CQL, IQL, or even a simple conservative variant to the same datasets. This directly tests whether the ranking constraint is essential or if any offline RL method would achieve similar results.
3. **Add the full-data GGCN baseline** (trained on 100k FSB transitions) for the easy benchmarks. This would show how much of the gap RCAC closes relative to a method trained on optimal abundant data — the most practically relevant comparison.
4. **Report all missing hyperparameters** (λ, γ, learning rates, batch size, *k*, δ) in the main text or supplement.
5. **Report full tMDP numerical results** for all easy benchmarks in the table, either adding the missing entries or explicitly stating when training was infeasible.
