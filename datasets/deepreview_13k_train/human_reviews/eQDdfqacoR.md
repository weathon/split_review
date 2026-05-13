# Evolving Multi-Scale Normalization for Time Series Forecasting under Distribution Shifts

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
Complex distribution shifts are the main obstacle to achieving accurate long-term time series forecasting. Several efforts have been conducted to capture the distribution characteristics and propose adaptive normalization techniques to alleviate the influence of distribution shifts. However, these methods neglect the intricate distribution dynamics observed from various scales and the evolving functions of distribution dynamics and normalized mapping relationships. To this end, we propose a novel model-agnostic \textbf{Evo}lving \textbf{M}ulti-\textbf{S}cale \textbf{N}ormalization (EvoMSN) framework to tackle the distribution shift problem. Flexible normalization and denormalization are proposed based on the multi-scale statistics prediction module and adaptive ensembling. An evolving optimization strategy is designed to update the forecasting model and statistics prediction module collaboratively to track the shifting distributions. We evaluate the effectiveness of EvoMSN in improving the performance of five mainstream forecasting methods on benchmark datasets and also show its superiority compared to existing advanced normalization and online learning approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces the Evolving Multi-Scale Normalization framework, a model-agnostic approach designed to address complex distribution shifts in time series forecasting. EvoMSN combines multi-scale statistics prediction, adaptive ensembling, and an evolving bi-level optimization strategy to improve the accuracy of long-term forecasts. The framework is evaluated on several real-world datasets and shown to significantly enhance the performance of five mainstream forecasting methods.

### Strengths
1. The EvoMSN framework introduces the concept of multi-scale statistics prediction, extending existing normalization methods. By combining this with adaptive ensembling and online learning strategies, the framework better captures and responds to data distribution changes. This integration of multiple techniques provides a new approach to addressing distribution shifts in time series forecasting.
2. The authors present robust experimental results that demonstrate the effectiveness and superiority of EvoMSN. These experiments span a variety of real-world datasets and utilize multiple advanced forecasting methods as backbones, ensuring the reliability and generalizability of the findings.
3. The paper is well-structured and logically coherent.

### Weaknesses
1. The paper aims to tackle the complex distribution shifts problem, but the description of what constitutes these distribution shifts is somewhat vague. It would be beneficial to provide a more specific description of how the distributions change. For instance, among the distributions \(P(X)\), \(P(Y)\), \(P(X|Y)\), and \(P(Y|X)\), which ones are changing and which ones remain constant? A clearer delineation of these changes would enhance the understanding of the problem being addressed. Specifically, it is unclear whether the shifts are primarily in the marginal distributions \(P(X)\) and \(P(Y)\), or in the conditional distribution \(P(Y|X)\), or a combination of both. Furthermore, the temporal dynamics of these shifts are not well-defined. Are the shifts abrupt or gradual? Are they periodic or random? A more precise characterization of these shifts is needed to fully appreciate the problem's complexity.

2. The paper lacks a detailed explanation of why normalization and denormalization can effectively address distribution shifts in time series forecasting. Providing a theoretical or empirical justification for this approach would strengthen the paper's arguments and help readers understand the underlying mechanisms better. For example, it's not clear how the proposed normalization method ensures that the transformed data retains the essential temporal dependencies required for accurate forecasting. The paper should discuss whether the normalization process might inadvertently remove or distort important time-series characteristics, such as trends or seasonality, and how the denormalization process recovers these characteristics without introducing bias.

3. The paper states that the EvoMSN framework can be combined with existing time series forecasting methods to improve their performance. However, it does not quantify the increase in computational complexity during training and testing when incorporating the EvoMSN framework. Understanding the trade-off between performance improvement and computational cost is crucial for practical applications. The paper should provide a detailed breakdown of the computational overhead introduced by the multi-scale statistics prediction module and the adaptive ensembling process, including both time and memory requirements. This analysis should consider the complexity of the backbone forecasting model and the number of scales used in the EvoMSN framework.

