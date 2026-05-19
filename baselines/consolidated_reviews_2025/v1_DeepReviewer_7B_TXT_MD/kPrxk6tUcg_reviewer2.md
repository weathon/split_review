### Summary

This paper proposes a neural network-based matrix completion method that incorporates an element-wise autoencoder to adaptively learn an activation function for the output layer. The authors provide theoretical analysis for the generalization ability of the proposed method under both MCAR and MNAR settings. The numerical results on synthetic and benchmark datasets demonstrate the effectiveness of the proposed method.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. This paper proposes a novel matrix completion method that incorporates an element-wise autoencoder to adaptively learn an activation function for the output layer.
2. The authors provide theoretical analysis for the generalization ability of the proposed method under both MCAR and MNAR settings.
3. The numerical results on synthetic and benchmark datasets demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The element-wise autoencoder is not a new concept, and its application in the context of matrix completion has been explored in previous works. The paper does not adequately highlight the specific differences or advantages of their approach compared to existing methods that use similar techniques. The core idea of using an autoencoder to learn a transformation is not novel in itself, and the paper needs to better articulate how their specific implementation and theoretical analysis provide a significant advancement.
2. The theoretical analysis, while comprehensive, relies on standard assumptions and techniques. The paper does not introduce fundamentally new theoretical tools or insights. The analysis, while covering both MCAR and MNAR settings, does not provide significant novel results compared to existing literature on matrix completion with missing data. The paper should emphasize the specific theoretical challenges addressed by their method and how it advances the state-of-the-art beyond existing results.
3. The experimental section lacks a thorough comparison with state-of-the-art methods. The paper should include a more comprehensive set of baselines, including recent deep learning-based matrix completion methods, to demonstrate the effectiveness of the proposed approach. The current experiments do not sufficiently establish the superiority of the proposed method over existing techniques.

### Suggestions

The paper should more clearly articulate the novelty of their approach by contrasting it with existing methods that use element-wise transformations or adaptive activation functions for matrix completion. A detailed comparison with methods that use similar techniques, such as polynomial functions or other non-linear transformations, is necessary to highlight the specific advantages of their neural network-based approach. The authors should provide a more in-depth discussion of the limitations of existing methods and how their proposed method overcomes these limitations. This should include a discussion of the computational complexity and convergence properties of their method compared to other approaches. Furthermore, the paper should include a more detailed analysis of the theoretical results, emphasizing the specific challenges addressed by their analysis and how it advances the state-of-the-art. The authors should clearly state the assumptions made in their theoretical analysis and discuss the limitations of these assumptions. 

The experimental section needs to be significantly improved by including a more comprehensive set of baselines. The paper should compare the proposed method with state-of-the-art deep learning-based matrix completion methods, including those that use similar techniques. The experiments should be conducted on a wider range of datasets, including larger and more complex datasets, to demonstrate the scalability and robustness of the proposed method. The paper should also include a more detailed analysis of the experimental results, including a discussion of the sensitivity of the method to different hyperparameter settings and the impact of different data characteristics on the performance of the method. The authors should also provide a more detailed analysis of the computational cost of their method compared to other approaches.

Finally, the paper should provide a more detailed discussion of the limitations of the proposed method and potential directions for future research. This should include a discussion of the assumptions made in the theoretical analysis and the potential impact of these assumptions on the practical applicability of the method. The authors should also discuss the potential for extending their method to other matrix completion problems, such as those with non-uniform missingness patterns or those with additional side information. The paper should also discuss the potential for using the proposed method in other applications, such as recommendation systems or computer vision.

### Questions

1. What is the novelty of the proposed method compared to existing works that use element-wise transformations or adaptive activation functions for matrix completion?
2. What is the theoretical contribution of the proposed method compared to existing works on matrix completion with missing data?
3. How does the proposed method compare to state-of-the-art deep learning-based matrix completion methods in terms of performance and computational complexity?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
