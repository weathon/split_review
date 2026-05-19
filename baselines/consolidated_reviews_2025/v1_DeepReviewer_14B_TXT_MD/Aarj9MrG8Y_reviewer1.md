### Summary

The paper proposes a new neural network for graphs, APGNN, that is based on a graph filter that is an infinite power series with exponentially decaying weights. The main motivation for this design is to address the over-smoothing problem, which is a kind of limitation of the depth in existing GNNs. The paper also presents a generalization analysis for the proposed class of graph filters, and shows some experimental results.

### Soundness

2 fair

### Presentation

3 good

### Contribution

1 poor

### Strengths

The paper is well-written and easy to follow. The proposed method is simple and the idea is nice. The generalization analysis is interesting.

### Weaknesses

#### Some Related Works

[1] A note on over-smoothing for graph neural networks
[2] DeepGCN: Building Deep Graph Neural Networks
[3] Beyond Over-smoothing: Uncovering the Trainability Challenges in Deep Graph Neural Networks
[4] On the Trade-Offs of Effective Propagation in Graph Neural Networks
[5] Revisiting Generalization of Graph Neural Networks: A Complexity Control Perspective

#### comment

The contribution of the paper is very limited. There are several important weaknesses:

- The claim that the proposed method is based on a "universal learning principle" is unjustified and an overstatement. The so-called principle is about the conditions that a power-series graph filter should satisfy so that it converges absolutely. This is more of a well-behaved condition for a graph filter, not a "principle" that is "universal". Furthermore, it is not even clear if this condition is necessary.

- The paper claims that existing methods do not satisfy this condition and are therefore "inconsistent" with infinite-depth versions. This is not accurate. For example, GCN clearly satisfies this condition with $\theta_k = \theta^k$ for some $\theta \in [0,1)$, and therefore is consistent with its infinite-depth version. The authors seem to misunderstand the condition they are proposing.

- The paper does not really show that the proposed APGNN can overcome the over-smoothing problem. The exponential decay of the filter might prevent the method from truly overcoming the over-smoothing problem. In fact, the method might suffer from over-smoothing even with a very deep network, we just might need to take the depth very large. The experiments are not convincing in this regard, as they do not compare against methods that are known to mitigate over-smoothing effectively. The datasets used are also very simple for evaluating over-smoothing.

- The novelty of the method is also limited. The idea of using exponentially decaying weights is not new and has been explored in various contexts. The paper does not adequately distinguish the proposed method from existing approaches that use similar techniques.

- The generalization analysis is interesting, but it is not clear how it supports the claim of overcoming over-smoothing. The analysis seems to focus on bounding the population error, but it does not address the practical challenges of training deep GNNs, such as vanishing gradients or loss landscape issues. The analysis also does not explain why the proposed method is better than existing methods in terms of generalization.

### Suggestions

The paper needs to address several key issues to improve its contribution. First, the authors should clarify the theoretical underpinnings of their proposed method and avoid overstating the "universal learning principle". The condition they propose for the graph filter is not a principle, but rather a sufficient condition for convergence. They should also acknowledge that other methods, such as GCN, can also satisfy this condition and are therefore consistent with their infinite-depth versions. A more rigorous analysis of the proposed method's convergence properties is needed, including a discussion of the necessary conditions for convergence and how the proposed method satisfies them. The authors should also provide a more detailed explanation of how their method differs from existing approaches that use exponentially decaying weights, and what specific advantages it offers.

Second, the paper needs to provide more convincing evidence that the proposed method can overcome the over-smoothing problem. The current experimental results are not sufficient to support this claim. The authors should compare their method against state-of-the-art methods that are known to mitigate over-smoothing, such as those based on residual connections or attention mechanisms. They should also use more challenging datasets that are known to exhibit over-smoothing. Furthermore, the authors should provide a more detailed analysis of the behavior of their method in deep networks, including an analysis of the gradient flow and the loss landscape. It is important to show that the method does not simply delay over-smoothing by requiring very large depths.

Finally, the authors should clarify the connection between their generalization analysis and the over-smoothing problem. The current analysis focuses on bounding the population error, but it does not address the practical challenges of training deep GNNs. The authors should explain how their generalization analysis provides insights into the over-smoothing problem and how it supports the claim that their method can overcome it. They should also discuss the limitations of their analysis and acknowledge that other factors, such as vanishing gradients and loss landscape issues, can also affect the performance of deep GNNs. The paper would benefit from a more thorough discussion of these issues and how they relate to the proposed method.

### Questions

Please see the weaknesses.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
