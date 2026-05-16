Now I have a thorough understanding of the paper and can verify each reviewer claim against the source text. Let me produce the consolidated final review.

## Summary

This paper presents an empirical study evaluating whether uncertainty-based abstention can improve LLM reliability across three scenarios: correctness on answerable questions, hallucination detection on unanswerable questions, and safety on adversarial prompts. Using statistical uncertainty measures (negative log-likelihood, predictive entropy, semantic entropy) and a verbalized measure (In-Dialogue Uncertainty / InDU — a hedge-word count), tested on Llama2 models (7B–70B), the study finds that selecting the right uncertainty type for each scenario enables effective abstention: statistical uncertainty for correctness and safety, InDU for unanswerable questions.

## Strengths

1. **Scenario-specific uncertainty selection yields large, quantifiable gains.** The paper provides concrete numbers demonstrating meaningful improvements: on TriviaQA, rejecting the 25% most uncertain samples boosts accuracy from 84.4% to 92.6% (+8.2%); on the SelfAware dataset, InDU filters nearly 50% of unanswerable questions at only 10% false positive rate; on AutoDAN, statistical uncertainty on RLHF models filters 99% of unsafe responses with only 10% false refusals. These numbers directly support the paper's core claim.

2. **RLHF preserves and even enhances uncertainty awareness for specific scenarios.** While prior work noted RLHF increases miscalibration, this paper demonstrates that RLHF models maintain strong AUROC for correctness (e.g., 0.85 semantic entropy on TriviaQA) and safety (0.99 negative log-likelihood on AutoDAN), and actually improve InDU for detecting unanswerable questions (AUROC 0.75 with RLHF vs. 0.69 without). This is a non-obvious finding.

3. **Systematic evaluation across diverse datasets and model scales.** The study covers five QA datasets (including reasoning and math), one dedicated unanswerable-question dataset, and two adversarial safety datasets, using model sizes from 7B to 70B. This breadth strengthens the generality of the conclusions.

4. **Methodological clarity in comparing multiple uncertainty metrics.** By jointly evaluating predictive entropy, semantic entropy, negative log-likelihood, and InDU under identical conditions, the paper provides a clean apples-to-apples comparison using both AUROC and Accuracy-Rejection Curves with specific threshold examples.

## Weaknesses

### Fatal
None.

### Major
None. All identified issues are addressable and do not threaten the paper's core claims.

### Minor

1. **ARC evidence for correctness is limited to one dataset.** The paper's abstract claims "improve correctness by 2% to 8%," but Accuracy-Rejection Curves (ARC) are shown only for TriviaQA (Figure 3a). While AUROC values in Table 1 confirm that uncertainty measures can rank correct vs. incorrect responses across all five datasets, the actual accuracy improvement under abstention is demonstrated for only one dataset. Adding ARC plots for at least one or two additional datasets (e.g., SciQA or CoQA) would substantiate the generality of the claim. (Section 5.1, Figure 3a)

2. **Hallucination results use an ROC curve rather than the ARC promised in the methodology.** The methods section states "We compute ARC and AUARC for both hallucinations and safety" (line 102), but for hallucinations only an ROC curve is presented (Figure 3b). While the ROC is informative and the specific operating point (≈50% detection at 10% FPR) is stated, the paper does not deliver the promised ARC/AUARC for this setting. The discrepancy should be resolved — either provide the ARC or adjust the methods text. (Section 5.2, Figure 3b)

3. **AUARC values mentioned in methodology but never reported.** The paper states it computes the Area Under the Accuracy-Rejection Curve (AUARC) — a threshold-free summary — but never reports any AUARC numbers in text, tables, or figure annotations. This is a missed opportunity for a clean comparison across settings. (Section 3.3, line 101)

4. **InDU validation is thin.** InDU is central to the hallucination claim, but the paper provides no analysis of how the hedge-word list performs across individual SelfAware categories (five distinct types of unanswerable questions), nor does it compare against a simple baseline like detecting explicit refusal phrases ("I don't know"). The paper acknowledges InDU "is not a perfect metric" (Section 3.2), but given that the ~50% hallucination reduction claim depends on it, additional validation would strengthen confidence. (Section 3.2, Section 5.2)

5. **No error bars or variance reported.** AUROC values in all three tables are point estimates. Sampling multiple responses for predictive/semantic entropy introduces randomness, but no standard deviations, confidence intervals, or bootstrap estimates are reported. For an empirical study comparing multiple metrics, this makes it difficult to assess whether observed differences (e.g., 0.78 vs. 0.85) are reliable. (Tables 1–3)

