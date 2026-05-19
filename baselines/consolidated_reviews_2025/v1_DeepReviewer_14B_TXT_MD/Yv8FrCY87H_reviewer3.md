### Summary

This paper introduces a Tree-of-Table method to enhance large language models (LLMs) for large-scale table understanding. The approach employs Table Condensation and Decomposition to distill and reorganize relevant data into a manageable format, followed by the construction of a hierarchical Table-Tree that facilitates tree-structured reasoning. The authors conduct experiments across diverse datasets, including WikiTQ, TableFact, FeTaQA, and BIRD, demonstrating that Tree-of-Table sets a new benchmark with superior performance, showcasing remarkable efficiency and generalization capabilities in large-scale table reasoning.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-organized and easy to follow.
2. The proposed Tree-of-Table method is intuitive and effective.
3. The authors conduct experiments across diverse datasets, including WikiTQ, TableFact, FeTaQA, and BIRD, demonstrating that Tree-of-Table sets a new benchmark with superior performance, showcasing remarkable efficiency and generalization capabilities in large-scale table reasoning.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not very innovative, as it is a simple combination of existing methods.
2. The paper lacks a detailed analysis of the experimental results. For example, the authors should provide more insights into why the Tree-of-Table method performs better than other methods on the BIRD dataset. Specifically, the analysis should delve into the types of questions and table structures where the method excels or struggles, and how the tree structure facilitates reasoning in these cases. A breakdown of performance based on question complexity or table size would be beneficial.
3. The paper does not provide a detailed analysis of the computational cost of the proposed method. For example, the authors should provide more information about the time and memory requirements of the Tree-of-Table method compared to other methods. This should include a breakdown of the time spent on each stage of the method (condensation, decomposition, tree construction, and reasoning) and how these costs scale with table size and complexity. Furthermore, the memory footprint of the tree structure should be analyzed, especially for large tables.

### Suggestions

The paper would benefit from a more in-depth analysis of the Tree-of-Table method's performance across different types of questions and table structures. For instance, the authors could categorize questions based on their complexity (e.g., simple lookup, aggregation, multi-step reasoning) and analyze how the method performs on each category. Similarly, tables could be categorized based on their size, number of columns, and presence of hierarchical relationships. This would provide a more nuanced understanding of the method's strengths and weaknesses. Furthermore, the authors should investigate the impact of the tree structure on the reasoning process. For example, how does the depth and branching factor of the tree affect performance? Are there specific types of questions or tables where a deeper or wider tree is more beneficial? This analysis could provide valuable insights into the design choices of the method.

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the time and memory requirements of each stage of the Tree-of-Table method. This should include the time spent on table condensation, decomposition, tree construction, and reasoning. The analysis should also consider how these costs scale with the size and complexity of the input tables. For example, how does the time required for tree construction change as the number of rows and columns increases? What is the memory footprint of the tree structure for different table sizes? This analysis should be compared to the computational costs of other methods, providing a clear picture of the trade-offs involved. The authors could also explore optimization techniques to reduce the computational overhead of their method, such as pruning the tree or using more efficient data structures.

Finally, the authors should provide a more detailed explanation of the Table Condensation process. While the paper mentions that the method identifies relevant portions of the tables, it lacks a clear description of how this is achieved. What specific criteria are used to determine which parts of the table are relevant? How does the method handle complex table structures with multiple levels of hierarchy? A more detailed explanation of this process would help readers understand the method's inner workings and its limitations. The authors could also explore alternative condensation strategies and compare their performance to the proposed approach. This would provide a more comprehensive evaluation of the method's effectiveness.

### Questions

Please refer to the Weaknesses.

### Rating

6

### Confidence

4

**********
