Now I have a thorough understanding of the paper. Let me synthesize the final consolidated review.

## Summary

The paper proposes Plasticity-Driven Sparsity Training (PlaD), a dense-to-sparse training method for deep RL that uses periodic replay buffer reset to preserve neural plasticity and dynamic weight rescaling (DWR) to stabilize training. It is motivated by observations that dense training in DRL induces increasing implicit sparsity (measured by a proposed Weight Shrinkage Ratio) and that sparse-to-sparse methods compound plasticity loss by enforcing high sparsity from the start. On MuJoCo locomotion tasks with SAC, PlaD (built on simple iterative magnitude pruning) achieves the best performance among sparse training baselines in 10/12 tasks at ≥85% sparsity, frequently matching or exceeding the dense model's normalized performance.

## Strengths

- **Novel and practical method combining memory reset with sparse DRL training.** The idea of periodically emptying the replay buffer (rather than resetting network weights as in prior work) to improve plasticity is clean, computationally lightweight, and distinct from existing approaches (Nikishin et al., 2022; Sokar et al., 2023). The ablation (Table 1) cleanly separates the contributions: memory reset drives most of the performance gain, while DWR primarily reduces variance.

- **Strong empirical results at high sparsity levels.** In Figure 5, PlaD outperforms all baselines (Random, Magnitude, Static Sparse, SET, RigL, RLx2) in 10/12 tasks at ≥85% sparsity on 4 MuJoCo environments. For example, at 90% sparsity on HalfCheetah, PlaD reaches 99.2% of dense performance vs. 82.5% for the best baseline (RLx2 at 3M steps). These results convincingly demonstrate that the dense-to-sparse paradigm, when enhanced with plasticity-preserving mechanisms, can outperform sparse-to-sparse methods at the same sparsity level.

- **DWR is a simple and effective stabilizer.** Figure 4 shows that PlaD without DWR exhibits higher critic loss variance and lower Q-values; Table 1 confirms that removing DWR degrades performance and increases variance across tasks. The technique is straightforward (essentially weight normalization applied to the pruned weights) and clearly justified by the instability introduced by combining memory reset with sparse training.

- **Ablation study (Table 1) isolates each component's role.** Comparing PlaD, PlaD (w/o DWR), and PlaD (w/o Reset) shows that memory reset is the primary driver of performance gains while DWR primarily reduces variance, cleanly validating the design rationale.

## Weaknesses

### Fatal
None. The paper's core claims are supported by the experimental design, even though some individual elements could be strengthened.

### Major

- **The claimed connection between sparsity and plasticity loss (Section 4) is asserted rather than rigorously established.** The paper introduces the Weight Shrinkage Ratio (WSR), which measures the proportion of weights whose magnitude decreased between checkpoints, and uses its upward trend (Fig. 2) and the increasing feasible pruning ratio (Fig. 3) to motivate a link to plasticity loss. However:
  - WSR measures weight magnitude trends — it is not a direct plasticity metric. No established plasticity diagnostics (e.g., dormant neuron ratio from Sokar et al. (2023), rank collapse from Kumar et al. (2021), or ability to fit a new task) are computed.
  - The increasing feasible pruning ratio shows the network becomes more compressible during training, which is a well-known phenomenon (consistent with the Lottery Ticket Hypothesis) and does not itself constitute evidence of plasticity *loss*.
  - The paper never directly tests whether *starting* sparse harms plasticity more than *gradually becoming* sparse — this is the core motivation for preferring dense-to-sparse over sparse-to-sparse, but it is asserted without experimental support.

  This weakens the paper's motivational framing. The method may still be effective for other reasons (e.g., the reset mechanism improves data diversity), but the claimed theoretical insight linking sparsity and plasticity is not convincingly demonstrated.

- **The memory reset mechanism is underspecified, hindering reproducibility.** The paper states "we periodically reset the replay buffer to empty (0.2M)" — the reset frequency (interval or schedule) is not reported, and the meaning of "empty (0.2M)" is ambiguous (does the buffer empty to a *capacity* of 0.2M, or is it emptied and then samples collected until reaching 0.2M?). The number of resets performed over the 1M training steps is also not given. These are not trivial details — they are necessary for understanding and reproducing the method.

### Minor

- **No learning curves or training dynamics plots are shown for the main experiments (Fig. 5).** Only final normalized performance at the end of training is reported. Without episodic return vs. environment steps, it is impossible to assess whether PlaD's gains come from faster initial learning, better asymptotic performance, or avoidance of performance collapse. This is especially important given the periodic resets, which could cause temporary dips in performance that the current evaluation hides.

- **The WSR definition (Definition 4.1) has a notation issue.** The formula uses $|h_{t,i}^l(x)|$ with an explicit dependence on input $x$, but $h$ is defined as the *weight vector* — weights do not depend on the input. The expectation over $\mathcal{D}$ suggests the authors may be computing something layer-activation-based, but the notation conflates weights and activations. This makes the definition harder to interpret than it needs to be.

- **The claim that "shrinkage persists across various activation functions" (Section 4.2) is stated without quantitative evidence.** The paper mentions testing Leaky ReLU and Sigmoid and reports that the pattern is "consistent," but no figures or tables are provided. This weakens the generality claim.

