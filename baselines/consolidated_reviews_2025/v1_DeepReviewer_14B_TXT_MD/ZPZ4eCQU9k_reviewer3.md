### Summary

The paper introduces a novel time series forecasting model called xLSTM-Mixer, which combines linear forecasting with xLSTM blocks to capture complex temporal and multivariate dependencies. The model employs a multi-stage approach that includes time mixing, joint mixing of time and variate information, and view mixing to reconcile different forecast perspectives. The authors demonstrate the model's superior long-term forecasting performance across various benchmarks and provide an extensive ablation study to analyze the contributions of individual components. The work contributes to the resurgence of recurrent models in time series forecasting and offers a robust framework for multivariate time series analysis.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. **Novel Architecture**: The paper introduces a unique architecture that combines linear forecasting with xLSTM blocks, effectively capturing complex temporal and multivariate dependencies. This approach is innovative and addresses the limitations of existing models.

2. **Comprehensive Evaluation**: The authors conduct extensive experiments across various benchmarks, demonstrating the model's superior long-term forecasting performance. The ablation study provides valuable insights into the contributions of individual components, strengthening the paper's claims.

3. **Theoretical Justification**: The paper provides a solid theoretical foundation for the proposed model, explaining the rationale behind each component and its contribution to the overall performance. This enhances the paper's credibility and understanding.

4. **Practical Implications**: The model's ability to handle multivariate time series data makes it highly relevant for real-world applications. The paper discusses the practical implications of the model, highlighting its potential impact on various industries.

5. **Robustness and Generalizability**: The paper demonstrates the model's robustness to varying hyperparameter settings and its ability to perform well across different datasets. This indicates the model's generalizability and potential for widespread adoption.

### Weaknesses

#### Some Related Works


#### comment

1. **Computational Complexity**: The paper does not adequately address the computational complexity of the proposed model. Given the multi-stage approach and the use of xLSTM blocks, it is crucial to understand the computational cost, especially when scaling to larger datasets or longer time series. A detailed analysis of the time and memory requirements, including a breakdown of the costs associated with each stage of the model, is missing. This makes it difficult to assess the practical feasibility of the model in resource-constrained environments.

2. **Sensitivity to Hyperparameters**: While the paper claims robustness to varying hyperparameter settings, it lacks a detailed analysis of how sensitive the model's performance is to different hyperparameter choices. The paper should include a more granular analysis, showing how performance varies across a range of values for key hyperparameters, such as the number of layers, hidden dimensions, and learning rates. This would provide a more complete picture of the model's stability and guide practitioners in tuning the model for specific applications.

3. **Comparison with State-of-the-Art**: Although the paper compares the proposed model with several baselines, it could benefit from a more direct comparison with the most recent state-of-the-art models in time series forecasting. The current comparison does not fully contextualize the performance of xLSTM-Mixer within the latest advancements in the field. A more thorough comparison, including models that utilize attention mechanisms or other advanced techniques, would be beneficial.

4. **Interpretability of Results**: The paper focuses on the quantitative performance of the model but does not provide much insight into the interpretability of the results. Understanding how the model makes its predictions, especially given the complex architecture, is crucial for building trust and for practical applications. The paper should include an analysis of the learned representations and how they contribute to the final forecast.

5. **Generalization to Other Domains**: The paper primarily focuses on time series forecasting. It would be beneficial to explore the model's potential for generalization to other domains, such as anomaly detection or classification. The paper should discuss the potential challenges and adaptations required for applying the model to these tasks.

### Suggestions

To address the computational complexity concerns, the authors should provide a detailed analysis of the time and memory requirements of the xLSTM-Mixer model. This analysis should include a breakdown of the computational cost associated with each stage of the model, such as the linear forecasting, xLSTM blocks, and view mixing. Furthermore, the authors should compare the computational cost of xLSTM-Mixer with other state-of-the-art models, providing a clear understanding of the trade-offs between performance and computational resources. This analysis should also consider the impact of different hyperparameter settings on the computational cost, allowing practitioners to make informed decisions about model selection and configuration. For example, the authors could provide a table showing the training time and memory usage for different model sizes and datasets.

To improve the analysis of hyperparameter sensitivity, the authors should conduct a more granular analysis of how the model's performance varies across a range of values for key hyperparameters. This analysis should include not only the final performance metrics but also the training dynamics, such as convergence speed and stability. The authors should also investigate the interaction between different hyperparameters and identify the optimal ranges for each parameter. This could be presented as a series of plots showing the performance of the model as a function of different hyperparameter values. Furthermore, the authors should provide guidelines for selecting appropriate hyperparameter values based on the characteristics of the dataset and the desired performance trade-offs. This would help practitioners to effectively tune the model for their specific applications.

To enhance the comparison with state-of-the-art models, the authors should include a more direct comparison with recent models that utilize attention mechanisms or other advanced techniques. This comparison should not only focus on the final performance metrics but also on other aspects, such as computational cost, interpretability, and robustness. The authors should also discuss the limitations of the proposed model compared to these state-of-the-art methods, providing a balanced view of the model's strengths and weaknesses. This would help readers to better understand the position of xLSTM-Mixer within the broader landscape of time series forecasting models. Additionally, the authors should explore the potential for combining the strengths of xLSTM-Mixer with other approaches, such as attention mechanisms, to further improve performance.

### Questions

1. **Computational Cost Analysis**: Could the authors provide a detailed analysis of the computational complexity of the xLSTM-Mixer model? This would help in understanding the practical feasibility of the model, especially for large-scale applications.

2. **Hyperparameter Sensitivity**: How sensitive is the model's performance to different hyperparameter settings? A detailed analysis would provide insights into the model's stability and guide practitioners in tuning the model for specific applications.

3. **Comparison with Recent Models**: How does xLSTM-Mixer compare with the most recent state-of-the-art models in time series forecasting? A direct comparison would help in contextualizing the performance of the proposed model.

4. **Interpretability of Forecasts**: Can the authors provide more insights into the interpretability of the model's forecasts? Understanding how the model makes its predictions is crucial for building trust and for practical applications.

5. **Generalization to Other Tasks**: What is the potential for generalizing the xLSTM-Mixer model to other time series tasks, such as anomaly detection or classification? This would broaden the impact of the proposed model.

### Rating

6

### Confidence

3

**********
