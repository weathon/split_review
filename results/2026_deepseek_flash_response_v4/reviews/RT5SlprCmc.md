## Summary

This paper proposes learning the Minimum Action Distance (MAD)—the minimum number of steps between two states in an MDP—from state-only trajectories, without requiring actions or rewards. The authors introduce MadDist (direct regression with a scale-invariant loss) and TDMadDist (temporal-difference variant), use quasimetric (asymmetric) distance functions to capture directional structure in irreversible environments, and evaluate on a diverse suite of environments where ground-truth MAD is known. MadDist achieves strong empirical results including near-perfect downstream planning success rates.

## Strengths

- **Scale-invariant loss (Eq. 5):** The normalized loss `(d_θ(s_i,s_j)/(j−i) − 1)²` is a well-motivated improvement over the unnormalized MSE in prior work (Steccanella & Jonsson, 2022). It prevents long-horizon state pairs from dominating the loss simply because their absolute errors are larger. This design choice is principled and empirically validated.

- **Strong downstream planning results (Table 1):** MadDist achieves 1.00±0.00 success rates on several OGBench PointMaze variants (Large Navigate, Large Stitch, Medium Navigate, Medium Stitch), decisively outperforming baselines. These results demonstrate that the learned MAD representation translates to effective goal-conditioned planning, not just numerical accuracy.

- **Asymmetric MAD modeling validated on irreversible environments (Figure 3, Section 5):** The KeyDoorGridWorld and CliffWalking environments exhibit inherent asymmetry (key pickup is irreversible; falling off the cliff creates a shortcut). MadDist achieves Pearson correlation ~0.9 while the symmetric Hilbert baseline stalls at ~0.6 on KeyDoorGridWorld, providing direct evidence that quasimetric modeling captures directional structure inaccessible to symmetric methods.

- **Diverse benchmark suite with known ground-truth MAD (Section 7):** The paper constructs environments where the true MAD is known analytically or via Floyd-Warshall, enabling three complementary metrics (Spearman ρ, Pearson r, Ratio CV) for systematic evaluation—a more rigorous setup than prior work on MAD learning.

## Weaknesses

### Fatal
None.

### Major

1. **Seed-count discrepancy (5 vs. 3 seeds).** The Empirical Setup (line 220) states: "All reported results are means over five independent runs (random seeds) to ensure statistical robustness." Yet the Figure 3 caption and alt-text (lines 230, 232, 238, 240) consistently refer to "minimum and maximum values across three random seeds." This is a verifiable internal contradiction. If the figure uses only 3 seeds, the variance signal is substantially weaker than claimed. The standard deviations in Table 1 are also relatively large for several baselines (0.17–0.30), amplifying the concern. The authors must clarify which number is correct and ensure consistency throughout the paper.

2. **Missing comparison against the most natural baseline (Steccanella & Jonsson, 2022).** The paper explicitly identifies Steccanella & Jonsson (2022) as the most closely related prior approach—Eq. 2 reproduces their loss, and the paper states that MadDist "uses an approach similar to prior work...but differs in the use of a quasimetric distance function and a scale-invariant loss" (line 137). Yet this prior method is never evaluated as a baseline. Including it would be the cleanest ablation: it isolates the combined effect of the two claimed improvements (scale-invariant loss + quasimetric support). Without this comparison, it is difficult to attribute performance gains specifically to the proposed changes versus other implementation differences.

### Minor

1. **d_max hyperparameter in the contrastive loss (Eq. 6) is not analyzed.** The contrastive loss L_r sets a target distance d_max for random state pairs, but the paper provides no sensitivity analysis or guidance on how d_max should be set relative to the environment's diameter or the distribution of true MAD values. The paper would be stronger with a discussion or ablation showing robustness to this choice.

2. **TDMadDist's underperformance is not explained.** The paper honestly reports that TDMadDist underperforms both MadDist and QRL (line 226), but offers no analysis of why the temporal-difference bootstrapping hurts rather than helps. Understanding this failure mode would be valuable for future work and would turn a puzzling negative result into a genuine insight.

### Trivial
None.

## Nice-to-Haves
- Include an ablation comparing MadDist with a symmetric distance (e.g., Euclidean with the same scale-invariant loss) to isolate the benefit of the quasimetric component.
- Provide a sensitivity analysis for the d_max hyperparameter.
- Analyze why TDMadDist's TD bootstrapping degrades performance relative to MadDist's direct regression.

## Removed Points
These points are flagged to be removed; treat them with caution:

