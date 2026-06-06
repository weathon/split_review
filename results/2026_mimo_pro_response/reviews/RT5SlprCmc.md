## Summary

This paper proposes two algorithms (MadDist and TDMadDist) and a novel quasimetric (d_simple) for learning the Minimum Action Distance (MAD) from state trajectories alone, without rewards or action labels. MadDist modifies the Steccanella & Jonsson (2022) framework with a quasimetric distance function and a scale-invariant loss. The paper introduces a comprehensive benchmark suite with known ground-truth MAD values and demonstrates that MadDist achieves near-perfect planning success rates across all OGBench PointMaze environments.

## Strengths

- **Scale-invariant loss formulation (Equation 5) addresses a concrete limitation of prior work.** By dividing the squared error by (j−i), MadDist prevents distant state pairs on a trajectory from dominating the loss simply because their absolute estimation error is larger. The paper explicitly contrasts this with the unscaled loss in Steccanella & Jonsson (2022, Equation 2). This is a principled modification directly improving learning dynamics.

- **Comprehensive benchmark suite with known ground-truth MAD enables rigorous evaluation.** The paper introduces environments spanning deterministic/stochastic dynamics, discrete/continuous state spaces, symmetric/asymmetric transitions, and noisy observations — all where the true MAD is computable (Section 7, lines 208–219). Prior work lacked systematic evaluation of MAD approximation methods against known ground truth, making this a genuine methodological contribution.

- **MadDist achieves near-perfect success rates on downstream planning (Table 1).** Across all six OGBench PointMaze environments, MadDist achieves 0.99–1.00 success rates, compared to 0.81–0.97 for QRL and 0.05–0.67 for Hilbert. This is particularly striking on the Stitch environments (requiring composition across disconnected trajectories) and Giant environments (requiring long-horizon reasoning), demonstrating that accurate MAD representation learning translates to practical utility.

- **The novel d_simple quasimetric (Equation 3) is both theoretically grounded and empirically effective.** Defined as a weighted combination of max and average positive differences via ReLU, it satisfies the triangle inequality and latent positive homogeneity (proven in Appendix B). Despite its simplicity, the paper claims it outperforms more elaborate quasimetrics like IQE (ablation in Appendix E).

- **Consistent empirical superiority in asymmetric environments (Figure 3).** MadDist and TDMadDist significantly outperform the symmetric-distance Hilbert baseline in CliffWalking and KeyDoorGridWorld, empirically validating the paper's central thesis that quasimetric formulations are essential for capturing directional structure that symmetric methods cannot.

## Weaknesses

### Fatal

None

### Major

- **Missing Steccanella & Jonsson (2022) as a baseline — the direct method being improved.** The paper explicitly states MadDist "learns state distances using an approach similar to prior work (Steccanella & Jonsson, 2022), but differs in the use of a quasimetric distance function and a scale-invariant loss" (Section 6.1, line 137). Yet the baselines (lines 204–206) include only QRL and Hilbert — both using entirely different optimization frameworks. This makes it impossible to quantify the contribution of the paper's two modifications to the predecessor method. The paper already includes quasimetric ablations in Appendix E, so a full ablation — (a) original with symmetric metric, (b) + quasimetric, (c) + scale-invariant loss, (d) MadDist — would be straightforward and would transform the evaluation from "we beat two other methods" to "we can measure our actual contribution over the method we modified."

- **TDMadDist consistently underperforms, weakening the dual-algorithm contribution.** Table 1 shows TDMadDist achieves 0.70 ± 0.30 on PM Large Navigate and 0.73 ± 0.24 on PM Large Stitch with high variance, compared to MadDist's 1.00 ± 0.00 on both. The paper acknowledges: "While TDMadDist underperforms the MadDist and QRL algorithm" (line 226). While the paper still presents TDMadDist as a co-equal contribution, the data shows it is unreliable and in some settings underperforms even QRL. Analyzing *why* TDMadDist fails (bootstrapping instability, target network rate, contrastive loss modification) would turn this weakness into a useful insight.

### Minor

- **Inconsistency in number of random seeds.** The Empirical Setup states "means over five independent runs (random seeds)" (line 220), but Figure 3 caption says "Shaded regions indicate minimum and maximum values across three random seeds" (line 230). This should be resolved.

- **All environments are grid/maze-based.** NoisyGridWorld, KeyDoorGridWorld, CliffWalking, PointMaze, and OGBench PointMaze are all grid-based or maze-based. While they vary in important dimensions (deterministic/stochastic, discrete/continuous, symmetric/asymmetric), the evaluation would be stronger with at least one environment having a fundamentally different state space structure.

- **PointMaze MAD approximation accuracy is not discussed.** The ground-truth MAD for PointMaze is computed using "Floyd-Warshall algorithm over the maze graph" (line 217) for a physics-based continuous environment with force-actuated dynamics. The grid-graph MAD is an approximation of the true MAD, but the paper does not discuss how accurate this approximation is.

- **Key environments' results relegated to appendix.** NoisyGridWorld and KeyDoorGridWorld results are in Appendix F, yet these environments specifically test stochastic dynamics and asymmetric structure — properties central to the paper's claims. Their presence in the main text would strengthen the paper.

## Nice-to-Haves

