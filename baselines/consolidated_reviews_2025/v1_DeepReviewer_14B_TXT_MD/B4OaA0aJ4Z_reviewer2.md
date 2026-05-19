### Summary

This paper introduces a new benchmark, FoundTS, for evaluating time series forecasting foundation models. FoundTS includes a variety of foundation models, such as large language models and pre-trained time series models, and supports different forecasting strategies like zero-shot, few-shot, and full-shot learning. The benchmark standardizes the evaluation process, including dataset splitting, loading, normalization, and sampling, to ensure fair comparisons. The authors conduct extensive evaluations on diverse datasets and provide insights into the strengths and limitations of existing foundation models, as well as directions for future model design.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. This paper is well-organized and easy to follow.
2. The benchmark includes a wide range of datasets from different domains, which allows for a more comprehensive evaluation of the models' generalization capabilities.
3. The benchmark supports multiple evaluation strategies, including zero-shot, few-shot, and full-shot learning, which provides a more complete picture of the models' performance under different data availability scenarios.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the foundation models, which is an important factor to consider when deploying these models in real-world applications.
2. The paper could benefit from a more in-depth discussion of the limitations of the current foundation models and potential directions for future research.
3. The paper does not explore the impact of different pre-training datasets on the performance of the foundation models, which could be an interesting area for future research.
4. The paper does not provide a detailed analysis of the sensitivity of the models to different hyperparameters, which is an important factor to consider when fine-tuning the models for specific tasks.
5. The paper does not explore the use of ensemble methods to combine the predictions of multiple foundation models, which could potentially improve the overall forecasting performance.

### Suggestions

The paper would benefit from a more thorough investigation into the computational demands of the evaluated foundation models. While the paper mentions the inclusion of various models, it lacks a detailed analysis of their training and inference time complexities, as well as memory requirements. This is crucial for practical applications, where resource constraints often dictate the feasibility of deploying a particular model. For instance, providing a breakdown of the FLOPs required for training and inference, along with the memory footprint of each model, would allow practitioners to make informed decisions about which models are suitable for their specific hardware and latency requirements. Furthermore, the paper should explore the trade-offs between model size, computational cost, and forecasting accuracy, which would provide valuable insights into the efficiency of different foundation models.

In addition to computational complexity, the paper should delve deeper into the limitations of current foundation models for time series forecasting. While the paper touches upon the performance of different models, it does not adequately discuss the specific scenarios where these models struggle. For example, it would be beneficial to analyze the performance of these models on time series with complex seasonality, high levels of noise, or non-stationary behavior. Furthermore, the paper should explore the potential reasons for these limitations, such as the inability of current models to capture long-range dependencies or the lack of robustness to outliers. This analysis would not only highlight the current shortcomings of foundation models but also provide valuable directions for future research. The discussion should also include the limitations of the benchmark itself, such as the types of datasets included and the evaluation metrics used, and how these choices might influence the conclusions drawn.

Finally, the paper should explore the impact of different pre-training datasets on the performance of the foundation models. The current study does not investigate how the choice of pre-training data affects the models' ability to generalize to different time series datasets. For example, it would be interesting to compare the performance of models pre-trained on datasets with different characteristics, such as those with varying levels of noise, seasonality, or length. This analysis would provide valuable insights into the importance of pre-training data selection and could guide future research on developing more robust and generalizable foundation models. Furthermore, the paper should investigate the sensitivity of the models to different hyperparameters, as this is a critical factor for practical applications. A detailed analysis of how different hyperparameters affect the models' performance would provide valuable guidance for practitioners who need to fine-tune these models for specific tasks.

### Questions

Please refer to the Weaknesses.

### Rating

6

### Confidence

4

**********
