### Summary

This paper proposes a new sequence parallelism (SP) method for linear attention models, named LASP-2, which improves the communication efficiency of the previous method, LASP-1. The authors also extend the method to a hybrid model, LASP-2H, which combines linear and standard attention modules. The experiments show that LASP-2 outperforms LASP-1 and Ring Attention on a Linear-Llama3 model with a 2048K sequence length.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method LASP-2 is simple and effective, and the authors provide a clear explanation of the algorithm and its implementation.
3. The authors conduct extensive experiments to evaluate the performance of LASP-2 on a Linear-Llama3 model with a 2048K sequence length, and the results show that LASP-2 outperforms LASP-1 and Ring Attention.

### Weaknesses

#### Some Related Works


#### comment

1. The paper only evaluates the performance of LASP-2 on a single model, Linear-Llama3, and does not provide results on other models or datasets. This limits the generalizability of the findings and makes it difficult to assess the robustness of the method.
2. The paper does not provide a detailed analysis of the communication overhead of LASP-2, which is a key aspect of the proposed method. It is unclear how the communication cost scales with the sequence length and the number of GPUs used.
3. The paper does not compare LASP-2 with other state-of-the-art sequence parallelism methods, such as HGRN and HGRN2. This makes it difficult to assess the relative performance of LASP-2 and its potential advantages over existing methods.

### Suggestions

The authors should conduct more extensive experiments to evaluate the performance of LASP-2 on a wider range of models and datasets. This would help to demonstrate the generalizability of the method and its applicability to different scenarios. Specifically, it would be beneficial to evaluate LASP-2 on models with different architectures and sizes, as well as on datasets with varying characteristics. For example, experiments could be conducted on models with different numbers of layers, attention heads, and hidden dimensions. Additionally, it would be useful to evaluate LASP-2 on datasets with different sequence lengths and complexities. This would provide a more comprehensive understanding of the strengths and limitations of the proposed method.

Furthermore, the authors should provide a more detailed analysis of the communication overhead of LASP-2. This analysis should include a breakdown of the communication costs associated with different parts of the algorithm, as well as an evaluation of how these costs scale with the sequence length and the number of GPUs used. It would be helpful to provide a theoretical analysis of the communication complexity of LASP-2, as well as empirical results that demonstrate how the communication cost varies with different parameters. This analysis should also consider the impact of network latency and bandwidth on the overall performance of LASP-2. A more thorough understanding of the communication overhead would allow for a more accurate assessment of the practical benefits of the proposed method.

Finally, the authors should compare LASP-2 with other state-of-the-art sequence parallelism methods, such as HGRN and HGRN2. This comparison should include a detailed analysis of the performance of each method in terms of throughput, scalability, and memory usage. The authors should also discuss the advantages and disadvantages of LASP-2 compared to these existing methods. This would help to establish the relative performance of LASP-2 and its potential contributions to the field. It would also be beneficial to compare LASP-2 with other sequence parallelism methods that are not based on ring-all-reduce, such as those that use tree-based parallelism or pipeline parallelism. This would provide a more comprehensive understanding of the landscape of sequence parallelism methods and help to position LASP-2 within this landscape.

### Questions

1. How does LASP-2 compare with other state-of-the-art sequence parallelism methods, such as HGRN and HGRN2?
2. How does the communication overhead of LASP-2 scale with the sequence length and the number of GPUs used?

### Rating

5

### Confidence

4

**********
