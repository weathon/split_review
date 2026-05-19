### Summary

This paper proposes a token pruning method for LLMs. The authors first analyze the redundancy of tokens across different layers and positions and then propose a token router to adaptively identify less important tokens. Experiments show that the proposed method outperforms other pruning methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The authors analyze the redundancy of tokens across different layers and positions.
2. The proposed method outperforms other pruning methods.

### Weaknesses

#### Some Related Works


#### comment

1. The authors propose a token pruning method. However, the motivation for the proposed method is not clear. The authors should clarify why token pruning is necessary and what specific problems it addresses. The paper lacks a clear explanation of the limitations of existing pruning methods that necessitate a token-level approach, and how the proposed method overcomes these limitations. It is not sufficient to simply state that token pruning is beneficial; the paper needs to articulate the specific scenarios where token pruning provides a significant advantage over block or neuron pruning.
2. The authors claim that the proposed method is fine-grained. However, the authors only prune tokens at the end of each block. The authors should clarify why they only prune tokens at the end of each block and what the benefits of this approach are. The paper needs to justify why pruning only the last token is sufficient, and whether this approach is truly fine-grained enough. A more detailed explanation of the rationale behind this design choice is needed, including a discussion of the potential limitations of only pruning the last token and how this might affect the model's ability to capture complex relationships between tokens.
3. The authors should provide a comparison of the proposed method with other pruning methods in terms of computational complexity and efficiency. The paper lacks a detailed analysis of the computational overhead introduced by the proposed token pruning method. A comparison of the training and inference time, as well as memory usage, with other pruning methods is necessary to demonstrate the practical viability of the approach. Without this analysis, it is difficult to assess the trade-offs between performance gains and computational costs.

### Suggestions

The paper needs to provide a more compelling motivation for using token pruning. The authors should clearly articulate the limitations of existing pruning methods, such as block or neuron pruning, and explain why a token-level approach is necessary to address these limitations. For example, they could discuss scenarios where block or neuron pruning fails to achieve significant performance gains, and how token pruning can overcome these shortcomings. The authors should also provide a more detailed analysis of the specific types of tasks or datasets where token pruning is most effective, and why. This would help to justify the need for a token pruning method and highlight its potential advantages over other approaches. Furthermore, the authors should discuss the potential impact of token pruning on the model's ability to capture long-range dependencies and contextual relationships between tokens. A more thorough discussion of these aspects would strengthen the motivation for the proposed method.

The authors need to provide a more detailed explanation of their fine-grained token pruning approach. The paper should clarify why pruning only the last token is sufficient, and whether this approach is truly fine-grained enough. The authors should discuss the potential limitations of only pruning the last token and how this might affect the model's ability to capture complex relationships between tokens. A more detailed explanation of the rationale behind this design choice is needed, including a discussion of the potential trade-offs between computational efficiency and performance. The authors should also explore the possibility of pruning tokens at different positions within the block, and discuss the potential benefits and challenges of such an approach. This would help to justify the claim of fine-grained pruning and demonstrate its effectiveness.

The paper should include a comprehensive analysis of the computational complexity and efficiency of the proposed method. The authors should provide a detailed comparison of the training and inference time, as well as memory usage, with other pruning methods. This analysis should include a breakdown of the computational costs associated with the token router and the pruning process. The authors should also discuss the scalability of the proposed method to larger models and datasets. This analysis is crucial for demonstrating the practical viability of the approach and for understanding the trade-offs between performance gains and computational costs. Without this analysis, it is difficult to assess the true value of the proposed method.

### Questions

See weaknesses.

### Rating

5

### Confidence

3

**********
