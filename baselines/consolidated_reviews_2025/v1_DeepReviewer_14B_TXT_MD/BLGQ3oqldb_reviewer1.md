### Summary

The paper proposes a novel neural layer, LogicMP, that performs mean-field variational inference over a Markov Logic Network (MLN). The key idea is to exploit the structure and symmetries in MLNs to accelerate the inference process. The authors demonstrate that LogicMP can reduce the inference complexity from exponential to polynomial. LogicMP can be plugged into any off-the-shelf neural network to encode first-order logic constraints while retaining modularity and efficiency. The authors evaluate LogicMP on various tasks over images, graphs, and text, and show that it outperforms advanced competitors in both performance and efficiency.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel neural layer, LogicMP, that performs mean-field variational inference over a Markov Logic Network (MLN). The key idea is to exploit the structure and symmetries in MLNs to accelerate the inference process. The authors demonstrate that LogicMP can reduce the inference complexity from exponential to polynomial. LogicMP can be plugged into any off-the-shelf neural network to encode first-order logic constraints while retaining modularity and efficiency.

2. The authors evaluate LogicMP on various tasks over images, graphs, and text, and show that it outperforms advanced competitors in both performance and efficiency.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of LogicMP. It is unclear how the runtime of LogicMP scales with the number of entities, predicates, and rules in the MLN. A formal analysis of the time and space complexity of the proposed approach is needed to better understand its scalability and limitations. Specifically, the paper lacks a discussion on how the mean-field approximation impacts the overall complexity, and how the parallelization strategy interacts with the underlying graph structure of the MLN. It is also unclear how the size of the largest clique in the MLN's dependency graph affects the practical runtime, which is a crucial factor in the mean-field approximation.

2. The paper does not provide a detailed comparison of LogicMP with other approaches for encoding first-order logic constraints in neural networks, such as Neural Probabilistic Logic and Probabilistic Logic Programming. A thorough comparison with these approaches is needed to better understand the advantages and disadvantages of LogicMP. The comparison should not only focus on performance metrics but also on the underlying assumptions, limitations, and the types of logical constraints that each method can handle effectively. For instance, it is unclear how LogicMP handles negation as failure, a common feature in many logic programming paradigms, and how it compares to methods that explicitly use answer set programming or SMT solvers.

### Suggestions

The paper should include a more rigorous analysis of the computational complexity of LogicMP, going beyond the high-level claims of polynomial time complexity. This analysis should explicitly state how the runtime scales with the number of entities, predicates, rules, and the size of the largest clique in the MLN's dependency graph. The authors should provide a breakdown of the time complexity for each step of the mean-field approximation, including the message passing and update rules. Furthermore, the analysis should consider the impact of different graph structures on the runtime, such as sparse versus dense graphs, and how the parallelization strategy mitigates these effects. A theoretical analysis should be complemented with empirical results on larger datasets to validate the scalability claims. It would also be beneficial to discuss the memory footprint of LogicMP, especially when dealing with large MLNs, and how it compares to other approaches.

To better position LogicMP within the landscape of neuro-symbolic reasoning, the paper should include a more detailed comparison with other methods for encoding first-order logic constraints in neural networks. This comparison should not only focus on performance metrics but also on the underlying assumptions, limitations, and the types of logical constraints that each method can handle effectively. For example, the authors should discuss how LogicMP handles negation as failure, a common feature in many logic programming paradigms, and how it compares to methods that explicitly use answer set programming or SMT solvers. The comparison should also address the differences in the underlying inference mechanisms, such as variational inference in LogicMP versus probabilistic inference in Neural Probabilistic Logic. A table summarizing the strengths and weaknesses of each approach would be beneficial for the reader. The authors should also discuss the limitations of LogicMP in terms of the types of logical constraints it can handle, and how it compares to other methods in this regard.

Finally, the paper should provide more details on the implementation of LogicMP, including the specific choices of activation functions, optimizers, and hyperparameters. The authors should also discuss the sensitivity of LogicMP to these choices and provide guidelines for selecting appropriate values. It would be helpful to include a pseudocode or a detailed algorithm description of the LogicMP layer, which would make it easier for other researchers to reproduce the results and integrate LogicMP into their own work. The paper should also discuss the potential limitations of the mean-field approximation, such as the possibility of inaccurate marginal distributions, and how these limitations might affect the performance of LogicMP.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
