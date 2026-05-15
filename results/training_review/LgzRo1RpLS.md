Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the final consolidated review.

## Summary

MambaExtend identifies that Mamba's failure on long contexts stems from out-of-distribution discretization step (Δ_t) accumulation across layers. The paper proposes calibrating per-layer scaling factors for Δ_t using either backpropagation (CF_BP) or zeroth-order SPSA optimization (CF_ZO), while keeping all pre-trained model weights frozen. This enables context extension from 2k to 64k with orders-of-magnitude fewer parameter updates and lower peak memory than fine-tuning alternatives, achieving competitive or better performance on perplexity, LongBench, and passkey retrieval tasks.

## Strengths

1. **Novel diagnosis of Mamba's long-context failure mechanism.** The paper provides clear empirical evidence (Fig. 2) that accumulated Δ_t magnitudes increase with context length, and shows that scaling Δ_t uniformly can reduce perplexity from ~268 to ~23.5 on Pile at 32k (Fig. 3). This root-cause analysis is genuine, well-motivated, and directly informs the proposed solution.

2. **Extreme efficiency gains over fine-tuning alternatives.** MambaExtend requires up to ~5.42×10⁶× fewer parameter updates and up to 3.87× lower peak memory than DeciMamba (Fig. 6), while matching or exceeding its performance. The comparison in Fig. 6 is well-controlled (all methods trained for one epoch) and cleanly demonstrates the practical advantage of calibrating only L scaling factors.

3. **Zeroth-order optimization matches backpropagation in practice.** Table 4 shows that CF_ZO (forward-pass-only) achieves nearly identical perplexity to CF_BP across context lengths 2k, 4k, and 8k on Pile. This validates the memory-efficient variant and strengthens the practical deployability claim.

4. **Informative ablation on scaling granularity.** Table 3 compares per-channel, per-token, and per-tensor sharing of scaling factors for passkey retrieval, showing that per-channel sharing dramatically outperforms coarser alternatives. This provides actionable guidance for deploying MambaExtend on different task types.

5. **Perplexity results on PG-19 demonstrate reliable long-context extension.** At 70k context, MambaExtend-130M achieves PPL 30.62 versus the pre-trained model's catastrophic PPL of 995,328 (Fig. 4), with consistent improvements over DeciMamba (up to ~40.6% PPL reduction). The trend across context lengths is clear and monotonic.

## Weaknesses

### Fatal
None.

### Major

1. **Missing baselines that isolate whether the optimization framework is necessary.** The paper compares against uniform global scaling (Fig. 3) and full fine-tuning, but never against simple alternatives such as: (a) per-layer scaling factors selected via grid search over a small range, (b) a hand-tuned heuristic such as scaling Δ_t proportionally to the ratio of training-to-evaluation context length. Since only L scalar parameters are learned (for the PPL experiments), a bounded grid search would be entirely feasible. Without such baselines, it is unclear whether the backprop or ZO optimization framework is needed, or whether a cheap non-iterative heuristic achieves comparable results. This gap directly weakens the claim that the calibration framework itself is a contribution.

2. **No cross-dataset or cross-domain generalization analysis.** Calibration is performed on 10–20 samples from the *same* dataset used for evaluation (e.g., calibrate on Pile train, evaluate on Pile test). There is no experiment where scaling factors calibrated on one domain (e.g., Pile) are evaluated on another (e.g., PG-19, books, code), or even intra-dataset generalization across non-overlapping splits. This makes it unclear whether the learned scaling factors overfit to the calibration distribution or are robust across text domains. The paper claims a "general-purpose" context extension method but provides no evidence of generality.

3. **Misleading "training-free" framing throughout the paper.** The title, abstract, introduction, and methodology section repeatedly describe MambaExtend as "training-free" and contrast it with "fine-tuning" approaches. However, both CF_BP (backpropagation-based gradient descent) and CF_ZO (iterative SPSA with forward passes and parameter update rules) are optimization procedures that constitute a form of training/calibration. The paper's own language acknowledges this — it "learns" scaling factors, performs "calibration," and uses "optimization" — yet the "training-free" label is applied as a central branding claim. This mischaracterization inflates the perceived novelty. The paper would be more accurate describing the method as "base-model-weight-free" or "minimal-parameter calibration."

### Minor

1. **The "~8145×" perplexity improvement factor is inflated by a catastrophic baseline.** The pre-trained model yields PPL ~995,328 at 64k (effectively infinite — random guessing). Dividing against a near-infinite denominator produces a large but uninformative ratio. The underlying result (MambaExtend prevents catastrophic PPL blow-up) is real, but presenting the fold-improvement as a headline figure is sensational and obscures the fact that absolute PPL at 64k (~30) is still much higher than at 2k (~3.7).

2. **LongBench gains are modest and inconsistently distributed across tasks.** The paper reports "up to 6.03%" average improvement, but individual task results (Table 2, shown as an image) suggest some tasks see small gains or even degradation. Absolute scores remain below 50% on most tasks. This weakens the claim that MambaExtend delivers practically meaningful long-context understanding improvements beyond perplexity and retrieval.

3. **Reproducibility details are incomplete.** The paper does not specify the number of calibration steps/iterations, learning rate schedule, or convergence criteria for either CF_BP or CF_ZO. While the small parameter count makes exhaustive reporting less critical, these details are necessary for exact reproducibility. The paper also does not report variance (error bars or standard deviations) for any experiment, which is particularly relevant given the small calibration set sizes (10–20 samples).

