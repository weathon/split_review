### Summary

The paper introduces the TDTransformer, a transformer-based model designed to improve performance on tabular data. The authors identify two main challenges in applying transformers to tabular data: the heterogeneity of data types and the difficulty in interpreting numerical values. To address these issues, the TDTransformer uses distinct embedding processes for different column types (categorical, numerical, and binary) and aligns them in a common embedding space. Additionally, the model employs piecewise linear encoding (PLE) to enhance the representation of numerical values. The authors evaluate the TDTransformer on 76 real-world tabular classification datasets from the OpenML benchmark, demonstrating its superiority over existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The paper addresses a critical gap in the application of transformer models to tabular data, which is a significant area in machine learning.
3. The authors provide a thorough experimental evaluation on a large number of real-world datasets, which strengthens the validity of their findings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed method compared to existing approaches. This is important for understanding the practical applicability of the TDTransformer, especially in resource-constrained environments. Specifically, the paper lacks a breakdown of the time and space complexity for both training and inference phases, making it difficult to assess the scalability of the method. For instance, how does the complexity scale with the number of features, the number of unique categories in categorical features, and the size of the dataset? A detailed analysis should include the number of parameters, FLOPs, and memory requirements.
2. The paper does not discuss the limitations of the proposed method or potential areas for future research. This could help readers understand the scope of the method and identify potential avenues for improvement. For example, the paper does not address how the method performs on datasets with a very high number of features or with highly imbalanced class distributions. It also does not discuss the sensitivity of the method to hyperparameter settings or the potential for overfitting on small datasets.

### Suggestions

The paper would benefit from a more thorough analysis of the computational complexity of the TDTransformer. The authors should provide a detailed breakdown of the time and space complexity for both training and inference, including the number of parameters, FLOPs, and memory requirements. This analysis should consider how the complexity scales with the number of features, the number of unique categories in categorical features, and the size of the dataset. Furthermore, it would be beneficial to compare the computational cost of the TDTransformer with that of the baseline methods used in the experiments. This would provide a clearer understanding of the practical trade-offs between performance and computational resources. For example, the authors could include a table that shows the training time and memory usage for each method on a subset of the datasets used in the experiments. This would help readers assess the feasibility of using the TDTransformer in different scenarios.

Additionally, the paper should include a more comprehensive discussion of the limitations of the proposed method and potential areas for future research. The authors should address how the method performs on datasets with a very high number of features or with highly imbalanced class distributions. They should also discuss the sensitivity of the method to hyperparameter settings and the potential for overfitting on small datasets. It would be helpful to include an analysis of the performance of the TDTransformer on datasets with varying characteristics, such as the number of features, the number of instances, and the class distribution. This would provide a more complete picture of the strengths and weaknesses of the method. Furthermore, the authors should discuss potential avenues for future research, such as exploring different encoding techniques for numerical features or developing methods to handle high-cardinality categorical features more efficiently.

Finally, the paper should provide more details on the hyperparameter settings used in the experiments. While the authors mention that they used the same hyperparameter settings for all datasets, they do not provide the specific values used. This makes it difficult to reproduce the results and to assess the sensitivity of the method to different hyperparameter settings. The authors should include a table that lists all the hyperparameters used in the experiments, along with their values. They should also discuss how they selected these hyperparameters and whether they performed any hyperparameter tuning. This would improve the reproducibility of the results and allow other researchers to build upon this work.

### Questions

1. Could the authors provide more details on the computational complexity of the TDTransformer compared to existing methods?
2. How does the TDTransformer perform on datasets with a very high number of features or with highly imbalanced class distributions?
3. Are there any specific types of datasets or tasks where the TDTransformer is expected to underperform compared to existing methods?

### Rating

6

### Confidence

4

**********
