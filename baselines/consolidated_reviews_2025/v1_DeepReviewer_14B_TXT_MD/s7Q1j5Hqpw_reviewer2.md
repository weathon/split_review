### Summary

This paper proposes a Shift-Resilient Diffusive Imputation (SRDI) model for improving VSF performance by resolving distribution shift. Specifically, SRDI employs a divide-and-conquer strategy to tackle inter-series shift and enhances the meta-learning framework to address intra-series shift.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The problem is well formulated and the motivation is clear.
2. The proposed method is reasonable and the experiments demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works

[1] RobustTSF: Towards Theory and Design of Robust Time Series Forecasting with Anomalies
[2] Towards Robust Time Series Forecasting under Distribution Shifts
[3] Time Series Forecasting with Distribution Shifts: A Causal View with Counterfactual Inference

#### comment

1. The problem of variable subset forecasting is very similar to the problem of time series forecasting with missing values. Please clarify the difference between these two problems.
2. The problem of variable subset forecasting is very similar to the problem of time series forecasting with distribution shifts. Please clarify the difference between these two problems.
3. More recent related works should be included, such as [1][2][3].
4. The experiments are not convincing. Please add more experimental results to further demonstrate the effectiveness of the proposed method. For example, the performance of the forecasting model with different proportions of missing variables should be provided.
5. The proposed method is too complex and the contribution of each component is not clear. Please provide more ablation experiments to verify the effectiveness of each component.

### Suggestions

The paper needs to more clearly differentiate the variable subset forecasting (VSF) problem from existing time series imputation and distribution shift scenarios. While the authors frame VSF as a distinct problem, the core challenge of handling incomplete data is shared with imputation tasks. The paper should provide a more rigorous definition of VSF, highlighting the specific nuances that set it apart from standard missing data problems. For example, are the missing variables completely random, or is there a structured pattern to their absence? Furthermore, the paper should clarify how the distribution shift in VSF differs from the distribution shifts addressed in the cited works [1,2,3]. A more detailed explanation of the unique challenges posed by VSF, beyond simply stating that it involves both missing values and distribution shifts, is needed to justify the proposed method's complexity. The authors should also consider providing a theoretical analysis of the problem to further clarify its unique characteristics.

The experimental section needs significant expansion to convincingly demonstrate the effectiveness of the proposed method. The current experiments lack sufficient detail and breadth. Specifically, the paper should include a more comprehensive evaluation of the model's performance under varying proportions of missing variables. This should include a systematic analysis of how the model's accuracy degrades as the percentage of missing variables increases. Furthermore, the experiments should explore different patterns of missingness, such as random missing, block missing, and missing not at random scenarios. This would provide a more realistic assessment of the model's robustness. The paper should also include a comparison with more recent and relevant baselines, particularly those designed for time series forecasting under distribution shifts. The current baselines are not sufficient to demonstrate the superiority of the proposed method. The experimental results should also include a detailed analysis of the computational cost of the proposed method, as well as the sensitivity of the model to different hyperparameter settings.

The proposed method's complexity raises concerns about its practical applicability and the interpretability of its components. The paper should provide a more detailed ablation study to justify the inclusion of each component. This should include a systematic analysis of the model's performance with and without each component, as well as a detailed explanation of the role of each component in the overall framework. The paper should also provide a more detailed explanation of the meta-learning framework, including the specific algorithms used and the rationale behind their selection. The authors should also consider providing a visualization of the learned representations to better understand how the model is capturing the underlying patterns in the data. Finally, the paper should discuss the limitations of the proposed method and suggest directions for future research.

### Questions

Please refer to the weaknesses.

### Rating

5

### Confidence

3

**********
