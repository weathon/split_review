Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes a guardrail-agnostic framework for evaluating societal bias in LVLMs. The key innovation is replacing attribute-inferring prompts (which trigger refusals from safety-guarded models) with person-irrelevant prompts (story generation, term explanation, exam-style QA) while attaching face images as provisional user context. The method achieves zero refusals across all 20 tested models and reveals that all models exhibit demographic disparities in their outputs, though proprietary models show lower bias than open-source ones.

## Strengths

- **Identifies a critical and timely practical problem**: Table 1 empirically confirms that existing bias benchmarks suffer from refusal rates of 49%–100% on proprietary models and 10%–94% on many open-source models, providing strong motivation for a new evaluation paradigm. This is the paper's most valuable contribution.

- **Achieves zero refusals across all tested models**: The "Ours" row in Table 1 shows 0% refusal rates for GPT-5, Claude 3.7 Sonnet, InternVL3.5, and 16 other models, directly demonstrating that person-irrelevant prompts circumvent safety guardrails and enable bias evaluation where prior benchmarks fail.

- **Broad and systematic evaluation**: Evaluating 20 recent LVLMs (16 open-source, 4 proprietary) across three diverse tasks (story generation, term explanation, exam-style QA) provides a valuable snapshot of current model behavior on a unified protocol.

- **Creative three-task design**: The tasks are thoughtfully chosen to probe different output modalities (open-ended generation, explanation, multiple-choice), and the paper shows that bias scores vary systematically with task openness (Observation 2.2: 27.23 vs. 4.67 vs. 1.48), supporting the need for multi-task evaluation.

- **Methodological care in demographic matching**: The paper explicitly ensures non-target demographic distributions (e.g., race and age when analyzing gender) are aligned between groups, a practice that addresses spurious confounds often overlooked in prior work.

## Weaknesses

### Fatal
None.

### Major

- **The central claim about measuring "societal bias" rests on an unvalidated normative assumption.** The paper's Hypothesis 1 — that an unbiased model's outputs should be statistically independent of user demographics — is stated without empirical or theoretical justification for why demographic disparities in person-irrelevant tasks constitute *harmful* bias rather than benign personalization, demographic reflection, or the model adapting outputs to be relatable to the user. The observed pattern (e.g., stories for male users feature mechanics, for female users nurses) could reflect the model trying to generate relatable content or mirroring training data correlations, neither of which necessarily constitutes harmful stereotyping in the sense that fairness research typically cares about. This does not invalidate the method as a *measurement of demographic disparity*, but it calls into question whether the headline claim — "all models undesirably use user demographic information" — is properly supported. The paper would benefit from either (a) a clear argument for why statistical parity is the correct fairness criterion for these tasks, or (b) framing the contribution more modestly as measuring demographic disparities rather than "societal bias."

- **The refusal-rate comparison is not controlled for image content.** Table 1 compares refusal rates on prior benchmarks (which use multi-person or scene images) against the authors' method (which uses FairFace face-centric images). The zero refusal rate could be driven by image content (face-only images may not trigger visual guardrails) rather than the prompt design. A controlled experiment using the *same* FairFace images with both attribute-inferring prompts and person-irrelevant prompts is needed to attribute the zero refusal rate to the prompt paradigm. Without this, the claim that the method is "guardrail-agnostic" is not fully established, as it may simply be avoiding triggers by changing the image distribution rather than decoupling the task from the person.

### Minor

- **Figure 3's caption contains confusing/inconsistent correlation values.** The figure caption lists asymmetric values for the same pairs (e.g., "Story Gen. to Term Exp. (r = 0.49)" vs. "Term Exp. to Story Gen. (r = 0.60)"; "Exam QA to Term Exp. (r = 0.08)" vs. "Term Exp. to Exam QA (r = 0.93)"). These cannot both be correct if they are Pearson correlations. While the text body's claims (task-wise correlations of −0.11 to 0.21; gender-race correlations of 0.49, 0.60, 0.93) are internally consistent, the figure's presentation conflates task-wise and cross-bias correlations, and the asymmetric values indicate a formatting error or mislabeling that undermines readability and trust. The authors should clarify which values correspond to which line type and ensure symmetry.

