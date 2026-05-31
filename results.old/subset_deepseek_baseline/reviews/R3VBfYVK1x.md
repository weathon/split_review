## Summary

This paper evaluates a large set of state-of-the-art LLMs (GPT-4o series, o3, o3-pro, Claude 3.5/3.6 Sonnet, DeepSeek V3/R1, Qwen3 variants) on 464 binary forecasting questions from Metaculus. Using a news retrieval pipeline (AskNews) to supply relevant context, the author compares model Brier scores against both the Metaculus human crowd (via prior work) and expert forecasters hired by Metaculus. The main reported finding is that o3 achieves Brier 0.1352, surpassing the crowd baseline from Halawi et al. (2024) of 0.149, but still far behind expert forecasters who achieve median Brier 0.0225 on a subset of questions. A narrative-prompting experiment yields worse performance than direct prompting.

## Strengths

- **Large-scale evaluation of many recent frontier models** – the paper tests 12 models including reasoning models (o3, o3-pro, o4-mini, DeepSeek R1) and open-weight models (Qwen3), providing a comprehensive snapshot of current LLM forecasting capability.
- **Careful data collection methodology** – the hold-out set (130 questions with news collected on the question open date) mitigates data leakage concerns. Using AskNews with date-filtered back-testing is a reasonable approach.
- **Detailed reporting of results by category and with calibration plots** – category-level breakdowns (politics, economics, healthcare, etc.) and calibration curves add useful nuance beyond aggregate Brier scores.

## Weaknesses

### Fatal

- **Selection bias in the expert forecaster comparison invalidates the central claim.** The expert forecasters predicted on only 47% of the main dataset (157/334 questions) and 31% of the hold-out set (41/130 questions). Experts almost certainly chose questions they were more confident about or had relevant knowledge for. The paper compares the experts’ Brier score (median 0.0225) on this cherry-picked subset to the models’ Brier scores on the *full* 334-question dataset. Without a matched comparison on exactly the same questions that the experts answered, it is impossible to conclude that models “still significantly underperform a group of experts.” The gap may largely reflect question difficulty selection rather than inherent forecasting ability.

### Major

- **Invalid cross-dataset Brier comparisons.** The abstract and conclusion state that o3 “surpasses the human crowd” by comparing its 0.1352 Brier to the 0.149 “crowd” score from Halawi et al. (2024) and the 0.121 from Karger et al. (2025). These scores come from *different question sets* with potentially different difficulty distributions. Brier scores are not comparable across datasets (the paper itself acknowledges this in Section 5.1 but then proceeds to make the comparison anyway). The paper should report the actual Metaculus community crowd Brier scores for its own questions, which would allow a proper within-dataset comparison.
- **No matched comparison between models and experts on the overlapping question subset.** The experts predicted on 157 questions. The paper could compute model Brier scores restricted to those 157 questions and compare directly. The fact that this is not done strongly suggests the gap would shrink or reverse, undermining the paper’s main conclusion.

### Minor

- **The narrative prompt experiment is overinterpreted.** The paper claims that “fictional jailbreaks could decrease the accuracy of models,” but the narrative prompt is a specific script-writing scenario (Nate Silver and Philip Tetlock discussing the forecast), not a typical jailbreak. The result is interesting but does not support generalizations about all fictional-framing jailbreaks.
- **Some category sample sizes are very small** (e.g., arts & recreation: 16 questions, sports: 32 questions). The paper appropriately caveats this, but the category-level tables (Tables 4, 10) still invite overinterpretation.

### Trivial

- Table 2 contains a duplicate row (“GPT-4.1-2025-04-14” appears twice). The figure caption for Figure 1 is repeated.

## Nice-to-Haves

- **Provide Brier scores for the Metaculus community crowd on the same question set** – this would make the “outperforming the crowd” claim properly supported.
- **Report model Brier scores on only the questions that experts answered**, so the expert vs. model comparison is fair.
- **Discuss selection bias explicitly** – if the author cannot obtain expert predictions on the full set, the limitation should be clearly stated and the comparison qualified.

## Novel Insights

None beyond the paper’s own contributions. The observation that models perform better on political than on economic forecasting is consistent across models and potentially interesting, but the paper does not deeply investigate why.

## Suggestions

1.  Provide a matched comparison: compute model Brier scores on the 157 questions (and 41 hold-out questions) that expert forecasters actually predicted on. Report both the full-set and matched-set model scores.
2.  Report the Metaculus community crowd Brier score for the same 464 questions (or at least the main 334) to enable a proper within-dataset crowd comparison.
3.  Revise claims about outperforming the crowd and falling short of experts to reflect the actual evidence: relative to the same question sets.
4.  Clarify that the narrative-prompt finding is specific to the script format used and should not be extrapolated to all fictional-framing prompts.

## Score and Decision

The paper evaluates a large number of recent models with a reasonable experimental setup, but the central comparisons are fatally undermined by selection bias (expert subset comparison) and invalid cross-dataset Brier comparisons (crowd baseline). Without addressing these issues, the paper’s main conclusions are not supported by the evidence presented.

MY FINAL SCORE: 3.0</score>
MY FINAL DECISION: Reject</decision>