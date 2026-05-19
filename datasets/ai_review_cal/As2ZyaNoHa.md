- Decision: Reject
- Avg Score: 3.33
- Scores: 3, 1, 6
Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper studies whether LLMs exhibit systematic temporal and cross-sectional knowledge gaps in the financial domain. It constructs RevenuePromptDataset (190k+ question-answer pairs covering 17k+ companies across 1980–2020), evaluates GPT-3.5, Llama-3-8B/70B, GPT-4, and Gemini, and finds that LLMs are significantly more accurate for recent years (post-1995) and for larger, more visible companies. It further claims that LLMs simultaneously hallucinate *more* for those same companies and years where they are most accurate — an overconfidence pattern. The core contributions are the large-scale temporally deep evaluation dataset and the systematic documentation of knowledge biases along temporal and cross-sectional dimensions.

## Strengths

1. **Novel large-scale documentation of retrograde knowledge bias in LLMs.** The paper provides clear evidence that LLMs perform dramatically worse on older financial data (e.g., Llama-3-70B: 52.01% accuracy for 2018 vs. 7.47% for 1995), even though that data has been publicly available for decades. Figure 4 and the accompanying analysis convincingly establish this temporal gradient across multiple models.

2. **Temporally deep, large-scale evaluation dataset.** RevenuePromptDataset (190k+ QA pairs, 41 years, 17k+ unique companies) is a substantial resource that enables analyses far beyond typical static QA benchmarks. The dataset construction is well-documented (Section 2.1), and the use of multiple models (including GPT-3.5, Llama-3-8B/70B, GPT-4, Gemini) provides breadth.

3. **Multi-factor cross-sectional investigation with year fixed effects.** The paper examines five distinct firm-level characteristics (market cap, retail attention, institutional attention, SEC access, readability) using logistic regressions with year fixed effects (Section 4). This provides a systematic, multivariate-framed account of which company attributes correlate with LLM knowledge gaps.

4. **Clear real-world motivation and practical significance.** The paper is well-framed around the "democratization of financial knowledge" narrative and the documented heavy use of LLMs by retail investors (Cheng et al., 2024; Oehler & Horn, 2024). The findings have direct implications for investors, financial literacy educators, and LLM developers.

5. **Reproducibility commitment.** Code, prompts, and model outputs will be made public (Abstract).

## Weaknesses

### Fatal

None. The core temporal finding and the cross-sectional accuracy findings are reproducible and well-supported even if the hallucination analysis needs clarification.

### Major

1. **The hallucination analysis conflates answer propensity with actual hallucination probability.** This affects a headline claim and needs to be addressed for the paper to be fully credible.

   The paper runs two separate logistic regressions (Equation 3): one for success (Y=2 vs. Y≠2) and one for hallucination (Y=1 vs. Y≠1). In the hallucination regression, the baseline group (Y≠1) includes both correct answers (Y=2) *and* refusals/abstentions (Y=0). If larger companies and more recent years elicit more numerical responses overall (i.e., fewer Y=0), then the positive coefficient in the hallucination regression could reflect higher *response propensity* rather than a higher conditional probability of hallucination given a numerical answer.

   The paper's claim that "the model is more likely to hallucinate for the same companies for which it is also more likely to provide the correct answer" (Section 4.3) rests on combining the positive coefficients from the success and hallucination regressions. But because the refusal rate (Y=0) likely varies systematically with market cap and year, the similarity in coefficients could be at least partially mechanical. Figure 5 provides suggestive evidence but does not resolve this confound, since it also counts years unconditionally. A conditional analysis (e.g., multinomial regression, or examining P(Y=1 | Y∈{1,2}) ) is needed to validate this claim.

   *Why it matters:* This is the paper's most attention-grabbing finding. While the temporal and cross-sectional accuracy findings are robust, the "overconfidence" claim about simultaneous accuracy and hallucination needs stronger support than currently provided.

2. **Cross-sectional variables are tested only in isolation, not jointly.** Table 2 reports separate regressions for each company-level variable (plus year fixed effects). Because market cap, retail attention, institutional attention, SEC access, and readability are all correlated, the individual coefficients may absorb shared variance. The positive coefficient for, say, readability could simply proxy for market cap. A multiple regression including all variables simultaneously is needed to establish which factors have independent predictive power. The paper's language ("lower readability leads to a decrease in the performance of LLMs") implies causal or independent effects that the current design does not support.

   *Why it matters:* This weakens claims about which specific firm characteristics *independently* matter. However, the core finding about market cap (size) does not depend on this — it is well-established in the univariate regression.

### Minor

1. **The 10% absolute-error threshold is arbitrary and untested.** The paper defines success as <10% error and hallucination as ≥10% without justifying this specific cutoff or testing sensitivity to it (e.g., 5%, 20%). Given that error magnitudes are likely heavy-tailed, different thresholds could shift patterns. A brief robustness check (even as an appendix note) would strengthen the evidence.

