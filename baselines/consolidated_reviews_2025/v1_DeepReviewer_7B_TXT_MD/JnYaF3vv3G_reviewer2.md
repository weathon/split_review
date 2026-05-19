### Summary

This paper proposes a new algorithm for label differential privacy (label DP), which is a relaxation of DP that only requires privacy for the labels. The main idea is to use the public input features to denoise the gradients before adding noise. The paper proposes several denoisers and shows that the proposed algorithm improves the state-of-the-art for label DP. The paper also provides theoretical analysis of the algorithm.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper proposes a novel algorithm for label DP, which is a useful privacy notion for many applications.
- The paper provides a comprehensive empirical evaluation of the proposed algorithm, showing that it outperforms existing methods.
- The paper provides theoretical analysis of the algorithm, which helps to understand its properties.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear explanation of why the proposed algorithm is better than existing methods. While the paper shows that the proposed algorithm outperforms existing methods empirically, it does not provide a theoretical explanation of why this is the case. Specifically, it is not clear how the denoising step helps to reduce the noise added to the gradients, and why this is beneficial for label DP. A more detailed analysis of the noise reduction mechanism would be helpful.
- The paper does not provide a clear explanation of how the proposed algorithm can be used in practice. While the paper provides some experimental results, it does not provide a detailed discussion of how to choose the hyperparameters of the algorithm, such as the denoising parameters and the privacy parameters. It would be helpful to provide some guidance on how to choose these parameters in practice.
- The paper does not provide a clear explanation of the limitations of the proposed algorithm. While the paper shows that the proposed algorithm outperforms existing methods, it does not discuss the limitations of the algorithm, such as the computational cost of the denoising step and the potential for overfitting. A more detailed discussion of these limitations would be helpful.

### Suggestions

The paper would benefit from a more in-depth theoretical analysis of the proposed algorithm. While the empirical results are promising, a theoretical justification for why the denoising step improves label DP is needed. Specifically, the authors should provide a formal analysis of how the denoising step reduces the noise added to the gradients. This could involve analyzing the variance of the noisy gradients with and without the denoising step, and showing that the denoising step leads to a lower variance. Furthermore, the authors should discuss the conditions under which the proposed algorithm is expected to perform well, and when it might not be suitable. For example, it would be useful to analyze the performance of the algorithm when the input features are noisy or when the label distribution is highly imbalanced. This would help to understand the limitations of the algorithm and to identify potential areas for improvement.

In addition to the theoretical analysis, the paper should provide more practical guidance on how to use the proposed algorithm. This should include a detailed discussion of how to choose the hyperparameters of the algorithm, such as the denoising parameters and the privacy parameters. The authors should provide some guidelines on how to select these parameters based on the characteristics of the dataset and the desired level of privacy. For example, they could provide a sensitivity analysis of the algorithm to different parameter values, and show how the performance of the algorithm changes as the parameters are varied. Furthermore, the authors should provide some practical advice on how to implement the algorithm efficiently, and how to handle large datasets. This would make the algorithm more accessible to practitioners and facilitate its adoption in real-world applications.

Finally, the paper should provide a more thorough discussion of the limitations of the proposed algorithm. This should include a discussion of the computational cost of the denoising step, and how this cost scales with the size of the dataset and the dimensionality of the input features. The authors should also discuss the potential for overfitting, and how this can be mitigated. For example, they could provide some guidelines on how to choose the regularization parameters to prevent overfitting. Furthermore, the authors should discuss the limitations of the algorithm in terms of the types of datasets and models for which it is suitable. This would help to clarify the scope of the algorithm and to identify potential areas for future research.

### Questions

- How does the proposed algorithm compare to existing methods in terms of computational cost?
- How can the proposed algorithm be used in practice, and what are the practical challenges of using it?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