- **The TVD metric is applied to accuracy scores in exam-style QA in a non-standard way.** For exam-style QA, the paper computes TVD as "the deviation of accuracies from their mean," which is not the standard definition of Total Variation Distance (which applies to probability distributions). This needs to be clearly explained and justified, or a more appropriate metric (e.g., demographic parity difference) should be used.

- **Exclusion of LLaVA-1.6 variants from exam-style QA is not fully justified.** The paper excludes these models because "near-random accuracies lead to misleadingly low bias scores." However, if a model performs at chance, a low TVD is interpretable (the model is not capable enough to exhibit bias) and including it would provide a complete picture. Excluding them may artificially inflate the correlation between bias and performance.

- **No uncertainty estimates are reported.** Table 2 reports bias scores without confidence intervals or standard errors. Given the modest sample sizes (500 images for story generation, 100 for term explanation), bootstrap confidence intervals would meaningfully inform readers about the reliability of model rankings.

- **The LLM assistant used for attribute extraction (Qwen3-32B) could itself introduce bias.** While the paper notes that its judgments align with human judges (deferred to Appendix D), the risk of the judge being affected by demographic cues in the extracted story content is not discussed in the main text.

### Trivial

- The term "attribute-infering" appears to be a typo ("attribute-inferring") in several places.
- The figure caption in Figure 3 is difficult to parse; consider reformatting to clearly separate solid-line (task-wise) and dotted-line (gender-race) correlations.

## Nice-to-Haves

- A controlled experiment applying both prompt types to the same FairFace image set to isolate the effect of prompt framing on refusal rates.
- Human evaluation to validate whether the observed demographic disparities are perceived as harmful stereotyping versus benign personalization.
- Extension to additional demographic axes (e.g., age, perceived socioeconomic status) and tasks (e.g., career advice as discussed in Section 5).
- Providing individual prompt-image pair variance (e.g., histograms of TVD across prompts) to assess whether bias is driven by a few extreme cases.

## Removed Points

These points are flagged to be removed — treat them with caution.
- **Criticism about missing appendix content (e.g., "TVD definition deferred to Appendix A (not provided)")**: The appendix exists in the original submission but was stripped by the PDF parser. The paper clearly states these details are in the appendix.
- **Criticism that the paper does not discuss whether refusals stem from guardrails or training data biases**: This distinction does not affect the paper's core argument that prior benchmarks are unreliable due to high refusal rates.
- **Criticism about "non-target demographic distributions" matching not being specified**: This is a detail appropriately placed in the appendix; the paper clearly states that matching is performed.
- **Claim that the paper "conflates any statistical difference with bias" as a fatal error**: This is a legitimate philosophical debate but not a methodology error; the paper transparently states its operational definition (Hypothesis 1) and many fairness papers adopt similar demographic parity criteria. It is a limitation worth noting but not a fatal flaw.
- **Demand for the paper to "quantify what fraction of prompts are actually valid bias measurements after filtering refusals"**: The paper's Table 1 already shows refusal rates, and the implication is clear — high refusals make the remaining sample unrepresentative.
- **Demand to discuss whether the model is "reflecting statistical correlations in the training data" rather than stereotyping**: This is essentially the same philosophical question as Point 1 above and does not affect the validity of the disparity measurement.
- **Generic formatting/style nitpicks**: Per instructions, these are parser artifacts.

## Novel Insights

