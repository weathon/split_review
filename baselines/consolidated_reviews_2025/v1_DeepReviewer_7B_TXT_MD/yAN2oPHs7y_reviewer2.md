### Summary

The paper introduces a novel method for learning rule lists from data in a differentiable manner, aiming to address the interpretability challenges in machine learning. Unlike traditional rule list methods, this approach learns both discretizations of features and rule conjunctions without pre-discretization or restrictions, making it more scalable and accurate. The method uses continuous relaxations and temperature annealing to ensure strict rule list convergence. Extensive experiments demonstrate its superior performance over existing methods on various datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel method for learning rule lists in a differentiable framework, which is a significant advancement in interpretable machine learning.
2. The proposed method is supported by a comprehensive set of experiments, including both real-world and synthetic datasets, demonstrating its effectiveness and robustness.
3. The paper is well-structured and clearly written, making it accessible to readers and facilitating understanding of the proposed approach.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the computational complexity and scalability of the proposed method, especially in comparison to existing approaches. Specifically, the paper lacks a rigorous analysis of how the number of features, the number of rules, and the size of the dataset impact the runtime and memory usage of the algorithm. This is crucial for assessing the practical applicability of the method to large-scale datasets.
2. While the paper compares the proposed method with several baselines, it would be beneficial to include a broader range of state-of-the-art methods, particularly those that also focus on differentiable rule learning. The current comparisons do not fully explore the landscape of existing techniques, and it is unclear how the proposed method compares to other methods that use similar techniques, such as gradient-based optimization for rule learning. A more comprehensive comparison would provide a better understanding of the strengths and weaknesses of the proposed approach.
3. The paper could provide more insights into the interpretability of the learned rule lists, especially in complex scenarios. While the paper claims that the method produces interpretable rule lists, it does not provide a detailed analysis of how the learned rules can be understood by humans, especially in cases where the rules are complex or numerous. It would be beneficial to include examples of the learned rule lists and discuss how they can be used to gain insights into the data.

### Suggestions

The paper should include a more thorough analysis of the computational complexity of the proposed method. This analysis should consider the impact of various factors, such as the number of features, the number of rules, and the size of the dataset, on the runtime and memory usage of the algorithm. The authors should provide a theoretical analysis of the time and space complexity of each step of the algorithm, and they should also provide empirical results on the runtime and memory usage of the algorithm on different datasets. This analysis would help to assess the practical applicability of the method to large-scale datasets and would provide a better understanding of the trade-offs between accuracy and computational cost. Furthermore, the authors should compare the computational complexity of their method with that of existing approaches, such as combinatorial optimization methods for rule learning, to highlight the advantages and disadvantages of their approach.

To strengthen the experimental evaluation, the authors should include a broader range of state-of-the-art methods, particularly those that also focus on differentiable rule learning. This would provide a more comprehensive comparison of the proposed method with existing techniques and would help to better understand its strengths and weaknesses. The authors should also consider including methods that use similar techniques, such as gradient-based optimization for rule learning, to provide a more complete picture of the current state of the art. The comparison should not only focus on the performance of the methods but also on their interpretability and computational cost. The authors should also provide a detailed analysis of the results, including a discussion of the strengths and weaknesses of each method. This would help to provide a more nuanced understanding of the performance of the proposed method and would help to identify areas for future research.

Finally, the paper should provide more insights into the interpretability of the learned rule lists, especially in complex scenarios. The authors should include examples of the learned rule lists and discuss how they can be understood by humans, especially in cases where the rules are complex or numerous. The authors should also discuss how the learned rules can be used to gain insights into the data and how they can be used to make predictions. The authors should also consider providing a visualization of the learned rule lists to help to understand their structure and meaning. This would help to make the method more accessible to a wider audience and would help to demonstrate its practical value.

### Questions

1. How does the proposed method handle noisy or irrelevant features in the dataset?
2. What are the limitations of the proposed method in terms of scalability and computational cost?
3. How does the method ensure the interpretability of the learned rule lists, especially in complex scenarios?

### Rating

6

### Confidence

3

**********
