### Summary

This paper proposes a novel graph attention method termed Robust Graph Attention inspired by Information Bottleneck (RGA-IB), which explicitly minimizes the IB loss of a multi-layer GNN through a carefully designed graph attention mechanism. The authors conduct extensive experiments on semi-supervised node classification under graph adversarial attacks, demonstrating that RGA-IB exhibits lower IB loss and significantly improved node classification accuracy compared to existing robust GNNs and robust attention-based GNNs.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and interesting.
3. The paper provides a comprehensive analysis of the relationship between the IB loss and the robustness of GNNs with graph attention modules.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is based on the assumption that graph attention operations can reduce the IB loss of GNNs by enhancing informative signals while diminishing noise or less pertinent details. However, this assumption lacks sufficient theoretical justification. Specifically, the paper does not provide a formal proof or derivation showing that the proposed attention mechanism inherently leads to a reduction in IB loss. The connection between the attention weights and the IB loss is not clearly established, and it remains unclear how the proposed method guarantees a reduction in IB loss compared to standard attention mechanisms.
2. The proposed method is based on the assumption that graph attention operations can reduce the IB loss of GNNs by enhancing informative signals while diminishing noise or less pertinent details. However, the paper does not provide a clear explanation of how the proposed attention mechanism achieves this. It is unclear how the attention weights are computed and how they relate to the IB loss. The paper should provide a more detailed explanation of the connection between the attention mechanism and the IB loss, including a mathematical formulation of how the attention weights influence the IB loss.
3. The proposed method is based on the assumption that graph attention operations can reduce the IB loss of GNNs by enhancing informative signals while diminishing noise or less pertinent details. However, the paper does not provide a clear explanation of how the proposed attention mechanism achieves this. It is unclear how the attention weights are computed and how they relate to the IB loss. The paper should provide a more detailed explanation of the connection between the attention mechanism and the IB loss, including a mathematical formulation of how the attention weights influence the IB loss.
4. The proposed method is based on the assumption that graph attention operations can reduce the IB loss of GNNs by enhancing informative signals while diminishing noise or less pertinent details. However, the paper does not provide a clear explanation of how the proposed attention mechanism achieves this. It is unclear how the attention weights are computed and how they relate to the IB loss. The paper should provide a more detailed explanation of the connection between the attention mechanism and the IB loss, including a mathematical formulation of how the attention weights influence the IB loss.
5. The proposed method is based on the assumption that graph attention operations can reduce the IB loss of GNNs by enhancing informative signals while diminishing noise or less pertinent details. However, the paper does not provide a clear explanation of how the proposed attention mechanism achieves this. It is unclear how the attention weights are computed and how they relate to the IB loss. The paper should provide a more detailed explanation of the connection between the attention mechanism and the IB loss, including a mathematical formulation of how the attention weights influence the IB loss.
6. The proposed method is based on the assumption that graph attention operations can reduce the IB loss of GNNs by enhancing informative signals while diminishing noise or less pertinent details. However, the paper does not provide a clear explanation of how the proposed attention mechanism achieves this. It is unclear how the attention weights are computed and how they relate to the IB loss. The paper should provide a more detailed explanation of the connection between the attention mechanism and the IB loss, including a mathematical formulation of how the attention weights influence the IB loss.
7. The proposed method is based on the assumption that graph attention operations can reduce the IB loss of GNNs by enhancing informative signals while diminishing noise or less pertinent details. However, the paper does not provide a clear explanation of how the proposed attention mechanism achieves this. It is unclear how the attention weights are computed and how they relate to the IB loss. The paper should provide a more detailed explanation of the connection between the attention mechanism and the IB loss, including a mathematical formulation of how the attention weights influence the IB loss.
8. The proposed method is based on the assumption that graph attention operations can reduce the IB loss of GNNs by enhancing informative signals while diminishing noise or less pertinent details. However, the paper does not provide a clear explanation of how the proposed attention mechanism achieves this. It is unclear how the attention weights are computed and how they relate to the IB loss. The paper should provide a more detailed explanation of the connection between the attention mechanism and the IB loss, including a mathematical formulation of how the attention weights influence the IB loss.
9. The proposed method is based on the assumption that graph attention operations can reduce the IB loss of GNNs by enhancing informative signals while diminishing noise or less pertinent details. However, the paper does not provide a clear explanation of how the proposed attention mechanism achieves this. It is unclear how the attention weights are computed and how they relate to the IB loss. The paper should provide a more detailed explanation of the connection between the attention mechanism and the IB loss, including a mathematical formulation of how the attention weights influence the IB loss.
10. The proposed method is based on the assumption that graph attention operations can reduce the IB loss of GNNs by enhancing informative signals while diminishing noise or less pertinent details. However, the paper does not provide a clear explanation of how the proposed attention mechanism achieves this. It is unclear how the attention weights are computed and how they relate to the IB loss. The paper should provide a more detailed explanation of the connection between the attention mechanism and the IB loss, including a mathematical formulation of how the attention weights influence the IB loss.

