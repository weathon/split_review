### Summary

The paper proposes a novel method called ReMasker for imputing missing values in tabular data. The main idea is to extend the masked autoencoding framework to impute missing values by randomly re-masking another set of values and then training the model to predict the re-masked set. The authors evaluate ReMasker on 12 benchmark datasets under various missingness settings and compare it with 13 state-of-the-art imputation methods. The results show that ReMasker performs on par with or better than existing methods in terms of both imputation accuracy and utility.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple yet effective.
- The experiments are comprehensive and thorough.
- The paper provides a theoretical justification for the effectiveness of the method.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is quite similar to MissForest, which is a widely used method for imputing missing values in tabular data. The authors should provide a more detailed comparison between ReMasker and MissForest, highlighting the key differences and advantages of ReMasker. Specifically, the paper lacks a discussion on how ReMasker's approach to feature selection and weighting compares to MissForest's, which uses a Random Forest model with feature importance scores. A more thorough analysis of these differences is needed to justify the novelty of ReMasker.
- The authors claim that ReMasker learns missingness-invariant representations of tabular data. However, they do not provide any empirical evidence to support this claim. It would be helpful to include some visualization or analysis of the learned representations to show that they are indeed invariant to missingness patterns. For example, the authors could visualize the feature importance scores or the learned weights for different features under different missingness scenarios. Without such evidence, the claim of missingness-invariant representations remains unsubstantiated.
- The authors only evaluate ReMasker on tabular data. It would be interesting to see how ReMasker performs on other types of data, such as time series or graph data. The paper should discuss the potential challenges and limitations of applying ReMasker to other data types and suggest potential modifications that could be made to adapt it to these domains. For instance, the paper could explore how the masking strategy would need to be adapted for sequential data or graph-structured data.

### Suggestions

The paper would benefit from a more detailed analysis of the computational complexity of ReMasker compared to existing methods, particularly MissForest. While the authors mention that ReMasker is based on a transformer architecture, they do not provide a clear comparison of the computational cost in terms of training time and memory usage. A table summarizing the computational complexity of ReMasker and other methods would be helpful. Furthermore, the authors should discuss the scalability of ReMasker to large datasets with a high number of features and observations. This is an important consideration for practical applications of the method.

To strengthen the claim that ReMasker learns missingness-invariant representations, the authors should include a more rigorous analysis of the learned representations. This could involve visualizing the feature importance scores or the learned weights for different features under different missingness scenarios. For example, the authors could train the model on datasets with different missingness patterns and then analyze the feature weights assigned to each feature. If the model is truly learning missingness-invariant representations, the feature weights should be relatively stable across different missingness patterns. Another approach would be to perform an ablation study where the missingness patterns are systematically varied, and the impact on the learned representations is analyzed. This could involve creating synthetic datasets with controlled missingness patterns and then observing how the learned representations change. Such analysis would provide more concrete evidence for the claim that ReMasker learns representations that are invariant to missingness patterns.

Finally, the paper should discuss the potential of ReMasker for other data types beyond tabular data. While the authors acknowledge that the method is designed for tabular data, they should explore the challenges and limitations of applying it to other data types, such as time series or graph data. For time series data, the authors could discuss how the masking strategy would need to be adapted to capture temporal dependencies. For example, instead of masking individual features, the authors could consider masking sequences of time points. For graph data, the authors could explore how the masking strategy would need to be adapted to capture the relationships between nodes and edges. The paper should also discuss potential modifications that could be made to the ReMasker architecture to adapt it to these different data types. This would broaden the scope of the paper and make it more relevant to a wider audience.

### Questions

- How does ReMasker compare to MissForest in terms of computational cost and memory usage? It would be helpful to provide a more detailed analysis of the computational complexity of ReMasker and compare it to other methods.
- How does the performance of ReMasker vary with different masking ratios? The authors should provide a more detailed analysis of the impact of the masking ratio on the performance of ReMasker.
- How does ReMasker handle high-dimensional data? The authors should provide a more detailed analysis of the performance of ReMasker on high-dimensional datasets and discuss any potential challenges or limitations.

### Rating

6

### Confidence

4

**********
