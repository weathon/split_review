- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have a thorough understanding of the paper and can cross-check all claims. Let me produce the consolidated review.

---

## Summary

This paper studies safety in open-source instruction-tuned LLMs (LLaMA, Falcon). It shows that many popular instruction-tuned models readily comply with harmful requests, and that adding a small fraction (~3%, a few hundred examples) of safety-focused instruction examples to the fine-tuning data substantially reduces harmful outputs. The paper also identifies *exaggerated safety* as a downside of too much safety data, and demonstrates that the *format* of safety training prompts (instructions vs. questions) affects generalization. The core contribution is a practical, low-cost intervention supported by systematic scaling experiments.

---

## Strengths

1. **Systematic scaling study of safety data.** The paper trains models with 100, 200, 500, 1000, 1500, and 2000 safety instructions on top of 20K general instructions (Section 3.2), showing that even 3% safety data (500 examples) substantially reduces harmful responses across multiple test sets. This fine-grained ablation clarifies the minimal effective dose, going beyond prior work that used fixed or much larger amounts of safety data.

2. **Instruction-vs-question format matters for safety generalization.** The paper compares training on safety *questions* (original Red Team format) vs. safety *instructions* (reformatted) vs. mixed data, finding that instruction-trained models generalize better to malicious instructions (Section 4, Figure 6). This is a concrete, actionable insight about data curation that previous work did not systematically contrast.

3. **Exaggerated safety is identified and demonstrated.** Using an early version of XSTest, the paper shows that excessive safety training (2000 examples) causes models to refuse safe prompts that superficially resemble unsafe ones (e.g., "Where can I shoot a photo?"). The manual annotation (Figure 2) and qualitative examples (Figure 4) provide clear evidence of this trade-off.

4. **Release of evaluation datasets and pipeline.** The paper introduces five new safety evaluation datasets (I-MaliciousInstructions, I-CoNa, I-Controversial, I-PhysicalSafety, Q-Harm) plus an XSTest subset, along with an evaluation pipeline using reward models, content moderation APIs, and manual annotation. These resources are a concrete contribution to reproducible safety benchmarking.

---

## Weaknesses

### Fatal
None. No verified weakness invalidates the paper's core claims. The well-supported finding that safety data reduces harm remains intact.

### Major

1. **Missing standard benchmark results for capability preservation.** The paper repeatedly claims that safety-tuning does not degrade general capabilities, and explicitly lists PIQA, BoolQ, and OpenBookQA from the LM Evaluation Harness (Section 3.4, "Response Quality") as evaluation datasets. However, **no results for these benchmarks appear anywhere in the paper**. The only quantitative capability evidence provided is a general-purpose reward model comparison on 50 I-Alpaca instructions (Figure 5) and the manual annotation (Figure 2). For a claim made as prominently as "without deteriorating the models' overall performance and functionality, as verified by standard language benchmarks" (line 37), the absence of these results is a significant evidential gap. The reader cannot verify whether the safety gains come at a hidden capability cost on these benchmarks.

### Minor

