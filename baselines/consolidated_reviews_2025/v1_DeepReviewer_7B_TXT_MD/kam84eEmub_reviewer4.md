### Summary

This paper introduces a novel autoregressive diffusion model for directed acyclic graph (DAG) generation. The authors propose a bipartite graph representation of DAGs, which allows for a layerwise node-by-node generation process. The method is evaluated on both synthetic and real-world datasets, demonstrating its effectiveness in generating high-quality DAGs with strong logical dependencies.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel approach to DAG generation by leveraging autoregressive diffusion models and bipartite graph representation. This is a creative combination of existing techniques that addresses the limitations of previous methods in capturing logical dependencies.

2. The authors provide a thorough evaluation of their method on both synthetic and real-world datasets. The experiments are well-designed and provide strong evidence of the method's effectiveness.

3. The paper is well-written and easy to follow. The authors clearly explain the proposed method and its advantages over existing approaches.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the computational complexity of the proposed method, especially in comparison to existing approaches. Specifically, the analysis should include a breakdown of the time and space complexity for each step of the algorithm, such as the bipartite graph construction, diffusion process, and sampling. Furthermore, it would be beneficial to discuss how the complexity scales with the number of nodes and edges in the DAG, and whether the method is suitable for very large-scale graphs.

2. While the paper demonstrates the effectiveness of the proposed method on several datasets, it would be valuable to explore its performance on a wider range of graph types and sizes. For instance, the evaluation could include graphs with different topological structures, such as trees, meshes, or random graphs, and graphs with varying degrees of sparsity and density. This would provide a more comprehensive understanding of the method's strengths and limitations.

### Suggestions

To further strengthen the paper, I suggest a more in-depth analysis of the computational aspects of the proposed method. While the authors mention the use of a bipartite graph representation and autoregressive diffusion, a detailed breakdown of the time and space complexity for each component would be highly beneficial. For instance, providing a Big O notation analysis for the bipartite graph construction, the diffusion process, and the sampling procedure would offer a clearer understanding of the method's scalability. Additionally, it would be valuable to explore how these complexities scale with the number of nodes (N) and edges (E) in the DAG. This could involve analyzing the impact of different graph densities and topologies on the computational cost. Furthermore, discussing potential optimizations or trade-offs to improve efficiency for large-scale graphs would be a valuable addition. For example, exploring parallelization strategies or approximation techniques for the diffusion process could enhance the method's practical applicability.

Expanding the experimental evaluation to include a broader range of graph types and sizes would also significantly enhance the paper's impact. While the current evaluation on synthetic and real-world datasets is promising, exploring the method's performance on graphs with different structural properties would provide a more comprehensive assessment. Specifically, including graphs with varying topological structures, such as trees, meshes, or random graphs, would help to understand the method's generalizability. Additionally, evaluating the method's performance on graphs with different degrees of sparsity and density would provide insights into its robustness. For instance, testing on graphs with varying average node degrees or edge densities could reveal potential limitations or strengths of the proposed approach. This could involve generating graphs with specific properties using established graph generation models and evaluating the performance of the proposed method on these datasets. Such an analysis would provide a more complete picture of the method's applicability and limitations.

Finally, while the paper focuses on DAG generation, briefly discussing potential extensions or modifications to the proposed method for generating other types of graphs could be a valuable addition. For example, exploring how the bipartite graph representation and autoregressive diffusion framework could be adapted for undirected graphs or graphs with cyclic dependencies would demonstrate the broader applicability of the proposed approach. This could involve discussing the necessary modifications to the graph representation and the diffusion process to accommodate different graph structures. Additionally, providing a high-level overview of how the method could be extended to handle attributed graphs, where nodes and edges have additional features, would further highlight the versatility of the proposed approach. This could involve discussing the integration of node and edge attributes into the diffusion process and the impact on the generation quality.

### Questions

1. How does the proposed method handle the generation of very large-scale DAGs, and what are the computational limitations of the approach?

2. How does the proposed method compare to other generative models in terms of computational efficiency, especially for large-scale DAGs?

### Rating

8

### Confidence

3

**********
