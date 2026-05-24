Now I have enough context to write the final review.

Let me summarize my calibration:

**Round 1 bracket:** Between 4.5 and 7.0 (wider bracket to start)

**Round 2 anchors I examined in full:**
- Symb4CO (6.67) — stronger paper, cleaner theory, accepted. TreeDQN is weaker.
- L2P-MIP (6.50) — stronger paper, novel research direction. TreeDQN is weaker.
- RDC-SAT (5.75, accepted poster) — similar A+B style, similar concerns about marginal gains. TreeDQN is comparable or slightly weaker due to flawed theoretical proof.
- Node Selection paper (3.75, reject) — weaker evaluation. TreeDQN is significantly stronger.
- Branches (4.75, reject) — different domain but similar quality issues.

The paper sits at approximately 5.0–5.5: has genuine contributions and solid experiments, but the flawed contraction proof and modest empirical gains relative to simpler baselines hold it back.

---

## Summary

This paper proposes TreeDQN, which adapts DQN (a standard off-policy RL algorithm) to the tree Markov Decision Process (tree MDP) framework for learning branching heuristics in Branch-and-Bound MILP solving. The two main technical contributions are: (1) a claimed contraction-in-mean proof for the tree Bellman operator, intended to justify using DQN-style TD updates in the tree setting, and (2) a mean squared logarithmic error (MSLE) loss that targets the geometric mean of the return and stabilizes training under high-variance tree-size distributions. The method is evaluated on five NP-hard MILP benchmarks (Combinatorial Auction, Set Cover, Maximum Independent Set, Facility Location, Multiple Knapsack) and compared against prior RL methods (FMCTS, tmdp+DFS), Imitation Learning, and Strong Branching.

## Strengths

