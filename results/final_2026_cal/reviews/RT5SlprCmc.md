Now I have a solid calibration picture. Let me synthesize the final review.

Let me also verify one more claim — that the paper claims d_simple "outperforms more elaborate quasimetrics" in Section 1:

The paper says (lines 23-25): "we define a novel quasimetric distance function that is computationally efficient and that, in spite of its simplicity, outperforms more elaborate quasimetrics in the existing literature."

But the quoted "elaborate quasimetrics" evidence is deferred to Appendix E only. Let me check what the main text says about this.

Also, let me check the exact wording about Figure 3's seeds more carefully.

From the figure caption: "Shaded regions minimum and maximum values across three random seeds" — this is explicitly stated in the alt-text.

From the setup section: "All reported results are means over five independent runs (random seeds) to ensure statistical robustness."

This is a genuine inconsistency. Figure 3 uses 3 seeds, while other results use 5. This needs to be flagged.

Now let me draft the final review.## Summary

This paper proposes learning the Minimum Action Distance (MAD) — the minimum number of actions to transition between two states in an MDP — from state-only trajectories, without rewards or action labels. It introduces MadDist, which combines a scale-invariant regression loss, a contrastive term, and quasimetric upper-bound constraints, along with a TD variant TDMadDist. The paper also proposes `d_simple`, a lightweight ReLU-based quasimetric, and releases a benchmark suite of environments with known ground-truth MAD. Empirical results on several grid-world and maze environments show that MadDist's learned distances correlate well with true MAD and yield strong downstream planning success rates that outperform QRL and a Hilbert-space baseline.

## Strengths

1. **Well-motivated problem and clean formulation.** The paper correctly identifies the gap between MAD (a structural property of the transition graph) and policy-dependent temporal distances, and formulates MAD learning as a constrained optimization problem. The connection to all-pairs shortest paths is clearly explained.

2. **Sensible loss design with practical innovations.** The scale-invariant objective (Eq. 5) is a principled fix for the known issue that longer-horizon pairs dominate standard MSE losses. The combination of regression, contrastive (Eq. 6), and upper-bound constraints (Eq. 7) within a quasimetric framework is a genuine algorithmic contribution over Steccanella & Jonsson (2022) and Park et al. (2024b).

3. **Benchmark suite with known ground-truth MAD.** The environments (NoisyGridWorld, KeyDoorGridWorld, CliffWalking, PointMaze, OGBench variants) span stochastic/deterministic, discrete/continuous, and symmetric/asymmetric dynamics, with exactly computable ground truth. This enables principled quantitative evaluation via Spearman/Pearson correlation and Ratio CV — a step beyond prior work that evaluated MAD approximations only indirectly through downstream task performance.

4. **Downstream planning validation.** Table 1 provides evidence that accurate MAD estimates (MadDist) translate to strong goal-oriented planning, outperforming QRL and Hilbert baselines across all OGBench PointMaze tasks.

## Weaknesses

### Major

1. **Evaluation compares against only two baselines, one of which is a clearly weak symmetric method.** The only asymmetric baseline is QRL; the Hilbert method is symmetric and predictably poor on asymmetric environments, so its inclusion mainly confirms that asymmetric > symmetric. The paper discusses successor features, time-contrastive representations (Myers et al., 2024), and Steccanella & Jonsson (2022) in related work — all of which produce temporal-distance-like quantities — but does not include them as baselines. While some of these methods learn different quantities (expected discounted visitations under a policy), they are the most relevant comparators for evaluating whether the quasimetric approach adds practical value over existing asymmetric temporal-distance learning. This narrow baseline set weakens the claim that the method "significantly outperforms existing state representation methods."

2. **Inconsistent seed reporting raises concerns about statistical rigor.** The caption of Figure 3 states "Shaded regions minimum and maximum values across three random seeds" (verified in paper at lines 342, 344, 350, 352), while the Empirical Setup states "All reported results are means over five independent runs (random seeds)" (line 332). This is an internal inconsistency. If Figure 3 used only 3 seeds, its shaded regions (min-max range) are insufficient to assess whether observed differences between MadDist and QRL are meaningful — especially given the substantial overlap in the Pearson correlation plots. Elsewhere, Table 1 reports standard deviations over 5 seeds; this should be consistent throughout.

3. **Downstream planning evaluation is underspecified with suspiciously perfect results.** The planning protocol (how the learned distance is used, the planning algorithm, environment details for OGBench tasks) is deferred entirely to Appendix H. MadDist achieves success rates of **1.00 ± 0.00** on four of six OGBench PointMaze environments (PM Large Navigate, PM Large Stitch, PM Medium Navigate, PM Medium Stitch). Perfect success with zero variance across 5 seeds is unusual and raises the question of whether the planning task is sufficiently discriminating, or whether a ceiling effect is at play. Without transparency about the planning procedure, the reader cannot assess whether this evaluation genuinely demonstrates the practical value of the learned representation or whether a simpler heuristic would suffice.

