Now I have all the calibration I need. Let me write the final review.

## Summary

This paper introduces the conditional causal bandit problem, where arms are single-node conditional interventions on a known causal graph. The authors provide a complete graphical characterization of the minimal set of nodes (mGISS) guaranteed to contain the optimal intervention node, proving it equals the LSCA closure of the parents of the reward variable (Theorem 13). They present the C4 algorithm that computes this set in O(|V|+|E|) time. Experiments on random and real-world graphs demonstrate substantial pruning, and a UCB-based bandit using mGISS shows improved cumulative regret.

## Strengths

1. **Theorem 13 (LSCA closure = mGISS)**: The central theoretical result — a complete graphical characterization of the minimal search space for conditional causal bandits — is elegant, nontrivial, and correctly proved. It cleanly generalizes the intuitions from Figure 1 into a crisp mathematical statement.

2. **Proposition 4 (conditional ↔ deterministic atomic superiority)**: Showing that conditional-intervention superiority reduces to deterministic atomic-intervention superiority is a clever simplification that makes the problem tractable. This enables reasoning with simpler deterministic interventions while maintaining relevance to the probabilistic setting — a genuine analytical insight.

3. **C4 algorithm and Theorem 16 (linear-time computation)**: The C4 algorithm runs in O(|V|+|E|) time and is both simple and clearly correct given the characterization. The connector concept (Definition 14 / Lemma 15) provides an intuitive grounding for why the algorithm works. Linear time is significant for practical applicability.

4. **Empirical pruning results**: Search space reduction experiments on both random graphs (e.g., 17% of ancestors retained for 500-node sparse graphs) and real-world bnlearn graphs (90%+ reduction for large models) convincingly demonstrate that the mGISS is often small, making the theoretical guarantee practically meaningful. The random graph results showing that sparser graphs benefit more (Table in Figure 5) are informative.

## Weaknesses

### Fatal
None.

### Major

1. **Regret experiments are underspecified.** The paper does not describe how SCM parameters (structural equations, noise distributions, reward functions) were instantiated from the bnlearn graphs for the bandit experiments. Without this information, the experiments cannot be reproduced or critically evaluated. While the paper provides a code repository, the experimental methodology should be self-contained in the manuscript. The paper states that for each dataset, the "estimated best arm" is defined as "the arm that most runs concluded to be the best at the end of training" — this is a reasonable empirical convergence heuristic but does not validate that the mGISS actually contains the theoretically optimal node under the true (unknown) SCM. Since the theory already provides an unconditional guarantee, the experiments should ideally go beyond what the theory says (e.g., by using SCMs with known ground-truth optimal interventions to verify containment, or by comparing against random pruning of equal size to show the mGISS is not merely removing arbitrary nodes).

### Minor

1. **Search space reduction experiments are purely graph-theoretic.** These experiments measure only the fraction of nodes pruned, which is informative but provides no evidence linking pruning to downstream bandit performance beyond what the theory guarantees. The paper correctly separates these from the bandit experiments, but the connection between the two could be made tighter.

2. **The Λ-structure characterization (Theorem 12) could be motivated more.** The Λ-structure definition is introduced and then immediately used in proofs, but its intuitive meaning for why it corresponds to nodes worth intervening on is only briefly mentioned. For a reader trying to build intuition, this transition is somewhat abrupt.

### Trivial
- Figure 1 caption appears twice with different formatting (parser artifact but should be deduplicated in the camera-ready version).
- Some notation overload (e.g., $\mathbf{U}$ used for both generic sets and the specific set $\mathbf{U}$ in Algorithm 1).

## Nice-to-Haves
- Provide full SCM parameterization details for the regret experiments in the main text or a dedicated appendix section.
- Include an ablation comparing mGISS-based pruning against random node pruning of equal size to confirm the mGISS retains genuinely useful nodes, not just any pruned set.
- Compare against the baseline of intervening on Pa(Y) only (the multi-node hard-intervention solution) to highlight the difference in complexity between the two settings.

## Removed Points

These points were flagged by reviewers but are not substantive weaknesses:

- **"Search space experiments do not validate that mGISS contains the optimal intervention"** — This is not a valid criticism because Theorem 13 provides an unconditional guarantee over all SCMs consistent with the graph. The experiments measure the size of the mGISS, which is a distinct and well-motivated question (how much pruning can be expected in practice). The guarantee holds regardless of what the experiments show.
- **"Faster convergence is a foregone conclusion"** — Pruning reduces the arm set, so some improvement in regret is expected. However, the paper's main claim is about *optimality* while pruning, not about faster convergence being surprising. The regret experiments illustrate a practical benefit; they do not claim to discover a non-obvious phenomenon.
- **"Missing appendix content / proofs"** — The appendix exists in the original submission; the parser strips it. This is a tool artifact, not a paper problem.
- **"Weaknesses about unfair comparison with baselines"** — The baseline (brute-force over all nodes) is the natural reference; the asymmetry favors the baseline, not the proposed method.

## Novel Insights

None beyond the paper's own contributions. The key insight — that the LSCA closure of Pa(Y) characterizes the minimal search space — is the paper's own and is genuinely novel.

## Suggestions

1. In the regret experiments, explicitly specify the SCM parameterization (structural equations and noise distributions) used to generate data from each bnlearn graph. If the parameterization is nontrivial, provide it in an appendix.
2. Add an experiment on a known SCM where the ground-truth optimal intervention node can be analytically determined, then verify that the mGISS contains it.
3. Add an ablation comparing mGISS pruning against random pruning of the same size to show that the mGISS is not merely removing nodes at random.
4. Clarify that the regret is computed relative to the empirical best arm, and discuss whether this could introduce any systematic bias between the two conditions being compared.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
| Path | Avg Score | Band | Comparison |
|------|-----------|------|------------|
| fSxiromxAq.md (Sparse Causal Model) | 3.00 | Low | Significantly weaker — vague methodology, no clear theoretical contribution |
| TRHyAnInUC.md (D³PM) | 3.25 | Low | Weaker — unrelated causal discovery paper with instability issues |
| MVpvyeVeyI.md (Causal Bayesian Optimization Unknown Graphs) | 3.40 | Low | Weaker — unclear framing, limited contribution |
| AvXrppAS2o.md (Improved outcome prediction) | 3.00 | Low | Much weaker — no theory |
| 2pEqXce0um.md (Root Cause Analysis) | 4.50 | Mid | Less novel — applies existing ideas to root cause analysis |
| IPayPEGwdE.md (Learning Good Interventions) | 5.00 | Mid | Similar weaknesses in experiments but weaker theory (simple chain graphs) |
| ZXs3pkmrRG.md (Test-Time Learning) | 5.50 | Mid | Comparable — solid experimental methodology, but less clean theoretical contribution |
| u63OVngeSp.md (Deriving Causal Order) | 7.00 | Mid | Stronger — cleaner theory + better experiments, accepted |
| xByvdb3DCm.md (Selection meets Intervention) | 8.00 | High | Stronger — broader impact, complete experimental validation |
| 3cuJwmPxXj.md (Identifying Representations) | 8.00 | High | Stronger — rigorous exposition across theory and experiments |
| A3YUPeJTNR.md (Hidden Cost of Waiting) | 8.00 | High | Stronger — complete, polished paper with clean story |
| 8BAkNCqpGW.md (Policy Gradient for POMDPs) | 8.00 | High | Stronger — theoretical depth with practical algorithms |

**Initial bracket (Round 1):** Between 4.5 and 7.0.

**Round 2 — Narrowing:**
| Path | Avg Score | Comparison |
|------|-----------|------------|
| IPayPEGwdE.md (Learning Good Interventions) | 5.00 | Inferior to this paper — weaker theory (simple chain graphs), both have experimental gaps |
| YcW8i9VCf5.md (Adversarial Causal BO) | 6.00 | Comparable — clean problem statement, decent theory, accepted despite some framing issues |
| pOoKI3ouv1.md (Robust agents learn causal world models) | 5.75 | Different type of contribution (theoretical result about representation learning) |
| fcl6WeMARK.md (Graph Feedback Bandits) | 4.33 | Weaker — incremental improvements, less novel |
| 8muemqlnG3.md (Causal Discovery via BO) | 6.50 | Slightly stronger — good empirical validation but accepted |
| mGmx41FTTy.md (Two Time-Slices) | 6.33 | Similar score — decent theory but rejected due to experimental limitations |
| 9UGAUQjibp.md (Quantized Local Independence) | 5.80 | Weaker — more applied RL setting, less clean theory |

**Final bracket (Round 2):** After narrowing, the paper sits between the 6.0 anchor (Adversarial Causal BO, which was accepted) and the 6.5-7.0 level. The theory here is cleaner and more self-contained than the 6.0 anchor. The main limitation is the experimental section's underspecification, which is addressable in revision. The paper's theoretical contribution is genuinely novel and correct, placing it above the "clear reject" range.

### Score

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>