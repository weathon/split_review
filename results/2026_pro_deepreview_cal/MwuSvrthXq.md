Now I have sufficient calibration. Let me now write the consolidated review.

---

## Summary

This paper presents WeCAN, an RL framework for heterogeneous DAG scheduling with task-resource compatibility. The key innovations are: (1) a weighted cross-attention (WeCA) layer that multiplies compatibility coefficients *outside* the softmax, enabling the architecture to adapt to variable numbers of resource pools and distinguish tasks with different compatibility profiles; (2) an LDDGNN that uses longest-directed-distance biases for encoding DAG dependencies; and (3) a skip-action mechanism integrated into single-pass inference to mitigate the optimality gap inherent in list scheduling. The empirical evaluation on TPC-H and Computation Graphs datasets shows meaningful improvements over both heuristic and neural baselines, with thorough ablation studies.

## Strengths

- **Weighted cross-attention design is well-motivated and empirically validated**: The outside-softmax placement of compatibility coefficients (Equation 3) is carefully justified — the paper's example of two tasks with identical attributes but different compatibility profiles correctly demonstrates that the outside placement distinguishes them while the inside (log-bias) placement does not. The ablation (Table 3) confirms this: replacing WeCA with the inside version degrades makespan by 3.5–5 percentage points on TPC-H-30/50.

- **Skip-action mechanism with theoretical grounding**: The paper proves (Theorems 1 and 2) that standard list scheduling can exclude optimal solutions and develops a dynamic skip score that enables surjectivity within single-pass inference. The empirical validation (Figure 3) shows 4–9% improvement on heavy-task variants, confirming the mechanism matters in practice.

- **Consistent empirical gains across diverse benchmarks**: WeCAN-S(256) achieves 7.7% relative improvement over the best neural baseline (One-Shot) on TPC-H-50 and 9.5% on Computation Graphs, while maintaining inference times (4.39 s) competitive with heuristics. The performance holds across Erdős-Rényi, Layer, and Stochastic Block graphs (Table 2).

- **Robust generalization to unseen environments**: Figure 2 demonstrates that WeCAN maintains 6.7–20.4% improvement over heuristics when tested on environments with more pools, pool types, tasks, or task types than seen during training, substantially outperforming One-Shot's generalization.

- **Thorough ablation studies**: Table 3 isolates contributions of WeCA layers, their placement, and LDDGNN versus standard GAT variants. The degradation when components are removed or altered is clear and consistent.

## Weaknesses

### Fatal

None.

### Major

- **Insufficient description of how baselines were adapted to heterogeneous compatibility constraints**: The paper compares against heuristics (CP, SFT, MOPNR, Tetris, HEFT) and neural methods (PPO-BiHyb, One-Shot) that were originally designed for settings without arbitrary compatibility coefficients. The main text mentions only that "for the 4 list scheduling algorithms, we apply three pool-selection rules and select the one with the best makespan" (line 222), without specifying what those rules are or how compatibility coefficients K_acc enter each baseline's decision-making. For One-Shot — which the paper itself notes "does not consider compatibility coefficients" — it is unclear how the method was extended to produce the results in Tables 1–2. Without this information, the reader cannot evaluate whether reported gains stem from architectural superiority or from baselines not having equivalent access to compatibility information.

- **Theory-empirical gap weakens the optimality-gap claims**: Theorem 1(iv) proves that there *exists* a set of scores such that greedy selection yields an optimal schedule. This is a representation/expressivity result, not a learning guarantee. The training uses REINFORCE with sampling, and there is no empirical analysis (e.g., comparison against MILP optimal solutions on small instances) showing the learned policy ever approaches such scores. The paper's language about "closing the gap" and "fixing" the optimality gap overstates what is actually demonstrated. The skip mechanism expands representational capacity, but whether RL training reliably finds policies that exploit this capacity is not established.

### Minor

- **Overstatement of novelty regarding the list-scheduling optimality gap**: The abstract claims the analysis "reveal[s] their inability to guarantee optimal solutions" — this is standard knowledge for list scheduling. What is novel is the formalization within the paper's reduced-space framework and the construction of the skip-action surjection, but the framing overstates the analytical novelty.

- **Skip score functional form is not justified**: The skip score $u_{\pi_{skip}} = u_a(1 - k/2n)^{u_b} + u_c$ (line 148) uses a power-law decay without motivation. Why this form rather than alternatives (e.g., a learned MLP over step index, or a simpler linear decay)? An ablation or brief justification would strengthen the design rationale.

- **Test set diversity is unclear**: The reported standard deviations are very small (e.g., ±10 on a makespan of ~19,000 for TPC-H-30, Table 1), which could indicate the test set has limited diversity (e.g., fixed problem instances). The paper should clarify whether test DAG structures and compatibility matrices are unseen.

### Trivial

None beyond what are clearly parser artifacts in the review copy.

## Nice-to-Haves

