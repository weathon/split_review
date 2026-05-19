### Summary

This paper proposes a method to generate counterfactuals for given text and concept, by prompting LLMs to generate the counterfactuals directly, or by learning a causal embedding space that can identify matches that approximate counterfactuals. The paper also introduces a new dataset for stance detection.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The paper studies an important problem of generating counterfactuals for given text and concept, which is a challenging task.
3. The paper proposes two methods to approximate counterfactuals, by directly prompting LLMs, or by identifying matches in a causal embedding space.
4. The paper proposes a metric called order-faithfulness, and shows that the proposed counterfactual approximation methods are order-faithful.
5. The paper presents experiments on the CEBaB dataset, and shows that the proposed methods outperform baselines.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not include any baselines for generating counterfactuals. It is important to compare the proposed methods with existing methods, such as those based on adversarial training or data augmentation, to demonstrate the effectiveness of the proposed approach. Without such comparisons, it is difficult to assess the true novelty and performance gains.
2. The proposed methods require a causal graph, which is not always available in real-world scenarios. The paper does not discuss how to obtain or learn the causal graph in practice, and how the performance of the proposed methods is affected by the quality of the causal graph. This is a significant limitation, as the accuracy of causal inference heavily depends on the correctness of the causal graph.
3. The proposed methods are limited to a specific causal graph structure, where all concepts are exogenous. The paper does not discuss how to extend the proposed methods to more complex causal graphs, such as those with confounding variables or feedback loops. This limits the applicability of the proposed methods to a narrow range of problems.
4. The paper does not provide a clear definition of the concept of "causal representation". It is unclear how the proposed methods learn a causal representation, and how this representation differs from existing methods for learning causal representations. This lack of clarity makes it difficult to understand the underlying mechanisms of the proposed methods.
5. The paper does not provide a clear explanation of the loss function used in the proposed methods. The paper does not explain the intuition behind the loss function, and how the different terms in the loss function contribute to the overall objective. This lack of explanation makes it difficult to understand the training process of the proposed methods.

### Suggestions

The paper should include a more comprehensive comparison with existing counterfactual generation methods. Specifically, the authors should consider baselines that use adversarial training or data augmentation techniques to generate counterfactuals. These methods, while not directly optimizing for causal effects, can provide a strong baseline for comparison. For example, methods that use gradient-based approaches to perturb input text or methods that use generative models to create counterfactuals should be included. Furthermore, the paper should provide a more detailed analysis of the quality of the generated counterfactuals, beyond just the order-faithfulness metric. This could include metrics such as semantic similarity, fluency, and diversity. A human evaluation of the generated counterfactuals would also be beneficial to assess their quality.

The paper should address the limitation of requiring a causal graph by exploring methods for learning or approximating the causal graph from data. The authors could consider using techniques from causal discovery, such as constraint-based methods or score-based methods, to learn the causal graph from observational data. The paper should also discuss how the performance of the proposed methods is affected by the quality of the learned causal graph, and how to handle uncertainty in the causal graph. Furthermore, the paper should explore how to extend the proposed methods to more complex causal graphs, such as those with confounding variables or feedback loops. This could involve using techniques from causal mediation analysis or causal inference with latent variables. The paper should also discuss the limitations of the proposed methods in these more complex scenarios.

The paper should provide a more detailed explanation of the concept of "causal representation" and how the proposed methods learn such a representation. The authors should clearly define what they mean by "causal representation" and how it differs from existing methods for learning causal representations. The paper should also provide a more detailed explanation of the loss function used in the proposed methods, including the intuition behind each term and how they contribute to the overall objective. The authors should also discuss the sensitivity of the proposed methods to the choice of hyperparameters, and provide guidelines for selecting appropriate hyperparameter values. Finally, the paper should include a more thorough analysis of the computational cost of the proposed methods, and compare it to existing methods.

### Questions

1. How do you ensure that the generated counterfactuals are realistic and preserve the style of the original text?
2. How do you handle the cases where the causal graph is not known or is misspecified?
3. How do you extend the proposed methods to more complex causal graphs, such as those with confounding variables or feedback loops?
4. How do you evaluate the quality of the generated counterfactuals, beyond just the order-faithfulness metric?
5. How do you compare the proposed methods with existing methods for generating counterfactuals, such as those based on adversarial training or data augmentation?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
