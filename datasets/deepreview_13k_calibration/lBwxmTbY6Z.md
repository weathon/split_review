# Tensor Time-Series Forecasting and Anomaly Detection with Augmented Causality

- Decision: Reject
- Avg Score: 3.75
- Scores: 8, 1, 3, 3

## Abstract
In time series, variables often exhibit high-dimensional characteristics, and relationships between variables tend to be intricate, encompassing aspects such as non-linearity and time-dependency. Understanding the interaction of variables and comprehending the distribution of their values can significantly enhance the effectiveness of time series data analysis tasks, such as forecasting and anomaly detection. Hence, in this paper, we start from the tensor time series, which can encode higher dimensional information than classic multivariate time series, and aim to discover and leverage their fine-grained time-dependent causal relations to contribute to a more accurate analysis. To this end, we first form an augmented Granger Causality model, named TBN-Granger Causality, which adds time-respecting Bayesian Networks to the time-lagged Neural Granger Causality through a bi-level optimization, such that the overlooking of instantaneous effects in typical causal time series analysis can be addressed. Then, we propose an end-to-end deep generative model, named TacSas, which takes the historical tensor time series, outputs the future tensor time series, and detects possible anomalies, by leveraging the TBN-Granger Causality in the history. Moreover, we show TacSas not only can capture the ground-truth causality but also can be applied when the ground-truth causal structures are hardly available, to help forecasting and anomaly detection. For evaluations, besides synthetic benchmark data, we have four datasets from the climate domain benchmark database ERA5 as the real-world tensor time series for forecasting. Moreover, we extend ERA5 with the extreme weather database NOAA for testing anomaly detection accuracy. We show the effectiveness of TacSas in different time series analysis tasks by comparing with causal baselines, forecasting baselines, and anomaly detection baselines.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper leverages Augmented Causality in tensor time series in forecasting and anomaly detection tasks.

It forms time-respecting Bayesian Networks to the time-lagged Neural Granger Causality (TBN-Granger Causality) model and addresses the overlooking instantaneous effects in typical causal time series analysis via a bi-level optimization. 

An end-to-end deep generative model, called Time-Augmented Causal Time Series AnalysiS Model, i.e., TacSas. is proposed with experimental results showing its outperformance.

### Strengths
- The paper is well-written, it provides a unified yet concrete view of how to capture Granger Causality in a generative manner.
- Experimental results show consistent outperformance on both forecasting and anomaly detection.

### Weaknesses
 - Capturing of Granger Causality in the context of tensor time series is not well reviewed in literature and methodology

### Questions
- The proposed method is overall interesting - However, could you provide a dedicated quantitative summary and micro case study in the Appendix regarding how TacSas can capture the ground-truth causality but also can be applied when the ground-truth causal structures are hardly available?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces TacSas, an end-to-end methodology for "tensor" time series forecasting that can be used for both forecasting in earth sciences, Granger causal discovery, anomaly detection, among others. TacSas reportedly includes 1/a custom pretrained autoencoder to preprocess tensor time series, 2/ a module for causal discovery for instantaneous effects and Granger-causality across time via bi-level optimization, 3/ anomaly detection in high dimensions inspired by extreme value theory. A few baselines are compared to, where TacSas appears to outperform baselines.

### Strengths
The paper posts a good review of literature for models in tensor-shaped time series and recent threads on causal discovery in time series with expressive models.

### Weaknesses
 - The paper is poorly written. It contains many spelling, grammar and other use-of-language mistakes that make it very difficult to discern the authors' intent and extremely difficult to follow the paper.
- Many important issues are handled with an off-hand approach. For example, see the citation of EVT for 'inspiration' or the expression of Thm 3.1. The theorem posits that "under standard causal discovery assumptions" the full causal graph can be recovered. Depending on what these assumptions are, this theorem may be a groundbreaking discovery. However the "proof sketch" of Thm 3.1 simply cites the source paper and does not construct any formal argument.
- Another example is the continued reference to "tensors" as being able to represent higher dimensional time series. This is the opposite of why tensors are conceptually used. Take the toy example of a 3x3 matrix and a 9-dimensional vector. Formally, there is nothing more 'high-dimensional' about the matrix.
- My final critique is on the experiment setup. The experiments contain no simple / naive baselines for forecasting or for anomaly detection. For such a complex architecture proposed, there is only a very limited ablation study to show which parts of TacSas are critical to its success.

