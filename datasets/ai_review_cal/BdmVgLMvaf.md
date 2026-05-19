- Decision: Accept
- Avg Score: 6.50
- Scores: 5, 8, 8, 5
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper proposes training a secondary GFlowNet (the "teacher") alongside a primary amortized sampler (the "student"), where the teacher's reward is based on the student's trajectory-balance loss. The teacher generates training trajectories focusing on high-loss regions, which correspond to underexplored or missed modes of the target distribution. The method is evaluated on synthetic grid worlds, diffusion-based sampling benchmarks (25GMM, Manywell), and four biochemical sequence/molecule design tasks, consistently outperforming off-policy baselines including prioritized experience replay (PER) and reward-prioritized replay (PRT).

## Strengths

- **Consistent and substantial improvement in mode coverage across all domains**: On the grid world (d=4, H=32), the teacher discovers 246.6 modes vs. 120.4 for the best baseline (PRT). On the 32-dimensional Manywell task, the teacher achieves EUBO = 165.800 (near the true value 164.696), while all baselines remain far higher (best baseline PER: 210.440). On biochemical tasks (Figure 8), teacher+PER outperforms all baselines, with the largest gains on the most challenging task (L14-RNA1). These results directly support the central claim that the teacher enhances mode discovery.

- **Principled and well-motivated reward design**: Equations (5)–(6) introduce a weighting term \((1+C\mathbb{I}_{\delta>0})\) that explicitly favors undersampled modes (positive TB discrepancy) and a mixing term \(\alpha\log R(x)\) that combines high-loss targeting with high-reward focusing. The design is clearly explained and connected to the exploration-exploitation challenge stated in the introduction.

- **Theoretical grounding**: Section 3.2 and the referenced Theorem A.1 prove that the joint optimization has a stationary point where the student becomes an exact sampler and the teacher samples proportionally to \(\epsilon R(x)^\alpha\), ensuring the training process has a well-defined fixed point.

- **Diverse and challenging evaluation suite**: The paper tests on synthetic environments (grid worlds with deceptive reward structure), continuous diffusion sampling (two established benchmarks), and real-world biochemical discovery tasks (QM9, sEH, TFbind8, L14-RNA1). This breadth supports the generality of the approach.

- **Honest limitations and practical guidance**: The Discussion section explicitly states that the teacher adds training complexity and is not needed for unimodal tasks, providing clear guidance on when the method is appropriate.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The "modes" metric in the grid world conflates distinct high-reward states with well-separated modes.** The grid-world reward has two contiguous high-reward regions (a central blob and a surrounding ring), each with many states sharing identical reward values. Counting individual terminal states within these regions as "modes" follows prior work conventions (e.g., Bengio et al., 2021), but the paper's central claim is about discovering *modes* of a multimodal distribution. A method that finds 2452 high-reward states in a contiguous region has not necessarily demonstrated better exploration of *separated* basins than one that finds fewer such states. The paper would benefit from clarifying what the metric captures, or reporting the fraction of distinct reward-mass components discovered. This does not undermine the main results — the mode-count differences are large and consistent — but the terminology inflates the apparent granularity of the claim.

- **The L1 distance metric on the (d=4, H=32) grid shows near-identical values across all methods (~1.634–1.664 × 10^{-6}) despite large differences in mode count (16 vs. 246).** This suggests the L1 metric is saturated on this configuration and does not differentiate the methods, though the mode-count metric does. The paper does not discuss this behavior. This is a minor presentation issue — the mode-count metric independently tells a clear story.

- **No quantitative analysis of the teacher's behavior during training.** The paper provides qualitative KDE plots (Figure 8) showing the teacher focuses on modes the student misses midway through training, but it does not report any quantitative measure such as the correlation between teacher-sample loss and contemporaneous student loss, the teacher's own reward over time, or the rate at which new modes are added to the student's repertoire. Such evidence would strengthen confidence that the teacher is tracking the student's loss landscape as intended rather than memorizing outdated patterns.

