Now let me draft the review and run calibration searches.Now I'll run the 5-band calibration searches simultaneously:Let me read a couple of the most comparable anchor papers to calibrate my score:Now I have all the information needed to write the final review.

---

## Summary
This paper proposes two self-supervised algorithms—MadDist and TDMadDist—for learning the Minimum Action Distance (MAD) from state trajectories alone, using asymmetric quasimetric embeddings and a novel scale-invariant loss. The paper also introduces d_simple, a lightweight parameter-free quasimetric, and contributes a benchmark suite covering discrete/continuous and deterministic/stochastic environments where ground-truth MAD values are known, enabling controlled evaluation. MadDist achieves near-perfect planning success rates (1.00±0.00) on multiple large-scale maze environments, decisively outperforming symmetric and quasimetric baselines.

---

## Strengths

- **Scale-invariant loss (Eq. 5) prevents long-distance dominance**: The normalized objective $\left(\frac{d_\theta(s_i,s_j)}{j-i}-1\right)^2$ avoids the bias in Steccanella & Jonsson's squared-error form (Eq. 2), where large index separations dominate. This directly translates to high Pearson correlations (>0.9) and low ratio CV (<0.2) across all evaluated environments (Figure 3).

- **Quasimetric support captures irreversibility where symmetric methods fail**: In asymmetric environments like CliffWalking and KeyDoorGridWorld, Figure 3 shows the Hilbert (symmetric) baseline collapsing to CV >0.35, while MadDist maintains CV ≈0.1. The directionality is architecturally enforced via d_simple (Eq. 3), d_WN, and d_IQE.

- **Downstream planning results are compelling**: Table 1 shows MadDist achieving 1.00±0.00 on PM Large Navigate/Stitch and PM Medium Navigate/Stitch, and 0.99±0.07 on PM Giant Stitch, decisively outperforming all baselines (Hilbert peaks at 0.67; QRL peaks at 0.97).

- **Benchmark suite with known MAD values**: The paper contributes environments spanning noisy observations, stochastic dynamics, and directed/undirected transitions where MAD is computable exactly—a genuine community resource that makes quantitative evaluation possible where prior work relied on proxy metrics.

- **d_simple (Eq. 3) is a practically useful novel quasimetric**: It requires no additional learned parameters beyond the embedding itself, satisfies the triangle inequality and latent positive homogeneity (per Appendix B), and outperforms more elaborate quasimetrics (d_WN, d_IQE) in ablations.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing most direct baseline—Steccanella & Jonsson (2022)**: The paper explicitly positions MadDist as "similar to prior work (Steccanella & Jonsson, 2022), but differs in the use of a quasimetric distance function and a scale-invariant loss" (Section 6.1), even reproducing their loss in Eq. 2. Yet S&J is absent from the experiments. Without this comparison, the paper cannot isolate whether MadDist's gains come from the quasimetric, the scale-invariant loss, or the richer supervision signal. This is the highest-priority evidentiary gap; the paper already contains everything needed to add this baseline.

- **Supervision signal confound with QRL**: Section 7 explicitly acknowledges that MadDist differs from QRL in two simultaneous ways: (a) quasimetric vs. symmetric embedding, and (b) "our method leverages the path distances between arbitrary states in a trajectory," whereas "QRL only uses the locality constraints." The paper's central framing—that asymmetric quasimetrics are the key missing ingredient—cannot be attributed with confidence when the supervision signal simultaneously differs. A symmetric-MadDist ablation (same scale-invariant loss and contrastive term, but L2 distance) in CliffWalking and KeyDoorGridWorld would isolate this directly. Without it, the attribution of improvement to asymmetry is unresolved.

- **Seed count inconsistency**: Section 7 states "All reported results are means over five independent runs (random seeds)," but the caption of Figure 3 explicitly reads "Shaded regions minimum and maximum values across *three* random seeds." This is a factual inconsistency in the submitted manuscript. Given that Table 1 reports standard deviations of 0.24–0.30 for TDMadDist, the actual seed count meaningfully affects result credibility.

### Minor

- **TDMadDist underperformance not explained**: The Discussion concedes TDMadDist "underperforms the MadDist and QRL algorithm," but offers no mechanistic analysis. TDMadDist outperforms MadDist on PM Giant Navigate planning (0.99 vs. 0.93, Table 1) but loses on all stitch tasks. The regime where TD bootstrapping helps vs. hurts is not identified, which limits the contribution of TDMadDist as a standalone algorithm.

- **Figure 3 vs. Table 1 ranking reversal unexplained**: Figure 3 shows MadDist (correlation ≈0.90) slightly outperforming TDMadDist (correlation ≈0.85) on OGBench PM Giant Navigate, but Table 1 reverses this: TDMadDist achieves 0.99±0.05 vs. MadDist's 0.93±0.17. This non-trivial reversal—where a worse embedding accuracy metric leads to better planning success—deserves explicit discussion and suggests the evaluation metrics may not fully capture planning-relevant properties.

### Trivial
None.

---

## Nice-to-Haves