- **Eq. 9 garbled:** Removed per rule—formatting artifacts from PDF parsing are not author errors; the original submission has the correct equation.
- **d_simple evidence deferred to Appendix E:** Removed per rule—the parser strips appendices; the evidence exists in the original submission.
- **Continuous state evaluation uses discretization:** Removed—the paper is transparent about computing ground-truth MAD via Floyd-Warshall over the discretized maze graph (line 218).
- **Hilbert baseline expected to fail on asymmetric tasks:** Removed—the paper explicitly motivates this baseline as illustrating the limitation of symmetric methods (line 206).
- **"Self-supervised" is an overclaim:** Removed—using step counts j−i as supervision is a standard form of self-supervision; the characterization is not misleading.
- **Coverage analysis not discussed:** Removed—this is a scope-creep request; the paper's setup with random-policy trajectories is standard.
- **"No actions required" claim clarification:** Removed—the paper's assumption that each step corresponds to one decision is standard and clearly stated.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Clarify the number of random seeds used (5 vs. 3) and ensure consistency between main text and figure captions.
- Include a comparison against Steccanella & Jonsson (2022) or, at minimum, an ablation comparing MadDist with a symmetric distance under the same loss.
- Provide a brief analysis of why TDMadDist underperforms MadDist.
- Report statistical significance tests or effect sizes to support comparative claims.

---

### Calibration Analysis

**Round 1 (Bracketing):** Identified plausible range as 5.0–6.5 based on similarity to temporal-distance and metric-learning papers.

**Round 2 (Narrowing):** Compared against six anchor papers in the 4.5–7.5 range.

**Anchor papers retrieved across all rounds:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| Solving Schrodinger Bridge (FjifPJV2Ol) | 3.40 | R1 | Irrelevant topic; rejected; weaker than current paper |
| Stochastic Safe Action Model Learning (5AbtYdHlr3) | 3.00 | R1 | Different topic; rejected; weaker |
| Structured World Models (B7cZvTQsUN) | 3.00 | R1 | Different topic; rejected; weaker |
| State Chrono Representation (oEzY6fRUMH) | 4.75 | R1/R2 | Temporal info for state representations; rejected; weaker—criticized for ad-hoc losses, unconvincing results |
| Distributional Distance Classifiers (qofh48zW3T) | 6.00 | R1 | Goal-conditioned RL distance; rejected due to math rigor concerns; comparable to current paper |
| Physics-informed TD Metric Learning (TOiageVNru) | 6.00 | R1 | Metric learning for planning; accepted; comparable but with mixed reviews |
| Episodic Novelty Through Temporal Distance (I7DeajDEx7) | 6.75 | R1/R2 | Temporal distance for exploration; accepted; cleaner execution than current paper |
| Structured Predictive Representations (sEv6vHIUnu) | 4.80 | R2 | GNN-based representation learning; rejected; weaker |
| Bisimulation Metric for MPC (F07ic7huE3) | 5.50 | R2 | Bisimulation in model-based RL; accepted; **current paper is clearly stronger** (clearer problem, stronger results, more substantial contributions) |
| Bridging State and History Representations (ms0VgzSGF2) | 6.75 | R2 | Theory paper on self-predictive representations; accepted; stronger theoretical contribution |
| State Representation Learning Using Unbalanced Atlas (cWdAYDLmPa) | 6.67 | R2 | Self-supervised representation learning; accepted; comparable but current paper has clearer motivation |

**Final score determination:** The paper is stronger than the 5.50 anchor (Bisimulation Metric for MPC, accepted) due to clearer problem framing, two new algorithms, and stronger results. It is weaker than the 6.67–6.75 anchors (Episodic Novelty, Unbalanced Atlas) due to the seed-count discrepancy and missing baseline, which are concrete issues those papers do not have. The paper is comparable to the 6.00 anchors (Distributional Distance Classifiers, Physics-informed TD Metric Learning) but with different weakness profiles. I place it at **5.5**—a solid paper with real contributions and strong results, held back by a verifiable internal inconsistency and a conspicuous evaluation gap.

**Bracket:** R1 estimated 5.0–6.5; R2 narrowed to ~5.5 based on comparison with the 5.50 (weaker) and 6.67 (stronger) anchors.

**Score:** 5.5 — this reflects that the core contributions (scale-invariant loss, quasimetric support, benchmark suite) are sound and the empirical results are strong, but the seed-count discrepancy and missing baseline comparison are non-trivial issues the authors must address. The weaknesses are fixable and do not threaten the core claims.

**Decision:** Accept — conditional on resolving the seed-count inconsistency and ideally addressing the missing baseline comparison.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>