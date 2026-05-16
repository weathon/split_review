Now I have enough information to construct the final consolidated review. Let me write it.

## Summary

This paper introduces Conditional Activation Steering (CAST), a method that extends standard activation steering by adding condition vectors that determine *when* to apply a behavior vector (e.g., refusal) based on input similarity. The key idea is that different prompt categories activate distinct hidden-state patterns, and these patterns can be extracted as condition vectors. CAST enables programmable behavioral rules such as "if input is about hate speech, then refuse" without weight optimization. Experiments across multiple models (Qwen, Llama, Hermes, OLMo, etc.) demonstrate selective refusal, multi-condition logical composition, and domain constraining.

## Strengths

1. **Selective refusal demonstrated quantitatively across multiple models.** Table 1 shows CAST achieves high harmful refusal rates (e.g., 90.7% for Qwen 1.5 Chat) while keeping harmless refusal near baseline (2.2%), producing a discrepancy of 88.5% — far exceeding the base model's 45.8%. This directly validates the core claim of enabling targeted rather than indiscriminate refusal.

2. **Logical composition of condition vectors for programmable control.** The paper shows that multiple condition vectors can be combined with OR logic (Figure 4a) and that refusal can be both induced and suppressed on specific categories (Figure 3b), enabling complex behavioral rules beyond single-vector steering.

3. **Duality and modulation properties.** The paper systematically identifies that flipping the comparison direction intervenes on the complement set of inputs (duality, Figure 2d) and that threshold θ modulates sensitivity (Figure 2a–c), providing interpretable control absent in existing activation steering methods.

4. **Generalization to unseen prompt categories.** Domain constraining via CAST remains effective on unseen categories (gambling, financial advice, privacy violence, malware generation) as shown in Figure 5b, demonstrating generalization beyond training categories.

5. **Semantic distinctiveness analysis provides explanatory insight.** The paper shows a positive correlation between a category's semantic distance from others and the effectiveness of constraining to that category (Figure 5c), offering a testable explanatory finding about when CAST works best.

6. **Efficiency and saturation properties.** CAST exhibits linear time scaling and performance plateaus with relatively little data (Figure 5a–b), with most experiments replicable within an hour, supporting the claim of computational efficiency without weight updates.

## Weaknesses

### Fatal
None.

### Major

- **Refusal rate detection protocol is not specified.** The paper's central evaluation metric — whether a model output constitutes a "refusal" — is never defined. There is no description of keyword matching, automated classifier, manual review, or any other protocol for determining refusal status. This affects all reported refusal rates in Table 1 and Figures 1–6. Without this specification, the numerical results cannot be independently reproduced or compared across settings. While the relative trends (CAST vs. standard AST vs. base) are visually supported in figures and would likely be robust, the exact numbers in Table 1 are unverifiable as reported.

### Minor

- **No variance or confidence estimates.** Refusal rates are presented as point estimates on test sets of 450–500 examples per class. No confidence intervals, error bars, bootstrap estimates, or replication runs are reported. Given the sample sizes, the numbers likely have nontrivial variance, making it difficult to judge whether observed differences (e.g., between models or threshold settings) are reliable.

- **Missing classifier-based baseline for comparison.** The paper's approach uses cosine similarity with a PCA-extracted condition vector to determine when to steer. A natural baseline — training a simple probe/classifier on the same contrastive hidden states to detect harmful prompts and applying the refusal vector only when the classifier fires — is not included. Such a comparison would clarify whether CAST's particular similarity-with-projection mechanism offers advantages over a separate detection pipeline. The paper would be strengthened by either including this baseline or explicitly arguing why it falls outside the paper's framing (e.g., the condition vector approach maintains a unified representation framework without needing a separately trained classifier).

- **Prompting baseline underspecified.** The prompting baseline in Figure 3c (red dotted line) is described only as "the model is simply prompted to comply with the target condition and refuse other conditions." The exact prompt wording is not given. Since prompting baseline performance is highly sensitive to wording, this omission weakens the comparison.

- **Semantic distance correlation not tested statistically.** The paper claims a positive correlation between semantic distance and constraining effectiveness (Figure 5c) based on visual inspection. A Spearman or Pearson coefficient would strengthen this analysis and provide a precise, testable finding.

