### Summary

This paper introduces a novel approach for tabular data learning by leveraging language models. The authors propose a Tabular Domain Transformer (TDTransformer) that addresses the challenges of tabular data heterogeneity and numerical value interpretation. The TDTransformer employs distinct embedding processes for different column types and uses piece-wise linear encoding for numerical values. The model is evaluated on 76 real-world tabular classification datasets from the OpenML benchmark, demonstrating significant improvements over state-of-the-art methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel approach to tabular data learning by adapting language models, which is a significant departure from traditional methods.
2. The use of distinct embedding processes for different column types and piece-wise linear encoding for numerical values are innovative techniques that address the specific challenges of tabular data.
3. The extensive experiments on 76 real-world datasets provide strong empirical evidence of the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential areas for future research.
2. The paper could provide more insights into the interpretability of the model and how it makes predictions.

### Suggestions

The paper should delve deeper into the limitations of the TDTransformer, particularly concerning its scalability and performance on extremely high-dimensional datasets. While the authors mention the use of piece-wise linear encoding (PLE) for numerical values, they should also discuss the potential computational overhead associated with this approach, especially when dealing with a large number of numerical features. Furthermore, the paper should explore the sensitivity of the model to hyperparameter tuning, such as the number of pieces in the PLE and the architecture of the transformer itself. A more thorough analysis of these aspects would provide a more complete picture of the method's practical applicability and limitations. Additionally, the authors should consider discussing the potential impact of data quality issues, such as missing values or outliers, on the performance of the TDTransformer, and how these issues might be addressed in future work.

To enhance the interpretability of the TDTransformer, the authors should explore techniques for visualizing the learned embeddings and attention weights. For example, they could investigate methods for projecting the high-dimensional embeddings into a lower-dimensional space for visualization, which could provide insights into how the model represents different column types and numerical values. Furthermore, the authors should consider developing methods for explaining the model's predictions at the instance level, such as by identifying the most influential features for a given prediction. This could involve techniques such as SHAP values or LIME, which are commonly used for explaining the predictions of complex models. The paper should also discuss the limitations of these interpretability techniques and how they might be improved in future work. A more detailed discussion of the model's decision-making process would greatly increase the practical value of the proposed method.

Finally, the paper should discuss the potential for extending the TDTransformer to handle more complex tabular data scenarios, such as datasets with hierarchical structures or time-series data. The current approach is primarily focused on static tabular data, and it is unclear how it would perform in more complex settings. The authors should also consider the potential for integrating the TDTransformer with other machine learning techniques, such as ensemble methods or reinforcement learning, to further improve its performance. A discussion of these potential extensions would provide a more comprehensive view of the method's potential and future research directions.

### Questions

1. How does the proposed method handle missing values or outliers in the data?
2. What are the computational requirements for training and inference with the TDTransformer?
3. How does the TDTransformer perform on datasets with a large number of columns or high cardinality categorical features?

### Rating

6

### Confidence

3

**********
