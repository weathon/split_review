### Summary

This paper studies the problem of Continual Learning (CL) with Stability and Plasticity, where the goal is to learn tasks sequentially while maintaining performance on previously learned tasks and forgetting new task knowledge as little as possible. The authors introduce a new metric called Probabilistic Pareto-optimality, which measures the degree to which a model can achieve a certain level of performance on a given task without compromising performance on previous tasks. The authors propose a novel algorithm called Imprecise Bayesian Continual Learning (IBCL) that uses variational inference to update a knowledge base of task distributions and a preference HDR computation to generate models that satisfy the Probabilistic Pareto-optimality metric. The authors evaluate their method on several CL benchmarks and show that it outperforms existing CL methods in terms of both accuracy and stability.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a new metric called Probabilistic Pareto-optimality, which provides a more flexible and nuanced way to evaluate the performance of CL models.
2. The authors propose a novel algorithm called Imprecise Bayesian Continual Learning (IBCL) that uses variational inference to update a knowledge base of task distributions and a preference HDR computation to generate models that satisfy the Probabilistic Pareto-optimality metric.
3. The authors evaluate their method on several CL benchmarks and show that it outperforms existing CL methods in terms of both accuracy and stability.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is very difficult to follow, with many technical details and mathematical notations that are not clearly explained. For example, the authors introduce the concept of a "knowledge base" but do not provide a clear definition of what it represents or how it is updated. The use of variational inference is also not well explained, and it is unclear how the authors choose the variational distribution and how it relates to the true posterior distribution. The authors should provide more intuitive explanations and examples to help readers understand the technical details.
2. The authors do not provide a clear explanation of how the proposed method addresses the issue of catastrophic forgetting, which is a key challenge in CL. While the authors claim that their method is able to learn new tasks without forgetting previous ones, they do not provide any empirical evidence to support this claim. The authors should provide more details on how their method avoids catastrophic forgetting and how it compares to other CL methods that explicitly address this issue.
3. The authors do not provide a detailed analysis of the computational complexity of their method. While they claim that their method is efficient, they do not provide any empirical evidence to support this claim. The authors should provide a more detailed analysis of the time and space complexity of their method and compare it to other CL methods.

### Suggestions

The paper needs significant improvements in clarity and technical depth. The authors should start by providing a more intuitive explanation of the core concepts, such as the "knowledge base" and the Probabilistic Pareto-optimality metric. Instead of diving directly into mathematical notations, they should first explain the underlying ideas using simple examples and analogies. For instance, when discussing the knowledge base, they could illustrate how it accumulates task distributions and how these distributions are used to generate new models. Similarly, the Probabilistic Pareto-optimality metric should be explained in terms of its practical implications for model selection, rather than just its mathematical definition. The authors should also provide a step-by-step walkthrough of the IBCL algorithm, highlighting the key decisions and trade-offs involved in each step. This would greatly enhance the readability and understanding of the paper.

To address the lack of clarity regarding catastrophic forgetting, the authors should provide a more detailed explanation of how their method avoids this issue. They should explicitly discuss the mechanisms that prevent the model from overwriting previously learned knowledge when learning new tasks. For example, they could explain how the variational inference process ensures that the model retains information from previous tasks while still being able to adapt to new ones. Furthermore, the authors should include a more comprehensive empirical evaluation of their method, specifically focusing on its ability to mitigate catastrophic forgetting. This could involve comparing the performance of their method on previously learned tasks with and without new task learning, and demonstrating that the performance degradation is minimal. The authors should also compare their method to other CL methods that explicitly address catastrophic forgetting, such as regularization-based approaches or replay-based methods.

Finally, the authors need to provide a more thorough analysis of the computational complexity of their method. They should provide a detailed breakdown of the time and space complexity of each step in the IBCL algorithm, and compare it to the complexity of other CL methods. This analysis should include both theoretical bounds and empirical measurements. The authors should also discuss the scalability of their method to larger datasets and more complex models. This would help readers understand the practical limitations of their method and its suitability for different applications. The authors should also consider providing an ablation study to analyze the impact of different components of their method on its overall performance and computational cost.

### Questions

1. How does the proposed method address the issue of catastrophic forgetting?
2. What is the computational complexity of the proposed method?
3. How does the proposed method compare to other CL methods in terms of both accuracy and stability?

### Rating

3

### Confidence

3

**********
