### Summary

This paper proposes a method for imputing missing values in tabular data using a masked autoencoder framework. The authors claim that their method is simple and effective, and they provide experimental results to support their claim. They also provide a theoretical justification for their method, showing that it tends to learn missingness-invariant representations of tabular data.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.
- The authors provide a theoretical justification for their method.
- The authors provide experimental results to support their claim.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is not very novel, as it is based on existing techniques.
- The theoretical justification is not very strong, and the authors do not provide any experimental results to support their claim.
- The paper does not provide any insights into the limitations of the proposed method.

### Suggestions

The paper would benefit from a more thorough discussion of the novelty of the proposed method. While the authors claim simplicity and effectiveness, the core idea of using a masked autoencoder for imputation is not entirely new. The authors should clearly articulate what specific modifications or insights they bring to this existing framework that make their approach unique and valuable. For example, they could discuss how their re-masking strategy differs from existing masking techniques in the context of tabular data, and why this difference is crucial for imputation performance. Furthermore, a more detailed comparison to other imputation methods, especially those that also leverage autoencoders, would help to better position the contribution of this work. This comparison should not only focus on performance metrics but also on computational complexity, ease of implementation, and sensitivity to hyperparameter choices.

Regarding the theoretical justification, the authors should provide more concrete evidence to support their claim that the method learns missingness-invariant representations. While the paper mentions this property, it lacks a rigorous analysis of how the proposed method achieves this. The authors could, for instance, analyze the learned latent space and demonstrate that the representations of incomplete and complete data points are indeed close. This could involve visualizing the latent space or quantifying the similarity between representations using metrics like cosine similarity. Furthermore, the authors should discuss the limitations of their theoretical analysis. For example, under what conditions might the method fail to learn missingness-invariant representations, and what are the implications of such failures? A more nuanced discussion of these aspects would strengthen the theoretical contribution of the paper.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. The authors should explore scenarios where the method might fail or perform poorly, such as when the missing data pattern is not random or when the data is highly skewed. They should also discuss the computational cost of the method, especially for large datasets, and how it compares to other imputation techniques. Furthermore, the authors should consider the sensitivity of the method to hyperparameter choices and provide guidelines for selecting appropriate values. A thorough discussion of these limitations would provide a more balanced and realistic assessment of the proposed method and help practitioners to use it effectively.

### Questions

- Can you provide more details on the theoretical justification for your method?
- Can you provide more insights into the limitations of your method?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
