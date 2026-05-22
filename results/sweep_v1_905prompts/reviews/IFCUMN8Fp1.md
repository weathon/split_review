Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes a spectral algorithm that learns POMDP parameters (transition and observation matrices, number of states) from a single action-observation trajectory by connecting Predictive State Representations (PSRs) to tensor decomposition methods. The key theoretical extension is the ability to handle POMDPs where multiple states share observation distributions across all actions, recovering model parameters up to a *full-rank observability partition* via joint diagonalization of all full-rank action-observation matrices. Experiments on small POMDPs (2–4 states) suggest the learned models match PSR planning performance, and the explicit likelihoods enable reward specification that black-box PSRs cannot support.

## Strengths

- **Theorem 1 provides formal guarantees for recovery up to the full-rank observability partition**: The theorem states that the algorithm recovers transition and observation likelihoods summing over states within each partition set, which is the first spectral guarantee that explicitly handles POMDPs where multiple states share observation distributions across all full-rank actions. This is a genuine theoretical extension of prior tensor decomposition work (Azizzadenesheli et al., 2016; Guo et al., 2016).

- **Joint diagonalization over *all* full-rank actions (Lemma 1, Equation 18) rather than per-action**: The method uses a single weighted sum of matrices over all full-rank actions and observations, which distinguishes it from prior approaches that process each action independently. This enables recovery even when no single action has unique observation distributions — only the aggregate across actions must be unique.

- **Concrete algorithmic handling of nontrivial observability partitions (Section 4.3)**: The paper introduces a preprocessing step with a random block-diagonal rotation matrix and rescaling to ensure the final transform satisfies Theorem 1's likelihood sums. This is a concrete solution for POMDPs where states are indistinguishable in their observation probabilities — a class prior tensor methods could not handle.

- **Reward specification experiments demonstrate a practical advantage over PSRs (Figure 4)**: In the noisy hallway domain, specifying rewards based on state properties (only possible with explicit observation/transition matrices) enables the planner to reach the goal, while observation-based reward specification (the only option with black-box PSRs) fails. This directly supports the paper's claim that explicit likelihoods enable task specification that is impossible with PSRs alone.

## Weaknesses

### Major

- **Experimental scale is limited to 2–4 state POMDPs, far below convincing demonstration**: Every experiment uses POMDPs with at most 4 states (Tiger: 2, T-Maze: 4, Sense-Float-Reset: 3/4, hallway domains: 3). The paper motivates the problem with furniture having hidden locking mechanisms and robot manipulation, but provides no evidence the method works beyond trivial toy domains. As state count grows, the SVD truncation and joint diagonalization steps become increasingly ill-conditioned. While the paper acknowledges scaling as future work, the gap between the motivating examples and the demonstrated scale is significant.

- **No sensitivity analysis for the critical full-rank action detection threshold**: Section 4.2 states that full-rank actions "can easily be determined by a threshold test on the singular value decomposition on all matrices M^a," but provides:
  - No analysis of how this threshold should be set
  - No experiments showing sensitivity to misclassification
  - No evaluation on POMDPs where some actions are *close* to singular but not exactly
  The tested POMDPs have obviously full-rank or obviously singular actions, so this step is never stressed. In practice, finite-sample estimates will never be exactly singular, and the threshold choice directly determines which observation matrices are used for joint diagonalization. This is a significant gap in the empirical validation.

### Minor

- **EM baseline is under-specified**: The paper states EM is given "a number of states determined by the number of components of the truncated SVD when learning a linear PSR" but does not report whether multiple random restarts were used, how EM was initialized, or the number of EM iterations. Given that EM is notoriously initialization-sensitive and the proposed method consistently outperforms it, the reader cannot determine whether EM was run in a reasonable configuration or deliberately suboptimal.

- **No pseudocode for the multi-step algorithm**: The algorithm in Section 4 has several interdependent steps (rank factorization, identifying full-rank actions via threshold, eigendecomposition of random weighted sum, block-diagonal rotation, renormalization) but is described only in prose. An algorithmic listing would significantly aid reproducibility and clarity.

- **Large error bars obscure convergence in some plots**: In Figure 3, several data points (e.g., T-Maze observation error at 10^6 interactions) show error bars spanning a substantial fraction of the y-axis range. For the proposed method, variance at intermediate data amounts is large enough that it is unclear whether the method has reliably converged or whether the mean estimate is driven by a subset of seeds. This variance is not discussed.

