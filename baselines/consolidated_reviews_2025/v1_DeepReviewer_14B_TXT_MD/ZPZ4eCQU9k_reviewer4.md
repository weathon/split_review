### Summary

The paper introduces xLSTM-Mixer, a novel model designed for multivariate time series forecasting that effectively integrates temporal sequences, joint time-variate information, and multiple perspectives. The model begins with a linear forecast that is refined by xLSTM blocks, which are key to modeling the complex dynamics of challenging time series data. xLSTM-Mixer reconciles two distinct views to produce the final forecast, demonstrating superior long-term forecasting performance compared to recent state-of-the-art methods. The paper also provides a thorough model analysis, confirming the robustness and effectiveness of the approach. This work contributes to the resurgence of recurrent models in time series forecasting.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel architecture, xLSTM-Mixer, which combines linear forecasting with xLSTM blocks for multivariate time series forecasting. This approach is innovative and leverages the strengths of both linear and recurrent models.

2. The model's ability to reconcile two distinct views for the final forecast is a unique feature that enhances its forecasting accuracy and robustness.

3. The paper provides extensive experimental evaluations, demonstrating that xLSTM-Mixer outperforms recent state-of-the-art methods in long-term forecasting across various datasets.

4. The authors conduct a thorough ablation study to analyze the contributions of individual components of the model, providing valuable insights into its effectiveness.

5. The paper is well-structured and clearly written, making it accessible to readers with a background in time series forecasting and deep learning.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational efficiency of xLSTM-Mixer compared to other models. While the model's performance is evaluated extensively, understanding its computational requirements is crucial for practical applications, especially in resource-constrained environments. The paper should include a more thorough breakdown of the computational cost, including FLOPs, memory usage, and training/inference time, and compare these metrics against the baselines.

2. The robustness of xLSTM-Mixer to varying hyperparameter settings is not fully explored. While the authors mention that the model is robust, a more detailed sensitivity analysis of key hyperparameters, such as the number of layers, hidden dimensions, and learning rate, is needed to understand the model's stability and generalizability. The paper should include a systematic exploration of the hyperparameter space and report the performance variations across different settings.

3. The paper could benefit from a more in-depth discussion of the limitations of xLSTM-Mixer, particularly in scenarios where the number of variates is very large. The current discussion does not fully address the potential challenges in scaling the model to high-dimensional time series data, such as the increased computational cost and potential for overfitting. A more detailed analysis of the model's performance with increasing numbers of variates is needed.

4. The paper's focus is primarily on long-term forecasting, and it does not explore the performance of xLSTM-Mixer in short-term forecasting or other time series tasks such as classification or imputation. This limits the understanding of the model's versatility and potential applications in different contexts. The paper should include experiments on short-term forecasting and other time series tasks to provide a more comprehensive evaluation of the model's capabilities.

### Suggestions

To address the lack of computational efficiency analysis, the authors should include a detailed comparison of xLSTM-Mixer with other models in terms of FLOPs, memory usage, and training/inference time. This analysis should be performed on the same hardware and software configurations to ensure a fair comparison. Furthermore, the authors should provide a breakdown of the computational cost for each component of the xLSTM-Mixer model, such as the linear forecast, xLSTM blocks, and view reconciliation, to identify potential bottlenecks and areas for optimization. This would provide valuable insights into the practical applicability of the model, especially in resource-constrained environments. The authors should also consider reporting the energy consumption of the model, which is an important factor in sustainable AI research.

To improve the robustness analysis, the authors should conduct a more systematic exploration of the hyperparameter space. This should include a sensitivity analysis of key hyperparameters, such as the number of layers, hidden dimensions, learning rate, and batch size. The authors should report the performance variations across different hyperparameter settings and identify the optimal configurations for different datasets. Furthermore, the authors should investigate the impact of different initialization strategies on the model's performance and stability. This would provide a more comprehensive understanding of the model's robustness and generalizability. The authors should also consider using automated hyperparameter tuning techniques, such as Bayesian optimization, to find the optimal hyperparameter configurations.

To address the limitations of the model, the authors should include a more detailed analysis of the model's performance with increasing numbers of variates. This should include experiments on datasets with varying numbers of variates to understand the scalability of the model. Furthermore, the authors should investigate the potential for overfitting when the number of variates is very large and explore techniques to mitigate this issue, such as regularization or dimensionality reduction. The authors should also consider exploring the use of attention mechanisms to handle high-dimensional time series data more effectively. Finally, the authors should expand the scope of their experiments to include short-term forecasting and other time series tasks, such as classification and imputation, to provide a more comprehensive evaluation of the model's capabilities and versatility.

### Questions

1. Can the authors provide a more detailed analysis of the computational efficiency of xLSTM-Mixer compared to other models? This would help in understanding the practical applicability of the model, especially in resource-constrained environments.

2. How does xLSTM-Mixer perform in terms of robustness to varying hyperparameter settings? A detailed sensitivity analysis would provide insights into the model's stability and generalizability.

3. What are the limitations of xLSTM-Mixer when dealing with time series data that have missing values or are highly irregular? This information is crucial for understanding the model's applicability in real-world scenarios.

4. How does the model scale with the number of variates? Are there any specific challenges or limitations when the number of variates is very large?

5. Can the authors provide more insights into the performance of xLSTM-Mixer on short-term forecasting tasks? This would help in understanding the model's versatility and potential applications in different contexts.

### Rating

6

### Confidence

3

**********
