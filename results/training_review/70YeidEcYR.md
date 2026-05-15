Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper introduces MM-R³, a benchmark for evaluating the consistency of Multimodal Large Language Models (MLLMs) across three tasks: Question Rephrasing, Image Restyling, and Context Reasoning. The authors evaluate nine MLLMs and uncover a key finding—accuracy and consistency often diverge, with some accurate models being inconsistent and vice versa. They additionally propose a lightweight adapter module to improve consistency, showing positive results on BLIP-2 and LLaVa 1.5M.

## Strengths

- **First systematic benchmark for MLLM consistency across linguistic and visual perturbations.** MM-R³ explicitly probes consistency under semantically-equivalent but surface-form-different inputs (Section 3), filling a clear gap relative to existing accuracy-only benchmarks. Human validation (92% for rephrases, 86% for stylized images) confirms the data quality is high.

- **Key finding that accuracy and consistency are often divergent in MLLMs.** The analysis across six open-source and three proprietary models shows that higher accuracy does not imply higher consistency (Tables 2–4, Section 4.2). This is a non-trivial, actionable insight that challenges the assumption that improving accuracy alone suffices for reliable deployment.

- **Comprehensive sensitivity analyses.** The paper examines the effects of model size (Table 5), image resolution (Figure 2), and decoding temperature (Figure 3) on consistency, providing deeper insights beyond a single performance table (e.g., "consistency does not always improve with larger model size," "lower resolution hurts consistency more than accuracy").

- **Coverage of proprietary models (GPT-4V, GPT-4o, Gemini) alongside open-source alternatives.** This enriches the comparison and shows that even the best proprietary models exhibit substantial consistency drops under semantic variations, reinforcing the importance of the problem.

## Weaknesses

### Fatal
None. The benchmark and analysis contributions are sound and independently valuable.

### Major

1. **Adapter validation lacks critical baselines.** The adapter is trained on data generated from the same pipeline as the evaluation benchmark (though disjoint in individual samples). The paper provides no comparison to simpler alternatives such as LoRA fine-tuning of the LLM decoder, full fine-tuning of the vision-language connector, or even prompt ensembling at inference time. Without such baselines, we cannot determine whether the consistency gains (Table 6) are attributable to the adapter's specific design (Bi-LSTM + max-pooling + MLP + prefix) or simply to any fine-tuning on the task distribution. This substantially weakens the paper's central technical contribution.

2. **No ablation of adapter components.** The adapter includes a Bi-LSTM, max-pooling, an MLP projection, and learned prefix tokens. No experiments test whether all components are necessary, whether simpler alternatives (mean pooling, direct projection) would suffice, or how the prefix size affects performance. This makes it difficult to understand what drives the improvement.

3. **No out-of-distribution evaluation for the adapter.** The adapter is only tested on data from the same generation pipeline as its training data (same rephrasing source, same style transfer method, same masking types). The claimed "invariance to surface form variability" is only demonstrated within this narrow distribution. Whether the adapter generalizes to unseen rephrasing patterns, different style transfer methods, or natural occlusions remains untested, leaving its practical value unclear.

### Minor

1. **Consistency threshold (0.7) lacks sensitivity analysis.** The threshold is justified by reference to the STS benchmark (Section 3.3), but the three tasks have different semantic granularities from STS paraphrase equivalence. No results are shown for alternative thresholds or different sentence embedding models, even though the consistency metrics drive most conclusions.

2. **Adapter tested on only 2 of 9 evaluated models.** While BLIP-2 and LLaVa 1.5M are reasonable choices, the claim that the adapter "can be added to any existing MLLM" is not supported by evidence from more architectures (e.g., Qwen-VL-Chat, mPLUG-Owl2, proprietary models).

3. **Disconnect between "invariance" framing and actual training objective.** The paper states the adapter is "trained to minimize inconsistency across prompts" (abstract), but the loss is standard cross-entropy on answer tokens (Section 5.2). While training on multiple variants per input does implicitly encourage consistency, the phrasing overstates the directness of the objective and conflates consistency as a training goal with consistency as a measured outcome.

