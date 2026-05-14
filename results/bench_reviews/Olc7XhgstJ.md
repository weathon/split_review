Now I have a thorough understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper proposes Steady Thought (ST), a thought-level preference optimization framework for mitigating "under-thinking" in Large Reasoning Models (LRMs). ST operates in three stages: (1) entropy-based segmentation of reasoning chains into thought units, (2) guided completion of each thought by suppressing switching tokens, and (3) fine-grained preference optimization (STPO) that encourages commitment to promising thoughts. Experiments across three model sizes and four benchmarks show token reductions up to 39.3% with accuracy improvements up to 5.3%.

## Strengths

- **Multi-model, multi-benchmark empirical scope**: Results span three model families (1.5B, 8B, 14B) and four benchmarks including an out-of-distribution code task (LiveCode), consistently showing token reduction with maintained or improved accuracy (Table 1). The OOD generalization on LiveCode—a code benchmark despite math-only training—provides some evidence that the learned pattern transfers domains.

- **Fine-grained switching analysis in Appendix C**: Table 8 quantifies valid (F→T) vs. invalid (T→F) thought switches before and after ST, showing that invalid switches are reduced more aggressively than valid ones across most settings. For the 1.5B model on AIME2024, valid exploration actually increases by 69.4%, providing some mechanistic evidence for the method's selectivity.