The most interesting insight from the reviews is that the paper's core methodological contribution — achieving zero refusals via person-irrelevant prompts — is solid and clearly demonstrated, but the *interpretation* of the resulting measurements as "societal bias" is conceptually fragile. This tension is common in fairness research: there is often a gap between what a metric measures (statistical disparity) and what researchers claim it measures (harmful bias). The paper would be strengthened by either closing this gap with a principled argument or reframing its claims. The three-task design revealing that bias is task-dependent and not monolithic is a genuinely useful empirical finding that holds regardless of one's stance on the bias interpretation debate.

## Suggestions

1. **Add a controlled refusal experiment**: Apply both attribute-inferring prompts from prior benchmarks and the authors' person-irrelevant prompts to the *same* FairFace image set. This would cleanly isolate the effect of prompt design from image content and directly support the guardrail-agnostic claim.

2. **Clarify the normative basis for Hypothesis 1**: Add a paragraph explaining why statistical independence of outputs from user demographics is the appropriate fairness criterion for these tasks, or alternatively reframe claims to "demographic disparity measurement" rather than "societal bias evaluation."

3. **Fix Figure 3**: Ensure correlation values are symmetric for Pearson correlations and clearly separate solid-line (task-wise) from dotted-line (gender-race) values in the caption.

4. **Report uncertainty**: Add bootstrap confidence intervals or standard errors for the bias scores in Table 2.

5. **Clarify the TVD computation for exam-style QA**: Explicitly state the formula used, as applying TVD to a mean accuracy (a scalar per group) is non-standard.

---

## Score and Decision

### Calibration Anchors

I retrieved these anchors via `calibration_search` and read them in full to calibrate my score:

| Path | Avg Human Score | How it compares to this paper |
|------|----------------|-------------------------------|
| `VKGTGGcwl6.md` "LLMs Get Lost In Multi-Turn Conversation" | 8.00 (Oral) | Significantly stronger — cleaner methodology, novel decomposition of performance, broader empirical rigor. This paper is not at this level. |
| `DG4S2OlGQA.md` "Vision Language Models are Biased" | 5.50 (Poster) | Similar topic area. That paper has cleaner ground-truth evaluation (counterfactual images with known answers) but narrower scope. This paper addresses a more practically important problem but has more interpretation issues. Slightly below this anchor. |
| `3rO59y6pgO.md` "Revealing the Impacts of ICL on Gender Bias" | 5.33 (Reject) | Similar domain (LVLM bias). That paper was rejected partly due to limited task scope and unclear figures. This paper is broader (20 models, 3 tasks) and has stronger empirical evidence, but shares some presentation clarity issues. Comparable quality. |
| `GLmPZhhCAE.md` "Benchmarking Bias Mitigation" | 5.50 (Poster) | Similar domain (bias in LVLMs). That paper had cleaner evaluation with standardized benchmarks. This paper has a more novel methodological contribution (circumventing guardrails) but messier execution. |
| `bKkdttFgYQ.md` "SEEING THROUGH LANGUAGE" | 3.00 (Reject) | Weaker — narrow domain (kitchen objects), questionable use of "bias" framing. This paper is substantially better: broader scope, more models, more practical relevance. |
| `YAYhkZYRNY.md` "My Answer Is NOT 'Fair'" | 0.67 (Reject) | Far weaker — major presentation issues, not ready for review. This paper is clearly superior in writing and contribution. |

### Score Rationale

The paper has a genuine and timely contribution (demonstrating that guardrail-agnostic evaluation is feasible via person-irrelevant prompts) and provides broad model coverage. However, it has three meaningful weaknesses that prevent it from being a strong paper: (1) the normative assumption equating demographic disparity with harmful bias is not adequately justified; (2) the refusal-rate comparison lacks a controlled experiment ruling out image-content confounds; (3) presentation issues in Figure 3 undermine readability. Against the anchors, this paper sits between the 5.0–5.5 range — it has real strengths that distinguish it from rejected papers (3.0 and below) but lacks the polish and rigor of the top-tier papers (7.0+). The weaknesses are addressable but substantive enough to hold the paper back from a strong accept.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>