- **Clear empirical improvements over prior RL methods.** Table 3 shows that TreeDQN achieves lower geometric-mean tree sizes than both FMCTS and tmdp+DFS on all five test tasks (e.g., Set Cover: 56 vs 76 vs 204; Maximum Independent Set: 42 vs 96 vs 88). Table 2 further shows substantially fewer training episodes to reach the best checkpoint (e.g., Comb.Auct: 700 episodes vs tmdp+DFS's 22,500). These results directly support the paper's core claim of "less training data and smaller trees compared to previous reinforcement learning methods."

- **The MSLE loss is well-motivated and empirically supported.** The paper correctly identifies that geometric mean is the appropriate aggregation metric for long-tailed tree-size distributions, and the MSLE loss directly optimizes for this. Table 6 shows that TreeDQN with MSLE achieves lower geometric-mean tree sizes than the MSE variant on all five tasks (e.g., Mult.Knap: 290 vs 367), with statistical significance on three tasks. Figure 5 additionally shows that MSLE produces lower and less volatile loss curves during training, supporting the claim of stabilized learning.

- **Thorough evaluation with statistical rigor.** The paper uses Wilcoxon paired tests throughout (Tables 4, 6), provides P-P plots for distributional analysis (Fig. 4), reports both geometric means and standard deviations, includes a transfer/generalization study (Table 5), and provides an ablation study. Code is provided. This level of evaluation is above the standard for this area.

- **Multiple Knapsack result is a clear win.** On this task, TreeDQN achieves tree size 290 — substantially better than IL (670), Strong Branching (700), FMCTS (299), and tmdp+DFS (308) — while also being much faster than IL (1.54s vs 7.90s). This demonstrates that the RL approach can discover genuinely better heuristics in some domains.

## Weaknesses

### Fatal

None.

### Major

- **The contraction-in-mean proof (Theorem 4.1) is not valid as stated.** The derivation arrives at the bound ||TV−TU||_∞ ≤ γ(p^+ + p^-)||V−U||_∞ and then computes E(p^+ + p^-) = (N−1)/N < 1 by noting that in a realized tree of N nodes there are N−1 edges. This is a deterministic graph-theoretic identity that applies *after* the tree is fully realized — it is not a probabilistic expectation over the MDP's state-action visitation distribution. The quantity (p^+ + p^-) is state-dependent (it can be 0, 1, or 2 at any given node), and averaging it over nodes of a completed tree does not establish the required contraction property for the Bellman operator on the underlying state space. The assumption that p^+, p^- are state-independent is also inconsistent with the B&B pruning process they are meant to model, as the paper itself acknowledges that pruning depends on the global upper bound which changes through the tree. **This does not invalidate the empirical results** — DQN has been applied successfully in many settings without formal convergence guarantees — but it makes the theoretical motivation that the paper prominently advertises (abstract, introduction, Section 4.1) unsupported. The paper should either provide a correct proof or drop the theoretical claim and present the method as a heuristic adaptation of DQN.

- **The comparison framing overstates the method's advantage.** The abstract claims "smaller trees" and the paper repeatedly emphasizes improvement over "prior RL methods," which is true. However, Tables 3 and 4 show that Imitation Learning — a much simpler supervised approach — achieves comparable or better geometric-mean tree sizes on 4 of 5 tasks (Comb.Auct: 56 vs 58, Set Cover: 53 vs 56, Max.Ind.Set: 42 vs 42, Facility Loc.: 323 vs 324) with similar or faster execution times. Strong Branching also outperforms TreeDQN on those same tasks. Only on Multiple Knapsack does TreeDQN clearly dominate both IL and SB. The paper should more prominently qualify the scope of its improvements and discuss when/why a practitioner would choose the more complex RL approach over IL.

### Minor

- **The MSLE loss benefit is inconsistent across tasks.** The Wilcoxon test in Table 6 shows that MSLE is statistically significantly better than MSE on only 3 of 5 tasks; for Facility Location (p = 0.115) and Multiple Knapsack (p = 0.052, borderline), the null hypothesis cannot be rejected at conventional levels. While the paper accurately reports this, the "crucial" role of MSLE is weakened.

- **Transfer results are mixed.** Table 5 shows TreeDQN underperforms FMCTS on Comb.Auct (1567 vs 1375) and underperforms tmdp+DFS on Max.Ind.Set (4541 vs 1713). The paper acknowledges this but does not deeply analyze why the transfer fails in these cases, limiting understanding of the method's generalization properties.

### Trivial

- The contraction proof inadvertently drops γ from the bound when transitioning from Equations (3)-(4) to the final claim (line 110 writes ||TV−TU||_∞ = (p^+ + p^-)·||V−U||_∞ without the discount factor γ that appears in the derivation). This is a minor notational inconsistency.

## Nice-to-Haves

- A direct analysis of how much performance changes when switching from DFS (training node selection) to SCIP default (testing node selection). The paper acknowledges the gap but does not quantify it.
- Confidence intervals on geometric means in Table 3 (bootstrapped) would be more informative than geometric std alone.
- Clarification of the discount factor γ used and its interaction with the tree MDP formulation.
- A discussion of the number of random seeds — 5 is reasonable but on the lower end.

## Removed Points

- *"Strong Branching and IL produce smaller trees"* — Removed as a criticism of the paper's stated claims. The paper explicitly says "previous reinforcement learning methods" in its abstract-level claim, and Tables 3-4 accurately report IL/SB performance without overstating. This information is properly scoped.
- *"The loss function ablation shows inconsistent benefits"* — Downgraded to Minor. The paper accurately reports the p-values, and the MSLE still achieves numerically better geometric means on all five tasks. The claim is not overstated.
- *"The assumption contradicts reality of B&B"* — The paper explicitly acknowledges this is an assumption and says it is "close to" the pruning process. It is clearly stated as a simplifying assumption for the theoretical model, not a factual claim about B&B.
- *"Execution time improvement is modest"* — Execution times in Table 4 show clear improvements over FMCTS and tmdp+DFS. The comparison with IL is approximately equal on most tasks.
- *Missing related works* — Removed per instructions; I cannot verify existence of unmentioned works.
- *Formatting/style nitpicks* — Removed as parser artifacts or non-substantive.
- Strength Finder's generic strengths about "addressing an important problem" — Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The combination of the two review inputs surfaces no genuinely novel observation that the paper itself does not make.

## Suggestions

1. **Fix or remove the contraction proof.** This is the paper's clearest vulnerability. The empirical work is strong enough to stand without a formal convergence guarantee. Consider presenting TreeDQN as a heuristic adaptation of DQN to the tree MDP setting, with the MSLE loss as the main methodological contribution.
2. **Add a dedicated discussion section that contextualizes TreeDQN against IL and Strong Branching.** Acknowledge that IL matches TreeDQN on most tasks at lower complexity, and explain the specific scenarios (e.g., Multiple Knapsack) where the RL approach provides clear benefits. This would strengthen rather than weaken the paper by demonstrating honest intellectual framing.
3. **Provide a more detailed analysis of the DFS-to-SCIP node selection gap.** This would help readers understand the practical implications of the training/inference mismatch.
4. **Investigate why transfer fails on Comb.Auct and Max.Ind.Set** — this could yield insights into the method's limitations and scope.

## Score and Decision

**Round 1 bracket:** 4.5–7.0

**Anchor comparison:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| /home/wg25r/review_agent/human_reviews/jKhNBulNMh.md (Symb4CO) | 6.67 | 2 | Stronger paper — cleaner theory, no flawed proof, accepted. TreeDQN is weaker. |
| /home/wg25r/review_agent/human_reviews/McfYbKnpT8.md (L2P-MIP) | 6.50 | 2 | Stronger — novel research direction, strong results. TreeDQN is weaker. |
| /home/wg25r/review_agent/human_reviews/uUsL07BsMA.md (RDC-SAT) | 5.75 | 2 | Similar quality — A+B approach, marginal gains over baselines. TreeDQN comparable or slightly weaker due to flawed proof. |
| /home/wg25r/review_agent/human_reviews/mMh4W72Hhe.md (Bound Implication) | 6.00 | 2 | Different domain (NN verification), cleaner execution. TreeDQN slightly weaker. |
| /home/wg25r/review_agent/human_reviews/Mw16Akb1CR.md (Branches) | 4.75 | 1 | Different domain (decision trees). Similar issues with theoretical framing. |
| /home/wg25r/review_agent/human_reviews/f3UIvWeAKs.md (Node Selection) | 3.75 | 1 | Much weaker evaluation. TreeDQN is substantially stronger. |
| /home/wg25r/review_agent/human_reviews/ghk8lnOYRq.md (k-HC) | 5.00 | 2 | Different problem (hyperplane clustering). Comparable quality. |
| /home/wg25r/review_agent/human_reviews/psDvcWtFdE.md (DIG-MILP) | 3.00 | 1 | Much weaker. TreeDQN substantially stronger. |
| /home/wg25r/review_agent/human_reviews/RAdBtquPiI.md (BOO) | 3.40 | 1 | Unrelated topic, lower quality. |

**Narrowed position:** The paper is weaker than Symb4CO (6.67) and L2P-MIP (6.50) but stronger than the reject papers (3.0–4.75). It is comparable to or slightly weaker than RDC-SAT (5.75, accepted) due to the flawed contraction proof. The empirical contributions (MSLE loss, DQN-for-tree-MDP, solid benchmarks) are genuine but marred by an invalid theoretical claim that the paper prominently features.

**Final score: 5.5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>