4. Section 3.3 introduces an offline two-stage pretraining and online alternate updating method to solve the bi-level optimization problem. The paper does not adequately explain why this particular method was chosen and whether there are theoretical guarantees for the optimization results obtained using this approach. A more detailed discussion of the advantages and potential limitations of this method would be beneficial. Specifically, the paper should explain why a bi-level optimization is needed and why the proposed offline-online strategy is suitable for this problem. The paper should also discuss the convergence properties of the proposed optimization method and whether it guarantees finding a local or global optimum.

5. The experimental results show that the EvoMSN framework does not consistently improve the performance of the models. The paper does not provide a detailed analysis of why this inconsistency occurs. A thorough investigation of the conditions under which the framework performs well or poorly would help in understanding the robustness of the proposed method and guide future improvements. For example, it is important to analyze whether the performance of EvoMSN is dependent on the specific characteristics of the datasets, such as the length of the time series, the presence of specific patterns, or the magnitude of distribution shifts. The paper should also investigate whether the choice of the backbone forecasting method affects the performance of EvoMSN.

### Questions
Refer to the weakness.

### Soundness
2

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
This paper introduces a model-agnostic Evolving Multi-Scale Normalization (EvoMSN) framework to tackle the forecasting of
time series with distribution shifts since existing implementations lack the capability of capturing the distribution dynamics
from various scales and modeling the evolving normalized input-output mapping functions caused by gradual distribution
shifts.

The contributions are as follows:

1. EvoMSN is a model-agnostic online normalization framework that enhances any arbitrary backbone forecasting models by
adaptively removing and recovering dynamical distribution information.

2. A multi-scale statistics prediction module is introduced to estimate the statistics of future distributions. An adaptive
ensemble strategy is designed to ensemble the denormalized outputs based on the weights of the local amplitude.

3. An evolving bi-level optimization strategy, including offline two-stage pretraining and online alternating learning, is
proposed to update the statistics prediction module and the backbone forecasting model collaboratively.

4. The effectiveness of the proposed method in boosting forecasting performance under distribution shifts is evaluated on
five large-scale real-world time-series benchmark datasets.

### Strengths
The proposed novel framework (EvoMSN) is unique since it combines multi-scale statistics prediction, adaptive ensembling, and
an evolving bi-level optimization strategy to tackle the distribution shift problem in time-series forecasting. It differs from existing
implementations that lack of the capability of capturing the distribution dynamics from various scales and modeling the evolving
normalized input-output mapping functions caused by gradual distribution shifts.

The research is based on sufficient analysis of related existing works. Each component of the proposed framework is well-
introduced. The effectiveness is demonstrated using five large-scale real-world time-series benchmark datasets with appropriate
experiment setup.

The paper is well-organized clear sections for introduction, related works, proposed framework, experiments and conclusion.
The introduction outlines the significance of distribution shift problem in time-series forecasting, the limitations of existing
methods, and the proposed solution.

This paper addresses the distribution shift problem more comprehensively compared to existing implementations. The proposed
framework improves the accuracy of the time-series forecasting. The proposed EvoMSN is model-agnostic that makes it
possible to enhance any arbitrary backbone forecasting models.

### Weaknesses
Online forecasting limitations
1. Module update frequency: The parameters of multi-scale statistics prediction module are updated only once for each
incoming new data which might lead to difficulties in extracting some fast-changing statistics, resulting in poor performance. This single update per new data point may not be sufficient to capture rapid shifts in the underlying data distribution. The model might struggle to adapt to sudden changes, potentially leading to inaccurate predictions during periods of high volatility or abrupt distributional changes. A more frequent update mechanism, perhaps triggered by a change detection algorithm, could be beneficial.