- **Fig. 4 (DWR stabilization) does not specify which task was used** — only one task is shown, and the caption does not identify it. While the ablation table provides across-task evidence, the main visual for DWR's effect would be more convincing if the task were named or if multiple tasks were shown.

- **The paper reports that PlaD exceeds 100% of dense performance (e.g., ~130% on Walker2d) without discussing whether the dense SAC baseline is converged at 1M steps.** While 1M steps is the community standard for MuJoCo SAC, the claim of *surpassing* dense performance would be strengthened by verifying that the dense model is near-optimal (longer training or comparison to published SOTA raw returns). As presented, the normalized numbers are useful for relative comparison but the absolute interpretation (especially "exceeding dense") is less clear.

### Trivial

- The abstract contains a duplicated sentence ("We assess PlaD on various MuJoCo locomotion tasks.") — clearly a parser artifact, not an author error.
- Table 1 and the main text report results with only 5 seeds. This is standard for the field, so not a weakness per se, but the standard deviations on some conditions (e.g., Ant-v4 PlaD w/o DWR: 62.5% ± 12.3%) are large enough that more seeds would increase confidence.

## Nice-to-Haves

- Report PlaD's performance at 3M steps to enable a fully controlled comparison with RLx2 (3M), which would further strengthen the claim that PlaD's paradigm is computationally efficient.
- Include direct plasticity measurements (dormant neuron ratio, ability to fit new targets) comparing PlaD, dense training, and sparse-to-sparse baselines to substantiate the plasticity-preservation claim.
- Add wall-clock time and FLOPs comparison to support the computational efficiency claims.
- Provide a sensitivity analysis on reset frequency and buffer size after reset.
- Report raw episodic returns alongside normalized values so readers can assess absolute performance.

## Removed Points

**These points are flagged to be removed, treat them with caution.**

1. **"Comparison to RLx2 is confounded by different training steps"** — The paper explicitly includes both RLx2 (1M) and RLx2 (3M) and is transparent about the step counts. The paper's claim about sparse-to-sparse requiring more steps is supported by the underperformance of RLx2 (1M) relative to RLx2 (3M). Removing this because the paper already addresses the concern.

2. **"The small buffer vs. reset buffer comparison is confounded"** — The critic argued that this comparison conflates buffer size and reset strategy, but Fig. 6 directly compares the same buffer size (0.2M) with vs. without reset. This is a properly controlled experiment. Removing this as the critic misread the experimental design.

3. **"5 seeds insufficient for Ant-v4 results"** — 5 seeds is the standard in the DRL literature for MuJoCo experiments. The reviewer's standard deviation concern is valid but applies to the field as a whole, not just this paper. Removing as a nitpick about standard practice.

4. **"Missing recent DRL-specific sparse training baselines beyond those cited"** — The reviewer does not name specific missing methods. The paper already covers the main paradigms (Random, Magnitude, Static Sparse, SET, RigL, RLx2). Removing due to vagueness.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the authors themselves did not articulate. The key tension is between the paper's strong empirical results (PlaD genuinely outperforms baselines at high sparsity) and its weaker motivation (the sparsity-plasticity link is asserted rather than proven). This is a gap the authors could address with additional measurements, not a contradiction that invalidates the work.

## Suggestions

1. **Tone down the motivational claim.** Replace "establish a connection between sparsity and plasticity loss" with "observe that dense training leads to increasing weight shrinkage and compressibility, which parallels known plasticity-loss phenomena." This would accurately reflect what Section 4 demonstrates.

2. **Specify the reset schedule.** Report the exact frequency of memory reset (e.g., every N steps, or at specific checkpoints) and clarify "empty (0.2M)" to resolve the ambiguity.

3. **Add learning curves.** Include episodic return vs. environment steps for the main experiments (Figure 5) with reset points marked, so readers can assess training dynamics and rule out catastrophic forgetting.

4. **Fix the WSR notation.** Remove the dependence on input $x$ from $h_{t,i}^l(x)$ — the weight values at step $t$ do not depend on the input — or clarify if the metric is actually computed on activations/neuron outputs rather than weights.

5. **Add raw return values.** Report the raw episodic returns alongside the normalized values so readers can assess absolute performance and compare to published results outside the paper's normalization scheme.

6. **Verify dense baseline convergence.** Show that the vanilla SAC baseline at 1M steps is near its asymptotic performance (e.g., by running a subset of tasks to 3M steps and reporting the additional gain) to strengthen the claim that PlaD genuinely matches or exceeds dense performance.

## Score and Decision

This is a borderline paper. The core method (PlaD) is novel and produces strong empirical results — outperforming a comprehensive set of baselines at high sparsity levels across multiple environments. The ablation study cleanly validates the design choices. The DWR component is simple yet effective. These are real contributions.

However, the paper's motivational framing overreaches: the claimed link between sparsity and plasticity loss is not experimentally established, and the WSR metric does not directly measure plasticity. The memory reset schedule is underspecified, and the absence of learning curves obscures training dynamics. These issues are addressable but lower the confidence in the paper's conclusions as presented.

The paper would benefit from a more modest framing and additional experimental details. In its current form, it is on the boundary between accept and reject depending on the reviewer's tolerance for motivational overclaiming versus appreciation of the empirical contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>