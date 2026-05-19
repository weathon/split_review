### Summary

This paper investigates the scaling laws of time series foundation models (TSFMs) and compares the performance of encoder-only and decoder-only Transformer architectures. The study evaluates model performance on both in-distribution (ID) and out-of-distribution (OOD) data, finding that model scaling follows a power-law relationship with improvements in OOD performance. Encoder-only models generally outperform decoder-only models, especially in OOD scenarios, though architectural improvements in decoder-only models do not translate to better OOD generalization.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper presents a comprehensive analysis of scaling laws for TSFMs, examining the impact of model size, compute budget, and dataset size on both ID and OOD performance. This systematic approach provides valuable insights into the scaling behavior of TSFMs.
2. The study compares encoder-only and decoder-only Transformer architectures, highlighting the superior scalability of encoder-only models in OOD scenarios. This comparison offers practical guidance for model selection in real-world applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's experimental setup is limited to univariate time series forecasting, which may not fully capture the complexities of multivariate time series data. The findings may not generalize to scenarios with multiple interdependent variables, where the relationships between variables can significantly impact model performance. Specifically, the absence of experiments involving multivariate time series limits the applicability of the conclusions to real-world datasets where multiple time series often exhibit complex correlations and dependencies. The paper should acknowledge this limitation and discuss how the observed scaling laws might differ in multivariate settings.
2. The paper does not explore the impact of different time series forecasting horizons on the scaling behavior of TSFMs. The scaling laws observed may vary for short-term and long-term forecasting tasks, which could affect the generalizability of the findings. The paper should investigate how the model size and training compute requirements change as the forecasting horizon increases or decreases. For instance, it is possible that larger models trained on longer sequences may not necessarily generalize well to shorter forecasting horizons, and vice versa. This aspect needs further investigation to ensure the robustness of the conclusions.
3. The paper lacks a detailed discussion on the practical implications of the observed scaling laws for real-world deployment of TSFMs. The findings may not directly translate to practical applications without further consideration of computational constraints and resource availability. The paper should provide concrete guidance on how to choose the appropriate model size and training compute based on specific application requirements and available resources. For example, it would be beneficial to include a discussion on the trade-offs between model size, computational cost, and performance, and how these trade-offs should be managed in practice.

### Suggestions

To enhance the paper's contribution, the authors should extend their experimental evaluation to include multivariate time series datasets. This would involve not only expanding the dataset size but also considering the unique challenges posed by multivariate data, such as the presence of complex interdependencies between variables. The authors should explore different methods for handling multivariate time series, such as using attention mechanisms that can capture cross-variable relationships or employing graph neural networks to model the dependencies between variables. Furthermore, the paper should analyze how the observed scaling laws differ in multivariate settings compared to univariate settings. This would provide a more comprehensive understanding of the scaling behavior of TSFMs and their applicability to real-world problems. The authors should also investigate the impact of different data preprocessing techniques, such as normalization and feature scaling, on the scaling behavior of TSFMs in multivariate settings.

In addition to expanding the experimental scope to multivariate time series, the authors should also investigate the impact of different forecasting horizons on the scaling behavior of TSFMs. This would involve conducting experiments with varying forecasting horizons, both short-term and long-term, and analyzing how the model size and training compute requirements change as the forecasting horizon increases or decreases. The authors should also explore the use of techniques such as time series decomposition to handle different forecasting horizons. For example, the authors could investigate whether models trained on longer sequences are more effective for long-term forecasting, or whether models trained on shorter sequences are more effective for short-term forecasting. This analysis would provide a more complete picture of the scaling behavior of TSFMs and their applicability to different forecasting tasks. The authors should also consider the use of ensemble methods to combine the predictions of models trained on different forecasting horizons.

Finally, the paper should provide a more detailed discussion on the practical implications of the observed scaling laws for real-world deployment of TSFMs. This would involve providing concrete guidance on how to choose the appropriate model size and training compute based on specific application requirements and available resources. The authors should include a discussion on the trade-offs between model size, computational cost, and performance, and how these trade-offs should be managed in practice. For example, the authors could provide a cost-benefit analysis of different model sizes and training compute requirements, considering the specific needs of different applications. The authors should also discuss the limitations of the observed scaling laws and the potential for future research to address these limitations. This would help to ensure that the findings of the paper are relevant and applicable to real-world scenarios.

### Questions

1. How would the scaling laws and model performance differ in multivariate time series forecasting tasks?
2. How does the model size and training compute requirements change as the forecasting horizon increases or decreases?

### Rating

5

### Confidence

4

**********
