## Summary

This paper proposes learning the Minimum Action Distance (MAD) — the minimum number of actions needed to transition between states — from state-only trajectories. It introduces two algorithms: MadDist (direct distance learning with a scale-invariant loss and quasimetric distance) and TDMadDist (a temporal-difference variant with bootstrapped targets). It also defines a simple quasimetric ($d_{\text{simple}}$) and a benchmark suite with known ground-truth MAD. Results show MadDist produces accurate MAD approximations that translate to strong downstream planning performance on OGBench PointMaze environments, substantially outperforming the QRL and Hilbert baselines.

## Strengths

1. **Scale-invariant loss (Eq. 5) that prevents distant state pairs from dominating training**: Prior work (Steccanella & Jonsson, 2022, Eq. 2) used an unscaled MSE where estimation errors for far-apart state pairs have larger magnitude simply because the target $(j-i)$ is larger. MadDist replaces this with $(d_\theta(s_i,s_j)/(j-i)-1)^2$, making the loss invariant to the prediction target's scale (lines 143–145). This is a clean, well-motivated improvement.

2. **Asymmetric quasimetric demonstrably captures irreversible dynamics**: In CliffWalking (asymmetric due to cliff shortcut) and KeyDoorGridWorld (asymmetric because keys are never dropped), MadDist achieves substantially lower Ratio CV (~0.1–0.2) than the symmetric Hilbert baseline (~0.35–0.6) (Figure 3). This provides direct quantitative evidence that modeling asymmetry matters and that the proposed methods succeed at it.

3. **Benchmark suite with known ground-truth MAD**: The paper designs environments spanning deterministic/stochastic dynamics, discrete/continuous state spaces, directed/undirected transitions, and noisy observations — all with computable ground-truth MAD (Section 7, lines 210–219). This enables controlled, quantitative evaluation that prior MAD approximation work lacked.

4. **Strong downstream planning performance**: In Table 1, MadDist achieves near-perfect or perfect success rates across all six OGBench PointMaze environments (4 of 6 at $1.00 \pm 0.00$), substantially outperforming both QRL and Hilbert baselines. This translates learned MAD representations into practical planning utility.

5. **Provably valid simple quasimetric**: $d_{\text{simple}}$ (Eq. 3) uses only ReLU operations, satisfies the triangle inequality (proven in Appendix B), and is computationally cheaper than Wide Norm or IQE alternatives, providing a theoretically sound yet efficient building block.

## Weaknesses

### Fatal
None.

### Major

- **Missing the most directly relevant baseline (Steccanella & Jonsson, 2022)**: The paper states that MadDist "learns state distances using an approach similar to prior work (Steccanella & Jonsson, 2022), but differs in the use of a quasimetric distance function and a scale-invariant loss" (lines 137–138). Eq. 2 explicitly describes this prior work's loss. Yet Steccanella & Jonsson is not included as an experimental baseline — the evaluation compares only against QRL and Hilbert (lines 204–206). Without comparing against the symmetric predecessor with the original unscaled loss, the paper cannot isolate whether improvements come from the quasimetric, the scale-invariant normalization, the added contrastive loss, or simply architecture/hyperparameter choices. An ablation isolating (a) symmetric + original loss, (b) symmetric + scale-invariant loss, (c) quasimetric + original loss, and (d) quasimetric + scale-invariant loss (MadDist) would be needed to attribute gains to the specific claimed innovations. This weakens the central claim that the proposed framework outperforms "existing state representation methods."

### Minor

- **Seed count discrepancy between text and figures**: Section 7 (line 220) states "All reported results are means over five independent runs (random seeds)," but Figure 3 captions (lines 230, 232, 238, 240) repeatedly state "Shaded regions indicate minimum and maximum values across three random seeds." These statements are contradictory and should be resolved.

- **Stochastic/noisy evaluation results deferred to appendix**: The abstract and Section 7 (lines 190–191) advertise evaluation on environments with "stochastic dynamics" and "noisy observations," yet NoisyGridWorld — the only environment described as having both stochastic transitions and observation noise (line 214) — does not appear in Figure 3 or Table 1. The main paper's results thus only show deterministic/nearly-deterministic environments, making it difficult to assess robustness claims from the main paper alone.

- **TDMadDist's contribution is unclear**: TDMadDist generally underperforms MadDist across reported metrics (e.g., OGBench Large Stitch: 0.73 vs. 1.00, Table 1). While the paper acknowledges this (line 226), it does not analyze why or identify a setting where the TD variant is preferable. A second algorithm that is consistently weaker needs better motivation.

- **Perfect success rates with zero variance warrant discussion**: In Table 1, MadDist achieves $1.00 \pm 0.00$ (std exactly zero across five seeds) in four of six OGBench PointMaze environments. While this could reflect genuine success, the result should at minimum discuss whether the downstream planning task has ceiling effects that limit discrimination between methods.

### Trivial
None.

