### Summary

This paper studies the scaling laws for time series foundation models (TSFMs). The authors investigate the performance of encoder-only and decoder-only transformers on both in-distribution and out-of-distribution data. The results show that both ID and OOD performance follow a power-law relationship with model parameters, compute budget, and training dataset size. However, encoder-only transformers demonstrate better scalability than decoder-only transformers, especially in OOD scenarios. The paper provides practical guidelines for designing and scaling TSFMs based on these findings.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper addresses an important and timely topic by investigating the scaling laws of TSFMs, which is crucial for advancing the development of robust and scalable time series forecasting models.
- The paper provides a systematic analysis of the scaling behavior of TSFMs, covering various factors such as model size, compute budget, and dataset size. This comprehensive approach offers valuable insights into the performance of TSFMs under different conditions.
- The paper presents clear and well-organized results, making it easy for readers to understand the key findings and their implications.

### Weaknesses

#### Some Related Works


#### comment

 - The paper focuses on univariate time series forecasting, which may not fully represent the complexities of real-world multivariate time series data. The findings may not generalize well to scenarios with multiple interdependent variables, where the relationships between variables can significantly impact model performance. Specifically, the absence of experiments involving multivariate time series limits the applicability of the conclusions to real-world datasets where multiple time series often exhibit complex correlations and dependencies. The paper should acknowledge this limitation and discuss how the observed scaling laws might differ in multivariate settings.
- The paper does not explore the impact of different time series forecasting horizons on the scaling behavior of TSFMs. The scaling laws observed may vary for short-term and long-term forecasting tasks, which could affect the generalizability of the findings. The paper should investigate how the model size and training compute requirements change as the forecasting horizon increases or decreases. For instance, it is possible that larger models trained on longer sequences may not necessarily generalize well to shorter forecasting horizons, and vice versa. This aspect needs further investigation to ensure the robustness of the conclusions.
- The paper lacks a detailed discussion on the practical implications of the observed scaling laws for real-world deployment of TSFMs. The findings may not directly translate to practical applications without further consideration of computational constraints and resource availability. The paper should provide concrete guidance on how to choose the appropriate model size and training compute based on specific application requirements and available resources. For example, it would be beneficial to include a discussion on the trade-offs between model size, computational cost, and performance, and how these trade-offs should be managed in practice.

### Suggestions

To enhance the paper's contribution, the authors should extend their experimental evaluation to include multivariate time series datasets. This would involve not only expanding the dataset size but also considering the unique challenges posed by multivariate data, such as the presence of complex interdependencies between variables. The authors should explore different methods for handling multivariate time series, such as using attention mechanisms that can capture cross-variable relationships or employing graph neural networks to model the dependencies between variables. Furthermore, the paper should analyze how the observed scaling laws differ in multivariate settings compared to univariate settings. This would provide a more comprehensive understanding of the scaling behavior of TSFMs and their applicability to real-world problems. The authors should also investigate the impact of different data preprocessing techniques, such as normalization and feature scaling, on the scaling behavior of TSFMs in multivariate settings.

In addition to expanding the experimental scope to multivariate time series, the authors should also investigate the impact of different forecasting horizons on the scaling behavior of TSFMs. This would involve conducting experiments with varying forecasting horizons, both short-term and long-term, and analyzing how the model size and training compute requirements change as the forecasting horizon increases or decreases. The authors should also explore the use of techniques such as time series decomposition to handle different forecasting horizons. For example, the authors could investigate whether models trained on longer sequences are more effective for long-term forecasting, or whether models trained on shorter sequences are more effective for short-term forecasting. This analysis would provide a more complete picture of the scaling behavior of TSFMs and their applicability to different forecasting tasks. The authors should also consider the use of ensemble methods to combine the predictions of models trained on different forecasting horizons.

Finally, the paper should provide a more detailed discussion on the practical implications of the observed scaling laws for real-world deployment of TSFMs. This would involve providing concrete guidance on how to choose the appropriate model size and training compute based on specific application requirements and available resources. The authors should include a discussion on the trade-offs between model size, computational cost, and performance, and how these trade-offs should be managed in practice. For example, the authors could provide a cost-benefit analysis of different model sizes and training compute requirements, considering the specific needs of different applications. The authors should also discuss the limitations of the observed scaling laws and the potential for future research to address these limitations. This would help to ensure that the findings of the paper are relevant and applicable to real-world scenarios.

### Questions

- How would the scaling laws and model performance differ in multivariate time series forecasting tasks?
- How does the model size and training compute requirements change as the forecasting horizon increases or decreases?

### Rating

5

### Confidence

4

**********
