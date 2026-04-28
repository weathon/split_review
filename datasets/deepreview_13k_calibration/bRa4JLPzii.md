# CoMRes: Semi-Supervised Time Series Forecasting Utilizing Consensus Promotion of Multi-Resolution

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
Long-term time series forecasting poses significant challenges due to the complex dynamics and temporal variations, particularly when dealing with unseen patterns and data scarcity. Traditional supervised learning approaches, which rely on cleaned and labeled data, struggle to capture these unseen characteristics, limiting their effectiveness in real-world applications. In this study, we propose a semi-supervised approach that leverages multi-view setting on augmented data without requiring explicit future values as labels to address these limitations. By introducing a consensus promotion framework, our method enhances agreement among multiple single-view models on unseen augmented data. This approach not only improves forecasting accuracy but also mitigates error accumulation in long-horizon predictions. Furthermore, we explore the impact of autoregressive and non-autoregressive decoding schemes on error propagation, demonstrating the robustness of our model in extending prediction horizons. Experimental results show that our proposed method not only surpasses traditional supervised models in accuracy but also exhibits greater robustness when extending the prediction horizon.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses challenges in long-term time series forecasting, particularly in managing unseen patterns and data scarcity. The authors propose CoMRes, a semi-supervised, multi-view approach to enhance forecasting by promoting consensus among multiple models on augmented, unseen data. This method aims to improve prediction accuracy and reduce error accumulation over extended horizons. Additionally, the study examines both autoregressive and non-autoregressive decoding schemes, emphasizing the robustness of non-autoregressive decoding in minimizing long-term error propagation. Experimental results highlight CoMRes's superior performance and stability compared to traditional supervised models.

### Strengths
The strengths are as follows:

- The paper is clear, well-written and presented.
- The authors cover most of the commonly used datasets in the field, and some relevant baselines: the empirical constributions appear sound as a result.
- Results indicate the method does indeed provide some life over the baselines.

### Weaknesses
The weaknesses are as follows:

- Absence of submitted code making reproducibility more difficult.
- The paper could benefit from more detailed comparisons with other time-series forecarsting methods.
- It would be interesting to include error bars on the results table, especially given the proximity of different methods.

### Questions
- Could the authors add error bars?
- What are the author's plans wrt. the release of code?

Edit: the authors have addressed the questions and points I raised to a level that I find satisfactory. I am raising my score as a result.

### Soundness
3

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
5

### Summary
The authors propose CoMRes, a long-term forecasting architecture based on Pathformer, which leverages a consensus promotion mechanism for multi-resolution views. The core idea is to align the supervised predictions of multiple resolutions with the aggregated prediction. Furthermore, they use augmentation strategies (Time Warping, Interpolation and Noise Injection) to construct the different views.  The work also presents an evaluation using autoregressive and non-autoregressive decoding schemes, aiming to show the robustness of the forecasts in longer prediction horizons. The authors claim that CoMRes outperforms traditional supervised models, exhibiting greater robustness and accuracy on multiple popular datasets.

### Strengths
- The paper introduces an interesting concept of promoting consistency among multi-resolution views, which has potential in capturing complex temporal relationships.

- The amount of datasets used in the experimental section is exhaustive, which adds impact to the of the experimental results.

- The addition of limited-resource scenarios is valuable, as this is often the case in time series applications.

- In general i think the writing of the paper is good and understandable.

- The discussed related work seems to be exhaustive.

### Weaknesses
 - The title and abstract do not clearly explain why the proposed approach is semi-supervised. It is challenging to understand how forecasting can be performed in a "semi-supervised" manner, given that "labels" can be constructed by shifting the time window. It would be helpful to provide more concrete explanations on this aspect, particularly regarding the proposed use of augmented data and the challenges with temporal dynamics.

- In lines 031-033, the statement about the superiority of transformers in forecasting is misleading. Multiple recent works (Das et al., 2023; Wang et al., 2024; Zeng et al., 2023) [1,2,3] have shown that transformers are not always state-of-the-art. This statement should be reconsidered or at least clarified with respect to specific contexts or benchmarks.

- The comparison against relevant baselines is lacking. The paper does not include benchmarks like TimeMixer, TiDE, PatchTST, D/NLinear, and other advanced transformer-based models (e.g., iTransformer). Including these baselines would significantly strengthen the evaluation and provide a better context for the proposed model.

