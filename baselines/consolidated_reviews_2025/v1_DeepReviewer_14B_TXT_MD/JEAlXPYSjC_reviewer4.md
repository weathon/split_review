### Summary

The paper proposes a simple strategy to improve the performance of CLIP models, especially those trained on smaller datasets. The authors show that extending the training procedure according to a simple heuristic can significantly improve the performance of CLIP models. The paper also compares the proposed strategy with other approaches employed to improve the performance of CLIP models.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed strategy is simple and effective.
3. The paper provides a comprehensive comparison with other approaches.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a theoretical analysis of the proposed strategy.
2. The paper does not explore the impact of the proposed strategy on other datasets and tasks.

### Suggestions

The paper's primary weakness lies in the lack of theoretical grounding for the proposed training extension strategy. While the empirical results demonstrate improved performance, the absence of a theoretical framework makes it difficult to understand why this specific heuristic works and when it might fail. For instance, it would be beneficial to analyze the loss landscape and how the extended training affects the model's convergence properties. A theoretical analysis could involve examining the gradient behavior during the extended training phase, or exploring the relationship between the extended training and the model's generalization ability. Without such analysis, the proposed strategy remains somewhat ad-hoc, limiting its broader applicability and interpretability. Furthermore, the paper should explore the sensitivity of the proposed strategy to different hyperparameter settings, such as the learning rate and batch size, during the extended training phase. This would provide a more complete understanding of the method's robustness and limitations.

Another significant limitation is the narrow scope of the experimental evaluation. The paper focuses primarily on CLIP models trained on smaller datasets, and it is unclear how the proposed strategy would perform on larger datasets or different tasks. For example, it would be valuable to evaluate the method on datasets with different characteristics, such as those with more complex image-text relationships or those with a larger number of classes. Additionally, the paper should explore the impact of the proposed strategy on different CLIP architectures and training objectives. This would help to determine the generalizability of the method and identify potential areas for improvement. The paper should also consider evaluating the method on tasks beyond image-text retrieval, such as zero-shot image classification or image captioning, to demonstrate its broader applicability.

Finally, the paper should provide a more detailed comparison with existing approaches for improving CLIP model performance. While the paper mentions other methods, it does not provide a thorough analysis of their strengths and weaknesses in relation to the proposed strategy. A more comprehensive comparison should include a discussion of the computational cost, the ease of implementation, and the potential for further improvements. This would help to position the proposed strategy within the broader context of CLIP model research and highlight its unique contributions. Furthermore, the paper should explore the potential for combining the proposed strategy with other existing methods to achieve even better performance.

### Questions

1. Can the authors provide a theoretical analysis of the proposed strategy?
2. Can the authors explore the impact of the proposed strategy on other datasets and tasks?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
