Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes two self-supervised algorithms (MadDist and TDMadDist) for learning the Minimum Action Distance (MAD) — the minimum number of actions required to transition between two states — from state-only trajectories, requiring neither rewards nor actions. The paper introduces a simple ReLU-based quasimetric, builds on a constrained optimization formulation of MAD, and evaluates on a diverse benchmark suite spanning discrete/continuous states, deterministic/stochastic dynamics, and symmetric/asymmetric transitions. MadDist achieves near-perfect success rates (0.99–1.00) on downstream planning tasks in OGBench PointMaze environments, decisively outperforming QRL and Hilbert baselines.

## Strengths

- **Strong downstream planning results.** MadDist achieves 0.99–1.00 success rates across all six OGBench PointMaze environments (Table 1), decisively outperforming QRL (0.81–0.97) and Hilbert (0.05–0.67). The planning evaluation uses a simple random-shooting MPC that isolates the quality of the learned metric, making this the paper's strongest evidence.

- **Novel simple quasimetric that works well.** The proposed _d_simple_ (Eq. 3) — a weighted max-mean of coordinate-wise ReLU differences — is computationally cheap and consistently outperforms both Wide Norm and IQE quasimetrics in the CliffWalking ablation (Appendix E.2, Figures 5–6). This is a clean design contribution.

- **Effective in asymmetric environments.** The method achieves near-0.9 Pearson correlation in KeyDoorGridWorld and CliffWalking (Figure 3), while the symmetric Hilbert baseline collapses. This validates the value of modeling asymmetry.

- **Comprehensive benchmark suite.** The paper constructs six environments with known (or well-approximated) MAD values spanning stochastic/deterministic dynamics, discrete/continuous state spaces, noisy observations, and structural asymmetry (Appendix G). This is a practical resource for future work.

- **Informative ablations.** Appendix E systematically varies latent dimension, quasimetric choice, and dataset size, showing graceful degradation and saturation behavior.

## Weaknesses

### Fatal

None.

### Major

- **Algorithm vs. quasimetric confound in the QRL comparison.** The paper compares MadDist (using its simple quasimetric) against QRL (using IQE). The ablation (Appendix E.2) shows MadDist-Simple > MadDist-IQE for the same algorithm, but the paper never compares MadDist-IQE against QRL directly. This means the claimed advantage over QRL could be driven entirely by the quasimetric choice rather than the MadDist learning algorithm. To fully support the claim that MadDist as an algorithm is superior, a controlled comparison (e.g., MadDist-IQE vs. QRL-IQE) is needed. The planning results (Table 1) partially mitigate this concern since they compare full systems, but the correlation metrics (Figure 3) are affected.

- **Hyperparameter ambiguity harms reproducibility.** Important hyperparameters are reported as ranges without environment-specific assignment (Table 2: _d_max_ ∈ {100, 500}, _w_r_ ∈ {1, 10}). The paper does not specify which value is used for which environment. This makes reproduction difficult and the results hard to interpret.

### Minor

- **"Ground truth" MAD in continuous environments is an approximation.** For PointMaze and OGBench, the paper computes MAD by discretizing the maze into a grid and running Floyd-Warshall (lines 599, 2917–2919). The paper does acknowledge this is an "approximation," but the resulting values are treated as ground truth for computing Pearson/Spearman correlations and CV ratios (Figures 3, 11, 12). For maze environments with continuous force-based dynamics, the grid-based shortest path through corridors is a reasonable proxy (wall geometry dominates the MAD), but the approximation error is not quantified. The correlation numbers should be interpreted with this caveat. The planning results (Table 1) are unaffected since they measure actual task success.

- **TDMadDist underperforms without analysis.** The TD-based variant underperforms both MadDist and QRL across all environments (Figures 3, 11, 12, Table 1). The paper acknowledges this (line 635) but provides no analysis of _why_ — e.g., whether bootstrapping introduces bias from function approximation in the target network, or whether the TD target is a tighter bound that is harder to learn. The inclusion of a consistently worse second algorithm weakens the paper's overall empirical narrative.

- **No confidence intervals or significance tests for correlations.** The correlation values (Figures 3, 11, 12) are reported with min/max ranges across seeds but without confidence intervals or statistical significance tests. This makes it difficult to assess whether differences between methods are reliable.

- **NoisyGridWorld analysis is incomplete.** The paper evaluates on NoisyGridWorld (4D observations with 2 noise dimensions) and reports high correlations (Figure 11), but does not analyze whether the learned embedding actually ignores the noise dimensions or whether the model overfits. A simple diagnostic (e.g., evaluating on clean observations and comparing) would strengthen this result.

### Trivial

- The scale-invariant loss (Eq. 5) divides by (j−i); the critic's concern about short-pair domination is a theoretical possibility not borne out in the results and not a meaningful weakness.
- Extension to continuous state spaces (Section 4) is described as "hand-wavy" by the critic, but the paper's algorithms do not rely on this extension — they learn from sampled trajectories.

## Nice-to-Haves

