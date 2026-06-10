## Summary

This paper introduces SafetyAnalyst, a framework for LLM safety moderation that generates structured "harm-benefit trees" — enumerating stakeholders, actions, harmful/beneficial effects with likelihood, severity, and immediacy — and aggregates these features via a 29-parameter mathematical function to produce a harmfulness score. The authors fine-tune an open-weight LLM (Llama-3.1-8B-Instruct) via symbolic knowledge distillation from five SOTA LLMs to specialize in generating these trees, and optimize aggregation weights on WildJailbreak labels. The system achieves competitive F1 (75.4 weighted average) across six safety benchmarks, and is designed to be interpretable (via the structured tree output) and steerable (via adjustable aggregation parameters).

## Strengths

- **Novel harm-benefit tree framework for safety moderation.** SafetyAnalyst is the first moderation system to ground decisions in a structured causal chain (stakeholders → actions → effects with likelihood/severity/immediacy) rather than a direct black-box classification mapping. This is a genuine conceptual departure from existing systems (OpenAI Moderation, LlamaGuard, WildGuard, ShieldGemma), and the paper provides a concrete implementation showing this approach can achieve competitive accuracy (Table 2). The motivating example ("how to transport drugs through airport security?") effectively illustrates the distinction between action-based and effect-based reasoning.

- **First taxonomy of harmful and beneficial effects for AI safety.** The paper draws on moral philosophy (Bernard Gert, John Rawls) to define a taxonomy of harmful/beneficial effects, extending beyond the action-based risk category taxonomies (AIR 2024) that dominate current work. This is a novel conceptual contribution that could influence future benchmark design.

- **Substantial engineering and data generation effort.** The paper generates 19k harm-benefit trees using five SOTA LLMs, distills this into a fine-tuned open-weight model (HarmReporter), and validates against 9 baselines on 6 public benchmarks. HarmReporter achieves F1=84.7 on WildJailbreak validation, close to GPT-4o's 91.8, using a much smaller fully open model — a practical contribution.

- **Transparently parameterized aggregation with 29 explicit weights.** The aggregation function (Section 2.3) decomposes the safety decision into inspectable parameters for each risk category, likelihood levels, extents, and immediacy. This is architecturally more transparent than end-to-end classifiers and provides a concrete mechanism for value alignment, even if the mechanism's operation is not empirically demonstrated.

## Weaknesses

### Major

- **The headline "outperforms" claim is misleading.** The paper repeatedly states that HarmReporter "outperforms existing LLM safety moderation systems" (abstract, Section 3, conclusion) based on a weighted average F1 of 75.4 vs. WildGuard's 71.7. However, Table 2 shows WildGuard beats HarmReporter on **five of six individual benchmarks**, often by wide margins: SimpleSafetyTests (99.5 vs. 95.2), HarmBench (99.7 vs. 94.4), WildGuardTest vanilla (91.7 vs. 88.3), WildGuardTest adversarial (85.5 vs. 73.7), and AIR-Bench (87.6 vs. 83.0). HarmReporter only wins on SORRY-Bench (69.1 vs. 58.2). The weighted average is dominated by SORRY-Bench's 9,450 prompts (nearly half the total test data). The paper's own more measured phrasing ("competitive performance on all benchmarks") is accurate; the abstract's "outperforms" framing is not. Furthermore, GPT-4 zero-shot (81.6 F1) exceeds both HarmReporter and all dedicated systems, which substantially weakens the claim that specialized architectures are needed for this task.

- **Interpretability and steerability — the paper's central selling points — are not empirically evaluated.** The paper criticizes existing systems for being uninterpretable and unsteerable, and presents SafetyAnalyst as the solution to these gaps. Yet the entire evaluation (Tables 1–2) measures only classification accuracy (F1, AUPRC, AUROC) — the same metrics used by the systems the paper faults. Specifically: (a) **Interpretability**: There is no user study, no human-grounded evaluation, not even a qualitative comparison showing that the harm-benefit tree leads to better understanding or trust than an alternative (e.g., a simple risk-category label). Figure 2 shows a tree example, but the paper does not test whether humans can actually act on this information. (b) **Steerability**: The paper describes how weights *could* be adjusted (Section 2.4, Figure 3), but no experiment demonstrates this. No results show what happens when weights change — e.g., up-weighting "Child Harm" to simulate a child-safety policy and verifying that classification shifts sensibly. The paper claims "steerability can be achieved" as a property of the architecture, but for a top venue a claimed advantage should be demonstrated, not just asserted. The human evaluation data referenced (Table human_eval_table, likely in appendix) validates feature quality (agreement on generated features), not interpretability or steerability. These are the paper's headline contributions and they are unvalidated.

- **No uncertainty quantification.** Every score in Tables 1 and 2 is a point estimate with no confidence intervals, standard errors, or bootstrap estimates. Given that benchmarks vary in size from 100 prompts (SimpleSafetyTests) to 9,450 (SORRY-Bench), and that HarmReporter involves LLM sampling, the 3.7-point average F1 gap between HarmReporter (75.4) and WildGuard (71.7) could easily fall within noise. This omission undermines confidence in the claimed performance advantage.

### Minor

