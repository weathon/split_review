Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final review.

---

## Summary

This paper presents R2PS, an approach for computing worst-case robust, real-time pursuit strategies in graph-based pursuit-evasion games under partial observability. The authors (1) prove that a DP algorithm for Markov PEGs maintains optimality under asynchronous evader moves, (2) design a belief preservation mechanism to extend DP policies to partial observability, and (3) embed this mechanism into the EPG framework for cross-graph RL training of a GNN pursuer policy. The trained policy achieves zero-shot generalization to unseen real-world graphs.

## Strengths

- **Rigorous theoretical extension of DP optimality to asynchronous moves**: Theorem 2, Corollary 1, and Theorem 3 (Section 3.1) establish that the DP-derived distance table yields strictly optimal pursuit and evasion strategies when the evader moves asynchronously and can observe the pursuers' actions. Lemma 1 provides the key minimax structural property of the distance table that underpins these results.

- **Belief preservation mechanism is well-motivated and empirically validated**: Lemma 2 guarantees that both the position-extended policy (5) and the belief-averaged policy (6) reduce to the provably optimal perfect-information policy when the evader's position is known. Empirically, DP_belief consistently outperforms DP_Pos across all ten test graphs (Table 1, e.g., Downtown Map 0.90 vs 0.73), confirming that averaging over beliefs improves over pure minimax under continual partial observability.

- **Cross-graph RL produces a policy that generalizes zero-shot to unseen real-world graphs**: Against the strictly optimal asynchronous-move DP evader, the RL policy achieves high success rates (e.g., 1.00 on Grid Map, 0.99 on Downtown Map, 0.95 on Times Square) while PSRO—trained directly on the test graphs—mostly fails (Table 2). The policy also scales to larger graphs (up to 2065 nodes) with inference times of ~0.008–0.010 seconds (Table 3), compared to >100 seconds for DP recomputation, demonstrating real-time applicability.

- **Thorough ablation studies on belief updates**: Table 4 shows that reducing belief update frequency degrades performance and that incorporating known opponent information in the belief update consistently improves success rates against the best-responding evader. This provides concrete evidence that the belief mechanism is doing meaningful work.

## Weaknesses

### Fatal

None.

### Major

- **The sole RL baseline (PSRO) confounds multiple contributions, limiting the informativeness of the central comparison**: The proposed method benefits from (a) DP reference policy guidance, (b) cross-graph training on 300 diverse graphs, and (c) the belief preservation mechanism. PSRO receives none of these and is trained only on each test graph individually with 10 iterations. The result that the proposed method outperforms PSRO (Table 2) is therefore consistent with multiple explanations—cross-graph training alone could account for much of the gap, or the DP guidance could be critical, or the belief mechanism could be the key factor. The paper includes no ablation that trains the same GNN policy on each test graph individually with the same DP guidance and belief mechanism, which would isolate the contribution of cross-graph generalization. Without such a baseline, the claim that the proposed approach is uniquely effective is not fully supported by the evidence presented. This is an evidential gap that cuts across the paper's central empirical claims.

### Minor

- **The belief update relies on a uniform prior over evader transitions, which the paper acknowledges but does not deeply analyze**: Equation (7) propagates belief using a uniform distribution over neighbors because the evader's true policy is unknown. The paper is transparent about this (Section 3.2: "ν(v) is set to be a uniform distribution over Neighbor(v) by default") and provides a useful comparison in Table 4 (Known Opponent vs Original), showing that using the actual evader policy improves performance. However, the paper does not discuss under what conditions the uniform approximation might lead to systematically poor belief tracking (e.g., on graphs with high degree variance where the evader's optimal policy concentrates on few edges). A brief analysis of when and why this approximation is safe would strengthen the worst-case robustness claim.

- **No error bars, confidence intervals, or variance reported on success rates**: All tables report point estimates from 500 test episodes without any measure of dispersion. Given the stochastic nature of the initial positions and the RL training process, reporting standard deviations or confidence intervals would help readers assess the reliability of the reported differences, particularly for narrower margins (e.g., Ours vs PSRO on Grid Map against DP_async: 1.00 vs 0.88).

- **The "first approach" claim is stated without a sufficiently deep survey of adjacent literatures**: The paper claims to introduce "the first approach to worst-case robust real-time pursuit strategies under partial observability" (Abstract, Section 1). While the combination of DP, belief preservation, and cross-graph RL for graph-based PEGs does appear novel, the paper does not engage with related work on POMDP-based planning for pursuit-evasion, belief-space planning in robotics, or online MPC methods for security games. A more thorough positioning against these adjacent areas would make the novelty claim more credible and situate the contribution more precisely.

### Trivial

- The conclusion (Section 6) summarizes results but does not acknowledge limitations of the approach (e.g., the uniform prior assumption, the restriction to two pursuers, the dependence on precomputed DP tables). A brief limitations paragraph would improve completeness.

## Nice-to-Haves

- A recurrent-policy baseline (e.g., LSTM-based policy that processes observation histories without explicit belief maintenance) would help quantify the benefit of the explicit belief preservation mechanism over implicit history encoding.
- An ablation training the same GNN with DP guidance on each test graph individually (no cross-graph training) would isolate the contribution of cross-graph generalization.
- A sensitivity analysis varying the assumed evader policy in the belief update (e.g., uniform vs random vs adversarial) would illuminate how much the uniform approximation matters in practice.
- Scaling experiments beyond m=2 pursuers would strengthen the generality of the approach.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The paper does not analyze the impact of this approximation on worst-case robustness"** — REMOVED. The paper explicitly acknowledges the uniform prior limitation (Section 3.2) and provides analysis through the "Known Opponent" vs "Original" comparison in Table 4, showing the performance gap attributable to the uniform approximation. The harsh critic's claim that no analysis exists is incorrect.

