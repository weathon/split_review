### Summary

This paper studies the problem of out-of-distribution (OOD) forecasting in physics-informed machine learning (PIML). Specifically, the paper focuses on OOD forecasting where test data comes from the same dynamical system but with OOD initial conditions and OOD system parameters. The paper proposes a meta-learning framework called MetaPhysiCa to improve the OOD robustness of PIML models. The proposed method leverages causal structure discovery to learn the underlying ODE structure and uses meta-learning to learn shared knowledge across multiple training trajectories. The paper evaluates the proposed method on three OOD forecasting tasks and shows significant improvements over existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper addresses an important problem in PIML, which is OOD forecasting. This is a crucial problem for real-world applications where the model needs to generalize to unseen scenarios.

2. The proposed method, MetaPhysiCa, is novel and combines causal structure discovery with meta-learning in a unique way to improve OOD robustness in PIML.

3. The paper is well-written and easy to follow.

4. The paper provides a comprehensive evaluation of the proposed method on three different OOD forecasting tasks, demonstrating its effectiveness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that the underlying ODE structure is known and fixed across all training tasks. This assumption may not hold in many real-world scenarios where the ODE structure can vary. Specifically, the method relies on a predefined set of basis functions to represent the ODE, which limits its ability to discover novel or more complex dynamics. The assumption of a fixed structure also neglects the possibility of parameter variations within the known structure, which could be crucial for accurate modeling.

2. The paper does not provide a detailed analysis of the computational complexity of the proposed method. This makes it difficult to assess its scalability to larger and more complex systems. The causal discovery step, in particular, could become a bottleneck for high-dimensional systems or those with a large number of potential causal relationships. The paper lacks a discussion on how the computational cost scales with the number of variables, time steps, or training trajectories.

3. The paper does not discuss the sensitivity of the proposed method to the choice of hyperparameters, such as the learning rate, the number of meta-learning iterations, and the regularization parameters. The performance of meta-learning algorithms is often highly dependent on these choices, and a lack of sensitivity analysis makes it difficult to reproduce the results or apply the method to new problems. The paper should include a more thorough investigation of how these parameters affect the model's performance and robustness.

4. The paper only evaluates the proposed method on three ODE-based systems. It is unclear how well the method would generalize to other types of dynamical systems, such as those with chaotic behavior or stochastic components. The evaluation lacks a broader range of dynamical systems to demonstrate the general applicability of the proposed method.

### Suggestions

The paper should address the limitation of assuming a fixed ODE structure by exploring methods for learning the ODE structure itself, rather than relying on a predefined set of basis functions. This could involve incorporating techniques from structural learning or neural architecture search to discover the underlying relationships between variables. Furthermore, the paper should investigate how the method performs when the true ODE structure deviates from the assumed structure, which is more realistic in many practical scenarios. This could involve introducing controlled perturbations to the ODE structure during training or evaluating the method on systems with known structural variations. The authors should also consider incorporating a mechanism to adapt the basis functions or the structure itself based on the observed data, allowing the model to capture more complex dynamics.

To address the lack of computational complexity analysis, the paper should include a detailed breakdown of the computational cost associated with each step of the proposed method, including the causal discovery step and the meta-learning step. This analysis should consider the scaling of the computational cost with respect to the number of variables, time steps, and training trajectories. The authors should also explore techniques for reducing the computational cost, such as using more efficient causal discovery algorithms or employing parallel computing. Furthermore, the paper should provide empirical results on the runtime of the method for different system sizes and complexities, allowing for a better understanding of its scalability. It would also be beneficial to compare the computational cost of the proposed method with existing OOD forecasting techniques.

Finally, the paper should include a comprehensive sensitivity analysis of the proposed method with respect to its hyperparameters. This analysis should systematically vary each hyperparameter and evaluate its impact on the model's performance. The paper should also provide guidelines for selecting appropriate hyperparameter values for different types of dynamical systems. Furthermore, the paper should expand its evaluation to include a wider range of dynamical systems, including those with chaotic behavior or stochastic components. This would provide a more comprehensive assessment of the method's generalizability and robustness. The authors should also consider evaluating the method on real-world datasets to demonstrate its applicability to practical problems.

### Questions

1. How does the proposed method handle cases where the true ODE structure is unknown or partially known?

2. How does the computational complexity of the proposed method scale with the size of the system and the number of training trajectories?

3. How sensitive is the proposed method to the choice of hyperparameters, such as the learning rate, the number of meta-learning iterations, and the regularization parameters?

4. How does the proposed method perform on other types of dynamical systems, such as those with chaotic behavior or stochastic components?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
