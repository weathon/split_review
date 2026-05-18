Now I have thoroughly verified the reviewer's claims against the paper. Let me produce the consolidated review.

---

## Summary

This paper evaluates the ability of six LLMs (GPT-4 Turbo, GPT-4o-mini, LLaMA 3-70B, LLaMA 3-8B, Gemma 2-9B, Gemma-7B) to produce explanations for ML models across two tabular tasks (Adult Income classification, California Housing regression). Using a functionally grounded approach, the authors measure LLM explanations against 11 XAI properties (accuracy, selectivity, fidelity, completeness, contrastness, certainty, degree of importance, consistency, stability, robustness, comprehensibility), comparing them to outputs from conventional XAI methods (DiCE, SHAP, LIME, linear model coefficients). The main finding is that LLMs systematically underperform conventional methods on nearly all technical XAI properties, but produce more readable natural-language explanations.

---

## Strengths

1. **First systematic, multi-property evaluation of LLMs for XAI**: Prior work (Susnjak 2023, Guo et al. 2024, Serafim et al. 2024, Mavrepis et al. 2024) explored LLMs for explanation generation but did not quantitatively evaluate against established XAI properties. The paper fills this gap by applying a functionally grounded evaluation framework (Doshi-Velez & Kim, 2017) across 11 properties, providing evidence that is missing from earlier anecdotal or single-task studies. (Sections 1, 2.3)

2. **Broad and systematic experimental design**: The evaluation covers 6 LLMs spanning different developers (OpenAI, Meta, Google), model sizes (7B–70B+), and generations; 5 ML models per task (2 tasks); and 11 XAI properties with distinct metrics. This breadth allows the paper to construct a profile of LLM strengths and weaknesses rather than a narrow comparison. (Section 3.1)

3. **Evidence-based identification of a genuine LLM strength**: While LLMs perform poorly on most properties, the comprehensibility results (Flesch-Kincaid readability scores) demonstrate that LLMs generate explanations accessible to educated non-expert audiences, whereas conventional XAI outputs often rely on technical jargon. This finding directly supports the paper's constructive proposal that LLMs may serve as "translators" of conventional XAI outputs rather than standalone explainers. (Section 4, Discussion)

4. **Transparent reporting of limitations**: The paper explicitly acknowledges resource constraints (1% test split), dependency on prompt construction, and the lack of standardised XAI benchmarks — and suggests concrete future directions (prompt engineering, few-shot examples, fine-tuning, multi-modal approaches) grounded in the findings. (Section 5)

---

## Weaknesses

### Fatal

None. The empirical results are real and informative even if one disagrees with the framing. No error invalidates the core finding that LLMs systematically disagree with conventional XAI methods on technical metrics.

### Major

1. **Fidelity evaluation covers only linear models, but conclusions generalize to all models**: Fidelity is measured by comparing LLM-estimated coefficients to actual logistic/linear regression coefficients. This is sensible for those two models, but the paper does not define or measure fidelity for Decision Tree, Random Forest, KNN, or Gradient Boosted Tree — which constitute 3 of 5 models per task. The Discussion (Section 5) nonetheless draws conclusions about LLMs' inability to "convey the actual workings of ML models" broadly. The fidelity claim is only supported for linear models. (Section 4, Fidelity paragraph; Section 5, Discussion)

2. **Consistency measurement does not verify that models had similar predictions**: The definition (Section 2.1) specifies consistency as "similarity between explanations of different models trained on the same task with **similar predictions**." However, the experiment (Section 4, Consistency) measures cosine similarity of influential features across all five ML models without checking whether those models made similar predictions on each test instance. If models disagree, low cosine similarity may reflect genuine differences in decision boundaries rather than inconsistency in the LLM's explanations. This is a methodological gap that could affect the validity of the consistency results. (Section 2.1 definition vs. Section 4 measurement)

3. **No variance or uncertainty estimates**: All results (Tables 1 and 2) are reported as point estimates (mean cosine similarity, mean RMSE, etc.) without standard deviations, confidence intervals, or any statistical significance test. The test sets are small (261 and 207 samples) and several metrics (e.g., fidelity, completeness) are averaged across models and samples, so variance could be substantial. Without error bars, the reader cannot judge whether reported differences between LLMs (e.g., llama3-70b at 0.28 fidelity vs. gpt-4-turbo at 0.57) are reliable or noise. This is particularly important because many cosine similarity scores are near zero — the paper interprets these as failures but does not assess whether the metric itself is noisy at those levels. (Section 4, Tables 1 and 2)

### Minor

1. **Framing overclaims by equating "agreement with a specific XAI method" with "satisfying a property" for 4 of 11 properties**: Selectivity is measured against DiCE, completeness against SHAP, degree of importance against LIME, and fidelity against linear coefficients. The paper acknowledges (Section 5) that "there are no standard ground-truth benchmarks for XAI," yet interprets low agreement as evidence that LLMs lack selectivity/completeness/etc. rather than that they disagree with a particular operationalization. This is a framing issue rather than a fatal flaw — the empirical comparison is still informative — but the conclusions (e.g., "LLMs lack the capacity to understand the influence of input features") are stronger than what the evidence directly supports. A more precise framing would be: "LLM explanations show low agreement with DiCE counterfactuals, SHAP values, LIME, and linear model coefficients."

2. **No discussion of chance-level or random baselines**: Several cosine similarity scores are near zero or negative. The paper interprets these as failures, but does not state what the expected cosine similarity would be between random feature-weight vectors. If chance-level cosine similarity is near zero, then a near-zero result is not evidence of deficiency — it may simply reflect that the metric has a zero baseline. Adding this context would sharpen the interpretation. (Section 4)

