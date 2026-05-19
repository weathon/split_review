### Summary

This paper introduces FoundTS, a benchmark designed to evaluate foundation models for time series forecasting (TSF). FoundTS includes ten datasets from diverse domains and assesses foundation models across zero-shot, few-shot, and full-shot settings. The authors standardize evaluation metrics and data splitting to ensure fair comparisons. The paper provides a comprehensive analysis of foundation models, highlighting their strengths and weaknesses, and offers insights for future model development in time series forecasting.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper is well-written and easy to follow.
2. The paper is well-motivated and addresses an important problem in the field of time series forecasting.
3. The paper provides a comprehensive analysis of foundation models, highlighting their strengths and weaknesses, and offers insights for future model development in time series forecasting.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not discuss the computational cost and efficiency of the foundation models, which is an important factor in practical applications.
2. The paper does not provide a detailed analysis of the limitations of the foundation models, such as their sensitivity to hyperparameters or their performance on specific types of time series data.
3. The paper does not compare the performance of the foundation models with traditional time series models, such as ARIMA or LSTM, which could provide a more comprehensive evaluation of their strengths and weaknesses.

### Suggestions

The paper should include a more detailed analysis of the computational resources required for training and deploying the foundation models. This should include metrics such as training time, inference time, memory usage, and energy consumption. A comparison of these metrics across different models would be valuable for practitioners to understand the trade-offs between model performance and computational cost. For example, the authors could provide a breakdown of the time required for pre-training versus fine-tuning for different models, along with the hardware specifications used for these experiments. Furthermore, the paper should explore the scalability of these models with respect to the length of the time series and the number of variables. This analysis should also consider the impact of different optimization algorithms and hardware configurations on the overall performance and efficiency of the models. Such a detailed analysis would provide a more complete picture of the practical applicability of these foundation models.

In addition to computational cost, the paper should delve deeper into the limitations of the foundation models, particularly their sensitivity to hyperparameter settings. The authors should investigate how different hyperparameters, such as learning rate, batch size, and the number of layers, affect the performance of these models across various datasets. A sensitivity analysis, perhaps using techniques like Sobol indices, could quantify the impact of each hyperparameter on the model's performance. Furthermore, the paper should analyze the models' performance on specific types of time series data, such as those with strong seasonality, trend, or noise. This analysis should include a discussion of the types of time series data for which the foundation models are most suitable and those for which they may not be appropriate. For example, it would be useful to know if the models perform well on datasets with long-range dependencies or if they struggle with datasets that have high levels of noise or missing data. This would help users understand the limitations of the models and make informed decisions about their applicability.

Finally, the paper should include a more comprehensive comparison with traditional time series models. While the authors mention ARIMA and LSTM, a more detailed comparison, including a discussion of the strengths and weaknesses of each model, would be beneficial. This comparison should not only focus on performance metrics but also consider the interpretability of the models. For instance, it would be useful to know if the foundation models are more robust to overfitting or if they are more sensitive to hyperparameter tuning. The paper should also discuss the computational cost and efficiency of the traditional models compared to the foundation models. This would provide a more complete picture of the trade-offs between the different approaches and help users choose the most appropriate model for their specific needs. The authors should also consider including more advanced traditional models, such as state-space models or gradient boosting methods, to provide a more comprehensive comparison.

### Questions

1. How do the foundation models perform on datasets with different characteristics, such as varying levels of noise, seasonality, or trend?
2. What is the computational cost and efficiency of the foundation models compared to traditional time series models?
3. How sensitive are the foundation models to hyperparameter settings, and what are the best practices for tuning these models?
4. How do the foundation models perform in real-world applications, and what are the challenges in deploying them in practical settings?

### Rating

8

### Confidence

3

**********
