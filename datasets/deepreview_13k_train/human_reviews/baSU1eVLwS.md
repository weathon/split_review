# TimeBridge: Non-Stationarity Matters for Long-term Time Series Forecasting

- Decision: Reject
- Scores: 8, 3, 3

## Abstract
Non-stationarity poses significant challenges for multivariate time series forecasting due to the inherent short-term fluctuations and long-term trends that can lead to spurious regressions or obscure essential long-term relationships. 
Most existing methods either eliminate or retain non-stationarity without adequately addressing its distinct impacts on short-term and long-term modeling.
Eliminating non-stationarity is essential for avoiding spurious regressions and capturing local dependencies in short-term modeling, while preserving it is crucial for revealing long-term cointegration across variates.
In this paper, we propose \NAME, a novel framework designed to \textit{bridge the gap between non-stationarity and dependency modeling in long-term time series forecasting}. 
By segmenting input series into smaller patches, \NAME applies Integrated Attention to mitigate short-term non-stationarity and capture stable dependencies within each variate, while Cointegrated Attention preserves non-stationarity to model long-term cointegration across variates.
Extensive experiments show that \NAME consistently achieves state-of-the-art performance in both short-term and long-term forecasting. Additionally, \NAME demonstrates exceptional performance in financial forecasting on the CSI 500 and S\&P 500 indices, further validating its robustness and effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces TimeBridge, a framework for multivariate time series forecasting that addresses the challenge of non-stationarity by differentiating between its impacts on short-term and long-term modeling. TimeBridge utilizes Integrated Attention to manage short-term fluctuations in batches, reducing spurious regressions and capturing local dependencies. Cointegrated Attention is introduced to preserve long-term non-stationarity across variates, enabling effective long-term dependency capture. Experiments on the CSI 500 and S&P 500 indices verify the short- and long-term forecasting performance. It is generally a method for handling nuanced non-stationarity effects in complex multivariate scenarios.

### Strengths
1. This paper is well written. The notations are clear.

2. It provides up-to-date literature on learning techniques for capturing stationary/non-stationary and dependency in sequential data. It combines the treatments of non-stationarity and dependency modeling in one shoot and delivers convincing performances.

3. The notion of cointegration of time series has been missing or forgotten in recent time series forecasting literature; this paper showed how cointegration could help reveal the non-stationary part when multiple time series evolve simultaneously. 
In Operations Research, cointegration is a well-established technique, and it has been introduced to machine learning literature for long:

Marco Cuturi, Alexandre D’Aspremont (ICML, 2013). https://proceedings.mlr.press/v28/cuturi13.html

The authors may refer to basic cointegration techniques to resolve the computational challenges or benchmark the extraction of stationary/non-stationary movements.

4. The experiments are comprehensive and cover recent state-of-the-art competing methods. The results are convincing, as shown by a solid ablation study showing the contribution of the building blocks, e.g., Integrated Attention and Cointegrated Attention.

### Weaknesses
1. According to Figure 3, the building blocks of the proposed methods are streamlined with no conjugation. In some sense, this is brute force and remains room for improvement or further technical development, speaking of the systematic organic treatment of the non-stationarity and dependency modeling in long-term time-series forecasting.


### Questions
Q. As mentioned in Strength 3, it would be interesting to recap traditional techniques for cointegration in operations research and benchmark the stationary or non-stationary time series before discussing the impact of an attention-powered module.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents TimeBridge for non-stationary time series forecasting. TimeBridge utilizes Integrated Attention to mitigate short-term non-stationarity and Cointegration Attention for modeling long-term non-stationarity. Experiment results on benchmarking time series demonstrate the effectiveness of TimeBridge.

### Strengths
+ Non-stationarity is a major challenge in time series forecasting. The paper aims to address this important task
+ Experiment results are encouraging, with a comprehensive ablation study.

