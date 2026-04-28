# Label Correlation Biases Direct Time Series Forecast

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
Time series modeling is uniquely challenged by the presence of autocorrelation in both historical and label sequences. Current research predominantly focuses on handling autocorrelation within the historical sequence but often neglects its presence in the label sequence. Specifically, emerging forecast models mainly conform to the direct forecast (DF) paradigm, generating multi-step forecasts under the assumption of conditional independence within the label sequence. This assumption disregards the inherent autocorrelation in the label sequence, thereby limiting the performance of DF-based models. In response to this gap, we introduce the Frequency-enhanced Direct Forecast (FreDF), which bypasses the complexity of label autocorrelation by learning to forecast in the frequency domain. Our experiments demonstrate that FreDF substantially outperforms existing state-of-the-art methods and is compatible with a variety of forecast models. Code is available at https://anonymous.4open.science/r/FreDF-0FB1.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work introduces a new loss term for multi-step time-series forecasting that penalizes errors within a decorrelated representation space of the ground truth labels. In its current formulation, this decorrelated space is defined as the frequency representation of both labels and forecasts. Experimental results demonstrate that the proposed approach significantly enhances forecasting accuracy across various datasets and base models.

### Strengths
1. The authors identify and address the bias introduced by label correlation in time-series modeling, which is a novel issue for me and holds substantial potential generality across different scenarios.
2. The method is sound, straightforward and shows very promising results. The theoretical results are relatively persuasive, demonstrating the bias caused by label correlation, and subsequently FreDF's elimination of label correlation and thereby bias.
3. The experiment is comprehensive. Extensive set of experiments showed that: the approach contributes to the state-of-the-art, different components of the loss contribute to performance, the approach is robust to hyperparameter values.

### Weaknesses
1. It seems that this work aims to penalize errors in a space that decorrelates labels. Experiments mainly achieve de-correlation via FFT or FFT2. It will be beneficial to explore the efficacy of other transformations beyond the Fourier transform?
2. While the introduction discusses various forecasting models, it could benefit from a stronger focus on established forecasting paradigms (e.g., direct forecasting, iterative forecasting). The inclusion of forecast models (iTransformer, Linear) may detract from highlighting the contribution and role of FreDF that seems to be orthogonal to forecast models.
3. The source code should be refined. The current implementation comprises numerous scripts, and it is somewhat unclear how each script relates to the experiments discussed in the manuscript. Besides, the current environment setup appears to depend on unexpected repositories like `torchmetrics` and `patool`. Including a `Dockerfile` or `conda` environment file would help a lot.

### Questions
1. In the experiments, how to determine the hyperparameters of FreDF and baselines?
2. According to the ablation study, the frequency term seems to be almost all that's needed. Is it correct?
3. During my attempt to reproduce the experiments, I encountered an error (`AttributeError: 'Exp_Short_Term_Forecast' object has no attribute 'seasonal_patterns'`) when running the short-term forecasting experiments. Is this error expected, or does it indicate a potential issue in the codebase?

Overall I think this work is interesting and promising. I will consider raising my score if my questions could receive positive responses, especially my major concerns (W1, Q1, Q3).

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Considering that in current time series prediction, DF only reuses general multi task learning methods without considering the dependency relationships  between labels. Especially, even if there is no correlation between labels, the above loss function can be used to train a multitasking model. When training the model, DF attempts to minimize the error between the predicted label sequence and the true label sequence; This assumes that the label sequence is conditionally independent between different time steps, thereby ignoring the correlation between each time step within the label sequence. So the author uses fast Fourier transform in the frequency domain to transform the data from a temporal perspective to a frequency perspective, in order to suppress autocorrelation. And the theoretical derivation of using frequency domain conversion to suppress time step correlation is given. A loss function combining time domain and frequency domain is designed, and the effectiveness of the design method is demonstrated by experimental results.

### Strengths
1. Solving the problem of autocorrelation in label sequences: The FreDF method proposed in this paper effectively bypasses the autocorrelation problem in label sequences by predicting in the frequency domain. This is a common but not fully addressed problem in existing direct prediction models.
2. Compatible with multiple prediction models: The FreDF method is not only suitable for existing state-of-the-art methods such as iTransformer, but can also be compatible with multiple prediction models. This compatibility makes it widely applicable in different prediction tasks.
3. Significant improvement in predictive performance: Experimental results show that the FreDF method is significantly superior to existing methods in multi-step prediction tasks. This indicates that the method has high accuracy and reliability in processing complex time series data.
4. Innovative applications of frequency domain analysis: By introducing frequency domain analysis into time series prediction, the FreDF method provides a new perspective to address autocorrelation issues in time series. This innovative application not only improves predictive performance, but also provides new directions for future research.

