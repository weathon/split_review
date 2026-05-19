# B4OaA0aJ4Z — Meta Review

- Model: DeepReviewer 7B
- Decision: Reject
- Rating: 6.25
- Soundness: 2.75
- Presentation: 3.0
- Contribution: 2.75

## Summary

This paper introduces FoundTS, a benchmark designed to evaluate the performance of foundation models in time series forecasting (TSF). The authors address a critical gap in the field by providing a comprehensive evaluation framework that includes ten datasets from diverse domains and assesses models under zero-shot, few-shot, and full-shot learning scenarios. The core contribution of this work lies in its systematic approach to evaluating various foundation models, both LLM-based and time-series pre-trained, against traditional time series models. The methodology involves standardizing data splitting and evaluation metrics across different settings, ensuring a fair comparison. The empirical findings highlight the strengths and weaknesses of current foundation models, demonstrating their potential in data-scarce scenarios but also revealing their limitations in fully utilizing data. The paper's significance is underscored by its potential to guide future model development and improve time series forecasting performance. However, the paper's practical utility is somewhat limited by the absence of a detailed analysis of computational costs, hyperparameter sensitivity, and performance on specific data characteristics, which are crucial for real-world applications.

## Strengths

The paper is well-structured and clearly written, making it easy to follow and understand. The authors provide a thorough comparison of foundation models across various datasets and settings, offering valuable insights into their strengths and weaknesses. One of the key strengths of FoundTS is its comprehensive evaluation of different types of foundation models, including LLM-based and time-series pre-trained models, and traditional time series models. This comparison is essential for the community to understand the relative performance of these models and to guide future model development. The inclusion of a diverse set of datasets from various domains, such as electricity consumption, traffic, and economic indicators, ensures that the benchmark is robust and applicable to a wide range of real-world scenarios. The paper also provides a detailed analysis of the performance of these models under different conditions, which is crucial for understanding their practical utility. The authors' efforts to standardize data splitting and evaluation metrics across different settings are commendable, as they ensure a fair and consistent comparison. Overall, the paper makes a significant contribution to the field by providing a much-needed benchmark for evaluating foundation models in time series forecasting.

## Weaknesses

