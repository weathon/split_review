Now let me write the final consolidated review.

## Summary

This paper proposes learning the Minimum Action Distance (MAD) — the minimum number of actions needed to transition between states — from state-only trajectories, without requiring actions or rewards. The authors introduce two algorithms (MadDist and TDMadDist) that use quasimetric distance functions to capture asymmetry in environments with irreversible dynamics, along with a simple new quasimetric (d_simple) and a scale-invariant loss. Experiments on grid-world and continuous maze environments show that MadDist recovers MAD more accurately than QRL and a Hilbert-space baseline, and that the learned distances translate to near-perfect planning success on OGBench PointMaze tasks.

## Strengths

1. **Well-motivated problem and clean formulation.** The paper carefully defines MAD through a linear programming lens (Equation 1), connects it to the all-pairs shortest-path problem, and clearly explains why MAD differs from policy-dependent temporal distances. The contrast between symmetric metrics and the asymmetric quasimetric approach is well articulated (Section 5).

2. **Scale-invariant loss is a principled design choice.** The main objective in Equation 5 normalizes the squared error by the temporal distance \(j-i\), preventing far-apart state pairs from dominating the gradient simply because their error magnitude is larger. This directly addresses a limitation in prior work (Steccanella & Jonsson, 2022) and is clearly motivated. (Section 6.1, Equation 5.)

3. **Strong planning downstream results.** On OGBench PointMaze environments, MadDist achieves success rates of \(1.00 \pm 0.00\) on four of six tasks, decisively outperforming QRL (best \(0.97 \pm 0.09\)) and the Hilbert baseline (best \(0.67 \pm 0.28\)). This demonstrates that the learned distance is practically useful for goal-oriented planning. (Table 1.)

4. **Benchmark suite with known ground-truth MAD.** The paper introduces environments (NoisyGridWorld, KeyDoorGridWorld, CliffWalking, PointMaze variants) where the true MAD is computable, enabling rigorous quantitative evaluation using Spearman correlation, Pearson correlation, and Ratio CV — a level of precision absent from prior MAD-learning work. (Section 7, Figure 3.)

## Weaknesses

### Major

1. **Abstract claims about stochastic/noisy environments are not supported in the main text.** The abstract and introduction prominently claim the method works across "deterministic and stochastic dynamics…and environments with noisy observations." However, Figure 3 and Table 1 — the only main-text results — cover only KeyDoorGridWorld (deterministic discrete), CliffWalking (nearly deterministic), and OGBench PointMaze (deterministic continuous). The NoisyGridWorld environment, which has stochastic transitions and noisy 4D observations, is described (Section 7, line 326) and included in the empirical setup, but zero results for it appear in the body. The paper defers to Appendix F for "full results." For a central advertised claim, the absence from the main paper is a structural gap rather than a minor omission.

2. **The claimed superiority of the proposed quasimetric `d_simple` is not substantiated in the main text.** The paper asserts (Section 1, lines 23–24) that `d_simple` "outperforms more elaborate quasimetrics in the existing literature." Yet no direct comparison of `d_simple` against Wide Norm or IQE appears in the main body — the comparison of MadDist (which uses `d_simple`) vs. QRL (which uses IQE) is an indirect algorithmic comparison, not an ablation of the quasimetric itself. The paper points to Appendix E, but a central novelty claim should have representative evidence in the main text. (Section 5, line 185; Section 7, line 334.)

### Minor

3. **Inconsistent reporting of random seeds.** Section 7 (line 332) states: "All reported results are means over five independent runs (random seeds)." The caption of Figure 3 (lines 342, 344, 350, 352) repeatedly says "Shaded regions indicate minimum and maximum values across three random seeds." This discrepancy is unexplained and undermines confidence in experimental reporting. If it is a typo, which number is correct? If Figure 3 used only 3 seeds, the variance estimates are weaker than claimed.

4. **Planning evaluation covers only one environment family.** Table 1 shows planning success rates only on OGBench PointMaze variants. The claim that "the high accuracy of the learned distance metric directly translates to superior performance in the goal-oriented planning" (lines 338–339) would be stronger if supported by planning results on at least one grid-world environment (e.g., CliffWalking or KeyDoorGridWorld). Without this, it is unclear whether the planning benefit generalizes beyond maze navigation.

5. **TDMadDist underperforms MadDist without a clear rationale for inclusion.** The paper acknowledges that "TDMadDist underperforms the MadDist and QRL algorithm" (line 338), but offers no analysis of when or why the TD variant might be beneficial. Since TDMadDist consistently underperforms MadDist across all presented environments, its inclusion dilutes the contribution. Either a discussion of conditions under which bootstrapping helps (e.g., longer horizons, sparse coverage, stochastic settings) or removal would strengthen the paper.

### Trivial

