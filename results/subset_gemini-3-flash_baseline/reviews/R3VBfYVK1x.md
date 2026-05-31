## Summary
This paper evaluates the forecasting capabilities of state-of-the-art Large Language Models (LLMs), including reasoning models like OpenAI’s o3 and DeepSeek-R1, on a dataset of 464 real-world binary questions from Metaculus. The author compares LLM performance against both a human crowd baseline and a group of expert forecasters, finding that while the best models (o3) now surpass the general human crowd, they still significantly underperform human experts. Additionally, the study explores the impact of "narrative prompting" (fictional framing) on accuracy, finding it generally degrades performance.

## Strengths
- **Timeliness and Relevance:** The paper evaluates very recent models (o3, GPT-4.1, DeepSeek-V3/R1) that were released only weeks or months prior to the study. This provides the community with an up-to-date snapshot of the "frontier" in LLM reasoning and forecasting.
- **Methodological Rigor regarding Leakage:** The use of a "hold-out set" where news articles were collected in real-time as questions opened is a strong defense against data contamination. The finding that performance is consistent between the main set and the hold-out set strengthens the claim that models are generalizing rather than memorizing.
- **Novel Prompting Analysis:** The comparison between direct prediction and narrative (script-writing) prediction provides empirical evidence that "jailbreak-style" framing, while useful for bypassing safety filters, may come at a significant cost to the model's analytical accuracy.
- **Expert Baseline:** Comparing models not just to a general crowd but to paid expert forecasters provides a clear "ceiling" for current AI capabilities, highlighting a substantial remaining gap (Brier score 0.135 vs 0.023).

## Weaknesses
### Major
- **Ambiguity in Expert Baseline Comparison:** In Section 5.4, the paper reports a median Brier score of 0.0225 for expert forecasters. This is an exceptionally low (good) score for real-world forecasting. However, the paper does not clarify if this score is calculated for the *aggregate* expert crowd or the *average individual* expert. If the LLM (an individual agent) is being compared to a "crowd of experts" (an ensemble), the comparison is biased in favor of the humans. Furthermore, the expert baseline is calculated on a subset (157 questions) rather than the full 464.
- **Statistical Significance:** While the paper provides standard errors for Brier scores, it lacks formal hypothesis testing (e.g., p-values or confidence intervals) to confirm if the differences between top models (e.g., o3 vs. o3-pro) or between models and the crowd are statistically significant, especially given the noise inherent in Brier scores.

### Minor
- **Extrapolation Logic:** Figure 1 attempts to extrapolate LLM performance to reach expert levels by 2027. This is highly speculative and assumes linear progress in a domain where gains may be logarithmic or hit a data-quality ceiling.
- **Category Imbalance:** As noted by the author, some categories (Arts & Rec) have very few questions (n=16), making the category-specific Brier scores in Table 4 highly volatile and potentially misleading.

## Nice-to-Haves
- A breakdown of "calibration by model family" would be interesting—do reasoning models (o-series, R1) show better calibration than standard chat models?
- Analysis of the "reasoning traces" (CoT) from o3/R1 to see if they identify the same "moving factors" as human experts.

## Novel Insights
The most significant insight is the "narrative penalty": the observation that framing a request as fiction (a common technique for jailbreaking or eliciting "latent knowledge") consistently degrades forecasting accuracy across almost all frontier models. This suggests that the "persona" adopted by the model significantly influences its access to or application of probabilistic reasoning. Additionally, the paper provides the first public benchmark of OpenAI's o3 and DeepSeek-R1 on the specific task of competitive forecasting, demonstrating that "reasoning" models provide a measurable but not yet "expert-level" leap in predictive performance.

## Suggestions
- Clarify the expert baseline: Is the 0.0225 score the result of a "Metaculus Prediction" (weighted ensemble) or an average of individual expert scores?
- Include a "Random" baseline (0.25) and a "No-Change/Always 50%" baseline in all tables for easier context.
- Perform a bootstrap analysis to provide 95% confidence intervals for the Brier scores to see if the gap between o3 and GPT-4.1 is statistically robust.

## Score and Decision
The paper is a solid empirical study that addresses a high-interest topic (LLM forecasting) with a rigorous approach to data leakage. While the expert comparison could be more granular, the inclusion of the latest reasoning models makes this a valuable contribution to the ICLR community.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>