6. **The "almost no additional computational overhead" claim is unquantified.** The abstract and results describe the approach as having "almost no additional computational overhead" but semantic entropy requires multiple forward passes (N samples) plus running a Deberta-large entailment model. The paper should quantify this cost (e.g., latency multiplier or FLOPs relative to a single forward pass) to help practitioners assess the trade-off. (Abstract, Section 5.1)

### Trivial

1. **Missing implementation details.** The hedge-word list is referenced to Islam et al. (2018) but not reproduced or summarized; the parameters of the "fuzzy exact match" (e.g., substring matching rules) are not specified. These are easy to fix and would improve reproducibility.

2. **Safety labeling approach not disaggregated.** The paper uses both Llama Guard and a keyword-based approach for labeling safety but does not discuss whether results differ across the two labeling methods. A brief note on agreement/disagreement would be useful. (Section 4.3)

## Nice-to-Haves

- **Additional model family.** The paper uses only Llama2 models. Including at least one other model family (e.g., a Mistral variant with log-probability access) would substantially increase confidence that findings generalize beyond a single architecture.
- **Simple baseline for safety abstention.** Comparing uncertainty-based abstention against a simple guardrail (e.g., "reject if prompt contains explicit keywords") would contextualize the practical gain.
- **Category-wise InDU analysis on SelfAware.** Breaking down InDU performance by the five SelfAware question categories would clarify whether the measure works uniformly or is driven by specific question types.

## Removed Points

- **"The 2–8% correctness improvement claim is empirically undersupported"** — softened to Minor (point 1 above). The AUROC evidence across five datasets supports that the uncertainty measures work; one detailed ARC plus the AUROC table constitutes reasonable support for an empirical study, though more ARC plots would strengthen it.
- **"The hallucination reduction claim lacks an abstention curve"** — softened to Minor (point 2 above). An ROC curve is the standard visualization for binary classification and does show the trade-off across thresholds. The real issue is the mismatch between what the methods section promises (ARC) and what is delivered (ROC), not a missing visualization per se.
- **"No comparison with alternative rejection criterion for safety"** — moved to Nice-to-Haves. The paper's contribution is about uncertainty-based abstention, not about proposing a complete guardrail system. This would be an extension, not a missing essential baseline.
- **"The paper should also cover more domains/tasks"** — removed as scope creep. The paper already covers five QA datasets, one unanswerable-question dataset, and two safety datasets. Demanding broader coverage would turn it into a different paper.
- **"Only operating points illustrated, not systematically tuned thresholds"** — softened. The paper shows ARCs (which cover all thresholds) and highlights specific operating points (5%, 10%, 25%) for concreteness. This is standard practice.
- **Formatting/style nitpicks and parser artifacts** — removed per hard rules. These are not present in the original submission.
- **Criticisms about missing appendix content** — removed per hard rules. The parser strips appendix sections; they exist in the original submission.

## Novel Insights

The paper's most valuable finding is the **scenario-dependent asymmetry** between uncertainty types: statistical uncertainty (entropy-based) works for correctness and safety, while verbalized uncertainty (hedge words) works for detecting unanswerable questions — and these roles do not switch or generalize. Equally notable is the finding that RLHF, despite reducing output diversity and increasing miscalibration, actually *preserves or enhances* the discriminative power of uncertainty measures for both correctness and safety, while specifically improving InDU for unanswerable questions. This nuanced picture is more informative than the blanket "RLHF hurts calibration" narrative common in prior work.

## Suggestions

1. Add ARC plots for at least 1–2 additional correctness datasets (e.g., SciQA, CoQA) to substantiate the 2–8% improvement claim.
2. Either provide the promised ARC/AUARC for the hallucination setting or adjust the methods text to match what is actually presented.
3. Report error bars (e.g., bootstrap confidence intervals) for AUROC values.
4. Include the hedge-word list in the appendix and specify fuzzy exact match parameters.
5. Quantify the computational overhead of semantic entropy (multiple forward passes + entailment model) to support the "minimal cost" claim.

## Score and Decision

The paper is a solid empirical study addressing an important practical problem. The safety results are particularly strong and well-supported. The main gaps are missing supplementary analyses and minor presentation inconsistencies rather than fundamental flaws. The paper's central findings are believable and useful.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>