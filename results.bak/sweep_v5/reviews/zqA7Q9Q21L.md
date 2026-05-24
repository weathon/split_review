Now I have sufficient calibration anchors. Let me write the final consolidated review.

## Summary

This paper presents R2PS, a method for computing pursuit strategies in graph-based pursuit-evasion games (PEGs) under partial observability that can be applied in real time. The authors: (1) prove that a dynamic programming (DP) algorithm for Markov PEGs produces optimal policies under asynchronous evader moves (Theorem 2); (2) propose a belief preservation mechanism to extend DP policies to partial observability; and (3) combine this mechanism with cross-graph adversarial RL (building on EPG) to train a GNN-based pursuer policy that generalizes zero-shot to unseen graphs. Experiments show the learned policy outperforms PSRO policies directly trained on test graphs, with inference under 0.01 seconds on GPU.

## Strengths

- **Theoretical proof of DP optimality under asynchronous moves.** Theorem 2 and Corollary 1 (Section 3.1) prove that the DP policies derived from Algorithm 1 are strictly optimal for both pursuer and evader when the evader can predict the pursuer's action and move asynchronously. This is a nontrivial extension of the synchronous DP analysis in prior work and provides a principled foundation for using the DP evader as a strong training adversary.

- **Real-time inference that is orders of magnitude faster than DP recomputation.** Section 4.2 derives O(n²m) inference complexity for the GNN policy, and Table 3 reports empirical GPU inference times <0.01 seconds on graphs with >2000 nodes, versus 6–139 seconds for DP recomputation. This directly supports the "real-time" claim and is practically meaningful for dynamically changing environments.

- **Zero-shot generalization outperforming directly-trained PSRO.** Table 2 shows the cross-graph RL policy consistently outperforms PSRO policies directly trained on the test graphs across a range of opponent types (Stay, DP_sync, DP_async, BR_async). The gap is particularly stark against the strong DP_async evader (e.g., Times Square: 0.95 vs 0.04). Since the RL policy never sees the test graphs during training, this is genuine zero-shot generalization.

- **Empirical validation that belief averaging improves DP performance under partial observability.** Table 1 shows DP_belief consistently outperforms DP_Pos across all 10 test graphs (e.g., Downtown Map: 0.90 vs 0.73), confirming the belief-averaged policy (6) adds value over the position-only minimax policy (5).

- **Ablation studies validating belief update frequency.** Table 4 shows reducing belief update frequency from every step to every 3 steps substantially lowers success rates against BR_async (e.g., Scotland-Yard Map: 0.73 → 0.28), confirming the belief preservation mechanism is practically beneficial.

## Weaknesses

### Major

- **The "worst-case robust" claim for the RL policy is not formally supported.** The title, abstract, and contributions repeatedly assert that R2PS produces "worst-case robust" pursuit strategies. The DP policies under perfect information do have theoretical worst-case guarantees (Theorem 2). However, the RL policy is trained against a specific opponent (the optimal DP evader) on a training distribution of graphs, and evaluated against a small set of opponent policies. No formal robustness guarantee is provided for the RL policy under arbitrary evader strategies, arbitrary observation conditions, or OOD graph structures. The best-responding evader BR_async is trained on the test graphs, but this still tests only a limited counterfactual. While the empirical results are promising, the central claim of "worst-case robustness" overreaches what is actually demonstrated. The authors should reframe this as "approximating worst-case robust strategies" or "empirically robust strategies."

- **Modest success rates against strong opponents on several graphs are not discussed with appropriate nuance.** Against the best-responding evader BR_async, the RL policy achieves only 0.10 (Hollywood Walk of Fame), 0.20 (Sagrada Familia), 0.23 (The Bund), and 0.27 (Times Square). These are fairly low capture rates for a security-motivated application. The paper presents these results without discussing whether such rates are practically meaningful, or what a "good enough" threshold would be for real-world deployment. The claim of "worst-case robust" is further undermined by these numbers.

### Minor

- **No confidence intervals or statistical significance tests reported.** All success rates in Tables 1-4 are reported as point estimates without variance, confidence intervals, or multi-seed results. Given the stochasticity of RL training and the modest number of test episodes (500), the reported differences may not be statistically significant in all cases.

- **The belief mechanism is heuristic and lacks theoretical grounding.** The belief update (7) assumes a uniform evader policy when the true policy is unknown, which is arbitrary. There is no analysis of how the belief averaging compensates for the optimistic bias in the DP distances under partial observability, and no regret bound or worst-case loss analysis. The paper's own Lemma 2 is trivial (reduction to perfect information when Pos is a singleton). While the mechanism is empirically validated, the theoretical gap between the DP guarantees and the belief-averaged heuristic is unbridged.

- **Missing baseline: RL policy vs. DP_belief directly.** Table 1 evaluates DP_belief under partial observability, but Table 2 (RL results) never compares against DP_belief as a baseline. Since DP_belief is real-time on small graphs and achieves decent success rates, a direct comparison would isolate whether the RL training adds value over the DP heuristic itself.

