## Summary
This paper proposes MadDist and TDMadDist, two algorithms for learning the Minimum Action Distance (MAD) — the minimum number of actions to transition between states — from state trajectories without rewards or action labels. MadDist combines a scale-invariant loss, a contrastive separation term, and an upper-bound constraint, using quasimetric distance functions to handle asymmetric environments. The paper also introduces a novel simple quasimetric (d_simple) and a benchmark suite with known ground-truth MAD.

## Strengths
- **Scale-invariant loss (Eq. 5) is a concrete, well-motivated improvement.** Normalizing by (j-i) prevents long-distance state pairs from dominating the loss, directly addressing a specific limitation of Steccanella & Jonsson (2022) Eq. 2's raw MSE. The formulation `((d_θ(s_i,s_j)/(j-i)) - 1)^2` is principled and clearly explained at line 143-145.
- **Comprehensive benchmark suite with known ground-truth MAD fills a genuine evaluation gap.** The paper introduces environments spanning discrete/continuous state spaces, deterministic/stochastic dynamics, symmetric/asymmetric transitions, and noisy observations (Section 7, Appendix G), enabling the first systematic evaluation of MAD approximation quality against ground truth where none existed before.
- **Strong empirical results on both representation quality and downstream planning.** MadDist achieves 0.99–1.00 success rates across all six OGBench PointMaze planning tasks (Table 1), decisively outperforming QRL (0.81–0.97) and Hilbert (0.05–0.67), with the gap especially pronounced on asymmetric and stitch environments.
- **Principled handling of asymmetric dynamics through quasimetrics.** The symmetric Hilbert baseline achieves only 0.05–0.55 success on asymmetric environments vs. MadDist's 0.99–1.00 (Table 1), demonstrating that quasimetric formulation is essential for environments with irreversible dynamics.

## Weaknesses

### Fatal
None.

### Major
- **Missing direct comparison to Steccanella & Jonsson (2022) — the immediate predecessor.** MadDist is explicitly described as modifying Steccanella & Jonsson's loss (line 137: "learns state distances using an approach similar to prior work (Steccanella & Jonsson, 2022), but differs in the use of a quasimetric distance function and a scale-invariant loss"). Their Eq. 2 is presented in the paper and MadDist (Eq. 4-7) modifies it with three changes: scale-invariant normalization, contrastive loss, and quasimetric instead of symmetric metric. Without comparing against this baseline, the paper cannot decompose its own contributions — it is impossible to tell whether improvements come from the loss redesign, the quasimetric, or both. QRL and Hilbert are too different in methodology to serve this decompositional role.

- **Which quasimetric is used in the main experiments is never stated.** The paper presents three quasimetric options (d_simple, d_WN, d_IQE) and claims d_simple "outperforms more elaborate quasimetrics" (line 19). However, the main results (Figure 3, Table 1) do not specify which quasimetric was used for MadDist or TDMadDist. The ablation is deferred to Appendix E (line 127, 222). If the main results use IQE, the claimed contribution of d_simple is unsupported by the main paper; if they use d_simple, the comparison to QRL (which uses IQE) confounds two simultaneous changes.

- **Abstract overclaims downstream evaluation scope.** The abstract states MAD "naturally enables critical downstream tasks such as goal-conditioned reinforcement learning and reward shaping." The only downstream evaluation is a planning success-rate task in OGBench PointMaze variants (Table 1). The conclusion (line 261) explicitly defers these: "Having established reliable MAD approximation, it can now be incorporated into downstream tasks, including goal-conditioned planning and reinforcement learning." The planning results are strong, but the gap between abstract promises and actual evaluation is too large.

### Minor
- **TDMadDist underperforms and its contribution is underexplored.** TDMadDist underperforms MadDist in 5/6 Table 1 entries and even underperforms QRL in 3/6. The paper acknowledges this (line 226) but offers only that it "still beats the symmetric Hilbert baseline." Why bootstrapping hurts is not analyzed. The algorithm receives equal section/billing despite being empirically weaker.
- **Ambiguity in data collection policy for OGBench environments.** Line 220 states "Each method was trained for 50,000 gradient steps on an offline dataset gathered by a random policy," but line 218 describes OGBench's navigate dataset as "collected by a noisy expert policy." The paper should clarify whether OGBench results use random policy data or the native OGBench datasets.

### Trivial
None.

## Nice-to-Haves
- The ablation of MadDist with symmetric vs. quasimetric metric should appear in the main text, not just Appendix E, to directly support the paper's thesis about asymmetry.
- A brief discussion of computational cost across quasimetrics would strengthen the claim that d_simple is "computationally efficient" (line 19).
- Testing with non-random behavior policies would demonstrate robustness to the data collection regime.

