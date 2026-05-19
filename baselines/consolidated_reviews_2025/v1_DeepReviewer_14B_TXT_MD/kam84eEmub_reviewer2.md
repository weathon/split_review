### Summary

This paper introduces a new autoregressive diffusion model for generating directed acyclic graphs (DAGs). The authors propose a novel approach to decouple strong node dependencies by interpreting the partial order of nodes as a sequence of bipartite graphs. The model leverages autoregressive generation to model directional dependencies and employs diffusion models to capture logical dependencies within each bipartite graph. The authors demonstrate the effectiveness of their approach through extensive experiments on both synthetic and real-world datasets, showing superior performance compared to existing DAG generative models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to DAG generation by combining autoregressive and diffusion models. The layerwise tokenization method is a creative way to decouple strong node dependencies, and the use of diffusion models to capture logical dependencies within each bipartite graph is innovative.
2. The paper is well-written and clearly explains the proposed method. The authors provide a thorough explanation of the layerwise tokenization, autoregressive generation, and diffusion-based generation processes. The experimental setup is well-described, and the results are presented in a clear and concise manner.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed model. It would be beneficial to understand how the model scales with the size of the DAGs and the number of layers. Specifically, the paper lacks a discussion on the time complexity of the diffusion process within each layer, and how this scales with the number of nodes and edges in the bipartite graphs. Furthermore, the memory requirements for storing intermediate diffusion states and the overall memory footprint of the model are not discussed, which is crucial for practical applications involving large DAGs.
2. The paper could benefit from a more in-depth discussion of the limitations of the proposed approach. For example, how does the model handle very large DAGs with thousands of nodes and edges? Are there any specific types of DAGs that the model struggles to generate? The paper should also address the potential for mode collapse in the diffusion process, and how this might affect the diversity of generated DAGs. It is also unclear how the model handles DAGs with complex hierarchical structures or those with highly variable node degrees.

### Suggestions

The paper should include a more rigorous analysis of the computational complexity of the proposed model. This should include a breakdown of the time complexity for each step of the generation process, including the autoregressive layer-wise generation and the diffusion process within each bipartite graph. The analysis should consider the number of nodes, edges, and layers, and should provide a clear understanding of how the model scales with these parameters. Furthermore, the memory requirements of the model should be analyzed, including the memory needed to store intermediate diffusion states and the overall memory footprint of the model. This analysis should be supported by empirical results on different sized DAGs to demonstrate the practical scalability of the approach. It would be beneficial to include a table or graph showing the relationship between DAG size and computational cost.

To address the limitations, the paper should include a more detailed discussion of the model's performance on very large DAGs, including those with thousands of nodes and edges. The authors should provide empirical results on such datasets, and discuss any challenges or limitations encountered. The paper should also explore the model's ability to generate different types of DAGs, including those with complex hierarchical structures or highly variable node degrees. It would be useful to include a qualitative analysis of the generated DAGs, highlighting any specific patterns or structures that the model struggles to capture. The authors should also discuss the potential for mode collapse in the diffusion process and how this might affect the diversity of generated DAGs. This could include an analysis of the generated DAG distributions and a discussion of any techniques used to mitigate mode collapse.

Finally, the paper should include a more detailed discussion of the model's sensitivity to hyperparameter settings. This should include an analysis of how different hyperparameter values affect the quality and diversity of the generated DAGs. The authors should also provide guidance on how to choose appropriate hyperparameter values for different datasets and applications. This could include a sensitivity analysis of the key hyperparameters, and a discussion of any techniques used to tune these parameters. It would be beneficial to include a table or graph showing the relationship between hyperparameter values and the performance of the model.

### Questions

1. How does the proposed model handle the generation of very large DAGs with complex dependencies? Are there any limitations in terms of scalability or computational cost?
2. What are the key factors that contribute to the superior performance of the proposed model compared to existing DAG generative models? Can the authors provide more insights into the specific advantages of their approach?
3. How sensitive is the proposed model to hyperparameter settings? Are there any specific hyperparameters that have a significant impact on the performance of the model?

### Rating

6

### Confidence

3

**********
