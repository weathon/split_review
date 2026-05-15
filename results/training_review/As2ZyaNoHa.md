Now I have everything I need. Let me synthesize the final consolidated review.

---

## Summary

This paper investigates temporal and cross-sectional knowledge gaps in LLMs using over 190k revenue questions spanning 41 years and 17k U.S. companies. It finds that LLMs are significantly more accurate for recent years (e.g., Llama-3-70B-Chat: 52% success for 2018 vs. 7.5% for 1995) and for larger, more prominent companies. A paradoxical finding is that hallucination rates also increase for the same large, recent firms where accuracy is highest, suggesting overconfidence. The paper contributes a systematic evaluation framework and a large-scale dataset spanning five LLMs.

## Strengths

- **Large-scale, multi-model evaluation of temporal knowledge gaps**: The paper evaluates 190k+ QA pairs across 41 years and 17k companies using GPT-3.5, Llama-3-8B, Llama-3-70B, plus subsets for GPT-4 and Gemini 1.5 Pro. The temporal finding — that accuracy drops sharply for years prior to ~1995 despite public data availability — is clearly demonstrated and robust (Figure 4; Llama-3-70B-Chat: 52% for 2018 vs. 7.5% for 1995).

- **Novel cross-sectional analysis linking firm characteristics to LLM performance**: The paper is the first to systematically connect LLM financial QA accuracy to market cap, retail investor attention (Robinhood), institutional attention (Bloomberg AIA), SEC filing access, and filing readability (Table 2). The market cap result (log-odds increase of ~0.96 per 10× increase for Llama-3-70B) is large and consistent across models.

- **Counterintuitive hallucination finding**: The observation that hallucination rates *also* increase with market cap (Table 3) — i.e., LLMs hallucinate more for the same firms where they are most accurate — is genuinely thought-provoking and, if validated with proper decomposition, could reveal important properties of LLM confidence calibration.

- **Generalizable framework**: The application of the same temporal/cross-sectional analysis to La Liga soccer statistics (Section 5) demonstrates the methodology can transfer beyond finance.

## Weaknesses

### Fatal
None.

### Major

- **Cross-sectional regressions are run separately per variable, not jointly, so the "independent effect" claims are unsupported.** Table 2 reports coefficients from separate logistic regressions (each with year fixed effects), not a single joint regression. Because firm-level variables are mechanically correlated (large market cap correlates with high retail interest, high institutional attention, more SEC accesses, etc.), the coefficients for retail investment, B-AIA, SEC access, and Bog Index may simply reflect the underlying effect of market cap. The paper's language — "LLMs demonstrate better accuracy for companies with larger market capitalizations, higher attention... higher SEC filing accesses, and better filing readability" — implies each factor has an independent relationship, but the evidence as presented only establishes bivariate associations. A joint regression including all variables simultaneously is the minimum needed to disentangle these effects. If the coefficients largely disappear when market cap is controlled, the paper's cross-sectional contribution reduces to "market cap matters."

- **The hallucination result is confounded with the model's decision to answer, and is not properly decomposed.** The paper defines hallucination rate (Eq. 2) as the fraction of *all* queries (including Y=0: no numerical answer) where the absolute % error ≥ 10%. Success rate is defined analogously. If the model's refusal rate (Y=0) is higher for small/obscure companies — which the paper itself suggests in its "overconfidence" hypothesis — then both the success rate and hallucination rate mechanically increase for large companies simply because the denominator now includes fewer Y=0 cases. The paper does not report hallucination rate *conditional on having given a numerical answer* (i.e., the error rate among answers), nor does it show how answer probability (Y>0 vs. Y=0) varies with market cap. Without this decomposition, the headline that "LLMs hallucinate more for larger companies" may be misleading: the conditional error rate could be lower for large companies while the higher attempt rate drives the unconditional result. This is a methodological gap because the paper's central paradoxical finding hinges on an unanalyzed compositional effect. (Figure 5 partially addresses the company-level correlation but uses raw counts, not rates, and does not control for year coverage.)

### Minor

- **The 2019–2020 performance dip is noted but not discussed in context.** Figure 4 shows a clear dip in all models' performance in 2019–2020. The paper calls this "unexplained" and a "compelling avenue for further research," yet does not mention the COVID-19 pandemic — which began in early 2020 and could have affected both the revenue data (anomalous earnings) and the training data. Even a brief acknowledgment of this obvious confound would strengthen the temporal analysis.

- **Sample sizes and time spans vary across cross-sectional regressions but are not reported in Table 2.** Robinhood data covers only 2018–2020, SEC Log data covers 2003–2017, Bog Index covers 1994–2021, and Bloomberg AIA covers an unspecified period. The number of observations per regression differs substantially, making direct comparison of coefficients across columns difficult. The paper should report N per regression.

