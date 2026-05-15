Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper investigates whether FP8 training for LLMs is stable and cost-effective compared to mixed-precision BF16. It finds that (a) even BF16 has non-trivial seed-dependent instability (~10% divergence), (b) MS-AMP FP8 training fails to match BF16 loss curves at equal steps, (c) reducing mantissa bits progressively degrades stability, and (d) a proposed loss-landscape sharpness metric on final-token logits correlates with impending divergence. The core empirical contribution is the systematic study of how representational precision affects training stability.

## Strengths

- **Demonstrates that even BF16 mixed-precision training has non-trivial instability.** The paper shows that with identical configurations, 18/188 BF16 runs (~10%) diverged within the first 5% of training while 0/70 TF32 runs diverged (Figure 1). This is a novel and cautionary empirical finding that challenges the assumption of BF16 stability and motivates the paper's inquiry.

- **The exponent vs. mantissa ablation (E7M7 failure traced to outer exponent clamping) provides clean mechanistic insight.** By isolating inner vs. outer exponent range clamping, the paper shows that the inability to represent large values — not reduced resolution — causes failure when exponent bits are removed. This is a clear, reproducible result that stands independently.

- **Introduces a loss landscape sharpness metric adapted for autoregressive models that correlates with instability.** The metric operates on the last-token logit, avoiding repeated forward passes, and shows increasing values before divergence is visible in the loss curve (Figures 7, 8, Table 1). This is a methodologically sensible adaptation of Keskar et al. (2017).

- **The systematic bit-masking methodology isolates the role of mantissa reduction in a controlled fashion.** By simulating intermediate-bit representations (E8M3, E8M4, E8M5) via clamping, the paper provides a principled ablation that supplements the real FP8 experiments.

## Weaknesses

### Fatal

None.

### Major

1. **The sharpness metric's "predictive" claim is not supported by the evidence.** The abstract states the metric "can predict when training divergence will occur" and the contribution list says it can "predict loss divergences even when the loss curve itself has not yet diverged." However, the experiments only show correlation in single runs: sharpness increases before divergence in Figure 7 (one run per precision) and Table 1 (one run per condition). There is no threshold analysis, no precision/recall evaluation, no out-of-sample testing, no comparison against simpler baselines (e.g., loss variance or gradient norm tracking), and no assessment of how far in advance the metric becomes informative. The body text is more measured ("We believe that, in the future, such analysis... can be used to identify when the model is at risk"), creating a discrepancy between the paper's headline claims and what the evidence supports. *This gap can be addressed by reframing claims and adding baseline comparisons, but the current wording oversells.*

2. **Most reduced-precision experiments are single runs, despite the paper's own demonstration that seed variation causes ~10% divergence in BF16.** The MS-AMP experiments (Figure 6), bit-reduction experiments (Figures 7, 8), and sharpness values (Table 1) lack error bars, confidence intervals, or multiple seeds. Given the paper's central finding that LLM training stability is stochastic, single-run results cannot distinguish systematic precision effects from random variation. The learning-rate robustness experiment (Figure 9, 18 seeds) is the sole exception. This is not a minor omission — it undermines the reliability of nearly all quantitative results in the paper.

3. **The cost-effectiveness conclusion is asserted without direct measurement.** The paper argues that FP8 is not cost-effective because it narrows the stable hyperparameter space, requiring additional tuning and restarts. However, the paper never measures wall-clock time per step for FP8 vs. BF16, never determines whether longer FP8 training (which could be faster per step) would close the gap, and never quantifies the actual additional cost of tuning or restarts. The "$100K per restart" anecdote is illustrative but not applied to any experiment. The core claim about cost-effectiveness requires a framework that the paper does not operationalize. The paper's evidence convincingly shows *reduced stability*, but the leap from "less stable" to "not cost-effective" is argued rather than demonstrated.

