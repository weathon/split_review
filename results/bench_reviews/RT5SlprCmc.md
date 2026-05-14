Now I have read the paper thoroughly and calibrated against human-reviewed anchors. Let me now write the consolidated review.

---

## Summary

This paper proposes two algorithms (MadDist, TDMadDist) for learning the Minimum Action Distance (MAD) between states from unlabeled state trajectories — without actions or rewards. The key innovations are (1) a scale-invariant, quasimetric-aware loss that combines a regression objective, a contrastive term, and an explicit constraint penalty, (2) a novel computationally efficient quasimetric (d_simple), and (3) a benchmark suite with known ground-truth MAD spanning discrete/continuous, deterministic/stochastic, and symmetric/asymmetric environments. The learned distances are evaluated via correlation metrics against ground truth and via downstream planning success rates on OGBench PointMaze tasks.

## Strengths

- **Strong empirical MAD approximation**: MadDist achieves high Pearson/Spearman correlations and low CV across all environments (Figure 3). It strictly outperforms QRL and Hilbert baselines on both correlation metrics and downstream planning (Table 1), achieving near-perfect success rates (0.99–1.00) on most OGBench PointMaze tasks. This validates the claim that MAD can be learned from state trajectories alone.

- **Novel simple quasimetric is effective and well-justified**: d_simple (Equation 3) is a lightweight weighted combination of max and mean ReLU reductions. Appendix B proves it satisfies the triangle inequality, and ablation studies (Figures 5–6, Appendix E) show it outperforms both Wide Norm and IQE quasimetrics across all three evaluation metrics. This is a neat technical contribution with practical value.

- **Diverse benchmark suite with known ground truth**: The evaluation suite (NoisyGridWorld, KeyDoorGridWorld, CliffWalking, PointMaze, OGBench PointMaze) systematically covers asymmetric dynamics, stochasticity, continuous states, and noisy observations. Having known MAD values enables rigorous quantitative comparison, which was previously absent in the literature.

- **TDMadDist extends the framework to TD-style bootstrapping**: The TDMadDist variant (Section 6.2) incorporates a target network and Bellman-consistent bootstrapped targets. While it underperforms MadDist in some settings, it still substantially outperforms the symmetric Hilbert baseline on asymmetric tasks, demonstrating the framework's flexibility.

- **Thorough ablation studies**: Appendix E systematically investigates latent dimension, quasimetric choice, dataset size, and network architecture (Figures 4–9). Results confirm graceful saturation and robustness to these design choices, adding confidence in the method.

- **Practical downstream utility**: Table 1 shows that the learned distances serve as effective planning heuristics with a simple random-shooting MPC planner, achieving 0.99 success rate on GiantMaze. This demonstrates that the representations are useful beyond correlation metrics.

## Weaknesses

### Fatal

None.

### Major

- **Loss function is a proxy, not an exact solver for the MAD constrained-maximization problem**: The paper defines MAD as the solution to a constrained maximization (Equation 1) but translates this into a regression loss (Equation 5) that drives learned distances toward the trajectory bound *j−i*. As the paper acknowledges (Appendix C: "serving as a proxy for the maximize objective"), this is an approximation — matching the upper bound is not equivalent to maximizing subject to the bound. When multiple trajectories provide different (non-tight) bounds for the same state pair, the MSE objective pushes the estimate toward an average of those bounds rather than the tightest one. The constraint loss (Lc) penalizes overshoot of the currently sampled bound but does not force exploitation of tighter bounds from other trajectories. While the TDMadDist variant partially addresses this by bootstrapping, the fundamental tension remains. This does not invalidate the empirical results, but it means the paper overstates the connection between the theoretical formulation and the practical algorithm. The authors should (a) explicitly discuss this gap, (b) analyze how often non-tight bounds appear in practice and how they affect learning, and (c) ideally provide an empirical demonstration that the learned distances recover the tightest bound rather than an average (e.g., a controlled experiment with known overlapping bounds).

### Minor

- **Ground-truth MAD in PointMaze/OGBench is a discretized grid approximation**: For continuous-control PointMaze environments, the paper computes ground-truth MAD via Floyd-Warshall on a discretized grid graph, which ignores velocity, momentum, force-based actuation, and wall collision dynamics. The paper acknowledges this ("approximate the ground truth MAD," line 599) but does not discuss how this approximation gap affects the reported Pearson/Spearman correlations. This matters for interpreting the correlation values in Figures 3, 11, and 12. However, this concern is partially mitigated by (1) the discrete environments (CliffWalking, KeyDoorGridWorld, NoisyGridWorld) where the MAD is exact, and (2) the planning experiments (Table 1) that evaluate downstream utility without relying on the approximate ground truth.

- **No isolation of asymmetry benefit from loss design benefit**: The paper compares against Hilbert (symmetric) and QRL (quasimetric) but does not include an ablation where the authors' own MadDist is run with a symmetric distance (e.g., Euclidean) on the same data. This makes it difficult to attribute gains specifically to the quasimetric versus the new loss formulation (scale-invariant MSE + contrastive + constraint terms). Adding this ablation would strengthen the central claim that asymmetry is crucial.

- **Ablation studies limited to CliffWalking**: The ablation experiments on latent dimension, quasimetric choice, dataset size, and architecture are conducted only in CliffWalking (Appendix E). While CliffWalking is a reasonable testbed (strongly asymmetric, exact ground truth), generalizability of these ablation findings to other environments is not demonstrated.

