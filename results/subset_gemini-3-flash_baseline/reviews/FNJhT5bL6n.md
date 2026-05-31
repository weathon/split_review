## Summary
The paper introduces a "shape morphing" framework for time series forecasting that adaptively reshapes exogenous variables based on their temporal saliency relative to a target variable. The core idea is to decouple the identification of variable interactions from the neural network's learning process by using statistical measures (e.g., correlation, mutual information) in a rolling window to compute a "morph ratio" that amplifies or attenuates exogenous signals. The authors evaluate this preprocessing step across several state-of-the-art Transformer architectures (Autoformer, iTransformer, PatchTST, etc.) and standard benchmarks, demonstrating that morphing can significantly improve forecasting accuracy, particularly for models that struggle with channel dependencies.

## Strengths
- The paper addresses a highly relevant problem in the community: the "blindness" of Transformer-based models to channel dependencies and the often-superior performance of channel-independent linear models.
- The proposed method is model-agnostic and computationally efficient, acting as a preprocessing step rather than requiring architectural changes to existing forecasting models.
- The experimental evaluation is extensive, covering seven datasets, five Transformer architectures, and five different statistical saliency measures across multiple forecast horizons.
- The motivation is well-supported by a comparison between learned attention weights (TFT) and statistical saliency (FARM), suggesting that statistical methods can effectively proxy for complex attention mechanisms.

## Weaknesses
### Fatal
None.

### Major
- **Selection Bias in Results:** In Table 1, the authors report the "best result of the performed ablation test obtained with the optimal configuration." This approach risks overstating the method's utility. Since the "optimal" saliency measure and window size vary significantly across datasets and models (as shown in Tables 2 and 3), it is unclear how a practitioner would select these hyperparameters in a real-world scenario without exhaustive grid searching.
- **Inconsistent Performance:** The paper notes that morphing is not "universally better when used blindly" and shows performance degradation in several cases (e.g., Weather dataset at longer horizons, or Autoformer on ETTh2). The lack of a clear heuristic for when morphing will be beneficial limits the practical impact of the work.
- **Baseline Comparison:** While the paper compares morphed vs. non-morphed versions of Transformers, it lacks a direct comparison against the very "simple channel-independent linear models" (like DLinear or RLinear) mentioned in the introduction as the current state-of-the-art benchmarks. Showing that morphing allows Transformers to finally beat these linear baselines would significantly strengthen the claims.

### Minor
- **Methodological Detail:** Equation 2 describes a simple multiplication ($r \cdot x$). However, the toy example mentions mapping correlation to a range $[0.3, 1.7]$. The paper lacks a generalized formula for how different statistical measures (like Entropy or Mutual Information, which have different scales) are normalized or mapped into the "morph ratio" $r_t$.
- **Clarity on "Exogenous":** The paper defines the task as predicting one target variable using multiple input channels. In many of the datasets used (like ETT or Weather), all variables are technically endogenous (part of a multivariate system). The distinction between "multivariate forecasting" and "forecasting with exogenous variables" in this context is slightly blurred.

## Nice-to-Haves
- A sensitivity analysis on the "morph ratio" range. Does the choice of $[0.3, 1.7]$ vs $[0, 1]$ significantly change the results?
- Visualization of the morphed series for a real-world dataset (e.g., ECL or ETTh1) to see if the amplified regions correspond to known physical or economic events.

## Novel Insights
The most significant insight is the empirical demonstration that statistical saliency measures (FARM, MI, etc.) can serve as a "hard-coded" attention mechanism that outperforms the learned attention of Transformers in identifying temporal relevance. By shifting the burden of "channel interaction" from the model's internal weights to a statistical preprocessing step, the authors provide a path for Transformers to overcome their inherent permutation-invariance limitations in time-series tasks.

## Suggestions
- Provide a clear algorithm or heuristic for selecting the saliency measure and window size.
- Include a table comparing the best "Morphed Transformer" against DLinear/NLinear to validate the claim that this closes the gap between linear and Transformer models.
- Explicitly define the normalization/mapping function used to transform raw statistical scores (like bits for MI or coefficients for Correlation) into the multiplier $r_t$.

## Score and Decision
The paper presents a simple, intuitive, and effective preprocessing technique that addresses a known weakness in deep forecasting models. While the hyperparameter dependency is a concern, the breadth of the experiments and the potential for the method to be used as a standard "plug-and-play" enhancement for multivariate forecasting make it a valuable contribution.

MY FINAL SCORE: 6.5
MY FINAL DECISION: Accept