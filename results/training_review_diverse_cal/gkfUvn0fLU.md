Now I have everything I need. Let me produce the final consolidated review.

## Summary

This paper studies reward model overoptimization in the context of composite (multi-component) reward functions used in RLHF. The authors first demonstrate that correlation between component reward models shifts the "proxy points" (the RM values beyond which further optimization harms ground-truth evaluation). They then propose using constrained RL (CMDPs with Lagrangian relaxation) to keep each component reward at or below its proxy point, learning dynamic weightings via Lagrange multipliers rather than tuning fixed weights. Several variants are introduced (μ-PPO, ξ-PPO, All-PPO, PPO-SAT), and ξ-PPO is shown to outperform standard PPO and PPO-SAT on a dialogue generation task. Finally, a derivative-free threshold search (NM-PPO) is proposed to identify proxy points in a single training run.

## Strengths

- **First systematic study of overoptimization in composite RMs**: The paper demonstrates that correlation between component reward models (METEOR and intent score) shifts the joint proxy point relative to independent proxy points (Figure 2, line 79). This is a genuine and practically important observation.

- **Constrained RLHF methods achieve higher and more stable evaluation performance**: Both μ-PPO and ξ-PPO consistently outperform standard PPO (with hyperparameter-tuned fixed weights) and PPO-SAT across training trajectories, with the advantage persisting under 3× extended training (Figure 4, line 162). Results are averaged over 5 seeds with standard error shading.

- **Proxy-point thresholds are empirically validated as optimal**: The ablation in Figure 5 (left, line 172) shows that setting thresholds 10% higher or 10% lower than the identified proxy points reduces final evaluation performance, confirming that the proxy points correspond to effective constraint bounds.

- **Constraint satisfaction is empirically verified**: Figure 5 (right, line 164) shows that each constrained method behaves as designed — μ-PPO meets or exceeds thresholds, All-PPO stays below them, and ξ-PPO approximately hits them.

## Weaknesses

### Fatal
None.

### Major

- **NM-PPO evaluation lacks variance information and the computational cost comparison is incompletely reported.** The NM-PPO result in Figure 7 (left, line 185) shows a single marker with no error bars, unlike the rest of the paper which uses 5 seeds with standard error (line 154). Without variance information, the robustness of the NM-PPO result cannot be assessed. Furthermore, the paper states "we use ξ-PPO to converge to those points and then evaluate the model once they're reached" (line 190) but does not report how many Nelder-Mead iterations or ξ-PPO evaluations occurred within the 256,000-step budget. Since the x-axis claims to include "total number of training steps (including hyperparameters searches)" for all methods, the lack of a detailed breakdown for NM-PPO makes the computational savings claim unverifiable. The paper notes a caveat about small feasible regions (line 191) but does not provide the raw numbers needed to evaluate the comparison.

### Minor

- **The "convex combination" claim about the mixed advantage formula is technically imprecise.** The paper states the formula yields "a convex combination of the task and constraint advantages" (line 143), but the weights sum to N, not 1. This is a presentation imprecision rather than an algorithmic error — the formula is clearly written and the algorithm is well-specified. However, the phrasing could confuse readers about the connection to the standard Lagrangian, and the theoretical guarantees cited for Lagrangian relaxation (convex-concave structure, sublinear regret) apply to the unbounded-multiplier case rather than this specific variant. The paper would benefit from clarifying that this is a practical heuristic following prior work (Stooke et al., Zahavy et al., Moskovitz et al.) rather than a direct instantiation of the textbook Lagrangian.

- **The correlation analysis in Figure 2 is descriptive rather than quantitative.** The paper shows a contour plot of a fitted surface and asserts that correlation shifts proxy points, but does not provide statistical measures (e.g., correlation coefficients between the RMs during training, confidence intervals on the joint proxy point location, or a formal test comparing the joint vs. independent proxy points). The qualitative visual is sufficient to motivate the approach, but the "analysis of correlation effects" claim would be stronger with more rigor.