- Connecting theory to practice more directly: reporting how often the learned greedy policy recovers the optimal schedule on small instances where MILP can be solved exactly would give the theoretical discussion empirical bite.
- Providing a more detailed account of how each baseline uses compatibility coefficients would transform a potential fairness concern into a strength.
- Justifying or ablating the functional form of the skip score.
- Clarifying whether the non-autoregressive decoder's speed-accuracy trade-off is favorable compared to an autoregressive alternative.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Misleading justification for the outside placement of compatibility coefficients" (Harsh Critic Issue 1)**: This criticism is factually incorrect. In the paper's example (two pools with identical capacity, two tasks with same attributes, v1 compatible with one pool, v2 with both), the outside placement produces $g_{v1} = f_v + 0.5p/\sqrt{d}$ and $g_{v2} = f_v + p/\sqrt{d}$ (different), while the inside (log-bias) placement produces $g_{v1} = g_{v2} = f_v + p$ (identical). The paper's claim is mathematically correct. The harsh critic's contrary calculation appears to contain an error.

2. **"Theoretical results are very weak" / "detached from empirical evaluation" (Harsh Critic framing of theory as "weak")**: The theoretical contribution (surjectivity analysis, Theorems 1–2, Assumption 1) is a meaningful formal contribution. The issue is the gap between the existence result and the learning process, which is kept as a Major weakness above but is not grounds for dismissing the theory as "weak."

3. **"Non-autoregressive comparison in Appendix B which is removed" (Harsh Critic)**: The appendix exists in the original submission; the review copy strips it. This is not a paper flaw.

4. **"Proofs rely heavily on appendix" (Harsh Critic)**: Same reason — appendix exists in the original. Not a flaw.

5. **"Training hyperparameters absent from main text" (Harsh Critic)**: The paper states these are in Appendices D, E, H, which exist in the original. Not a flaw.

6. **"PPO-BiHyb reference should be checked" (Harsh Critic)**: The paper cites Wang et al. (2021) which is a real paper; the baseline adaptation concern is captured under the Major weakness above.

7. **Strength Finder generic strengths**: None identified — the Strength Finder's points are all concrete and evidence-backed.

## Novel Insights

The paper's analysis of the reduced space and surjection condition (Section 4, Assumption 1, Theorem 2) provides a useful formal lens for understanding *why* list scheduling fails for certain problem structures and what properties a generation map needs to represent optimal solutions. The insight that skip actions can be integrated into single-pass inference through a parametric score function (rather than a separate network call) is a practically valuable design pattern for other single-pass scheduling architectures. The concentration argument — that poor solutions from excessive skipping cluster in regions of high $u_a, u_c$, making them easier for training to avoid — is an interesting observation about why the design works in practice.

## Suggestions

- Clarify baseline adaptations: for each baseline, specify in 1–2 sentences exactly how compatibility coefficients enter the decision-making (e.g., whether HEFT modifies its computation cost matrix directly, how One-Shot's one-hot embeddings are extended).
- Either provide a small-scale optimality-gap study (MILP vs. learned policy) or explicitly qualify Theorem 1(iv) as a representational-capacity result rather than a learning guarantee.
- Report test-set construction details (are DAG structures and K_acc matrices unseen?) and consider whether fixed test instances explain the small standard deviations.

---

## Score and Decision

### Anchor comparison:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Multi-task bandit CO solver (`Dgc5RWZwTR`) | 4.75 | R1 | WeCAN is clearly stronger: more novel architecture, theoretical analysis, broader evaluation |
| Neural solver selection (`CFLEIeX7iK`) | 5.75 | R1 | WeCAN is stronger: more architecturally novel, theory-backed, better ablation |
| CCBPP encoder-decoder (`6hvtSLkKeZ`) | 6.40 | R2 | WeCAN comparable or slightly stronger: more novel architecture (WeCA, LDDGNN, skip) and theoretical content |
| TRGNN node selection (`gyvYKLEm8t`) | 6.50 | R2 | WeCAN comparable: TRGNN has strong theory but generalization concerns (per-problem training); WeCAN shows better cross-environment generalization |
| Symb4CO symbolic discovery (`jKhNBulNMh`) | 6.67 | R2 | Symb4CO slightly stronger: highly novel symbolic framework. WeCAN is a solid paper in the same quality tier |

**Round 1 bracket**: 5.5–7.5 (clearly above 4.75 bandit and 5.75 solver-selection, below the 8.0 non-CO papers)

**Round 2 narrowing**: The paper sits between CCBPP (6.40) and Symb4CO (6.67). It is more architecturally novel than CCBPP but has a clearer theory-empirical gap than Symb4CO. The baseline adaptation issue is addressable but real. **Final score: 6.5**.

This is a solid paper with genuine architectural innovations, strong empirical results, and thorough ablations. The two Major weaknesses (baseline adaptation details and theory-empirical gap) are addressable and do not undermine the core contributions, but they prevent a higher score. The paper is a clear accept.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>