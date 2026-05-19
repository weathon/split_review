### Summary

In this paper, the authors introduce a novel method called DPaI (Differentiable Pruning at Initialization), which optimizes the pruning mask using a differentiable approach. DPaI adopts a dynamic and adaptable pruning process, allowing easier optimization and better solutions. The empirical results demonstrate that DPaI significantly outperforms current state-of-the-art PaI methods on various architectures, such as Convolutional Neural Networks and Vision-Transformers.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper introduces a novel differentiable pruning at initialization method that takes into account network topology, specifically the Node-path Balancing Principle (NBP).
2. It extends NPB into a differentiable formulation, making its integration with the training process of sparse neural networks more natural. Different from NPB, our DPaI enables readily use of the existing rich body of efficient gradient-based methods.
3. Extensive experiments on diverse datasets show that the proposed DPaI can discover superior sparse sub-networks across multiple sparsity levels.

### Weaknesses

#### Some Related Works


#### comment

1. In the introduction, the motivation is not clear. The authors should emphasize the limitations of existing work and highlight the significance of this work.
2. In the introduction, the authors list their contributions, but the contributions of this work are somewhat similar to NPB. The authors should further clarify the contribution of this paper.
3. In the method section, the authors should explain in more detail why the existing NPB method is not differentiable and how the proposed method makes NPB differentiable.
4. In the method section, the authors should explain in more detail why the proposed method can make the network thinner and faster.
5. In the experimental section, the authors should explain in detail the significance of applying pruning at initialization methods to various tasks.
6. In the experimental section, the authors should explain in more detail why the DPaI method performs better on different network structures.

### Suggestions

The introduction should more clearly articulate the limitations of current pruning-at-initialization (PaI) techniques. Specifically, the authors should discuss why existing methods struggle to find optimal sparse sub-networks and the computational challenges they pose. For example, many PaI methods rely on iterative pruning and retraining, which is computationally expensive and may not converge to the best solution. The introduction should emphasize the need for a method that can efficiently identify high-performing sparse networks at initialization without extensive retraining. Furthermore, the authors should highlight the significance of their work by explaining how their method addresses these limitations and provides a more efficient and effective approach to PaI. This will help to establish the context and importance of their contribution.

In the method section, the authors need to provide a more detailed explanation of the non-differentiability of the original Node-Path Balancing (NPB) method. They should explain that NPB relies on discrete optimization techniques, which are not compatible with gradient-based optimization methods used in deep learning. The authors should then clearly articulate how their Differentiable Pruning at Initialization (DPaI) method overcomes this limitation by introducing a differentiable relaxation of the NPB objective. This explanation should include the specific mathematical transformations used to make the NPB principle differentiable, such as the use of differentiable approximations for discrete operations. Furthermore, the authors should explain how the DPaI method achieves network thinning and speedup. They should clarify that the method directly optimizes the pruning mask, which determines which connections are removed, resulting in a sparse network. The authors should also explain how the reduced number of connections leads to a thinner and faster network during inference, and how this is different from other pruning methods that may not directly optimize for this.

Finally, the experimental section should provide a more detailed explanation of the significance of applying PaI methods to various tasks. The authors should discuss why finding sparse sub-networks at initialization is beneficial for different applications, such as deployment on resource-constrained devices or accelerating training. They should also explain how the DPaI method's performance varies across different network structures. For example, they should discuss why DPaI might perform better on ResNet-like architectures compared to VGG networks. This discussion should include the specific architectural features that make certain networks more amenable to the DPaI method, such as the presence of skip connections or the depth of the network. This will help to provide a more comprehensive understanding of the method's strengths and limitations.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

3

**********
