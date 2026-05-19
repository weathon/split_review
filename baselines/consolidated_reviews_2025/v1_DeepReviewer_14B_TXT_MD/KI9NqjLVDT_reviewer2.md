### Summary

This paper introduces REMASKER, a novel method for imputing missing values in tabular data using the masked autoencoding framework. The method is simple, effective, and learns missingness-invariant representations. The authors show that REMASKER performs on par with or outperforms state-of-the-art methods in terms of imputation fidelity and utility under various missingness settings. The performance advantage of REMASKER often increases with the ratio of missing data. The authors also provide a theoretical justification for the effectiveness of REMASKER, showing that it tends to learn missingness-invariant representations of tabular data.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The idea of using the masked autoencoding framework for imputing missing values in tabular data is novel and interesting.
3. The authors provide a theoretical justification for the effectiveness of REMASKER, which adds credibility to their approach.
4. The authors show that REMASKER performs on par with or outperforms state-of-the-art methods in terms of imputation fidelity and utility under various missingness settings.

### Weaknesses

#### Some Related Works


#### comment

1. The theoretical justification is not strong enough. The authors provide a theoretical explanation for the effectiveness of REMASKER, but the analysis is not rigorous and lacks detailed mathematical proofs. Specifically, the connection between the masked autoencoding objective and the imputation task is not clearly established. The paper would benefit from a more formal analysis of how the learned representations are related to the missing data distribution.
2. The computational complexity and efficiency are not well analyzed. The authors do not provide a detailed analysis of the computational complexity of REMASKER, especially when dealing with large-scale tabular datasets. It is unclear how the method scales with the number of features and samples, and a comparison with other imputation methods in terms of runtime and memory usage is missing.

### Suggestions

To strengthen the theoretical justification, the authors should provide a more formal analysis of the relationship between the masked autoencoding objective and the imputation task. This could involve deriving bounds on the imputation error based on the reconstruction error of the autoencoder, or showing that the learned representations capture relevant information about the missing data distribution. For example, the authors could explore the connection between the learned representations and the conditional distribution of the missing values given the observed values. A more rigorous analysis would enhance the credibility of the proposed method and provide a deeper understanding of its effectiveness. Furthermore, it would be beneficial to discuss the limitations of the theoretical analysis and the conditions under which the proposed method is expected to perform well.

To address the lack of computational analysis, the authors should provide a detailed breakdown of the time and memory complexity of REMASKER. This should include an analysis of the computational cost of each step of the algorithm, such as the masking, encoding, and decoding processes. The authors should also compare the computational efficiency of REMASKER with other state-of-the-art imputation methods, both theoretically and empirically. This comparison should consider the scalability of the methods with respect to the number of features and samples. It would be helpful to provide a table or graph showing the runtime and memory usage of REMASKER and other methods on different datasets. This would allow readers to better understand the practical implications of using REMASKER in real-world applications. Additionally, the authors should discuss any potential optimizations that could be used to improve the computational efficiency of REMASKER.

Finally, the authors should provide more details on the hyperparameter selection process. While they mention that the model complexity needs to fit the given dataset, they do not provide specific guidelines on how to choose the optimal hyperparameters. It would be helpful to include a sensitivity analysis of the hyperparameters, showing how the performance of REMASKER varies with different settings. This analysis should consider the impact of hyperparameters such as the masking ratio, the learning rate, and the architecture of the encoder and decoder. The authors should also discuss any heuristics or rules of thumb that they used for hyperparameter selection. This would make the method more accessible to practitioners and facilitate its adoption in real-world applications.

### Questions

1. How does the performance of REMASKER compare to other state-of-the-art methods in terms of computational efficiency?
2. Can the authors provide more insights into the choice of hyperparameters for REMASKER?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