- **The reward-to-go trick for Lagrange multiplier updates is not ablated.** The paper replaces value estimates with raw sum-of-rewards-to-go in the constraint-violation update because "early in training, value estimates are inaccurate" (line 147). While the intuition is reasonable, an ablation showing that performance degrades without this trick would strengthen the methodological contribution.

### Trivial

- The paper says the mixed advantages are a "convex combination" when the weights sum to N (line 143). This should be corrected to "linear combination" or the formula should be renormalized.

## Nice-to-Haves

- Comparison against an adaptive-weighting baseline (e.g., a method that dynamically adjusts RM weights based on held-out evaluation without explicit constraints) would help clarify whether the benefit comes from the constraint formulation itself or merely from adaptivity.
- Details on the Nelder-Mead implementation (number of evaluations, stopping criterion, initial simplex selection) would improve reproducibility.
- Validation with more than two component RMs and on additional domains (the paper acknowledges this as future work, line 198).

## Removed Points

- **Criticism that proxy points found without KL are mismatched with ξ-PPO where KL is the task reward (Harsh Critic point 2).** This criticism misunderstands what a proxy point is. The proxy point is defined as "the value at which further increasing the proxy reward results in decreased ground-truth performance" (line 72) — this is a property of the RM's fidelity as a proxy, not of the optimization algorithm. The independent-vs-joint proxy point comparison in Figure 5 (right) already validates that the relevant thresholds work under the constrained objective. The ±10% ablation (Figure 5 left) further supports robustness to threshold specification.

- **Criticism that the mixed advantage formula invalidates the theoretical guarantees.** The formula is presented as a practical modification (following prior work), not as the canonical Lagrangian. The theoretical section (line 113) discusses guarantees for the general framework; the practical modifications are a separate contribution. The algorithm is clearly specified and works as described.

- **Criticism about lack of an "adaptive weighting baseline."** The constrained methods ARE adaptive — the Lagrange multipliers are learned dynamically. The paper compares against multiple baselines including PPO with optimal fixed weights (tuned over 10 runs).

- **Criticism about needing validation with more than 2 component RMs.** This is acknowledged as future work (line 198). Demanding it as a condition for acceptance is scope creep.

- **Criticism about missing appendix/pseudocode.** The parser strips these sections; they exist in the original submission. (Referenced as `\cref{alg:cPPO}`, line 112.)

## Novel Insights

The sharpest insight from the review process is that the paper's core contribution (constrained RLHF for composite RMs) is empirically well-supported independently of the NM-PPO extension. The main results in Figures 4 and 5 use 5 seeds with standard errors and show clear improvements over strong baselines. The NM-PPO result, while interesting, is the least methodologically rigorous part of the paper and carries disproportionate weight in the computational-savings claim. The paper would be stronger if it clearly separated these two contributions and either (a) provided proper multi-seed results for NM-PPO or (b) presented NM-PPO as a preliminary/exploratory result rather than a claimed contribution. Additionally, the "convex combination" vs. Lagrangian derivation point, while minor, is a useful signal: the paper should more clearly delineate the textbook Lagrangian framework from the bounded-multiplier variant used in practice, which would prevent reader confusion.

## Suggestions

1. Add multi-seed results and error bars for NM-PPO, or clearly state it as a single-run demonstration.
2. Provide a detailed breakdown of the computational cost of NM-PPO (number of Nelder-Mead iterations, steps per evaluation, total steps).
3. Correct the "convex combination" claim (or renormalize the formula so weights sum to 1).
4. Add an ablation of the reward-to-go trick for the Lagrange multiplier update.
5. Include a short quantitative analysis of the correlation effect (e.g., correlation coefficient between RMs during training, confidence region on the joint proxy point).

## Score and Decision

The paper addresses an important and timely problem (overoptimization in composite RMs), proposes a well-motivated solution grounded in constrained RL, and provides empirical evidence that the constrained methods outperform standard approaches. The main experimental results (Figures 4, 5) are solid, with 5-seed averages and standard errors. The primary weaknesses are in the NM-PPO extension (missing error bars, unclear computational cost reporting) and some presentation imprecisions. These are addressable in a revision and do not undermine the core contribution.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>