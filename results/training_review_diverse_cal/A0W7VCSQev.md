Now I have a thorough understanding of the paper and can verify all claims. Let me compose the final review.

---

## Summary

This paper introduces QK-score and Attention-score, extracted from "select-and-copy" attention heads in LLMs, as an alternative to standard logit-based decoding for multiple-choice QA. The key idea is that certain attention heads in middle layers perform a semantic option-selection operation whose signals can outperform the model's own final-layer logits, especially when format-following degrades output accuracy. Experiments across LLaMA2 (7B–70B) and LLaMA3 (8B–70B) models on MMLU, CosmosQA, HellaSwag, HaluDialogue, and a synthetic dataset show consistent gains, including up to 27 percentage point improvement on HellaSwag with LLaMA3-8B and near-perfect accuracy on the synthetic task where the baseline is near-random.

## Strengths

1. **Consistent and significant accuracy gains across models and benchmarks.** QK-score improves over the logit baseline by 7–16% (absolute) on LLaMA2-7B and up to 10% on larger models across four real MCQA datasets (Table 1, Figure 3), demonstrating the practical value of probing internal head signals.

2. **Causal evidence via zero-ablation.** Removing the top 10 select-and-copy heads causes accuracy to drop substantially, often below random chance (Figure 6). This provides a causal link between these specific heads and task performance, beyond mere correlation.

3. **Robustness to option permutation and selection bias.** The Permutation Accuracy (PA) metric shows QK-score is consistently more stable than the baseline under random option re-ordering (Table 1, Figure 3), and the analysis reveals complementary bias patterns across heads (e.g., head (14,20) biased toward A/D, head (14,24) toward B/C) that partially mitigate positional biases.

4. **Cross-model and cross-dataset generality of select-and-copy heads.** The same heads (notably (14,24) and (14,20) in LLaMA2-7B) appear among the top performers across multiple datasets and shot settings (Figure 8a), and the method yields gains from 7B to 70B models (Table 1), showing the phenomenon is not artifact of a single model or task.

5. **Unsupervised head discovery without labeled validation data.** The paper proposes an attention-concentration-and-variability score that identifies the same robust heads without requiring labeled validation data (Section 6.4), enabling application in label-scarce scenarios.

## Weaknesses

### Fatal
None. None of the identified issues invalidate the paper's core claims.

### Major

1. **Head selection advantage conflated with the core mechanism in main results.** The paper reports test accuracy using per-condition best heads selected on 5% validation labels (with labels), while the baseline receives no analogous adaptation. This makes it impossible to determine how much of the reported gain comes from the QK-score mechanism itself versus from validation-driven cherry-picking across 1024 heads. The paper partially addresses this with universal head analysis (Figure 8) and unsupervised selection (Section 6.4), but these analyses are presented separately and do not feed into the main results table. The headline "up to 16% gain" could partly reflect the selection advantage. A table column reporting QK-score with a *fixed* universal head (e.g., (14,24)) across all conditions would cleanly separate mechanism from selection.

### Minor

2. **Tension between the QK-score and the paper's mechanistic interpretation.** The QK-score explicitly omits positional encoding (RoPE) that the model itself uses in actual attention computation (lines 116–117). The paper is transparent about this and provides a rationale (focus on semantics over position), but the claim that certain heads "select the proper option and copy the information from it" (line 82) refers to what the head *actually* does during normal forward passes. QK-score's success without RoPE could partly stem from it being a useful derived quantity that diverges from actual head behavior. The paper shows one comparative example (Figure 7) but no systematic correlation analysis between QK-score and actual pre-softmax attention (with RoPE) across many examples. This gap weakens the mechanistic narrative.

3. **No variance or stability estimates.** All reported accuracies are point estimates with no error bars, confidence intervals, or multiple-seed runs. This is common practice in LLM evaluation, but it matters here because (a) head selection uses only 5% of the data — different validation splits could yield different best heads — and (b) some reported gains are small (e.g., MMLU LLaMA3-70B: 74.5 vs 75.3), where the conclusion could flip under reasonable variance. Without variance estimates, the reliability of small-margin results is uncertain.

4. **E/F prediction rates not reported.** The paper adds "E. None of the above" and "F. I don't know" options to every question (always incorrect) but never reports how often either the baseline or QK-score predicts these options. If QK-score systematically avoids E/F while the baseline predicts them more often, this could mechanically inflate QK-score's accuracy without reflecting better option discrimination among A–D. Reporting E/F prediction rates is necessary to interpret the gains.

### Trivial
None.

## Nice-to-Haves

- A systematic correlation analysis between QK-score (without RoPE) and actual pre-softmax attention (with RoPE), showing that their rankings of options are largely consistent. This would resolve the mechanistic tension.
- A table column showing QK-score results using a fixed universal head (e.g., (14,24)) across all datasets and shot settings, to separate the mechanism from the selection advantage.
- Reporting E/F prediction rates for both baseline and QK-score to verify the gains are not driven by differential avoidance of these always-wrong options.
- Additional discussion of why the HellaSwag baseline is so low (33.5% for LLaMA3-8B) and how much of the 27-point gain reflects format recovery versus actual knowledge extraction.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *Reviewer claim about missing code/data release*: The parser likely stripped appendix sections; the paper cites its synthetic dataset (SSD) and references figures. This raises no verifiable concern about the submission's completeness.
- *Reviewer claim about computational cost not being mentioned*: A reasonable practical question but not a methodological weakness that affects the paper's validity.
- *Reviewer suggestion that the synthetic dataset may have in-distribution words*: Highly unlikely given the words are drawn at random; the paper's design is defensible for testing format following.
- *The HellaSwag baseline being "surprisingly low"*: The paper explicitly notes it added E/F options (line 151), changing the task from 4-option to 6-option, which likely explains the low baseline. This is an acknowledged design choice, not an oversight.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between the mechanistic claim and the modified QK-score, the confounding of head selection with mechanism evaluation, and the need for variance estimation — all of which are useful refinements but do not constitute new findings.

## Suggestions

1. Add a main-results column using a fixed universal head (e.g., (14,24)) selected without validation labels, alongside the per-condition best head results. If the universal head still outperforms the baseline by most of the margin, this would strongly support the mechanistic claim.
2. Run a correlation analysis: for each head and each question, compute both the actual pre-softmax attention (with RoPE) and the QK-score (without RoPE) for option-representative tokens, and report how often their argmax rankings agree.
3. Report E/F prediction rates for both baseline and QK-score across all conditions.
4. Provide variance estimates either through multiple validation/test splits or bootstrap resampling, especially for cases where the gain margin is small.

## Score and Decision

This paper presents a genuinely interesting approach to extracting knowledge from LLM internals for MCQA, with strong empirical support from a range of models and a clever synthetic validation. The weaknesses are real but addressable: the head-selection advantage partially confounds the mechanistic interpretation, and a few important diagnostic details (E/F rates, variance estimates, systematic QK-attention correlation) are missing. These can be remedied in revision without changing the paper's core contributions.

**Originality**: Good — the select-and-copy head formulation and QK-score are novel.
**Importance**: High — addressing format-following failures in MCQA is practically relevant.
**Soundness**: Moderate — strong ablation and synthetic evidence, but the main comparison is confounded by head selection.
**Clarity**: Good — the method is clearly described and the figures are helpful.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>