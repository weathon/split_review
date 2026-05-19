### Summary

This paper proposes a meta-learning framework for physics-informed machine learning (PIML) methods to improve their out-of-distribution (OOD) robustness in forecasting dynamical systems. The framework leverages causal structure discovery and invariant risk minimization to learn the underlying ODE structure and adapt to new OOD test tasks. The authors demonstrate the effectiveness of their approach on three OOD forecasting tasks and show significant improvements over existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper addresses a critical challenge in physics-informed machine learning (PIML) by proposing a meta-learning framework that enhances the OOD robustness of PIML models. This is an important and timely contribution to the field.
2. The proposed method is well-motivated and grounded in causal discovery and invariant risk minimization. The authors provide a clear and comprehensive explanation of the framework and its components.
3. The experimental results are convincing and demonstrate the effectiveness of the proposed method. The authors evaluate their approach on three different OOD forecasting tasks and show significant improvements over existing methods. The results are presented clearly and are well-supported by the experimental setup.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that the underlying ODE structure is known and fixed across all training tasks. This assumption may not hold in many real-world scenarios where the ODE structure can vary. Specifically, the method relies on a predefined set of basis functions to represent the ODE, which limits its ability to discover novel or more complex dynamics. The assumption of a fixed structure also neglects the possibility of parameter variations within the known structure, which could be crucial for accurate modeling.
2. The paper does not provide a detailed analysis of the computational complexity of the proposed method. This makes it difficult to assess its scalability to larger and more complex systems. The causal discovery step, in particular, could become a bottleneck for high-dimensional systems or those with a large number of potential causal relationships. The paper lacks a discussion on how the computational cost scales with the number of variables, time steps, or training trajectories.
3. The paper does not discuss the sensitivity of the proposed method to the choice of hyperparameters, such as the learning rate, the number of meta-learning iterations, and the regularization parameters. The performance of meta-learning algorithms is often highly dependent on these choices, and a lack of sensitivity analysis makes it difficult to reproduce the results or apply the method to new problems. The paper should include a more thorough investigation of how these parameters affect the model's performance and robustness.
4. The paper only evaluates the proposed method on three ODE-based systems. It is unclear how well the method would generalize to other types of dynamical systems, such as those with chaotic behavior or stochastic components. The evaluation lacks a broader range of dynamical systems to demonstrate the general applicability of the proposed method.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of assuming a fixed ODE structure. While the authors mention the use of a predefined set of basis functions, they do not adequately address the potential for discovering novel or more complex dynamics that are not captured by this initial set. A more robust approach might involve incorporating techniques from structural learning or neural architecture search to discover the underlying relationships between variables. Furthermore, the paper should explore how the method performs when the true ODE structure deviates from the assumed structure, which is more realistic in many practical scenarios. This could involve introducing controlled perturbations to the ODE structure during training or evaluating the method on systems with known structural variations. The authors should also consider incorporating a mechanism to adapt the basis functions or the structure itself based on the observed data, allowing the model to capture more complex dynamics.

To address the lack of computational complexity analysis, the paper should include a detailed breakdown of the computational cost associated with each step of the proposed method, including the causal discovery step and the meta-learning step. This analysis should consider the scaling of the computational cost with respect to the number of variables, time steps, and training trajectories. The authors should also explore techniques for reducing the computational cost, such as using more efficient causal discovery algorithms or employing parallel computing. Furthermore, the paper should provide empirical results on the runtime of the method for different system sizes and complexities, allowing for a better understanding of its scalability. It would also be beneficial to compare the computational cost of the proposed method with existing OOD forecasting techniques.

Finally, the paper should include a comprehensive sensitivity analysis of the proposed method with respect to its hyperparameters. This analysis should systematically vary each hyperparameter and evaluate its impact on the model's performance. The paper should also provide guidelines for selecting appropriate hyperparameter values for different types of dynamical systems. Furthermore, the paper should expand its evaluation to include a wider range of dynamical systems, including those with chaotic behavior or stochastic components. This would provide a more comprehensive assessment of the method's generalizability and robustness. The authors should also consider evaluating the method on real-world datasets to demonstrate its applicability to practical problems.

### Questions

Please refer to the weaknesses.

### Rating

8: accept, good paper

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
