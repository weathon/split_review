### Summary

This paper proposes a method to enhance the reasoning capabilities of large language models (LLMs) for complex tabular data. The approach involves condensing and decomposing tables into a hierarchical structure called a "table-tree," which is then executed in a breadth-first manner. The method is evaluated on several datasets, including WikiTQ, TableFact, FeTaQA, and BIRD, demonstrating improved performance over existing methods.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a novel approach to handling large and complex tables by structuring them as a hierarchical tree, which is an interesting and innovative idea.
2. The method shows significant improvements in performance on multiple datasets, indicating its potential effectiveness in real-world applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed explanation of the table condensation and decomposition processes. It is unclear how these processes are implemented and what specific algorithms or techniques are used to transform the original table into the hierarchical table-tree structure. The description lacks sufficient detail to allow for replication or a full understanding of the method's inner workings. For example, the criteria for determining the optimal level of condensation and decomposition are not clearly defined, and the impact of different condensation strategies on the final performance is not explored.
2. The paper does not provide a thorough analysis of the computational complexity of the proposed method. The process of building the table-tree and executing it in a breadth-first manner may introduce significant computational overhead, especially for large tables. The paper should include a detailed analysis of the time and space complexity of each step, and compare it with existing methods. It is also unclear how the method scales with increasing table size and complexity.
3. The paper does not discuss the limitations of the proposed method. It is important to acknowledge the potential drawbacks and challenges of the approach, such as its sensitivity to noise or its performance on tables with complex relationships between columns and rows. The paper should include a discussion of these limitations and suggest potential directions for future research.
4. The paper does not provide a clear explanation of how the breadth-first search is implemented. The paper mentions that the method executes the table-tree in a breadth-first manner, but it does not provide a detailed description of the algorithm or the data structures used to implement this search. The paper should also discuss the impact of different search strategies on the final performance.

### Suggestions

The paper would benefit significantly from a more detailed explanation of the table condensation and decomposition processes. The authors should provide a step-by-step description of how the original table is transformed into the hierarchical table-tree structure, including the specific algorithms or techniques used. This should include a discussion of the criteria for determining the optimal level of condensation and decomposition, and the impact of different condensation strategies on the final performance. For example, the authors could explore different clustering algorithms for condensing rows and columns, and analyze their impact on the final results. Furthermore, the paper should include a detailed analysis of the computational complexity of each step, including the table condensation, tree construction, and breadth-first search. This analysis should compare the proposed method with existing approaches and discuss the scalability of the method with increasing table size and complexity. The authors should also provide a clear explanation of how the breadth-first search is implemented, including the data structures used and the impact of different search strategies on the final performance. This should include a discussion of the trade-offs between breadth-first and depth-first search, and the rationale for choosing breadth-first search in this context.

To improve the reproducibility of the results, the authors should provide a more detailed description of the experimental setup, including the specific parameters used for each dataset and the hardware used for the experiments. The paper should also include a discussion of the limitations of the proposed method, including its sensitivity to noise and its performance on tables with complex relationships between columns and rows. The authors should also suggest potential directions for future research, such as exploring different tree structures or incorporating additional information into the table-tree. For example, the authors could explore the use of graph neural networks to learn the relationships between columns and rows, or incorporate additional metadata into the table-tree. The paper should also include a more thorough comparison with existing methods, including a discussion of the advantages and disadvantages of each approach. This should include a comparison of the performance of the proposed method with existing methods on a wider range of datasets, and a discussion of the specific scenarios where the proposed method is expected to perform well or poorly.

Finally, the paper should include a more detailed explanation of the evaluation metrics used, including the specific formulas used to calculate the scores. The authors should also discuss the limitations of the evaluation metrics and suggest alternative metrics that could be used to evaluate the performance of the proposed method. For example, the authors could explore the use of metrics that measure the interpretability of the table-tree or the robustness of the method to noisy data. The paper should also include a more detailed discussion of the related work, including a comparison of the proposed method with existing approaches and a discussion of the novelty of the proposed method. This should include a discussion of the specific challenges that the proposed method addresses and the advantages of the proposed method over existing approaches.

### Questions

1. How are the tables condensed and decomposed into the hierarchical structure? What specific algorithms or techniques are used in this process?
2. What is the computational complexity of the proposed method? How does it scale with increasing table size and complexity?
3. What are the limitations of the proposed method? How does it perform on tables with complex relationships between columns and rows?
4. How is the breadth-first search implemented? What data structures are used, and what is the impact of different search strategies on the final performance?

### Rating

3

### Confidence

4

**********