- The tables, particularly Table 1, are difficult to read. I'm not sure what red or blue means at least its not stated in the caption.

- The baseline method achieves the best result multiple times without the proposed augmentations, which weakens the argument for using the augmentations. In general I'm pretty confused about what the idea of multiple resolutions vs augmentations is in this work.

- While the limited-resource scenario is a useful addition, it does not effectively demonstrate how the method performs on datasets with many variables (e.g., Traffic or Electricity). This should at least be stated in the limitations/conclusion section.

### Questions
1. In line 032, the paper cites Wang et al., suggesting multi-resolution methods "overlook consistency." Could you provide specific details about what was missed in the multi-resolution reconciliation methods used by Wang et al.?

2. In Section 3, you mention that augmentations are less effective in forecasting compared to classification and anomaly detection. Could you elaborate on why this is the case? Specifically, how does your chosen augmentations differ?

3. Why do you assume a Euclidean distance to measure consensus between the aggregated prediction and each view? Would other measures, such as soft-DTW, work better?

4. Does your framework also work with more "complex" augmentation strategies beyond the three mentioned (time warping, noise injection, interpolation)? Maybe discussing the limitations is a valuable contribution.

5. Could you clarify whether MRes is your method (with ablated components)? I would not count that as a baseline.

6. I'm a bit confused, at what points do you use augmentations, and at what different resolutions (scales)? Could you describe this process in more detail?

7. The paper claims superior robustness compared to traditional supervised learning approaches. Could you clarify how exactly robustness was demonstrated?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a "consensus promotion" learning objective to enhance the consistency of multi-scale time series data predictions. Additionally, given this learning objective is well-suited for semi-supervised learning, the authors introduce data augmentation strategies aligned with the proposed framework to further improve model generalizability. Extensive experiments are conducted on various datasets and ablation settings.

### Strengths
(1) This paper proposes and investigates a novel perspective on improving time-series prediction tasks: the consistency of predictions across different patch sizes of time-series data, which represents an interesting and promising research direction.

### Weaknesses
The main weakness of this paper lies in its evaluation.

(1) The variance of model performance and metrics is not reported for any experimental results, making it difficult for readers to assess whether the minor improvements are consistent and significant or simply due to stochastic gradient descent. The authors are encouraged to report variances for all results and conduct comprehensive statistical tests to demonstrate whether the improvements are statistically significant.

(2) There is no experimental evidence to demonstrate whether the proposed consensus promotion is actually beneficial. For example, what is the exact prediction MSE for each "individual-view model"? Do they actually become more consistent after applying the unsupervised consistency loss? Additionally, in Table 1, if I understand correctly, the only difference between "MRes (SL)" and "MRes w. consensus" is that "MRes w. consensus" includes additional consensus promotion learning objectives. However, there are no consistent patterns indicating which model's MSE is generally smaller. The authors are encouraged to design clear experiments that demonstrate whether the proposed consensus promotion works as expected and whether it is beneficial for the prediction task.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper discusses multi-resolution long-term time-series forecasting (LTSF). This work extends the Pathformer architecture with two components: data augmentation, and consensus-based training loss for multiple MLP outputs. Comparison between the ablated components and Pathformer is held on widely used time-series prediction benchmarks. Proposed CoMRes improves over the baselines.  Further analysis is done on resource-efficient case.

### Strengths
1) The multi-resolution time-series forecasting task is an important direction.

2) Authors have done an in-depth study on the ablation study.

### Weaknesses
1) I am uncertain about the novelty of the proposed paper. This paper borrows most of the architecture from the Pathformer, except the MLP for the individual component output and the aggregation layer. Furthermore, the consensus-based loss that minimizes the relative difference can be naturally formulated while utilizing the ensemble. I feel like this paper is a sheer extension of the Pathformer and the previous methods that utilize data augmentation.

2) The experiment results do not convince the efficacy of the method. MRes with consensus training often underperform over the MRes baseline. Furthermore, performance differences between the data augmentations are small. This questions the efficacy of each component as a general method. Finally, ComRes drastically underperforms Pathformer in one dataset, which questions the efficacy of the whole algorithm in general.

3) The extra MLP layer may induce an extra computation burden on the training and inference stage, especially since (M+1) calculations are all required for the final computation. Maybe further analysis of the computation efficiency will further help to understand the limitations.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
