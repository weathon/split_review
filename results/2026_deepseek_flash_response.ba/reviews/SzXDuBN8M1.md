I have sufficient calibration data. Let me produce the final consolidated review.

## Summary

TD-JEPA proposes a temporal-difference (TD) latent-predictive representation learning method for zero-shot unsupervised RL. It jointly trains state and task encoders, policy-conditioned predictors, and latent-space policies via a TD-based self-predictive loss that operates on off-policy, reward-free transitions — overcoming the on-policy and single-policy limitations of prior latent-predictive methods. Theoretically, it connects latent-predictive learning to successor-measure factorization under idealized assumptions. Empirically, it evaluates across 65 tasks in 13 datasets from ExoRL and OGBench, showing strong results particularly on pixel-based domains where it achieves an ~8% improvement over the next best method on DMC_RGB.

## Strengths

1. **Novel TD-based latent-predictive loss for multi-policy, off-policy zero-shot RL.** Prior latent-predictive methods were limited to one-step, single-policy, or on-policy settings. TD-JEPA's formulation (Eq. 7→9) enables training from any offline reward-free dataset with sampled actions, which the paper explicitly identifies as a limitation of prior work (lines 17–18, 88–92). This is a genuine algorithmic advance.

2. **Gradient-matching theorems connecting latent-prediction to successor-measure approximation.** Theorem 3 proves that, for fixed representations under tabular assumptions, the optimal predictors and gradients of the TD-JEPA loss match those of explicit forward/backward TD losses for the successor measure. Theorem 1 establishes the analogous result for the MC case. The paper correctly notes this "generaliz[es] and impl[ies] all previous guarantees" (line 157) for latent-predictive analyses, extending prior single-step/single-policy results to the multi-policy TD setting.

3. **Non-collapse guarantee for the doubly-latent-predictive TD setting.** Theorem 2 proves that under a continuous-time relaxation, covariance matrices remain constant over time, preventing collapse. The paper correctly identifies this is more complex than prior proofs (Tang et al., 2023) because the TD target is doubly latent-predictive.

4. **Comprehensive and rigorous empirical evaluation.** The paper evaluates on 65 tasks across 13 datasets (ExoRL + OGBench), 7 baselines, 2 observation modalities. On DMC_RGB, TD-JEPA achieves 628.8 ± 5.5 vs. next-best 582.4 ± 9.8 (BYOL-γ*), an ~8% improvement, with even larger margins on individual domains like walker (738.9 vs 648.3). The probability-of-improvement analysis (Fig. 2) provides rigorous bootstrap-based statistical comparison showing TD-JEPA is consistently among top performers across diverse settings, avoiding the narrow-specialization pattern of many baselines.

5. **Frozen representations enable fast downstream adaptation.** Figure 4 shows that TD-JEPA's pre-trained state encoder, kept frozen during fine-tuning, often matches or exceeds training from scratch in sample efficiency, demonstrating additional practical value beyond zero-shot performance.

## Weaknesses

### Fatal
None.

### Major

1. **BC regularization in OGBench is insufficiently documented.** Footnote 4 (line 249) states "We additionally apply BC regularization in OGBench based on Park et al. (2025b), as detailed in App. E.6" — but Appendix E is not visible in the submission. The core ambiguity is whether this regularization was applied uniformly to all methods or only to TD-JEPA. Given that OGBench uses low-coverage data where BC regularization likely helps significantly, this affects the interpretability of the OGBench results (Table 1). The paper states "each method is tuned over comparable hyperparameter grids and adopts the same architecture" (line 247), which suggests uniform treatment, but this should be explicitly clarified rather than relegated to a footnote referencing an inaccessible appendix.

2. **Theory-practice gap is substantial and downstream claims are presented without sufficient hedging.** The theoretical analysis (Theorems 1–4) assumes orthonormal representations (A1), uniform state distribution (A2), symmetric transition matrices (A3), linear predictors, and a tabular setting. The paper acknowledges these assumptions (line 157) and notes they "can be relaxed" in the appendix. However, it then presents conclusions as though they apply more directly to the practical algorithm than warranted: "Both these quantities are indirectly optimized by TD-JEPA (Th. 1, 3), which is thus a sound approach for zero-shot policy evaluation" (line 190). In practice, none of A1–A3 hold for any deep-network instantiation, the orthonormality is only weakly regularized, and the predictors are nonlinear. The gap between what is proven and what is asserted about the practical algorithm needs to be more carefully delineated.

### Minor

1. **BYOL-γ*, BYOL*, ICVF* are novel adaptations by the authors, not independently validated methods.** The paper is transparent about this (footnote 5, line 251), which is commendable. However, on DMC_RGB, the strongest competitor BYOL-γ* (582.4) is one such adaptation. The paper's claim of "matching or outperforming state-of-the-art baselines" remains supported by comparisons against established methods (FB at 456.2, RLDP at 525.7 on DMC_RGB), so this caveat does not undermine the core contribution, but it should temper the framing.