- **No comparison against simple baselines.** The paper's absolute accuracy numbers (e.g., 52% success for 2018) are presented without context. Reporting a simple baseline — such as predicting the median revenue for the industry-year, or using a lagged revenue value — would help readers interpret whether the LLMs' performance is meaningful or merely reflects the difficulty of the task.

- **The advice in the Discussion (Section 5) is generic and not tightly coupled to the findings.** Suggestions like "be mindful of pre-training data" and "use debiasing techniques" are universally applicable and do not follow specifically from the paper's temporal or cross-sectional results. The paper would benefit from more concrete recommendations (e.g., using retrieval augmentation for smaller/older companies).

### Trivial
None.

## Nice-to-Haves

- Error distribution analysis for the hallucination finding: are hallucinations for large companies near-misses (close to 10% error) or wild errors? A finer-grained analysis would strengthen the "overconfidence" interpretation.
- A multi-panel figure showing answer rate, success rate given answer, and hallucination rate given answer across market cap quantiles would directly address the decomposition issue.
- Including RAG as a comparison would be a natural extension but is beyond the paper's stated scope.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that "democratizing" framing is not operationalized (Harsh Critic Point 3):** The paper tests a specific claim from Yue et al. (2023) by asking whether LLMs have unbiased financial knowledge. Finding systematic biases is a legitimate way to interrogate the democratization thesis. The framing serves as motivation, not a formal research question that needs operationalization. Removing as a strawman that misreads the paper's purpose.
- **Criticism that the "first study" novelty claim is too strong due to Onoe et al. (2022) and Kasai et al. (2024) (Harsh Critic section notes):** The paper explicitly distinguishes itself from these works — they study "knowledge produced after the cut-off dates" (post-cutoff), while this paper studies *retrograde* bias (knowledge of the past). The paper's claim about being "first to analyze retrograde knowledge bias" is consistent with its own framing of prior work. The reviewer conflates two distinct temporal directions.
- **Criticism that the paper should compare to RAG / retrieval augmentation (Harsh Critic "Obvious Next Steps"):** The paper scopes itself as an evaluation of raw LLM knowledge — adding RAG is a future direction, not a missing experiment. Removing as scope creep.
- **Criticism about missing analysis of refusal behavior across firm types (Harsh Critic "Obvious Next Steps"):** This is a reasonable extension but beyond the paper's current experiments. Removing as scope creep.
- **Strengths from Strength Finder that are generic/drop due to verified weaknesses:** The strength "Commitment to reproducibility" is generic and not specific to this paper's contribution; dropped. The strength "Demonstrated framework transferability" is specific (La Liga example) and kept.

## Novel Insights

The most valuable observation emerging from the reviews — beyond the paper's own contributions — is that the co-occurrence of high accuracy and high hallucination for the same entities is likely driven by the model's decision boundary for attempting an answer. If the model's refusal policy (Y=0) is calibrated to some internal confidence threshold, then for entities where it has more training data (large-cap, recent years), it attempts to answer more often, mechanically raising both success and hallucination rates under the paper's current definitions. The paper's "overconfidence" interpretation presumes this is a *calibration* phenomenon, but it could equally be a *coverage* phenomenon. Distinguishing these requires conditioning hallucination on answer attempt — a straightforward analysis the paper does not perform, but one that could sharpen the paper's core insight considerably.

## Suggestions

1. **Run a joint logistic regression** including all cross-sectional variables (log market cap, retail attention, institutional attention, SEC access, Bog Index) simultaneously with year fixed effects. Report whether the coefficients for the non-MCap variables remain significant. This is essential for substantiating the claimed independent effects.

2. **Decompose the hallucination analysis.** Report (a) the probability of receiving any numerical answer (Y>0 vs. Y=0) as a function of market cap and year, and (b) the hallucination rate *conditional on having answered* (i.e., P(Y=1 | Y>0)). This will resolve whether the positive hallucination–market cap relationship is driven by lower refusal rates for large companies or by genuinely higher conditional error rates.

3. **Report sample sizes (N)** for each column in Table 2, since the cross-sectional variables cover different time spans.

4. **Acknowledge COVID-19 as a potential confound** for the 2019–2020 performance dip, at minimum noting that pandemic-era revenue anomalies could affect both the ground truth and the training data.

5. **Add simple baselines** (e.g., median industry-year revenue) to calibrate the meaning of the absolute accuracy numbers.

---

## Score and Decision

The paper addresses an important and timely question with a large-scale, carefully constructed dataset and multiple LLMs. Its core temporal finding is solid and well-supported. However, two methodological gaps — the separate (not joint) cross-sectional regressions and the conflated hallucination metric — mean that two of the paper's headline claims are not supported by the evidence as currently presented. These issues are fixable with additional analysis, and the underlying research question and data are valuable. In its current form, the paper cannot be accepted, but it could become a strong contribution after revision.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>