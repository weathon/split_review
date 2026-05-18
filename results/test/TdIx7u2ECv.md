I now have a thorough understanding of the paper and all reviewer claims. Here is my consolidated review.

---

## Summary

This paper proposes ITES (Imagine To Ensure Safety), a hierarchical safe RL method that decomposes safety into two levels: a cost model guides the high-level policy to generate safe subgoals, and a world model enables the low-level policy to verify safety through trajectory imagination before execution. The method is built on top of HRAC and evaluated on SafetyGym (short-horizon) and a custom SafeAntMaze (long-horizon). Results on SafeAntMaze show a dramatic cost reduction (~5 vs ~120 for the Lagrangian HRL baseline) at comparable success rates, which is the paper's strongest evidence.

## Strengths

1. **Novel dual-level safety decomposition in HRL.** The idea of separating safety into subgoal-level (via a learned cost model) and trajectory-level (via world model imagination) within a hierarchical framework is well-motivated and clearly described (Sections 3.2–3.3). This is a non-trivial integration that goes beyond simply adding a Lagrangian multiplier to a hierarchical policy.

2. **Dramatic improvement on long-horizon SafeAntMaze.** On SafeAntMazeCshape, ITES achieves a success rate of ~0.90 with an average cost of ~5.43, whereas the Lagrangian-based HRAC-LAG reaches a comparable success rate but at a cost of ~120 (Figure 4, Table 1). This order-of-magnitude cost reduction on a long-horizon task where flat safe baselines fail is the paper's strongest empirical contribution and directly supports the claim that hierarchical decomposition with model-based safety is effective for such settings.

3. **Ablation study validates the necessity of both safety levels.** Figure 6 shows that removing low-level safety (HRAC-SafeSubgoals) increases cost and variance, while removing high-level safety (HRAC-SafeController) degrades safety further. The full ITES achieves the lowest cost with tightest variance, providing clear evidence that both the cost-model-based subgoal selection and the imagination-based trajectory safety are complementary and necessary.

4. **Honest treatment of limitations.** The paper explicitly acknowledges that ITES does not use the cost budget *d*, minimizes cost independently per time step, and requires manual goal-space design (Section 6, lines 224–226). This transparency is appreciated.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison with SafetyLayer+HiRO, the closest hierarchical safe RL baseline.** The Related Work section (line 221) identifies SafetyLayer+HiRO (Roza et al., 2022) as "the most closed to us" among hierarchical safe RL approaches, yet the experiments contain no comparison against it. This is a significant omission. The paper's central experimental contribution is showing that its specific two-level safety design outperforms a Lagrangian adaptation of HRAC (HRAC-LAG) that the authors constructed themselves. Without comparing against the existing hierarchical safe RL method from the literature, it is unclear whether the gains are attributable to the ITES design specifically or would be achieved by any principled hierarchical safe approach. This gap weakens the claim that ITES advances the state of the art in hierarchical safe RL.

2. **Unclear and potentially biased MBPPOL comparison in the sparse-reward setting.** The paper states (line 194): "MBPPOL used weights that achieved the highest performance during training, while ITES utilized weights with a similar cost metric during training." This description is ambiguous — "similar cost metric" to what? If ITES weights were selected to match MBPPOL's cost while MBPPOL weights were selected for best performance, the comparison is systematically biased toward ITES. The paper then claims "under similar safety conditions, ITES exhibits superior performance," but the selection methodology is not sufficiently described to allow the reader to verify this. A fairer approach would be to compare both methods at their best trade-off points (e.g., along a Pareto frontier) or to select checkpoints under a clearly matched criterion for both.

### Minor

3. **No diagnostic analysis of world model or cost model quality.** The entire safety mechanism depends on the reliability of the world model (for imagined rollouts) and the cost model (for subgoal safety scoring). Yet the paper provides no empirical validation of either: no prediction error on held-out transitions, no analysis of how cost model accuracy correlates with final safety, no study of how world-model rollout error propagates over the multi-step imagination horizon. While the end-to-end results are reassuring, the claim that the method works "through imagination" would be significantly strengthened by diagnostic evidence that the imagined safety correlates with actual costs.

