### Summary

This paper proposes a new method for generating directed acyclic graphs (DAGs) using autoregressive diffusion models. The method leverages a bipartite graph representation to capture both node attributes and logical dependencies in DAGs. The authors evaluate their method on both synthetic and real-world datasets, demonstrating its effectiveness in generating high-quality DAGs with strong logical constraints.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to generating DAGs by combining autoregressive diffusion models with a bipartite graph representation. This approach is innovative and addresses the limitations of existing methods in capturing both node attributes and logical dependencies in DAGs.

2. The authors conduct extensive experiments on both synthetic and real-world datasets, demonstrating the effectiveness of their method in generating high-quality DAGs with strong logical constraints.

3. The paper is well-organized and clearly written, making it easy to follow the methodology and experimental results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the computational complexity of the proposed method, especially in comparison to existing approaches. Specifically, the analysis should include a breakdown of the time and space complexity for each step of the algorithm, such as the bipartite graph construction, diffusion process, and sampling. Furthermore, it would be beneficial to discuss how the complexity scales with the number of nodes and edges in the DAG, and whether the method is suitable for very large-scale graphs.

2. While the paper demonstrates the effectiveness of the proposed method on several datasets, it would be valuable to explore its performance on a wider range of graph types and sizes. For instance, the evaluation could include graphs with different topological structures, such as trees, meshes, or random graphs, and graphs with varying degrees of sparsity and density. This would provide a more comprehensive understanding of the method's strengths and limitations.

### Suggestions

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the time and space requirements for each component of their method. This should include the construction of the bipartite graph, the diffusion process, and the sampling procedure. For example, the authors should specify the number of operations required for each layer of the diffusion process and how this scales with the size of the bipartite graph. Furthermore, they should discuss the memory requirements of the algorithm, especially when dealing with large graphs, and explore potential strategies for optimizing memory usage. A comparison of the computational complexity with existing DAG generation methods would also be beneficial, highlighting the advantages and disadvantages of the proposed approach in terms of computational efficiency. This analysis should be presented in a clear and concise manner, possibly using Big O notation to describe the asymptotic behavior of the complexity.

To enhance the evaluation of the proposed method, the authors should consider a more diverse set of graph types and sizes. This could include graphs with different topological structures, such as trees, meshes, or random graphs, which would provide a more comprehensive understanding of the method's generalizability. Additionally, the evaluation should include graphs with varying degrees of sparsity and density to assess the method's performance under different conditions. For instance, the authors could generate graphs with different average node degrees and analyze the impact of this parameter on the quality of the generated DAGs. Furthermore, the authors should explore the performance of their method on larger graphs, beyond the 300 nodes used in the current experiments, to demonstrate its scalability and applicability to real-world scenarios. This could involve testing the method on graphs with thousands or millions of nodes, if computationally feasible, or by using techniques such as graph sampling or parallelization to handle larger graphs.

Finally, the authors should provide a more in-depth discussion of the limitations of their method and potential directions for future research. This could include a discussion of the types of graphs that the method is not well-suited for, and the potential challenges in applying the method to very large-scale graphs. For example, the authors could discuss the limitations of the bipartite graph representation for certain types of DAGs, or the challenges in capturing complex logical dependencies using the diffusion process. Furthermore, the authors should suggest potential avenues for future research, such as exploring alternative graph representations or diffusion processes, or developing more efficient algorithms for generating large-scale DAGs. This would provide a more balanced and comprehensive view of the method and its potential impact on the field.

### Questions

See weaknesses.

### Rating

6

### Confidence

2

**********