### Trivial

- The planning experiment (Appendix H) uses a random-shooting MPC planner that queries the true simulator. Success rates may partly reflect the planner's local exploration capability rather than the global accuracy of the learned distance metric. This could be noted as a caveat.

## Nice-to-Haves

- It would be interesting to see an analysis of failure modes: state pairs where the learned distance grossly overestimates the true MAD despite high overall correlation — to understand whether the method captures global structure or merely a coarse ranking.

- A comparison of computational cost (training time, inference latency) between MadDist and the QRL/Hilbert baselines would help practitioners.

- Evaluating on analytically-tractable environments and reporting absolute error metrics (MAE, RMSE) in addition to correlation metrics would provide a more complete picture of MAD recovery accuracy.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh Critic Claim: "The loss function fundamentally changes the problem and invalidates the central claim."** → Kept as a Major weakness but downgraded from "fatal/structural error." The paper openly presents this as a proxy, the approach works empirically, and the claim of *approximation* (not exact recovery) is supported. The critique is real but does not invalidate the paper.

- **Harsh Critic Claim: "The baseline comparison with Hilbert is unfair because Hilbert needs reward/goal-conditioned signals."** → Moved to Removed Points. The paper applies the same data regime to all methods and is transparent about the setup. Hilbert's failure on random-policy data is informative, not unfair — it demonstrates that the proposed method works in a data regime where the baseline does not. However, the absence of a symmetric-vs-asymmetric ablation of the authors' own method is kept as a Minor weakness.

- **Harsh Critic Claim: "The ground-truth MAD used to evaluate the method in continuous environments is unreliable" followed by "the evidence that the method accurately learns the MAD in continuous domains is not trustworthy."** → Kept as a Minor weakness but substantially weakened. The paper acknowledges the approximation; discrete environments provide exact ground truth; planning results provide independent validation. The absolute claim that evidence is "not trustworthy" overstates the issue.

- **Harsh Critic: "The ablation on latent dimension and quasimetric choice only uses CliffWalking; generalisation claims are limited."** → Kept as a Minor weakness (already incorporated above).

- **Strength Finder: "Comprehensive benchmark with known ground-truth MAD"** → Kept but with the caveat about approximate ground truth in continuous environments already reflected in the Minor weakness.

## Novel Insights

None beyond the paper's own contributions. The review synthesis does not reveal insights not already present in the paper.

## Suggestions

- Explicitly discuss the gap between the constrained-maximization formulation (Equation 1) and the proxy regression loss (Equation 5). Add a paragraph acknowledging when and why the proxy can fail (e.g., when loose bounds dominate the data) and how the constraint loss and contrastive loss help mitigate this.

- Add a controlled experiment (even in a simple grid world) demonstrating that the learned distance converges to the tightest bound when multiple trajectories with different bounds exist for the same state pair.

- Add a MadDist-with-Euclidean-distance ablation on one or two environments to isolate the benefit of the quasimetric from the benefit of the loss formulation.

## Score and Decision

### Calibration Anchor Comparison

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/UElh7vzgKX.md` | 5.20 | Quasimetric GCRL paper, accepted. Has strong empirical results but unclear theoretical contribution and limited novelty (n-step extension of prior work). Our paper has clearer novelty (simple quasimetric, two algorithms, benchmark), more comprehensive evaluation, and stronger ablations. **Our paper is stronger.** |
| `/home/wg25r/review_agent/human_reviews_2026/5WhsCB0Vty.md` | 6.00 | Eik-QRL paper, accepted. Strong theoretical contribution with PDE formulation, comprehensive experiments, but gains vanish on manipulation tasks and relies on strong isotropy assumptions. Our paper has similar empirical breadth and comparable novelty. The proxy-loss gap is comparable in severity to the isotropy assumption limitation. **Comparable quality.** |
| `/home/wg25r/review_agent/human_reviews_2026/jdL6WB5jHZ.md` | 6.50 | Simple method (RLDP) that matches SOTA on zero-shot RL, accepted. Clean theory-to-practice connection, strong results. Our paper has more diverse evaluation but the proxy-loss gap creates a similar theory-practice tension. **Our paper is slightly weaker** because of the acknowledged approximation gap. |
| `/home/wg25r/review_agent/human_reviews_2026/rw0vvcHZPe.md` | 5.50 | MAD-based metric space learning, accepted. Novel method but limited environments. Our paper has more comprehensive evaluation and stronger ablations. **Our paper is stronger.** |
| `/home/wg25r/review_agent/human_reviews_2026/FkeURAdA0h.md` | 4.50 | Representation learning for GCBC, accepted. Theory-experiment mismatch, unclear motivation. Our paper has clearer motivation, stronger empirical validation. **Our paper is stronger.** |
| `/home/wg25r/review_agent/human_reviews_2026/VFaYukYt6K.md` | 3.33 | Motion planning with autoencoders, rejected. Poor writing, weak empirical evaluation, unclear contribution. **Our paper is substantially stronger.** |

Positioning: The paper is clearly above the 5.0–5.5 range (stronger than the 5.20 quasimetric paper and the 5.50 MAD paper). It is comparable to the 6.0 Eik-QRL paper in terms of contribution quality and empirical breadth — both have a meaningful limitation that tempers their theoretical contribution, but strong empirical results. The paper is slightly below the 6.50 RLDP paper, which has an elegant simplicity and cleaner theory-practice alignment. 

Score: **6.0**

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>