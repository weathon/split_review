Now I have all the evidence I need. Here is my consolidated meta-review.

## Summary

This paper proposes RCAC (Ranking-Constrained Actor-Critic), an offline RL approach for learning branching strategies in MILP solvers. The method trains a reward-weighted scoring function G_ω to rank candidate actions, then constrains an actor-critic policy to only consider top-k actions when estimating Q-values. This aims to learn effective branching from sub-optimal or small datasets without requiring expensive near-optimal demonstrations (IL) or costly online interaction (online RL). Experiments across six benchmarks show RCAC outperforms GGCN (IL) and tMDP (online RL) on four easy synthetic problems, with more modest results on two hard real-world problems.

## Strengths

- **First principled offline RL application to MILP branching.** The paper correctly identifies that prior neural branching methods either require near-optimal demonstrations (IL) or costly online interaction (online RL). RCAC is the first approach that explicitly tackles the distributional shift problem in offline RL for branching, with a clear motivation grounded in the limitations of existing methods. The paper discusses this contribution transparently (Section 5.1) and distinguishes itself from prior work by Huang et al. (2023b) and Qu et al. (2022), which it correctly notes do not address OOD actions.

- **Consistent and strong results on four easy synthetic benchmarks.** On SC, MIS, CA, and CFL, RCAC trained on either a sub-optimal (VHB) or small near-optimal (FSB) dataset consistently outperforms GGCN and tMDP in both solving time and tree size (Tables 2, 3; Figure 1). Results are reported with mean and standard deviation across 5 random seeds. This convincingly demonstrates that offline RL can learn effective branching from lower-quality or smaller datasets in settings where exact solving is feasible.

- **Practical data-efficiency gains.** Table 1 documents that collecting the sub-optimal VHB dataset takes only 0.5–8 hours, and the small FSB dataset (5% of standard size) takes 1–5 hours, compared to 5–21+ hours for standard FSB datasets. This is a genuine practical advantage; the paper's core practical claim — that RCAC reduces dependency on expensive expert demonstrations — is well-supported by these numbers.

- **Ablation clarifies the source of improvement.** Table 5 shows that the reward-weighted scoring model G_ω already outperforms GGCN, and RCAC further improves over G_ω in most cases (most prominently on CA). The k-ablation (Figure 3) shows that RCAC's performance improves with larger k, indicating RCAC is genuinely learning Q-values to select among top candidates rather than merely distilling G_ω. This disentangles the reward-weighted scoring from the RL component.

## Weaknesses

### Major

1. **The evidence on hard problems is too weak to support the paper's main motivation.** The paper explicitly motivates RCAC by the difficulty of collecting demonstrations for large/hard MILPs, yet on the two hard benchmarks (WA and AP), the results are marginal:
   - The paper reports only "best results" (line 178) without mean, standard deviation, or confidence intervals across seeds — in contrast to the easy benchmarks where 5 seeds and std are reported.
   - The improvements over GGCN and RPB appear small (e.g., WA best RCAC score vs. GGCN vs. RPB are closely clustered based on Table 4).
   - Only 20 testing instances are used per problem. The paper itself acknowledges "neural methods do not show a very strong advantage against non-neural methods" (line 180), yet the abstract claims RCAC "consistently outperforms" across all 6 benchmarks — this is an overclaim for the hard problems.
   - If the paper's primary value proposition is enabling learning where high-quality data is scarce, the hard-problem experiments are the most critical. As they stand, they show at best "promising signals" rather than convincing superiority.

2. **The ranking constraint's role is not well supported by the ablation.** The core algorithmic innovation is the ranking constraint that depresses Q-values for actions outside top-k (Equation 7). However, Figure 3 shows that **larger k (weaker constraint) monotonically improves performance** (fewer nodes) on CA. This means the method works best when the constraint is weakest. The paper interprets this as evidence that RCAC learns Q-values rather than distilling G_ω, which is a fair claim, but the result simultaneously undermines the justification for the constraint itself. If the constraint were serving its intended purpose of filtering toxic OOD actions, one would expect too-large k to eventually degrade performance. The paper does not demonstrate a k value where performance degrades, nor does it show that the constraint provides benefit over an unconstrained actor-critic. Together with Table 5 (where RCAC improves over G_ω only modestly on most benchmarks), this leaves uncertainty about whether the ranking constraint is a genuine algorithmic contribution or a design artifact that could be replaced by simpler mechanisms.

### Minor

3. **No comparison with standard offline RL baselines.** The paper positions RCAC as an offline RL method and claims to be "the first attempt to apply offline RL algorithms to MILP solving" (Section 1). Yet it compares only against GGCN (IL), tMDP (online RL), and hand-crafted heuristics. Standard offline RL algorithms (e.g., CQL, IQL, TD3+BC) could in principle be adapted to the branching setting. The paper briefly notes that its method handles the "dynamic action space" (Section 5.2), which is a valid challenge, but it does not provide a concrete argument for why existing offline RL methods would fail, nor does it include any representative baseline. This makes it difficult to assess whether RCAC represents a meaningful advance over adapting general offline RL techniques.