- Compare MadDist and QRL using the same quasimetric to isolate the algorithm contribution.
- Quantify the approximation error of the grid-based MAD in continuous mazes (e.g., by comparing against a finer discretization or an exact shortest-path computation on a continuous mesh).
- Analyze whether the learned embedding in NoisyGridWorld actually zeros out noise dimensions.
- Investigate why TDMadDist underperforms MadDist — e.g., whether bootstrapping introduces bias.
- Add t-SNE/PCA visualizations of learned embeddings for continuous environments.

## Removed Points

- **Criticism about "ground truth invalidates central quantitative claims"**: Overstated. The grid-based shortest path is a reasonable proxy for maze MAD (wall geometry dominates); the paper acknowledges the approximation. This is a minor caveat, not a fatal flaw. Moved to Minor.
- **Criticism that the paper's results "could reflect overfitting to the grid approximation"**: Speculative and not supported by evidence. The planning results (Table 1) use the true simulator, not the grid approximation, and show strong performance.
- **Criticism about "extension to continuous state spaces is hand-wavy"**: The paper's algorithms are sampling-based and do not depend on a rigorous continuous-space proof. This is not a weakness.
- **Criticism about "scale-invariant loss could be dominated by short pairs"**: A theoretical possibility not backed by empirical evidence. The method works well in practice.
- **Criticism about "SELU without justification"**: A trivial implementation nitpick.
- **Claim from Strength Finder that the paper provides "theoretical grounding linking MAD to constrained optimization"**: This is correctly identified as a strength (it's a formal proof in Appendix A), so I keep it.
- **Strength Finder's claim about "graceful degradation with dataset size"**: Supported by Appendix E, kept.
- **Several generic strength statements from Strength Finder** ("comprehensive benchmark suite" is kept; some redundant phrasing consolidated).

## Novel Insights

The reviewers surface an important tension: the paper's contribution bundle (algorithm + quasimetric) makes it difficult to attribute improvements to one component over the other. This is a recurring challenge in representation learning papers where the algorithm and the architecture are jointly optimized. The paper would be strengthened by a crossover experiment. Separately, the lack of explanation for TDMadDist's underperformance is a missed opportunity — understanding when TD bootstrapping helps or hurts for distance learning could be a finding in its own right.

## Suggestions

1. **Run a controlled comparison** where MadDist and QRL use the same quasimetric (e.g., both using IQE) to disentangle algorithm from architecture contributions.
2. **Specify hyperparameters per environment** for _d_max_ and _w_r_, or provide a tuning procedure.
3. **Quantify the grid approximation error** for continuous mazes (e.g., compare grid-MAD to a finer-resolution computation or argue theoretically why the approximation is tight).
4. **Add a diagnostic for NoisyGridWorld** showing that noise dimensions are properly ignored in the learned embedding.
5. **Investigate TDMadDist's underperformance** — a simple experiment varying the target network update rate or analyzing whether the Bellman equation for MAD is well-approximated by the TD target would clarify the role of bootstrapping.

## Score and Decision

**Comparative analysis against anchors:**

| Anchor Paper | Avg Score | Comparison |
|---|---|---|
| Eik-QRL (5WhsCB0Vty) | 6.00 | Stronger theory (PDE formulation), similar experimental scope. This paper has weaker theory but stronger planning results in absolute terms (1.00 vs 0.99 on PointMaze). |
| Multistep QD (UElh7vzgKX) | 5.20 | Stronger real-world evaluation (Bridge robot), comparable quasimetric learning contribution. This paper's benchmark diversity and planning isolation are strengths. |
| Geometry of Uncertainty (rw0vvcHZPe) | 5.50 | Similar goal of learning distance metrics from trajectories. This paper has cleaner ground-truth evaluation but less novelty in the learning algorithm itself. |
| Dual Goal Reps (aMKFTidLSM) | 5.50 | Stronger theoretical framing but similar experimental quality on OGBench. Both papers have a gap between theory and practice. |
| Safety-Aware RL (lxKH0pnbhS) | 2.00 | Significantly weaker — results fail to support claims. This paper is clearly stronger. |
| RLDP (jdL6WB5jHZ) | 6.50 | Stronger experimental rigor, cleaner contribution. This paper has more diverse environments but the confound issue is a real gap. |
| Unifying URL (nNmd4pPSck) | 4.40 | More conceptual/theoretical but less empirical. This paper has stronger experimental validation. |
| Emergent Exploration (mwgYORsqtv) | 6.00 | Cleaner analysis with a focused claim. This paper has broader scope but less mechanistic insight. |

**Calibration:** The paper has genuine contributions (simple quasimetric, strong planning results, diverse benchmark suite) and is clearly above reject-quality papers like Safety-Aware RL (2.00) and comparable to mid-range papers like MQE (5.20) and Dual Goal Reps (5.50). However, the algorithm-vs-quasimetric confound and hyperparameter ambiguity prevent it from reaching the 6.0 tier of Eik-QRL or RLDP. The planning results are genuinely impressive but tempered by the confound issue.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept (Poster)</orange>