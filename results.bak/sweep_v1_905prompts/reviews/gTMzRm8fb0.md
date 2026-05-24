Now I have enough calibration context. Let me finalize my analysis and write the review.

**Round-1 bracket:** Between 4.0 and 7.5. The weak anchors (2.00–3.40) are clearly weaker papers; the 7.5+ anchors are top-tier theoretical/LLM papers in different areas.

**Round-2 narrowing:** The paper is stronger than the 5.25 anchor (Embedding Collapse, rejected, weaker empirics) and the 5.75 anchor (PreferDiff, accepted, offline-only). Comparable to the 6.00–6.50 range papers in terms of contribution breadth. I place it at **6.0**.

---

## Summary

This paper challenges the prevailing (Multi-)Generator–Evaluator (MG-E) paradigm for ranking in recommender systems. It proves (Theorem 1) that a single sufficiently large generator-only model can achieve strictly smaller approximation error to the optimal ranking policy than any finite MG-E system. To train such a model in practice, it introduces **group-relative optimization**: using a learned reward model to construct a reference policy via group-normalized softmax, then training the generator via cross-entropy against this reference. The resulting system, **GoalRank**, is evaluated on three offline datasets (including an industry dataset) and through large-scale online A/B tests on a platform with >0.5 B daily active users, where it outperforms production MG-E systems across all engagement metrics.

## Strengths

1. **Theoretical result on expressiveness of generator-only models.** Theorem 1 provides the first formal comparison showing that a single larger generator's policy space can strictly dominate a mixture of bounded generators with an evaluator, and that the approximation error to the optimal policy vanishes as model size grows. This gives theoretical grounding to the idea that MG-E is not architecturally necessary.

2. **Novel group-relative training objective.** The derivation from the Boltzmann optimal policy through a biased reward model to a tractable reference policy (Eq. 4–5) is conceptually clean. Using group-mean centering and standard-deviation scaling to mitigate reward bias is a well-motivated heuristic, and the resulting loss is simple to implement.

3. **Comprehensive empirical validation with online A/B test.** The paper goes well beyond standard offline benchmarks by deploying GoalRank on a real platform with >0.5 B DAU. The two-week A/B test shows statistically significant improvements across all business metrics (APP Stay Time +0.149%, Watch Time +0.197%, Effective Views +1.212%). This is the strongest evidence for the practical viability of the approach.

4. **Clear scaling behavior.** Figure 3 demonstrates that GoalRank's performance improves monotonically as model size grows from 1M to 0.1B parameters, while baselines (including scaled MG-E) saturate. This directly validates the theoretical prediction in Theorem 1.

5. **Robustness analysis.** The ablation on reward-model bias (Table 3) and group size (Table 2) shows that GoalRank degrades gracefully and outperforms baselines even under suboptimal configurations, which is important for practical deployment.

## Weaknesses

### Major

1. **Confounded comparison in offline evaluation.** GoalRank's generator is trained on a reference policy derived from the reward model (Eq. 5), while all baselines are trained on standard ranking losses (pointwise/listwise) using historical interaction data. The G-E baselines use the same reward model only at inference time for selection. This means GoalRank benefits from a training signal that is directly aligned with its evaluation proxy (the reward model), while baselines do not. The paper asserts "all baselines share exactly the same evaluator (reward model) as GoalRank," but this only covers the inference-stage evaluator, not the training signal. The large offline gains (+25% H@6 on Industry) are therefore difficult to attribute specifically to the generator-only paradigm vs. simply using the reward model during training. A controlled experiment training a small generator with the same Eq. 5 objective would help isolate the source of improvement.