### Questions
N/A

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed a model for spatial-temporal learning for forecasting and anomaly detection in weather prediction. The proposed model finds embedding for location and uses causal modeling to model the relationship between location for the final task. As experimental evidence paper shows results on 2 data sets and a comparison with only 3 benchmark models.

### Strengths
The paper is technically sound. I am aware of many spatio-temporal models but not sure if the causal model has been explored previously for this task. To me it paper gives a novel probabilistic model for the spatio temporal learning.

The paper is well-written and easy to follow.

### Weaknesses
Literature Survey misses many SOTA for example 

Spatio-temporal forecasting :
1. Li, Peiyuan, Yin Yu, Daning Huang, Zhi‐Hua Wang, and Ashish Sharma. "Regional heatwave prediction using Graph Neural Network and weather station data." Geophysical Research Letters 50, no. 7 (2023): e2023GL103405.
Anomaly detection 
2. Lira, Hernan, Luis Martí, and Nayat Sanchez-Pi. "A graph neural network with spatio-temporal attention for multi-sources time series data: An application to frost forecast." Sensors 22, no. 4 (2022): 1486.

The author should include more recent literature in his survey. 

According to my understanding, this approach only detects if some anomaly has a very high value, i.e.,  it detected only extreme values. But. In time series temporal anomalies i.e., anomalies containing the rare temporal pattern, and inter-variable i.e. anomalies where the inter-variable relationship does not match with the common pattern are of main concern. The paper did not detect. It needs to show the performance of the proposed model in various data in terms of temporal, inter-variable, or inter-location anomalies too. Please check  

Zhang, C., Song, D., Chen, Y., Feng, X., Lumezanu, C., Cheng, W., Ni, J., Zong, B., Chen, H. and Chawla, N.V., 2019, July. A deep neural network for unsupervised anomaly detection and diagnosis in multivariate time series data. In Proceedings of the AAAI conference on artificial intelligence (Vol. 33, No. 01, pp. 1409-1416).

### Questions
Why author did not compare with sota in the case of forecasting? 
1. Li, Peiyuan, Yin Yu, Daning Huang, Zhi‐Hua Wang, and Ashish Sharma. "Regional heatwave prediction using Graph Neural Network and weather station data." Geophysical Research Letters 50, no. 7 (2023): e2023GL103405.
Anomaly detection 
2. Lira, Hernan, Luis Martí, and Nayat Sanchez-Pi. "A graph neural network with spatio-temporal attention for multi-sources time series data: An application to frost forecast." Sensors 22, no. 4 (2022): 1486.

Why author did not go for other anomalies other than extreme value?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this manuscript, the authors start from the tensor time series, which can encode higher dimensional information than classic multivariate time series, and aim to discover and leverage their fine-grained time-dependent causal relations to contribute to a more accurate analysis. To this end, the authors first form an augmented Granger Causality model, named TBN-Granger Causality, which adds time-respecting Bayesian Networks to the time-lagged Neural Granger Causality through a bi-level optimization, such that the overlooking of instantaneous effects in typical causal time series analysis can be addressed.

### Strengths
1. Compared with only three baseline models, the proposed solution is significantly better. In particular, a unique visual example is given to analyze the effectiveness of the proposed method.

### Weaknesses
1. The authors ignore a large number of recent excellent graph convolution or graph attention models for time series prediction. It is worth mentioning that the classical baseline DCRNN is the result of 2018 years of reporting and is almost outperformed by current solutions. Obviously, it is difficult for the authors to complete the comparison of SOTA algorithm in such a short rebuttal period. Therefore, I believe that the experimental results of the manuscript cannot fully illustrate the effectiveness of the proposed method.

Interestingly, recent studies [1-2] in spatiotemporal representation learning (from the perspective of the equivariance [1] and latent fields [2]) have investigated the common characteristics among for related tasks, such as traffic, physical simulations, motion tracking.

From the perspective of graph convolutional networks for Spatio-Temporal representation learning, some baselines of current excellent performance are listed as [3-6]. Although these studies focus on traffic flow or smart city studies, they are similar to meteorological information in different geographical locations from the perspective of geospatial information mining.

E.g., STGCN [3], STSGCN [4], STFGNN [5] and ST-SSL [6].

### Questions
Please see details of the weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
