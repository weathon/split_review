### Summary

The paper proposes a new message passing scheme for GNNs based on the curvature of the edges. The authors use this scheme to propose a rewiring method that is compared to other rewiring methods on several datasets.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well written and easy to follow.
- The proposed method is simple and intuitive.
- The paper proposes a new rewiring method that outperforms other rewiring methods on several datasets.

### Weaknesses

#### Some Related Works

[1] On the bottleneck problem in graph neural networks: A spectral perspective
[2] Revisiting heterophily for graph neural networks

#### comment

 - The proposed message passing scheme is not novel. The proposed message passing scheme is very similar to the message passing scheme proposed in [1]. The main difference is that the proposed message passing scheme uses the Ollivier curvature of the edges to guide the message passing, while the message passing scheme proposed in [1] uses the Forman curvature of the edges to guide the message passing. The paper does not provide a clear justification for why Ollivier curvature is superior to Forman curvature in this context, nor does it discuss the potential limitations of using Ollivier curvature, such as its computational cost or sensitivity to noise.
- The paper does not provide a clear motivation for the proposed message passing scheme. The paper does not explain why the proposed message passing scheme is expected to be more effective than existing message passing schemes. The paper does not provide any theoretical analysis or empirical evidence to support the claim that the proposed message passing scheme is better than existing message passing schemes. The paper also does not discuss the potential limitations of the proposed message passing scheme, such as its sensitivity to hyperparameter tuning or its performance on different types of graphs.
- The paper does not provide a clear explanation of how the proposed message passing scheme is implemented. The paper does not provide any pseudocode or implementation details. The paper also does not provide any information about the computational complexity of the proposed message passing scheme. The paper does not discuss the potential challenges of implementing the proposed message passing scheme, such as the need for specialized data structures or algorithms.
- The paper does not provide a clear explanation of how the proposed message passing scheme is evaluated. The paper does not provide any details about the evaluation metrics used. The paper does not discuss the potential limitations of the evaluation metrics used. The paper does not provide any information about the statistical significance of the results.
- The paper does not provide a clear explanation of how the proposed message passing scheme is compared to other message passing schemes. The paper does not provide any details about the experimental setup used to compare the proposed message passing scheme to other message passing schemes. The paper does not discuss the potential limitations of the experimental setup used. The paper does not provide any information about the statistical significance of the results.
- The paper does not provide a clear explanation of how the proposed message passing scheme is related to the over-squashing problem. The paper does not provide any theoretical analysis or empirical evidence to support the claim that the proposed message passing scheme is effective in mitigating the over-squashing problem. The paper does not discuss the potential limitations of the proposed message passing scheme in mitigating the over-squashing problem.
- The paper does not provide a clear explanation of how the proposed message passing scheme is related to the heterophily problem. The paper does not provide any theoretical analysis or empirical evidence to support the claim that the proposed message passing scheme is effective in handling heterophilic graphs. The paper does not discuss the potential limitations of the proposed message passing scheme in handling heterophilic graphs.

### Suggestions

The paper needs to provide a more thorough justification for the use of Ollivier curvature over Forman curvature, especially given the similarities to existing work. A detailed analysis of the computational cost and sensitivity to noise of Ollivier curvature is needed. The authors should also discuss the potential limitations of using Ollivier curvature, such as its sensitivity to hyperparameter tuning or its performance on different types of graphs. Furthermore, the paper should provide a more detailed explanation of how the proposed message passing scheme is implemented, including pseudocode or implementation details. The authors should also discuss the computational complexity of the proposed message passing scheme and the potential challenges of implementing it, such as the need for specialized data structures or algorithms. The paper should also provide a more detailed explanation of how the proposed message passing scheme is evaluated, including the evaluation metrics used and the potential limitations of these metrics. The authors should also discuss the statistical significance of the results and provide a clear explanation of how the proposed message passing scheme is compared to other message passing schemes. The paper should also provide a more detailed explanation of how the proposed message passing scheme is related to the over-squashing problem and the heterophily problem. The authors should provide theoretical analysis or empirical evidence to support the claim that the proposed message passing scheme is effective in mitigating these problems. The paper should also discuss the potential limitations of the proposed message passing scheme in mitigating these problems.

To improve the paper, the authors should consider conducting a more comprehensive experimental evaluation of the proposed message passing scheme. This should include a wider range of datasets, different graph structures, and different message passing schemes. The authors should also compare the performance of the proposed message passing scheme with other state-of-the-art methods for handling over-squashing and heterophily. The experimental results should be analyzed in detail, and the authors should discuss the potential limitations of the proposed message passing scheme. The authors should also provide a more detailed discussion of the related work, including a comparison of the proposed message passing scheme with other methods for handling over-squashing and heterophily. The authors should also discuss the potential limitations of the proposed message passing scheme and suggest directions for future research.

Finally, the authors should provide a more detailed explanation of the motivation behind the proposed message passing scheme. The authors should explain why they expect the proposed message passing scheme to be more effective than existing message passing schemes. This explanation should be supported by theoretical analysis or empirical evidence. The authors should also discuss the potential limitations of the proposed message passing scheme, such as its sensitivity to hyperparameter tuning or its performance on different types of graphs. The authors should also provide a more detailed explanation of how the proposed message passing scheme is related to the over-squashing problem and the heterophily problem. The authors should provide theoretical analysis or empirical evidence to support the claim that the proposed message passing scheme is effective in mitigating these problems. The paper should also discuss the potential limitations of the proposed message passing scheme in mitigating these problems.

### Questions

- Why is the proposed message passing scheme better than other message passing schemes?
- What is the motivation for using Ollivier curvature instead of Forman curvature?
- What are the computational costs of the proposed message passing scheme?
- How is the proposed message passing scheme evaluated?
- How is the proposed message passing scheme compared to other message passing schemes?
- How is the proposed message passing scheme related to the over-squashing problem?
- How is the proposed message passing scheme related to the heterophily problem?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
