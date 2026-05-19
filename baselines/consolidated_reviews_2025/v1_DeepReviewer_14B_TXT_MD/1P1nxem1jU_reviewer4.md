### Summary

This paper proposes a new graph data augmentation method based on spectral graph theory. The authors first show that the low-frequency eigenvalues are closely related to the graph properties and then propose to augment graphs by only changing the high-frequency eigenvalues. The proposed method is evaluated on 21 real-world datasets across three different domains.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is novel and interesting.
- The experimental results are comprehensive and convincing.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is based on the eigen-decomposition of the Laplacian matrix, which is computationally expensive. How does the proposed method perform on large graphs?
- The paper does not provide a clear explanation of how the proposed method can be applied to directed graphs.
- The paper does not provide a clear explanation of how the proposed method can be applied to dynamic graphs.

### Suggestions

The paper should include a more detailed analysis of the computational complexity of the proposed method, especially concerning the eigen-decomposition of the Laplacian matrix. While the authors mention that it is computationally expensive, a more rigorous analysis, perhaps including a comparison with other graph augmentation techniques, would be beneficial. Specifically, the authors should discuss the time complexity in terms of the number of nodes and edges, and how this scales with larger graphs. Furthermore, it would be helpful to see a breakdown of the computational cost associated with each step of the proposed method, such as the eigen-decomposition, the modification of high-frequency eigenvalues, and the reconstruction of the augmented graph. This would allow readers to better understand the practical limitations of the method and its applicability to different graph sizes. The authors could also consider providing empirical results on the runtime of the method for different graph sizes to demonstrate its scalability.

Regarding the applicability of the proposed method to directed graphs, the paper should provide a more detailed explanation of how the Laplacian matrix is defined for directed graphs and how the eigen-decomposition is performed in this context. The authors should discuss the specific challenges associated with applying spectral graph theory to directed graphs, such as the potential for complex eigenvalues and the need for alternative definitions of the Laplacian matrix. Furthermore, the authors should provide a clear explanation of how the proposed method can be adapted to handle directed graphs, including any modifications to the algorithm or the choice of parameters. It would also be beneficial to include experimental results on directed graph datasets to demonstrate the effectiveness of the proposed method in this setting. The authors should also discuss the limitations of the proposed method for directed graphs and potential future research directions to overcome these limitations.

Finally, the paper should address the applicability of the proposed method to dynamic graphs. The authors should discuss the challenges of applying spectral graph theory to dynamic graphs, such as the need to update the Laplacian matrix and the eigen-decomposition over time. The authors should propose a strategy for handling temporal changes in the graph structure, such as using a sliding window approach or incremental eigen-decomposition techniques. Furthermore, the authors should discuss the potential for using the proposed method to augment dynamic graphs in a way that preserves the temporal dependencies in the graph. It would be beneficial to include experimental results on dynamic graph datasets to demonstrate the effectiveness of the proposed method in this setting. The authors should also discuss the limitations of the proposed method for dynamic graphs and potential future research directions to overcome these limitations.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