## Nice-to-Haves
- Report wall-clock time or compute requirements to compare the computational profiles of IQE, Wide Norm, and $d_{\text{simple}}$ quasimetrics.
- Analyze data coverage adequacy — a random policy with 100 or 1000 trajectories may not cover the state space evenly, especially in large mazes.
- Situate $d_{\text{simple}}$ relative to existing asymmetric norms in the quasimetric literature (e.g., Asymmetric L1, skewed norms).

## Removed Points
*These points are flagged to be removed, treat them with caution.*

- **"Hilbert baseline may be a straw man"** (Harsh Critic): The paper explicitly states (line 206) that this baseline is included "to demonstrate the benefits of methods that explicitly model the quasimetric nature of the MAD over those that do not." This is intentional and properly motivated; the comparison is informative.

- **"d_simple outperforms more elaborate quasimetrics claim unsubstantiated in main paper"**: The evidence for this claim is in Appendix E. Per the review rules, weaknesses about content deferred to the appendix are removed since the parser strips appendix sections from all papers — the evidence exists in the original submission.

- **"Cannot be independently verified" / reproducibility concerns about cited references**: The rules prohibit questioning the existence or availability of cited models, tools, or references.

- **Generic formatting nitpicks, typos, and parser artifacts**: Not author errors.

- **General "evaluation lacks rigor" / "scope creep" concerns**: Not specifically anchored to paper content; removed per filtering discipline.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Add Steccanella & Jonsson (2022) as a baseline** with both the original symmetric metric and original unscaled loss. Include ablations isolating the effect of each proposed modification (quasimetric, scale-invariant loss, contrastive loss). This is the single highest-leverage improvement.

2. **Resolve the seed-count inconsistency**: Clarify whether the main results use 3 or 5 seeds and ensure consistency throughout the paper.

3. **Include NoisyGridWorld results in the main paper** to substantiate the abstract's claims about robustness to stochasticity and noise.

4. **Either demonstrate a setting where TDMadDist excels** (e.g., under partial observability or longer horizons) or move it to the appendix as an ablation.

5. **Discuss the ceiling-effect interpretation** of the $1.00 \pm 0.00$ results in Table 1.

---

## Calibration

**Round 1 — Bracketing:**
- Low band (avg < 3.5): Queried "learning minimum action distance from trajectories asymmetric metric quasimetric." Anchors: Schrodinger Bridge Problem (3.40), Beyond Dynamics Conservation (3.00), Discovering Global Minima (2.60), Stochastic Safe Action Model Learning (3.00). Our paper is clearly above this band.
- Middle band (3.5–7.5): Queried "quasimetric learning asymmetric distance reinforcement learning state embedding." Anchors: State Chrono Representation (4.75), Weak Bisimulation (3.75), Distributional Distance Classifiers (6.00), Metric Node Embeddings (6.20).
- High band (>7.5): Queried "minimum action distance MAD learning state representation from trajectories." Anchors: Predictive aux objectives in deep RL (8.00), Intervention Extrapolation (8.00), Time-lagged Information Bottleneck (8.00), Interpreting Emergent Planning (8.00). Our paper is below this band.
- **Initial bracket: 4.0–6.5**

**Round 2 — Narrowing:**
- Query (3.5–6.0): "learning distance metric state representation reinforcement learning from trajectories" — Exploiting Action Distances (3.75), BS-MPC (5.50), plus previously retrieved State Chrono (4.75), Weak Bisimulation (3.75).
- Query (5.5–8.0): "quasimetric asymmetric distance function state embedding MDP" — Quantum-Inspired RL (5.75), STARC Reward Differences (6.50), plus previously retrieved Metric Node Embeddings (6.20), Distributional Distance Classifiers (6.00).

**Key anchor comparisons (read in full):**
- *BS-MPC (5.50, Accept)*: Integrated bisimulation into TD-MPC; reviewers found it incrementally novel ("just adding a loss"). Our paper has more substantial methodological novelty (two algorithms, new quasimetric, benchmark suite) but has a missing baseline gap that BS-MPC did not have.
- *Distributional Distance Classifiers (6.00, Reject)*: Mixed reviews (6,8,5,3,8) with interesting ideas but unclear writing and some questionable claims. Our paper is comparably structured but better written.
- *Metric Node Embeddings (6.20, Accept)*: Strong theoretical proofs, scalable algorithms, clear contributions. More theoretically mature than our paper.
- *State Chrono Representation (4.75, Reject)*: Ad-hoc losses, unconvincing results, grandiose claims. Our paper is significantly stronger.

**Final score determination:** The paper is clearly above the 3.75–4.75 band (State Chrono, Weak Bisimulation, Exploiting Action Distances). It is comparable to BS-MPC (5.50) in overall quality but has a more significant missing-baseline gap; conversely, it has more methodological novelty. It falls below the 6.20 Metric Embeddings paper in theoretical polish. The fixable nature of the major weakness (adding one baseline) suggests the paper has solid potential. Score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>