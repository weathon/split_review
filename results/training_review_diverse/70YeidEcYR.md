Now I have a thorough understanding of the paper. Let me compile the final consolidated review.

---

## Summary

This paper introduces MM-R³, a benchmark for evaluating semantic consistency of MLLMs across three tasks (Question Rephrasing, Image Restyling, Context Reasoning). The benchmark systematically perturbs either the linguistic or visual surface form while preserving semantic content, then measures both accuracy and consistency of model responses. The paper evaluates nine SoTA MLLMs and finds that accuracy and consistency often diverge — high-accuracy models can be inconsistent and vice versa. A lightweight adapter module is proposed to improve consistency.

## Strengths

1. **Novel and well-motivated evaluation dimension.** The paper is the first to systematically benchmark MLLM consistency across both lingual and visual perturbations. The motivation — that consistency is a prerequisite for reliability distinct from accuracy — is clearly articulated and convincingly established. Unlike prior benchmarks focused solely on accuracy (MM-Bench, SEED-Bench, MM-Vet, MME), MM-R³ fills a genuine gap.

2. **Clear empirical evidence that accuracy and consistency are not aligned.** The paper demonstrates this divergence concretely across all three tasks. For instance, GPT-4V achieves the highest accuracy on Question Rephrasing but Qwen-VL-Chat outperforms it on consistency metrics (Table 2). On Context Reasoning, BLIP-2 and LLaVa 1.5M have lower accuracy but higher consistency than several other models (Table 4). This finding is the paper's central empirical contribution and is well-supported.

3. **Comprehensive evaluation across nine SoTA MLLMs and three diverse tasks.** The evaluation spans both open-source (BLIP-2, mPLUG-Owl2, LLaVa 1.5M, MoE-LLaVa, Qwen-VL-Chat, BLIP-3) and proprietary (Gemini, GPT-4V, GPT-4o) models on 3,516 rephrased questions, 5,328 styled images, and 4,500 masked images. The scale and breadth support the generalizability of the findings.

4. **Human validation of semantic equivalence for generated data.** The paper reports forced-choice human evaluations finding 92% of rephrased questions and 86% of restyled images are semantically equivalent for humans (Section 3.2). This validates that measured inconsistencies stem from model behavior rather than data artifacts.

5. **Informative auxiliary analyses.** The resolution analysis (Figure 2), model size analysis (Table 5), and temperature analysis (Figure 3) provide actionable insights — e.g., consistency does not always scale with model size or resolution, and mPLUG-Owl2/MoE-LLaVa degrade more sharply with temperature than Qwen-VL-Chat. These go beyond simple leaderboard reporting and demonstrate the benchmark's utility for diagnosing model behavior.

## Weaknesses

### Fatal
None.

### Major

1. **Adapter evaluation conflates the adapter's effect with the effect of training on task-specific data.** The paper compares the base off-the-shelf model (no training) against the same model with an adapter trained on the benchmark's task data (Section 5.2). Since the base model is *not* fine-tuned on the same data without the adapter, the observed gains cannot be attributed to the adapter's architecture (Bi-LSTM + pooling + prefix tokens) — they could simply reflect the benefit of any parameter-efficient fine-tuning on the task distribution. A proper control (full fine-tuning of the frozen layers on the same data, or a simpler linear projection baseline) is needed to isolate the adapter's design as the cause of improvement. This does not affect the benchmark contribution, but it undermines the method as a claimed contribution.

2. **Abstract claims numbers that do not match reported results.** The abstract states "absolute improvements of 5.7% and 12.5%, on average on widely used MLLMs such as BLIP-2 and LLaVa 1.5M in terms of consistency." Inspection of the paper text reveals that for Question Rephrasing, the Con improvements are +13.6 (BLIP-2) and +10.8 (LLaVa 1.5M). The numbers 5.7 and 12.5 appear nowhere in the experimental section, and no averaging scheme or metric is specified that would yield these values. This discrepancy must be resolved — it erodes trust in the reported figures.

### Minor

