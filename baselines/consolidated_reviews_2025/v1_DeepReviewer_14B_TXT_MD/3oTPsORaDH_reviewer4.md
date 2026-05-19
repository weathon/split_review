### Summary

The paper introduces SEGNO, a second-order equivariant graph neural network framework that incorporates physical inductive biases to improve the generalization ability of models in simulating complex multi-object physical systems. SEGNO addresses the limitations of existing equivariant graph neural networks (Equiv-GNNs) by incorporating continuous dynamics and second-order motion laws. The authors provide theoretical insights into SEGNO, demonstrating that it can learn a unique trajectory between adjacent states and that the discrepancy between the learned and true trajectories is bounded. Extensive experiments on molecular dynamics and motion capture datasets show that SEGNO outperforms state-of-the-art baselines, highlighting the benefits of incorporating second-order inductive biases in equivariant GNNs.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces SEGNO, a novel framework that combines second-order motion laws with equivariant graph neural networks (Equiv-GNNs) using Neural Ordinary Differential Equations (Neural ODEs). This approach addresses the limitations of existing discrete models by incorporating continuous dynamics and second-order information, which is crucial for accurately modeling physical systems.

2. The authors provide rigorous theoretical analysis, proving the uniqueness of the learned latent trajectory and establishing an upper bound on the discrepancy between the learned and actual latent trajectories. This theoretical foundation strengthens the credibility of the proposed method.

3. The paper demonstrates the effectiveness of SEGNO through extensive experiments on complex dynamical systems, including molecular dynamics and motion capture. The results show significant improvements over state-of-the-art baselines, validating the benefits of incorporating second-order inductive biases.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of SEGNO compared to other models. Understanding the computational cost is crucial for assessing the practicality of the proposed method, especially in large-scale applications. Specifically, the paper lacks a breakdown of the time and memory requirements for both training and inference, making it difficult to evaluate the scalability of SEGNO. A comparison of the number of floating-point operations (FLOPs) or the actual runtime on different hardware configurations would be beneficial.

2. The paper could benefit from a more comprehensive discussion of the limitations of SEGNO. While the authors mention the potential for future work to address stochastic and partial differential equations, a more detailed discussion of the current limitations would provide a clearer understanding of the scope and applicability of SEGNO. For example, it is unclear how SEGNO would perform with systems that exhibit chaotic behavior or with very long time dependencies. The paper should also discuss the sensitivity of SEGNO to the choice of hyperparameters and the potential for overfitting.

3. The paper could provide more insights into the choice of the backbone Equiv-GNN and how it affects the performance of SEGNO. While the authors mention that SEGNO can adapt various backbones, a deeper analysis of the impact of different backbone architectures on the overall performance would be valuable. For instance, the paper could explore how the expressiveness of the backbone affects the ability of SEGNO to learn complex dynamics. It would also be useful to understand if certain backbones are more suitable for specific types of physical systems.

### Suggestions

To address the lack of computational complexity analysis, the authors should include a detailed breakdown of the time and memory requirements for both training and inference. This should include a comparison of the number of floating-point operations (FLOPs) and the actual runtime on different hardware configurations. Furthermore, the authors should analyze the scalability of SEGNO by evaluating its performance on larger datasets and more complex systems. This analysis should also consider the impact of different batch sizes and sequence lengths on the computational cost. Providing this information will allow readers to better assess the practicality of SEGNO for real-world applications.

To enhance the discussion of limitations, the authors should explore the performance of SEGNO on systems that exhibit chaotic behavior or with very long time dependencies. This could involve testing SEGNO on benchmark datasets that are known to be challenging for dynamical systems models. Additionally, the authors should investigate the sensitivity of SEGNO to the choice of hyperparameters and the potential for overfitting. This could involve performing a hyperparameter search and analyzing the generalization performance of SEGNO on held-out data. A more thorough discussion of these limitations will provide a more complete picture of the applicability of SEGNO.

Finally, to provide more insights into the choice of the backbone Equiv-GNN, the authors should conduct a more detailed analysis of the impact of different backbone architectures on the overall performance of SEGNO. This could involve comparing the performance of SEGNO with different backbones on a range of datasets and tasks. The authors should also explore how the expressiveness of the backbone affects the ability of SEGNO to learn complex dynamics. It would be useful to understand if certain backbones are more suitable for specific types of physical systems. This analysis should also consider the computational cost of different backbones and how it affects the overall efficiency of SEGNO.

### Questions

1. How does the computational complexity of SEGNO compare to other models, especially in large-scale applications?

2. Can SEGNO be extended to handle stochastic or partial differential equations, and what are the potential challenges in doing so?

3. How does the choice of the backbone Equiv-GNN affect the performance of SEGNO, and are there specific backbones that are more suitable for certain types of physical systems?

4. What are the limitations of SEGNO in terms of modeling very long-term dynamics or systems with high degrees of freedom?

### Rating

6

### Confidence

2

**********
