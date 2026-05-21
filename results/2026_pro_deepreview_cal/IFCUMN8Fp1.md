Now I have enough context to write the review. Let me compile everything.

---

## Summary

This paper proposes a spectral method for learning discrete POMDP parameters (transitions, observations) from a single trajectory collected under uniform exploration. The core idea is to first learn a Predictive State Representation (PSR) via Hankel matrix decomposition, then apply a joint tensor-diagonalization step over all full-rank actions using random weighted sums to estimate the similarity transform linking the PSR factors back to the original POMDP basis. When states share observation distributions across all full-rank actions, the method recovers transitions only up to an observability partition, with a post-processing step yielding partition-level belief sums. Experiments on small POMDPs (2–4 states) show convergence toward ground-truth parameters and planning performance on par with PSRs, plus a post-hoc reward-specification advantage.

## Strengths

- **Novel algorithmic bridge between PSRs and tensor decompositions.** The paper connects two previously separate lines of spectral POMDP learning by reformulating tensor decomposition methods to operate on PSR matrices via joint diagonalization with random weighted sums (Section 4.2). This allows simultaneous use of observation distributions from all full-rank actions rather than relying on per-action uniqueness, which prior tensor methods require. Lemma 1 formalizes the eigenvalue separation condition.

- **Clear theoretical framing with Theorem 1.** The paper states a formal guarantee (Theorem 1, Section 4.1) that the recovered matrices yield correct partition-level likelihood sums — the entries must be summed over observability-partition indices to obtain proper probabilities. This is a non-trivial extension of the Carlyle & Paz / Balle et al. result connecting PSRs to the original POMDP basis.

- **Practical demonstration of post-hoc reward specification.** Figure 4 shows a genuinely useful capability: after learning the POMDP, the agent can assign rewards to inferred states (not just action-observation pairs) to elicit desired planner behavior. In the noisy hallway domain, state-based reward assignment succeeds where observation-based assignment fails because the observation distributions are ambiguous. This capability is unavailable with black-box PSRs.

- **Well-motivated assumptions.** Section 4.1.1 provides concrete motivation for the full-rank action and ergodicity assumptions in the context of robot manipulation (failure-prone actions with self-transitions, sensing actions that break periodicity), grounding the theoretical framework in a plausible real-world setting.

## Weaknesses

### Fatal

None.

### Major

- **Very limited empirical scale (2–4 states).** All experiments use toy POMDPs: Tiger (2 states), T-Maze, Sense-Float-Reset (3 and 4 states), and two custom 3-state hallway domains. While these serve as proof-of-concept, they do not demonstrate that the method works at even modestly larger scales (e.g., 5–10 states). This severely limits the significance of the empirical contribution. The paper acknowledges this limitation in Section 7 but does not address it experimentally.

- **No comparison with existing tensor-based POMDP methods.** The paper explicitly positions itself as improving upon Azizzadenesheli et al. (2016) and Guo et al. (2016) by relaxing the per-action observation-uniqueness assumption. Yet the experiments only compare against EM and PSRs, never against those tensor methods. On Tiger (where observations are unique per action), the paper should show at least parity with those methods. On domains where the paper claims an advantage (shared observation distributions), it should demonstrate that prior tensor methods fail while the proposed method succeeds. Without such comparisons, the claimed improvement remains unvalidated.

### Minor

