### Summary

This paper proposes a novel multi-view learning framework called Hebbian View Orthogonal Projection (HVOP), which aims to address the problem of view forgetting in dynamic multi-view learning. The proposed method is inspired by the biological processes in the human brain, such as Hebbian learning and orthogonal projection. The framework is designed to integrate and transfer knowledge across multiple views while retaining previously learned information. The authors conduct experiments on node classification tasks and demonstrate the effectiveness of the proposed method compared to traditional multi-view learning methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors clearly explain the motivation behind the proposed method and the underlying biological inspiration.
2. The proposed method is novel and addresses a significant problem in multi-view learning, which is the issue of view forgetting in dynamic environments.
3. The authors provide a thorough theoretical analysis of the proposed method and its connection to biological processes.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed explanation of the specific implementation of the orthogonal projection and Hebbian learning components. The description of how the orthogonal projection is achieved and how the Hebbian learning rule is applied to the graph structure is not sufficiently clear. For example, it is unclear how the projection matrix is updated and how the graph structure is modified to incorporate the Hebbian learning rule. The lack of detail makes it difficult to reproduce the results and understand the inner workings of the method.
2. The experiments are limited to node classification tasks, which may not fully demonstrate the effectiveness of the proposed method in other types of multi-view learning tasks. The paper should include experiments on other tasks, such as clustering or dimensionality reduction, to show the generalizability of the method. The current experiments do not provide sufficient evidence that the proposed method is effective in a broader range of multi-view learning scenarios.
3. The paper does not provide a detailed analysis of the computational complexity of the proposed method. The authors should provide a more detailed analysis of the time and space complexity of the proposed method, especially when dealing with large-scale datasets. The lack of computational complexity analysis makes it difficult to assess the scalability of the method and its suitability for real-world applications.

### Suggestions

The authors should provide a more detailed explanation of the implementation of the orthogonal projection and Hebbian learning components. Specifically, they should clarify how the projection matrix is updated and how the graph structure is modified to incorporate the Hebbian learning rule. A step-by-step description of the algorithm, including the mathematical formulations and implementation details, would greatly enhance the clarity and reproducibility of the method. For example, the authors could provide a pseudocode representation of the algorithm, detailing the steps involved in the orthogonal projection and Hebbian learning processes. This would allow other researchers to implement the method and build upon it.

To address the limited scope of the experiments, the authors should include experiments on other multi-view learning tasks, such as clustering or dimensionality reduction. These experiments would provide a more comprehensive evaluation of the method's effectiveness and generalizability. For example, the authors could evaluate the method on a clustering task using a multi-view dataset, or a dimensionality reduction task using a different type of multi-view data. This would demonstrate the versatility of the method and its applicability to a broader range of multi-view learning problems. The authors should also compare the performance of the proposed method with state-of-the-art methods in these tasks.

Finally, the authors should provide a detailed analysis of the computational complexity of the proposed method. This analysis should include both time and space complexity, and should consider the impact of different parameters on the computational cost. The authors should also discuss the scalability of the method and its suitability for large-scale datasets. For example, the authors could provide a table showing the time and space complexity of the method as a function of the number of nodes, edges, and views. This would allow readers to assess the practical applicability of the method and its potential for real-world applications.

### Questions

1. How does the proposed method handle the issue of view forgetting in dynamic environments with a large number of views?
2. Can the authors provide more details on the computational complexity of the proposed method and its scalability to large-scale datasets?

### Rating

6

### Confidence

3

**********
