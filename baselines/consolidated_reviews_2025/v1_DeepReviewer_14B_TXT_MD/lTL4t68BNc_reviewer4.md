### Summary

This paper introduces a novel graph attention method called Robust Graph Attention inspired by Information Bottleneck (RGA-IB), which aims to enhance the robustness of Graph Neural Networks (GNNs) against adversarial attacks. The authors propose that the Information Bottleneck (IB) loss of attention-based GNNs is a strong indicator of their robustness against various graph adversarial attacks. They observe that attention-based GNNs with lower IB loss learn node representations that correlate less with the input training data while aligning better with the target outputs. Motivated by this observation, they design the RGA-IB method to explicitly minimize the IB loss of a multi-layer GNN through a carefully designed graph attention mechanism. The experimental results demonstrate that GNNs equipped with RGA-IB exhibit lower IB loss and significantly improved node classification accuracy under various graph adversarial attacks compared to existing robust GNNs.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel graph attention method, RGA-IB, which is inspired by the Information Bottleneck (IB) principle. This approach is innovative in the context of improving the robustness of GNNs against adversarial attacks.
2. The authors provide a clear and detailed explanation of the RGA-IB method, including the theoretical basis and the implementation details. The paper is well-structured and easy to follow.
3. The experimental results are comprehensive and demonstrate the effectiveness of the proposed method. The authors evaluate RGA-IB on multiple datasets and under various adversarial attack scenarios, showing significant improvements in node classification accuracy compared to existing robust GNNs.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the computational complexity of the proposed RGA-IB method. It is important to understand how the method scales with the size of the graph and the number of layers in the GNN.
2. The authors could provide more insights into the choice of hyperparameters for the RGA-IB method. It would be helpful to understand how sensitive the performance of the method is to different hyperparameter settings.
3. The paper could include a more thorough comparison with other state-of-the-art robust GNN methods. This would help to better understand the advantages and limitations of the proposed RGA-IB method in the context of existing approaches.

### Suggestions

The paper introduces an interesting approach by leveraging the Information Bottleneck (IB) principle for robust graph attention, but it would benefit from a more rigorous analysis of its computational demands. Specifically, a detailed breakdown of the time and space complexity of the RGA-IB method is needed, considering the number of nodes, edges, and layers in the GNN. This analysis should not only focus on the theoretical complexity but also provide empirical evidence of how the method scales with increasing graph sizes. For example, the authors could include experiments on larger datasets to demonstrate the practical scalability of their approach. Furthermore, it would be beneficial to compare the computational cost of RGA-IB with other robust GNN methods, highlighting the trade-offs between robustness and computational efficiency. This would provide a more comprehensive understanding of the practical applicability of the proposed method.

To enhance the practical utility of the RGA-IB method, a more detailed discussion of hyperparameter selection is crucial. The paper should provide a sensitivity analysis of the key hyperparameters, such as the learning rate, the number of attention heads, and the hidden layer sizes. This analysis should explore how different hyperparameter settings affect the performance of the method under various adversarial attack scenarios. It would be helpful to provide guidelines for selecting appropriate hyperparameter values based on the characteristics of the dataset and the specific attack model. Additionally, the authors could investigate the use of automated hyperparameter tuning techniques to optimize the performance of RGA-IB. This would make the method more accessible and easier to use for practitioners.

Finally, a more comprehensive comparison with state-of-the-art robust GNN methods is necessary to fully contextualize the contributions of RGA-IB. The paper should include a detailed comparison with other recent robust GNN methods, highlighting the advantages and limitations of RGA-IB in terms of robustness, accuracy, and computational efficiency. This comparison should not only focus on the performance under different adversarial attacks but also consider other aspects such as the interpretability of the learned representations and the robustness to different types of noise. Furthermore, it would be beneficial to analyze the theoretical properties of RGA-IB, such as its convergence behavior and its ability to generalize to unseen data. This would provide a more complete understanding of the strengths and weaknesses of the proposed method.

### Questions

1. How does the computational complexity of the RGA-IB method compare to other robust GNN methods? Are there any specific computational bottlenecks in the proposed approach?
2. How sensitive is the performance of the RGA-IB method to the choice of hyperparameters? Are there any guidelines for selecting appropriate hyperparameter values?
3. How does the RGA-IB method perform on larger and more complex graph datasets? Are there any scalability issues that need to be addressed?
4. Can the authors provide more insights into the theoretical properties of the RGA-IB method? For example, how does the method ensure the robustness of the learned node representations?

### Rating

6

### Confidence

3

**********