### Weaknesses
1. Complexity of frequency domain conversion: Although frequency domain analysis can bypass the autocorrelation problem in label sequences, the fast Fourier transform (FFT) required for frequency domain conversion may introduce computational overhead, especially with long time series. The paper does not provide a detailed analysis of the computational cost associated with the FFT, nor does it discuss how this cost scales with increasing sequence lengths. This is a critical consideration for practical applications involving large datasets.
2. Model generalization ability: While the FreDF method demonstrates promising results on the datasets used in the experiments, the paper lacks a thorough investigation into its generalization capabilities across diverse domains and datasets. The experiments seem to focus on a limited set of time series datasets, and it's unclear how the method would perform on data with different statistical properties or noise characteristics. The paper should include more experiments on a wider variety of datasets to validate its robustness.
3. Dependence on frequency domain features: The FreDF method relies on the assumption that the frequency domain representation of the label sequences provides a more suitable space for prediction by mitigating temporal correlations. However, the paper does not address scenarios where the frequency domain features are not well-defined or informative. For instance, if the time series data contains primarily non-periodic components, the FFT might not yield meaningful features, and the performance of FreDF could degrade. The paper should discuss the limitations of the method in such cases and provide guidelines for its applicability.

### Questions
1. Computational complexity of frequency domain conversion: Will the frequency domain conversion mentioned in the paper significantly increase computational complexity? How efficient is the FreDF method when dealing with large-scale datasets?
2. Generalization ability: How does the FreDF method generalize across different domains and datasets? Has it been tested and validated in more practical application scenarios?
3. Applicability of frequency domain features: How effective is the FreDF method for data with unclear or difficult to extract frequency domain features? Are there any relevant experimental results or analysis?
4. Model interpretability: Does the FreDF method have interpretability in the frequency domain? How do users understand and interpret these predicted results?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a new Frequency-enhanced Direct Forecast method for time series predictions that aims to improve the predictions generated by direct forecast (DF) models by training the models using a combination of standard MSE errors and errors defined in the FFT transformed space. The new approach is motivated by the fact that the MSE errors for direct forecast (DF) models are biased and do not properly account for correlations in predicted sequences, while errors on the FFT on the predicted sequences may be more robust to such dependencies.  The experiments on multiple datasets and multiple baseline DF models demonstrate the improved performance of the new method over baselines.

### Strengths
Originality: The idea of augmenting an objective function with a loss in alternate bases that is more robust to value dependences in prediction sequences, in this case Fourier bases, is novel and interesting.

Significance: The extension applies to a subclass of direct forecasting models that predict components of future sequences independently, ignoring dependences that may exist among them.  This makes the method potentially applicable to a variety of SOTA time series models. 

Quality: The authors attempt to analyze the problem of using simple additive error functions for predicting sequences and its fixes via errors in the FFT transformed space both theoretically and experimentally. Extensive experimentation across multiple datasets and tasks show the merits of the proposed approach compared to SOTA baselines.

Other strengths: Exploration of properties and extension of the proposed framework and its benefits, such as, different prediction length, ablation models,  possible new transformations and errors defined on these transformations. 

Code: Authors provide the code for reproducing the experiments.

### Weaknesses
Limited analysis of a bias in Theorem 1: Theorem 1 considers only univariate sequences, cross-correlation terms are not accounted for in the Bias formula. The sequence has dimensionality D.  The bias expression should explicitly account for the interactions between different dimensions of the multivariate time series, as these interactions can significantly impact prediction accuracy. Specifically, the formula should include terms that capture the covariance or correlation between the different time series components, which are not addressed in the current formulation. This omission limits the theorem's applicability to real-world scenarios where time series are often multivariate and exhibit complex interdependencies.

Notational inconsistency and formula errors in the paper: 
- The use of 'L' is overloaded, it denotes both the length and inputs of the input sequence. 
- Equation 1 has a mistake. Y and Y_hat should be compared on the same indexes. 
- Definition 3.2, uses 'j' instead of “i”  

The main results in the paper do not report performance over distinct random seeds. Given this is an experimental study, reporting the results on multiple distinct random seed could help to understand its sensitivity. The lack of this analysis makes it difficult to assess the robustness of the proposed method and whether the observed improvements are consistent across different training runs. This is particularly important for time series forecasting, where the initial conditions and random initialization can significantly affect the results.

The short-term forecasting task results in the appendix report only qualitative time spans. It would be good to specify the results in terms of forecasting lengths, similar to the Table 1 for long-term forecasting. The absence of specific forecasting lengths makes it difficult to compare the performance of the proposed method with other approaches and to understand its behavior across different prediction horizons. Providing quantitative results for each forecasting length would allow for a more thorough and meaningful evaluation.

### Questions
Are there any settings where defining the errors by transferring the predictions to the frequency domain is detrimental to the prediction accuracy?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to measure the distance between time series prediction outputs and target signals in the frequency domain. 
As claimed, this allows to capture label autocorrelation in time series prediction tasks. Speciafically, in practice, distances in both time and frequency domains are utilized for training in a combined manner.

### Strengths
The presentation of the paper is clear and the idea is straightforward.

### Weaknesses
The proposed approach lacks novelty. Measuring time series structure (e.g., autocorrelation) in the frequency domain has been well-explored. Several prior works have investigated capturing time series characteristics or enhancing robustness in loss functions, including:
  1. Incorporating Fourier transformation in loss functions [1,2].
  1. Employing DTW-based loss to keep shape information of time series [3,4].
   1. Utilizing multiresolution trends during training [5,6].

These approaches are all relevant to this study. However, this paper does not adequately investigate, discuss, or compare these related methods.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
