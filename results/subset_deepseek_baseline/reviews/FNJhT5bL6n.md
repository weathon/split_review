## Summary
This paper proposes a "morphing" framework for time series forecasting that preprocesses exogenous variables by adaptively reshaping them based on their temporally-varying relevance to the target variable. The approach computes a morphing ratio from statistical measures (correlation, mutual information, covariance, entropy, FARM) between each exogenous channel and the target within a sliding window, then multiplies the exogenous series by this ratio before feeding it to transformer-based forecasting models. The authors evaluate their approach across 7 datasets, 5 transformer models, and 5 saliency detection methods, reporting improvements in approximately 73% of experimental configurations, with particularly strong gains for Crossformer, Autoformer, and iTransformer models.

## Strengths
- **Addresses a well-motivated and practically important problem**: The observation that exogenous variables are only informative in specific intervals (temporal saliency) is intuitive and relevant. The paper correctly identifies that current transformer models struggle to leverage exogenous information effectively, and the proposed decoupling of saliency detection from modeling is a sensible approach.
- **Comprehensive ablation study**: The experimental design is extensive, covering 7 datasets, 5 transformer architectures, 5 saliency detection methods, multiple window sizes, and 4 forecast horizons. This provides a thorough characterization of when and how the morphing approach works.
- **Clear empirical evidence of benefit**: The results show that morphing can yield substantial improvements in specific configurations (e.g., Crossformer improvements of +31.9% on average, up to +76.6% on individual settings), and the paper honestly reports cases where morphing hurts performance, which strengthens credibility.

## Weaknesses
### Fatal
None.

### Major
- **Lack of comparison to strong baselines**: The paper evaluates morphing against a "no exogenous information" baseline, but does not compare against standard approaches for incorporating exogenous variables (e.g., simply concatenating raw exogenous series, using lagged exogenous features, or other preprocessing methods). The key question is whether morphing outperforms simpler alternatives like feeding raw exogenous data or using standard feature engineering. Without this comparison, it's unclear whether the benefit comes from the morphing specifically or just from including exogenous information in any form.
- **No statistical significance testing reported in the main paper**: While the appendix mentions significance tests, the main results (Table 1) present only point estimates without confidence intervals or statistical tests. Given the variability across window sizes and saliency methods, it's unclear which improvements are statistically reliable. The paper claims "73% of experiments show improvement" but doesn't quantify how many of these improvements are meaningful versus noise.
- **The morphing approach introduces additional hyperparameters without clear guidance**: The method requires choosing both a saliency detection function and a window size, and the results show these choices significantly impact performance (e.g., morphing can hurt in some configurations). The paper provides no practical guidance on how to select these hyperparameters in a real deployment scenario, limiting the method's usability.

### Minor
- **The synthetic toy example (Figure 2) is helpful but limited**: It only demonstrates morphing with a simple Ridge regression forecaster, not with the transformer models that are the paper's focus. A similar demonstration with a transformer would strengthen the motivation.
- **The paper's claim about "decoupling saliency detection from modeling" is overstated**: While morphing does move saliency detection to a preprocessing step, the optimal choice of saliency method and window size still depends on the downstream model and dataset, as evidenced by the results. True decoupling would require the preprocessing to be model-agnostic.
- **Missing analysis of computational overhead**: The paper doesn't discuss the computational cost of computing morphing ratios for each exogenous variable at each time step, which could be significant for datasets with many exogenous variables (e.g., ECL with 320 variables).

### Trivial
- The paper uses "morphing" and "shape morphing" somewhat interchangeably, which could be confusing.
- Table 1 would benefit from clearer formatting (e.g., highlighting the best results per row).

## Nice-to-Haves
- A comparison against a simple baseline that uses raw (unmorphed) exogenous variables would be the most informative addition.
- An analysis of how the optimal morphing configuration varies with dataset characteristics (e.g., number of exogenous variables, signal-to-noise ratio) would provide practical guidance.
- A discussion of how morphing interacts with the iterative forecasting procedure (using previous forecasts as input) would be valuable.

## Novel Insights
The paper's key insight is that the temporal saliency of exogenous variables can be effectively captured by simple statistical measures computed in a sliding window, and that applying these saliency weights as multiplicative factors to the exogenous series before feeding them to transformer models can improve forecasting performance. This is a practical observation that challenges the assumption that complex attention mechanisms within transformers are necessary to identify relevant exogenous information. The finding that simple statistical preprocessing can sometimes outperform learned attention for this specific task is noteworthy, though the paper would benefit from more rigorous comparison to validate this claim.

## Suggestions
- Add a baseline that feeds raw (unmorphed) exogenous variables to the same transformer models, so readers can directly assess the value added by morphing versus simply including exogenous data.
- Report confidence intervals or perform statistical tests (e.g., paired t-tests) for the main results in Table 1 to distinguish meaningful improvements from noise.
- Provide practical guidance on selecting the saliency detection method and window size, perhaps through a simple heuristic or a small validation set procedure.

## Score and Decision
The paper addresses a relevant problem with a sensible approach and provides extensive experimental evaluation. However, the lack of comparison to the most natural baseline (raw exogenous variables) is a significant gap that prevents a clear assessment of the method's contribution. The results are promising but not yet conclusive.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>