4. **Only one real FP8 method is tested, on one architecture.** The paper evaluates MS-AMP at optimization level O1 on GPT-2 (nanoGPT), not on Llama (the paper's primary architecture). The Llama experiments use simulated bit masking, not actual FP8 hardware. The paper's conclusion generalizes to "currently available methods for FP8 training" but does not test NVIDIA's Transformer Engine or other FP8 frameworks. This weakens the generality of the headline claims.

### Minor

1. **The MS-AMP experiments use GPT-2, while the main bit-reduction experiments use Llama.** This architectural inconsistency makes it difficult to directly compare the real FP8 and simulated precision results. The paper could strengthen its case by running MS-AMP on the TinyLlama codebase as well.

2. **The sharpness metric's design choices are not ablated.** The metric uses only the last token's logit — the justification is reasonable (the last token attends to all others) but no ablation explores sensitivity to token position, sequence length, or vocabulary size.

3. **"Loss spikes" are not quantitatively defined in Section 4.4.** The LR robustness experiment (Figure 9) reports "more frequent loss spikes" without a threshold or statistical test. This weakens an otherwise well-designed multi-seed experiment.

4. **The cost anecdote (lines 85–90) and the broader cost-effectiveness framing are rhetorically potent but not operationalized.** The paper never returns to this cost model to analyze any experiment, making it feel disconnected from the empirical work.

### Trivial

- Figure 12 (data quality experiments) is referenced but its content is not visible in the extraction.

## Nice-to-Haves

- A throughput measurement (steps/second) for FP8 vs. BF16 on the same hardware would transform the cost-effectiveness argument from a logical inference into a testable claim.
- The sharpness metric could be compared against simpler alternatives (e.g., logit variance, gradient norm tracking) to demonstrate its added value.
- An ablation of the ε hyperparameter for the sharpness metric would strengthen confidence in the results.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Section 3.2 (Masking) is insufficiently specified"** — Removed because the section content is almost certainly a parser-induced artifact (the heading exists but the body was stripped during PDF extraction, similar to how all other non-text content was removed). The original submission would contain the full methodology description.

2. **"Only GPT-2 is used, not a modern architecture" (the initial BF16 motivation experiment)** — This criticism misunderstands the purpose: the 10% divergence finding on nanoGPT is presented as a *motivating observation*, not a general claim about all architectures. The paper explicitly transitions to Llama for its main experiments.

3. **"The discussion section suggests untested mitigations (speculation rather than analysis)"** — Not a weakness per se; the paper clearly identifies these as future work ("we leave their investigation to future work"), which is standard practice for a paper that identifies a problem.

4. **"The paper never establishes what performance degradation is acceptable"** — This is scope creep. The paper's argument is that FP8 training is not a drop-in replacement for BF16, not that it must match BF16 exactly. The claim is about robustness and hyperparameter sensitivity, not about specifying acceptable degradation thresholds.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that meaningfully reframes or extends the paper's findings.

## Suggestions

1. **Reframe the central claims to match the evidence.** The sharpness metric should be described as "correlated with instability" or "a diagnostic signal," not as a predictor until proper predictive validation is conducted. The cost-effectiveness claim should either be backed with throughput data or softened to "reduced stability and robustness" — which the paper does have evidence for.

2. **Replicate key experiments with multiple seeds.** Given the paper's own finding of seed-dependent divergence in BF16, the MS-AMP and bit-reduction experiments should be repeated with at least 5–10 seeds per condition. For 7B models where this is expensive, the paper should at minimum run multiple seeds for the 120M-scale experiments where this is feasible.

3. **Add one additional FP8 framework** (e.g., Transformer Engine) on the same architecture used for the bit-masking experiments (TinyLlama/Llama) to assess whether the observed instability is specific to MS-AMP or general.

4. **Define "loss spike" quantitatively** (e.g., a threshold-based criterion) in the LR robustness experiment, or provide the trace of individual seeds so readers can assess the claim.

5. **Modify the abstract to match the paper's actual findings.** The abstract claims the metric "can predict when training divergence will occur" — this should be softened to something like "indicates increasing instability before divergence is visible in the loss curve."

## Score and Decision

**Originality:** Moderate — the paper adapts an existing sharpness metric and applies systematic bit ablation, which is novel in this specific framing. The BF16 instability finding is genuinely surprising.

**Importance of research question:** High — whether FP8 is practical for LLM training is a timely and economically significant question.

**Claims vs. evidence:** The claim that FP8 narrows the stable hyperparameter space is supported. The claim that the sharpness metric *predicts* divergence is oversold (correlation ≠ prediction with current evidence). The cost-effectiveness claim is asserted without direct measurement.

**Soundness of experiments:** Moderate — the exponent vs. mantissa ablation is clean. However, the single-run design for most experiments is a significant methodological gap given the paper's own demonstration of stochastic instability.

**Clarity of writing:** Good — the paper is well-structured and the motivation is clear.

**Value to community:** The BF16 instability finding and the systematic bit-reduction study are useful empirical results. The sharpness metric is a promising diagnostic tool even if not yet validated as a predictor.

**Overall:** The paper has genuine contributions — the BF16 instability finding, the E7M7 mechanism analysis, and the systematic study of mantissa-bit effects are valuable. However, the headline claims about prediction and cost-effectiveness are significantly over-extended relative to the evidence, and the single-run design limits the reliability of most quantitative results. The paper would need substantial additional work (multi-seed replication, throughput measurement, proper predictive evaluation of the metric) to support its strongest claims. In its current form, the submission reads as preliminary evidence that motivates further study rather than a complete empirical study.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>