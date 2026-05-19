### Summary

This paper proposes a novel method for generating directed acyclic graphs (DAGs) by leveraging autoregressive diffusion models. The authors address the challenges posed by the structural and logical dependencies inherent in DAGs, which have been a persistent issue in existing generative models. By representing DAGs as sequences of bipartite graphs, the proposed method enables the sequential generation of DAGs in a layer-by-layer manner, effectively capturing both node attributes and logical dependencies. Extensive experiments demonstrate that the proposed method outperforms existing models in terms of expressiveness and generalization, particularly for large-scale DAGs. The authors also highlight the potential applications of their method in benchmarking computing systems and creating synthetic datasets for benchmarking deep learning models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to generating directed acyclic graphs (DAGs) by combining autoregressive diffusion models with a bipartite graph representation. This innovative methodology addresses the limitations of existing models in capturing both node attributes and logical dependencies in DAGs.
2. The paper provides extensive experimental results on both synthetic and real-world datasets, demonstrating the effectiveness of the proposed method. The authors also highlight the potential applications of their method in benchmarking computing systems and creating synthetic datasets for benchmarking deep learning models.
3. The paper is well-written and organized, with clear explanations of the proposed method and experimental results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the computational complexity of the proposed method, especially in comparison to existing approaches. Specifically, the analysis should include a breakdown of the time and space complexity for each step of the algorithm, such as the bipartite graph construction, diffusion process, and sampling. Furthermore, it would be beneficial to discuss how the complexity scales with the number of nodes and edges in the DAG, and whether the method is suitable for very large-scale graphs.
2. While the paper demonstrates the effectiveness of the proposed method on several datasets, it would be valuable to explore its performance on a wider range of graph types and sizes. For instance, the evaluation could include graphs with different topological structures, such as trees, meshes, or random graphs, and graphs with varying degrees of sparsity and density. This would provide a more comprehensive understanding of the method's strengths and limitations.

### Suggestions

To enhance the paper, the authors should provide a more thorough analysis of the computational complexity of their proposed method. This should include a detailed breakdown of the time and space complexity for each step of the algorithm, such as the construction of the bipartite graph, the diffusion process, and the sampling procedure. The analysis should explicitly consider how these complexities scale with the number of nodes and edges in the DAG, and whether the method is suitable for very large-scale graphs. For example, the authors could analyze the number of operations required for each layer of the diffusion process and how this scales with the size of the bipartite graph. Furthermore, it would be beneficial to compare the computational complexity of their method with existing approaches for DAG generation, highlighting the advantages and disadvantages of each method in terms of computational efficiency. This analysis should also consider the memory requirements of the algorithm, especially when dealing with large graphs, and discuss potential strategies for optimizing memory usage.

In addition to the computational complexity analysis, the authors should also expand their experimental evaluation to include a wider range of graph types and sizes. This should include graphs with different topological structures, such as trees, meshes, or random graphs, and graphs with varying degrees of sparsity and density. For example, the authors could evaluate the performance of their method on synthetic graphs generated using different graph generation models, such as the Erdős–Rényi model or the Barabási–Albert model. This would provide a more comprehensive understanding of the method's strengths and limitations across different graph structures. Furthermore, the authors should also consider evaluating the method on real-world datasets with varying characteristics, such as social networks, citation networks, or biological networks. This would demonstrate the practical applicability of the method and its ability to generalize to different types of graphs. The evaluation should also include a comparison of the generated graphs with real-world graphs in terms of various graph properties, such as degree distribution, clustering coefficient, and path length.

Finally, the authors should also discuss the limitations of their method and potential directions for future research. This should include a discussion of the types of graphs that the method is not well-suited for, and the potential challenges in applying the method to very large-scale graphs. For example, the authors could discuss the limitations of the bipartite graph representation for certain types of DAGs, or the challenges in capturing complex logical dependencies using the diffusion process. Furthermore, the authors should also suggest potential directions for future research, such as exploring alternative graph representations or diffusion processes, or developing more efficient algorithms for generating large-scale DAGs. This would provide a more balanced and comprehensive view of the method and its potential impact on the field.

### Questions

1. How does the proposed method handle the generation of very large-scale DAGs, and what are the computational limitations of the approach?
2. How does the proposed method compare to other generative models in terms of computational efficiency, especially for large-scale DAGs?

### Rating

6

### Confidence

3

**********
