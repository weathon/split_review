### Summary

This paper studies the problem of online Laplacian-based representation learning in reinforcement learning. The authors propose the Asymmetric Graph Drawing Objective (AGDO) and provide a theoretical analysis of the convergence of running online projected gradient descent on AGDO under mild assumptions. The experimental results show that the proposed method can converge to the true Laplacian representation and is compatible with different reinforcement learning algorithms.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and interesting.
3. The theoretical analysis is solid and the experimental results are promising.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion of the limitations of the proposed method and potential directions for future research.
2. The paper could benefit from a more thorough comparison with existing methods for online representation learning in reinforcement learning.

### Suggestions

The paper would be strengthened by a more detailed discussion of the limitations of the proposed Asymmetric Graph Drawing Objective (AGDO) within the context of online Laplacian-based representation learning. Specifically, the authors should explore scenarios where the assumption of bounded drift in the policy might not hold, and how this could impact the convergence of the online projected gradient descent (PGD) algorithm. For example, in highly non-stationary environments or with very aggressive exploration strategies, the policy changes might be too rapid for the representation to adapt effectively, leading to instability or divergence. Furthermore, the authors should discuss the computational cost associated with the online PGD, particularly in high-dimensional state spaces, and how this might limit the scalability of the approach. A discussion of the sensitivity of the method to the choice of hyperparameters, such as the learning rate and the barrier coefficient, would also be valuable. Finally, the authors should consider the potential for the learned representation to be sensitive to the specific environment or task, and how this might affect its generalization capabilities.

To enhance the paper, a more thorough comparison with existing online representation learning methods in reinforcement learning is needed. The authors should not only compare the proposed method with other Laplacian-based approaches, but also with methods that use different techniques for representation learning, such as autoencoders or contrastive learning. This comparison should include a discussion of the advantages and disadvantages of each method in terms of computational complexity, sample efficiency, and generalization performance. For example, how does the proposed method compare to methods that learn representations based on temporal differences or reward-based signals? A detailed analysis of the trade-offs between these different approaches would provide a more comprehensive understanding of the proposed method's strengths and weaknesses. Furthermore, the authors should discuss the potential for combining the proposed method with other representation learning techniques to improve performance.

Finally, the authors should provide more insights into the practical implications of the theoretical results. While the theoretical analysis provides guarantees on the convergence of the online PGD algorithm, it would be helpful to discuss how these guarantees translate into practical performance. For example, how does the convergence rate of the algorithm depend on the specific properties of the environment and the policy? What are the practical implications of the bounded drift assumption? A more detailed discussion of these issues would help the reader to better understand the practical relevance of the theoretical results and how they can be used to guide the design of effective reinforcement learning algorithms.

### Questions

1. Can the authors provide more insights into the choice of hyperparameters for the AGDO?
2. How does the proposed method perform in more complex environments with high-dimensional state spaces?
3. Can the authors provide more details on the implementation of the online PGD algorithm and its computational complexity?

### Rating

6

### Confidence

3

**********