4. **Motivational case study (Section 3) is limited in scope.** The analysis of Δ_t accumulation (Fig. 2) and the uniform scaling experiment (Fig. 3) are only shown for one model (Mamba 1.4B) on one dataset (Pile). Demonstrating this pattern on a second model scale (e.g., 130M) or a second domain would strengthen the generality of the diagnosis.

5. **No calibration set size ablation.** All experiments use 10–20 calibration samples. Since stochastic optimization with such tiny datasets can be unstable, testing the sensitivity to calibration set size (e.g., 1, 5, 10, 50, 100 samples) would be informative.

### Trivial

None.

## Nice-to-Haves

- A plot of the learned per-layer scaling factors (s_i) across layers for different model sizes, showing whether early layers require less scaling than later layers.
- Convergence curves for CF_BP and CF_ZO showing loss over iterations.
- Qualitative examples from LongBench where MambaExtend improves (and where it fails), to ground the numerical scores.
- Combination with DeciMamba (orthogonal approaches — MambaExtend scales Δ_t, DeciMamba decimates tokens — that could be complementary).

## Removed Points

- **Criticism about Table 2 formatting / missing numbers**: Parser artifact from PDF extraction; the original submission has proper formatting.
- **Criticism about Section 5.3 "garbled text"**: Parser artifact; the original sentence is intact.
- **Criticism about baselines being "potentially handicapped by 1 epoch"**: The paper explicitly controls for this ("for a fair comparison, we fine-tune for the same epochs as ours"), making this speculation rather than a verified flaw.
- **"3500× fewer parameters is expected" complaint**: This is a strength, not a weakness — demonstrating competitive accuracy with vastly fewer parameters is precisely the contribution.
- **"Up to 6.03% suggests cherry-picking"**: "Up to" is standard reporting language; the reviewer provides no evidence of cherry-picking.
- **Missing related work on SSM parameter-efficient methods**: Per meta-reviewer rules, I cannot confirm the existence of such works and must not mention missing related works.
- **Criticism about Section 5.3 misreferencing "40.6% reduced PPL"**: The paper correctly states this as PPL reduction vs. DeciMamba; the claim is consistent across sections.
- **Strength Finder's generic/padding strengths**: Filtered out claims like "this paper addressed an important problem" that lack concrete specificity.

## Novel Insights

Both reviews converge on the same pattern: the paper's core technical contribution — diagnosing that Δ_t accumulation causes Mamba's long-context failure and showing that per-layer scaling factors prevent catastrophic degradation — is genuinely novel and well-supported. The controversy is entirely about evaluation completeness, not about whether the method works. Neither reviewer disputes the perplexity curves, the passkey retrieval results, or the efficiency numbers. The disagreement is about how much weight to place on missing baselines (per-layer grid search) versus the value of the contribution. A notable subtlety is that the "training-free" critique, while valid as a framing concern, may be overstated: "training-free" in the SSM context is reasonably understood as "no re-training of base model parameters," which the paper's method satisfies. The missing generalization analysis is the most actionable gap — it would directly address whether the scaling factors capture domain-invariant properties of Δ_t drift or merely memorize calibration samples.

## Suggestions

1. **Add per-layer grid search baselines.** For the PPL setting (L scalar parameters), perform a bounded grid search over, e.g., s_i ∈ {0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0} independently per layer. If this matches CF_BP/CF_ZO results, the optimization framework is unnecessary but the core insight (per-layer scaling helps) still stands. If grid search performs worse, the optimization contribution is validated.

2. **Add cross-dataset generalization experiments.** Calibrate on Pile and evaluate on PG-19 (and vice versa). Also test intra-dataset generalization (calibrate on 10 samples from one Pile subset, evaluate on a disjoint subset). Report whether scaling factors from one domain transfer.

3. **Tone down the "training-free" branding.** Replace with precise language such as "without updating base model weights" or "lightweight calibration." The method's efficiency and parameter savings speak for themselves.

4. **Report variance across runs.** Re-run calibration with different random seeds (at least 3) and report mean ± std for perplexity and retrieval. This is especially important given the small calibration set sizes.

5. **Report calibration hyperparameters.** Add a table specifying number of CF_BP/CF_ZO iterations, learning rate, SPSA perturbation size, and convergence criteria.

6. **Replace headline "8145×" with a more meaningful metric.** Use absolute PPL values or relative improvement over a non-catastrophic baseline. The factor is technically correct but creates a misleading impression.

## Score and Decision

The paper makes a genuine contribution by identifying Δ_t accumulation as the root cause of Mamba's long-context failure and demonstrating that per-layer scaling of Δ_t — using either backprop or ZO — enables context extension to 64k with extreme parameter efficiency. The core experiments (PPL, passkey retrieval, ablation on granularity) are sound and the efficiency gains are convincingly demonstrated. However, the evaluation has two significant gaps: (1) missing baselines (per-layer grid search, heuristic schedules) that would isolate whether the optimization framework itself contributes value beyond the scaling insight, and (2) no cross-dataset generalization analysis, which weakens the claim of a general-purpose method. The "training-free" framing and the headline "8145×" factor also overstate the contribution. These gaps are addressable but require additional experiments and toned-down claims. The paper is borderline: the core idea is worth publishing, but the current evaluation is incomplete. With the suggested revisions, it could be a strong paper.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>