4. **Abstract overclaims on SafetyGym results.** The abstract states that ITES demonstrates "superior performance quality while maintaining comparable safety violations." On PointGoal1, however, ITES achieves reward 21.42 with cost 1.46 while CUP achieves reward 15.92 with cost 0.79 — nearly doubling the cost. The paper's own text (line 192) honestly acknowledges this trade-off. The contribution list (line 27) uses the more accurate phrasing "only slightly compromising on safety," but the abstract does not match this nuance and should be revised.

5. **Cost budget *d* is formally defined but never used.** Section 2.1 sets up the CMDP framework with a cost limit *d*, but ITES minimizes cost violations unconditionally rather than respecting a user-specified budget. The paper acknowledges this in the limitations (line 225), but the framing in Section 2.1 sets reader expectations that *d* will be used. This should be flagged earlier in the paper.

6. **No ablation on the imagination horizon *k* or the random sampling of *n*.** The imagination horizon *n* is sampled uniformly from {1,…,k-1} (line 125), but there is no analysis of how this choice affects safety outcomes. A sensitivity study showing results for fixed *n*=1 or *n*=k/2 would help justify the random sampling design.

### Trivial
- The paper uses "most closed to us" (line 221); standard phrasing would be "closest to ours."

## Nice-to-Haves
- Statistical significance testing (e.g., paired bootstrap) to assess whether observed differences are meaningful given the 3-seed variance.
- A more detailed discussion of how the cost model interacts with the adjacency constraint in HRAC's embedding space (the reviewer's observation about locality benefits is insightful but not a flaw).
- Comparison with SafetyLayer+HiRO, if resources permit, would substantially strengthen the paper.

## Removed Points
- *The reviewer's request for "statistical tests or confidence intervals beyond standard deviation from 3 seeds"* — this is downgraded to Nice-to-Have. Reporting mean ± std over 3 seeds is standard practice in RL; the paper follows the norm of its field.
- *The reviewer's point that "the related work section would benefit from more direct discussion of why Lagrangian methods suffer in hierarchical settings"* — this is a suggestion for improvement, not a weakness. The paper does provide such intuition (lines 179–180: the safety critic is contingent on the low-level policy's behavior, making optimization hard).
- *The reviewer's suggestion to "add an ablation removing the cost model and replacing it with a Lagrangian on the high-level only"* — this is a specific experimental suggestion, not a weakness. Placed in Nice-to-Haves.

## Novel Insights
The most interesting observation that emerges from the reviews is the tension between the two SafetyGym environments: on PointGoal1, ITES trades safety for performance (doubling cost for ~34% reward gain), while on CarGoal1 it achieves both better performance and comparable safety. This suggests that the ITES dual-level safety mechanism may be sensitive to environment properties such as observation modality (lidar vs. other sensors), obstacle layout, or the distance at which the cost model can accurately predict safety from local observations. The paper does not explore this variation, but understanding when the method's safety–performance trade-off is favorable vs. unfavorable would be a valuable direction for future work.

## Suggestions
1. Add an experimental comparison with SafetyLayer+HiRO, or at minimum, clearly state why such a comparison was not feasible and temper the claims about hierarchical safe RL accordingly.
2. Clarify the MBPPOL checkpoint selection methodology and either (a) present a Pareto frontier of reward vs. cost across training for both methods, or (b) select checkpoints under a matched cost threshold.
3. Add a brief model validation section reporting world model prediction error (MSE on held-out transitions) and cost model accuracy (ROC AUC or binary accuracy), even if only in the appendix.
4. Revise the abstract to align with the more nuanced language in the contribution list ("only slightly compromising on safety" rather than "maintaining comparable safety violations").
5. Add an ablation on the imagination horizon *k* to show how sensitive the results are to this hyperparameter.

## Score and Decision

This paper makes a genuine contribution: the dual-level safety design for HRL is well-motivated, the SafeAntMaze results are striking, and the ablation study is informative. The weaknesses are real but primarily relate to missing comparisons and incomplete analysis rather than flawed methodology. The missing SafetyLayer+HiRO comparison and the unclear MBPPOL selection are the most impactful issues. The paper would benefit from revision but the core ideas have merit.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>