- The discussion of when MAD is a good approximation vs. when SSP is needed (Section 4, line 78) is brief. A more nuanced treatment of MAD's limitations in stochastic settings would strengthen credibility given this is a paper about MAD.
- Moving the quasimetric ablation study from Appendix E to the main paper would better support the claim that d_simple "outperforms more elaborate quasimetrics" (line 19).

## Removed Points

These points are flagged to be removed, treat them with caution.

- The harsh critic's observation about environments being insufficiently challenging (MadDist achieving 1.00 ± 0.00) is speculative — perfect performance could equally indicate the method works well rather than the environments being too easy. The environments include 100×100 mazes requiring long-horizon reasoning and Stitch variants requiring composition across disconnected trajectories.
- No other points from the harsh critic or strength finder required removal; all major criticisms were substantiated by the paper text.

## Novel Insights

The paper's central insight — that the Minimum Action Distance is inherently asymmetric and that learning it with quasimetric embeddings rather than symmetric metrics yields substantially better representations — is validated by the empirical results in asymmetric environments (CliffWalking, KeyDoorGridWorld) where the symmetric Hilbert baseline collapses to 0.05–0.67 success while MadDist achieves 0.99–1.00. The scale-invariant loss (Equation 5) is a practical contribution addressing a real issue in trajectory-based distance learning. The benchmark suite with computable ground-truth MAD is itself a contribution that future work in this space can leverage.

## Suggestions

1. Add Steccanella & Jonsson (2022) as a baseline with a full ablation isolating the quasimetric and scale-invariant loss contributions.
2. Analyze why TDMadDist underperforms — turn this into insight about when TD-based distance learning works vs. fails.
3. Resolve the "five runs" vs "three seeds" inconsistency.
4. Move NoisyGridWorld/KeyDoorGridWorld results and the quasimetric ablation into the main paper.

## Calibration Anchors

| Round | Path | Avg Human Score | Comparison |
|-------|------|----------------|------------|
| 1 | EWKPEtwjTy (Discrete Actor/Critic) | 2.50 | Far weaker; different topic, rejected |
| 1 | Q1Hr9dVfDS (Continual RL) | 3.00 | Weaker; incremental and rejected |
| 1 | oEzY6fRUMH (State Chrono Representation) | 4.75 | Weaker; ad-hoc losses, overlapping CIs, rejected |
| 1 | I7DeajDEx7 (Episodic Novelty Through Temporal Distance) | 6.75 | Slightly stronger; uses quasimetric temporal distance for exploration, more novel idea, accepted |
| 1 | V71ITh2w40 (Intrinsic Dimensionality) | 6.20 | Different topic but similar embedding focus |
| 1 | P7KIGdgW8S (Hölder Stability) | 8.00 | Much stronger; theoretical depth, topically distant |
| 2 | XMOaOigOQo (ContraDiff) | 5.67 | Weaker; marginal improvements, unclear theory, less clean evaluation |
| 2 | qofh48zW3T (Distributional Distance Classifiers) | 6.00 | Similar quality; interesting ideas but weak baselines, high variance in scores (3–8), rejected |
| 2 | TOiageVNru (Physics-informed TD Metric Learning) | 6.00 | Very comparable; incremental improvement on prior work, both have metric learning + TD components, planning success rate evaluation |
| 2 | skGSOcrIj7 (Neural Spacetimes for DAGs) | 6.80 | Stronger; quasimetric embedding with stronger theoretical guarantees |
| 2 | F07ic7huE3 (Bisimulation Metric for MPC) | 5.50 | Weaker; narrower contribution |
| 2 | 8egnwady4b (Dynamic Contrastive Skill Learning) | 6.33 | Somewhat stronger; more novel skill definition approach |
| 3 | 5iWim8KqBR (Memory-Efficient Algorithm Distillation) | 5.50 | Less relevant topically |
| 3 | o5Bqa4o5Mi (π2vec) | 5.25 | Less relevant; policy representation |
| 3 | BUEQlOwGMY (Object-Based Sub-Environment Recognition) | 5.50 | Less relevant |

**Round 1 bracket:** Between 5.5 and 7.0 — the paper is clearly above the rejected/incremental papers (4.75–5.50) but below the stronger accepted papers (6.75–6.80).

**Round 2 narrowing:** The paper is most comparable to Physics-informed TD Metric Learning (6.00) — both incrementally improve on a predecessor method with metric learning components and evaluate planning success rates. The paper under review is cleaner and has stronger benchmark results but the missing direct predecessor baseline is a significant evaluation gap. Compared to ContraDiff (5.67, accepted), the paper under review is stronger with cleaner methodology and stronger results. Compared to Episodic Novelty Through Temporal Distance (6.75), the paper under review has a notable evaluation blind spot.

**Final positioning:** Slightly above the Physics-informed TD Metric Learning anchor (6.00) due to cleaner evaluation and the novel benchmark suite contribution, but with the missing Steccanella baseline preventing a higher score. The paper sits at 6.0.

## Score and Decision

The paper presents a clear, well-motivated contribution (learning asymmetric MAD with quasimetric embeddings and a scale-invariant loss) with strong empirical results on downstream planning and a genuine benchmark suite contribution. However, the missing direct predecessor baseline is a significant evaluation gap that prevents quantifying the paper's actual contribution over the method it modifies. TDMadDist's underperformance weakens the dual-algorithm framing but does not undermine MadDist's strong results. This is above-average work with a clear but addressable evaluation blind spot.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>