4. **Claim that d_simple "outperforms more elaborate quasimetrics" is unsupported in the main text.** The paper states in Section 1 that `d_simple` "outperforms more elaborate quasimetrics in the existing literature" but provides no comparison against `d_WN` or `d_IQE` for the proposed algorithms in the main paper. The only evidence is deferred to Appendix E. This claim should either be supported in the main text or appropriately qualified.

### Minor

5. **TDMadDist underperformance is noted but not analyzed.** The paper states that "TDMadDist underperforms the MadDist and QRL algorithm" but offers no analysis of *why* the TD-based objective is less effective. Is the bootstrapping introducing bias or variance? Is the target network update (Eq. 10, parameter β) not properly tuned? A brief diagnostic (e.g., comparing whether the value of the bootstrapped target `d_{θ'}(s_{i+1}, s_j)` is systematically over- or underestimated) would deepen understanding of when the TD variant fails.

6. **All test environments are navigation / maze-based.** While the environments vary along several axes (stochasticity, asymmetry, continuous/discrete), they are all variants of grid-world or maze navigation. Whether the method scales to high-dimensional observation spaces (e.g., pixel observations) or qualitatively different dynamics (e.g., robotic manipulation with contact) is an open question. The paper tests NoisyGridWorld with added noise dimensions, but this is a weak proxy for high-dimensional observations.

### Trivial

None.

## Nice-to-Haves

- A small-scale comparison against a simple baseline (e.g., Euclidean distance in observation space, or a planner using true MAD) would calibrate Table 1. Currently, we cannot tell whether the 1.00 success rates are near-optimal or whether a trivial planner would also succeed.
- A brief hyperparameter sensitivity analysis for H_c, d_max, w_r, w_c in the main text (rather than deferred to appendix).

## Removed Points

- *Criticism that the Hilbert method comparison is uninformative.* The paper explicitly states its purpose ("to demonstrate the benefits of methods that explicitly model the quasimetric nature"), making this a designed experimental choice, not a weakness.
- *Criticism that d_simple is "a straightforward composition of standard operations."* Simplicity is a stated virtue; the paper's claim is that it is *effective despite* its simplicity. This is not a weakness.
- *General criticisms about "missing confidence intervals" or "underspecified hyperparameters" without concrete anchor in the paper text.* These are noise-level complaints that apply to most papers and do not specifically harm this paper's core claims.
- *Criticism about "only three random seeds" — this is merged into the actual inconsistency finding above (3 vs. 5 seeds).*
- *Criticism about the paper not reporting computational cost.* This is a generic request; the primary claims do not hinge on runtime.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the seed inconsistency.** Clarify whether Figure 3 uses 3 or 5 seeds and ensure consistent reporting. If only 3, increase to 5 or report with proper confidence intervals.
2. **Add at least one more asymmetric temporal-distance baseline** (e.g., learning a successor-feature-based distance or Myers et al. 2024) to strengthen the claim that the quasimetric approach provides a meaningful advantage over existing asymmetric methods.
3. **Move the planning protocol description into the main paper or a referenced appendix** and explain the planning algorithm, how the learned distance is consumed, and why certain methods achieve 1.00 ± 0.00. If there is a ceiling effect, acknowledge it.
4. **Provide a brief diagnostic for TDMadDist's underperformance** — even a single ablation or analysis of the bootstrap target values would help.
5. **Support the d_simple claim in the main text** or qualify it (e.g., "as shown in Appendix E").

## Score and Decision

**Round 1 bracket:** After reading the paper and the initial anchor search, I bracketed between 4.0 and 6.0, comparing against papers on quasimetric learning and temporal distance representation (weak anchors ~2.5–3.3; middle anchors ~4.5–6.0; strong anchors ~8.0+).

**Round 2 narrowing:** Three topically close anchors provided the calibration:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| UElh7vzgKX (Multistep Quasimetric Distances) | 5.20 | R2 | Stronger evaluation: more baselines, real-robot experiments, full OGBench suite. Current paper has a cleaner problem framing but weaker empirical support. Slightly below this anchor. |
| 5WhsCB0Vty (Eikonal-Constrained QRL) | 6.00 | R1 | Substantially stronger: theoretical derivation (PDE connection), broader experiments across many task types. Current paper is clearly below. |
| aMKFTidLSM (Dual Goal Representations) | 5.50 | R2 | Broader evaluation (20 tasks, pixel-based) and cleaner theory. Current paper is below this anchor due to weaker baselines and underspecified planning evaluation. |
| gOk3o4lMRD (TRIDENT) | 4.50 | R3 | Comparable in empirical thoroughness — both have narrow baselines and presentation issues — but the current paper's problem (MAD learning) is better motivated and the loss design is cleaner. Roughly comparable. |

The paper is substantially better than the weak bracket (~2.5–3.3) and sits in the lower portion of the middle bracket. Compared to the ~5.2–5.5 anchors, the paper's evaluation is narrower and has concrete flaws (seed inconsistency, underspecified planning). Compared to the 4.5 anchor, it has a cleaner contribution but similar empirical limitations. I place it at **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>