3. **Temperature settings for all models in the main evaluation are not fully reported.** BLIP-2 and LLaVa 1.5M are explicitly noted as being at temperature 0 (Section 4.3.1). However, for models like mPLUG-Owl2, MoE-LLaVa, Qwen-VL-Chat, and BLIP-3, the temperature used in Tables 2–4 is not stated. Given that Section 4.3.5 shows temperature strongly affects consistency (e.g., mPLUG-Owl2's consistency drops significantly as temperature increases), the failure to standardize or report inference settings across all models makes cross-model comparisons of consistency potentially unfair. The authors should report the temperature for all models and ideally standardize it.

4. **No human validation for the Context Reasoning (masking) task.** Human validation was conducted for rephrasing (92%) and restyling (86%) but not for whether humans would consistently infer the same object across different mask types (lines, shapes, colors). The paper assumes this is true (Section 3.2), but since the masking task produces the largest consistency divergence among models, verifying this assumption with a forced-choice experiment would strengthen the benchmark's validity.

5. **Adapter tested on only two model families.** The paper claims the adapter can be added to "any MLLM" but only evaluates on BLIP-2 and LLaVa 1.5M. While these represent two different architectures (Q-Former vs. CLIP projection), testing on at least one more model (e.g., Qwen-VL-Chat or mPLUG-Owl2) would make the generality claim more credible. This is particularly important given that the adapter training uses the same data generation pipeline as the benchmark, raising questions about generalization beyond the training distribution.

6. **No limitations discussion.** The paper does not discuss limitations. Important caveats include: reliance on GPT-3.5 for rephrasing (potential bias), use of a single style transfer method, single sentence embedding model for all semantic similarity metrics, and the restricted set of perturbations (four styles, three mask types). A limitations section would strengthen the paper's scientific posture.

### Trivial

7. The Sampling analysis (querying the model 4 times with identical input) is introduced as a control for inherent stochasticity but is not used in the adapter evaluation or in most of the subsequent analysis, which is a missed opportunity for consistency.

## Nice-to-Haves

- The 0.7 threshold used for the Con metric is based on STS-B and may not generalize perfectly to multimodal open-ended responses. A brief sensitivity analysis (e.g., showing results for 0.6 and 0.8) would strengthen the metric's justification.
- The paper notes that the P-Adapter (Newman et al., 2022) is the inspiration for the adapter but does not clearly explain how the multimodal version differs or improves upon the prior work.
- An analysis of consistency on correct vs. incorrect answers (mentioned as in the appendix) would be informative if included in the main paper.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Missing appendix content (Appx A.5)"** — The parser strips appendix sections from all papers; they exist in the original submission.
- **"The adapter does not report number of epochs, convergence behavior, or variance across runs"** — These are implementation-level details and the instruction directs removing such reproducibility nitpicks.
- **"No comparison to simpler linear adaptation"** — This is subsumed under the broader baseline concern in Major weakness #1 and is not a separate issue.
- **"Training data uses same pipeline as benchmark, raising generalization questions"** — This is a valid concern but is covered by Minor weakness #5 (limited model testing). The training/evaluation data are explicitly stated to be disjoint, which is good practice.
- **Strength from Strength Finder about the adapter: "Proposed adapter yields significant consistency improvements on two model families"** — This strength partially conflicts with the verified weakness (Major #1) about inadequate baselines. The improvements are numerically real but cannot be cleanly attributed to the adapter design. Moved here for caution.

## Novel Insights

The most novel insight emerging from the reviews is that the paper's strongest finding — the accuracy-consistency divergence — is robust and well-supported, while the adapter contribution is the weakest part. This suggests the paper would be stronger if it reframed the adapter as a preliminary investigation rather than a core contribution, and doubled down on the analysis (e.g., probing *why* Qwen-VL-Chat is more consistent — is it the Qwen LLM backbone? the training data? the vision-language connector?). The resolution, model size, and temperature analyses already hint at productive directions for understanding MLLM consistency, and these could be expanded.

## Suggestions

1. **Fix the abstract numbers.** Clarify what metric and averaging scheme yields 5.7% and 12.5%, or correct the abstract to match Table 6.
2. **For the adapter, either add proper baselines** (full fine-tuning on the same data, a simpler linear adapter) to isolate the design's contribution, or **scale back the claims** to a preliminary finding with clearly stated limitations.
3. **Report temperature settings for all models in the main evaluation** (Tables 2–4) and ideally standardize them to temperature 0 for fair comparison.
4. **Add human validation for the context reasoning task** (or explicitly acknowledge its absence as a limitation).
5. **Add a limitations section** discussing the scope of perturbations, reliance on specific models for data generation, and generalizability constraints.

## Score and Decision

The benchmark (MM-R³) and the empirical finding that accuracy and consistency diverge across SoTA MLLMs constitute a solid, timely contribution. The analysis is well-conducted, the data is human-validated (for two of three tasks), and the auxiliary analyses (resolution, model size, temperature) add useful depth. The adapter contribution is the paper's weakest part, but it is not the paper's primary contribution. The main issues (abstract number discrepancy, adapter evaluation) are fixable in revision and do not undermine the core benchmark contribution.

I recommend acceptance conditional on the authors resolving the abstract number discrepancy and either strengthening the adapter evaluation or appropriately scaling back its claims.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>