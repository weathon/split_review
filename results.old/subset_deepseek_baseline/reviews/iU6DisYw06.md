## Summary

This paper proposes a behavioral framework to evaluate whether the self-explanations (highlighted tokens) produced by LLMs for sentiment classification are **functionally consistent** with the models’ own predictive behavior. Instead of assessing textual plausibility, the authors define and measure three metrics—sufficiency, comprehensiveness, and counterfactuality—on scalar review scores (1–10). Experiments on IMDB and Steam reviews with five LLMs (GPT-4o-mini, Gemma3, Granite8B, DeepSeek-R1 1.5B/14B) reveal that GPT-4o-mini, Gemma3, and Granite8B exhibit a coherent progression across interventions, while DeepSeek models display distinct failure modes (contradiction in the 1.5B variant and over-reliance in the 14B variant). The work highlights that explanation faithfulness cannot be assumed from scale or openness alone.

## Strengths

- **Principled operationalization of explanation faithfulness**: The paper moves beyond textual plausibility to test whether claimed important tokens actually drive the model’s predictions, using well-defined interventions (remove, isolate, invert). This avoids circularity from probability-based measures and does not require internal model access.
- **Clear and comprehensive experimental design**: Multiple models across different families, scales, and openness (proprietary vs. open-source) are tested on two sentiment datasets with stratified sampling. The metrics are carefully defined, and the aggregation (π_alt, π_red, ΔR, σ_ΔR) provides a complete picture.
- **Revealing and non-obvious empirical findings**: The study uncovers qualitatively distinct failure patterns: DeepSeek-1.5B shows contradictions (tokens are neither sufficient nor stable), while DeepSeek-14B exhibits over-sensitivity (predictions collapse under perturbation). These insights go beyond a simple “explanations are unfaithful” result.
- **Reproducibility and transparency**: The code, exact prompts, and data sources are provided, ensuring that experiments can be replicated and extended.
- **Clear writing and logical flow**: The paper is well-structured, with each concept motivated and defined before results are presented.

## Weaknesses

### Fatal
None. The core claims are well-supported by the methodology and results.

### Major
1. **Limited task and domain generalizability**: Only sentiment analysis on two review datasets is evaluated. It is unclear whether the findings hold for other tasks (e.g., NLI, question answering) or for more complex textual genres. The paper acknowledges this limitation but does not provide any evidence of cross-task transfer.
2. **Crude counterfactual construction**: Replacing highlighted tokens with WordNet antonyms or prepending “not” is a coarse proxy for semantic inversion. Many replacements may be unnatural or fail to truly flip polarity (e.g., “not boring” vs. “exciting”). This can add noise to the counterfactuality metric and weaken the conclusions about DeepSeek models.
3. **Lack of baseline or sanity checks**: The paper only tests the model’s own highlighted tokens. Without comparing to random token removal/retention or to an alternative explanation method (e.g., attention weights, leave-one-out), it is difficult to assess whether the observed functional consistency is unique to the self-explanations or merely a property of any salient phrase.
4. **Reliance on scalar score variability without calibration analysis**: The review score (1–10) is taken as a reliable measure of model sentiment intensity. The paper does not investigate the score’s consistency across repeated runs or its linearity (e.g., is a 2-point shift always meaningful?). Noise in the score could inflate some metrics, especially for smaller models.
5. **Potential for extraction artifacts**: The method extracts highlighted tokens from the model’s free-text response. It is not fully validated whether these tokens are always verbatim substrings of the original input (as claimed) or whether the model sometimes outputs paraphrased or absent tokens, which could break the intervention logic.

### Minor
1. The term **auto-consistency** is introduced but could be confused with “self-consistency” in chain-of-thought literature. The paper defines it clearly, but a different term (e.g., “functional consistency”) might be more distinctive.
2. The description of the directional transformation (Section 4) is slightly dense; a clearer table or formula could aid readability.
3. The figures (Figure 1 and 2) are low-quality (appear as OCR placeholder diagrams) and add little value in their current form.

### Trivial
None.

## Nice-to-Haves

- Include a baseline where randomly selected tokens (same length as highlighted set) are used in the interventions. This would help quantify whether the observed effects are specific to the claimed explanatory tokens.
- Perform a small human evaluation of the counterfactual edits to ensure they are indeed semantic opposites as intended.
- Analyze the stability of the highlighted token set across multiple trials with the same input to assess the consistency of the explanation generation.

## Novel Insights

The paper’s main novel insight is that **different LLMs exhibit structurally different patterns of (dis)agreement between their stated explanations and their behavior**, which cannot be reduced to a single axis of “faithfulness.” Specifically, the smaller DeepSeek model fails because highlighted tokens are neither sufficient nor stable (a logical contradiction), while the larger DeepSeek model fails because predictions are disproportionately brittle to perturbations of those tokens. This suggests that understanding explanation reliability requires evaluating multiple behavioral dimensions rather than a single metric, and that neither model scale nor openness guarantees functional consistency.

## Suggestions

- Extend the evaluation to at least one non-sentiment task (e.g., toxicity detection, news classification) to assess generalizability.
- Conduct a robustness check by randomly perturbing the highlighted token set (e.g., swap one highlighted token with a random word) to verify that the metrics are not simply capturing random variation.
- Report confidence intervals or bootstrapped statistics for all aggregate metrics (ΔR, π_alt, etc.) to quantify uncertainty.

## Score and Decision

Score: 8 - Accept.

The paper addresses an important and timely problem (faithfulness of LLM self-explanations) with a rigorous, principled, and well-executed empirical methodology. The results reveal nuanced failure modes that advance our understanding beyond prior work. While the study has limitations in generalizability and certain operational choices, the core contribution—a functional consistency framework plus comparative findings across models—is strong and clearly valuable to the ICLR community.

MY FINAL SCORE: <score>8</score>
MY FINAL DECISION: <decision>Accept</decision>