- **Reward-specification results require 10^7 interactions to converge**: The "Ours_state" method's reward in the noisy hallway converges only after ~10^7 interactions (Figure 4), an order of magnitude more data than needed for basic model learning (10^6 in Figure 3). The practical advantage of state-based reward specification over the simpler observation-based method is thus marginal and only emerges after very large amounts of data.

### Trivial

- The notation in Equation 7 flips between $T^{ao}$ and $T^a$ inconsistently — the text should clarify that $T^{ao}$ means $O^{ao}T^a$.

## Nice-to-Haves

- A discussion of failure modes: what happens when the SVD rank estimate does not equal the true number of states, or when the ergodicity assumption is violated?
- Runtime/wall-clock comparisons between the spectral method and EM on the tested domains.
- Add an experiment on a moderately-sized POMDP (e.g., 8–10 states with a nontrivial observability partition) to show that the joint diagonalization and block-diagonal recovery steps work beyond the smallest cases.

## Removed Points

- **Criticism about Section 4.1.1 oversimplifying full-rank claims**: The paper's claim about $p_{succ}T + (1-p_{succ})I$ being full-rank is referenced to Appendix A.6 (stripped from the extracted text). The proof exists in the appendix. The critic's specific concern about different failure models is a scope issue — the paper describes one particular modeling choice.
- **Criticism about reward-specification requiring a priori knowledge**: The paper describes computing entropy from the *learned* observation matrices, not using a priori knowledge. The critic misread this section.
- **Criticism about missing error bars in Figure 4**: The figure caption explicitly states "Error bars report standard deviation over 100 seeds." Error bars are present.
- **Criticism about "rewards as observations" not being justified**: The paper cites Izadi & Precup (2008) for this technique. The reference addresses the concern.
- Pure formatting nitpicks, claims about missing appendix proofs, and speculation about unreleased artifacts.
- **Strength about planning performance matching PSR baseline (Figure 3, Row 4)**: Retained as a genuine strength; however, the overlap between methods does not establish *advantage* over PSRs, only parity, which is consistent with the paper's claims.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add at least one experiment on a moderately-sized POMDP (8–10 states) with a nontrivial observability partition to demonstrate that the joint diagonalization and block-diagonal recovery steps work beyond the smallest cases.
2. Perform a sensitivity analysis on the full-rank detection threshold — show what happens when the threshold is set too high or too low.
3. Run EM with 10–20 random restarts, report the best run per seed, and provide initialization details, so the EM comparison is fair.
4. Provide a pseudocode algorithm block for the procedure in Section 4 to improve reproducibility.
5. Discuss the high variance observed in some Figure 3 data points and whether it reflects instability in the algorithm or the evaluation protocol.

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| B5kAfAC7hO (Provable Representation POMDP RL) | 5.33 | R1/R2 | Theory-heavy POMDP RL paper, rejected for limited novelty. This paper has stronger originality but weaker experiments. Slightly weaker overall. |
| KrtGfTGaGe (Wasserstein Believer) | 4.50 | R1/R2 | Accepted despite score, but relied on a strong assumption (latent observability during training). This paper avoids that assumption and has cleaner theory. |
| GvsCOOPxoI (Provable Learning DEC-POMDP) | 6.17 | R1/R2 | Substantial theory with no experiments. Rejected for presentation issues. This paper has better presentation but less ambitious theory. |
| Qja5s0K3VX (OPE in POMDPs) | 6.00 | R2 | Accepted with solid theory and no experiments. This paper has experiments and comparable theory quality but weaker rigor. |
| Q00CO1Tm6M (POMDP Hardness/Tractability) | 5.75 | R2 | Rejected for writing quality. This paper is better written. |
| sEv6vHIUnu (Structured Predictive Repr.) | 4.80 | R2 | GNN-based PSR paper, rejected for limited novelty. This paper has stronger theory novelty. |

**Round-1 bracket**: between 3.5 (weak anchors) and 8.0 (strong anchors).

**Round-2 narrowing**: The paper sits between the 5.33 anchor (weaker theory novelty, rejected) and the 5.75–6.00 anchors (stronger theory, weaker experiments or writing). The paper's theoretical contribution is genuinely novel, but the experimental validation is too limited for its claims.

**Final score**: 5.0. The paper has a clear theoretical contribution and is well-written, but the empirical validation is insufficient — the experiments are on tiny POMDPs (2–4 states), the critical threshold detection is unanalyzed, and the EM baseline is under-specified. These gaps prevent the paper from being accepted in its current form but the theoretical framing has genuine promise.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>