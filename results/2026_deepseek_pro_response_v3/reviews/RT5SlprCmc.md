Now let me finalize the review with the calibration results.

## Round 1 Bracket

Based on comparison with round-1 anchors:
- **State Chrono Representation (4.75)**: Had significant issues (questionable theorems, ad-hoc losses, unconvincing results). Our paper is clearly stronger — more rigorous evaluation, clearer methodology, stronger empirical results.
- **Distributional Successor Measure (5.75)**: Interesting theory but experiments limited to toy gridworld. Our paper has more comprehensive, diverse evaluation.
- **Self-Predictive RL (6.75)**: Unifying theoretical framework with strong conceptual contribution but somewhat inconclusive empirical results. Our paper has clearer empirical results but less theoretical depth.

**Bracket**: 5.5 – 7.0

## Round 2 Narrowing

Retrieved and compared:
- **π2vec (5.25)**: Policy representation with successor features, accepted. Weaknesses included limited theoretical analysis and missing ablations. Our paper is stronger — more comprehensive evaluation, clearer methodology, downstream planning validation.
- **ETD — Episodic Novelty Through Temporal Distance (6.75)**: Very relevant. Learns temporal distances via contrastive learning for exploration. Clean story, strong results. Our paper is comparable but slightly weaker due to the TDMadDist underdevelopment and missing symmetric ablation. ETD's core method is tighter.

**Final positioning**: Our paper sits between π2vec (5.25) and ETD (6.75), closer to ETD. The contributions are clear, the evaluation is comprehensive, and the weaknesses are all minor. Score: **6.5**.

## Summary
This paper proposes MadDist and TDMadDist, two self-supervised algorithms for learning the Minimum Action Distance (MAD) from unlabeled state trajectories, requiring neither rewards nor actions. Key innovations include a scale-invariant loss normalized by temporal index difference, native support for quasimetric (asymmetric) distance functions including a new simple quasimetric d_simple, and a diverse benchmark suite with known ground-truth MAD. Experimental results across discrete/continuous, deterministic/stochastic, and symmetric/asymmetric environments show MadDist substantially outperforms QRL and Hilbert baselines on both representation quality metrics and downstream goal-oriented planning.

## Strengths
- **Scale-invariant loss design (Eq. 5)**: Divides the squared error by (j-i), preventing long-horizon state pairs from dominating the optimization. This is a clean, well-motivated improvement over prior work's raw squared error, and Figure 3 shows it yields substantially better Pearson correlation and Ratio CV than baselines.
- **Comprehensive benchmark suite with known ground-truth MAD**: The paper constructs environments spanning discrete (KeyDoorGridWorld, CliffWalking) and continuous (NoisyGridWorld, PointMaze) state spaces, deterministic and stochastic dynamics, and symmetric and asymmetric transitions — all with exactly computable ground-truth MAD. This enables rigorous, controlled evaluation absent from prior work.
- **Native quasimetric support with simple, efficient d_simple (Eq. 3)**: The framework supports any quasimetric including d_simple, which requires no learned parameters beyond the embedding itself, is proven to satisfy the triangle inequality, and empirically performs competitively with more elaborate quasimetrics.
- **Downstream planning validation (Table 1)**: MadDist achieves near-perfect or perfect success rates (0.93–1.00) across all six OGBench PointMaze variants, including the large-scale Giant maze and the Stitch setting requiring composition from disconnected trajectories, decisively outperforming all baselines.
- **Multi-faceted evaluation**: Pearson correlation, Spearman correlation, and Ratio CV collectively capture linear scaling, rank preservation, and ratio consistency, providing a more complete picture than any single metric.
- **Training from random-policy trajectories**: All methods are evaluated using offline data collected by a random behavior policy, making the setup realistic and not dependent on expert demonstrations.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Missing internal symmetric ablation for MadDist**: The paper compares against Hilbert (a different symmetric algorithm) and QRL (a different quasimetric algorithm), but does not run MadDist with a symmetric Euclidean distance to isolate the quasimetric's contribution. While the comparison against Hilbert provides indirect evidence for the value of asymmetry, a controlled ablation within the same algorithmic framework would more directly support the paper's narrative about the importance of quasimetrics.
- **Evaluation state-pair sampling protocol is not explicitly specified**: The paper does not describe how state pairs are selected for computing the evaluation metrics (all pairs, random sample, only from training trajectories, etc.). Making this explicit would strengthen confidence that the reported correlations reflect genuine MAD recovery rather than potential overlap with the training distribution.
- **TDMadDist's contribution is underdeveloped**: TDMadDist consistently underperforms MadDist in most settings. The paper acknowledges this but offers no diagnosis of why bootstrapping degrades performance, nor does it identify a clear regime where TDMadDist is preferred over MadDist. As a secondary contribution, its value proposition is unclear.
- **Perfect planning success rates (1.00 ± 0.00) on four environments receive no discussion**: While these results speak to MadDist's effectiveness, a brief note contextualizing the planning protocol and success criterion would help readers interpret these striking numbers.

