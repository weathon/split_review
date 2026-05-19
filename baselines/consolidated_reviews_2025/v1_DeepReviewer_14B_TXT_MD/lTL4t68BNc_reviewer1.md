### Summary

This paper proposes a robust graph attention method inspired by the information bottleneck (IB) principle, called RGA-IB. It aims to improve the robustness of GNNs against adversarial attacks by minimizing the IB loss. Extensive experiments are conducted to evaluate the performance of RGA-IB.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The idea of leveraging the IB principle to enhance the robustness of GNNs is interesting.
2. The authors provide a theoretical analysis of the relationship between the IB loss and the robustness of GNNs.
3. The authors conduct extensive experiments to evaluate the performance of RGA-IB.

### Weaknesses

#### Some Related Works

[1] Graph Structure Learning for Robust Graph Neural Networks
[2] On the Robustness of Graph Neural Networks against Adversarial Attacks

#### comment

1. The novelty of this paper is somewhat limited. There have been several studies that leverage the IB principle to enhance the robustness of GNNs, such as GIB, RG-GIB, and UGRL. The authors do mention these methods in the related works section. However, they do not provide a detailed comparison between RGA-IB and these existing methods. The authors should provide a more comprehensive comparison to highlight the advantages of RGA-IB over these methods. Specifically, the authors should clarify how RGA-IB's approach to minimizing the IB loss differs from these prior works, particularly in terms of the specific formulation of the IB objective and the optimization strategy used. A more detailed discussion of the differences in the attention mechanisms and how they contribute to robustness would also be beneficial.

2. The authors claim that RGA-IB reduces the IB loss, but they do not provide a formal proof of this claim. It would be better if the authors could provide a theoretical guarantee that RGA-IB reduces the IB loss. The authors should provide a rigorous mathematical derivation demonstrating that the proposed attention mechanism, when optimized, leads to a reduction in the IB loss. This should include a clear definition of the IB loss function being used and a proof that the gradient descent update rule for the attention weights indeed minimizes this function.

3. In the experiments, the authors only evaluate the performance of RGA-IB on small-scale datasets. It would be better if the authors could evaluate the performance of RGA-IB on large-scale datasets, such as OGBN-ARXIV. The authors should also compare RGA-IB with other state-of-the-art robust GNN methods, such as GCORN and SGFormer. The evaluation should include a range of datasets with varying sizes and characteristics to demonstrate the generalizability of the proposed method. Furthermore, the comparison with state-of-the-art methods should include a detailed analysis of the computational cost and memory requirements of RGA-IB compared to other methods.

4. The authors do not provide the code for RGA-IB, which makes it difficult to reproduce the results. It would be better if the authors could provide the code to ensure the reproducibility of the results. The code should be well-documented and include instructions on how to run the experiments. This will allow other researchers to verify the claims made in the paper and build upon the proposed method.

5. The authors do not discuss the limitations of RGA-IB. It would be better if the authors could discuss the potential limitations of RGA-IB, such as its computational complexity and its sensitivity to hyperparameter settings. The authors should also discuss the potential failure cases of RGA-IB and provide insights into why the method might fail in certain scenarios. This will help other researchers to better understand the applicability of RGA-IB and its limitations.

### Suggestions

To address the lack of detailed comparison with existing methods, the authors should include a table that explicitly compares RGA-IB with GIB, RG-GIB, and UGRL across several dimensions, such as the specific formulation of the IB loss, the attention mechanism used, the optimization strategy, and the computational complexity. This table should highlight the unique aspects of RGA-IB and clearly articulate its advantages over these existing methods. Furthermore, the authors should provide a more in-depth discussion of how the proposed attention mechanism differs from the attention mechanisms used in these prior works, and how these differences contribute to the improved robustness of RGA-IB. This discussion should include a theoretical analysis of the properties of the attention mechanism and how it affects the information flow in the network. The authors should also provide a more detailed explanation of how the proposed method addresses the limitations of existing methods, such as the local dependency assumption of GIB.

To provide a theoretical guarantee for the reduction of the IB loss, the authors should include a formal proof that the proposed attention mechanism, when optimized, leads to a reduction in the IB loss. This proof should include a clear definition of the IB loss function being used and a rigorous mathematical derivation demonstrating that the gradient descent update rule for the attention weights indeed minimizes this function. The proof should also address any assumptions made about the data distribution or the network architecture. Furthermore, the authors should provide a theoretical analysis of the convergence properties of the optimization algorithm used to train RGA-IB. This analysis should include a discussion of the conditions under which the algorithm is guaranteed to converge to a local minimum of the IB loss function. The authors should also provide a discussion of the limitations of the theoretical analysis and the potential impact of these limitations on the practical performance of the method.

To improve the experimental evaluation, the authors should include experiments on a wider range of datasets, including large-scale datasets such as OGBN-ARXIV, and datasets with varying characteristics. The authors should also compare RGA-IB with other state-of-the-art robust GNN methods, such as GCORN and SGFormer, and provide a detailed analysis of the computational cost and memory requirements of RGA-IB compared to these methods. The evaluation should include a range of metrics, such as accuracy, robustness, and efficiency. The authors should also provide a discussion of the limitations of the experimental evaluation and the potential impact of these limitations on the conclusions drawn from the results. Finally, the authors should provide the code for RGA-IB to ensure the reproducibility of the results. The code should be well-documented and include instructions on how to run the experiments.

### Questions

Please refer to the weaknesses.

### Rating

5

### Confidence

4

**********
