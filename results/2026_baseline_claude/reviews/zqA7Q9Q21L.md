## Summary

This paper introduces R2PS (Robust Real-time Pursuit Strategies), the first approach to worst-case robust, real-time pursuit strategies in graph-based pursuit-evasion games (PEGs) under partial observability. The work (1) proves that a dynamic programming (DP) algorithm yields strictly optimal strategies even when the evader moves asynchronously (after observing pursuers' actions), (2) proposes a belief preservation mechanism to track possible evader positions under partial observability, and (3) integrates the belief mechanism into the Equilibrium Policy Generalization (EPG) framework for cross-graph reinforcement learning, yielding a GNN policy with zero-shot generalization to unseen real-world graphs.

---

## Strengths

- **Clean theoretical contribution on asynchronous moves**: Theorems 2–3 and Corollary 1 rigorously show that the DP distance table D from Algorithm 1 simultaneously encodes optimal strategies for both synchronous and asynchronous evaders. Lemma 1 cleanly characterizes the minimax structure of D, and the optimality proof is tight: the asynchronous evader has strictly more information, yet the pursuer policy (1) remains undefeatable, which is non-trivial and well-motivated.

- **Computationally efficient belief mechanism**: The belief update (Eq. 7) runs in Õ(|V|) per step while the DP requires Õ(n^{m+1}) per recomputation. The concrete numbers in Section 4.2 are compelling: GPU-accelerated RL inference is <0.01 s vs. >100 s for DP on 1800-node graphs (Table 3).

- **Empirically strong zero-shot generalization**: Table 2 is striking. The R2PS-trained policy, never having seen the 10 test graphs, consistently and often decisively outperforms PSRO trained directly on those graphs across all evader types (Stay, DP_sync, DP_async). The gap against DP_async on Scotland-Yard (0.76 vs. 0.00) and Times Square (0.95 vs. 0.04) is especially impressive.

- **Belief ablation validates the mechanism**: Table 4 cleanly shows that reducing update frequency from every step to every 2–3 steps causes large success-rate drops, providing causal evidence that belief preservation is the operative ingredient and not incidental.

- **Lemma 2 provides a principled sanity check**: Showing that both PO pursuer policies (5) and (6) reduce exactly to the perfect-information policy when Pos is always a singleton cleanly anchors the partial-observability extension to the proven optimal baseline.

---

## Weaknesses

### Fatal
None.

### Major

1. **No suboptimality bound under continual partial observability.** The theoretical apparatus covers full information (Theorem 2) and the degenerate limit (Lemma 2), but there is no guarantee—not even an approximate one—for how much worse belief-averaging performs when Pos is large. The belief update (Eq. 7) assumes a uniform evader transition policy, a heuristic choice that is justified only empirically. For a paper that claims worst-case robustness, the lack of any theoretical bound on the PO performance gap is a significant omission.

2. **Incremental novelty relative to EPG.** The RL pipeline (Section 4.1) is directly inherited from Lu et al. (2025a)'s EPG framework with the belief state substituted in as input. The paper acknowledges this but does not articulate why the substitution is non-trivial beyond plugging in different inputs to the same architecture. The main novelty is the belief mechanism itself, but its individual components (Bayesian position tracking via Neighbor(Pos), HMM-style belief propagation) are individually standard in the POMDP literature.

3. **Weak comparison baseline.** The sole head-to-head baseline is PSRO, which is known to have poor cross-graph generalization—a limitation explicitly discussed by prior work. No comparison is made against POMDP-based belief-space planners, other observation-based MARL methods, or even ablations of EPG without the belief mechanism (i.e., EPG with only local observations). This makes it difficult to attribute improvements specifically to the belief mechanism vs. cross-graph training.

### Minor

1. **Worst-case robustness is overstated for harder maps.** Against BR_async (the best-responding evader trained on the RL policy), success rates fall to 0.10 (Hollywood Walk of Fame) and 0.20 (Sagrada Familia). The claim of "worst-case robustness" sits uneasily with these numbers. The paper defines robustness relative to the DP-derived opponent, not a truly worst-case adversary.

2. **Training set sensitivity is unexamined.** The model is pretrained on Dungeon maps and fine-tuned on random Google Maps urban graphs. There is no ablation on training set composition (e.g., what happens with only Dungeon maps, or only urban maps), making it unclear whether the strong generalization stems from diversity or from the graph topology overlap between random urban graphs and test locations.

3. **Fixed observation range during training.** The model is always trained with range=2. While Table 7 shows monotone improvement with larger inference-time range, training with variable ranges might yield a more robust and adaptable policy; this is not explored.

### Trivial
None worth listing.

---

## Nice-to-Haves

- A theoretical bound (even asymptotic) on the suboptimality of DP_belief relative to the full-information DP policy as |Pos| grows would substantially strengthen Section 3.2.
- An additional baseline that applies EPG/cross-graph RL without belief (using only local observation) would isolate the contribution of the belief mechanism.
- Reporting variance (standard deviation) on the success rates in Tables 2–4 would improve statistical rigor.

---

## Novel Insights

The most genuinely novel insight is that the DP distance table D, computed under synchronous moves, is simultaneously the value function for the asynchronous game where the evader observes the pursuers' actions before responding. This follows from the minimax structure of D (Lemma 1) and shows that allowing the evader to forecast pursuer moves does not change the game's strategic landscape—it merely eliminates the inner maximization in the evader's best response, which D already accounts for. This unification is elegant and practically valuable: it means a single offline computation yields optimal strategies against both synchronous and asynchronous evaders. The second genuine insight is that belief-averaged minimax (Eq. 6) outperforms worst-case minimax over Pos (Eq. 5) precisely because the latter becomes overly pessimistic when Pos is large, causing the pursuer to park at high-value "rest points" rather than advance—a behavioral characterization that is both insightful and experimentally verified.

---

## Suggestions

1. Provide a theoretical analysis (even a loose bound) on how pursuit time increases as a function of |Pos|, to give the partial observability extension stronger theoretical grounding.
2. Add at least one additional baseline: EPG-style cross-graph RL with no belief (just concatenated local observations) to show belief preservation is the decisive factor.
3. Discuss when DP_belief still fails and what structural properties of graphs (e.g., long diameter, low connectivity) make partial-observability pursuit fundamentally hard, to set honest expectations for practitioners.

---

## Score and Decision

The paper addresses a well-motivated, practically important gap (real-time pursuit under partial observability with varying graph structure), provides clean theoretical results on asynchronous optimality, a principled if heuristic belief mechanism, and strong empirical evidence of zero-shot generalization. The major weaknesses—incremental novelty over EPG, absence of PO suboptimality bounds, and limited baselines—prevent a clear accept, but the combination of contributions and the convincing experimental story clear the bar for borderline acceptance at ICLR.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>