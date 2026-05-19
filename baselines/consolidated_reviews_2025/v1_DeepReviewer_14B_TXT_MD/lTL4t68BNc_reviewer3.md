### Summary

This paper proposes a new method for robust graph attention, which is inspired by the information bottleneck (IB) principle. The authors first find that the IB loss of attention-based GNNs is a strong indicator of their robustness against variant graph adversarial attacks. Then, they propose a new graph attention method termed Robust Graph Attention inspired by Information Bottleneck, or RGA-IB, which explicitly minimizes the IB loss of a multi-layer GNN through a carefully designed graph attention mechanism. Extensive experiments demonstrate the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The idea of utilizing the IB principle to improve the robustness of graph attention is novel and interesting.
2. The paper is well-written and easy to follow.
3. The proposed method is simple yet effective, and the experimental results are promising.

### Weaknesses

#### Some Related Works

[1] Graph Structure Learning for Robust Graph Neural Networks
[2] On the Robustness of Graph Neural Networks against Adversarial Attacks

#### comment

1. The novelty of this paper is somewhat limited. There have been several studies that leverage the IB principle to enhance the robustness of GNNs, such as GIB, RG-GIB, and UGRL. The authors do mention these methods in the related works section. However, they do not provide a detailed comparison between RGA-IB and these existing methods. The authors should provide a more comprehensive comparison to highlight the advantages of RGA-IB over these methods.
2. The authors claim that RGA-IB reduces the IB loss, but they do not provide a formal proof of this claim. It would be better if the authors could provide a theoretical guarantee that RGA-IB reduces the IB loss.
3. In the experiments, the authors only evaluate the performance of RGA-IB on small-scale datasets. It would be better if the authors could evaluate the performance of RGA-IB on large-scale datasets, such as OGBN-ARXIV. The authors should also compare RGA-IB with other state-of-the-art robust GNN methods, such as GCORN [1] and SGFormer [2].
4. The authors do not provide the code for RGA-IB, which makes it difficult to reproduce the results. It would be better if the authors could provide the code to ensure the reproducibility of the results.
5. The authors do not discuss the limitations of RGA-IB. It would be better if the authors could discuss the potential limitations of RGA-IB, such as its computational complexity and its sensitivity to hyperparameter settings.

### Suggestions

The paper introduces an interesting approach by applying the Information Bottleneck (IB) principle to graph attention networks for robustness against adversarial attacks. However, the novelty is somewhat incremental, as the core idea of using IB for robustness in GNNs has been explored in prior works like GIB, RG-GIB, and UGRL. The authors should provide a more detailed comparison, perhaps in a table, highlighting the specific differences in the IB formulation, optimization strategies, and attention mechanisms used in RGA-IB compared to these existing methods. This would help clarify the unique contributions of RGA-IB. For example, a discussion of how RGA-IB's attention mechanism differs from the attention mechanisms in these prior works, and how these differences contribute to robustness, would be beneficial. Furthermore, a more rigorous theoretical analysis of the proposed method is needed to support the claim that RGA-IB reduces the IB loss. A formal proof, or at least a detailed derivation, demonstrating that the proposed attention mechanism, when optimized, leads to a reduction in the IB loss, would significantly strengthen the paper.

To further validate the effectiveness of RGA-IB, the authors should conduct experiments on larger, more challenging datasets, such as OGBN-ARXIV, and compare its performance against state-of-the-art robust GNN methods like GCORN and SGFormer. The current evaluation is limited to small-scale datasets, which may not fully reflect the method's performance in real-world scenarios. The experimental section should also include a detailed analysis of the computational cost and memory requirements of RGA-IB, especially when compared to other robust GNN methods. This is crucial for understanding the practical applicability of the proposed method. Additionally, the authors should provide a sensitivity analysis of the hyperparameters used in RGA-IB, as this would help in understanding the robustness of the method to different parameter settings. The lack of code makes it difficult to reproduce the results, and the authors should provide the code to ensure the reproducibility of the results.

Finally, the paper would benefit from a more thorough discussion of the limitations of RGA-IB. This should include a discussion of the computational complexity of the method, its sensitivity to hyperparameter settings, and potential failure cases. For example, the authors should discuss the scenarios where RGA-IB might not perform well, such as when the graph structure is highly adversarial or when the data is very noisy. This would provide a more balanced view of the method's strengths and weaknesses. The authors should also discuss the potential impact of the choice of the IB loss function on the performance of RGA-IB, and whether other IB loss functions could be used to further improve the robustness of the method.

### Questions

Please refer to the weaknesses.

### Rating

6

### Confidence

4

**********