- **Incomplete baseline comparison on the weighted average.** As noted in the paper (line 135), LlamaGuard, Aegis-Guard-Defensive, and Aegis-Guard-Permissive could not be evaluated on SORRY-Bench (due to context window limits), so their averages are computed over fewer benchmarks. This means the weighted average comparison to HarmReporter — which includes all 6 benchmarks — is not entirely apples-to-apples for those baselines.

- **The benefit component is effectively non-functional.** The optimized weights (Figure 3) assign beneficial effects only 13.4% relative importance vs. harmful effects, and benefits are pre-multiplied by -1 (treated as negative harms, line 91). The paper speculates this reflects WildJailbreak's annotation bias, but it could equally reflect that the benefit features are noisy or the benefit taxonomy is poorly structured. Without analysis, this interpretation is ungrounded, and the benefit component contributes negligibly to decisions.

- **WildGuard comparison is not truly zero-shot.** The paper claims HarmReporter's evaluation is zero-shot because it was not trained on the benchmark datasets. However, HarmReporter's feature generator was fine-tuned on WildJailbreak prompts, and its aggregation weights were optimized on WildJailbreak labels. WildJailbreak and WildGuardTest originate from the same WildTeaming pipeline, giving HarmReporter indirect distributional exposure. This does not invalidate the comparison, but the "zero-shot" framing is overstated.

- **Model naming inconsistency.** The paper correctly refers to "Llama-3.1-8B-Instruct" in the Figure 1 caption and line 34, but line 77 incorrectly says "Llama-3.1-7B-Instruct." Llama 3.1 has an 8B variant. This is a typo that should be corrected.

### Trivial

- None beyond those listed above.

## Nice-to-Haves

- A runtime/efficiency comparison (even rough inference cost per prompt) would be valuable, since the paper acknowledges slower inference as a limitation but provides no data. This would help practitioners assess the interpretability-efficiency trade-off.
- A steerability demonstration: pick two value profiles (e.g., a child-safety policy, a scientific-research policy), adjust weights accordingly, and show that classification behavior changes sensibly on a small set of test prompts. This would directly substantiate a core claim.
- Reporting bootstrap confidence intervals on all F1 scores would substantially strengthen the reliability of the results with minimal effort.

## Removed Points

These points from the inputs were removed with justification:

- **Critic's point about weight optimization on the same dataset as feature generation (information leak):** REMOVED. The paper explicitly states (line 111) that the evaluation was on "balanced vanilla harmful and benign prompts in WildJailbreak held-out from fitting the aggregation algorithm." The critic misread this section.
- **Strength Finder's strength #6 (human annotation validation):** REMOVED. The paper mentions human annotation data from 126 Prolific workers and references "Table human_eval_table," but this table is absent from the main text (likely in the appendix, which was stripped by the parser). The strength cannot be verified from the available content and the Strength Finder's characterization exceeds what is presented.
- **Critic's point about ShieldGemma-2B's perfect 100 F1 on HarmBench:** REMOVED because this is an observation about benchmark properties rather than a weakness of the paper's method. It does not affect SafetyAnalyst's evaluation.
- **Critic's point about two specialist models being "hardware-contingent rather than architecturally motivated":** REMOVED. The paper provides a clear hardware constraint justification (context window of 18,000 tokens, line 77). Criticizing a pragmatic engineering decision is not a substantive weakness.
- **Strength Finder's strength #3 framing as "zero-shot SOTA performance":** WEAKENED to the Minor weakness above rather than kept as a strength at full strength. The "outperforming" claim is misleading, not a strength.
- **Strength Finder's strength #6 about human evaluation:** MOVED to Removed Points as described above.

## Novel Insights

The interplay between the two main weaknesses creates an interesting tension: the paper's novel framework (harm-benefit trees) is architecturally designed for interpretability and steerability, but its evaluation falls back on black-box accuracy metrics — precisely the paradigm it criticizes. This exposes a broader pattern in safety research where systems are motivated by desiderata (interpretability, steerability, fairness) that go unevaluated because the community lacks standardized evaluation protocols for them. The paper would benefit from acknowledging this evaluation gap more explicitly rather than presenting interpretability and steerability as validated properties of the system.

## Suggestions

1. **Recalibrate the claims.** Replace "outperforms" with "competitive performance" or state the result more precisely: "HarmReporter achieves the highest weighted-average F1, driven particularly by performance on SORRY-Bench, while being competitive on all other benchmarks." This matches what the evidence actually shows.

2. **Add a steerability experiment.** Even a simple demonstration — e.g., optimizing weights on two different label distributions to simulate different community values, then showing that classification behavior shifts predictably — would substantially strengthen the paper. This requires no additional data collection.

3. **Add uncertainty quantification.** Bootstrap confidence intervals for all F1 scores in Tables 1 and 2 are quick to compute and would directly address a significant methodological concern.

4. **Include a summary of human evaluation data in the main text.** If the human agreement data (Table human_eval_table from the appendix) shows strong agreement, a brief summary would directly support the claim that the generated features are meaningful and interpretable to human annotators.

5. **Consider whether interpretability needs a user study or can be claimed as a structural property.** If the paper intends to claim interpretability as an architectural property (the output is structured and inspectable by design), this should be stated explicitly and the limitations of this type of claim should be acknowledged. Currently the paper implies but does not commit to a specific standard of interpretability.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>