Now I have thoroughly verified all claims. Let me write the final consolidated review.

## Summary

This paper proposes Ranking-Constrained Actor-Critic (RCAC), an offline reinforcement learning approach for learning branching policies in MILP solvers. The key idea is to train a reward-weighted ranking model to define the "safe" action support, then constrain an actor-critic to only consider the top-k ranked actions. This prevents out-of-distribution action queries that plague standard offline RL while preserving the ability to exploit rare but good actions not captured by density-based constraints. Experiments compare against imitation learning (GGCN), online RL (tMDP), and heuristic baselines across 6 benchmark datasets, using both sub-optimal (VHB) and small near-optimal (FSB 5%) datasets for training.

## Strengths

- **Problem motivation is strong and practical.** Reducing dependence on expensive FSB demonstrations is a recognized bottleneck in learning to branch. The paper clearly articulates this motivation and designs two realistic training scenarios (sub-optimal heuristic data, small near-optimal data) that directly address it. Table 1 shows the data collection time reduction is dramatic (e.g., 1–6 hours vs 78–540 hours for the standard dataset).

- **The ranking-constrained approach is well-motivated for the branching domain.** The paper correctly identifies that standard density-based offline RL constraints would exclude rare but high-quality actions when the behavior policy is sub-optimal. Using dual-bound improvement (the reward signal) to define the action support rather than action frequency is a natural and sensible adaptation to the branching setting (Section 3.2, Equations 6–8). The ablation (Table 5, Figure 3) provides evidence that RCAC is not merely distilling the ranking model but learning Q-values among top candidates.

- **Experimental design thoughtfully addresses the stated motivation.** Using two distinct data scenarios (sub-optimal VHB dataset and small near-optimal FSB 5% dataset) tests exactly the conditions the paper claims to address. On 4 of 6 benchmarks (SC, MIS, CA, WA) results favor RCAC, and on 2 (CFL, AP) results are mixed. The ablation study comparing RCAC against its own ranking model G_ω helps disentangle the source of improvement.

- **The paper reports mean and standard deviation over 5 seeds for the 4 easy benchmarks** (Section 4.2, line 159), enabling assessment of statistical reliability for the core exact-solving results.

## Weaknesses

### Fatal
None.

### Major

- **The claim that RCAC "consistently outperforms the representative baseline methods across 6 benchmark datasets" (Introduction, line 19) is not supported by the reported results.** On CFL, RCAC-H has higher solving time (373.48±28.28) and larger search tree (219.92 nodes) than GGCN-H (361.47±8.95, 211.56 nodes) — i.e., RCAC loses on both metrics with the VHB dataset. On AP, RCAC-S and RCAC-H both underperform GGCN-S and GGCN-H in dual-integral score (Table 4). The paper further claims on line 164 that "RCAC is better than GGCN across all benchmarks and two types of training datasets," which is contradicted by the CFL-H results. These overstatements are not minor — they directly undermine the paper's headline claim and need to be corrected with precise, qualified language acknowledging where RCAC does and does not outperform baselines.

- **No comparison against standard offline RL algorithms adapted to the branching domain.** The paper positions RCAC as an offline RL method and claims it is "the first work in applying offline RL in learning to branch" (Section 5.1). However, no general offline RL algorithm (e.g., CQL, IQL, AWAC adapted to branching) is compared against. Without such a comparison, it is unclear whether RCAC's design choices (ranking constraint, etc.) provide meaningful advantages over adapting existing offline RL methods to the branching MDP. The comparison to GGCN (IL) and tMDP (online RL) does not fill this gap. This weakens the paper's framing and its claim of being a novel offline RL contribution.

- **Insufficient statistical reporting on hard problems (WA, AP).** The paper states it "report[s] the best results for each model" (line 178) with no variance or confidence interval. Given that Table 4 shows small margins between methods (e.g., GGCN-S at 1299.89 vs RCAC-S at 1285.98 on AP), single best-value reporting makes it impossible to assess whether differences are meaningful. This is a significant methodological gap for the experiments on two of the six claimed benchmarks.

