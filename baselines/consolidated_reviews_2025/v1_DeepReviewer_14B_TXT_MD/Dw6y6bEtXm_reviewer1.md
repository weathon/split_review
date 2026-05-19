### Summary

This paper proposes a method for learning the evolution of physical systems, particularly for cases where only coarse-grained data is available. The authors propose to combine a data driven and a physics-informed approach by introducing an encoder that learns to transform the coarse-grained data to a fine-grained representation that can then be used to predict the evolution of the system. The authors propose to split the learning process into a base-training and a fine-tuning step, where in the first step both the encoder and the transition function are trained, while in the second step only the transition function (with physics loss) is trained. The proposed approach is tested on 3 benchmarks, and the results show that the proposed approach outperforms the considered baselines.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The problem of learning physical systems from coarse-grained data is relevant and challenging.
- The paper is well-structured, and the experiments are well explained and conducted.

### Weaknesses

#### Some Related Works

[1] LEARNING ROBUST PHYSICS-INFORMED DYNAMICS WITH GRAPH NETWORKS
[2] Super-resolution of spatio-temporal processes via Fourier neural operators

#### comment

 - The proposed approach is not explained clearly. In particular, it is unclear why the proposed approach should learn the fine-grained representation of the system (instead of directly predicting it). Specifically, the paper lacks a clear explanation of the necessity for a learnable fine-grained representation rather than a direct prediction of the system's evolution from coarse-grained data. The motivation behind this design choice needs to be more thoroughly justified, especially considering the added complexity of introducing an encoder-decoder architecture.
- The baselines considered are not really suitable for assessing the performance of the proposed approach. In particular, the physics loss is not a standard physics-informed neural network (PINN) loss, and the data loss is not a simple data-driven loss. The combination of these two losses makes the comparison with pure data-driven and pure physics-informed approaches not meaningful. Furthermore, the specific implementation details of how the physics loss is applied to the baseline methods are not sufficiently detailed, making it difficult to assess the fairness of the comparison. The baselines should be more clearly defined, and the loss functions used in each baseline should be explicitly stated.
- The paper overstates the novelty of the proposed approach. In particular, the idea of learning a fine-grained representation of the system has been proposed in previous works, and the idea of using both a data-driven and a physics-informed approach has also been explored in the literature. The paper fails to adequately acknowledge and discuss existing literature that employs similar techniques, such as methods that learn fine-grained representations or combine data-driven and physics-informed approaches. The novelty of the proposed method is therefore not as significant as claimed.
- The authors do not discuss the limitations of the proposed approach. It would be beneficial to discuss the computational cost of the proposed approach, its sensitivity to hyperparameters, and its potential failure modes. The paper lacks a critical analysis of the proposed method's limitations, such as its computational complexity, sensitivity to hyperparameter choices, and potential failure scenarios. A thorough discussion of these limitations is essential for a balanced evaluation of the method's practical applicability.

### Suggestions

The paper needs to provide a more detailed explanation of the rationale behind learning a fine-grained representation instead of directly predicting the system's evolution. The authors should clarify why a direct prediction approach is insufficient for the problem at hand and why the introduction of an encoder-decoder architecture is necessary. This explanation should include a discussion of the specific challenges posed by coarse-grained data and how the proposed architecture addresses these challenges. For example, the authors could discuss the potential for information loss when using coarse-grained data directly and how the fine-grained representation helps to mitigate this loss. Furthermore, the authors should provide a more detailed analysis of the encoder's role in capturing the underlying physics of the system and how this representation is used by the transition function. A clear explanation of the benefits of this approach over direct prediction is crucial for justifying the proposed architecture.

The comparison with baseline methods needs to be significantly improved. The authors should clearly define the loss functions used for each baseline, including the specific form of the physics loss and how it is applied. If the baseline methods are modified to include physics loss, this should be explicitly stated, and the modifications should be justified. It is important to ensure that the comparison is fair and that the baselines are appropriately adapted to the problem setting. Furthermore, the authors should consider including additional baselines that are more directly comparable to the proposed approach, such as methods that also learn a fine-grained representation or combine data-driven and physics-informed approaches. The results should be presented in a way that allows for a clear understanding of the relative performance of each method, and the authors should provide a detailed analysis of the strengths and weaknesses of each approach.

The paper should also include a more thorough discussion of the limitations of the proposed approach. This discussion should include an analysis of the computational cost of the method, its sensitivity to hyperparameter choices, and its potential failure modes. The authors should also discuss the assumptions made by the proposed approach and the conditions under which it is expected to perform well. A critical analysis of these limitations is essential for a balanced evaluation of the method's practical applicability. Furthermore, the authors should acknowledge the existing literature that employs similar techniques and discuss how the proposed approach differs from these methods. This discussion should include a comparison of the proposed method's performance with that of existing methods and a justification for the proposed approach's novelty and contribution.

### Questions

- Why do you think learning the fine-grained representation of the system is beneficial with respect to directly predicting the evolution of the system?
- How is the physics loss calculated for the baseline methods?
- How does your approach compare with the one proposed in [1] for learning the dynamics of fluid flows from sparse data?
- How does your approach compare with the one proposed in [2] for super-resolving coarse and noisy data?

[1] Ha, J., Li, P., & Liu, M. C. (2022). LEARNING ROBUST PHYSICS-INFORMED DYNAMICS WITH GRAPH NETWORKS. In A. D. Bonds, A. Gajjar, A. J. Smola, & P. Wang (Eds.), Advances in Neural Information Processing Systems 35: Annual Conference on Neural Information Processing Systems 2022, NeurIPS 2022, New Orleans, LA, USA, December 2022. Curran Associates, Inc.

[2] Ren, P., Li, Z., Shi, L., Wu, L., & Zhang, L. (2022). Super-resolution of spatio-temporal processes via Fourier neural operators. Computers & Geosciences, 101101.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
