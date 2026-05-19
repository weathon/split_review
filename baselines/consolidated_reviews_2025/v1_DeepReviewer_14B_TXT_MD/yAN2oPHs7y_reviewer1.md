### Summary

The paper introduces a novel differentiable rule list learning framework. The proposed method uses continuous optimization to simultaneously learn feature discretization, rule construction, and rule ordering. The method is evaluated on multiple datasets and compared with several baselines.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is technically sound and achieves superior performance on most datasets compared with several baselines.
3. The source code is provided.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is limited to the rule list model, which may lack expressiveness and could be less effective on complex tasks. Specifically, the reliance on a strict rule list structure, where rules are evaluated sequentially and only the first matching rule is applied, can limit the model's ability to capture complex interactions between features. This is particularly concerning in scenarios where multiple conditions might need to be considered simultaneously, or where the optimal decision boundary is not well-represented by a series of disjoint rules.

2. The method currently only supports binary classification, limiting its applicability to a subset of machine learning tasks. The extension to multi-class classification is non-trivial, as it's not clear how the rule learning process would adapt to handle multiple classes directly. A naive one-vs-all or one-vs-one approach might not be optimal, and could lead to a large number of rules, thereby impacting the interpretability which is a key advantage of the rule list model.

### Suggestions

The authors should investigate methods to enhance the expressiveness of the rule list model without sacrificing interpretability. One potential direction is to explore the use of weighted rules, where each rule contributes to the final decision based on its confidence or relevance, rather than having a hard cutoff at the first matching rule. This could allow the model to capture more nuanced relationships in the data. Another approach could be to incorporate some form of rule interaction, where the outcome of one rule can influence the application of subsequent rules, potentially through a dependency graph or a similar mechanism. This would allow the model to capture more complex logical relationships between features, moving beyond simple sequential evaluation.

To address the limitation of binary classification, the authors should explore methods for directly extending the rule list model to multi-class problems. One approach could be to learn a set of rules for each class, and then use a voting or aggregation mechanism to determine the final class label. Another approach could be to use a hierarchical structure, where rules at higher levels determine the class and rules at lower levels refine the decision. The key challenge here is to ensure that the learned rules remain interpretable and do not become overly complex. The authors should also consider how the proposed differentiable learning framework can be adapted to handle multi-class scenarios, as the current formulation is specifically designed for binary outcomes. This might involve modifying the loss function or the rule evaluation process to accommodate multiple classes.

Finally, the authors should provide a more detailed analysis of the computational complexity of the proposed method, particularly in relation to the number of features and the length of the rule list. While the method is differentiable, the optimization process might still be computationally expensive for high-dimensional datasets or long rule lists. It would be beneficial to provide some guidelines on how to choose the rule list length and other hyperparameters, and to discuss the trade-offs between model complexity, performance, and computational cost. Furthermore, a comparison of the training time with other baselines would be valuable to assess the practical applicability of the proposed method.

### Questions

1. How does the proposed method handle continuous features? Is it through binning? If so, how many bins are typically used?
2. What is the computational complexity of the proposed method? How does it scale with the number of features and the length of the rule list? It would be helpful to compare the training time with other baselines.
3. In the experiments, how is the rule list length chosen? What criteria should be used to determine the optimal length of the rule list?
4. How can the proposed method be extended to handle missing values in the dataset?

### Rating

6

### Confidence

4

**********
