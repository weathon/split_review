### Summary

This paper proposes a per-instance noise variance optimization (NVO) game, framed as a common interest game, to achieve per-instance differential privacy (pDP). The authors prove that the Nash equilibrium (NE) points of this game ensure pDP. They propose two algorithms to derive strategies for achieving NE: an approximate enumeration (AE) using a genetic algorithm and best response dynamics (BRD). The authors evaluate the NVO game on various statistical metrics and regression tasks, demonstrating that the proposed method outperforms the conventional Laplace mechanism.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive background on per-instance differential privacy (pDP) and the challenges associated with achieving it.
3. The authors propose a novel approach to achieve pDP by optimizing noise variance, which is a significant contribution to the field.
4. The authors provide a theoretical analysis of their proposed method, proving that the NE points of the NVO game ensure pDP.
5. The authors evaluate their method on various statistical metrics and regression tasks, demonstrating its effectiveness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed algorithms. This is important for assessing the practicality of the method, especially for large datasets.
2. The paper does not provide a detailed analysis of the sensitivity of the proposed method to the choice of hyperparameters. This is important for understanding the robustness of the method.
3. The paper does not provide a detailed comparison of the proposed method with other existing methods for achieving pDP. This is important for understanding the advantages and disadvantages of the proposed method.
4. The paper does not provide a detailed discussion of the limitations of the proposed method. This is important for understanding the scope of applicability of the method.

### Suggestions

The paper would benefit from a more thorough analysis of the computational complexity of the proposed algorithms, particularly the Best Response Dynamics (BRD) and the Approximate Enumeration (AE) methods. While the paper mentions that BRD is more efficient, a more detailed analysis, including a breakdown of the time complexity for each step and how it scales with the size of the dataset and the number of iterations, is needed. For instance, providing a Big O notation for the time complexity of each step in the BRD algorithm, and comparing it to the complexity of the AE method, would be beneficial. Furthermore, the paper should discuss the practical implications of this complexity, such as the expected runtime for different dataset sizes. This analysis should also consider the memory requirements of the algorithms, which can be a limiting factor for large datasets. A concrete example of how the runtime scales with the number of data points would greatly enhance the practical value of the paper.

In addition to the computational complexity, a more detailed analysis of the sensitivity of the proposed method to hyperparameter choices is crucial. The paper should explore how the choice of the discretization parameter K, the target epsilon, and the initialization of the variance set affects the performance of the method. For example, the paper could include experiments that systematically vary these parameters and analyze the resulting impact on the privacy-utility trade-off. It would be helpful to provide guidelines for selecting appropriate values for these hyperparameters based on the characteristics of the dataset and the desired level of privacy. Furthermore, the paper should discuss the potential for adaptive hyperparameter tuning, which could improve the robustness of the method. A sensitivity analysis would provide a more complete understanding of the method's behavior and its practical applicability.

Finally, the paper should provide a more comprehensive comparison of the proposed method with existing approaches for achieving per-instance differential privacy (pDP). While the paper mentions that the proposed method outperforms the conventional Laplace mechanism, it would be beneficial to include a more detailed comparison with other state-of-the-art methods. This comparison should not only focus on the privacy guarantees but also on the utility of the resulting mechanisms. For example, the paper could compare the proposed method with other methods that achieve pDP through different mechanisms, such as noise addition or data perturbation. A detailed comparison should also include a discussion of the advantages and disadvantages of each method, highlighting the specific scenarios where the proposed method is most effective. This would help to position the proposed method within the broader context of pDP research and provide a clearer understanding of its contributions.

### Questions

1. How does the proposed method compare to other existing methods for achieving pDP in terms of both privacy guarantees and utility?
2. What is the computational complexity of the proposed algorithms, and how does it scale with the size of the dataset?
3. How sensitive is the proposed method to the choice of hyperparameters, and what are the guidelines for selecting appropriate values?
4. What are the limitations of the proposed method, and in what scenarios is it most effective?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
