Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes Ranking-Constrained Actor-Critic (RCAC), an offline reinforcement learning algorithm for learning branching policies in MILP solvers. RCAC trains a ranking model to identify promising candidate actions using dual-bound improvement rewards, then constrains the actor-critic policy to only consider the top-k candidates, thereby handling the dynamic action space and out-of-distribution actions typical in offline RL for branch-and-bound. The experiments show RCAC consistently outperforms imitation learning (GGCN) on the same limited or suboptimal datasets across four easy and two hard benchmarks, while also comparing favorably against hand-crafted heuristics (FSB, RPB) and online RL (tMDP).

## Strengths

1. **Novel and well-motivated offline RL formulation for branching**: The paper correctly identifies a real bottleneck in prior neural branching methods—their reliance on large, near-optimal demonstrations—and proposes a principled offline RL solution. The ranking-constrained design specifically addresses the unique challenges of B&B (dynamic action space, OOD action risk) that generic offline RL methods do not handle. This is stated clearly in Section 3.2 and Section 5.1.

2. **Consistent empirical advantage over IL on the same limited data**: Across all six benchmarks (SC, MIS, CA, CFL, WA, AP), RCAC outperforms GGCN when both are trained on the same datasets—whether suboptimal (VHB-100k) or small near-optimal (FSB-5k). This is demonstrated in both exact-solving metrics (Tables 2, 3; Figure 1) and time-constrained dual-integral scores (Table 4; Figure 2). The advantage is especially pronounced on MIS and CA, where RCAC reduces solving time by factors of 2–5× over GGCN on the same data.

3. **Ablation validates that RCAC learns beyond the ranking model**: Table 5 and Figure 3 show that RCAC improves over the pretrained ranking model \(G_{\omega}\) alone, and that varying the top-k constraint affects performance in a manner consistent with learning Q-values (rather than simply distilling \(G_{\omega}\)). This disentangles the RL component from the ranking pretraining.

4. **Practical data-efficiency advantage**: Table 1 quantifies the data collection time, showing that VHB-100k and FSB-5k datasets require hours of collection versus days for the standard FSB-100k dataset. Combined with the performance results, this supports the paper's practical motivation.

## Weaknesses

### Fatal

None.

### Major

1. **Missing comparison against GGCN trained on full FSB-100k (standard practice)**. The paper's narrative is that RCAC overcomes the need for expensive, high-quality demonstrations. To fully substantiate this, the paper should compare RCAC (trained on cheap VHB-100k or small FSB-5k) against GGCN trained on the standard 100k FSB dataset—i.e., the prior state of the art that the paper aims to replace. The current experiments compare RCAC and GGCN only when both are trained on the same limited data, which shows RCAC makes better use of limited data but does not answer the practical question: can RCAC on cheap data match or surpass GGCN on expensive data? This gap weakens the strongest practical claim in the abstract and conclusion. Table 1 already reports the collection times, making this a straightforward extension that would either strongly validate or honestly qualify the central claim.

2. **No comparison against other offline RL algorithms adapted for B&B**. The paper claims to be "the first work in applying offline RL in learning to branch" and introduces a custom ranking constraint. But without comparing against a generic offline RL method adapted to this setting (e.g., a variant of CQL or IQL using the same GNN architecture and Bellman updates, without the ranking constraint), it is unclear whether the reported gains come from the specific ranking-constrained design or simply from using any offline RL with reward signals instead of IL. The paper describes the distributional-shift challenge but never validates that its specific solution is necessary; a simple conservative Q-learning baseline would isolate the contribution of the ranking constraint.

### Minor

1. **The ranking model's shortsightedness is acknowledged but not directly tested**. The scoring function \(G_{\omega}\) weights actions by immediate dual-bound improvement (Equation 6 with \(\zeta=0\)). The top-k constraint can filter out actions with low immediate reward but high long-term value. The ablation (Figure 3) is consistent with this concern—increasing \(k\) (relaxing the constraint) improves performance on CA. The paper shows RCAC improves over \(G_{\omega}\), but does not test whether a softer penalty (e.g., a weighted BC term or using \(G_{\omega}\) as a prior rather than a hard cutoff) would be more effective. This does not invalidate the method but leaves an important design question open.