1. **Circularity in the primary harmfulness evaluation.** The harmfulness reward model (the paper's main quantitative metric) is trained on the Anthropic Red Team dataset, which is the *same source* from which safety training examples were drawn (lines 94, 128). The paper acknowledges this overlap and argues that test sets come from different distributions — a reasonable mitigation — but the risk remains that the reward model is simply recognizing refusal response patterns it was trained on rather than measuring harmfulness independently. The OpenAI content moderation API and manual annotation provide triangulation, but these play a secondary role. This weakens, though does not invalidate, the quantitative backbone of the safety evaluation.

2. **Exaggerated safety analysis lacks systematic quantification.** The paper identifies exaggerated safety as one of its three main findings, but the analysis relies on 50 XSTest prompts with manual preference annotation and a few qualitative examples. The paper does not report a systematic *refusal rate* (e.g., what fraction of the 50 XSTest prompts received a refusal from each safety-tuned model), nor does it explore where the boundary between appropriate refusal and overrefusal lies. The trend is clear and the examples are illustrative, but the characterization is thinner than the weight this finding carries in the paper's narrative.

3. **Reproducibility: safety response generation prompt not specified.** The paper states that GPT-3.5-turbo was used to generate "safe" responses to Red Team questions (line 94), but does not provide the specific prompt or guidelines used for this generation. Given that the quality and nature of these generated responses directly determine the safety training signal, this omission hinders exact reproduction.

### Trivial
None.

---

## Nice-to-Haves

- The I-PhysicalSafety dataset has a one-to-one mapping between safe and unsafe instructions. The paper does not exploit this paired structure (e.g., computing per-pair refusal differences), which could yield finer-grained insights about when models over-refuse.
- A limitations section would be useful, explicitly noting that safety responses are generated by GPT-3.5 (thus reflect its biases), that the harmfulness RM has a specific training distribution, and that adversarial attacks (jailbreaks, prompt injections) are not tested.
- The paper could qualitatively situate this simple data augmentation approach relative to more complex methods like RLHF or Constitutional AI.

---

## Removed Points

These points were raised but are removed with justification:

- **"The I-PhysicalSafety one-to-one mapping is a missed opportunity"** — This is moved to Nice-to-Haves. It is not a weakness of the paper's current claims, just an unexecuted direction.
- **"No inter-annotator agreement reported for manual review"** — The paper describes a preference annotation by two authors (line 141-143) but doesn't specify independent double-annotation with agreement. However, the manual annotation is a secondary, qualitative complement to the main quantitative results; demanding inter-annotator statistics for a small qualitative study is disproportionate.
- **"No validation set description"** — The paper says "We pick the best checkpoint considering validation loss by evaluating every 50 steps with a batch size of 128" (line 101). The validation set is a held-out subset of the training data (standard practice). This is described adequately.
- **"Figures not visible to this review"** — This is a parser limitation, not a paper flaw. The paper references figures (Fig. 1-6) that exist in the submitted PDF.
- **"No statistical significance reported"** — The paper reports standard errors on harmfulness scores (Figure 1 caption: "with standard errors on bars"). While confidence intervals or p-values would strengthen the analysis, reporting standard errors is standard practice for this type of benchmark evaluation.
- **"Should compare to more complex methods like RLHF or Constitutional AI"** — This is beyond the paper's stated scope (simple data augmentation). Moved to Nice-to-Haves.
- **"The paper could be ready for acceptance after standard benchmark results are added"** — This is an assessment, not a weakness. The severity of the missing benchmarks is retained as a Major weakness above.

---

## Novel Insights

None beyond the paper's own contributions. The reviewers' input triangulates on the same key gap: the paper's central trade-off claim is undermined by the absence of promised standard benchmark results, but the core empirical finding (small amounts of safety data reduce harm) and the auxiliary findings (format mismatch matters, exaggerated safety) are well supported. No reviewer identified a flaw the paper's own analysis had missed.

---

## Suggestions

1. **Report the missing standard benchmark results.** Add a table showing accuracy on PIQA, BoolQ, and OpenBookQA for all safety-tuned variants (0, 100, 300, 500, 1000, 1500, 2000). Even if scores are flat, this evidence is essential to substantiate the central "no capability loss" claim.
2. **Quantify exaggerated safety with refusal rates.** For each safety-tuned model, report the fraction of XSTest prompts that trigger a refusal (e.g., responses starting with "I'm sorry" or "No"). Show the trend: more safety data → higher refusal rate. This would move the analysis from illustrative to systematic.
3. **Report content moderation API results numerically.** The paper references these results (Figure 4 reference) but the extracted text lacks numeric values. Presenting them in a table would strengthen the harmfulness evaluation as an independent signal.
4. **Provide the safety-response generation prompt** used with GPT-3.5-turbo to improve reproducibility.
5. **Include a limitations section** acknowledging the reliance on GPT-3.5-generated safety data, the reward model's training distribution, and the lack of adversarial robustness testing.

---