### Trivial
- **Seed-count inconsistency**: The main text states "five independent runs" (line 220) while Figure 3's caption references "three random seeds" (lines 230, 240).
- **Eq. 9 in Section 6.2 contains a parser artifact** and appears garbled; this should be corrected in a camera-ready version.

## Nice-to-Haves
- A discussion of when quasimetrics are necessary vs. when symmetric distances suffice. CliffWalking and KeyDoorGridWorld are the clearly asymmetric environments, while PointMaze environments have largely undirected transition graphs where MAD is approximately symmetric. Explicitly analyzing where asymmetry matters would strengthen the paper's framing.
- Including NoisyGridWorld results in the main text (currently only in the stripped appendix), as this environment tests robustness to observation noise — one of the paper's stated evaluation questions.
- An additional metric directly measuring MAD error (e.g., mean absolute error in action steps) would complement the correlation-based metrics, since high correlation can coexist with systematic offsets.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: Evaluation measures memorization, not generalization** — Speculative claim not verified from the paper. The paper evaluates across diverse environments with standard metrics; the concern about memorization is not substantiated by anything in the paper text.
- **Harsh Critic: Perfect success rates "strain credibility" due to actuation noise** — The paper states ground-truth MAD is computed over a grid graph (line 217), and planning likely operates over this abstraction rather than raw physics. Without access to the stripped Appendix H, this criticism is speculative.
- **Harsh Critic: TDMadDist "is not a contribution"** — Overstated. TDMadDist outperforms Hilbert and occasionally MadDist (PM Giant Navigate: 0.99 vs 0.93 in Table 1). Exploring TD-style bootstrapping for MAD is a reasonable secondary contribution.
- **Harsh Critic: Results only for subset of environments in main text** — Standard practice; full results are in Appendix F. Not a weakness.
- **Harsh Critic: NoisyGridWorld results absent from main text** — Standard practice for appendix material. Moved to Nice-to-Have.
- **Harsh Critic: Abstract claim broader than demonstrated** — The paper compares against the two most relevant baselines (QRL and Hilbert) for MAD approximation. The claim is appropriately scoped.
- **Harsh Critic: Missing related work (Hartikainen et al., 2020)** — The paper does cite and discuss Hartikainen et al. (2020) on line 38. This criticism is factually incorrect.
- **Harsh Critic: d_simple imposes a strong ordering constraint** — This conflates the identity condition (Q1) with a limitation. d_simple satisfies Q1 (d(x,x)=0) by construction. The critique is a general observation about quasimetrics, not a specific flaw.
- **Strength Finder: TDMadDist as "conceptually interesting extension" elevated to a strength** — While the exploration has some value, its consistent underperformance makes this an overstatement. Not retained as a strength.

## Novel Insights
None beyond the paper's own contributions. The combination of scale-invariant loss with quasimetric distance functions for MAD learning is a sensible and effective synthesis of ideas, but neither the reviews nor cross-checking against the paper text identify genuinely novel insights beyond what the paper itself articulates.

## Suggestions
- Add a MadDist variant with a symmetric Euclidean distance to isolate the quasimetric's contribution and directly validate the importance of asymmetry within the same algorithmic framework.
- Explicitly describe how evaluation state pairs are sampled and consider reporting separate metrics for in-distribution vs. out-of-distribution pairs to strengthen confidence in the results.
- Either diagnose TDMadDist's underperformance (e.g., analyze whether bootstrapping introduces bias or whether the EMA rate is the issue) or reframe it as a negative result with clear lessons about when and why bootstrapping degrades MAD learning.
- Briefly contextualize the perfect planning success rates by noting the planning protocol and success criterion in the main text.
- Fix the seed-count inconsistency between the main text and Figure 3 caption.

## Calibration Anchors Referenced

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| State Chrono Representation (oEzY6fRUMH) | 4.75 | 1 | Weaker: questionable theoretical claims, limited evaluation, unconvincing results |
| Distributional Successor Measure (OMwD6pGYB4) | 5.75 | 1 | Weaker: toy experiments, incremental theory, our paper has more comprehensive evaluation |
| Self-Predictive RL (ms0VgzSGF2) | 6.75 | 1 | Stronger: deeper theoretical framework, but our paper has clearer empirical results |
| π2vec (o5Bqa4o5Mi) | 5.25 | 2 | Weaker: limited analysis, missing ablations, our evaluation is more comprehensive |
| ETD — Episodic Novelty Through Temporal Distance (I7DeajDEx7) | 6.75 | 2 | Comparable but slightly stronger: tighter story, clearer novelty. Our paper has comparable strengths but TDMadDist is underdeveloped |

The paper sits clearly above π2vec (5.25) and the Distributional Successor Measure (5.75), and slightly below ETD (6.75). The core contributions are well-supported, the evaluation is comprehensive across diverse environments with ground truth, and the weaknesses are all minor. Score: 6.5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>