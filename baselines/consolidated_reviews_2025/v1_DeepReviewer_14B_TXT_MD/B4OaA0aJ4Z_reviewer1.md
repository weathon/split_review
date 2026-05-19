### Summary

This paper presents a benchmark for evaluating foundation models in time series forecasting. The benchmark covers different types of models, including large language models and pre-trained time series models. It also includes various forecasting strategies, such as zero-shot, few-shot, and full-shot learning. The authors provide a standardized evaluation pipeline that includes dataset splitting, loading, normalization, and sampling. The paper reports extensive evaluations of foundation models across diverse datasets, highlighting their strengths, limitations, and potential directions for future model design.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

The paper is easy to read and well-organized. It provides a comprehensive overview of existing time series foundation models and evaluates them across various datasets and forecasting strategies. The authors also offer insights into the practical aspects of using foundation models for time series forecasting, such as data sampling and normalization. The paper's contributions are significant, as it provides a valuable resource for researchers and practitioners working on time series forecasting with foundation models.

### Weaknesses

#### Some Related Works


#### comment

While the paper provides a comprehensive benchmark for evaluating foundation models in time series forecasting, it has some limitations. The paper primarily focuses on quantitative analysis and does not delve deeply into the qualitative aspects of the models' performance. Additionally, the benchmark could be expanded to include a wider range of datasets and evaluation metrics. Furthermore, the paper could benefit from more in-depth comparisons between different foundation models and a more detailed discussion of the trade-offs between them. There is a lack of novelty in this paper. It is more like a summary of the existing LLM and TS foundation models without bringing new insights to the TS forecasting community.

### Suggestions

The paper would benefit from a more thorough qualitative analysis of the foundation models' behavior. For instance, the authors could investigate the types of time series patterns that each model is able to capture effectively, and conversely, the types of patterns that pose challenges. This could involve analyzing the models' predictions on specific data subsets, such as those with high seasonality, trend, or noise, and visualizing the prediction errors to identify systematic biases. Furthermore, the authors could explore the models' sensitivity to different data preprocessing techniques, such as normalization or detrending, and how these choices impact the final forecasting performance. Such an analysis would provide a deeper understanding of the models' strengths and weaknesses beyond aggregate metrics.

To enhance the benchmark, the authors should consider incorporating a more diverse set of evaluation metrics that are tailored to specific forecasting tasks. For example, in addition to standard metrics like MAE and RMSE, metrics such as the Mean Absolute Scaled Error (MASE) or the Symmetric Mean Absolute Percentage Error (SMAPE) could be included to assess the models' performance in different scenarios. Furthermore, the benchmark could be expanded to include datasets with varying characteristics, such as different lengths of time series, varying levels of noise, and different types of temporal dependencies. This would provide a more comprehensive evaluation of the models' generalizability and robustness. The inclusion of time series classification tasks would also be valuable, as it would allow for a more holistic assessment of the models' capabilities.

Finally, the paper should include a more detailed discussion of the trade-offs between different foundation models. This should go beyond simply reporting the performance metrics and delve into the computational costs, memory requirements, and training time associated with each model. For example, the authors could compare the number of parameters, the training time, and the inference speed of different models, and discuss how these factors influence the choice of model for specific applications. Furthermore, the authors could explore the impact of different pre-training strategies on the models' performance and efficiency. This would provide valuable insights for practitioners who are considering using foundation models for time series forecasting.

### Questions

1. How do you ensure the reproducibility of the results across different foundation models and datasets? Are there any challenges in maintaining consistency in the evaluation process?
2. Can you elaborate on the practical implications of your findings for real-world time series forecasting applications? How can practitioners use your benchmark to select the most appropriate foundation model for their specific needs?
3. What are the computational costs associated with evaluating foundation models using your benchmark? How scalable is your approach to larger datasets and more complex models?
4. How do you plan to maintain and update the benchmark as new foundation models and time series forecasting techniques emerge?
5. Can you discuss any potential biases in your evaluation process or in the datasets used? How might these biases affect the conclusions drawn from your benchmark?

### Rating

5

### Confidence

4

**********