2. **Hyperparameters not stated in the main text**. Key values for \(k\), \(\delta\), \(\lambda\), learning rates, and network architecture details are absent from the main paper. These affect reproducibility and are needed for practitioners to assess or implement the method.

3. **Wall-clock training time for RCAC not reported**. The paper reports data collection time but not the actual training time of RCAC (including the ranking model pretraining and actor-critic training). This information would help assess practical feasibility, especially since the GNN architecture is used three times (for \(G_{\omega}\), \(\pi_{\phi}\), and \(Q_{\theta}\)).

### Trivial

None.

## Nice-to-Haves

- **Translate the dual-integral scores into physically meaningful units** (e.g., relative optimality gap over time) for WA and AP, to help readers judge effect size beyond relative rankings.
- **Test a softer variant of the ranking constraint** (e.g., using \(G_{\omega}\) scores as importance weights or a penalty coefficient rather than a hard top-k cutoff), to directly address the shortsightedness concern.
- **Report the percentage of actions filtered out by the top-k constraint in practice**, to help readers understand how restrictive the constraint actually is.

## Removed Points

- **"PRB vs RPB typo"**: Minor inconsistency between "PRB" (Section 4.1) and "RPB" (Section 2.1) in the paper. Removed per hard rule on typo criticisms.
- **"Single GNN architecture for all three networks is expensive"**: The harsh critic notes this as an observation, not a weakness. The paper acknowledges the shared architecture choice in Section 3.3. Not a substantive weakness.
- **"The method description could be clearer about δ"**: The critic notes δ is not discussed in the main paper. This is a hyperparameter that belongs in the experimental setup section; papers routinely defer hyperparameter values to appendices. Minor and borderline-pedantic.

## Novel Insights

The key insight emerging from the reviews is that the paper's evaluation design creates a blind spot: by comparing RCAC and GGCN only on the *same* limited data, it proves that offline RL extracts more value from constrained data than IL does, but it never tests the most practically relevant comparison—whether the *total cost* of RCAC (cheap data + training) pays off relative to the established practice of GGCN trained on expensive data. This is a case of framing the experiments around the algorithmic question ("does offline RL beat IL given the same data?") rather than the practical question ("does the proposed pipeline beat the existing pipeline when you account for all costs?"). Both questions are valid, but the paper claims to answer the latter while providing evidence only for the former.

## Suggestions

1. **Add GGCN trained on full FSB-100k as a baseline.** This single comparison would directly test the paper's practical claim. Even one benchmark (e.g., SC or MIS, where data collection is cheapest) would be informative. If RCAC on VHB-100k or FSB-5k matches or beats this baseline, the paper's central claim is strongly validated. If not, honestly report the gap and discuss trade-offs.

2. **Add a generic offline RL baseline** (e.g., CQL with the same GNN architecture, with the action space handled by masking invalid actions). This would isolate whether the ranking constraint is the source of improvement or merely the offline RL framework itself.

3. **Report key hyperparameters** (\(k\), \(\delta\), \(\lambda\), training details) in the main paper or a clear pointer to where they appear.

4. **Deepen the ablation on the ranking constraint**: test a "soft" variant where \(G_{\omega}\) scores are used as a penalty weight rather than a hard filter, to determine whether the hard cutoff is beneficial or harmful.

## Score and Decision

The paper proposes a genuinely novel and well-motivated approach to a recognized problem in neural MILP solving. The core algorithmic contribution (ranking-constrained actor-critic) is clean and the experiments convincingly show RCAC > IL on the same limited data across diverse benchmarks. However, the evaluation has meaningful gaps: the most practically relevant baseline (GGCN on full FSB-100k) is absent, and the contribution of the specific ranking constraint (versus any offline RL method) is not isolated. These gaps prevent the paper from fully supporting its strongest claims about overcoming data-collection obstacles. The paper is a solid contribution that would be substantially strengthened by addressing these gaps. I recommend a borderline accept with the expectation that the missing baselines be addressed in the final version.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>