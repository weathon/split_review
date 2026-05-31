## Human Reviewer 1

### Summary
This paper proposes a morphing framework that adaptively reshapes exogenous time series before forecasting. Specifically, for each channel and time step, a morphing function computes a ratio from the local relationship between the exogenous input and the target series and amplifies useful intervals accordingly. Results show that morphing is a simple yet effective way to enhance the utility of exogenous information.

### Strengths
- The paper is well-structured and easy to follow.

- The proposed morphing approach builds on a preceding statistical analysis to identify the temporal influence of the exogenous series on the target variable, which is simple yet effective.

### Weaknesses
- The overall novelty is limited. A key component of the morphing framework is temporal saliency detection, yet there is no additional design or novel contribution specifically addressing this module.

- The experimental implementation details are missing. The authors select five transformer-based models, which exhibit substantial architectural diversity; in particular, Autoformer maps the channel dimension directly to the hidden dimension. Consequently, it remains unclear how the proposed morphing framework is adapted or applied to each architecture. A detailed explanation of how the framework is instantiated for each model is required.

- The experimental results in Table 2 are unclear. It lacks explanations of why experiments conducted on the same datasets, with the same models and saliency detection settings, yield different results. In addition, terms such as ipfarm and pentropy require clarification.

### Questions
- There is a significant performance decline for the Autoformer architecture on the Weather dataset. Could the authors provide a more in-depth analysis of this issue?

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes **Shape Morphing**, a model-agnostic preprocessing framework to solve the temporal saliency problem in time series forecasting.

The method computes a rolling statistical relationship (like correlation or mutual information) between the exogenous input and the target series, creating a dynamic morph ratio. This ratio is then used to gate the original input, amplifying its signal when it is relevant and attenuating it when it is not.

### Strengths
1. While many works have tried to incorporate exogenous variables by designing complex, model-specific attention mechanisms, this paper reframes the problem. It proposes Shape Morphing, a model-agnostic preprocessing framework. This model-external design is an original contribution that makes the solution highly generalizable. It can be applied to any forecasting model (new or existing) that accepts exogenous inputs, significantly broadening its potential impact and making it easy for practitioners to adopt.

2. This paper conducts a large ablation test across seven diverse datasets and five different state-of-the-art Transformer architectures (Autoformer, Crossformer, etc.). This rigorous validation demonstrates that the improvements are not an isolated phenomenon but are achievable across various model and data types, lending strong credibility to the method's effectiveness.

### Weaknesses
**1. Clarity and Paper Structure: The paper's overall clarity is a primary concern.**

- Unbalanced Focus: The writing in sections like Related Work (Section 2), as well as the experimental setup and conclusion, is overly verbose. These sections are excessively detailed, diminishing the focus on the paper's algorithm, which, by contrast, is not explained sufficiently.

- Core Algorithm in Appendix: The detailed algorithm of the Shape Morphing is explained in the appendix. This forces the reader to constantly switch between the main text and the appendix to build a complete understanding of the proposed method, which hinders readability.

- Lack of Intuitive Figures: This clarity issue is compounded by a lack of helpful visualizations. While Figure 2 provides a high-level overview, it fails to clearly illustrate how morphing impacts the final prediction. The paper would be significantly improved by a dedicated diagram illustrating the core algorithmic steps.

**2. Questions on Performance Significance: The empirical results raise questions about the method's true necessity and utility for modern architectures.**

- Inconsistent Gains: The paper highlights the large performance boost on Crossformer, but this result does not sufficiently represent the algorithm's universal utility. For other SOTA models that already perform well (e.g., PatchTST, TimeXer), the performance gains are minor and, in some cases, performance even degrades.

- Necessity for Modern Architectures: This inconsistency leaves a critical question unanswered: Is the Shape Morphing algorithm a truly necessary component for modern, robust SOTA architectures, or is its primary benefit in addressing the limitations of specific models?

