- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 5, 3
Now I have a complete picture. Let me construct the final review.

---

## Summary

This paper addresses the tension between LLM safety and general capability. It proposes three interventions: (1) a fine-grained data categorization scheme (Explicit/Implicit/Mixed Harmful Data) with empirically-derived minimal data ratios, (2) an adaptive message-wise RL alignment method using token-level gradient masking, and (3) an inference-time harmful token filter. The core thesis is that finer-grained signals at the data, training, and inference levels can achieve better safety with less data than standard approaches.

## Strengths

1. **Empirically-grounded observation about diminishing returns of safety data.** The paper identifies that IHD (implicit harmful data) safety scores plateau quickly with additional data, while EHD (explicit harmful data) improves only gradually. The authors derive concrete minimal data ratios (IHD 1:100–1:50, EHD 1:30–1:20, MHD 1:200–1:100 relative to general data) and claim ~13K safety samples suffice vs. ~50K for naïve approaches. This practical contribution could directly reduce the cost of safety alignment.

2. **Novel token-level masking framework that improves on sample-level baselines.** The paper proposes a masking function M(x,y) that selectively highlights tokens in both chosen and rejected responses based on per-token reward relative to a batch-adaptive baseline. The experiments (Section 4.2) compare ADPO/APPO/ARJ against DPO, PPO, KTO, and reject sampling using the same data mixture, providing direct evidence that the masking strategy adds value beyond the base algorithm.

3. **Inference-time token filter with concrete online A/B test results.** Section 4.3 reports specific numerical results from an online A/B test: safety score improving from 0.9020 to 0.9670 (to 0.9855 after a month of iteration) while precision barely changed (0.5185 → 0.5180). These numbers suggest the filter mainly blocks harmful tokens without degrading general output quality.

4. **Useful conceptual distinction between safety alignment and safety knowledge.** The paper clearly delineates two root causes of unsafe outputs — inadequate value alignment vs. insufficient factual safety knowledge — and argues these require different remedies (alignment vs. filtering), which is a clean framing that could guide future work.

## Weaknesses

### Fatal
None.

### Major
1. **Adaptive message-wise alignment method is incompletely specified in the main text.** The paper provides the masking function M(x,y) that determines which tokens to highlight (Equation 2), but does not specify how this mask integrates with the loss function of any base RL algorithm (DPO, PPO, etc.). The sentence "We propose an adaptive message-wise RLHF, which can be formulated as follows:" is followed by no visible formulation in the parsed text. The three tested variants (ADPO, APPO, ARJ) suggest the method modifies DPO, PPO, and potentially reject sampling, but the exact mechanism — whether the mask zeros out log-probability gradients, masks the reward signal, or modifies a preference loss — is never stated in the main text. The paper defers to the appendix ("More detailed descriptions will be included in the supplementary materials"), but for a claimed main contribution, the algorithmic core should be understandable from the main paper alone at a level sufficient for an informed reviewer to assess its novelty and soundness.

2. **Incomplete ablations prevent attributing gains to individual contributions.** The paper presents three distinct interventions but does not cleanly isolate each. Specifically:
   - Section 4.2 holds the fine-grained data mixture constant and compares ADPO vs. standard methods — this is a valid ablation of the masking strategy.
   - However, there is no experiment that isolates the data selection strategy (contribution 1) by comparing, e.g., standard DPO with the proposed fine-grained data mixture vs. standard DPO with a random safety data subset of the same size. Section 4.1 studies data proportions but uses unspecified alignment training, making it unclear whether the benefits of minimal data come from the data composition or from the adaptive alignment method.
   - The token filter (contribution 3) is evaluated only as an add-on to the best model, with no control condition showing the same model without the filter under identical evaluation conditions.

   Without these ablations, the reader cannot assess what each component contributes individually.

3. **No variance or statistical significance reported for any experimental result.** No standard deviations, confidence intervals, or significance tests are provided anywhere in the paper. The online A/B test (Section 4.3) reports point estimates without sample size, test duration, or statistical significance. This makes it impossible to assess whether observed improvements are reliable.

### Minor