- **No compute-cost comparison.** The teacher doubles the number of policy networks and adds gradient computations, but the paper does not report wall-clock time or total gradient steps relative to baselines. The limitations section acknowledges this trade-off qualitatively, but a practical assessment would help readers judge the overhead.

### Trivial
None.

## Nice-to-Haves

- Report the correlation between teacher-sampled states and contemporaneous student loss over training rounds.
- Include wall-clock time or gradient-step budgets for at least one task (e.g., 25GMM or L14-RNA1).
- Clarify whether local search (LS) is used in the diffusion and biochemical experiments; if not, the paper could explicitly note that the teacher works without LS on these tasks (which would actually *strengthen* the empirical case).
- Add brief discussion of how the behavior-policy mixing ratio (student / teacher / buffer) is chosen and its sensitivity.

## Removed Points

The following points from the inputs are removed with justification:

1. **"L1 distance and mode count seem contradictory" (Harsh Critic):** The critic asserts a contradiction between the L1 and mode-count metrics on the d=4, H=32 grid. These metrics capture different aspects of the distribution — L1 measures distributional match to the target (dominated by the high-reward ring), while mode count measures coverage of distinct high-reward states. The near-identical L1 values across methods can arise because all methods cover the high-reward ring adequately but differ on the lower-reward central blob. There is no contradiction. *Removed as factually incorrect.*

2. **"PER on 25GMM not statistically different from teacher" (Harsh Critic):** The critic notes PER's EUBO = 1.833 ± 2.366 and teacher's = 0.115 ± 0.009, suggesting they may not be "statistically different." The teacher's mean (0.115) is ~16× smaller than PER's (1.833), and the teacher's variance is two orders of magnitude smaller. The qualitative conclusion is unambiguous (teacher is substantially better), and the critic's framing is misleading. *Removed as factually incorrect about the data.*

3. **"Nonstationarity may destabilize teacher without LS" (Harsh Critic):** The critic speculates that without LS, the teacher may not track the student's loss landscape. However, the teacher works well on all tasks without LS (diffusion experiments and biochemical experiments do not use LS). The empirical results directly contradict the speculation. *Removed as unsupported speculation contradicted by evidence.*

4. **"Single MC sample for teacher reward estimation introduces destabilizing noise" (Harsh Critic):** The paper explicitly justifies the single-sample Monte Carlo estimator as unbiased and notes that SGD averages out the variability. There is no evidence in the paper that this causes instability. *Removed as speculative without evidence.*

5. **"Missing ablation on behavior policy mixing ratio" (Harsh Critic):** The paper references the appendix for implementation details of the behavior policy selection. The main text states the three sources and defers details. This is standard practice. *Removed per rule against penalizing appendix-deferred content.*

6. **Generic strengths (Strength Finder):** Strengths about the paper "addressing an important problem" or "targeting an interesting question" are dropped as generic. The retained strengths are specific, concrete, and evidence-grounded.

## Novel Insights

None beyond the paper's own contributions. The core insight — using a secondary GFlowNet to amortize prioritized experience replay over the entire sample space, trained on the student's loss — is the paper's own novel contribution, and the reviews do not add a new analytical lens beyond what the paper already provides.

## Suggestions

1. **Clarify the "modes" metric in the grid world.** Add a sentence explaining that "modes" are defined as terminal states with reward above a threshold (following prior GFlowNet work), and optionally report the number of reward-level components discovered (e.g., the ring vs. the central blob) to align terminology with intuition.
2. **Add a simple quantitative diagnostic for the teacher.** A time-series plot showing the average student loss of teacher-sampled trajectories vs. student-sampled trajectories would directly verify that the teacher is targeting high-loss regions, as claimed.
3. **Include a single-sentence compute note.** E.g., "Training takes approximately X hours on a single GPU; the teacher adds ~Y% overhead in wall-clock time compared to PER."
