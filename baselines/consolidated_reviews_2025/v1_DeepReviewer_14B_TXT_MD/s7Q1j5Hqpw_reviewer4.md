### Summary

This paper introduces a novel Shift-Resilient Diffusive Imputation (SRDI) model designed to enhance Variable Subset Forecasting (VSF) performance by addressing distribution shifts. The SRDI model categorizes shifts in VSF into two types: inter-series shift and intra-series shift. It employs a diffusion model-based approach, utilizing a divide-and-conquer strategy to manage inter-series shifts and enhancing the meta-learning framework to tackle intra-series shifts. Extensive experiments on four real-world datasets demonstrate that SRDI outperforms state-of-the-art methods, effectively addressing the distribution shift challenge in VSF tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-organized, with a clear and logical structure that facilitates understanding of the proposed SRDI model and its components.
2. The authors provide a thorough explanation of the SRDI model, including the rationale behind the divide-and-conquer strategy and the meta-learning framework.
3. The experimental results are comprehensive, with detailed comparisons to state-of-the-art methods across multiple datasets, demonstrating the effectiveness of SRDI.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the SRDI model and potential areas for future research. Specifically, the current discussion lacks a rigorous analysis of the model's sensitivity to hyperparameter choices, particularly within the meta-learning framework. The paper should explore how different learning rates, batch sizes, and the number of inner-loop iterations affect the model's performance and convergence. Furthermore, a discussion on the computational cost associated with the meta-learning component, especially in comparison to simpler imputation methods, would be valuable.
2. While the paper provides a comprehensive evaluation of the SRDI model, it could include more diverse datasets to further validate the model's generalizability. The current selection of datasets, while relevant, may not fully capture the range of challenges encountered in real-world VSF scenarios. For example, datasets with varying degrees of seasonality, trend, and noise characteristics could provide a more robust assessment of the model's adaptability. Additionally, the paper should consider including datasets with different spatial dependencies, as the current datasets may not fully represent the complexity of real-world spatial-temporal data.

### Suggestions

To address the limitations regarding hyperparameter sensitivity, the authors should conduct a more thorough ablation study, systematically varying key hyperparameters within the meta-learning framework. This should include a detailed analysis of how these parameters affect the model's convergence speed, stability, and overall performance. For instance, the authors could explore the impact of different learning rates on the inner and outer loops of the meta-learning process, as well as the effect of varying batch sizes on the model's generalization capabilities. Furthermore, the authors should provide a clear rationale for their chosen hyperparameter values, justifying their selection based on empirical evidence and theoretical considerations. This analysis should also include a discussion of the computational cost associated with different hyperparameter settings, providing practical guidance for users of the SRDI model.

To enhance the generalizability of the SRDI model, the authors should expand their experimental evaluation to include a more diverse set of datasets. This should include datasets with varying degrees of seasonality, trend, and noise characteristics, as well as datasets with different spatial dependencies. For example, the authors could consider incorporating datasets from different domains, such as finance, energy, or environmental monitoring, to assess the model's performance across a wider range of applications. Additionally, the authors should explore the model's behavior on datasets with different spatial structures, such as those with non-uniform or dynamic dependencies. This would provide a more comprehensive understanding of the model's strengths and limitations, and help to identify potential areas for future improvement. The authors should also consider using datasets with varying time granularities to assess the model's adaptability to different temporal scales.

Finally, the authors should provide a more detailed analysis of the model's performance on different subsets of the data. This could include analyzing the model's performance on different regions of the spatial domain, or on different time periods. This would help to identify potential biases or limitations of the model, and provide insights into its behavior under different conditions. The authors should also consider visualizing the model's predictions and the corresponding errors, to gain a better understanding of its strengths and weaknesses. This analysis should be accompanied by a discussion of the potential implications of these findings for real-world applications.

### Questions

1. How does the SRDI model perform in real-time forecasting scenarios, and what are the computational requirements for such applications?
2. Can the authors discuss the potential for extending the SRDI model to handle other types of time series data or forecasting tasks beyond VSF?

### Rating

6

### Confidence

3

**********