Despite its strengths, the paper has several limitations that need to be addressed to enhance its practical utility and robustness. One of the most significant concerns is the lack of a detailed analysis of the computational costs and efficiency of the foundation models. While the paper mentions the number of parameters for some models in Table 1, it fails to provide any metrics such as training time, inference time, memory usage, and energy consumption. This omission is critical because computational efficiency is a major factor in the practical applicability of models, especially in resource-constrained environments. For instance, the paper does not discuss how the computational requirements of these models scale with the length of the time series or the number of variables, which is essential for understanding their real-world deployment. The absence of this analysis limits the paper's ability to provide a complete picture of the models' practical utility (High confidence, supported by the lack of computational metrics in the

## Suggestions

To address the identified limitations and enhance the practical utility of FoundTS, I have several concrete recommendations. First, the authors should conduct a detailed analysis of the computational costs and efficiency of the foundation models. This should include metrics such as training time, inference time, memory usage, and energy consumption for each model. The analysis should also explore how these metrics scale with the length of the time series and the number of variables, providing a more comprehensive understanding of the models' practical applicability. Additionally, the authors should consider including the hardware and software environment used for these experiments, as this can significantly affect computational performance. This level of detail is crucial for practitioners to make informed decisions about model deployment.

Second, the paper should delve deeper into the limitations of the foundation models, particularly their sensitivity to hyperparameter settings. The authors should investigate how different hyperparameters, such as learning rate, batch size, and the number of layers, affect the performance of these models across various datasets. A sensitivity analysis, perhaps using techniques like Sobol indices, could quantify the impact of each hyperparameter on the model's performance. Furthermore, the paper should analyze the models' performance on specific types of time series data, such as those with strong seasonality, trend, or noise. This analysis should include a discussion of the types of time series data for which the foundation models are most suitable and those for which they may not be appropriate. For example, it would be useful to know if the models perform well on datasets with long-range dependencies or if they struggle with datasets that have high levels of noise or missing data.

Third, the paper should include a more comprehensive comparison with traditional time series models. While the authors mention ARIMA and LSTM, a more detailed comparison, including a discussion of the strengths and weaknesses of each model, would be beneficial. This comparison should not only focus on performance metrics but also consider the interpretability of the models. For instance, it would be useful to know if the foundation models are more robust to overfitting or if they are more sensitive to hyperparameter tuning. The authors should also discuss the computational cost and efficiency of the traditional models compared to the foundation models. This would provide a more complete picture of the trade-offs between the different approaches and help users choose the most appropriate model for their specific needs. The inclusion of more advanced traditional models, such as state-space models or gradient boosting methods, would further strengthen the evaluation.

Fourth, the authors should provide a more thorough discussion of the results, focusing on the performance differences between foundation models and traditional models. This analysis should include a detailed discussion of the potential reasons for these differences, such as the inductive biases of the models, their ability to generalize to unseen data, and their computational efficiency. The authors should also discuss the limitations of their study and suggest directions for future research. For example, they could explore the performance of foundation models on more diverse datasets or investigate the impact of different training strategies on their performance. This would provide a more complete and nuanced understanding of the capabilities and limitations of foundation models for time series forecasting.

Finally, the authors should consider including a more detailed description of the experimental setup, including specific hyperparameters and training procedures for each model. This should include the optimization algorithms, learning rates, batch sizes, and any data preprocessing steps. The authors should also specify the hardware and software environment used for the experiments. This level of detail is crucial for ensuring the reproducibility of the results and allowing other researchers to build upon their work. The inclusion of ablation studies to analyze the impact of different hyperparameters on the performance of the foundation models would also be beneficial.

## Questions

1. How do the foundation models perform on datasets with varying levels of noise, seasonality, or trend? A detailed analysis of performance based on these characteristics would provide valuable insights into the models' strengths and weaknesses.

2. What is the computational cost and efficiency of the foundation models compared to traditional time-series models like ARIMA and LSTM? This comparison should include metrics such as training time, inference time, memory usage, and energy consumption, and should be conducted across different datasets and settings.

3. How sensitive are the foundation models to hyperparameter settings, and what are the best practices for tuning these models? The authors should provide a sensitivity analysis using techniques like Sobol indices and discuss the optimal settings for different types of time series data.

4. How do the foundation models perform in real-world applications, and what are the challenges in deploying them in practical settings? The authors should include experiments or analysis that focus on real-world scenarios and discuss the practical implications of their findings.

5. How do the foundation models handle specific types of time series data, such as those with long-range dependencies or high levels of noise? The authors should provide a detailed analysis of the models' performance on these datasets and discuss their limitations in such scenarios.

## Full Content

## Summary:

This paper introduces FoundTS, a benchmark designed to evaluate the performance of foundation models in time series forecasting (TSF). The authors address a critical gap in the field by providing a comprehensive evaluation framework that includes ten datasets from diverse domains and assesses models under zero-shot, few-shot, and full-shot learning scenarios. The core contribution of this work lies in its systematic approach to evaluating various foundation models, both LLM-based and time-series pre-trained, against traditional time series models. The methodology involves standardizing data splitting and evaluation metrics across different settings, ensuring a fair comparison. The empirical findings highlight the strengths and weaknesses of current foundation models, demonstrating their potential in data-scarce scenarios but also revealing their limitations in fully utilizing data. The paper's significance is underscored by its potential to guide future model development and improve time series forecasting performance. However, the paper's practical utility is somewhat limited by the absence of a detailed analysis of computational costs, hyperparameter sensitivity, and performance on specific data characteristics, which are crucial for real-world applications.


## Soundness:

2.75


## Presentation:

3.0


## Contribution:

2.75


## Strengths:

The paper is well-structured and clearly written, making it easy to follow and understand. The authors provide a thorough comparison of foundation models across various datasets and settings, offering valuable insights into their strengths and weaknesses. One of the key strengths of FoundTS is its comprehensive evaluation of different types of foundation models, including LLM-based and time-series pre-trained models, and traditional time series models. This comparison is essential for the community to understand the relative performance of these models and to guide future model development. The inclusion of a diverse set of datasets from various domains, such as electricity consumption, traffic, and economic indicators, ensures that the benchmark is robust and applicable to a wide range of real-world scenarios. The paper also provides a detailed analysis of the performance of these models under different conditions, which is crucial for understanding their practical utility. The authors' efforts to standardize data splitting and evaluation metrics across different settings are commendable, as they ensure a fair and consistent comparison. Overall, the paper makes a significant contribution to the field by providing a much-needed benchmark for evaluating foundation models in time series forecasting.


## Weaknesses:

Despite its strengths, the paper has several limitations that need to be addressed to enhance its practical utility and robustness. One of the most significant concerns is the lack of a detailed analysis of the computational costs and efficiency of the foundation models. While the paper mentions the number of parameters for some models in Table 1, it fails to provide any metrics such as training time, inference time, memory usage, and energy consumption. This omission is critical because computational efficiency is a major factor in the practical applicability of models, especially in resource-constrained environments. For instance, the paper does not discuss how the computational requirements of these models scale with the length of the time series or the number of variables, which is essential for understanding their real-world deployment. The absence of this analysis limits the paper's ability to provide a complete picture of the models' practical utility (High confidence, supported by the lack of computational metrics in the 


## Suggestions:

To address the identified limitations and enhance the practical utility of FoundTS, I have several concrete recommendations. First, the authors should conduct a detailed analysis of the computational costs and efficiency of the foundation models. This should include metrics such as training time, inference time, memory usage, and energy consumption for each model. The analysis should also explore how these metrics scale with the length of the time series and the number of variables, providing a more comprehensive understanding of the models' practical applicability. Additionally, the authors should consider including the hardware and software environment used for these experiments, as this can significantly affect computational performance. This level of detail is crucial for practitioners to make informed decisions about model deployment.

Second, the paper should delve deeper into the limitations of the foundation models, particularly their sensitivity to hyperparameter settings. The authors should investigate how different hyperparameters, such as learning rate, batch size, and the number of layers, affect the performance of these models across various datasets. A sensitivity analysis, perhaps using techniques like Sobol indices, could quantify the impact of each hyperparameter on the model's performance. Furthermore, the paper should analyze the models' performance on specific types of time series data, such as those with strong seasonality, trend, or noise. This analysis should include a discussion of the types of time series data for which the foundation models are most suitable and those for which they may not be appropriate. For example, it would be useful to know if the models perform well on datasets with long-range dependencies or if they struggle with datasets that have high levels of noise or missing data.

Third, the paper should include a more comprehensive comparison with traditional time series models. While the authors mention ARIMA and LSTM, a more detailed comparison, including a discussion of the strengths and weaknesses of each model, would be beneficial. This comparison should not only focus on performance metrics but also consider the interpretability of the models. For instance, it would be useful to know if the foundation models are more robust to overfitting or if they are more sensitive to hyperparameter tuning. The authors should also discuss the computational cost and efficiency of the traditional models compared to the foundation models. This would provide a more complete picture of the trade-offs between the different approaches and help users choose the most appropriate model for their specific needs. The inclusion of more advanced traditional models, such as state-space models or gradient boosting methods, would further strengthen the evaluation.

Fourth, the authors should provide a more thorough discussion of the results, focusing on the performance differences between foundation models and traditional models. This analysis should include a detailed discussion of the potential reasons for these differences, such as the inductive biases of the models, their ability to generalize to unseen data, and their computational efficiency. The authors should also discuss the limitations of their study and suggest directions for future research. For example, they could explore the performance of foundation models on more diverse datasets or investigate the impact of different training strategies on their performance. This would provide a more complete and nuanced understanding of the capabilities and limitations of foundation models for time series forecasting.

Finally, the authors should consider including a more detailed description of the experimental setup, including specific hyperparameters and training procedures for each model. This should include the optimization algorithms, learning rates, batch sizes, and any data preprocessing steps. The authors should also specify the hardware and software environment used for the experiments. This level of detail is crucial for ensuring the reproducibility of the results and allowing other researchers to build upon their work. The inclusion of ablation studies to analyze the impact of different hyperparameters on the performance of the foundation models would also be beneficial.


## Questions:

1. How do the foundation models perform on datasets with varying levels of noise, seasonality, or trend? A detailed analysis of performance based on these characteristics would provide valuable insights into the models' strengths and weaknesses.

2. What is the computational cost and efficiency of the foundation models compared to traditional time-series models like ARIMA and LSTM? This comparison should include metrics such as training time, inference time, memory usage, and energy consumption, and should be conducted across different datasets and settings.

3. How sensitive are the foundation models to hyperparameter settings, and what are the best practices for tuning these models? The authors should provide a sensitivity analysis using techniques like Sobol indices and discuss the optimal settings for different types of time series data.

4. How do the foundation models perform in real-world applications, and what are the challenges in deploying them in practical settings? The authors should include experiments or analysis that focus on real-world scenarios and discuss the practical implications of their findings.

5. How do the foundation models handle specific types of time series data, such as those with long-range dependencies or high levels of noise? The authors should provide a detailed analysis of the models' performance on these datasets and discuss their limitations in such scenarios.


## Rating:

6.25


## Confidence:

3.5


## Decision:

Reject