1. **Data categorization (EHD/IHD/MHD) lacks validation in the main text.** The three categories are intuitively defined and the experiments show they exhibit different learning dynamics, which is encouraging. However, no inter-annotator agreement, no concrete examples in the main body, and no human validation of the labeling quality are provided. The paper says "specific examples will be included in the supplementary materials," but the main text would benefit from at least one concrete example per category given the categorization is central to the data strategy.

2. **Token filtering mechanism is described at a high level.** Section 4.3 states that a 1B reward model (output layer → classification layer) assigns per-token risk scores based on "nearby preceding contextual information" and "excludes" harmful tokens during sampling, but does not specify the architecture for deriving per-token scores from a sequence-level reward model, the exact filtering operation (masking logits, resampling, or token replacement), or the thresholding strategy. The 3M-dataset reward model training is mentioned but not detailed.

3. **Limited model and dataset scope.** Experiments are conducted only on Qwen2-7B with one safety data pool. While the findings about data proportions are internally consistent, generalizability to other model families and data distributions is unstated.

### Trivial
None.

## Nice-to-Haves
- An explicit loss function (or modified loss) for ADPO/APPO/ARJ would make the method self-contained and reproducible without needing the appendix.
- An ablation comparing standard DPO + fine-grained data vs. standard DPO + random data vs. ADPO + fine-grained data would cleanly separate data selection from algorithm improvements.
- Reporting sample sizes and confidence intervals for the online A/B test would strengthen the token filtering results.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"No numerical evidence for the main experimental claims"** (Harsh Critic). REMOVED. Table 1 and Figures 2–5 are embedded images in the original submission that the parser could not extract. The text DOES report some numerical results (safety scores 0.9020→0.9670, 0.9430→0.9705, precision 0.5185→0.5180, data ratios, model scale comparison at 72B). The claim that results are "virtually absent" is based on a parser artifact, not a genuine paper deficiency.

- **"Incomplete specification — not a parser artifact"** (Harsh Critic). PARTIALLY REMOVED as a fatal claim. The missing equation after "formulated as follows" is very likely a parser artifact (equation not extracted from image/special formatting). However, the broader concern that the method's integration with the base RL algorithm is unspecified in the main text is retained as a Major weakness (#1 above), because even with the equation present, the surrounding text does not explain how the mask enters the loss.

- **"Missing related works"** (Harsh Critic). REMOVED. I cannot confirm that any specific related work is missing without external sources, and the rule prohibits mentioning missing related works.

- **"Reproducibility concerns about code/data release and hyperparameters"** (Harsh Critic "Missing Parts"). REMOVED per instructions: these are nitpicks about reproducibility (undisclosed hyperparameters, large artifacts impractical for a submission). The paper reports temperature, top_P, top_K, batch-average baseline computation, and data composition; other details are plausibly in the supplementary materials (stripped by parser).

- **GPT-4 evaluation not validated** (Harsh Critic). REMOVED per instructions about missing appendix content. The paper states evaluation details are in supplementary materials.

- **"Strengthening the Paper on Its Own Terms" items** (Harsh Critic). These are suggestions, not weaknesses. Most are already covered in Nice-to-Haves above.

- **Strength Finder generic strengths about problem importance.** REMOVED. Generic statements about importance do not constitute concrete evidence of contribution quality.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fully specify the loss function for the message-wise alignment.** Provide the exact modified DPO/PPO loss showing how the mask M(x,y) enters gradient computation — e.g., whether it zeros out per-token log-probability gradients, masks the reward, or weights the preference loss term. This is the single most important fix for a resubmission.

2. **Add an ablation that cleanly separates data selection from the alignment algorithm.** Run: (a) standard DPO + random safety subset, (b) standard DPO + fine-grained mixture, (c) ADPO + same mixture. This would show the independent contribution of the data strategy.

3. **Report confidence intervals or standard deviations** for all main results, and provide sample size and significance test for the online A/B test.

4. **Include at least one concrete example per category (EHD/IHD/MHD) in the main text**, with the harm type and the model's response, to ground the categorization.

5. **Describe the token filtering architecture more concretely** — how per-token risk scores are obtained from a model trained on full-sentence preferences, and the exact filtering operation during decoding (logit manipulation? resampling? vocabulary masking?).

---