## Removed Points
These points are flagged to be removed, treat them with caution.
- Formatting/presentation nitpicks (garbled equation at line 171, etc.) — parser artifacts, not author errors.
- Minor seed count inconsistency between figures (3 seeds) and tables (5 seeds) — trivial reporting issue.

## Novel Insights
The paper's most novel insight is the demonstration that scale-invariant normalization is critical for MAD learning — prior work (Steccanella & Jonsson, 2022) used raw MSE which lets long-distance pairs dominate the loss. The benchmark suite with known ground-truth MAD is also a genuinely novel contribution that fills a real evaluation gap in the field.

## Suggestions
1. Add Steccanella & Jonsson (2022) as a baseline to decompose contributions.
2. Explicitly state the quasimetric used in every main-text experiment.
3. Move TDMadDist to an appendix or provide deeper analysis of its failure mode.
4. Add at least one genuine downstream RL evaluation to substantiate the abstract's claims.
5. Clarify data collection policy for OGBench environments.

## Calibration Report

**All retrieved anchors:**
| Round | Path | Avg Score | Comparison |
|-------|------|-----------|------------|
| 1 | CaNp8ALCRT (Drug Discovery MDP) | 3.00 | Weak, unrelated domain — our paper is clearly stronger |
| 1 | Q1Hr9dVfDS (Continual RL) | 3.00 | Poor writing, simple experiments — our paper is clearly stronger |
| 1 | ms0VgzSGF2 (Self-Predictive RL) | 6.75 | Strong theoretical unification, mixed empirical — comparable |
| 1 | cWdAYDLmPa (Unbalanced Atlas) | 6.67 | Unclear motivation, marginal improvements — our paper is stronger |
| 1 | 9pW2J49flQ (DeepLTL) | 8.00 | Well-written, strong experiments, broad evaluation — our paper is weaker |
| 1 | agPpmEgf8C (Predictive Aux Objectives) | 8.00 | Strong neuroscience-RL connection — our paper is weaker |
| 1 | stUKwWBuBm (Tractable Multi-Agent RL) | 8.00 | Strong theory and experiments — our paper is weaker |
| 1 | 7BLXhmWvwF (Geometry-aware RL) | 8.00 | Novel geometry, broad evaluation — our paper is weaker |
| 1 | WQ6rnDriHj (Unified Decision-Making) | 4.75 | Rejected, limited novelty — our paper is stronger |
| 1 | cWdAYDLmPa (Unbalanced Atlas) | 6.67 | Duplicate of above |
| 1 | oEzY6fRUMH (State Chrono) | 4.75 | Rejected — our paper is clearly stronger |
| 2 | skGSOcrIj7 (Neural Spacetimes) | 6.80 | Novel quasimetric embedding, limited downstream eval — comparable, slightly below |
| 2 | V71ITh2w40 (Intrinsic Dimensionality) | 6.20 | Metric embeddings for graphs — tangentially related |
| 2 | cCl10IU836 (Interaction Asymmetry) | 7.00 | Strong theory, good experiments — our paper is slightly weaker |
| 2 | ZkBg5D2lgT (Hyperbolic Manifolds) | 6.25 | Novel geometry, limited eval — comparable |
| 2 | qofh48zW3T (Distributional Distance) | 6.00 | Clear insights, narrow baselines, rejected — our paper is stronger |
| 2 | 5iWim8KqBR (Memory-Efficient AD) | 5.50 | Rejected — our paper is stronger |
| 2 | o5Bqa4o5Mi (π2vec) | 5.25 | Borderline accept — our paper is stronger |
| 2 | G6dMvRuhFr (Grounding Video Models) | 7.33 | Broad evaluation, practical contribution — our paper is slightly weaker |
| 2 | ms0VgzSGF2 (Self-Predictive RL) | 6.75 | Duplicate |
| 2 | o2IEmeLL9r (Pre-Training Goal-based) | 7.33 | Broad downstream eval — our paper is slightly weaker |
| 2 | cWdAYDLmPa (Unbalanced Atlas) | 6.67 | Duplicate |

**Bracketing:** Round 1 bracket: 5.5–7.5. Round 2 narrows to 6.0–7.0.
**Comparison:** The paper is clearly stronger than the 6.0 anchor (Distributional Distance Classifiers, rejected) due to stronger empirical results and a cleaner formulation. It is comparable to the 6.75–6.80 anchors (Unbalanced Atlas, Neural Spacetimes) but has a more meaningful empirical contribution. It falls short of the 7.0–7.33 anchors (Interaction Asymmetry, Pre-Training Goal-based Models) due to narrower baselines and overclaimed downstream evaluation. The score of 6.5 places it above the accept/reject boundary, reflecting a solid paper with genuine contributions and fixable weaknesses.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>