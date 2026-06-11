## Final Review

## Summary
This paper proposes methods for learning the Minimum Action Distance (MAD) — the minimum number of actions to transition between states — from state-only trajectories in MDPs. It introduces two algorithms (MadDist, a direct regression with scale-invariant loss and contrastive regularization; TDMadDist, a TD-learning variant with target networks), a simple ReLU-based quasimetric d_simple, and a benchmark suite of environments with known ground-truth MAD. MadDist demonstrates strong results against QRL and Hilbert baselines on correlation, Ratio CV, and downstream planning success.

## Strengths
- **Scale-invariant loss design (Eq. 5):** Normalizing by trajectory distance (d_θ(s_i, s_j)/(j-i) - 1)² prevents distant state pairs from dominating the loss, a genuine improvement over Steccanella & Jonsson (2022)'s unscaled squared error (Eq. 2). Figure 3 shows MadDist achieves substantially lower Ratio CV than all baselines (e.g., ~0.15 vs ~0.35 for Hilbert on OGBench Giant Maze).
- **Support for asymmetric quasimetrics:** The paper identifies that prior MAD methods (Park et al. 2024b; Steccanella & Jonsson 2022) use symmetric Euclidean distances to approximate an inherently asymmetric quantity. In asymmetric environments (CliffWalking, KeyDoorGridWorld), the symmetric Hilbert baseline achieves ~0.6–0.8 Pearson correlation while MadDist reaches ~0.9+ (Figure 3).
- **Comprehensive benchmark suite with known ground-truth MAD (Section 7):** Environments span discrete/continuous, deterministic/stochastic, symmetric/asymmetric, and noisy observations, with ground-truth MAD computable in all cases. This enables the first systematic quantitative comparison of MAD approximation quality.
- **Strong downstream planning results (Table 1):** MadDist achieves perfect 1.00±0.00 success rates on 4/6 OGBench PointMaze planning tasks including Stitch settings requiring composition from disconnected trajectories, while Hilbert scores 0.05–0.67 and QRL scores 0.81–0.97. This provides compelling evidence that accurate MAD approximation translates to practical utility.

## Weaknesses

### Fatal
None.

### Major
- **The main experiments do not specify which quasimetric was used, confounding the comparison.** The paper proposes d_simple as a contribution and evaluates MadDist and TDMadDist in the main body (Section 7, Figure 3, Table 1) but never states which quasimetric these algorithms used. Line 127 explicitly defers this: "In Appendix E, we present an ablation study examining how this choice affects our algorithms." QRL uses IQE by definition (line 204). If MadDist used d_simple, the advantage over QRL could come from the learning algorithm or the quasimetric — the two contributions cannot be disentangled. If MadDist used IQE, then d_simple receives no main-body validation, and the claim that it "outperforms more elaborate quasimetrics" (lines 19–20, 30) rests entirely on appendix material. Either way, the paper's two main contributions — the algorithm and the quasimetric — cannot be independently validated from the main body. This is a structural gap in the experimental design.

- **TDMadDist is presented as a co-equal contribution but consistently underperforms, with no analysis of why.** Table 1 shows TDMadDist winning on only 1 of 6 PointMaze environments (PM Giant Navigate). Figure 3 shows it trailing MadDist in all three environments and trailing QRL in two. The paper acknowledges this in one sentence (line 226: "While TDMadDist underperforms the MadDist and QRL algorithm...") but provides no analysis of why TD bootstrapping fails — e.g., whether the bootstrap from s_{i+1} to a random state s_r produces noisy targets, whether the target network update rate β is problematic, or whether the design of Eq. 9 (bootstrapping to random states rather than subsequent trajectory states) is fundamentally flawed. Presenting a negative result as a co-equal contribution without analysis weakens the paper.

- **No absolute distance accuracy metric is reported.** The primary metrics — Pearson/Spearman correlation and Ratio CV — all measure relative ordering or scaling consistency. A method that consistently predicts d_MAD × 5 would score perfectly on correlation and Ratio CV. The paper never reports MAE, RMSE, or the actual scaling factor μ_r from the Ratio CV computation (Eq. 11). While Table 1 shows downstream planning works (suggesting the distances are practically useful), the gap between the paper's goal of providing "a dense, geometrically meaningful measure of progress" (abstract, line 9) and the evidence presented (only relative metrics) weakens the evaluation.

### Minor
- **Seeds/reporting discrepancy.** Line 220 states "All reported results are means over five independent runs (random seeds)" but Figure 3's caption (lines 232, 238, 240) states "Shaded regions indicate minimum and maximum values across three random seeds." This needs resolution.
- **Contrastive loss (Eq. 6) lacks justification.** The loss pushes all randomly sampled state pairs to have distance ≥ d_max, but in connected environments many random pairs are genuinely close. The paper does not discuss why this is safe, how d_max is chosen, or how this term interacts with the constraint loss. An ablation with and without L_r would clarify its contribution.
- **Only 3 of the described environments appear in the main body's figures.** NoisyGridWorld (the only environment testing observation noise robustness, per the research question at line 194) and the UMaze/MediumMaze results are relegated to Appendix F.

### Trivial
None.

## Nice-to-Haves
- A factorial experiment (MadDist × {d_simple, IQE, d_WN}) reported in the main body would cleanly disentangle algorithm vs. quasimetric contributions.
- Discussion of how the behavior policy π_b affects MAD learnability — a random policy may never traverse certain directed edges.
- Reporting μ_r (the mean scaling factor) alongside Ratio CV would indicate whether predictions are systematically over- or under-scaled.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Missing hyperparameters (d_max, H_c, w_r, w_c, α, β, embedding dimension) in main text:** Standard to defer to appendix/supplementary; Appendix D exists in the original submission.
- **Garbled Equation 9 (line 171):** Parser artifact, not an author error.
- **Missing appendix content (Appendix B proof, Appendix E ablations, Appendix F full results, Appendix H planning setup):** These exist in the original submission.
- **Formatting/style nitpicks:** Parser artifacts.
- **Claims about missing related works:** Cannot verify without external sources.

## Novel Insights
The key insight from the review process is that the paper's two main contributions — the MadDist algorithm and the d_simple quasimetric — are presented jointly without factorial disentanglement. The scale-invariant loss (Eq. 5) is a genuine methodological advance over Steccanella & Jonsson (2022), and the benchmark suite fills a real gap. However, without knowing which quasimetric was used in the main experiments, the reader cannot independently validate either contribution. A revised version that runs the factorial experiment and reframes TDMadDist as a negative result with analysis would be substantially stronger.

## Suggestions
- Run a full factorial experiment in the main body: MadDist × {d_simple, IQE, d_WN} vs. QRL (IQE-only). This cleanly isolates whether MadDist's advantage comes from the algorithm, the quasimetric, or both.
- Reframe TDMadDist as a negative result with analysis rather than a co-equal contribution. Discuss why TD bootstrapping to random targets fails.
- Add an absolute error metric (MAE or RMSE normalized by true distance) alongside the existing relative metrics.
- Resolve the seeds discrepancy (five runs vs. three seeds).
- Add an ablation of the contrastive loss L_r to demonstrate its contribution.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>

# Selected Anchors
<related>["GwKNdRc9Bj", "x7Q0uFTH2a", "oEzY6fRUMH", "OMwD6pGYB4", "FNiqaC382D", "plebgsdiiV", "EW6bNEqalF"]</related>