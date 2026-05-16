Now I have a thorough understanding of the paper and all reviewer claims. Let me compose the final consolidated review.

---

## Summary

This paper introduces ORSO (Online Reward Selection and Policy Optimization), a framework that treats the problem of selecting among candidate shaping reward functions as an online model selection problem. The method uses bandit/online selection algorithms (ETC, ε-greedy, UCB, EXP3, D³RB) to allocate training iterations across candidate reward functions. The paper provides a regret analysis under an idealized monotonicity assumption (Assumption 4.2), showing that D³RB achieves improved regret bounds, and presents empirical results on six continuous control tasks in Isaac Gym.

## Strengths

- **Framing reward selection as online model selection is sensible and practically motivated.** The paper formalizes a real bottleneck in reward design — the need to evaluate many candidate reward functions — as an exploration-exploitation problem, which is a natural and useful framing. The distinction between reward generation and reward selection phases is clearly drawn.

- **Systematic comparison of five selection algorithms with informative ablation.** The paper compares ETC, ε-greedy, UCB, EXP3, and D³RB (Section 5.3, Figures 4–6), showing that more exploratory algorithms (D³RB, EXP3) outperform greedy methods, and that even simple strategies beat uniform allocation. This ablation provides genuine insight into which algorithms suit the reward selection problem.

- **Empirical results demonstrate ORSO reaches human-level performance faster than uniform allocation.** Across 6 tasks, 3 budgets, and multiple seeds, ORSO with D³RB reaches human-level performance in roughly half the iterations of the naive uniform-allocation baseline (Figure 2, left). The method also scales with budget and outperforms naive selection on large candidate sets (K=48,96, Figure 6).

- **Improved regret analysis under the monotonicity assumption.** Lemma 4.4 shows that under Assumption 4.2, D³RB's regret scales with the true regret coefficient \(d_T^{i_\star}\) rather than the worst-case coefficient \(\bar{d}_T^{i_\star}\), which is a genuine refinement of the general D³RB analysis in Dann et al. (2024).

## Weaknesses

### Fatal
None.

### Major

- **The main empirical baseline ("Naive Selection") is confusingly specified, undermining the headline quantitative claims.** The paper states "We employ EUREKA as a baseline for the naive selection approach" (Section 5.1.1) but then describes naive selection as allocating a fixed number of iterations uniformly across candidates — a description that does not match EUREKA's actual evolutionary algorithm. The central claims that ORSO is "more than twice as fast" (abstract, Figure 2) and requires "up to 16× less compute" (Section 5.2, Figure 3) are measured against this baseline. Because the baseline's implementation is unclear — is it EUREKA's full evolutionary process, or simply uniform allocation after generation? — the significance of these headline comparisons is unclear. The paper would substantially benefit from (a) clarifying exactly what the baseline does, (b) separating the uniform-allocation ablation from a "prior method" comparison, and (c) tempering the claim that speedups are relative to "current methods" rather than to a naive strategy.

### Minor

- **Assumption 4.2 is strong and its practical relevance is not examined.** The assumption requires that the optimal learner's *expected cumulative reward dominates all others at all time steps* and has non-decreasing average performance. The paper does not test whether this holds empirically, nor does it discuss how the algorithm degrades when the assumption is violated. The theoretical contribution is valuable under the stated assumption, but the gap between theory and practice is unaddressed.

- **Only aggregated results are shown; per-task breakdowns are absent.** The paper reports that ORSO "consistently matches or exceeds human-designed rewards, particularly in more complex environments" (Section 5.2), but results are only shown as averages across 6 tasks, 3 budgets, and 3 random seeds (Figure 2). Without per-task data, the reader cannot assess whether the aggregate advantage is driven by a subset of tasks or is consistent across all environments. This is especially relevant given that the PPO hyperparameters were tuned specifically for the human-designed rewards (acknowledged in Sections 5.1 and 5.3), which gives the human baseline a structural advantage that may vary by task.

- **The "twice as fast" claim is complicated by the baseline not reaching the threshold.** The paper states that "the naive selection strategy on average does not manage to select an effective reward function within the limited budget" (Section 5.2). If the naive baseline plateaus below human-level performance, claiming "twice as fast to reach human-level" is comparing against a baseline that never reaches that milestone — making the comparison somewhat ill-defined. The paper should clarify the basis for this computation.

