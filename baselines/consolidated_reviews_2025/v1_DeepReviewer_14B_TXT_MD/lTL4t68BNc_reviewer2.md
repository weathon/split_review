### Summary

This paper introduces a novel graph attention method, Robust Graph Attention inspired by Information Bottleneck (RGA-IB), aimed at enhancing the robustness of Graph Neural Networks (GNNs) against adversarial attacks. The authors find that the IB loss of attention-based GNNs is a strong indicator of their robustness against variant graph adversarial attacks. Attention-based GNNs with lower IB loss learn node representations that correlate less to the input training data while aligning better with the target outputs. Due to better adhering to the IB principle, attention-based GNNs with lower IB loss usually show stronger robustness against graph adversarial attacks. Inspired by such observation, this paper proposes a novel graph attention method termed Robust Graph Attention inspired by Information Bottleneck, or RGA-IB, which explicitly minimizes the IB loss of a multi-layer GNN through a carefully designed graph attention mechanism. Extensive experiment results on semi-supervised node classification under variant graph adversarial attacks show that GNNs equipped with RGA-IB exhibit lower IB loss, which indicates better adherence to the IB principle, and show significantly improved node classification accuracy under graph adversarial attacks compared to existing robust GNNs.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method, Robust Graph Attention inspired by Information Bottleneck (RGA-IB), is novel and interesting. It explicitly minimizes the IB loss of a multi-layer GNN through a carefully designed graph attention mechanism. 
2. The paper is well-written and easy to follow. 
3. The authors conduct extensive experiments on semi-supervised node classification under variant graph adversarial attacks. The results show that GNNs equipped with RGA-IB exhibit lower IB loss and show significantly improved node classification accuracy under graph adversarial attacks compared to existing robust GNNs.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method, Robust Graph Attention inspired by Information Bottleneck (RGA-IB), is novel and interesting. It explicitly minimizes the IB loss of a multi-layer GNN through a carefully designed graph attention mechanism.
2. The paper is well-written and easy to follow.
3. The authors conduct extensive experiments on semi-supervised node classification under variant graph adversarial attacks. The results show that GNNs equipped with RGA-IB exhibit lower IB loss and show significantly improved node classification accuracy under graph adversarial attacks compared to existing robust GNNs.

1. The paper lacks a detailed analysis of the computational complexity of the proposed method. It is unclear how the computational cost scales with the size of the graph and the number of layers in the GNN. A comparison of the time and memory requirements with existing methods would be beneficial.
2. The paper does not provide a theoretical analysis of the proposed method. While the empirical results are promising, a theoretical understanding of why the proposed method works is lacking. For example, it would be helpful to analyze the convergence properties of the proposed optimization algorithm and provide guarantees on the robustness of the learned node representations.
3. The paper does not explore the sensitivity of the proposed method to hyperparameter settings. It is unclear how the performance of the method is affected by the choice of hyperparameters, such as the learning rate, the number of attention heads, and the hidden layer sizes. A sensitivity analysis would help to understand the robustness of the method to different hyperparameter settings.
4. The paper does not provide a detailed analysis of the limitations of the proposed method. It is unclear under what conditions the proposed method might fail or perform poorly. A discussion of the limitations would help to understand the scope of the proposed method and identify areas for future research.

### Suggestions

The paper introduces an interesting approach to enhancing the robustness of GNNs against adversarial attacks by leveraging the Information Bottleneck (IB) principle. However, several aspects of the methodology and evaluation could be strengthened. First, a more thorough analysis of the computational complexity is needed. The paper should provide a detailed breakdown of the time and space complexity of the RGA-IB method, considering the number of nodes, edges, and layers in the GNN. This analysis should also include a comparison with the computational costs of existing robust GNN methods. Furthermore, it would be beneficial to provide empirical results on the training and inference time of the proposed method on different datasets, which would give a more practical understanding of its computational overhead. This analysis should also consider the impact of different hyperparameter settings on the computational cost.

Second, the paper would benefit from a more rigorous theoretical analysis. While the empirical results demonstrate the effectiveness of the proposed method, a theoretical justification for why minimizing the IB loss leads to more robust node representations is lacking. The authors should explore the theoretical properties of the proposed optimization algorithm, such as its convergence behavior and the conditions under which it is guaranteed to find a good solution. It would also be helpful to provide theoretical guarantees on the robustness of the learned node representations against adversarial attacks. This could involve analyzing the sensitivity of the learned representations to perturbations in the input graph structure or node features. Such analysis would provide a deeper understanding of the method's strengths and limitations.

Finally, a more detailed sensitivity analysis of the hyperparameters is needed. The paper should investigate how the performance of the RGA-IB method is affected by different choices of hyperparameters, such as the learning rate, the number of attention heads, and the hidden layer sizes. This analysis should include a systematic exploration of the hyperparameter space and provide guidelines for selecting appropriate hyperparameter values for different datasets. Furthermore, the paper should discuss the limitations of the proposed method in more detail. It is important to identify the scenarios where the method might fail or perform poorly, such as when the graph structure is highly noisy or when the adversarial attacks are very strong. This discussion should also include a comparison with the limitations of existing robust GNN methods, which would help to understand the relative strengths and weaknesses of the proposed approach.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

3

**********