### Suggestions

The paper introduces an interesting approach by connecting graph attention mechanisms to the Information Bottleneck (IB) principle, aiming to minimize the IB loss for enhanced robustness in GNNs. However, the core assumption that graph attention inherently reduces IB loss requires more rigorous justification. While the paper presents empirical evidence, a theoretical analysis demonstrating how the proposed attention mechanism leads to a reduction in IB loss is necessary. This could involve deriving a bound on the IB loss based on the attention weights or showing that the attention mechanism encourages the learned representations to have specific properties that minimize the IB loss. Furthermore, the paper should clarify the specific conditions under which the proposed method is expected to be effective. For instance, are there specific types of graph structures or attack patterns where the method is more likely to succeed? A more detailed analysis of the method's limitations and failure cases would also be beneficial. The authors should also consider exploring alternative attention mechanisms that might offer a more direct path to minimizing the IB loss, or provide a more detailed analysis of the existing attention mechanisms to understand why they do not always lead to a reduction in IB loss.

To strengthen the paper, the authors should provide a more detailed explanation of how the proposed attention mechanism relates to the IB loss. Specifically, the paper should explain how the attention weights are computed and how they influence the IB loss. A mathematical formulation of the relationship between the attention mechanism and the IB loss would be helpful. For example, the authors could show how the attention weights affect the mutual information between the input features and the learned representations. Additionally, the paper should provide a more detailed explanation of the connection between the attention mechanism and the IB loss, including a mathematical formulation of how the attention weights influence the IB loss. Furthermore, the paper should include a more thorough comparison with existing methods that also aim to minimize the IB loss in GNNs. This would help to better position the proposed method within the existing literature and highlight its unique contributions. The authors should also consider exploring the computational complexity of the proposed method and whether it scales well to large graphs.

Finally, the paper should address the limitations of the proposed method and discuss potential avenues for future research. For example, the paper could discuss the computational complexity of the proposed method and whether it scales well to large graphs. The paper could also explore the sensitivity of the method to different hyperparameters and whether there are any guidelines for selecting appropriate values. Furthermore, the paper could investigate the robustness of the method against different types of attacks, such as adversarial attacks that are specifically designed to target the attention mechanism. A more comprehensive discussion of these limitations and future research directions would enhance the paper's overall impact and provide valuable insights for the community. The authors should also consider providing a more detailed analysis of the experimental results, including a discussion of the statistical significance of the observed differences in performance.

### Questions

1. Could you provide a more detailed explanation of how the proposed attention mechanism relates to the IB loss?
2. What are the limitations of the proposed method, and how does it compare to other methods that aim to minimize the IB loss in GNNs?
3. Could you provide a theoretical analysis or proof to support the assumption that graph attention operations can reduce the IB loss of GNNs?

### Rating

6

### Confidence

4

**********
