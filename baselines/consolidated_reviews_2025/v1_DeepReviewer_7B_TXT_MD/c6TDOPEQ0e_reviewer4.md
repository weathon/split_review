### Summary

This paper proposes LASP-2, a sequence parallelism (SP) approach designed to enhance the efficiency of linear attention models for handling long sequences. The authors identify that existing SP methods, such as LASP and Ring Attention, suffer from inefficient communication and computation, particularly when dealing with long sequences. To address these issues, LASP-2 reorganizes the computation and communication process to minimize communication overhead. The paper also introduces LASP-2H, an extension that combines linear and standard attention modules, enabling the model to handle both linear and standard attention layers. Experimental results demonstrate that LASP-2 and LASP-2H achieve throughput improvements of 15.2% over LASP and 36.6% over Ring Attention, respectively, on a Linear-Llama3 model with a 2048K sequence length. The paper also discusses the theoretical cost analysis of LASP-2 and LASP-2H, highlighting their efficiency in terms of communication and computation.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses a critical challenge in handling long sequences in linear attention models by proposing LASP-2, which optimizes sequence parallelism to reduce communication overhead. This is a significant contribution to the field of large language models, as it enables more efficient training and inference on long sequences.
2. The paper provides a theoretical cost analysis of LASP-2 and LASP-2H, demonstrating their efficiency in terms of communication and computation. This analysis helps to validate the effectiveness of the proposed methods and provides a solid foundation for future research.
3. The paper is well-written and easy to follow, with clear explanations of the proposed methods and experimental results. The authors also provide a comprehensive comparison of LASP-2 with existing methods, such as LASP and Ring Attention, highlighting its advantages in terms of throughput and scalability.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper demonstrates the effectiveness of LASP-2 on a Linear-Llama3 model, it would be beneficial to evaluate its performance on other models and datasets to ensure its generalizability. The current evaluation is limited to a single model architecture, and it is unclear how LASP-2 would perform on models with different attention mechanisms or architectures. For example, it would be valuable to see results on models with varying numbers of layers or different attention head configurations. This would provide a more comprehensive understanding of the method's applicability and robustness.
2. The paper does not discuss the potential limitations of LASP-2, such as its scalability to even longer sequences or its performance in resource-constrained environments. While the paper demonstrates throughput improvements, it does not address the potential trade-offs in terms of memory usage or computational complexity. It is important to understand how LASP-2 would perform with extremely long sequences, such as those exceeding 100,000 tokens, and whether it would still be feasible to use in environments with limited resources. A discussion of these limitations would provide a more balanced view of the method's strengths and weaknesses.
3. The paper could benefit from a more detailed analysis of the communication overhead of LASP-2, particularly in comparison to other sequence parallelism methods. While the paper mentions that LASP-2 reduces communication overhead, it does not provide a quantitative analysis of the communication costs. It would be helpful to see a breakdown of the communication costs associated with different parts of the algorithm, such as the all-gather and reduce-scatter operations. This would provide a more concrete understanding of the method's efficiency and allow for a more direct comparison with other approaches.

### Suggestions

To strengthen the paper, the authors should conduct a more comprehensive evaluation of LASP-2 across a wider range of models and datasets. This should include models with different architectures, such as those with varying numbers of layers or different attention head configurations. For example, evaluating LASP-2 on models with 12 or 24 layers, and with different numbers of attention heads (e.g., 32, 64, 128), would provide a more robust assessment of its generalizability. Furthermore, it would be beneficial to test LASP-2 on datasets with different characteristics, such as those with varying sequence lengths or different types of input data. This would help to understand the method's performance in different scenarios and identify any potential limitations. The authors should also provide a detailed analysis of the memory usage of LASP-2, particularly in comparison to other sequence parallelism methods. This analysis should include a breakdown of the memory costs associated with different parts of the algorithm, such as the all-gather and reduce-scatter operations. This would provide a more concrete understanding of the method's efficiency and allow for a more direct comparison with other approaches. It would also be valuable to explore the scalability of LASP-2 to even longer sequences, such as those exceeding 100,000 tokens. This would help to understand the method's performance in extreme scenarios and identify any potential bottlenecks. The authors should also discuss the potential trade-offs in terms of memory usage or computational complexity, and provide recommendations for optimizing the method for resource-constrained environments.

In addition to the above, the authors should provide a more detailed analysis of the communication overhead of LASP-2. This should include a quantitative analysis of the communication costs associated with different parts of the algorithm, such as the all-gather and reduce-scatter operations. This would provide a more concrete understanding of the method's efficiency and allow for a more direct comparison with other approaches. The authors should also discuss the potential limitations of LASP-2, such as its scalability to even longer sequences or its performance in resource-constrained environments. This would provide a more balanced view of the method's strengths and weaknesses. Furthermore, it would be beneficial to compare LASP-2 with other state-of-the-art sequence parallelism methods, such as HGRN and HGRN2, to provide a more comprehensive evaluation of its performance. This comparison should include a detailed analysis of the performance of each method in terms of throughput, scalability, and memory usage. This would help to establish the relative performance of LASP-2 and its potential advantages over existing methods.

Finally, the authors should provide a more detailed explanation of the theoretical cost analysis of LASP-2 and LASP-2H. This should include a discussion of the assumptions made in the analysis and the limitations of the theoretical model. It would also be beneficial to provide a more detailed explanation of the communication and computation costs associated with different parts of the algorithm. This would provide a more concrete understanding of the method's efficiency and allow for a more direct comparison with other approaches. The authors should also discuss the potential limitations of the theoretical analysis and suggest directions for future research. This would help to ensure that the theoretical analysis is accurate and relevant to the practical application of LASP-2.

### Questions

1. How does LASP-2 perform on models with different architectures or datasets? Are there any specific scenarios where LASP-2 might not be as effective?
2. What are the potential limitations of LASP-2 in terms of scalability to even longer sequences or its performance in resource-constrained environments?
3. How does the communication overhead of LASP-2 compare to other sequence parallelism methods, such as HGRN and HGRN2? Could you provide a more detailed analysis of the communication costs associated with different parts of the algorithm?

### Rating

6

### Confidence

4

**********
