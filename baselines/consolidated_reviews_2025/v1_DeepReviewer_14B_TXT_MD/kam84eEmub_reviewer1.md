### Summary

This paper proposes a novel DAG generator model, which decomposes the generation of a DAG into a sequence of generating sets of nodes (and accompanying edges) layer by layer. Each layer is generated autoregressively conditioned on the previous ones, and the nodes and edges within each layer are generated using a diffusion model. The authors also propose a flexible quality-efficiency trade-off scheme by adjusting the number of denoising steps according to the layer index. The authors conducted experiments on a synthetic dataset and two real-world datasets, demonstrating the superiority of the proposed model over baseline models in terms of validity, statistical properties, and benchmarking performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The proposed model makes sense and is novel. It effectively leverages the strengths of both autoregressive and diffusion models, avoiding the inefficient one-node-at-a-time generation of autoregressive models while also addressing the issue of ignoring topology that may arise when using a diffusion model to generate a DAG directly.
- The experiments are comprehensive and convincing. The authors conducted extensive experiments on both synthetic and real-world datasets, comparing the proposed model with several baseline models and demonstrating its superiority in various aspects. The experiments also validate the effectiveness of the proposed flexible quality-efficiency trade-off scheme.

### Weaknesses

#### Some Related Works


#### comment

 - The description of the proposed model is somewhat unclear, particularly regarding the inputs and outputs of each module and how they interact. Specifically, the paper lacks detail on how the autoregressive component conditions on previous layers when generating a new layer. The exact mechanism by which the layer index is encoded and used within the diffusion model is also not sufficiently explained. Furthermore, the paper does not clearly specify the architecture of the denoising network used in the diffusion process, making it difficult to assess the model's complexity and potential limitations.
- The paper lacks a complexity analysis of the proposed model. It is unclear how the computational cost scales with the number of nodes, layers, and denoising steps. This analysis is crucial for understanding the practical applicability of the model, especially for large-scale DAG generation. The absence of a detailed analysis makes it difficult to compare the proposed model's efficiency with other potential approaches.
- The experiments are conducted on relatively small datasets, with the maximum number of nodes being around 400. While the authors claim that this is sufficient for benchmarking, it is unclear how the model would perform on much larger DAGs, which are common in many real-world applications. The lack of experiments on larger graphs raises concerns about the model's scalability and generalizability.

### Suggestions

To address the lack of clarity in the model description, the authors should provide a more detailed explanation of the inputs and outputs of each module, including the specific data structures used. They should also clarify how the autoregressive component conditions on previous layers, perhaps by providing a concrete example of how the layer index is encoded and used within the diffusion model. A diagram illustrating the flow of information between modules would be beneficial. Furthermore, the authors should specify the architecture of the denoising network, including the number of layers, the type of activation functions, and the number of parameters. This would allow for a better understanding of the model's complexity and potential limitations. It would also be helpful to include a pseudocode representation of the algorithm to clarify the step-by-step process.

To address the lack of complexity analysis, the authors should provide a detailed breakdown of the computational cost of each step in the proposed model, including the autoregressive component and the diffusion process. This analysis should consider the number of nodes, layers, and denoising steps, and should clearly state the time and space complexity of the model. The authors should also compare the complexity of their model with that of the baseline models, highlighting the trade-offs between performance and efficiency. This analysis should be presented in a way that is easy to understand and should include both theoretical analysis and empirical results. It would be beneficial to include a table summarizing the time and space complexity of each component of the model.

Finally, to address the concerns about scalability, the authors should conduct experiments on larger datasets with significantly more nodes. This could involve generating synthetic datasets with varying sizes or using real-world datasets with larger DAGs. The authors should also analyze the performance of the model on these larger datasets, paying particular attention to the computational cost and memory usage. It would be beneficial to include a plot showing how the performance of the model scales with the number of nodes. This would provide a better understanding of the model's limitations and potential for use in real-world applications. The authors should also discuss any potential bottlenecks or limitations that may arise when scaling the model to larger graphs.

### Questions

- Could the authors provide a complexity analysis of the proposed model and compare it with the baseline models?
- How does the proposed model perform on larger DAGs, e.g., with 1,000 or 10,000 nodes? What are the limitations or challenges in scaling the model to larger graphs?
- Could the authors provide more details on the proposed model, e.g., input/output of each module, how they interact with each other, and how the layer index is encoded and used in the model?

### Rating

6

### Confidence

4

**********