- **Preference optimization ablation**: Table 4 compares SFT, DPO, and STPO on the same preference data, demonstrating that the length-normalized, thought-conditioned STPO objective achieves the best accuracy-efficiency trade-off (84.4% on MATH500 with 2809 tokens vs. DPO's 82.6% with 4273 tokens).

## Weaknesses

### Major

- **Hyperparameter tuned on test benchmarks (Section 4.4.3, Table 3)**: The entropy threshold for thought segmentation—which determines which training preference pairs are constructed—was selected by evaluating accuracy and token count on MATH500 and AIME2024, the same test sets used to report final performance. While Table 3 shows some robustness (all three thresholds improve over the base model), the chosen threshold of 3.0 was explicitly picked because "it yielded the best overall performance" on these test benchmarks. This constitutes test-set leakage; the reported gains on MATH500 and AIME2024 cannot be treated as unbiased estimates of generalization. The GSM8K and LiveCode results are not directly affected by this leakage, partially mitigating the concern.

- **Under-thinking evidence not fully disentangled from length reduction**: Section 4.4.2 equates "correct intermediate thoughts" with "invalid switches," which is logically imprecise—a model could switch from one correct thought to another correct thought, inflating the metric. Appendix C partially addresses this by distinguishing T→F from F→T switches in Table 8, but the data there reveals that for Qwen3-8B on MATH500, valid switches also decrease by 53.5%, and the 1.5B model on MATH500 loses 26.4% of valid switches. The claim that ST "preserves and even optimizes exploration" (Appendix C) is supported only for the 1.5B model on AIME2024 (a single data point). For most settings, useful exploration is also suppressed, complicating the paper's central narrative.

### Minor

- **Missing comparison with step-level preference optimization baselines**: The paper compares against holistic DPO and SFT (Table 4) but not against step-level preference methods like Step-DPO (Lai et al., 2024), which the paper cites in Section 5.2. A comparison using "\n\n" step boundaries (without entropy segmentation) paired with the same STPO objective would isolate the contribution of entropy-based thought segmentation.

- **No statistical reporting for small test sets**: AIME2024 (30 problems) and LiveCode (400 problems) are small enough that accuracy improvements of ~3 percentage points could be sensitive to sample variance. The paper reports averaging over multiple runs (8 for AIME, 2 for LiveCode) but omits standard deviations, confidence intervals, or significance tests.

- **No quality analysis of synthetic completions**: The thought-completion stage (Section 3.2) suppresses an extensive list of transition tokens (Table 5) to prevent switching. The paper does not evaluate whether these constrained-decoding completions remain coherent, fluent, or representative of natural reasoning. While this is not a fatal omission, it leaves open the possibility of distributional shift in the training data.

### Trivial

- The problem formulation in Section 2 is largely restating the SimPO framework with renamed notation; the "Steadiness Score" is simply the policy log-probability.

- Section 4.4.1's analysis (shorter responses, larger proportion of last thought) is largely a restatement of length reduction rather than independent evidence of deeper reasoning.

## Nice-to-Haves

- Reporting automatic quality metrics (perplexity, length distribution) or a small human evaluation of completions generated under token suppression, to validate that the synthetic training data is not degraded.

- Tuning the entropy threshold on a held-out validation split of the training data rather than test benchmarks, which would be standard practice.

- A comparison against a baseline that simply applies STPO to standard "\n\n"-delimited step boundaries (without entropy segmentation), which would isolate the value of entropy-based thought detection.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"No comparison to step-level preference optimization baselines"** — this was moved to Minor (not Major) because step-level DPO is a reasonable comparison but not an absolutely required baseline; the paper already compares against holistic DPO and SFT.

- **"Missing variance/statistics"** — moved from potential Major to Minor because single-run or few-run evaluation with small test sets is common in this subfield, and the overall multi-model, multi-benchmark consistency provides some robustness signal.

- **"Thought-completion without analysis of distributional impact"** — moved from Major to Minor because while a quality analysis would strengthen the paper, the method's effectiveness on downstream tasks provides indirect evidence that the completions are functional.

- **Harsh critic's claim about Brad-Terry formalization adding nothing beyond SimPO** — kept as Trivial; the formalization is descriptive framing, not a claimed novel contribution.

- **Harsh critic's claim about baseline comparison being unfair (test-time only vs. training)** — removed. The paper legitimately compares against test-time methods as a different class of approaches, and also includes training-based baselines (SFT, DPO). The asymmetry is not unfairly favoring the authors.

- **Harsh critic's claim about Table 8 showing suppressed exploration universally** — partially incorporated into Major Weakness #2. The table does show NVS reductions for most model/dataset pairs, but this doesn't fully invalidate the method since (a) some NVS may be redundant, (b) accuracy improves, and (c) the 1.5B/AIME case shows increased exploration.

## Novel Insights

The paper's most interesting—though imperfectly validated—insight is that thought-level preference optimization can selectively reduce wasteful thought-switching while preserving productive exploration, at least for weaker models on hard problems (Table 8, 1.5B/AIME2024: +69.4% valid switches). The entropy-based segmentation as a way to identify thought boundaries without manual annotation is a practically useful idea, though the current implementation's reliance on test-set tuning weakens the contribution.

## Suggestions

- **Rerun threshold selection on a held-out validation split.** This is the most important fix: split the omni-math training data into train/validation, tune the entropy threshold on validation accuracy, and report final test results. This would address the most significant methodological concern without requiring new experiments.

- **Report statistical confidence.** For AIME2024 (30 problems) and LiveCode (400), bootstrapped confidence intervals or binomial tests would clarify whether the observed accuracy gains are statistically meaningful.

- **Add the step-boundary baseline.** Comparing STPO with "\n\n" step boundaries (no entropy segmentation) against the full ST method would cleanly isolate the value of entropy-based thought detection.

- **Tone down the exploration-preservation claim.** The current claim in Appendix C that ST "preserves and even optimizes" exploration is supported by a single datapoint. A more accurate characterization would acknowledge that ST reduces both invalid and valid switches in most settings, with accuracy preserved through more efficient use of the remaining switches.

## Score and Decision

### Anchor Comparison

| Anchor Paper | Avg Score | Decision | Comparison |
|---|---|---|---|
| PREMISE (gFSQNmBXx1) | 2.67 | Reject | Weaker: prompt-only, limited baselines, unclear method, no training contribution. ST is substantially stronger with its training-based approach and broader empirical validation. |
| Token Bayesian Optimization (esXvdhwUQ5) | 3.50 | Reject | Weaker: limited baselines, prompt-level optimization only. ST has a richer method and more analysis. |
| LoRR (0SSKmVjj8O) | 4.00 | Reject | Comparable in spirit (plug-in for preference optimization) but LoRR had unclear algorithmic details and limited novelty. ST has stronger empirical results but the test-set leakage issue is more serious. Roughly comparable quality. |
| LCPO (8xSU8Oscvg) | 5.00 | Accept (Poster) | LCPO is the closest comparator: similar domain, similar goals, preference optimization for LRM length reduction. LCPO achieved larger reductions (50%+) with maintained accuracy and had more systematic analysis of the BT loss. ST has the test-set leakage issue that LCPO (apparently) did not, and less thorough benchmark coverage. ST is slightly weaker. |
| Concise Reasoning Lagrangian (msKQYIfgVm) | 5.00 | Reject | Similar quality. CRL had a principled Lagrangian formulation but evaluation concerns. ST has test-set leakage and incomplete evidence for the under-thinking claim. Comparable. |
| OptimalThinkingBench (N5kWa3sRJt) | 5.33 | Accept (Poster) | Stronger: benchmark contribution with comprehensive evaluation of 33 models and novel metrics. Different category (benchmark vs. method). |
| DAG-Math (ylr6WArKQN) | 6.00 | Accept (Poster) | Stronger: novel graph-based evaluation framework for CoT, clean contribution. |
| InternGeometry (1sffPGGQyT) | 7.00 | Accept (Poster) | Much stronger: SOTA IMO geometry results, novel agent design, impressive data efficiency. |

The Steady Thought paper sits between LoRR (4.0) and LCPO (5.0). The test-set leakage is a genuine methodological problem that prevents a score in the strong-accept range, but the paper's multi-model empirical scope, OOD generalization, and detailed switching analysis in the appendix prevent it from falling into the reject range. I calibrate to 4.5.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>