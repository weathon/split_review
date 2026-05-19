### Summary

The paper proposes an algorithm based on neural operators for learning the dynamic optimal transport mapping between two densities.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The paper is relatively well written and the idea is interesting.

### Weaknesses

#### Some Related Works


#### comment

I believe there are several important issues in the paper:

1. The main issue is that it is not clear at all what the loss (10)-(12) actually optimizes. The fact that it involves the solution to (7) and (8) means that the loss cannot be the Lagrangian (6) because the latter does not involve the solution to (7) and (8). What optimization problem are (10)-(12) the empirical version of? The authors should provide a rigorous derivation of the loss function, starting from a principled optimization problem, and clearly explain how the chosen loss relates to the desired optimal transport solution. The current presentation lacks a clear connection between the proposed loss and the theoretical underpinnings of optimal transport.

2. The DeepONet architecture involves the evaluation of two operators, one for (7) and another for (8). Then, the loss is computed as a sum of three terms, each one involving the evaluation of several operators. How is this computation performed? Is it possible to provide a complexity analysis of the algorithm? The description of how the DeepONet architecture is used to solve the coupled PDEs and compute the loss is insufficient. The authors need to provide a detailed explanation of how the operators are evaluated, how the loss is computed, and a clear analysis of the computational complexity, including the number of operators involved and the cost of each evaluation. Without this, it is difficult to assess the practical feasibility of the proposed method.

3. The authors compare their method with other methods only for the case of Gaussian mixture densities. It is well known that the optimal transport mapping between two Gaussian mixtures is in general not known in closed form. Thus, it is not clear why the authors use the POT library to compute the Wasserstein distance (I guess the authors use the function ot.wasserstein() which actually implements the classic dynamic OT algorithm). It is not clear at all how the reference solutions are computed. The comparison with existing methods is limited to Gaussian mixtures, which is not sufficient to demonstrate the general applicability of the proposed method. Furthermore, the use of `ot.wasserstein()` from the POT library for reference solutions is questionable, as this function implements a static OT algorithm, not the dynamic formulation. The authors need to clarify how the reference solutions are obtained and provide comparisons with other methods on more diverse datasets.

4. The authors do not provide any details about the architectures of the MLPs involved in the algorithm. How many MLPs are involved? What is the architecture of each MLP? How many parameters are involved in total? The lack of details regarding the MLP architectures makes it difficult to reproduce the results and assess the complexity of the model. The authors should provide a complete description of the MLP architectures, including the number of layers, the number of neurons per layer, the activation functions, and the total number of parameters.

5. The authors do not provide any details about the training process. What learning rate is used? How are the parameters found? What hardware is used? How much time does it take to train the model? The absence of details about the training process makes it difficult to evaluate the practical aspects of the proposed method. The authors should provide a comprehensive description of the training process, including the learning rate, the optimization algorithm, the batch size, the hardware used, and the training time.

6. The authors do not provide any details about the inference process. How much time does it take to infer a mapping? The authors should provide a clear explanation of the inference process and the computational cost associated with it.

7. I believe the results on MNIST are not very convincing. It seems that the proposed algorithm is not able to capture the main features of the digits. The results on MNIST are not compelling, and it is not clear that the proposed method can effectively capture the complex structures of real-world data. The authors should provide more qualitative and quantitative results to support their claims.

8. I believe the results on Gaussian mixtures are also not very convincing. The results on Gaussian mixtures, while providing a controlled setting, do not demonstrate the full potential of the proposed method. The authors should provide more challenging examples and comparisons with other methods to better evaluate the performance of their approach.

### Suggestions

The paper needs significant improvements in several areas to be considered for publication. First, the authors must provide a rigorous derivation of the loss function, clearly explaining its connection to the dynamic optimal transport problem. This should include a detailed explanation of how the loss function is derived from the primal-dual formulation of the optimal transport problem, and how it relates to the continuity equation and the Hamilton-Jacobi equation. The authors should also clarify how the proposed loss function ensures that the learned solution satisfies the necessary conditions for optimal transport. Furthermore, the authors should provide a more detailed explanation of how the DeepONet architecture is used to solve the coupled PDEs, including a clear description of how the operators are evaluated and how the loss is computed. A complexity analysis of the algorithm, including the number of operators involved and the cost of each evaluation, is also necessary to assess the practical feasibility of the method. This analysis should include a discussion of the computational cost of both training and inference.

Second, the authors need to provide a more comprehensive evaluation of their method. This includes comparing their method with other existing methods on more diverse datasets, beyond Gaussian mixtures. The authors should also clarify how the reference solutions are obtained for the Gaussian mixtures, and why they use `ot.wasserstein()` from the POT library, which implements a static OT algorithm. It is crucial to use a dynamic OT solver or provide a clear justification for using the static version. The authors should also provide more details about the MLP architectures used in their method, including the number of layers, the number of neurons per layer, the activation functions, and the total number of parameters. This information is essential for reproducibility and for assessing the complexity of the model. Additionally, the authors should provide a comprehensive description of the training process, including the learning rate, the optimization algorithm, the batch size, the hardware used, and the training time. The inference process also needs to be described in detail, including the computational cost associated with it.

Finally, the authors should provide more convincing results on both MNIST and Gaussian mixtures. For MNIST, the authors should demonstrate that their method can effectively capture the complex structures of the digits, and provide more qualitative and quantitative results to support their claims. For Gaussian mixtures, the authors should provide more challenging examples and comparisons with other methods to better evaluate the performance of their approach. The authors should also discuss the limitations of their method and suggest potential directions for future research. The current results are not sufficient to demonstrate the effectiveness and general applicability of the proposed method, and more rigorous evaluation and analysis are needed.

### Questions

I believe that the authors should address the issues I pointed out above.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
