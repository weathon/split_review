### Summary

This paper proposes a deep neural operator learning framework GeONet for the Wasserstein geodesic. The method is based on learning the optimality conditions in the dynamic formulation of the OT problem, which is characterized by a coupled PDE system in the primal and dual spaces. The method can learn the highly non-linear Wasserstein geodesic operator from a wide collection of training distributions. The method is mesh-independent, data-driven, and designed to accommodate specific physical laws governed by certain partial differential equations (PDEs).

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well written and easy to follow.
2. The proposed method is interesting and novel.
3. The experimental results show the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only evaluated in low-dimensional settings, and it is unclear how it would scale to high-dimensional problems. Specifically, the experiments are limited to 1D and 2D cases, and there is no discussion of the potential challenges in extending the method to higher dimensions, such as the curse of dimensionality affecting the accuracy of the neural network approximation or the increased computational cost of training.
2. The paper does not provide a theoretical analysis of the proposed method, such as convergence guarantees or error bounds. The lack of theoretical justification makes it difficult to assess the reliability of the method and understand its limitations. Specifically, there is no discussion of the conditions under which the neural network approximation converges to the true solution of the PDE system, or how the approximation error relates to the network architecture and training data.
3. The paper does not compare the proposed method with other existing methods for learning the Wasserstein geodesic, such as the method proposed in "Learning Interpolations Between Distributions with Rectified Flow" (Li et al., 2022). The absence of a comparison with relevant baselines makes it difficult to evaluate the relative performance and advantages of the proposed method. It is unclear whether the proposed method offers any improvement over existing techniques in terms of accuracy, efficiency, or robustness.

### Suggestions

The authors should investigate the scalability of their method to higher-dimensional problems. This could involve conducting experiments on synthetic datasets with increasing dimensionality, or exploring techniques to mitigate the curse of dimensionality, such as using dimensionality reduction methods or incorporating inductive biases into the neural network architecture. Furthermore, the authors should provide a more detailed analysis of the computational cost of their method, including the training time and inference time, and compare it with other methods. It would also be beneficial to explore the use of more efficient neural network architectures or training techniques to improve the scalability of the method. The current evaluation is limited to simple cases and does not provide sufficient evidence for the practical applicability of the method in real-world scenarios.

The paper would benefit significantly from a theoretical analysis of the proposed method. This could involve deriving convergence guarantees for the neural network approximation, or establishing error bounds for the approximation error. The authors should also investigate the relationship between the network architecture, training data, and approximation error. This analysis would provide a deeper understanding of the method's behavior and limitations, and would help to guide the design of more effective neural network architectures. It would also be useful to explore the use of techniques from numerical analysis to analyze the accuracy of the neural network approximation. Without a theoretical foundation, it is difficult to assess the reliability and robustness of the method.

Finally, the authors should compare their method with other existing methods for learning the Wasserstein geodesic, such as the method proposed in "Learning Interpolations Between Distributions with Rectified Flow" (Li et al., 2022). This comparison should include both quantitative and qualitative results, and should evaluate the performance of the methods in terms of accuracy, efficiency, and robustness. The authors should also discuss the advantages and disadvantages of their method compared to existing techniques, and should identify the scenarios in which their method is most effective. This comparison would provide a more comprehensive evaluation of the proposed method and would help to establish its contribution to the field.

### Questions

Please see the Weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