4. **The paper's claims slightly overstate the consistency of results.** The abstract says RCAC shows "advanced performance ... for different types of MILP problems on multiple evaluation benchmarks," and the conclusion says it "outperforms previous IL-based and RL-based neural branching methods in both branching quality and training efficiency, for both exact solving and time-constrained solving." On the hard problems (WA, AP), the dual-integral results are comparable to baselines with small margins, and the paper itself acknowledges neural methods "do not show a very strong advantage." These qualified internal statements should be reflected in the high-level claims.

5. **Limited analysis of reward sparsity.** The paper sets ζ = 0 to handle sparse rewards (line 107) but does not analyze how often the dual-bound improvement is zero for individual branching decisions. Since the scoring function G_ω is trained with reward-weighted log-likelihood, near-zero rewards for most actions could make G_ω behave similarly to behavior cloning. The paper does not investigate how sensitive the method is to the reward signal quality or the sparsity of positive-reward actions.

### Trivial

- The paper uses absolute k rather than k% for the ranking constraint (line 121). This means the number of candidates considered varies across instances with different numbers of fractional variables. The paper acknowledges this choice but does not analyze its impact.

## Nice-to-Haves

- Report mean and standard deviation across seeds for the hard problem results (WA, AP), and include more testing instances if available.
- Compare against at least one standard offline RL baseline (e.g., a version of TD3+BC adapted to the branching action space) to substantiate the claim of being a meaningful offline RL contribution.
- Systematically vary the sub-optimality of the behavior policy (e.g., different FSB mixing ratios in VHB) to demonstrate robustness to dataset quality.
- Run the k-ablation at more values and on more benchmarks to establish whether there exists a k where performance degrades, which would confirm the constraint's necessity.
- Report training and inference time of RCAC relative to GGCN and tMDP.

## Removed Points

- **"G_ω does not solve the OOD problem"** — The paper does not claim to fully solve OOD; it proposes a practical heuristic to "filter out toxic OOD actions" by using reward-weighted scoring. The criticism mischaracterizes the claim as stronger than it is.
- **"VHB is not purely sub-optimal"** — The paper clearly states VHB uses FSB with probability 0.05. VHB is sub-optimal relative to pure FSB. The characterization is accurate and transparent.
- **"Terminology inconsistency"** — Style nitpick about the paper not using standard offline RL vocabulary (pessimism, concentration coefficients). The paper situates itself relative to the offline RL literature adequately for its target domain.
- **"Reward function is essentially the dual integral with discounting"** — The paper explicitly acknowledges this (line 91: "The discount factor γ also favors an early improvement...as the dual integral does"). Not a weakness — a transparent design choice.

## Novel Insights

The reviews surface a tension that the paper does not fully resolve: the ranking constraint is both the primary algorithmic contribution and the component whose role is least supported by evidence. The ablation shows that making the constraint weaker monotonically helps, which shifts the burden of proof onto the authors to explain why the constraint is needed at all, rather than simply using G_ω as a prior within an otherwise standard actor-critic. A more informative ablation would compare RCAC against an unconstrained actor-critic (with no ranking constraint) trained on the same data, which would isolate the constraint's effect from the benefit of Q-learning itself. The paper's current explanation — that larger k simply gives the Q-function more candidates to evaluate — is plausible but does not address why the constraint is necessary at small k values.

## Suggestions

1. For hard problems, report mean and standard deviation across multiple seeds, and use more testing instances or a statistical test (e.g., paired bootstrap) so readers can assess whether the observed margins are reliable.
2. Either (a) add one representative standard offline RL baseline (e.g., TD3+BC adapted to the branching setup), or (b) provide a more rigorous argument for why such methods are inapplicable (e.g., demonstrate that they fail empirically, or explain formally why the dynamic action space breaks them).
3. Add an ablation that compares RCAC against an unconstrained actor-critic (no ranking constraint, just standard Q-learning with a behavior-cloning penalty as in TD3+BC). This would directly isolate whether the ranking constraint is beneficial, neutral, or harmful.
4. Temper the high-level claims to match the hard-problem evidence. Replace "consistently outperforms" with language that distinguishes strong results on easy problems from promising but preliminary results on hard problems.
5. Analyze the effective sparsity of the reward signal in the training data (fraction of actions with non-zero dual-bound improvement) and discuss how this affects G_ω and the Q-function.

## Score and Decision

The paper addresses an important practical problem and demonstrates a clear advantage on easy benchmarks where exact solving is feasible. However, the motivation for the method depends most heavily on the hard problems, where the evidence is weakest, and the core algorithmic component (the ranking constraint) is not convincingly justified by the ablation. The paper has genuine contributions (first offline RL for branching, practical data efficiency, strong easy-benchmark results) but needs to either substantially strengthen the hard-problem evidence or recalibrate its claims. A score of 6.0 represents a paper with clear contributions that falls short of the standard for full acceptance due to the gap between claimed scope and demonstrated evidence.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>