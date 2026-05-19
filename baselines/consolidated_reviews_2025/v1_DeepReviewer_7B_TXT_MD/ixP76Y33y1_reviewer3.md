### Summary

This paper investigates the relationship between the generalization ability of neural networks and the intrinsic dimension of their training datasets. The authors introduce a novel metric called "label sharpness" to measure the intrinsic dimension of datasets. They demonstrate that the generalization error of a trained network is negatively correlated with the label sharpness of the dataset. Furthermore, they show that the adversarial robustness of a trained network is positively correlated with the label sharpness. The paper provides a theoretical framework to support these findings and validates them through extensive experiments on six medical imaging datasets and eleven natural image datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper introduces the concept of "label sharpness" as a metric for intrinsic dimension, which is a novel contribution to the field.
2. The paper provides a theoretical framework to support the empirical findings, adding rigor to the analysis.
3. The paper includes extensive experiments on multiple datasets, demonstrating the practical relevance of the proposed metric.

### Weaknesses

#### Some Related Works

[1] On the relationship between intrinsic dimension and generalization in deep learning.

#### comment

1. The paper does not provide a detailed comparison of the proposed "label sharpness" metric with existing intrinsic dimension estimation methods, such as those based on Lipschitz constants or other established techniques. This makes it difficult to assess the novelty and advantages of the proposed metric.
2. The theoretical framework relies on certain assumptions, such as the Lipschitz continuity of the loss function and the model. The paper does not adequately address the limitations of these assumptions, especially in the context of deep neural networks, which are known to be highly non-linear and may not satisfy these conditions. Specifically, the assumption of Lipschitz continuity for the loss function is particularly problematic, as the loss landscape of deep networks is known to be highly non-convex and can have regions where the loss changes rapidly, violating this assumption. The paper should discuss how these assumptions might affect the validity of the theoretical results.
3. While the paper demonstrates the correlation between label sharpness and adversarial robustness, it does not provide a clear explanation of why this correlation exists. The paper should delve deeper into the underlying mechanisms that cause this relationship, perhaps by analyzing the loss landscape or the feature representations learned by the network. It is not sufficient to simply observe the correlation; a mechanistic explanation is needed to understand the underlying phenomenon.
4. The experiments are conducted on relatively small datasets. The paper does not discuss the scalability of the proposed metric to larger datasets, which is a crucial consideration for practical applications. The computational cost of estimating label sharpness on large datasets is not addressed, and it is unclear whether the metric can be computed efficiently in such scenarios.

### Suggestions

The paper would benefit significantly from a more thorough comparison of the proposed "label sharpness" metric with existing intrinsic dimension estimation techniques. The authors should provide a detailed analysis of how their metric differs from methods based on Lipschitz constants, such as the MLE or TwoNN estimators, and other established techniques. This comparison should not only focus on the theoretical differences but also on the practical implications for generalization and adversarial robustness. For example, the authors could analyze the computational cost and accuracy of their metric compared to these existing methods on various datasets. Furthermore, a discussion of the sensitivity of each metric to different types of data and network architectures would be valuable. This would help to establish the unique advantages and limitations of the proposed metric.

To address the limitations of the theoretical framework, the authors should provide a more detailed discussion of the assumptions made, particularly the Lipschitz continuity of the loss function and the model. They should analyze how these assumptions might be violated in the context of deep neural networks and discuss the implications for the validity of their theoretical results. For instance, they could explore the impact of non-smooth activation functions or highly non-linear network architectures on the Lipschitz constant of the loss function. Furthermore, the authors should consider alternative theoretical frameworks that do not rely on such strong assumptions, or at least provide a more robust justification for why their current framework is still applicable in the context of deep learning. This could involve exploring weaker forms of smoothness or considering the geometry of the loss landscape more carefully.

Finally, the paper needs to provide a more in-depth analysis of the relationship between label sharpness and adversarial robustness. The authors should explore the underlying mechanisms that cause this correlation, perhaps by analyzing the loss landscape or the feature representations learned by the network. For example, they could investigate how the sharpness of the loss landscape affects the network's sensitivity to adversarial perturbations. They could also analyze the feature representations learned by the network to see if they are more robust when the label sharpness is higher. Furthermore, the authors should discuss the practical implications of this relationship, such as how it can be used to improve the robustness of deep learning models. The paper should also address the scalability of the proposed metric to larger datasets, providing a discussion of the computational cost and potential strategies for efficient computation on large datasets.

### Questions

1. How does the proposed "label sharpness" metric compare to existing intrinsic dimension estimation methods in terms of accuracy and computational cost?
2. What are the limitations of the theoretical framework, particularly regarding the assumptions of Lipschitz continuity?
3. Can the authors provide a more detailed explanation of the relationship between label sharpness and adversarial robustness?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
