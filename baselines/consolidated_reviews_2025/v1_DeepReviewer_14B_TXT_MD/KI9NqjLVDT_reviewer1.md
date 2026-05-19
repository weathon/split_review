### Summary

The authors propose REMASKER, a method for imputing missing values in tabular data by extending the masked autoencoding framework. REMASKER not only imputes missing values but also reimplements a subset of observed values (re-masking), optimizing the autoencoder to reconstruct this re-masked set and applying the trained model to predict the missing values. The authors demonstrate that REMASKER performs on par with or outperforms state-of-the-art methods in terms of imputation fidelity and utility across various missingness settings, with its performance advantage increasing with the ratio of missing data.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The idea is simple but effective. The re-masking strategy is a novel idea for tabular data imputation.
3. The experiments are extensive and thorough, with various datasets, missingness scenarios, and baselines.

### Weaknesses

#### Some Related Works


#### comment

1. The theoretical justification is not strong enough. The authors provide a theoretical explanation for the effectiveness of REMASKER, but the analysis is not rigorous and lacks detailed mathematical proofs. Specifically, the paper does not provide a clear theoretical explanation of why the re-masking strategy should lead to better imputation performance compared to standard masked autoencoders. The argument that minimizing the difference between representations under different masks leads to missingness-invariant representations is not rigorously proven and lacks a clear connection to the imputation task. The analysis would benefit from a more formal treatment, including a clear definition of the properties of the learned representations and how these properties relate to imputation accuracy.
2. The computational complexity and efficiency are not well analyzed. The authors do not provide a detailed analysis of the computational complexity of REMASKER, especially when dealing with large-scale tabular datasets. The paper lacks a discussion of how the re-masking strategy impacts the computational cost, and there is no comparison of the computational efficiency of REMASKER with other state-of-the-art methods. A more thorough analysis should include a breakdown of the time and memory requirements for each step of the algorithm, and how these scale with the size of the dataset and the number of features. Furthermore, the paper does not discuss the practical implications of these computational costs for real-world applications.

### Suggestions

The authors should provide a more rigorous theoretical analysis of the re-masking strategy. This should include a formal definition of the properties of the learned representations and a mathematical proof that demonstrates how these properties lead to improved imputation performance. For example, the authors could explore the relationship between the re-masking strategy and the generalization ability of the model, or provide a bound on the imputation error based on the properties of the learned representations. The theoretical analysis should also address the limitations of the proposed approach and discuss the conditions under which it is expected to perform well. This would provide a more solid foundation for the proposed method and enhance the understanding of its behavior.

The paper should include a detailed analysis of the computational complexity of REMASKER. This analysis should include a breakdown of the time and memory requirements for each step of the algorithm, and how these scale with the size of the dataset and the number of features. The authors should also compare the computational efficiency of REMASKER with other state-of-the-art methods, both theoretically and empirically. This comparison should include a discussion of the practical implications of these computational costs for real-world applications. For example, the authors could provide a table that shows the training time and memory usage of REMASKER and other methods on different datasets, and discuss the trade-offs between imputation accuracy and computational cost. This would help the readers to understand the practical limitations of the proposed method and to choose the most appropriate method for their specific needs.

Finally, the authors should provide more details about the implementation of REMASKER. This should include a discussion of the specific choices made for the hyperparameters, such as the masking ratio, the learning rate, and the architecture of the autoencoder. The authors should also discuss the sensitivity of the method to these hyperparameters and provide guidelines for choosing appropriate values. Furthermore, the authors should provide a clear explanation of how the method handles different types of missing data, such as missing completely at random (MCAR), missing at random (MAR), and missing not at random (MNAR). This would make the method more accessible to other researchers and facilitate its adoption in practice.

### Questions

Please see the weaknesses above.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