- **"The paper does not report the hyperparameters used for PSRO or the neural architecture"** — REMOVED. The paper states that implementation details and hyperparameter settings are in Appendix C. The appendix is stripped by the parser; these details exist in the original submission.

- **"The paper claims real-time applicability but does not report the total latency of the entire pipeline, including belief update, GNN forward pass, and action selection"** — REMOVED. The paper reports inference times of 0.007–0.010 seconds on GPU in Table 3 and provides a complexity analysis in Section 4.2 showing the overall inference time complexity is O(n²m). This is sufficient evidence for real-time applicability.

- **"The theoretical contribution is modest, and the novelty of the belief-preservation mechanism is not situated in related work on POMDPs"** — DEMOTED to Minor (rephrased as the "first approach" claim issue). The harsh critic frames this as a fatal lack of novelty, but the theoretical results (Lemma 1, Theorem 2, Corollary 1, Theorem 3) constitute a real contribution even if they build on prior DP work, and the belief preservation mechanism, while conceptually simple, is applied to a non-trivial setting with empirical validation.

- **"The extension of DP optimality to asynchronous moves is a straightforward corollary"** — REMOVED. This is a judgment call, not an identified error. The paper provides full proofs (in appendix) and the results are non-trivial (the evader policy changes from Equation 2 to Equation 3, and the proof requires Lemma 1 to establish the minimax property of D). Even if the proof technique is straightforward, the result itself is a contribution.

- **"There is no comparison with a recurrent-policy baseline"** — MOVED to Nice-to-Haves. This is a reasonable suggestion but not a core weakness for a paper whose contribution is explicit belief maintenance. The paper's design choice to use explicit belief is well-motivated by the desire to leverage the DP distance table.

- **"The experiments are restricted to two pursuers; scaling to more pursuers is not discussed"** — MOVED to Nice-to-Haves. The paper explicitly justifies m=2 in the experimental setup (line 217) and the theoretical framework is general. Scaling to more pursuers would be a nice extension but is not essential for the core contributions.

## Novel Insights

The paper's key insight—that a DP distance table precomputed for perfect-information Markov PEGs can be reused both to prove optimality under asynchronous evader moves and to construct effective observation-based policies under partial observability via belief averaging—is practically valuable. The combination of this insight with cross-graph RL training against the DP evader yields a policy that achieves zero-shot generalization. The finding that the uniform-prior belief update is sufficient for strong performance in practice (while being improvable with known opponent information, Table 4) is a useful empirical observation.

## Suggestions

- Add a single-graph RL baseline (same GNN architecture, same DP guidance, same belief mechanism, trained on each test graph individually) to isolate the contribution of cross-graph training. This would directly address the major weakness above.
- Report standard deviations on success rates across the 500 test episodes to enable assessment of statistical significance.
- Add a brief limitations paragraph to the conclusion acknowledging the uniform prior assumption, the m=2 restriction, and the reliance on precomputed DP tables.
- Cite and briefly discuss the most relevant POMDP-based or belief-space planning methods for pursuit-evasion to strengthen the "first approach" claim and better position the work.

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| DjHnxxlqwl (UNSG/GraphChase) | 4.75 | R1 | R2PS is substantially stronger — real algorithmic contribution + thorough experiments vs a benchmarks paper with thin validation |
| zwU9scoU4A (Graphex MFG) | 6.67 | R1 | Comparable in structure (theory + algorithm + real-world experiments); Graphex MFG has a more novel theoretical extension; R2PS has more extensive empirical evaluation |
| stUKwWBuBm (Tractable MARL) | 8.00 | R1 | R2PS is clearly below — Tractable MARL has deeper theoretical contributions (new equilibrium concept, sample complexity) and broader significance |
| 99tKiMVJhY (Dec-POMFC) | 6.33 | R2 | Most comparable anchor — similar profile (theory + algorithm + experiments), similar weakness (baseline fairness concern). R2PS has more extensive experiments (10 real-world graphs + scalability + ablations vs 2 swarm models). R2PS is slightly stronger empirically but has a more significant baseline confound. |
| s9SVlWOcLt (Proto Successor Measure) | 6.75 | R2 | PSM has a more novel theoretical insight (affine set representation) but weaker experiments. R2PS is more practically grounded but less theoretically novel. |

**Round 1 bracket:** 5.0–7.5. The paper is clearly above the 4.75 UNSG benchmark paper and clearly below the 8.00 Tractable MARL paper.

**Round 2 narrowing:** The Dec-POMFC anchor (6.33) is the closest comparable. R2PS has more extensive experiments but a more significant confound in its primary RL baseline. The Graphex MFG (6.67) has stronger theoretical novelty. PSM (6.75) also has a more novel theoretical insight.

**Final score:** 6.0. The paper makes genuine contributions — a non-trivial theoretical extension of DP optimality to asynchronous moves, a practical belief preservation mechanism with empirical validation, and a cross-graph RL pipeline that achieves strong zero-shot generalization. The experiments are extensive for the domain, with evaluations on 10 real-world graphs, scalability tests, and meaningful ablation studies. However, the sole RL baseline (PSRO) confounds multiple factors, leaving the central empirical comparison less informative than it should be. With proper ablations disentangling cross-graph training from DP guidance, the paper would be a clear accept. In its current form, it is a solid paper with a significant but addressable evidential gap.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>