- **Selection algorithm hyperparameters are not reported.** The paper does not specify the ε value for ε-greedy, the learning rate for EXP3, the confidence parameter \(c\) for D³RB, or the value of \(d_{\min}\). These details affect reproducibility and may influence the relative ranking of selection algorithms in the ablation study.

### Trivial
None.

## Nice-to-Haves

- A per-task results table (normalized return for each environment) would substantially strengthen the empirical evaluation.
- A discussion of how the regret bounds degrade when Assumption 4.2 is violated would improve the theory section's honesty.
- Wall-clock time measurements (rather than approximations based on per-iteration time) for the GPU comparison would be more convincing.
- An analysis of how often iterative resampling is triggered and the quality of the generated reward set (e.g., fraction of buggy candidates) would contextualize the selection problem.

## Removed Points

- **Missing comparison against L2R, Text2Reward, etc.:** These are reward *generation* methods, not selection methods. Criticizing the paper for not comparing against a fundamentally different paradigm is scope creep (Soft Rule — scope).
- **Proof not visible in paper body / missing appendix:** Rule 9 — the appendix is stripped by the PDF parser; the proof exists in the original submission.
- **Missing related work on bandit-based reward selection:** Rule 4 — cannot confirm existence of relevant prior work without external sources.
- **Seeds not clearly stated:** Factually incorrect — the paper states 3 seeds for main experiments (Section 5.2) and 5 for the large reward set (Section 5.3).
- **Figure 1 contradicts Assumption 4.2:** Misreading. Figure 1(b) shows a scenario where f² hasn't been trained yet early on, not where it has intrinsically worse expected returns per training iteration. The assumption is about expected rewards given equal training, which the figure does not violate.
- **Human-designed reward baseline is "wrong gold standard":** The paper explicitly acknowledges the hyperparameter tuning advantage (Sections 5.1, 5.3) and addresses it directly. The criticism is already addressed by the paper.

## Novel Insights

The reviews surface an interesting tension: the paper's main claim to practical impact rests on a speedup relative to a baseline that is both weakly specified and probably too weak to be a fair proxy for "current methods." However, the internal ablation study — comparing five selection algorithms on the same candidate set — provides genuine evidence that framing reward selection as an online learning problem is useful, independent of whether the naive baseline is strong or weak. This suggests the paper's real contribution is the problem formalization and the finding that D³RB and EXP3 outperform greedy methods on this task, not the absolute speedup claim.

## Suggestions

1. **Clarify the naive selection baseline.** State explicitly whether the baseline uses full EUREKA evolution or simply samples candidates once and allocates uniformly. If the latter, rename it "Uniform Allocation" and remove the EUREKA reference. Add a separate uniform-allocation baseline that is unambiguously described.

2. **Add a per-task results table** to the main paper (or make the appendix visible). This is essential for readers to assess where ORSO gains and where it does not, especially given the acknowledged hyperparameter bias toward the human baseline.

3. **Temper the headline claims** to reflect what is actually compared. Replace "2× faster than current methods" with "2× faster than uniform allocation" or provide a comparison against a credible prior method.

4. **Discuss the gap between Assumption 4.2 and practice.** Even a brief paragraph acknowledging that the assumption is strong and describing how the method behaves without it would significantly strengthen the theory section.

5. **Report selection algorithm hyperparameters** (ε, learning rate, c, d_min) in the main paper or a table.

## Score and Decision

The paper formalizes a useful problem and provides a clean empirical comparison of online selection algorithms for reward design. The internal ablation study is solid, and the theoretical refinement of D³RB's regret bound is a genuine contribution. However, the paper's headline claims are built on a baseline that is confusingly specified, and the absence of per-task results makes it difficult to assess the robustness of the empirical conclusions. These issues are addressable via revision but are substantive enough that the paper in its current form overclaims relative to the evidence. I recommend revision and resubmission.

**MY FINAL SCORE:** <pineapple>5.5</pineapple>
**MY FINAL DECISION:** <orange>Reject</orange>