- **No ablation isolating the belief mechanism at the RL level.** While Table 4 ablates belief update frequency, there is no experiment comparing RL with belief vs. RL without belief (using only Pos). This makes it hard to attribute improvements to the belief mechanism vs. the GNN architecture or cross-graph training.

### Trivial

- **Time complexity comparison between RL inference and DP recomputation could be clearer.** The paper compares per-timestep RL inference time with DP recomputation time (Table 3). While the paper's context is dynamically changing graphs where DP would need recomputation, this distinction should be made more explicit to avoid the appearance of comparing apples to oranges.

## Nice-to-Haves

- Evaluating against a broader set of learned evader opponents (e.g., population-based training or PSRO on the evader side) would strengthen the robustness claims.
- A small case study visualization showing trajectories from the RL policy, DP_belief, and DP_Pos would help illustrate how belief updates affect behavior.
- Analyzing how the size of the Pos set grows over time in practice (worst-case exponential vs. typical-case bounded) would clarify the Õ(|V|) complexity claim.

## Removed Points

**These points are flagged to be removed — treat them with caution.**

1. *"PSRO comparison is unfair because RL benefits from a much larger data distribution."* — Removed. This misreads the experimental setup. The RL policy uses 100k total episodes across 300 training graphs (~333 episodes/graph on average). PSRO uses 100k episodes *per test graph* (10× more per graph) *and* trains directly on the test graphs. The comparison actually favors PSRO in terms of per-graph data, making the RL result stronger, not weaker.

2. *"Training details are deferred to an inaccessible appendix."* — Removed. The appendix was stripped by the PDF parser; it exists in the original submission. The paper explicitly provides a code link and states the appendix contains implementation details.

3. *"The paper does not justify why observation range 2 is chosen."* — Removed. The range-2 setting is the hardest test case (limited sensing), and Tables 6-7 (referenced in appendices) show monotonic improvement with larger ranges. Choosing the hardest setting for main results is standard practice.

4. *"The comparison of RL inference time with DP recomputation time is unfair."* — Demoted to Trivial. The paper explicitly states the comparison is in the context of "dynamically changing graph structures" where "Algorithm 1 needs to be repeatedly executed." This is a valid comparison, though the distinction could be made more explicit.

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs largely align on the paper's strengths (theoretical DP extension, real-time capability, zero-shot generalization) and weaknesses (overclaimed robustness, heuristic belief mechanism, evaluation gaps). The harsh critic's structural criticism about "worst-case robust" being unsupported is the most penetrating observation; the strength finder's identification of the concrete empirical results provides useful counterbalance. No truly novel synthesis emerges beyond what the two inputs already surface.

## Suggestions

1. Tone down the "worst-case robust" claim throughout the paper. Frame the RL policy as "empirically robust" or "approximating worst-case robust strategies." Reserve the stronger claim for the DP policies under perfect information and reserve a limitations paragraph discussing the gap.

2. Add confidence intervals (e.g., bootstrapped or over 5 seeds) to all success rate tables.

3. Include a baseline comparing the RL policy against DP_belief directly (Table 2), and an ablation of RL trained without belief (only Pos input).

4. Add a brief theoretical discussion of when the belief update (uniform evader assumption) may fail and under what conditions it provides a reasonable approximation — even an informal characterization would improve rigor.

## Score and Decision

**Anchor calibration:**

| Anchor Path | Avg Score | Comparison |
|---|---|---|
| `SEjdainnpB.md` (Differential Games, one-sided info) | 4.00 | Much weaker empirical validation than R2PS; purely theoretical. R2PS is stronger. |
| `Q00CO1Tm6M.md` (POMDP hardness) | 5.75 | Stronger theory, no experiments; comparable overall quality though R2PS has more practical contribution. |
| `KD5nJUgeW4.md` (DRDA for POSGs) | 7.00 | Cleaner theory + experiments; stronger acceptance. R2PS is weaker due to overclaiming. |
| `Zi1QNJKXAD.md` (Robust MDPs) | 3.20 | Weak experiments, incremental contribution. R2PS is substantially stronger. |
| `x36mCqVHnk.md` (Sample efficiency for zero-sum MGs) | 5.50 | Pure theory, rejected for clarity issues. R2PS is roughly comparable with more empirical weight. |
| `ySRsm6HDy5.md` (Robust MARL) | 5.00 | Pure theory with no experiments. R2PS has stronger empirical support. |
| `iGHPVbttMs.md` (Cyclical chaos) | 3.40 | Unclear contribution, poor presentation. R2PS is substantially stronger. |
| `CrMyHiUttz.md` (Bilinear zero-sum games) | 3.00 | Incremental theory. R2PS has more practical value and stronger validation. |

The paper has genuine contributions — the theoretical extension to asynchronous-move optimality, the cross-graph RL pipeline with belief preservation, and convincing zero-shot generalization results. However, the central claim of "worst-case robust" strategies is not supported for the RL policy, the evaluation lacks statistical rigor (no confidence intervals), and several informative baselines are missing. Against the calibration anchors, this paper sits in the 5.0-5.5 band — it has more practical contribution than the rejected theory papers at that level but has enough overclaiming and evaluation gaps to remain below the acceptance threshold without revisions.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>