4. **Empty outputs in Context Reasoning** (marked with *, Table 5) are simply ignored rather than analyzed. If empty outputs correlate with lower consistency, excluding them may bias the metrics.

5. **Limited scope of visual variation.** The Image Restyling task uses only 4 styles from a single method (Johnson et al., 2016), and the Context Reasoning task uses synthetic masks rather than natural occlusions. These are reasonable starting points but narrow operationalizations of visual consistency.

### Trivial
None.

## Nice-to-Haves

- Sensitivity analysis for the consistency threshold (0.7) and the choice of sentence embedding model
- t-SNE or PCA visualization of vision-language encoder outputs before/after the adapter to directly show whether semantically equivalent inputs are pulled together in embedding space
- Error analysis on cases where the adapter improves accuracy but not consistency, or vice versa

## Removed Points

These points were flagged by one or more reviewers but are removed from the main review for the reasons stated. Treat them with caution.

- **"The motivating example in Figure 1 does not quantify why the three questions are semantically equivalent"**: The reviewer acknowledged this is "fine for a motivating example." This is not a real weakness; motivating examples are by nature illustrative rather than formal.
- **"The data generation prompt includes the answer, which may introduce bias"**: The paper already addresses this concern with a human evaluation (92% semantic equivalence on 100 samples). The concern is legitimate in principle but the paper provides evidence that the issue is minimal.
- **"No evidence that the adapter learns invariance vs. simply fine-tuning on the same distribution"**: This is retained as a Major weakness (see above) but rephrased to recognize that the train/test splits are disjoint—the issue is lack of baselines, not data leakage.
- **"Sampling results may inflate consistency because some models use temperature 0"**: The paper separately analyzes temperature effects in Section 4.3.5, so the main sampling comparison is acknowledged as conditional. This concern is diminished by the paper's own analysis but not fully eliminated.

## Novel Insights

The most interesting finding that emerges from this paper—and one that goes beyond simply stating the problem—is that consistency and accuracy are not merely different metrics but can move in opposite directions as model size scales. Table 5 shows that for the Context Reasoning task, larger BLIP-2 and LLaVa models actually regress on consistency metrics (Con and S_C) while improving on accuracy. This suggests a potential trade-off baked into current MLLM training paradigms: scaling up may optimize for answer correctness at the expense of stability under semantically-equivalent input variations. If this pattern holds more broadly, it implies that consistency is not a downstream property that automatically improves with model capability, but rather a distinct design dimension requiring explicit attention in architecture and training.

## Suggestions

1. **Add a LoRA fine-tuning baseline.** Train a LoRA adapter on the LLM decoder using the same training data and compare its consistency improvements to the proposed adapter. This is the single most important experiment to establish whether the adapter's specific architecture matters.

2. **Perform component ablations.** Test variants without Bi-LSTM, with mean pooling instead of max-pooling, and with different prefix sizes. This would identify which design choices drive the consistency gains.

3. **Test on at least one more MLLM architecture** (e.g., Qwen-VL-Chat or mPLUG-Owl2) to support the generality claim.

4. **Add threshold sensitivity analysis** for the consistency metric (e.g., plot Con across thresholds 0.5–0.9).

5. **Clarify the training objective.** Rephrase the claim to "trained on data with multiple surface-form variants of the same semantic content" rather than "trained to minimize inconsistency," which implies a direct consistency loss.

## Score and Decision

The paper makes a genuine contribution with the MM-R³ benchmark and the finding that accuracy and consistency often diverge in MLLMs. These alone are publishable contributions. However, the adapter-based mitigation strategy is insufficiently validated (missing baselines, no ablations, narrow model coverage), which weakens but does not invalidate the overall paper. The benchmark and analysis sections meet the bar for acceptance; the adapter needs substantial strengthening before it can be considered a validated method.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>