2. Periodicity extraction: The global dominant periodicity is determined based on the training data. In the online setting, a
relatively small training data split ratio might cause inappropriate periodicity extraction and will affect the effectiveness of
multi-scale slice-based analysis. The reliance on a fixed periodicity derived from initial training data could be problematic. If the underlying periodicity of the time series changes over time, the fixed periodicity used for slicing will become misaligned with the actual data patterns, leading to suboptimal performance. The method should consider adaptive periodicity extraction or a mechanism to detect and adjust to changes in periodicity.

Offline forecasting limitations

1. Module update scopes: In the offline pretraining stage, the multi-scale statistics prediction module is only updated on the
training data. The distinct statistics evolving dynamic of training data and testing data may cause worse performance in the
evaluation stage. The pretraining of the statistics prediction module solely on training data may not generalize well to the test data, especially if the test data exhibits different distributional characteristics. The model might overfit to the training data's specific distribution dynamics, leading to poor performance on unseen data with different statistical properties. This limitation highlights the need for a more robust pretraining approach that accounts for potential distributional differences between training and testing data.

Modeling limitations

1. Incomplete distribution characteristics: The multi-scale statistics prediction module only produces the mean and the
deviation of each slice. More comprehensive characteristics of distribution, such as minimum and maximum value, are
significant but neglected in the proposed framework. By only considering mean and standard deviation, the model might miss important distributional information. For example, the presence of outliers or skewness in the data, which are not captured by mean and standard deviation alone, could significantly impact the accuracy of the forecasting. Incorporating additional distribution characteristics, such as quantiles or higher-order moments, could lead to a more robust and accurate model.

### Questions
1. The multi-scale statistics prediction module is a two-layer perceptron network. Have you ever attempted to employ any
other different architecture and analyze the sensitivity?

2. Windowing functions are often coupled with FFT. Have you ever attempted to use different windowing functions and
analyze the sensitivity?

3. FFT often assumes the time-series data is stationary. When this assumption is violated, the resulting frequency-amplitude
information might be not meaningful. Have you consider using any other approaches, and if so, how does the performance
vary?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents the EvoMSN framework, a novel approach to time series forecasting under distribution shifts. It introduces a model-agnostic methodology that utilizes multi-scale statistics prediction and adaptive ensembling to normalize and denormalize data, addressing the complexities of distribution dynamics and non-stationarity. The framework is evaluated through comprehensive experiments on real-world datasets, demonstrating significant improvements over the original models.

### Strengths
1. The proposal to use multi-scale statistics prediction and adaptive ensembling for normalization is innovative and addresses a critical gap in handling distribution shifts in time series data. And the framework is model-agnostic, increasing its versatility and applicability across various forecasting models.
2. The paper provides a thorough experimental evaluation, showcasing the effectiveness of EvoMSN in improving forecasting performance under distribution shifts across different datasets and forecasting models as well as other frameworks. The results demonstrate substantial improvements over state-of-the-art methods.

### Weaknesses
1. The paper could benefit from a more detailed discussion on the limitations of the EvoMSN framework, such as assumptions made, potential scenarios where the framework may underperform, and its scalability challenges. Specifically, the paper lacks a discussion on the sensitivity of the framework to the choice of multi-scale parameters, such as the number of scales and the length of each scale. Furthermore, the paper should address the potential for error accumulation when predicting statistics across multiple scales, and how this might impact the final forecasting performance. A discussion on the types of distribution shifts that EvoMSN is most effective at handling, and those where it might struggle, would also be beneficial.

2. While the framework is innovative, the paper lacks a detailed analysis of its computational complexity and scalability, which are crucial for practical applications, especially with large datasets. Even more, the training samples are sampled from a look back windows, which means that the effectiveness of the module relies heavily on the training data, potentially affecting the framework's performance in real world data. And how is it able to learn the preicise multiscale statistics predictions without sampling from a multiscale look back window. The paper does not specify the computational cost associated with the multi-scale statistics prediction module, nor does it analyze how the complexity scales with the input time series length or the number of scales considered. The paper needs to provide a more rigorous analysis of the time and space complexity of the proposed method, especially in comparison to existing methods.

