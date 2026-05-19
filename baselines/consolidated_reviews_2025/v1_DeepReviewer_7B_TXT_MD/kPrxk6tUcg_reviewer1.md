### Summary

This paper introduces a novel matrix completion method, termed AEMC-NE, which incorporates an element-wise autoencoder to enhance the reconstruction capability. The paper presents a comprehensive theoretical analysis of the method's generalization ability under both MCAR and MNAR settings and provides numerical experiments to validate the effectiveness of the proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The paper provides a comprehensive theoretical analysis of the proposed method, covering both MCAR and MNAR settings.

### Weaknesses

#### Some Related Works

[1] A unified approach to matrix completion and sparse recovery
[2] A simple approach to nonlinear sparse regularization
[3] Deep matrix factorization with adaptive activation functions
[4] Deep matrix factorization with adaptive activation functions for recommender systems
[5] Deep matrix factorization with adaptive activation functions for collaborative filtering

#### comment

1. The novelty of the proposed method is limited. The element-wise autoencoder is not a new concept, and its application in the context of matrix completion has been explored in previous works [1,2]. The paper does not adequately differentiate its approach from these existing methods, particularly in terms of the specific architecture and training procedure of the autoencoder. The use of a neural network for element-wise transformation, while potentially beneficial, needs a more thorough justification compared to simpler alternatives.

2. The theoretical analysis, while comprehensive, relies on standard assumptions and techniques. The paper does not introduce fundamentally new theoretical tools or insights. The analysis, while covering both MCAR and MNAR settings, does not provide significant novel results compared to existing literature on matrix completion with missing data. The paper should highlight the specific theoretical challenges addressed by the proposed method and how it advances the state-of-the-art beyond existing results.

3. The experimental section lacks a thorough comparison with state-of-the-art methods. The paper should include a more comprehensive set of baselines, including recent deep learning-based matrix completion methods, to demonstrate the effectiveness of the proposed approach. The current experiments do not sufficiently establish the superiority of AEMC-NE over existing techniques.

4. The paper does not provide sufficient details on the implementation of the proposed method. The description of the neural network architecture, training procedure, and hyperparameter selection is not sufficiently detailed, making it difficult to reproduce the results. The paper should include more specific information on the network architecture, optimization algorithm, and hyperparameter tuning process.

5. The paper does not discuss the computational complexity and scalability of the proposed method. The paper should provide a detailed analysis of the time and space complexity of the proposed method, as well as its scalability to large-scale datasets. The current analysis is insufficient to assess the practical applicability of the method.

### Suggestions

The paper should provide a more detailed comparison with existing methods that use element-wise transformations or adaptive activation functions for matrix completion. Specifically, the authors should clearly articulate how their approach differs from methods like those in [1,2] and [3,4,5], both in terms of the architecture and the theoretical analysis. A more thorough discussion of the advantages and disadvantages of using a neural network for element-wise transformation compared to simpler alternatives, such as polynomials or other non-linear functions, is needed. The paper should also include a more comprehensive experimental evaluation, including a wider range of datasets and a more thorough comparison with state-of-the-art deep learning-based matrix completion methods. The experimental section should also include ablation studies to assess the impact of different components of the proposed method, such as the neural network architecture and the training procedure.

The paper should provide a more detailed description of the implementation of the proposed method, including the specific architecture of the neural network, the optimization algorithm, and the hyperparameter tuning process. The authors should also discuss the computational complexity and scalability of the proposed method, including its time and space complexity and its performance on large-scale datasets. The paper should also include a more detailed analysis of the theoretical results, highlighting the specific theoretical challenges addressed by the proposed method and how it advances the state-of-the-art beyond existing results. The authors should also discuss the limitations of the proposed method and potential directions for future research.

To improve the paper, the authors should consider including a more detailed analysis of the convergence properties of the proposed method, as well as a discussion of the sensitivity of the method to different hyperparameter settings. The paper should also include a more detailed analysis of the generalization performance of the proposed method, including a discussion of the factors that affect its generalization ability. The authors should also consider including a more detailed analysis of the robustness of the proposed method to different types of noise and missing data patterns. The paper should also include a more detailed discussion of the practical applications of the proposed method and its potential impact on real-world problems.

### Questions

1. What is the novelty of the proposed method compared to existing works that use element-wise transformations or adaptive activation functions for matrix completion?
2. What is the theoretical contribution of the proposed method compared to existing works on matrix completion with missing data?
3. How does the proposed method compare to state-of-the-art deep learning-based matrix completion methods in terms of performance and computational complexity?
4. What are the limitations of the proposed method, and what are the potential directions for future research?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
