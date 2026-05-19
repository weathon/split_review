### Summary

This paper introduces Imprecise Bayesian Continual Learning (IBCL), an algorithm designed to address the challenge of Continual Learning under Specific Trade-offs (CLuST). IBCL efficiently generates models corresponding to specified stability-plasticity preferences without the need for retraining, using a zero-shot approach based on convex combinations of model parameter distributions. The algorithm updates a knowledge base represented as a convex hull of parameter distributions and generates Pareto-optimal models for given trade-offs. Experiments demonstrate that IBCL achieves significant improvements in task accuracy and maintains near-zero to positive backward transfer, with constant training overhead regardless of the number of preferences requested.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel approach to continual learning by focusing on generating models that balance stability and plasticity according to user-defined preferences. This is a significant contribution to the field, as it addresses a practical challenge in deploying continual learning systems in real-world applications.

2. The use of a convex hull of model parameter distributions to represent the knowledge base is an innovative idea. This allows for efficient generation of new models through convex combinations, eliminating the need for retraining and significantly reducing computational overhead.

3. The experimental results are compelling, showing substantial improvements in task accuracy and backward transfer compared to existing methods. The constant training overhead, regardless of the number of preferences, is a notable achievement that enhances the scalability of the approach.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion of the computational complexity of the proposed algorithm, particularly concerning the update of the knowledge base and the generation of new models. While the authors claim constant-time updates, a more rigorous analysis of the time and space complexity would be beneficial. Specifically, the process of updating the convex hull of model parameter distributions, which involves adding new vertices and potentially removing others, needs further clarification. The computational cost of these operations, especially as the number of tasks and preferences grows, should be explicitly addressed. Furthermore, the memory requirements for storing the knowledge base, which includes the model parameter distributions and their convex combinations, should be analyzed in terms of scalability.

2. The paper does not provide a thorough comparison with other state-of-the-art continual learning methods, particularly those that also address the stability-plasticity trade-off. A more comprehensive evaluation, including a wider range of benchmark datasets and comparison with more recent methods, would strengthen the paper's claims. The current evaluation, while showing promising results, could be enhanced by including comparisons with methods that use different approaches to manage the stability-plasticity trade-off, such as regularization-based or replay-based techniques. This would provide a more complete picture of the proposed method's strengths and weaknesses relative to the broader landscape of continual learning algorithms.

### Suggestions

To address the lack of detailed computational complexity analysis, the authors should provide a more rigorous breakdown of the time and space complexity of the IBCL algorithm. This should include a formal analysis of the time required to update the knowledge base, specifically focusing on the convex hull update operations. The analysis should consider the number of tasks, the number of preferences, and the dimensionality of the parameter space. Furthermore, the authors should provide a detailed analysis of the memory requirements for storing the knowledge base, including the model parameter distributions and their convex combinations. This analysis should consider the scalability of the method as the number of tasks and preferences increases. It would be beneficial to include empirical measurements of the time and memory usage of the algorithm on different datasets and with varying numbers of tasks and preferences. This would provide a more concrete understanding of the practical computational cost of the proposed method.

To strengthen the evaluation, the authors should include a more comprehensive comparison with state-of-the-art continual learning methods. This should include a wider range of benchmark datasets, including more complex and challenging datasets. The comparison should also include methods that use different approaches to manage the stability-plasticity trade-off, such as regularization-based methods (e.g., Elastic Weight Consolidation, Synaptic Intelligence) and replay-based methods (e.g., iCaRL, Deep Generative Replay). The evaluation should also include a detailed analysis of the performance of the proposed method under different scenarios, such as varying degrees of task similarity and different levels of task complexity. This would provide a more complete picture of the proposed method's strengths and weaknesses relative to the broader landscape of continual learning algorithms. Furthermore, the authors should provide a more detailed analysis of the hyperparameter sensitivity of the proposed method, including the impact of different choices of hyperparameters on the performance of the algorithm.

Finally, the authors should provide a more detailed discussion of the limitations of the proposed method. This should include a discussion of the potential challenges of applying the method to more complex and high-dimensional parameter spaces, as well as the potential limitations of the convex combination approach for generating new models. The authors should also discuss the potential impact of the choice of the base model on the performance of the proposed method. A more thorough discussion of these limitations would provide a more balanced and realistic assessment of the proposed method's capabilities and potential for future research.

### Questions

1. How does the choice of the base model affect the performance of the IBCL algorithm? Are there specific types of models for which the proposed method is more suitable?

2. Can the authors provide more details on the practical implementation of the algorithm, such as the specific optimization techniques used and the hardware requirements for running the experiments?

### Rating

6

### Confidence

3

**********
