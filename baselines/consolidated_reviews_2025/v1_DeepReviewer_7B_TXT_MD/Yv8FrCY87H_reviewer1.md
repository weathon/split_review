### Summary

The paper introduces a novel approach called "Tree-of-Table" designed to enhance the reasoning capabilities of large language models (LLMs) when dealing with large and complex tabular data. The method involves three main steps: table condensation, tree-based decomposition, and table-tree execution. By structuring table understanding as a hierarchical reasoning process, Tree-of-Table aims to improve accuracy and efficiency in tasks such as question answering and fact verification over large datasets. The authors demonstrate that their approach outperforms existing methods on several benchmark datasets, including WikiTQ, TableFact, FeTaQA, and BIRD, highlighting its potential for advancing table understanding in real-world applications.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper is well-written and easy to follow, with clear explanations of the proposed method and its components. The authors provide a detailed description of the Tree-of-Table approach, including the table condensation and decomposition steps, which are essential for understanding how the method works. The experimental setup is comprehensive, with evaluations conducted on multiple datasets, including WikiTQ, TableFact, FeTaQA, and BIRD. The results show that Tree-of-Table outperforms existing methods, demonstrating its effectiveness in improving the reasoning capabilities of LLMs for tabular data. The paper also includes an efficiency analysis, which highlights the computational advantages of the proposed method, particularly in terms of the number of generated samples required to achieve accurate answers.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's contribution is somewhat limited, as it primarily focuses on applying existing techniques such as table condensation and tree-based decomposition to the problem of table understanding. While the Tree-of-Table approach is innovative in its combination of these techniques, the individual components lack significant novelty. The method's reliance on established concepts may limit its impact on the field, as it does not introduce groundbreaking ideas or methodologies. The core idea of decomposing complex tasks into smaller sub-tasks is well-established, and the paper does not present a novel way of implementing this decomposition for tabular data. The table condensation step, while useful, is a straightforward application of existing summarization techniques, and the tree-based decomposition, while presented as a key contribution, is essentially a standard tree structure used for hierarchical organization. The lack of a truly novel algorithmic contribution is a significant weakness.
2. The paper lacks a detailed discussion of the limitations of the Tree-of-Table approach. While the authors mention that the method may require careful calibration to balance depth and breadth effectively, they do not provide a thorough analysis of potential failure cases or scenarios where the method might not perform well. For instance, the paper does not explore how the method handles tables with complex relationships between columns or rows, or how it deals with noisy or incomplete data. A more comprehensive discussion of these limitations would provide a more balanced view of the method's applicability and robustness. The paper should also discuss the computational cost associated with building and executing the tree structure, especially for very large tables, and how this cost scales with the size of the input.
3. The paper does not provide a clear explanation of how the Tree-of-Table approach handles tables with complex relationships between columns or rows. The method's reliance on a hierarchical structure may not be suitable for tables where relationships are not easily decomposable into independent sub-tasks. For example, in a table with columns representing different time points and rows representing different entities, the relationships between columns are sequential and not easily broken down into independent branches. The paper should provide a more detailed explanation of how the method handles such cases and how it ensures that the hierarchical structure accurately reflects the underlying data relationships. Furthermore, the paper does not discuss how the method handles tables with a large number of columns or rows, and how it ensures that the hierarchical structure remains manageable and does not become computationally expensive.

### Suggestions

The paper would benefit significantly from a more detailed explanation of the tree construction process, particularly how the method handles tables with complex relationships between columns and rows. The current description lacks the necessary specifics to understand how the hierarchical structure is built and how it ensures that the relationships are accurately represented. For instance, the paper should clarify how the method determines the optimal branching factor for the tree and how it handles cases where the relationships are not easily decomposable into independent sub-tasks. A concrete example, such as a table with columns representing different time points and rows representing different entities, would be beneficial to illustrate how the method handles sequential relationships. The authors should also discuss how the method handles tables with a large number of columns or rows, and how it ensures that the hierarchical structure remains manageable and does not become computationally expensive. Furthermore, the paper should provide a more detailed explanation of the table condensation step, including the specific algorithms or techniques used and how they are adapted to the specific characteristics of tabular data. The paper should also discuss the limitations of the table condensation step and how it might affect the overall performance of the method.

To address the lack of novelty, the authors should explore more innovative ways of implementing the tree-based decomposition for tabular data. Instead of relying on a standard tree structure, the paper could investigate adaptive tree structures that are tailored to the specific characteristics of the input data. For example, the paper could explore the use of graph-based structures that can capture more complex relationships between columns and rows. The paper should also discuss how the method handles noisy or incomplete data, and how it ensures that the hierarchical structure remains accurate and reliable. The authors should also consider incorporating techniques from other areas of machine learning, such as reinforcement learning, to optimize the tree structure and improve the overall performance of the method. A more detailed analysis of the computational cost associated with building and executing the tree structure is also needed, especially for very large tables.

Finally, the paper should include a more comprehensive discussion of the limitations of the Tree-of-Table approach. The authors should explore potential failure cases and scenarios where the method might not perform well, such as tables with highly complex relationships or tables with a large number of columns or rows. The paper should also discuss the sensitivity of the method to different hyperparameters and how these parameters should be tuned for optimal performance. A more thorough analysis of the method's robustness and generalizability would provide a more balanced view of its applicability and limitations. The paper should also include a comparison with other state-of-the-art methods for tabular data understanding, to demonstrate the advantages and disadvantages of the proposed approach.

### Questions

1. How does the Tree-of-Table approach handle tables with complex relationships between columns or rows? Are there specific strategies or algorithms used to manage these relationships effectively?
2. What are the limitations of the Tree-of-Table approach, and in what scenarios might it not perform well? How does the method handle noisy or incomplete data?
3. How does the computational cost of the Tree-of-Table approach scale with the size of the input table? Are there any optimizations or trade-offs that can be made to improve efficiency for very large tables?

### Rating

3

### Confidence

4

**********