- **Section 4.3 post-processing exposition is too abbreviated.** The derivation of the final similarity transform (the block-diagonal rotation and the $\operatorname{diag}(RP'^{-1}m_\infty)RP'^{-1}$ construction) is covered in roughly four sentences in the main paper, with the proof deferred to Appendix A.5. The intuition about transforming the final vector back to 1 is mentioned but the connection to the partition-level sum guarantees of Theorem 1 is not fully spelled out. A brief proof sketch in the main text would substantially improve readability and confidence in the method's correctness.

- **No discussion of finite-data sensitivity for the $M^a$ inversion.** The algorithm inverts $M^a$ (Equation 17) for full-rank actions. When $M^a$ is estimated from finite data, near-singularity is a practical concern. The paper does not discuss regularization strategies, threshold selection for determining full-rankness, or how inversion error propagates through the subsequent steps. This omission makes it hard to assess real-world feasibility.

- **Transition error curves are truncated when the state count is misestimated.** In Figure 3 Row 3, transition errors are only reported when the estimated number of states matches ground truth. This truncation means the reader cannot see how transition error behaves during the most challenging regime (when the state count is wrong), giving an incomplete picture of the method's practical performance.

### Trivial

- The experiments would benefit from standard deviations on the observation and transition error curves (Figure 3 Rows 2–3), not only on the reward curves.
- The heuristic for selecting the "middle state" in the reward-specification experiments (maximizing sum of entropies of observation distributions) is domain-specific and could use brief justification.

## Nice-to-Haves

- A heuristic discussion of how error in the $M^a$ inversion propagates through the joint diagonalization would improve the paper's practical grounding, even without a full finite-sample analysis.
- Demonstrating the method on at least one domain with 5–8 states and a non-trivial observability partition would substantially strengthen the empirical evidence.
- A comparison with per-action tensor methods (Azizzadenesheli et al., 2016) on a domain where observations are unique per action, to validate that the proposed joint diagonalization at least matches prior work in the regime where both apply.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic: The post-processing theoretical guarantee is unsubstantiated ("hand-wavy"), raising doubts about correctness.** REMOVED — the paper explicitly states "see Appendix A.5 for proof of correctness" (line 228). The appendix was stripped by the parser; speculating about its contents is not valid. The main-text exposition is thin (kept as a Minor weakness above), but this does not mean the proof is absent or incorrect.

- **Harsh critic: The hallway domains use deterministic "stay" (identity) as the full-rank action, which doesn't match the failure-prone action motivation.** REMOVED — Section 4.1.1 describes failure-prone actions as one way to achieve full-rank transitions, not the only way. A deterministic stay action with an identity transition matrix is full-rank by definition and is perfectly consistent with the method's requirements. The motivation section is illustrative, not prescriptive.

- **Harsh critic: "no standard deviations on the error curves (only on reward)."** PARTIALLY REMOVED — the figure caption states "Error bars represent standard deviation over 100 seeds." However, inspecting Figure 3's description, it's ambiguous whether error bars appear on all rows or only Row 4. Moved to Trivial as a clarification suggestion rather than a substantive weakness.

- **Harsh critic: The claim about deep-learning belief-state learners is "too strong."** REMOVED — the paper's characterization (line 332-333: "Like PSRs, the representation of the hidden state learned by these models is [opaque], and cannot readily provide likelihood models for probabilistic inference") is reasonable. RNN hidden states are not interpretable as explicit transition/observation matrices, which is the key distinction the paper draws.

- **Strength Finder: "Clear problem formalization and assumption justification" as a standalone strength.** DEMOTED — this is correct but generic. The assumption justification in 4.1.1 is good but not a core contribution; it supports the main strengths.

- **Harsh critic: "The paper does not discuss what happens when the full-rank action set is empty."** DEMOTED to Nice-to-Have — the paper explicitly states this as a requirement/assumption. Criticizing a method for not working when its stated assumptions are violated is scope creep. The paper acknowledges that it restricts the class of learnable POMDPs.

## Novel Insights

The paper's reformulation of tensor decomposition methods to operate on PSR matrices — specifically, computing $M^{ao} \cdot M^{a-1}$ to isolate observation matrices and then applying random-weighted joint diagonalization across all full-rank actions — is a clean synthesis that had not been articulated before. It reveals that the "per-action uniqueness" assumption in prior tensor methods can be relaxed to "uniqueness across the aggregated observation distributions of all full-rank actions," which is a meaningfully weaker condition. The observation that the resulting ambiguity is block-diagonal with blocks corresponding to the full-rank observability partition is also a useful structural insight.

## Suggestions

- Add a brief proof sketch for the post-processing step (Section 4.3) in the main paper rather than deferring entirely to the appendix. Even 3–4 lines showing why $\operatorname{diag}(RP'^{-1}m_\infty)RP'^{-1}$ restores the partition-level sum property would greatly improve readability.
- Include at least one experiment comparing against a per-action tensor method (Azizzadenesheli et al., 2016) on Tiger, where both methods should succeed, to establish a baseline.
- Discuss a simple regularization strategy (e.g., pseudoinverse with a small ridge term) for the $M^a$ inversion when estimated from finite data.

## Score and Decision

**Anchor comparison:**

| Paper | Score | Round | Comparison |
|-------|-------|-------|------------|
| Stochastic Safe Action Model Learning | 3.00 | R1 | Much weaker — different problem, limited novelty |
| Structured World Models From Low-Level Observations | 3.00 | R1 | Weaker — less formal theory, comparable empirical scale |
| Provable Representation with Efficient Planning for POMDP | 5.33 | R1/R2 | Stronger — has sample complexity analysis, more benchmarks, but less algorithmic novelty |
| Proto Successor Measure | 6.75 | R1 | Much stronger — deeper theory, more polished |
| The Wasserstein Believer | 4.50 | R2 | Comparable — novel POMDP learning method, some theory, limited experiments |
| HAL: Harmonic Learning | 4.50 | R2 | Comparable in contribution level |
| Value-Biased MLE | 4.25 | R2 | Slightly weaker — more incremental |
| Theoretical Hardness and Tractability of POMDPs | 5.75 | R2 | Stronger — rigorous theory paper with well-developed results |

**Bracket from Round 1:** 4.0–6.5, narrowed to 4.0–5.5 based on anchor comparisons.

**Round 2 narrowing:** The paper is clearly weaker than the 5.75 and 5.33 anchors (which have stronger theory and/or broader evaluation) and comparable to the 4.50 Wasserstein Believer, which also has a novel POMDP-learning idea with limited experiments. The current paper's algorithmic contribution is arguably more original than the Wasserstein Believer, but its empirical validation is weaker (no standard benchmarks, no comparison to prior tensor methods). 

**Final assessment:** The paper makes a genuine contribution — the algorithmic connection between PSRs and tensor decompositions is novel and potentially useful. Theorem 1 provides a clear theoretical foundation. However, the experimental validation is too limited in scale and scope to convince at an ICLR level; the absence of comparisons with the tensor methods the paper claims to improve upon is a significant gap. The paper is closer to a workshop contribution that needs scaling up than a mature conference paper. **Score: 4.5, Reject.**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>