### Summary

This paper studies the problem of label differential privacy (label DP) in deep learning. The authors propose a new family of label DP training algorithms called LabelDP-Pro, which leverages the power of the central model of DP and interleaves gradient projection operations with private stochastic gradient descent steps to improve the utility of the trained model while guaranteeing the privacy of the labels. The authors provide both theoretical and empirical results to support the effectiveness of their proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper studies a new family of label DP training algorithms and is well-written.
2. The proposed algorithm naturally leverages the power of the central model of DP. It interleaves gradient projection operations with private stochastic gradient descent steps in order to improve the utility of the trained model while guaranteeing the privacy of the labels.
3. The paper provides both theoretical and empirical results.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed algorithm naturally leverages the power of the central model of DP, meaning that the feature is public. This assumption may limit the applicability of the algorithm in scenarios where features are also sensitive or private. Specifically, the reliance on public features restricts the algorithm's use in settings where feature data itself requires privacy guarantees, such as in medical or financial datasets where both features and labels are sensitive. The paper does not explore the implications of this limitation or potential modifications to address it.
2. The algorithm's performance may depend on the choice of the projection operation and its parameters. The paper does not provide sufficient guidance on how to choose these parameters optimally, which could make it difficult to apply the algorithm in practice. The lack of a clear methodology for selecting the projection matrix and its associated parameters introduces a practical challenge. The paper should include a more detailed analysis of how different projection choices impact the algorithm's performance and provide recommendations for parameter selection based on dataset characteristics.
3. The proposed algorithm may not be suitable for all types of data or models. For example, it may not work well with small datasets or complex models. The paper lacks a detailed analysis of the algorithm's performance across different data modalities and model architectures, making it hard to assess its generalizability. The paper should include experiments on a wider range of datasets and models, including those with high dimensionality or complex dependencies, to better understand the limitations of the proposed approach. It is unclear how the algorithm would perform with highly structured data or with models that have very different loss landscapes.

### Suggestions

The paper should include a more thorough discussion on the limitations of the public feature assumption. While many label differential privacy (DP) works make this assumption, it is crucial to explicitly state the scenarios where this assumption does not hold and how that would impact the applicability of the proposed algorithm. Furthermore, the paper should explore the performance of the algorithm when the features are not completely public, for example, when they are differentially private or have some other form of noise. This would help to better understand the robustness of the algorithm and its potential for broader use cases. The authors should also consider adding experiments with different levels of feature privacy to show how the performance of the algorithm degrades as the features become less public. This would provide a more complete picture of the algorithm's practical limitations and potential for real-world applications.

To address the dependence on the projection operation, the paper should provide a more detailed analysis of how the choice of projection dimension and the method for determining the projection matrix affect the performance of the algorithm. The authors should explore different methods for selecting the projection matrix, such as random projections or projections based on the data distribution. They should also provide guidelines on how to choose the projection dimension based on the characteristics of the dataset and the model. A sensitivity analysis of the algorithm's performance with respect to these parameters would be very helpful for practitioners. Furthermore, the paper should discuss the computational cost of the projection operation and how it scales with the size of the dataset and the model. This would help to understand the practical feasibility of the proposed approach for large-scale applications.

Finally, the paper should include a more comprehensive evaluation of the algorithm's performance across different data modalities and model architectures. The authors should consider adding experiments with different types of data, such as text or graph data, and with different types of models, such as recurrent neural networks or graph neural networks. This would help to better understand the generalizability of the algorithm and its limitations. The paper should also discuss the performance of the algorithm with small datasets and complex models, and provide guidelines on how to adapt the algorithm to these scenarios. It would be beneficial to include a comparison with other label DP algorithms on a wider range of datasets and models to better demonstrate the advantages and disadvantages of the proposed approach. This would provide a more robust evaluation of the algorithm's effectiveness and its potential for practical use.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