2. **No analysis of failure cases or systematic limitations.** The paper identifies domains where TD-JEPA is not competitive (e.g., antmaze-ms RGB where TD-JEPA scores 84.4 vs RLDP's 90.6; cube-single proprioception where TD-JEPA scores 34.2 vs BYOL-γ*'s 79.4) but provides no discussion of patterns in these failures. What kinds of tasks or data distributions does TD-JEPA systematically struggle with?

3. **No computational cost comparison.** TD-JEPA trains four networks (φ, ψ, T_φ, T_ψ) plus policy π, which is more expensive than many baselines. Training time, wall-clock time, and parameter counts are not reported. This omission matters for practitioners.

4. **No hyperparameter sensitivity discussion.** Given the multiple components (two encoders, two predictors, policy, regularization λ, target network update rates), a brief sensitivity statement would strengthen the paper.

### Trivial
None.

## Nice-to-Haves

- An empirical validation of the theoretical claims on a small tabular domain (e.g., measure actual successor measure approximation error ‖M^{π_z} − φT_zψ^⊤‖).
- A brief discussion of which theoretical guarantees plausibly extend to the nonlinear case and which are fundamentally tied to the linear/tabular setting.

## Removed Points

- **"Eq. 9 notation mismatch with Algorithm 1 (stop-gradient only on ψ(s'))"** — Removed as factually incorrect. Eq. 9 applies stop-gradient to both ψ(s') AND T_φ(...). The algorithm uses target networks, which is the standard practical instantiation. No inconsistency.

- **"BYOL* baselines are unfair because authors controlled instantiation"** — Removed as overblown. The paper clearly separates established zero-shot methods from adapted representation-learning methods (footnote 5), and the empirical advantages hold against established methods alone.

- **"Gradient matching doesn't guarantee same for nonlinear"** — Merged into Major #2 (theory-practice gap).

- **"Theorem 2 only prevents future collapse, doesn't guarantee useful representations"** — This is technically true of any non-collapse result. The proof is a valid contribution; this limitation is inherent to the class of results.

- **Missing related works, formatting nitpicks, and presentation issues** — Removed per instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Clarify in the main text (not just a footnote) whether BC regularization in OGBench was applied uniformly to all baselines or only to TD-JEPA.
2. Add a brief paragraph discussing systematic failure patterns and limitations.
3. Add a computational cost comparison table (training time, parameter counts).
4. In Section 4, add a cautionary statement explicitly distinguishing which guarantees hold for the practical algorithm and which require the idealized setting.

## Score and Decision

**Calibration anchors** (all papers from /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/):

| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Proto Successor Measure | s9SVlWOcLt | 6.75 | R1 | Stronger theory, much weaker experiments. Rejected due to limited eval. TD-JEPA is more complete. |
| Conservative World Models | X5qi6fnnw7 | 4.75 | R1 | Incremental contribution (CQL+FB). TD-JEPA is more novel with broader evaluation. |
| Distributional Analogue to SR | OMwD6pGYB4 | 5.75 | R1 | Interesting theory but limited practical scope. TD-JEPA has stronger empirical validation. |
| π2vec | o5Bqa4o5Mi | 5.25 | R1 | Narrower scope (policy evaluation only). TD-JEPA is more comprehensive. |
| Bridging Self-Predictive RL | ms0VgzSGF2 | 6.75 | R2 | Unifying theory + some experiments. Comparable quality, different contribution type. |
| Episodic Novelty Through TD | I7DeajDEx7 | 6.75 | R2 | Exploration-focused. TD-JEPA has more comprehensive evaluation. |
| Actor-Critic Representations | tErHYBGlWc | 6.80 | R2 | Representation analysis paper. Comparable quality to TD-JEPA. |
| Foundation Policies Memory | It4KL6XnPq | 3.00 | R1 | Significantly weaker; TD-JEPA far stronger. |
| Unsupervised Cognition | eRAXvtP0gA | 2.50 | R1 | Not comparable; speculative approach. |

**Round 1 bracket**: [6.0, 8.0]. The weak anchors (2.0–3.0) clearly fall below TD-JEPA. The middle anchors (4.75–6.75) span the range of zero-shot RL/representation learning papers. The strong anchors (>7.5) are not closely related.

**Round 2 narrowing**: Papers at 6.75–6.80 (Bridging Self-Predictive RL, Episodic Novelty, Actor-Critic Representations) are the closest comparators in quality and topic. TD-JEPA's empirical evaluation is more comprehensive than any of these (65 tasks, 13 datasets, 7 baselines). Its theoretical analysis, while cleaner than most, has a notable practice gap. The BC regularization ambiguity is a transparency issue that needs addressing.

TD-JEPA sits above the 6.75 anchors: its empirical evaluation is more thorough than Bridging Self-Predictive RL, its contribution is more practical than the Distributional Analogue, and its scope is broader than π2vec. However, the theory-practice gap and BC regularization issue prevent it from reaching the 8.0 range. **Final score: 7.0.**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>