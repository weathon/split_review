### Summary

The authors introduce a framework called CAUSE (CAusal Unsupervised Semantic sEgmentation) which utilizes causal inference to improve unsupervised semantic segmentation. CAUSE constructs a concept clusterbook as a mediator to define clustering granularity and employs concept-wise self-supervised learning to enhance pixel-level grouping. The framework achieves state-of-the-art performance in unsupervised semantic segmentation on various datasets.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. This work provides a causal inference perspective for unsupervised semantic segmentation, which is rarely explored.
2. The proposed framework achieves state-of-the-art performance in unsupervised semantic segmentation on various datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is difficult to follow. For example, the authors introduce many new terms such as "concept clusterbook", "concept fractions", "concept prototypes", and "concept bank", without providing clear and detailed explanations of these concepts. Specifically, the relationship between these terms and how they contribute to the overall framework is not well-defined. The lack of formal definitions makes it hard to understand the underlying methodology.
2. The motivation for the proposed approach is not clear. Although the authors claim that they address the question of "How can we define what to cluster and how to do so under an unsupervised setting?", the paper lacks a detailed explanation of why the proposed method can solve this problem. The connection between the causal inference framework and the practical clustering of pixels remains vague. It is not clear how the 'concept clusterbook' helps in defining what to cluster in a way that is superior to existing methods.
3. The comparison with existing methods is not fair. For example, the proposed CAUSE-MLP leverages additional information from the pre-trained DINO model, while the compared methods do not use any additional information. This makes it difficult to assess the true contribution of the proposed method, as the performance gains might be attributed to the pre-trained model rather than the novel aspects of the CAUSE framework. The use of DINO features gives an unfair advantage in the comparison.
4. The authors should provide more analysis and visualization results to demonstrate the effectiveness of the proposed method. For example, it would be helpful to visualize the "concept clusterbook" and how it influences the clustering process. Without such visualizations, it is hard to understand the practical impact of the proposed method. The paper lacks sufficient qualitative analysis to support the quantitative results.

### Suggestions

The paper needs significant improvements in clarity and motivation. The authors should start by providing formal definitions for the newly introduced terms such as "concept clusterbook", "concept fractions", "concept prototypes", and "concept bank". These definitions should clearly explain the role of each concept within the framework and how they relate to each other. For example, the paper could benefit from a detailed explanation of how the concept clusterbook is constructed, what the concept fractions represent, and how these are used to form concept prototypes. Furthermore, the authors should provide a clear explanation of how the concept bank is used during training and inference. It would be beneficial to include a diagram that illustrates the flow of information between these components. This would greatly enhance the reader's understanding of the proposed method.

To address the lack of motivation, the authors should provide a more detailed explanation of why their proposed method can solve the problem of defining what to cluster in an unsupervised setting. The paper should clearly articulate how the causal inference framework, specifically the concept clusterbook, helps in determining the appropriate level of granularity for clustering. The authors need to explain why this approach is superior to existing methods that do not explicitly define what to cluster. A concrete example would be helpful to illustrate how the concept clusterbook leads to better clustering results compared to methods that directly cluster pixel features. The authors should also discuss the limitations of their approach and under which conditions it might fail. This would provide a more balanced view of the proposed method.

Finally, the authors should conduct a more fair comparison with existing methods. This could involve comparing the proposed method with and without the pre-trained DINO features. This would help to isolate the contribution of the CAUSE framework from the benefits of the pre-trained model. Additionally, the authors should provide more qualitative results, such as visualizations of the concept clusterbook and how it influences the clustering process. This would help to demonstrate the effectiveness of the proposed method and provide a better understanding of its inner workings. The paper would also benefit from an analysis of the sensitivity of the method to different hyperparameter settings. This would help to assess the robustness of the proposed approach.

### Questions

Please refer to the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
