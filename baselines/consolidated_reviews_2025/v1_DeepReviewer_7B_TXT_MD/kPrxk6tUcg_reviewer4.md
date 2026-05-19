### Summary

This paper proposes a neural network-based matrix completion method, AEMC-NE, which is composed of two neural networks: one is a layer-wise network and the other is an element-wise network that is able to learn an activation function for the output layer adaptively. The authors provide theoretical analysis for AEMC-NE, covering both MCAR and MNAR settings. AEMC-NE outperformed many baselines on a few benchmark datasets of collaborative filtering.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The theoretical analysis is comprehensive, covering both MCAR and MNAR settings.
3. The proposed method outperformed many baselines on a few benchmark datasets of collaborative filtering.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The element-wise autoencoder is not a new concept, and its application in the context of matrix completion has been explored in previous works. The paper does not adequately highlight the specific differences or advantages of their approach compared to existing methods that use similar techniques. The core idea of using an autoencoder to learn a transformation is not novel in itself, and the paper needs to better articulate how their specific implementation and theoretical analysis provide a significant advancement.
2. The theoretical analysis, while comprehensive, relies on standard assumptions and techniques. The paper does not introduce fundamentally new theoretical tools or insights. The analysis, while covering both MCAR and MNAR settings, does not provide significant novel results compared to existing literature on matrix completion with missing data. The paper should emphasize the specific theoretical challenges addressed by their method and how it advances the state-of-the-art beyond existing results.
3. The experimental section lacks a thorough comparison with state-of-the-art methods. The paper should include a more comprehensive set of baselines, including recent deep learning-based matrix completion methods, to demonstrate the effectiveness of the proposed approach. The current experiments do not sufficiently establish the superiority of the proposed method over existing techniques.

### Suggestions

The paper needs to more clearly articulate the novelty of its approach in the context of existing methods that use element-wise transformations or adaptive activation functions for matrix completion. While the use of a neural network for this purpose is not entirely new, the specific architecture and training procedure of the proposed method should be highlighted as a key differentiator. The authors should provide a detailed comparison with existing methods that use similar techniques, such as polynomial functions or other non-linear transformations, to demonstrate the advantages of their neural network-based approach. This comparison should not only focus on the architecture but also on the theoretical properties and practical performance of the methods. For example, the authors could discuss the computational complexity, convergence properties, and generalization ability of their method compared to existing approaches. Furthermore, the paper should include a more detailed discussion of the limitations of existing methods and how the proposed method addresses these limitations. This would help to establish the significance of the proposed method and its potential impact on the field.

The theoretical analysis, while comprehensive, needs to be more clearly positioned within the existing literature on matrix completion with missing data. The authors should emphasize the specific theoretical challenges addressed by their method and how it advances the state-of-the-art beyond existing results. The paper should clearly state the assumptions made in the theoretical analysis and discuss the limitations of these assumptions. The authors should also provide a more detailed explanation of the theoretical results, including the implications of the theorems and corollaries. For example, the authors could discuss the conditions under which their method is guaranteed to converge and the rate of convergence. The paper should also include a more detailed discussion of the practical implications of the theoretical results, such as how they can be used to guide the design of the method and the selection of hyperparameters. The authors should also discuss the limitations of the theoretical analysis and potential directions for future research.

The experimental section needs to be significantly improved by including a more comprehensive set of baselines. The paper should compare the proposed method with state-of-the-art deep learning-based matrix completion methods, including those that use similar techniques. The experiments should be conducted on a wider range of datasets, including larger and more complex datasets, to demonstrate the scalability and robustness of the proposed method. The paper should also include a more detailed analysis of the experimental results, including a discussion of the sensitivity of the method to different hyperparameter settings and the impact of different data characteristics on the performance of the method. The authors should also provide a more detailed comparison of the proposed method with existing methods in terms of both performance and computational cost. This would help to establish the practical value of the proposed method and its potential for real-world applications. The authors should also discuss the limitations of the experimental results and potential directions for future research.

### Questions

1. What is the novelty of the proposed method compared to existing works that use element-wise transformations or adaptive activation functions for matrix completion?
2. What is the theoretical contribution of the proposed method compared to existing works on matrix completion with missing data?
3. How does the proposed method compare to state-of-the-art deep learning-based matrix completion methods in terms of performance and computational complexity?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
