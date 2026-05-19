### Summary

This paper studies the problem of interaction quantification in a semi-supervised setting with unlabeled multimodal data. The authors propose a method to estimate the information shared between modalities, and validate their method on both synthetic and real-world datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The problem of interaction quantification is important and interesting.
2. The paper is well-written and easy to follow.
3. The proposed method is novel and interesting.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not very practical. It requires training a classifier for each modality, which can be time-consuming and computationally expensive, especially for high-dimensional data. The paper does not provide a clear analysis of the computational complexity of the proposed method, making it difficult to assess its scalability.
2. The experiments are not very comprehensive. The paper only considers a limited number of datasets and does not explore the performance of the proposed method under different experimental settings, such as varying the amount of labeled and unlabeled data. The lack of ablation studies makes it difficult to understand the contribution of each component of the proposed method.

### Suggestions

The paper should provide a more detailed analysis of the computational complexity of the proposed method. Specifically, the authors should analyze the time and space complexity of training the classifiers for each modality and the subsequent interaction quantification. It would be beneficial to compare the computational cost of the proposed method with existing approaches for interaction quantification. Furthermore, the authors should discuss the potential for parallelization of the proposed method to improve its scalability. The paper should also include a discussion of the memory requirements of the proposed method, especially when dealing with high-dimensional data. For example, the authors could provide a table showing the training time and memory usage for different dataset sizes and dimensionalities.

To improve the comprehensiveness of the experiments, the authors should conduct more extensive experiments on a wider range of datasets. It would be beneficial to include datasets with varying characteristics, such as different modalities, data sizes, and noise levels. The authors should also explore the performance of the proposed method under different experimental settings, such as varying the amount of labeled and unlabeled data. This would help to understand the robustness and generalizability of the proposed method. Furthermore, the authors should conduct ablation studies to evaluate the contribution of each component of the proposed method. For example, they could evaluate the performance of the method with and without the classifier training step, or with different choices of classifiers. This would help to identify the key factors that contribute to the performance of the proposed method. The authors should also consider using a more diverse set of evaluation metrics to assess the performance of the method.

Finally, the paper should provide a more detailed discussion of the limitations of the proposed method. The authors should discuss the assumptions made by the method and the potential impact of these assumptions on the results. For example, the method assumes that the classifiers are accurate, but it does not provide any analysis of the impact of classifier errors on the interaction quantification. The authors should also discuss the potential for bias in the estimated interactions due to the choice of classifiers. A thorough discussion of these limitations would help to provide a more balanced and realistic assessment of the proposed method. The authors should also consider comparing their method to other existing methods for interaction quantification, highlighting the advantages and disadvantages of their approach.

### Questions

See the weakness

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