### Minor

- **Key hyperparameter values (λ, δ, γ) are not reported in the visible text.** The method depends on λ (reward-weighting factor), δ (penalty magnitude for out-of-top-k actions), and γ (discount factor). While k is explored on one dataset (Figure 3, CA), no values for λ, δ, or γ are given. This impairs reproducibility. (If these values were in a stripped appendix, they should be moved to the main paper.)

- **Insufficient discussion of negative results on CFL (VHB dataset) and AP.** On CFL, RCAC-H underperforms GGCN-H, and on AP, both RCAC variants underperform GGCN. The paper notes that neural methods "do not show a very strong advantage" on hard problems (line 180), but does not discuss why RCAC specifically underperforms GGCN on these benchmarks while succeeding on others. Similarly, the ablation notes G_ω underperforms GGCN-H on CFL (Table 5), but this is not explored. Understanding when/why the ranking constraint fails would strengthen the contribution.

### Trivial
- "PRB" is used as the acronym for reliability pseudocost branching on line 142, while "RPB" is used on line 47. These should be consistent.

## Nice-to-Haves
- Comparison against at least one general offline RL baseline (e.g., CQL or IQL) adapted to branching, to substantiate the claim that RCAC's design is advantageous.
- Sensitivity analysis for λ (the reward-weighting factor) analogous to Figure 3 for k.
- Statistical significance testing (e.g., confidence intervals) for the hard-problem results in Table 4.
- An analysis of how often G_ω ranks genuinely good actions outside top-k, which could explain performance drops on CFL.
- A brief discussion of why CFL and AP differ from the other benchmarks in terms of RCAC's relative performance.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Strength Finder's strength 2** ("Outperforms prior IL-based and online RL-based methods in exact solving on four standard benchmarks"): Conflict with verified weakness — RCAC does not always outperform, e.g., CFL-H. Moved due to conflict with verified overclaiming weakness.
- **Criticism about the paper's claim "is the first attempt" being questionable given Huang et al. (2023b) and Qu et al. (2022):** The paper explicitly addresses these works in Section 5.1, distinguishing RCAC by its handling of OOD actions and sub-optimal datasets. The distinction is reasonable and acknowledged.
- **Criticism about the VHB baseline using FSB with probability 0.05 being "quite informed":** The paper explicitly describes VHB as a "vanilla hybrid branching" heuristic designed to be sub-optimal. It is clearly described — this is not a hidden advantage.
- **Criticism about tMDP exclusion from hard problems:** The paper provides a reason (long training time and bad performance on easy problems). While the absence of an RL competitor is noted, the reasoning is transparent.
- **Hyperparameter criticism framed as appendix stripping issue:** The core concern (values not given) is kept above; the framing about missing appendix is removed per hard rules.

## Novel Insights
None beyond the paper's own contributions. The reviews largely converge on the paper's stated narrative: a well-motivated offline RL approach for branching that achieves good results on most benchmarks but overclaims its consistency, lacks comparison against general offline RL baselines, and has weak statistical reporting on hard problems. The most useful insight from the review process is that the paper's headline claim of "consistent" outperformance is contradicted by its own data on CFL and AP, suggesting the contribution may be more domain-dependent than claimed.

## Suggestions
1. Reword the headline claims: replace "consistently outperforms across 6 benchmark datasets" with precise, per-dataset language acknowledging where RCAC leads, ties, or trails baselines.
2. Add at least one adapted offline RL baseline (e.g., CQL or IQL) to the comparison, or provide a substantive argument for why adaptation is non-trivial and the existing comparison suffices.
3. Report mean and variance (over multiple seeds) for the hard-problem results in Table 4, consistent with the reporting on easy problems.
4. Disclose all hyperparameter values (λ, δ, γ) used in the reported experiments, either in the main paper or a public repository.
5. Add a discussion section analyzing the failure cases (CFL with VHB data, AP) — e.g., problem characteristics that might cause the ranking constraint to be less effective.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>