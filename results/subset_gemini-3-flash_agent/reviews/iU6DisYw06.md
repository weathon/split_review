## Summary
This paper introduces the concept of "auto-consistency" to evaluate the functional reliability of Large Language Model (LLM) explanations. Unlike existing work that focuses on textual plausibility, the authors propose a behavioral framework that tests if a model "trusts" its own justifications by observing how its predictions change when highlighted tokens are isolated (Sufficiency), removed (Comprehensiveness), or inverted (Counterfactuality). Through experiments on sentiment analysis datasets (IMDB and Steam), the study reveals distinct consistency profiles across model families, highlighting structural contradictions in smaller reasoning models (DeepSeek-1.5B) and over-sensitivity in larger ones (DeepSeek-14B).

## Strengths
- **Principled "Auto-Consistency" Framework:** The paper moves beyond evaluating explanations based on human-centric plausibility and instead focuses on functional faithfulness. It systematically adapts classical interpretability metrics (Sufficiency, Comprehensiveness, and Counterfactuality) to a generative setting.
- **Robust Metrics for Generative Models:** The use of scalar review scores [1, 10] effectively extracts a more granular signal than binary labels and avoids the circularity of probability-based measures in RLHF-calibrated models.
- **Identification of Distinct Model "Profiles":** The findings demonstrate that LLMs do not have uniform explanatory reliability. The paper identifies a clear distinction between models that follow a coherent progression (GPT-4o-mini, Gemma3) and those with structural deviations (DeepSeek family), providing actionable behavioral insights for users of these models.
- **Comprehensive Benchmarking:** The study evaluates multiple model families (GPT, Gemma, Granite, DeepSeek) across two different domains, ensuring the observations are robust to variations in model architecture and dataset context.

## Weaknesses

### Fatal
None.

### Major
- **Confounding Effect of Highlight Intensity/Length:** The "over-sensitivity" observed in models like DeepSeek-14B (Comprehensiveness flip rate of 45.5% on Steam) is presented as a property of its internal logic. However, the paper does not normalize these metrics against the number or proportion of tokens highlighted ($\mathcal{T}$). If one model family highlights significantly fewer (or more) tokens than another, its sufficiency and comprehensiveness scores are not directly comparable. A correlation analysis between the amount of intervention (length of $\mathcal{T}$) and the resulting variation in score ($\Delta R$) is missing, which makes it difficult to determine if a model is "brittle" or just very "sparse" in its extraction strategy.

### Minor
- **Lack of Syntax Control in Behavioral Interventions:** Removing tokens (Comprehensiveness) can result in ungrammatical or nonsensical text. While the paper assumes changes in the review score reflect a loss of *semantic* importance, they may partially reflect model "confusion" or hallucination triggered by broken syntax. A control experiment, such as removing a random set of tokens of equal length, would help isolate the functional role of the highlighted features from the noise of syntactic disruption.
- **Ambiguity in "Negative Sufficiency" (Footnote 5 and Table 1):** GPT-4o-mini shows negative $\Delta R$ values for Sufficiency (-0.28 on IMDB). This implies the model is more confident in the sentiment when *only* the "important" tokens are present than with the full context. This "dilution" effect—where peripheral context weakens a model's judgment—is a significant nuance of the auto-consistency argument that could have been explored deeper to distinguish between "clean" reasoning and "over-fitting" on selective features.
- **Domain Limitation:** While the framework is robust for sentiment analysis where a scalar [1, 10] proxy is intuitive, the discussion on how this generalizes to more complex, multi-step reasoning tasks (e.g., math or logic puzzles) where the "Review Score" proxy does not apply is limited.

### Trivial
None.

## Nice-to-Haves
- A comparison or correlation between the "sparsity" of highlights (percentage of tokens selected) and the sensitivity metrics.
- Control experiments using random token removal as a baseline for Comprehensiveness.

## Removed Points
- **Metric Inversion Concern:** The harsh critic's concern about metric inversion (Footnote 5) was removed. The paper's use of a symmetric transformation for $\Delta R$ is a standard and necessary methodological choice to ensure that positive values represent a reduction in favorability regardless of the original label.
- **Reproducibility/Logs:** Critiques regarding missing training logs or minor implementation details were removed per protocol.
- **Formatting/Typos:** Parser artifacts and minor presentation nitpicks were removed.

## Novel Insights
The most significant insight is the discovery of "structural contradiction" in reasoning-focused models like DeepSeek-1.5B. These models demonstrate a behavioral paradox: the same tokens they identify as "most relevant" are insufficient to maintain a prediction in isolation (high Sufficiency flip rates), yet the model cannot recover the prediction if they are removed (high Comprehensiveness flip rates). This implies a fragmentation between the model's extraction of importance and its actual decision boundaries, suggesting that small-scale "reasoning" models may generate plausible justifications that are functionally disconnected from their internal logic.

## Suggestions
- Include a "Sparsity" metric (avg tokens in $\mathcal{T}$ / total tokens) in Table 1 to allow for a better comparison of Sensitivity vs. Extraction Strategy.
- Perform a baseline test using random feature removal to verify the significance of the $\Delta R$ and $\pi_{alt}$ values for the selected explanatory tokens.
- Expand the discussion on the relationship between model scale and robustness to self-justification, as the 14B DeepSeek model showed significantly higher brittleness than the 4B Gemma3 model.

## Score and Decision

The paper sits in a similar bracket to papers that propose behavioral frameworks for LLM consistency (e.g., "Large Language Models Often Say One Thing and Do Another" [avg 6.25] and "Do Models Explain Themselves?" [avg 5.67]). It provides a cleaner adaptation of the ERASER benchmark to the generative setting than previous works. While the lack of a normalization for the length of highlighted tokens is a major methodological oversight that prevents a perfectly fair ranking between model families, the core concept of "auto-consistency" and the identification of distinct failure modes in reasoning models like DeepSeek are valuable and well-supported contributions.

Initial Bracket: (5.5, 7.5)
The paper is more rigorous than `kJgi5ykK3t` (5.6, "Measuring... Logical Consistency") because it uses functional interventions rather than just checking for transitivity/negation in rankings. It is comparable in quality to `RTHbao4Mib` (6.25, "Words and Deeds"), though it lacks some of the scaling/correlation-analysis depth found in the highest-scoring interpretability papers.

**Calibration Anchors:**
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/RTHbao4Mib.md (6.25): This paper uses a similar "Words and Deeds" consistency paradigm. The current paper is similarly structured but focuses specifically on feature-level interpretability metrics.
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/kJgi5ykK3t.md (5.6): The current paper is stronger because the "auto-consistency" interventions are more direct probes of model functionality than the logical property checks used here.
- /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/VvAiCXwPvD.md (5.67): This paper also uses simulatability. The current paper is slightly more comprehensive by including Sufficiency and Counterfactuality alongside Comprehensiveness.

Given the novel observations regarding the DeepSeek family and the well-motivated use of the scalar review proxy, the paper is a strong candidate for acceptance despite the minor methodological gap in highlight length normalization.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>