- A symmetric-MadDist ablation (L2 loss with same scale-invariant scaling and contrastive term) in CliffWalking and KeyDoorGridWorld would cleanly isolate the quasimetric contribution from the loss design changes—one experiment, two environments.
- Varying trajectory length in a grid environment to test whether TDMadDist outperforms MadDist when trajectories are short (the natural hypothesis for why TD bootstrapping might help).
- A brief discussion of when MAD (as a lower bound) is a tight vs. loose proxy for task-relevant distance in stochastic environments, expanding on the current conclusion's acknowledgment.

---

## Removed Points
*These points are flagged to be removed, treat them with caution.*

- **d_simple geometric distortion in complex mazes** (Harsh Critic): The critic speculates that in environments without clear linear ordering, d_simple "may force the embedding into distorted shapes." However, empirical results in Figure 3 and Table 1 show d_simple-based MadDist working well in complex OGBench Giant Maze environments. With strong contradicting empirical evidence and no concrete anchor in the paper showing failure, this is speculative.

- **d_max hyperparameter burden** (Harsh Critic): The contrastive term introduces d_max, with details deferred to Appendix D. This is a routine hyperparameter handled per community norms in an appendix; calling it a "practical appeal" issue without evidence of sensitivity is too minor to retain.

- **PointMaze ground-truth approximation as evaluation invalidity** (Harsh Critic): The paper explicitly states "we use in our experiments to approximate the ground truth MAD, by computing the all pairs shortest path using the Floyd-Warshall algorithm over the maze graph" (Section 7). The paper is transparent about this approximation; the critic's framing that it undermines "known MAD values" ignores the explicit caveat. Demoted to non-issue.

- **TDMadDist as "TD learning paradigm"** (Strength Finder): The claim that TDMadDist "demonstrates that TD-style distance learning is viable" is weakened by the paper's own admission that TDMadDist underperforms MadDist on most metrics. Not a strong standalone strength as framed.

---

## Novel Insights

The most noteworthy underappreciated finding is the reversal of relative performance rankings between embedding quality metrics (Figure 3) and downstream planning success (Table 1) for TDMadDist vs. MadDist on PM Giant Navigate. TDMadDist has *worse* Pearson correlation and ratio CV but *better* planning success (0.99 vs. 0.93). This suggests that (a) embedding accuracy as measured by these metrics is not a monotone predictor of planning utility, and (b) the bootstrapped target structure in TDMadDist may impose an inductive bias—possibly smoothing or sharpening distances in ways useful for graph-based planning—that does not manifest in correlation measures against ground-truth MAD. This deserves follow-up: what property of TDMadDist's learned geometry leads to better plans despite lower fidelity to the true MAD?

---

## Suggestions

1. **Add S&J 2022 as a baseline**: Eq. 2 is already in the paper; this comparison directly answers which component drives the improvement.
2. **Add symmetric-MadDist ablation** (L2 + scale-invariant loss, no quasimetric) in CliffWalking and KeyDoorGridWorld—one experiment, directly supports the central claim.
3. **Resolve the 3-vs-5 seed inconsistency** between Section 7 and Figure 3 caption before submission.
4. **Analyze the Figure 3 / Table 1 reversal** for TDMadDist: what geometric property of the bootstrapped embeddings leads to better planning despite lower correlation with ground-truth MAD?

---

## Evaluation on Key Axes

**Originality**: Moderate-to-good. The combination of scale-invariant loss + quasimetric for MAD learning is novel; d_simple is a clean new contribution. The overall framing is an incremental extension of S&J 2022 with technically motivated improvements.

**Importance**: Good. MAD is a practically useful metric for goal-conditioned RL and planning; a reliable learning algorithm for it with a benchmark suite addresses a real gap.

**Claim support**: Moderate. MadDist results are strong, but the central attribution of improvement to quasimetrics is confounded by simultaneous supervision signal changes. The seed inconsistency weakens result confidence.

**Experimental soundness**: Good in structure, but weakened by the missing most-direct baseline and the confound described above.

**Clarity**: Good. The formalism is clean, the paper is well-organized, and the design choices are well-motivated.

**Value to community**: Good. The benchmark suite and d_simple are concrete contributions beyond the algorithms themselves.

---

## Score and Decision

The paper has real and useful contributions—the benchmark suite, scale-invariant loss, d_simple quasimetric, and strong planning results—but the evidentiary case for the central claim (asymmetric quasimetrics are the key missing ingredient) is insufficiently supported due to the missing S&J baseline and the supervision signal confound. The seed count inconsistency is a factual error. These are addressable in revision, not fatal flaws, but they prevent the paper from clearing the acceptance bar at a top venue in its current form.

Score: **5.5** — Borderline reject. The paper is above average in contribution but below the acceptance threshold due to the missing direct comparison and unresolved confound.

---

# Selected Anchors

<related>["I7DeajDEx7", "GwKNdRc9Bj", "oEzY6fRUMH", "s9SVlWOcLt", "1OGhJCGdcP"]</related>

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>