3. The paper needs a much more detailed visualization on the learned statistics predictions to prove that the module actually works. The current visualizations are insufficient to demonstrate the efficacy of the multi-scale statistics prediction module. The paper should include visualizations that show the predicted statistics (mean and standard deviation) at each scale, compared to the actual statistics, over a longer time horizon. This would allow for a more thorough evaluation of the prediction module's accuracy and its ability to capture the dynamics of the time series data. Furthermore, the paper should provide a visualization of how the adaptive ensembling weights change over time, and how these weights are influenced by the predicted statistics.

### Questions
As is commented in Weakness.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The author proposed a new model-agnostic Evolutionary Multi-Scale Normalization (EvoMSN) framework to address the distribution shift issue. It includes a multi-scale statistical prediction module and flexible normalization and denormalization methods with adaptive integration. The experiments demonstrated the effectiveness of the model.

### Strengths
Time series prediction is very important.

The author proposes an effective model.

### Weaknesses
Q1. The relevant experimental details are confusing. What does the statement 'According to the widely applied online setting, the forecasts will be made as each test data sample arrives, and the model will be updated by one epoch according to the online forecasting loss' mean? Do you update the model once for a test sample or once for a batch sample? Please further explain the specific settings of online learning in detail.

Q2.  To validate the model's effectiveness across a broader spectrum, larger-scale datasets spanning longer time periods should be incorporated.  This will help ascertain the model's robustness and applicability in scenarios with more significant temporal variations.

Q3. Could authors add more baselines in the experiment, such as PatchMixer, Crossgcn, iTransformer, TimeMixer, Koopa, and other models.

Q4. The author's contribution is incremental. The author's online learning strategy mainly involves patch normalization and two-stage training strategies, which have already been discussed in SAN and [2]. The contributions of SAN and [2] were overlooked in the related work and methods section. Additionally, what are the differences between the evolutionary training strategy and [2]? In Table 14, I did not observe significant performance improvements of the proposed model compared to SAN. The idea of multi-scale modeling originates from TimeMixer. It is recommended that the author further discuss these works in detail to clearly demonstrate their contribution. Furthermore, I suggest rewriting the recommendation section to highlight the technical gaps in existing works more clearly to clarify the motivation.

Q5. In Table 5, we can see that the primary performance of the proposed method comes from the Online-strategy based on BI-LEVEL OPTIMIZATION, as discussed in [1] and [2]. Additionally, why did the author not evaluate the performance variability of multi-scale modeling variables? What findings are observed when K is greater than 4? Why were only ablation experiments conducted on DLinear? As far as I know, DLinear is a small model with unstable training, where even a small difference in a epoch could lead to significant performance variations. Therefore, it is recommended to add more benchmarks for a comprehensive evaluation.

Q5. Time series datasets are typically offline, and the running time of various models does not exceed one day.  Could you elaborate on the practical applications and advantages of online time series learning? 

Q6. DLinear reported a performance of 0.081 in the Exchange but 0.131 in this paper, and the performance of other benchmarks also dropped significantly in this paper. What could be the reason for this? A significant decline in baseline performance also occurs in Table 13. Please explain potential reasons for the discrepancy in results.

Q7. Can the author provide a comparison of other models in Table 11?

Q8. The author's motivation for the paper is the non-stationarity of time series, and the contribution is to address this problem from an online learning perspective. However, by comparing Table 1 and Table 8, I find that online learning does not actually have any benefits, and the performance of most models has shown a huge decline. The potential reason is that a test sample will lead to overfitting after updating the model. We do not need this update, and the original model can perform very well (at least better than after online learning).

Q9. Unfair comparison. As mentioned above, updating the model with data from one batch or one sample can lead to overfitting. The baseline model was updated twice, while the author's model was actually updated only once, resulting in a delayed decrease in model performance.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