### Weaknesses
 - The idea of Integrated Attention and Cointegration Attention is not new. The model in general lacks novelty.

- The improvement by TimeBridge is not as much as claimed in the paper (over 10%). On most of the datasets, TimeBridge achieves similar results or marginally better results (Table 1 and 2). In general, the popular benchmarking time series are relatively easier tasks. On finance applications, TimeBridge's performance is similar to TSmixer.

### Questions
What is TimeBridge's performance on bigger time series dataset, such as New York Taxi or Climate Data?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces TimeBridge for predicting non-stationary time series, aiming to resolve the contradiction between short-term fluctuations and long-term trends. By dividing the input sequence into small segments and applying an integrated attention mechanism to reduce short-term instability while utilizing joint attention mechanisms to preserve non-stability to capture long-term co-integration relationships across variables, TimeBridge effectively captures stable dependencies without introducing pseudo-regression risks. Experimental results demonstrate that TimeBridge performs well on multiple tasks, particularly outperforming current state-of-the-art methods in financial time series prediction. Additionally, through a series of ablation studies, the importance of removing or preserving non-stability and the order of integrated and joint attention modules is further validated, revealing optimal model configurations under different dataset backgrounds. This work not only enhances the accuracy and robustness of time series prediction but also provides new perspectives and methods for handling non-stationary data in the future.

### Strengths
- Resolving the conflict between short-term fluctuations and long-term trends: TimeBridge can effectively capture stable dependencies by reducing short-term non-stability through dividing the input sequence into small fragments and applying integrated attention mechanisms, while utilizing joint attention mechanisms to preserve non-stability to capture cross-variable long-term co-integration relationships.

- Improving the accuracy and robustness of time and sequence prediction: TimeBridge performs well on multiple tasks, particularly outperforming current state-of-the-art methods in financial time series prediction.

- Providing new perspectives and methods for handling non-stationary data in the future: Through a series of ablation studies, this article further verifies the importance of removing or retaining non-stability, as well as the sequence of integrated and joint attention modules, and reveals the optimal model configuration under different datasets, providing new perspectives and methods for handling non-stationary data in the future.

### Weaknesses
 - The paper lacks sufficient originality, as it primarily builds upon existing methods without presenting a clear, novel contribution to the field. This limits the manuscript's potential impact and reduces its value as an advancement in research.

- The lack of experiments with varying input/output (I/O) ratios raises concerns about the fairness of the comparisons. Different I/O settings can affect model outcomes substantially, and without exploring these variations, the paper provides an incomplete evaluation of model performance.

- The authors have only considered MSE and MAE as metrics for their long-term forecasting task, which is insufficient. This limited evaluation may obscure important aspects of model accuracy, particularly in cases where relative error size is a crucial factor for assessing model effectiveness.

- The paper lacks a clear description of the hyperparameter tuning process for the comparative algorithms, which raises concerns about the comparisons. Without adequate tuning, it is difficult to ascertain if the reported performance differences are truly reflective of each model's capabilities.

### Questions
- The experimental settings are not reasonable. Why input length is set to 720, output length O is set to 96, 192, 336, 720 and not something more practical, like 1 month of data? 

- The paper does not account for the impact of varying input/output (I/O) ratios, which can significantly influence model performance. Fixing different input length for baselines without comprehensive experiments may lead to biased comparisons and limit the robustness of the results. The author needs to report the results of the baseline under the same experimental setup.

- The paper lacks an evaluation of the algorithm's complexity, particularly with respect to its theoretical complexity, GPU resource cost, and runtime efficiency. Without this assessment, it is difficult to gauge the algorithm's practicality and scalability, especially in resource-constrained environments.

- The absence of detailed hyperparameter optimization for the baseline algorithms undermines the fairness of the comparisons presented in the paper. Without this tuning, the results may not accurately represent the optimal performance of the comparative models, potentially leading to biased conclusions.

### Soundness
2

### Presentation
2

### Contribution
2
