### Summary

The paper introduces CrysBFN, a novel method for generating crystal structures using a periodic Bayesian flow network. The key innovation is the adaptation of Bayesian Flow Networks (BFN) to model the periodic physical symmetry of crystals by introducing a periodic Bayesian flow on a hyper-torus. This approach addresses the limitations of existing diffusion-based methods, which struggle with the unique geometric constraints of crystal data. The authors demonstrate the effectiveness of CrysBFN through extensive experiments, showing state-of-the-art performance on benchmarks for both ab initio crystal generation and crystal structure prediction tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach by extending Bayesian Flow Networks (BFN) to handle periodic data on a hyper-torus. This is a significant departure from traditional Euclidean-based generative models and is well-suited for the inherent periodicity of crystal structures.
2. The authors provide a thorough theoretical foundation for their method, including the derivation of the periodic Bayesian flow and the introduction of a new entropy conditioning mechanism. The reformulation of BFN for efficient sampling is also a notable technical contribution.
3. The empirical results are compelling, with CrysBFN achieving state-of-the-art performance on multiple benchmarks. The significant improvement in sampling efficiency (100x speedup over DiffCSP) is a major practical advantage.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed comparison with existing methods, particularly in terms of computational cost and scalability. While the authors mention a 100x speedup in sampling efficiency, a more thorough analysis of training time and resource requirements would be valuable. Specifically, the paper lacks a detailed breakdown of the computational complexity of the proposed method compared to existing diffusion-based approaches, making it difficult to assess the practical trade-offs. For instance, a comparison of the number of floating-point operations (FLOPs) required for training and inference, as well as memory usage, would provide a more complete picture.
2. The theoretical challenges associated with the non-additive accuracy in the periodic Bayesian flow could be explained in more detail. Providing more intuition behind the mathematical formulations would enhance the paper's accessibility. The paper should elaborate on why the standard additive accuracy property of Bayesian flows does not directly translate to the periodic setting, and what specific mathematical challenges arise from this non-additivity. A more detailed explanation of the implications of this non-additivity on the convergence and stability of the training process would also be beneficial.
3. The ablation studies, while informative, could be expanded to include a wider range of datasets and tasks. This would further validate the generalizability of the proposed method. The current ablation studies are limited to a few datasets and tasks, and it is unclear how the method would perform on more diverse crystal structures or under different conditions. For example, testing the method on datasets with varying crystal symmetries or compositions would provide a more robust evaluation of its generalizability.

### Suggestions

To address the lack of detailed computational cost analysis, the authors should include a comprehensive comparison of the computational complexity of CrysBFN with existing diffusion-based methods. This should include a breakdown of the number of FLOPs required for both training and inference, as well as the memory footprint of the model. Furthermore, the authors should provide a comparison of training times on different hardware configurations, and how these times scale with the size of the dataset. This analysis should also consider the impact of different hyperparameter settings on computational cost. For example, the authors could investigate how the number of flow steps affects both the sampling speed and the quality of the generated crystals, and how this trade-off compares to diffusion-based methods. This would provide a more complete understanding of the practical trade-offs associated with using CrysBFN.

To improve the explanation of the non-additive accuracy in the periodic Bayesian flow, the authors should provide a more detailed mathematical analysis of this phenomenon. This should include a clear explanation of why the standard additive accuracy property of Bayesian flows does not hold in the periodic setting, and what specific mathematical challenges arise from this non-additivity. The authors could provide a concrete example, perhaps using a simplified one-dimensional case, to illustrate how the non-additivity affects the flow dynamics. Furthermore, the authors should discuss the implications of this non-additivity on the convergence and stability of the training process. This could include an analysis of how the non-additivity affects the loss landscape and the optimization process. A more intuitive explanation of the mathematical formulations would also enhance the paper's accessibility.

To further validate the generalizability of the proposed method, the authors should expand the ablation studies to include a wider range of datasets and tasks. This should include datasets with varying crystal symmetries, compositions, and sizes. The authors could also consider testing the method on more challenging tasks, such as generating crystals with specific properties or predicting the structure of complex materials. Furthermore, the authors should analyze the performance of the method under different conditions, such as varying the training data size or the number of flow steps. This would provide a more robust evaluation of the method's generalizability and its ability to handle diverse crystal structures and tasks. The authors should also discuss any limitations of the method that are revealed by these additional experiments.

### Questions

1. Could the authors elaborate on the choice of the von Mises distribution as the base distribution for the periodic Bayesian flow? How does it compare to other circular distributions in terms of modeling performance and computational efficiency?
2. The paper mentions that CrysBFN is the first periodic E(3) equivariant Bayesian flow network. Could the authors discuss the potential limitations of this approach and possible future directions for improving the equivariance of the model?
3. How does the proposed entropy conditioning mechanism compare to other conditioning techniques used in generative models? Are there any specific advantages or disadvantages of this approach?

### Rating

6

### Confidence

4

**********
