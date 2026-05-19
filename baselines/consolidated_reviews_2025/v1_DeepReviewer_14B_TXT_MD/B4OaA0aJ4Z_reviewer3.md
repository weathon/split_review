### Summary

This paper introduces a benchmark for evaluating foundation models for time series forecasting. The benchmark includes various datasets, models, and evaluation strategies, and provides a standardized evaluation pipeline. The authors conduct extensive experiments and provide insights into the strengths and limitations of existing foundation models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The benchmark covers a wide range of datasets, models, and evaluation strategies, making it a comprehensive resource for researchers and practitioners.
3. The authors conduct extensive experiments and provide detailed analysis of the results, which adds credibility to their findings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not discuss the potential biases in the datasets used for evaluation, which could affect the generalizability of the results.
2. The paper could benefit from a more in-depth discussion of the limitations of the proposed benchmark and potential directions for future research.

### Suggestions

The paper should include a more thorough analysis of potential biases within the datasets used for evaluation. While the authors mention the diversity of the datasets, they do not delve into specific biases that might be present. For example, many time series datasets exhibit seasonality, trends, or other temporal patterns that could disproportionately favor certain model architectures or pre-training strategies. A detailed analysis should consider how these characteristics might influence the performance of different foundation models, and whether the benchmark adequately accounts for these variations. Furthermore, the paper should explore the impact of data quality issues, such as missing values or outliers, on the evaluation results. This analysis should not only identify potential biases but also propose methods to mitigate their impact, such as data augmentation or re-weighting techniques. This would significantly enhance the robustness and generalizability of the benchmark.

In addition to addressing dataset biases, the paper should provide a more comprehensive discussion of the limitations of the proposed benchmark. The current discussion is somewhat brief and does not fully explore the potential shortcomings of the evaluation framework. For example, the benchmark primarily focuses on forecasting tasks, but many foundation models are also capable of other time series tasks, such as classification, anomaly detection, or imputation. The paper should acknowledge this limitation and discuss how the benchmark could be extended to include these other tasks. Furthermore, the paper should address the computational cost of evaluating foundation models, which can be a significant barrier for many researchers. The authors should discuss the trade-offs between model complexity, computational resources, and evaluation time, and provide guidance on how to select the most appropriate models for evaluation. A more detailed discussion of these limitations would provide a more balanced and realistic assessment of the benchmark's capabilities.

Finally, the paper should explore potential directions for future research. While the authors mention some future directions, they could be more specific and actionable. For example, the paper could discuss the need for more robust evaluation metrics that are less sensitive to data biases. It could also explore the potential of using meta-learning techniques to adapt foundation models to new datasets and tasks. Furthermore, the paper could discuss the need for more efficient training methods that can reduce the computational cost of evaluating foundation models. By providing more concrete and actionable directions for future research, the paper could have a greater impact on the field.

### Questions

1. How does the proposed benchmark compare to existing benchmarks for time series forecasting?
2. What are the key differences between the proposed benchmark and other related work?
3. How does the proposed benchmark address the limitations of existing benchmarks?

### Rating

8

### Confidence

3

**********
