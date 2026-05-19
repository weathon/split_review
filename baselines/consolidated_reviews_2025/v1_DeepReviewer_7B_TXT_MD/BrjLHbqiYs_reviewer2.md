### Summary

This paper studies the problem of quantifying interactions between modalities for a semi-supervised multi-modal learning setting. The authors propose lower and upper bounds for synergistic interactions and validate these bounds on synthetic and real-world datasets. They also demonstrate how these bounds can be used to estimate multi-modal model performance, guide data collection, and select appropriate multi-modal models.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The paper provides a novel approach to quantifying synergistic interactions in semi-supervised multi-modal learning settings.
3. The proposed bounds are validated on both synthetic and real-world datasets, demonstrating their effectiveness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not clearly explain how the proposed bounds can be used in practice. For example, it is unclear how the bounds can be used to guide data collection or model selection. The paper mentions that the bounds can be used to estimate multi-modal model performance, but it does not provide a clear methodology for how this can be achieved. It is also not clear how the bounds can be used to select appropriate multi-modal models, especially when there are multiple models with similar performance.
2. The paper does not compare the proposed approach with existing methods for quantifying interactions in multi-modal learning. It is not clear how the proposed approach compares to existing methods in terms of accuracy, computational complexity, and robustness. The paper should provide a more detailed comparison with existing methods to demonstrate the advantages of the proposed approach.
3. The paper does not discuss the limitations of the proposed approach. For example, it is not clear how the proposed approach handles noisy or missing data. The paper should discuss the limitations of the proposed approach and provide guidance on how to address these limitations.

### Suggestions

The paper would benefit significantly from a more detailed explanation of how the proposed bounds can be practically applied. Specifically, the authors should provide a step-by-step methodology for using the bounds to guide data collection. For instance, if the bounds indicate a high potential for improvement from multi-modal data, the authors should specify how to determine the optimal amount of data to collect from each modality. This could involve a cost-benefit analysis, considering the cost of acquiring data from each modality and the potential improvement in performance. Furthermore, the authors should provide a concrete example of how the bounds can be used to select appropriate multi-modal models. This could involve comparing the bounds for different models and selecting the model with the highest bounds, or it could involve using the bounds to identify models that are likely to perform well on a specific task. The authors should also discuss the limitations of the proposed approach, such as how it handles noisy or missing data, and provide guidance on how to address these limitations. For example, the authors could discuss how to use robust estimators to handle noisy data or how to use imputation techniques to handle missing data.

To strengthen the paper, the authors should include a more comprehensive comparison with existing methods for quantifying interactions in multi-modal learning. This comparison should not only focus on the accuracy of the bounds but also on their computational complexity and robustness. For example, the authors could compare their approach with methods based on mutual information or other information-theoretic measures. The comparison should also consider the assumptions made by each method and discuss the situations in which each method is most appropriate. This would help to clarify the advantages and disadvantages of the proposed approach and provide a more complete picture of the state-of-the-art in this area. The authors should also discuss the limitations of the proposed approach in comparison to existing methods. For example, the authors could discuss whether the proposed approach is more or less robust to certain types of data or models.

Finally, the authors should provide more details on the experimental setup and the datasets used in the paper. This should include a description of the data preprocessing steps, the model architectures used, and the evaluation metrics. The authors should also provide a more detailed analysis of the results, including a discussion of the statistical significance of the findings. For example, the authors could provide confidence intervals for the bounds and discuss the uncertainty in the estimates. The authors should also discuss the limitations of the experimental setup and how these limitations might affect the results. This would help to increase the reproducibility of the results and provide a more complete picture of the performance of the proposed approach.

### Questions

See the weakness.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
