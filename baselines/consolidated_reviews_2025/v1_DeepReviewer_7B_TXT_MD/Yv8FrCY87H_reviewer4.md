### Summary

The paper presents a new approach for LLMs to perform reasoning on tabular data. The proposed method first condenses the table into a smaller, more manageable table, then decomposes the table into sub-tables, and finally executes the sub-tables in a breadth-first manner. The method is evaluated on four datasets, showing improved performance over existing methods.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The method is well-motivated and well-explained.
- The experimental results show the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is not very novel. The idea of condensing and decomposing tables has been explored in previous works, such as Dater and Chain-of-Table. The main difference of the proposed method is that it performs condensation and decomposition in a table-agnostic manner, whereas previous works perform table decomposition based on the context of the question.
- The paper lacks a thorough analysis of the computational efficiency of the proposed method. The authors should provide a detailed comparison of the time and memory consumption of the proposed method with existing methods, including the time taken for table condensation, decomposition, and execution.
- The paper does not discuss the limitations of the proposed method. For example, how does the method handle tables with a large number of columns or rows? How does the method handle tables with complex relationships between columns and rows?

### Suggestions

The paper should provide a more detailed comparison with existing methods, specifically focusing on the differences in how table decomposition is performed. While the authors mention that their method is table-agnostic, a more thorough analysis of the impact of this design choice is needed. For example, the paper could include experiments that compare the performance of the proposed method with methods that perform table decomposition based on the context of the question, to better understand the trade-offs of the proposed approach. Furthermore, the paper should include a more detailed analysis of the computational cost of the proposed method. This should include a breakdown of the time and memory consumption for each step of the method, including table condensation, decomposition, and execution. This analysis should be compared with the computational cost of existing methods to provide a clear understanding of the efficiency of the proposed method. The paper should also discuss the limitations of the proposed method in more detail. For example, the paper should discuss how the method handles tables with a large number of columns or rows, and how it handles tables with complex relationships between columns and rows. The paper should also discuss the sensitivity of the method to the quality of the condensed and decomposed tables. For example, how does the performance of the method change if the condensed table is too small or the decomposed tables are too large? 

To improve the evaluation, the authors should consider including a more diverse set of datasets, including datasets with different characteristics, such as different table sizes, different types of relationships between columns and rows, and different types of questions. This would provide a more comprehensive evaluation of the proposed method and its limitations. The paper should also include a more detailed analysis of the results, including error analysis and ablation studies. For example, the paper could include an ablation study that examines the impact of each step of the method on the overall performance. This would help to identify the key components of the method that contribute to its effectiveness. The paper should also discuss the potential for future work, such as exploring different table condensation and decomposition techniques, or incorporating additional information into the method, such as the context of the question.

Finally, the paper should provide a more detailed explanation of the implementation details of the proposed method. This should include a description of the algorithms used for table condensation and decomposition, as well as the specific parameters used for the method. This would make it easier for other researchers to reproduce the results and build upon the proposed method. The paper should also include a discussion of the potential for parallelization of the method, as well as the potential for optimizing the method for large-scale datasets. This would help to identify potential areas for future research and development.

### Questions

- How does the proposed method compare with existing methods in terms of computational efficiency?
- How does the proposed method handle tables with a large number of columns or rows?
- How does the proposed method handle tables with complex relationships between columns and rows?

### Rating

5

### Confidence

4

**********
