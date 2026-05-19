### Summary

This paper proposes a novel framework, CAUSE, for unsupervised semantic segmentation (USS). The authors introduce a causal perspective to address the challenge of determining the appropriate level of clustering for segmenting concepts. CAUSE utilizes a concept clusterbook as a mediator and employs concept-wise self-supervised learning to enhance pixel-level grouping. The framework achieves state-of-the-art performance in unsupervised semantic segmentation on various datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel perspective by applying causal inference to unsupervised semantic segmentation.
2. The concept clusterbook provides an explicit link between pre-trained features and concept-wise self-supervised learning.
3. The framework achieves state-of-the-art performance on various datasets, demonstrating its effectiveness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational complexity of the proposed framework. Specifically, the paper does not provide a breakdown of the time complexity for each stage of the CAUSE framework, such as the construction of the concept clusterbook, the causal adjustment, and the final segmentation. This makes it difficult to assess the practical scalability of the method, especially when dealing with high-resolution images or large datasets. Furthermore, the paper does not discuss the memory footprint of the model, which is crucial for deployment on resource-constrained devices.
2. The paper does not provide a comprehensive comparison with other state-of-the-art methods in terms of computational efficiency. While the paper claims state-of-the-art performance, it does not discuss the trade-offs between accuracy and computational cost compared to other unsupervised semantic segmentation methods. A detailed comparison of inference time and memory usage would be beneficial to understand the practical advantages and limitations of the proposed approach.
3. The paper lacks a detailed analysis of the sensitivity of the framework to hyperparameter settings. The paper mentions several hyperparameters, such as the number of concepts in the clusterbook, the relaxation parameters for positive and negative concept selection, and the parameters for the concept bank. However, it does not provide a systematic analysis of how these parameters affect the performance of the framework. It is unclear how the performance varies when these parameters are changed, and what are the optimal ranges for these parameters. This lack of sensitivity analysis makes it difficult to reproduce the results and to apply the method to new datasets.

### Suggestions

The paper should include a detailed analysis of the computational complexity of the proposed framework. This analysis should include a breakdown of the time complexity for each stage of the CAUSE framework, such as the construction of the concept clusterbook, the causal adjustment, and the final segmentation. The analysis should also consider the memory footprint of the model, which is crucial for deployment on resource-constrained devices. Furthermore, the paper should provide a comparison of the computational cost of the proposed method with other state-of-the-art unsupervised semantic segmentation methods. This comparison should include metrics such as inference time and memory usage, in addition to accuracy. This would provide a more complete picture of the practical advantages and limitations of the proposed approach.

To address the lack of sensitivity analysis, the paper should include a comprehensive study of how the performance of the framework varies with different hyperparameter settings. This study should include a systematic exploration of the parameter space, and it should identify the optimal ranges for each parameter. The analysis should also discuss the trade-offs between different parameter settings, and it should provide guidelines for selecting appropriate values for new datasets. For example, the paper could include a series of experiments where the number of concepts in the clusterbook is varied, and the impact on performance is measured. Similarly, the paper could explore the effect of different relaxation parameters for positive and negative concept selection. This analysis should be presented in a clear and concise manner, with visualizations such as plots and tables to illustrate the results.

Finally, the paper should provide more details on the implementation of the concept-wise self-supervised learning. Specifically, the paper should explain how the positive and negative concept features are selected, and how the concept bank is updated. The paper should also discuss the impact of the concept bank size on the performance of the framework. It would be beneficial to include ablation studies that explore the effect of different design choices, such as the size of the concept bank and the method for selecting positive and negative concept features. This would provide a better understanding of the inner workings of the proposed method and would help to identify potential areas for improvement.

### Questions

Please refer to the weakness part.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