2. **Missing data handling for cross-sectional variables with different coverage periods is not discussed.** Robinhood data covers only 2018–2020, SEC Access only 2003–2017, Bog Index 1994–2021. The paper does not explain how these varying coverage windows are handled in the regressions (listwise deletion? variable-specific subsamples?). The "full sample with year fixed effect" description for Table 2 is ambiguous when the independent variable itself has limited temporal coverage.

3. **Regression tables lack standard errors and sample sizes.** Table 2 and Table 3 report coefficients and significance stars but no standard errors or observation counts per model. Standard errors (and whether they are clustered by firm, year, or both) are essential for evaluating precision. Per-model sample sizes are needed to assess whether comparisons across models are affected by different data subsets.

4. **Figure 4 error bands are underspecified.** The caption states "standard deviation of model performance" but does not clarify whether this is the standard deviation across companies within a year, across bootstrap resamples, or something else. Confidence intervals (e.g., 95% CI via bootstrap) would be more informative.

### Trivial

None of note.

## Nice-to-Haves

- **Conditional hallucination analysis:** Report the hallucination rate *conditional on the model giving a numerical answer* (i.e., P(Y=1 | Y∈{1,2})). This would cleanly separate the probability of hallucinating from the probability of responding.
- **Multiple regression for cross-sectional analysis:** Add a table with all company-level variables included simultaneously to assess independent predictive power.
- **Threshold sensitivity:** Show that the main temporal and cross-sectional results are robust to thresholds of 5%, 10%, and 20%.
- **Refusal rate analysis:** Report how the refusal rate (Y=0) varies with company size and year, to contextualize the hallucination findings.
- **The La Liga soccer example** (Section 5) is acknowledged as illustrative, but reporting effect sizes for the same two findings (temporal and cross-sectional) would make it more convincing as evidence of generalizability.
- **Continuous error analysis:** Complement the binary logistic regressions with a continuous analysis (e.g., regressing log absolute error on firm characteristics) to reveal richer patterns.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Criticism that "first study" claim is too strong and should be softened.* The paper already uses "To the best of our knowledge" (Section 1, bullet 2). The critic misread the text. **Removed as factually incorrect.**
- *Criticism that the paper does not discuss whether temporal improvement after 1995 is tied to EDGAR data availability.* The paper explicitly states: "It's pertinent to highlight the dotted line at the year 1995, signifying the inception of the SEC's EDGAR filing system. After this date, detailed financial information from US public companies became publicly accessible online, thus augmenting the datasets available for model training" (Section 3.2). **Removed as factually incorrect.**
- *Criticism about missing related work.* Per rules, I cannot mention missing related works without external verification. **Removed.**
- *Criticism about missing appendix content or proofs.* The PDF parser strips these; they exist in the original submission. **Removed.**
- *Formatting/presentation nitpicks.* **Removed per rules.**
- *Criticism that the La Liga example is too brief to demonstrate generalizability.* The paper frames it as "an example of an extension" and "a clear demonstration of the value" — not as rigorous validation. Criticizing it for not being more rigorous is scope creep. Moved to Nice-to-Haves.
- *Strength Finder's generic strengths about "addressing an important problem" and "targeting an interesting question."* These are generic and not specific to the paper's content. **Removed.**
- *Strength Finder's claim about "counterintuitive finding of simultaneous higher accuracy and higher hallucination" as a strength.* The weakness (#1 above) directly undermines the evidence for this finding. Per the rule "when a strength and weakness disagree, the weakness wins," this strength is demoted and its validity is contingent on resolving the confound.

## Novel Insights

None beyond the paper's own contributions. The Harsh Critic's main insight — that the hallucination regression conflates answer propensity with conditional hallucination probability — is a standard statistical concern but is usefully applied to this paper's design. The paper's core contributions (temporal gradient documentation, large-scale evaluation dataset) stand on their own regardless.

## Suggestions

1. **Rerun the hallucination analysis conditioned on giving a numerical answer** (i.e., exclude Y=0 from the hallucination regression, or use a multinomial logit with three outcomes). This is the single most impactful revision: if the positive coefficient persists, the claim is substantially strengthened; if it disappears, the result is an artifact, and the paper should acknowledge this honestly.
2. **Add a multiple-regression table** including all cross-sectional variables simultaneously with year fixed effects, so readers can assess which factors have independent predictive power beyond market cap.
3. **Report standard errors and sample sizes** in all regression tables, and clarify whether standard errors are clustered.
4. **Add a threshold sensitivity analysis** (e.g., 5%, 10%, 20%) for the main temporal and cross-sectional findings.
5. **Clarify how missing data is handled** for variables with different coverage periods (Robinhood, SEC Access, Bog Index, etc.).
6. **Report refusal rates (Y=0)** across conditions to contextualize both the success and hallucination analyses.
