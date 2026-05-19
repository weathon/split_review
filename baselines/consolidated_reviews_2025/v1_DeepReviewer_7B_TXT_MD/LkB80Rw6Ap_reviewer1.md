### Summary

This paper proposes a message passing scheme that uses the Ollivier curvature of the edges to guide the message passing. The message passing scheme is based on two curvature-constrained homophily measures. The paper also proposes two variants of the message passing scheme that are based on one-hop and two-hop neighborhoods. The paper compares the proposed message passing scheme with rewiring-based methods on 11 datasets and shows that the proposed message passing scheme outperforms the rewiring-based methods on 7 out of 11 datasets.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The proposed message passing scheme is simple and easy to implement.
- The proposed message passing scheme is evaluated on 11 datasets and outperforms the rewiring-based methods on 7 out of 11 datasets.

### Weaknesses

#### Some Related Works

[1] On the bottleneck problem in graph neural networks
[2] On the bottleneck problem in graph neural networks: A spectral perspective
[3] Revisiting heterophily for graph neural networks

#### comment

 - The proposed message passing scheme is not novel. The proposed message passing scheme is very similar to the message passing scheme proposed in [1]. The main difference is that the proposed message passing scheme uses the Ollivier curvature of the edges to guide the message passing, while the message passing scheme proposed in [1] uses the Forman curvature of the edges to guide the message passing. The paper does not provide a clear justification for why Ollivier curvature is superior to Forman curvature in this context, nor does it discuss the potential limitations of using Ollivier curvature, such as its computational cost or sensitivity to noise.
- The paper does not provide a clear motivation for the proposed message passing scheme. The paper does not explain why the proposed message passing scheme is expected to be more effective than existing message passing schemes. The paper does not provide any theoretical analysis or empirical evidence to support the claim that the proposed message passing scheme is better than existing message passing schemes. The paper also does not discuss the potential limitations of the proposed message passing scheme, such as its sensitivity to hyperparameter tuning or its performance on different types of graphs.
- The paper does not provide a clear explanation of how the proposed message passing scheme is implemented. The paper does not provide any pseudocode or implementation details. The paper also does not provide any information about the computational complexity of the proposed message passing scheme. The paper does not discuss the potential challenges of implementing the proposed message passing scheme, such as the need for specialized data structures or algorithms.
- The paper does not provide a clear explanation of how the proposed message passing scheme is evaluated. The paper does not provide any details about the evaluation metrics used. The paper does not discuss the potential limitations of the evaluation metrics used. The paper does not provide any information about the statistical significance of the results.
- The paper does not provide a clear explanation of how the proposed message passing scheme is compared to other message passing schemes. The paper does not provide any details about the experimental setup used to compare the proposed message passing scheme to other message passing schemes. The paper does not discuss the potential limitations of the experimental setup used. The paper does not provide any information about the statistical significance of the results.
- The paper does not provide a clear explanation of how the proposed message passing scheme is related to the over-squashing problem. The paper does not provide any theoretical analysis or empirical evidence to support the claim that the proposed message passing scheme is effective in mitigating the over-squashing problem. The paper does not discuss the potential limitations of the proposed message passing scheme in mitigating the over-squashing problem.
- The paper does not provide a clear explanation of how the proposed message passing scheme is related to the heterophily problem. The paper does not provide any theoretical analysis or empirical evidence to support the claim that the proposed message passing scheme is effective in handling heterophilic graphs. The paper does not discuss the potential limitations of the proposed message passing scheme in handling heterophilic graphs.

### Suggestions

The paper needs to provide a more thorough justification for the use of Ollivier curvature over Forman curvature, especially given the similarities to existing work [1]. A detailed analysis of the computational cost and sensitivity to noise of Ollivier curvature is needed. The authors should also discuss the potential limitations of using Ollivier curvature, such as its sensitivity to hyperparameter tuning or its performance on different types of graphs. Furthermore, the paper should provide a more detailed explanation of how the proposed message passing scheme is implemented, including pseudocode or implementation details. The authors should also discuss the computational complexity of the proposed message passing scheme and the potential challenges of implementing it, such as the need for specialized data structures or algorithms. The paper should also provide a more detailed explanation of how the proposed message passing scheme is evaluated, including the evaluation metrics used and the potential limitations of these metrics. The authors should also discuss the statistical significance of the results and provide a clear explanation of how the proposed message passing scheme is compared to other message passing schemes. The paper should also provide a more detailed explanation of how the proposed message passing scheme is related to the over-squashing problem and the heterophily problem. The authors should provide theoretical analysis or empirical evidence to support the claim that the proposed message passing scheme is effective in mitigating these problems. The paper should also discuss the potential limitations of the proposed message passing scheme in mitigating these problems.

The paper should also provide a more detailed explanation of the motivation behind the proposed message passing scheme. The authors should explain why they expect the proposed message passing scheme to be more effective than existing message passing schemes. This explanation should be supported by theoretical analysis or empirical evidence. The paper should also discuss the potential limitations of the proposed message passing scheme, such as its sensitivity to hyperparameter tuning or its performance on different types of graphs. The authors should also provide a more detailed explanation of how the proposed message passing scheme is related to the over-squashing problem and the heterophily problem. The authors should provide theoretical analysis or empirical evidence to support the claim that the proposed message passing scheme is effective in mitigating these problems. The paper should also discuss the potential limitations of the proposed message passing scheme in mitigating these problems.

Finally, the paper needs to address the lack of clarity in the experimental setup. The authors should provide more details about the datasets used, the evaluation metrics, and the experimental procedure. The paper should also discuss the potential limitations of the experimental setup and the statistical significance of the results. The authors should also provide a more detailed explanation of how the proposed message passing scheme is related to the over-squashing problem and the heterophily problem. The authors should provide theoretical analysis or empirical evidence to support the claim that the proposed message passing scheme is effective in mitigating these problems. The paper should also discuss the potential limitations of the proposed message passing scheme in mitigating these problems.

### Questions

- What is the motivation for the proposed message passing scheme?
- What is the novelty of the proposed message passing scheme?
- How does the proposed message passing scheme compare to existing message passing schemes?
- How is the proposed message passing scheme evaluated?
- How is the proposed message passing scheme related to the over-squashing problem?
- How is the proposed message passing scheme related to the heterophily problem?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