2. **Offline metrics measure historical match, not utility alignment.** The offline ground truth is the user's chronological last-six interactions. GoalRank is trained to maximize a learned reward model (estimating utility), not to reproduce historical order. There is no demonstrated correlation between the reward model's scores and the historical ranking, so the offline metrics may conflate memorization of behavior patterns with actual ranking quality. The paper does not report reward-model-based offline metrics (e.g., the reward model's own score of output lists), which would be a natural sanity check.

### Minor

3. **Theorem 1 does not connect directly to the training method.** The theorem is an expressiveness result about policy classes at infinite-data, optimal-training limits. It does not provide guarantees about whether the proposed Eq. 5 training objective will realize the theoretical advantage with finite data, nor does it bound the gap between the group-relative reference policy and the true optimal policy. The connection from theory to method is conceptual, not quantitative.

4. **"Evidence upper bound" claim is unclear.** The paper states it "derives an evidence upper bound of the one-stage optimization objective" but no formal bound is presented in the main text. Section 3.2 derives the Boltzmann optimal policy and then constructs a heuristic reference policy; no inequality bounding KL(π\_θ ∥ π\*) in terms of tractable quantities appears in the visible portion. This claim is likely substantiated in the (stripped) appendix, but the main text could be clearer about what exactly is bounded.

5. **No variance or confidence intervals reported for offline results.** The paper states results are averaged over five runs but reports only point estimates. Given the large improvements claimed, standard deviations would help assess reliability.

### Trivial

6. The scaling experiments scale MG-E by increasing the *number* of generators while scaling GoalRank by increasing *model size*. These are the natural scaling axes for each paradigm, but a side-by-side comparison at matched total parameters would strengthen the claim.

## Nice-to-Haves

- Train a small generator-only baseline with the same Eq. 5 objective to isolate whether gains come from the training signal or model capacity.
- Report reward-model-based offline metrics (e.g., average reward-model score of output lists) alongside the historical-match metrics.
- Include standard deviations for the five-run offline results.

## Removed Points

- **"Unfair baseline (structural)" claim about training signal mismatch.** This is kept as a Major weakness (point 1 above), but the characterization as "unfair" or "structural" is too strong. The paper proposes a complete new paradigm (training + inference); comparing it against existing systems with their standard training is valid. The issue is that the source of improvement is confounded, not that the comparison is invalid. The harsh critic's demand that all baselines be retrained with Eq. 5 is a reasonable suggestion for an ablation, not a requirement for a fair system-level comparison.

- **Criticism that Theorem 1 is "trivial" / a "universal approximation statement."** REMOVED. The theorem is non-trivial because it compares different *architectures* (mixture of bounded generators + evaluator vs. single larger generator), showing the single generator's policy space *strictly contains* the mixture's. This goes beyond a simple universal approximation claim. However, the gap between theory and training method is noted as a Minor weakness.

- **Claim that the evaluator/reward model training may have selection bias, position bias, etc.** REMOVED. These are speculative concerns about details deferred to the (stripped) appendix. The paper's robustness ablation (Table 3) partially addresses this by showing graceful degradation under injected Gaussian noise.

- **Criticism about unstated latency/serving cost for the large generator.** REMOVED. The paper mentions latency is discussed in Figure 4 in the appendix. This is an implementation detail, and demanding it as a weakness is scope creep for a research paper.

- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem"). REMOVED. Only concrete, evidence-backed strengths are retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a controlled experiment training a small generator with Eq. 5 to disentangle the effect of the training signal from that of model capacity.
2. Report both historical-match metrics and reward-model-based evaluation scores in offline experiments.
3. Include standard deviations for the five-run results.
4. In a revision, clarify what exactly the "evidence upper bound" bounds — a one-line inequality would suffice.

## Score and Decision

**Round-1 bracket:** The paper clearly exceeds the weak anchor papers (2.00–3.40) on contribution depth and empirical validation. It is below the top-tier theoretical/LLM papers (7.5+) in rigor of theoretical analysis. Initial bracket: 4.0–7.5.

**Round-2 anchors examined in full:**
- *PreferDiff* (5.75, accepted) — weaker empirical validation (offline-only), comparable contribution novelty. **GoalRank is stronger** (online A/B test, more novel theory).
- *Embedding Collapse* (5.25, rejected) — narrower contribution, weaker experiments. **GoalRank is stronger.**
- *MQL4GRec* (6.50, accepted) — similar scope, but lacks online validation. **GoalRank is comparable** with stronger real-world evidence.
- *Learn Your Reference Model* (6.00, accepted) — similar reference-model approach, different domain (LLM alignment). **GoalRank is comparable** in structure and quality.

**Final score:** 6.0. The paper makes genuine contributions (theoretical grounding for generator-only ranking, novel training principle, online validation) but has real weaknesses in experiment design (confounded training signal, misaligned offline metrics) that prevent a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>