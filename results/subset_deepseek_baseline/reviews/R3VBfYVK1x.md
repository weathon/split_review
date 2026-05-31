## Summary
This paper evaluates state-of-the-art LLMs on 464 forecasting questions from Metaculus, comparing their performance against expert human forecasters. The author finds that frontier models like o3 achieve Brier scores (0.1352) that surpass the human crowd baseline but still significantly underperform expert forecasters (0.0225). The paper also tests narrative prompting and finds it degrades performance, and provides category-level analysis showing models perform better on political than economic forecasting.

## Strengths
- **Timely and relevant research question**: Evaluating whether LLMs can forecast real-world events is a genuinely important question for the community, and the paper addresses a clear gap in understanding how frontier models (2024-2025) perform compared to earlier work.
- **Clean experimental design**: The hold-out dataset (130 questions) where news was collected on the question open date provides a strong safeguard against data leakage, and the use of AskNews with date filtering is appropriate.
- **Comprehensive model coverage**: Testing 12 models including GPT-4o, o3, o3-pro, Claude 3.5/3.6 Sonnet, DeepSeek V3/R1, and Qwen3 variants provides a useful snapshot of the current landscape.

## Weaknesses

### Fatal
None.

### Major
- **Expert forecaster comparison is fundamentally flawed**: The expert forecasters predicted on only 47% of questions (157 out of 334) in the main dataset and 31% (41 out of 130) in the hold-out set. The paper reports the expert median Brier score as 0.0225, but this is computed on a different, likely easier subset of questions. The LLMs predicted on all questions. Comparing scores across different question sets is invalid, and the paper acknowledges this for cross-study comparisons but then makes exactly this error for the expert comparison. The claim that "expert forecasters still significantly outperform the bots" is not supported by the evidence presented.

- **No statistical significance testing**: The paper reports Brier scores and standard errors but provides no statistical tests comparing models to each other or to baselines. Given the noise in forecasting evaluation (as the paper itself notes with the Nikos 2023 reference), confidence intervals and significance tests are essential. The claim that o3 "outperforms the crowd baseline" cannot be evaluated without knowing whether the difference is statistically significant.

- **Missing critical methodological details**: The paper does not specify the temperature setting used for non-reasoning models, only noting "default temperature" for the 5 predictions. The prompt templates referenced (Figures 5, 6, 7) are in the removed appendix, making the methodology impossible to reproduce. The narrative prompt design is described but the actual prompt is not provided in the main text.

- **Inconsistent and potentially misleading comparisons**: The paper compares o3's 0.1352 to Halawi et al.'s 0.149 and Karger et al.'s 0.121, but these are from different question sets with different difficulty levels. The paper acknowledges this issue but then proceeds to make the comparison anyway. The extrapolation in Figure 1 suggesting LLMs will reach "superforecaster levels" by May 2027 is not supported by the data (only ~6 data points over ~1 year) and should not be presented as a serious prediction.

### Minor
- **The narrative prompt experiment is under-motivated**: The paper claims this tests whether "fictional jailbreaks could decrease the accuracy of models," but the connection between narrative forecasting prompts and jailbreak scenarios is not well established. The experiment tests a specific prompting strategy, not a general claim about jailbreaks.
- **Category-level analysis has limited statistical power**: Several categories have very few questions (Arts & Rec: 16, Sports: 32), making the per-category Brier scores noisy and the comparisons unreliable.
- **The paper does not control for question difficulty when comparing models across categories**: Different categories may have inherently different difficulty levels, making cross-category comparisons of Brier scores potentially misleading.

### Trivial
- Table 2 lists GPT-4.1 twice with the same knowledge cutoff date.
- Table 7 has a typo: "Qwen3-2335B-A22B" instead of "Qwen3-235B-A22B".

## Nice-to-Haves
- Including calibration curves for individual models (not just the aggregate plots) would help diagnose specific model biases.
- Testing whether ensembling multiple LLM predictions (e.g., averaging across models) improves performance would be a natural extension.
- Reporting the distribution of predictions (e.g., histograms) would help understand whether models are using the full probability range.

## Novel Insights
The paper's most interesting finding is the consistent pattern across all models of better performance on political forecasting than economic forecasting, which suggests fundamental differences in how LLMs handle these domains. The degradation under narrative prompting is also noteworthy, though the mechanism is unclear. However, the core empirical contribution—that frontier models approach but do not match expert forecasters—is largely confirmatory of trends already visible in Halawi et al. (2024) and Karger et al. (2025).

## Suggestions
1. Recompute the expert forecaster comparison using only the questions that both experts and LLMs predicted on, and report the LLM scores on that subset. This is essential for a fair comparison.
2. Add statistical significance tests (e.g., paired bootstrap or permutation tests) for all model comparisons and baseline comparisons.
3. Include the full prompts in the main text or a clearly accessible appendix, and specify all hyperparameters (temperature, top-p, etc.) for reproducibility.
4. Remove or substantially qualify the extrapolation in Figure 1, as it is not supported by the data.

## Score and Decision
The paper addresses an important question and has a reasonable experimental design, but the fatal flaw in the expert forecaster comparison undermines the paper's central claim. Without a valid comparison to experts, the paper's main conclusion ("SoTA models still fall short of expert forecasters") is not supported by the evidence. The remaining contributions—benchmarking frontier models and the narrative prompt experiment—are incremental and do not compensate for this core issue.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>