3. **Contrastness metric for regression uses a range (20–40%) without justification and an imprecise evaluation**: The California Housing contrastness metric computes the average percentage change and checks whether it falls in [0.20, 0.40]. The choice of this range is not explained, and the metric does not penalize going over 40% (e.g., a 100% increase could produce the same average as a 30% increase). Absolute deviation from the midpoint of the target range would be more precise. (Section 4, Contrastness paragraph)

### Trivial

- The robustness results (error rates) are described qualitatively ("frequent basic errors," "larger models had the lowest rates") in the main text rather than reported as exact percentages in Tables 1 and 2.
- The consistency section has a typo: "he larger LLMs" (should be "The larger LLMs").

---

## Nice-to-Haves

- Reporting standard deviations for each metric across test samples and models.
- Including a random-vector baseline for cosine-similarity-based metrics to contextualize near-zero scores.
- For selectivity, clarifying in the main text how DiCE counterfactual instances were converted to feature-importance vectors for cosine similarity computation (details available in Appendix A.2/A.3).
- For contrastness (regression), considering absolute deviation from the target midpoint as a supplementary metric.
- Verification that models used in the consistency evaluation actually made similar predictions on the test instances, or a sub-analysis restricted to instances where models agreed.
- Reporting exact error percentages for the robustness metric in the tables.

---

## Removed Points

These points from the reviewers were identified as problematic under the hard rules and are removed, meaning they should not be treated as valid weaknesses:

- **Criticism about the paper using conventional XAI methods as "de facto ground truths," claiming the paper conflates method agreement with property satisfaction across "nearly every property."** Verified: only 4 of 11 properties (selectivity, fidelity, completeness, degree of importance) rely on comparison to a single conventional method. Accuracy, contrastness, certainty, consistency, stability, robustness, and comprehensibility use different evaluation approaches (actual labels, model decision changes, model probabilities, cross-model agreement, repeated-sample stability, error rates, readability). The paper also explicitly acknowledges (Section 5) that "there are no standard ground-truth benchmarks for XAI" and justifies the approach as a functionally grounded comparison against established methods. The critic's generalization to "nearly every property" is factually inaccurate based on the paper's own description.

- **Criticism that robustness metric "conflates instruction-following with robustness."** The paper explicitly defines robustness as "the ability of the LLM-generated explanations to be error-free" (Section 4, Robustness paragraph). This is a clear, narrow operationalization of a self-defined property. The paper does not claim to measure the broader concept of XAI robustness (stability under input perturbations), which is tested separately under "stability." The paper's own definition is internally consistent.

- **Criticism that "Comprehensibility" uses only Flesch-Kincaid and the conclusion is "too strong."** The paper explicitly calls Flesch-Kincaid a "proxy for comprehensibility" (Section 4, Comprehensibility paragraph). The conclusion that LLMs "present model outputs in a more understandable way" is tempered by the proxy language and is a reasonable inference from the readability data.

- **Criticism about the paper not comparing against models/tasks outside its scope** (e.g., wanting image/text modalities). The paper explicitly limits itself to two tabular datasets (Adult Income, California Housing) and acknowledges this in the limitations (Section 5). Demanding broader modality coverage would change the paper into a different study.

- **Criticism about the 99%/1% split being too small.** The paper acknowledges this as a resource constraint (Section 5). The split is transparently reported and the limitation is discussed.

- **Criticism about "missing appendix" content** — the parser strips appendices from all papers; they exist in the original submission.

---

## Novel Insights

The reviews do not generate insights beyond the paper's own findings. The core tension — that the paper's framing equates "disagreement with SHAP/LIME/DiCE" with "failure to satisfy a property" — is a genuine framing concern, but it is primarily a presentational issue rather than a discovery about the method or results. The paper's own most important finding (LLMs are poor at technical XAI properties but excellent at readability) remains intact regardless of how the framing is adjusted.

---

## Suggestions

1. **Reframe the evaluation as a comparative benchmarking study** rather than a definitive property-satisfaction test. Change statements like "LLMs lack completeness" to "LLMs show low agreement with SHAP values on feature marginal contribution estimation." The empirical contribution stands on its own without the stronger framing.

2. **For fidelity, either (a) extend the evaluation to non-linear models** using an appropriate operationalization (e.g., feature permutation tests, or checking whether the LLM explanation correctly identifies which features matter to the model's predictions), or **(b) explicitly restrict fidelity claims to linear models** and clarify that fidelity for non-linear models was not measured.

3. **For consistency, either (a) filter to instances where models made similar predictions** before computing cross-model similarity, or **(b) acknowledge the gap** and note that the current consistency scores may conflate genuine consistency with models agreeing (or disagreeing) on their predictions.

4. **Add standard deviations or interquartile ranges** to all metrics in Tables 1 and 2, and discuss the most notable variance patterns.

5. **Add a random/chance baseline** for cosine-similarity metrics (expected value of cosine similarity between two random vectors of the feature dimension) to contextualize low scores.

6. **Tone down the claim of being "the first rigorous evaluation"** (line 168) — it invites skepticism even if true. Instead, emphasize the systematic methodology and the specific gaps filled.

---

## Score and Decision

The paper makes a real contribution: it is the broadest quantitative evaluation of LLMs for XAI to date, covering 6 LLMs, 5 ML models, 2 tasks, and 11 properties. The empirical work is careful, the methodology is transparently documented, and the limitations are honestly acknowledged. The main weaknesses are (a) a framing that overinterprets method-agreement as property-satisfaction for 4 properties, (b) fidelity only being measured for linear models, (c) consistency not verifying similar model predictions, and (d) missing variance estimates. None of these is fatal; all are addressable in a revision. The paper would benefit from a more precise framing and additional robustness checks, but the core empirical contribution is informative and timely.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>