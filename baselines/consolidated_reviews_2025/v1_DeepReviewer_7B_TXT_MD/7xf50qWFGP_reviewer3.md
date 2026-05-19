### Summary

This paper studies the problem of learning Laplacian-based representation in reinforcement learning. The authors propose an online optimization formulation by introducing the stop gradient operator. Theoretical analysis shows that the proposed formulation converges to a stationary point under mild assumptions. The paper also provides empirical results to validate the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The theoretical analysis is comprehensive and provides a solid foundation for the proposed method.
3. The empirical results are supportive of the theoretical analysis.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is not self-contained. The authors should provide more background information on the Laplacian-based representation learning and the stop gradient operator. Specifically, the connection between the stop gradient operator and the underlying optimization problem needs more clarification. It's not immediately obvious how this operator facilitates the desired learning dynamics, and a more detailed explanation of its role in the context of Laplacian-based representations is needed.
2. The authors should also provide more background information on the related work on representation learning and online learning. The current introduction lacks sufficient context to position the proposed method within the broader landscape of representation learning and online learning techniques. A more thorough discussion of existing approaches and their limitations would help to highlight the novelty and significance of the proposed method.
3. The authors should also provide more background information on the related work on the representation learning in RL. The current discussion is too brief and does not adequately cover the existing literature on representation learning in reinforcement learning. A more comprehensive overview of different representation learning techniques, such as proto-value functions, proto-representations, and spectral methods, is necessary to properly contextualize the proposed approach.
4. The authors should also provide more background information on the related work on the Laplacian representation learning. The paper needs to clearly articulate how the proposed method differs from existing Laplacian-based representation learning techniques. A more detailed discussion of the specific advantages and disadvantages of the proposed approach compared to existing methods is needed.

### Suggestions

To improve the paper, the authors should begin by providing a more detailed explanation of the stop gradient operator and its role in the proposed optimization framework. This should include a step-by-step breakdown of how the operator is applied in the context of Laplacian-based representations, and how it contributes to the learning process. For example, a concrete example illustrating how the stop gradient operator affects the gradients during backpropagation would be beneficial. Furthermore, the authors should elaborate on the theoretical implications of using this operator, such as its impact on convergence and stability. This would help the reader understand the rationale behind the proposed approach and its potential advantages. The authors should also clarify how the proposed method addresses the challenges of learning representations in online settings, and how it differs from existing methods that are typically applied in offline settings.

In addition, the authors should expand the related work section to provide a more comprehensive overview of representation learning in reinforcement learning. This should include a discussion of various representation learning techniques, such as proto-value functions, proto-representations, and spectral methods, and how they relate to the proposed approach. The authors should also discuss the limitations of existing methods and how the proposed method addresses these limitations. For example, the authors could discuss how their method compares to spectral methods in terms of computational complexity and sample efficiency. A more thorough discussion of the related work would help to better position the proposed method and highlight its contributions. The authors should also clarify the novelty of their approach compared to existing Laplacian-based representation learning techniques, and provide a more detailed discussion of the specific advantages and disadvantages of their method.

Finally, the authors should provide a more detailed comparison of their method with existing Laplacian-based representation learning techniques. This should include a discussion of the specific advantages and disadvantages of their approach compared to existing methods. For example, the authors could discuss how their method compares to proto-representations in terms of the quality of the learned representations and their computational cost. A more detailed comparison would help to better understand the novelty and significance of the proposed approach. The authors should also clarify the specific scenarios where their method is most effective, and how it compares to other methods in terms of performance and computational cost.

### Questions

See the weaknesses.

### Rating

5

### Confidence

3

**********
