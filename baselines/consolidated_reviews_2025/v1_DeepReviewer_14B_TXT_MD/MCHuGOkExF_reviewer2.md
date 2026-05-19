### Summary

This paper proposes a novel approach to scaling LLM inference for code generation. It frames code generation as a black box optimization problem within the code space, and employs optimization-inspired techniques to enhance exploration. Specifically, it introduces Scattered Forest Search (SFS) to enhance solution diversity while searching for solutions. The theoretical analysis illustrates how these methods avoid local optima during optimization. Extensive experiments on HumanEval, MBPP, APPS, CodeContests, and Leetcode reveal significant performance improvements.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper proposes a novel approach to scaling LLM inference for code generation. It frames code generation as a black box optimization problem within the code space, and employs optimization-inspired techniques to enhance exploration. Specifically, it introduces Scattered Forest Search (SFS) to enhance solution diversity while searching for solutions. 
2. The theoretical analysis illustrates how these methods avoid local optima during optimization. 
3. Extensive experiments on HumanEval, MBPP, APPS, CodeContests, and Leetcode reveal significant performance improvements.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost associated with the proposed method. While the authors mention that their approach is more efficient than repeated sampling, a rigorous comparison of the computational resources required by SFS and other search methods (e.g., tree search, line search) is missing. Specifically, the paper should include a breakdown of the time complexity for each step of the SFS algorithm, including the generation of diverse solutions, evaluation, and selection processes. Furthermore, empirical results on the actual runtime and resource consumption (e.g., GPU usage, memory) for different problem sizes and search budgets are needed to fully assess the practical applicability of the method.
2. The paper does not provide a comprehensive analysis of the sensitivity of the proposed method to the hyperparameters. While the authors mention that SFS is parameter-free, the performance of the method is likely influenced by the settings of the underlying LLM (e.g., temperature, maximum token length) and the specific implementation details of the search algorithm. A thorough sensitivity analysis should explore how variations in these parameters affect the performance of SFS across different datasets and problem settings. This analysis should include not only the final pass@k rate but also other metrics such as the convergence speed and the diversity of the generated solutions.
3. The paper lacks a detailed analysis of the limitations of the proposed method. While the authors mention that SFS may not be suitable for all types of code generation tasks, a more in-depth discussion of the specific scenarios where SFS might fail or underperform is needed. For example, the paper should discuss the potential challenges of applying SFS to tasks that require complex reasoning or planning, or to tasks where the solution space is highly constrained. Additionally, the paper should explore the potential for SFS to get stuck in local optima, and discuss strategies for mitigating this issue.
4. The paper lacks a detailed analysis of the generalization ability of the proposed method. While the authors evaluate SFS on several code generation benchmarks, a more rigorous analysis of the method's ability to generalize to unseen tasks and datasets is needed. This analysis should include experiments on datasets that are significantly different from the training data of the underlying LLM, as well as experiments on tasks that require different types of reasoning or problem-solving skills. Furthermore, the paper should discuss the potential for overfitting to the specific benchmarks used in the evaluation, and strategies for mitigating this issue.

### Suggestions

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the time complexity for each step of the SFS algorithm, including the generation of diverse solutions, evaluation, and selection processes. This analysis should be complemented with empirical results on the actual runtime and resource consumption (e.g., GPU usage, memory) for different problem sizes and search budgets. For example, the authors could present a table showing the average runtime per problem for SFS and other search methods (e.g., tree search, line search) on different datasets, along with the corresponding GPU usage and memory consumption. This would allow for a more rigorous comparison of the computational efficiency of the proposed method and provide a better understanding of its practical applicability. Furthermore, the authors should investigate the scalability of SFS with respect to the size of the search space and the complexity of the code generation task. This could be done by evaluating SFS on larger and more complex code generation benchmarks, and analyzing how the runtime and resource consumption scale with the problem size.

To address the lack of sensitivity analysis, the authors should conduct a thorough investigation of how variations in the hyperparameters of the underlying LLM (e.g., temperature, maximum token length) and the specific implementation details of the search algorithm affect the performance of SFS. This analysis should include not only the final pass@k rate but also other metrics such as the convergence speed and the diversity of the generated solutions. For example, the authors could present a series of plots showing how the pass@k rate varies with different temperature settings of the LLM, or how the convergence speed is affected by different selection strategies in the SFS algorithm. This would provide a better understanding of the robustness of the proposed method and help to identify the optimal hyperparameter settings for different tasks and datasets. Furthermore, the authors should investigate the potential for adaptive hyperparameter tuning, where the hyperparameters are adjusted during the search process based on the performance of the algorithm.

To address the lack of analysis of the limitations, the authors should provide a more in-depth discussion of the specific scenarios where SFS might fail or underperform. This should include a discussion of the potential challenges of applying SFS to tasks that require complex reasoning or planning, or to tasks where the solution space is highly constrained. For example, the authors could discuss how SFS might struggle with code generation tasks that require a deep understanding of the problem context or that involve multiple interacting components. Additionally, the authors should explore the potential for SFS to get stuck in local optima, and discuss strategies for mitigating this issue. This could involve incorporating techniques such as simulated annealing or genetic algorithms into the SFS framework. Finally, the authors should provide a more detailed analysis of the generalization ability of the proposed method, including experiments on datasets that are significantly different from the training data of the underlying LLM, as well as experiments on tasks that require different types of reasoning or problem-solving skills. This would provide a more comprehensive evaluation of the method's ability to generalize to unseen tasks and datasets.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

3

**********