6. **Equation 9 is garbled by the parser** (`d_theta(s_i, s_{i+1} + d_{theta'}(s_{i+1}, s_r) - 12(9)))` — clearly a formatting artifact; the surrounding text explains the intended meaning, but a clean equation should appear in the original.

## Nice-to-Haves

- A discussion of what happens when trajectory coverage is poor (states that never co-occur within a trajectory). The method assumes trajectories provide enough state pairs to infer MAD, but this is not analyzed.
- A simple baseline comparison to shortest-path distances on the observed trajectory graph (graph from consecutive state pairs + Dijkstra) would isolate the value of the learned embedding.
- An ablation of the scaling factor in Equation 5 (unscaled version) to show whether it matters empirically.
- The planning results would benefit from confidence intervals that account for the number of test episodes per seed, not just standard deviation over seeds.

## Removed Points

- **Criticism that claims are "not supported in the main paper" about NoisyGridWorld** — Kept as Major Weakness 1 (it is a genuine gap). However, the harsh critic's framing as "structural flaw" is accurate; I demoted from "fatal" to "major" because the results exist in the appendix and the method itself is not invalidated.
- **Criticism that Equation 9 is a "reproducibility risk"** — Removed. The harsh critic acknowledges it is a parser artifact. The text explains the intended semantics. This is not a paper error.
- **Strength about d_simple outperforming more elaborate alternatives** — Weakened and moved. The Strength Finder cites this as a strength with evidence "assumed present" in Appendix E. Since we cannot verify the appendix, and the main text lacks direct evidence, this strength is downgraded. The indirect evidence (MadDist vs QRL in Figure 3) is real but conflates algorithm and quasimetric, so it is mentioned in the context of Major Weakness 2.
- **Harsh critic's point about QRL being "designed for quasimetric RL, not specifically for MAD"** — Removed. The paper uses QRL as a baseline for MAD learning, which is entirely appropriate regardless of QRL's original design intent.
- **The criticism about shaded regions being "based on only three runs" and "insufficient for reliable comparison"** — Subsumed into Minor Weakness 3 (seed inconsistency). The underlying statistical concern is valid but the critic's tone overstates it; the seed count (3 vs 5) is the primary issue, and fixing that addresses the concern.
- **Strength Finder's generic strength about "addressing an important problem"** — Removed as generic/superficial. The retained strengths are concrete.

## Novel Insights

None beyond the paper's own contributions. The two reviewers' assessments are largely convergent on the paper's key strengths (well-motivated formulation, strong planning results) and weaknesses (missing main-text evidence for stochastic settings, unsupported quasimetric claim, seed inconsistency). No reviewer identified a weakness the paper's authors would be surprised by.

## Suggestions

1. Move NoisyGridWorld results (at least one summary figure or table) from Appendix F into the main paper to substantiate the advertised robustness claims.
2. Include a small table or figure comparing `d_simple`, Wide Norm, and IQE within the MadDist algorithm in the main text, or add a clear paragraph summarizing the ablation.
3. Reconcile the seed-count inconsistency (5 vs. 3) with a clear statement.
4. Either remove TDMadDist or add an analysis of when bootstrapping helps (e.g., longer-horizon or sparse-coverage settings).
5. Add planning results for at least one grid-world environment (e.g., CliffWalking).
6. Add a limitations paragraph discussing coverage requirements and the impact of poor trajectory coverage.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Three queries for "learning minimum action distance or temporal distance from trajectories" at score bands (0–3.5), (3.5–7.5), and (7.5+). Weak anchors averaged ~2.9 (rejected papers with thin experiments or unclear methods). Middle anchors averaged ~4.8 (range 3.75–6.75). Strong anchors averaged ~8.2 (accepted papers with strong theory/experiments). The paper clearly sits in the middle band. **Initial bracket: 4–6.5.**

**Round 2 (Narrowing):** Two targeted queries — "quasimetric or asymmetric distance learning from trajectories" (4.5–6.5) and "minimum action distance temporal distance representation learning" (5.5–7.5). Key anchors read in full:

- **Episodic Novelty Through Temporal Distance** (6.75, accepted Poster) — Also learns temporal distances, uses contrastive learning. Compared to this paper: ETD has more extensive experiments across more environments and cleaner presentation, but its core innovation is less novel (closely follows prior work on successor distances). The current paper has a more novel problem framing (MAD from state-only trajectories) but weaker experimental presentation (missing key results in main text, seed inconsistency). The current paper is notably weaker on presentation rigor than this anchor.

- **Contrastive Difference Predictive Coding** (7.00, accepted Poster) — Derives TD variant of InfoNCE for goal-conditioned RL. Strong theory, extensive experiments, but had its own issues (3 seeds, hyperparameter concerns). Still, the experiments were broader and more thorough than the current paper's main-text presentation. Current paper is below this anchor.

- **Reinforcement Learning with Elastic Time Steps** (3.75, Rejected) — Unclear method, thin experiments, poor clarity. The current paper is substantially stronger than this anchor.

- **Various other middle-band papers** (4.6–6.0) — These are generally rejected or borderline papers with interesting ideas but incomplete evaluation or presentation gaps.

**Final calibration:** The paper is clearly above the 3.75 rejected anchor but below the 6.75 accepted Poster anchor. The core contribution is sound and the method works, but the main-text presentation has significant gaps (missing evidence for key claims, seed inconsistency, narrow planning evaluation). These are fixable but as-is they prevent the paper from reaching the acceptance threshold. The paper is closest to the 4.75–5.25 rejected/borderline papers in the middle band — papers with solid ideas but incomplete evidence in the submission format.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>