### Questions
Please refer to weaknesses above

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
The paper investigates the problem of forecasting with exogenous variables, where multiple auxiliary time series are used to predict a single target variable. The authors highlight the phenomenon of temporal saliency of exogenous variables, referring to the varying relevance of external inputs over time. To better exploit this property, the paper proposes a morphing framework that adaptively reshapes exogenous time series before forecasting. For each channel and time step, a morphing function computes a ratio from the local relationship between the exogenous input and the target series, amplifying informative intervals accordingly. Experiments conducted on multiple long-horizon forecasting benchmarks show that morphing can yield notable improvements for certain model–dataset combinations, suggesting that this approach effectively enhances the utility of exogenous information.

### Strengths
1.The proposed framework refines how exogenous signals contribute to target prediction, introducing time-dependent adaptive processing that adds interpretability and practical value.
2.The approach is conceptually simple, easy to integrate with existing time series method, and potentially useful in real-world multivariate forecasting scenarios.

### Weaknesses
1.The experimental evaluation is relatively limited, covering only five deep learning models in the main results. Moreover, while the paper focuses primarily on a data-processing perspective, it lacks broader comparisons with classical statistical, machine learning, and time-series pretraining frameworks. Expanding the experiments to include these baselines would provide a more convincing assessment of the proposed framework’s generality, effectiveness, and position within the broader landscape of time-series research.

2.The selection of datasets is rather narrow. Including additional benchmarks such as EPF, which is widely used in studies involving exogenous variables, would significantly enhance the credibility and comprehensiveness of the results.

3.The improvements reported in Table 1 are not consistent across all experimental settings. In particular, models like TimeXer and PatchTST exhibit little or no gain, which raises concerns about the robustness and reliability of the proposed morphing mechanism.

4.The paper suffers from several presentation and structural issues. The Related Work section is missing, and parts of the literature review are scattered within the Method section, which obscures the connection between the proposed approach and prior studies. The overall organization of the paper is unclear, with weak transitions between sections. Moreover, the dataset descriptions in the Experiment section could be moved to the Appendix for better readability, and the Conclusion section is overly lengthy and repetitive, diluting the main findings. A clearer structure and more concise presentation would substantially improve the paper’s readability and impact.

### Questions
Since the morphing operation locally rescales the exogenous series in the numerical domain, could this distort the original temporal patterns of exogenous variables and negatively impact the tokenization or representation learning of these covariates?

### Soundness
1

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper proposes a simple preprocessing framework that rescales each exogenous channel over time using a morph ratio derived from rolling, lag-aware statistics (e.g., correlation, covariance, entropy, mutual information) computed between that channel and the target series. The goal is to emphasize intervals where the exogenous signal is predictive (“temporal saliency”) and attenuate it elsewhere, before feeding inputs to forecasting models. The approach targets the observation that channel-dependent Transformers often fail to capitalize on exogenous features. The paper reports broad ablations on 7 long-horizon benchmarks and 5 Transformer families.

### Strengths
- The motivation is significant, where exogenous variables are typically informative only in specific intervals and irrelevant elsewhere. 
- The idea is simple and model-agonistic.
- Temporal saliency detection is an interesting experiment to me.

### Weaknesses
- In the empirical analysis, it seems the method only brings a substantial gain on Crossformer, but just marginal on more recent models, such as PatchTST, TimeXr, and iTransformer. 
- Many baselines use “original hyperparameters” (no tuning), while morphing gets extensive tuning. This risks an uneven playing field.
- Statements that Transformers are “permutation-invariant” and “cannot learn channel dependency” are somewhat over-broad; many architectures inject positional encodings and learn cross-channel structure.
- For ECL and Traffic, results are incomplete due to “exhausted computational power,” weakening the generality of claims precisely on the hardest multivariate settings (hundreds of exogenous channels).

### Questions
- Can you report the average gain for different models?
- Were the experiments run many times for a fair comparison?
- Was morph function + window size selected on validation only?

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
4