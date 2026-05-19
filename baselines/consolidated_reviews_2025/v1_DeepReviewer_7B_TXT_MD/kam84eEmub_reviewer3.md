### Summary

This paper proposes a novel autoregressive diffusion model for DAG generation. The proposed method leverages the bipartite graph representation of DAGs and autoregressive generation to capture the dependencies between nodes and edges. The authors demonstrate the effectiveness of the proposed method through experiments on synthetic and real-world datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method is novel and interesting. The idea of leveraging autoregressive diffusion models for DAG generation is novel and promising. The proposed method leverages the bipartite graph representation of DAGs and autoregressive generation to capture the dependencies between nodes and edges.

2. The authors conduct extensive experiments on both synthetic and real-world datasets to demonstrate the effectiveness of the proposed method. The experimental results show that the proposed method outperforms existing methods in terms of generation quality and efficiency.

3. The paper is well-written and easy to follow. The authors provide a clear explanation of the proposed method and the experimental setup. The experimental results are presented in a clear and concise manner.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method relies on a bipartite graph representation of DAGs, which may not be suitable for all types of DAGs. For example, DAGs with complex hierarchical structures or cyclic dependencies may not be well-represented by bipartite graphs. The paper does not discuss the limitations of this representation or how it might affect the performance of the proposed method on different types of DAGs.

2. The proposed method is computationally expensive, especially for large-scale DAGs. The autoregressive diffusion process requires multiple iterations to generate each node and edge, which can be time-consuming for large DAGs. The paper does not provide a detailed analysis of the computational complexity of the proposed method or discuss potential strategies for improving its efficiency.

3. The paper does not provide a clear explanation of how the proposed method handles the trade-off between generation quality and efficiency. The authors mention that the proposed method can generate high-quality DAGs with a single layer, but they do not provide a detailed analysis of how the number of layers affects the generation quality and efficiency. The paper also does not discuss how the proposed method can be used to generate DAGs with different levels of complexity.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of using a bipartite graph representation for DAGs. Specifically, the authors should analyze how the structure of the bipartite graph impacts the ability to capture complex dependencies within the original DAG. For instance, if the bipartite graph representation leads to a loss of information about the original DAG's structure, this could significantly affect the quality of the generated graphs. The authors should consider providing examples of DAGs where the bipartite representation is particularly effective or ineffective, and discuss the implications for the proposed method. Furthermore, it would be beneficial to explore alternative graph representations that might be more suitable for capturing complex DAG structures, such as hypergraphs or other hierarchical representations. This would provide a more comprehensive understanding of the proposed method's applicability and limitations.

To address the computational expense of the proposed method, the authors should provide a more detailed analysis of the time and space complexity of the autoregressive diffusion process. This analysis should include a breakdown of the computational cost associated with each step of the process, such as the forward and reverse diffusion steps, and the autoregressive generation of nodes and edges. The authors should also discuss potential strategies for improving the efficiency of the method, such as using more efficient sampling techniques or parallelizing the computation. Furthermore, it would be helpful to compare the computational cost of the proposed method with other DAG generation methods, to provide a better understanding of its relative efficiency. This analysis should also consider the impact of the number of layers on the computational cost, and how this trade-off can be managed to generate DAGs of varying complexity.

Finally, the paper should provide a more detailed explanation of how the proposed method balances generation quality and efficiency. The authors should analyze how the number of layers affects the quality of the generated DAGs, and provide a clear explanation of how the method can be used to generate DAGs with different levels of complexity. This analysis should include a discussion of the trade-offs between the number of layers, the generation quality, and the computational cost. The authors should also provide guidelines on how to choose the optimal number of layers for a given application, based on the desired level of complexity and the available computational resources. This would make the proposed method more practical and easier to use for researchers and practitioners.

### Questions

1. How does the proposed method handle the trade-off between generation quality and efficiency? Can the method generate high-quality DAGs with a single layer, or does it require multiple layers to achieve good results?

2. What is the computational complexity of the proposed method, and how does it compare to other DAG generation methods? Can the method be used to generate large-scale DAGs efficiently?

3. How does the proposed method handle the generation of DAGs with complex hierarchical structures or cyclic dependencies? Are there any limitations to the proposed method in terms of the types of DAGs it can generate?

### Rating

6

### Confidence

3

**********