- **Machine-generated training data not verified beyond basic quality checks.** The paper trains condition vectors on machine-paraphrased data without filtering beyond basic quality checks (Section 3.2). While the authors note they "found this process generally robust to small data perturbations" and manually checked only the test sets, the training data quality is not independently verified, which could introduce artifacts.

### Trivial

- **tanh transformation not explained.** The paper mentions applying `sim(h, tanh(proj_c h))` "for more predictable behavior" (Section 3.1) but does not explain why tanh is beneficial or how it affects threshold behavior. The element-wise application of tanh to a vector is standard, but the motivation is absent.

- **Reference model configurations not aligned with experimental setup.** Reference models A and B in Table 1 (LLaMA 3.1 Inst 8B, LLaMA 2 Chat 13B) are presented as examples of safe behavior, but the paper does not report whether their evaluation configuration (system prompt, temperature, decoding parameters) was aligned with the CAST experiments. The paper's own footnote acknowledges these are "just examples" and may use different taxonomies, so this is a comparability concern rather than an error.

## Nice-to-Haves

- Adding a statistical test (Spearman/Pearson correlation) for the semantic distance analysis in Figure 5c.
- Including an ablation comparing `sim(h, proj_c h)` (absolute cosine similarity) against the projected formulation to verify whether the projection step is necessary.
- Exploring continuous modulation (scaling α by similarity) as an alternative to the binary step function threshold, which the paper mentions but does not experimentally evaluate.
- Demonstrating CAST on a non-refusal behavior (e.g., style or tone) to support the claim of broader applicability.

## Removed Points

- *Criticism about `sim(h, proj_c h)` being equivalent to absolute cosine similarity.* This is a mathematically correct observation but is not a weakness — it describes what the formulation does, not a flaw. Equivalent formulations are common in the literature.
- *Criticism that reference models are not directly comparable.* The paper's footnote already acknowledges these are "just examples" and may use different harm taxonomies. The paper does not claim to match or beat these references; they are provided as context.
- *Criticism about the paper not covering dynamic thresholding or confidence-based gating.* The paper explicitly states it does not explore modulation beyond the binary threshold (Section 4, "we do not explore it further in this study"). Criticizing this omission is scope creep.
- *Strengths from Strength Finder that were generic.* All six strengths listed were specific and evidence-backed; none were removed.
- *Criticism about missing generalization beyond refusal.* The paper's title and framing are about refusal; demanding non-refusal experiments would be a different paper.

## Novel Insights

The most interesting observation to emerge from combining the reviews is that the paper's core technical contribution (condition vectors as unified detectors and steering triggers) is both its strength and the source of its main evaluation gap. The strength is that the same PCA-based extraction pipeline produces both condition and behavior vectors without separate training; the gap is that the refusal detection metric itself is never specified, so the entire quantitative evaluation rests on an unreported procedure. Additionally, the semantic distinctiveness finding (Figure 5c) — that CAST works better for categories that are further from others in embedding space — is a genuinely useful design principle that the paper identifies but does not fully develop into a predictive guideline.

## Suggestions

1. **Specify the refusal detection protocol.** Clearly state whether keyword matching, a classifier, or manual review was used to determine refusal. If keyword-based, provide the exact list of patterns. If manual, report inter-annotator agreement. This is the single most important fix.

2. **Add variance estimates.** Bootstrap confidence intervals on refusal rates (e.g., 10,000 resamples) would give readers a sense of estimate stability without requiring multiple experimental runs.

3. **Disclose the exact prompt used for the prompting baseline** in Section 5.

4. **Add a Spearman correlation coefficient** to the semantic distance analysis in Figure 5c.

5. **Consider adding a simple probe baseline** in a single setting to bracket whether the condition vector mechanism is necessary or whether any hidden-state detector suffices. Even one additional experiment (e.g., logistic regression probe on layer 7 hidden states to detect harmful prompts, then apply refusal vector) would clarify the marginal contribution of the condition vector formulation.

## Score and Decision

The paper presents a clean, well-motivated extension to activation steering and backs it with experiments across multiple models and conditions. The core claims (selective refusal, logical composition, domain constraining) are supported by the evidence. However, the evaluation is undermined by the unspecified refusal detection metric — a basic reporting gap that prevents verification of the central numerical results. This is fixable and does not invalidate the paper's qualitative findings, but it must be addressed. The paper also lacks variance estimates and a natural classifier baseline. I recommend acceptance after these issues are resolved.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>