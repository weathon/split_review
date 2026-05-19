### Summary

This paper proposes a method to improve the performance of normalizing flows for OOD detection. The authors address the issue that normalizing flows tend to assign higher likelihoods to OOD samples with low complexity. To address this, they propose incorporating synthetic outliers during training and using a softplus-based penalty for OOD samples. The method is evaluated on image and text datasets, showing improved performance in OOD detection.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.

- The proposed method is simple and easy to implement.

- The authors provide a comprehensive evaluation of their method on both image and text datasets, demonstrating its effectiveness across different domains.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a detailed explanation of the novelty of the proposed method. While the authors mention that they address the bias in normalizing flows, they do not clearly articulate how their approach differs from existing methods for OOD detection, particularly those that use likelihood-based approaches. A more thorough comparison with related work is needed to highlight the unique contributions of this paper.

- The paper does not provide a clear explanation of how the complexity of the input data is measured and why this is important for OOD detection. The authors mention that normalizing flows tend to assign higher likelihoods to OOD samples with low complexity, but they do not provide a detailed explanation of the underlying mechanisms. A more in-depth discussion of the relationship between data complexity and likelihood is needed to justify the proposed method.

- The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors mention that the method is simple and easy to implement, they do not discuss the computational overhead associated with generating synthetic outliers and using the softplus-based penalty. A more thorough analysis of the computational cost is needed to assess the practicality of the proposed method.

- The paper does not provide a detailed analysis of the limitations of the proposed method. While the authors demonstrate the effectiveness of their method on several datasets, they do not discuss the potential failure cases or scenarios where the method may not perform well. A more thorough discussion of the limitations of the proposed method is needed to provide a balanced assessment of its strengths and weaknesses.

### Suggestions

The paper would benefit from a more detailed explanation of the novelty of the proposed method. The authors should clearly articulate how their approach differs from existing methods for OOD detection, particularly those that use likelihood-based approaches. A thorough comparison with related work is needed to highlight the unique contributions of this paper. For example, the authors could discuss how their method addresses the limitations of existing likelihood-based OOD detection methods, such as the sensitivity to the choice of the threshold or the difficulty in modeling complex data distributions. A more detailed discussion of the theoretical underpinnings of the proposed method would also be beneficial. The authors should explain why the softplus-based penalty is effective in addressing the bias towards low-complexity OOD samples and how it relates to the underlying properties of normalizing flows. This would help to establish a stronger theoretical foundation for the proposed method and make it more convincing.

The paper needs a more detailed explanation of how the complexity of the input data is measured and why this is important for OOD detection. The authors should provide a clear definition of data complexity and explain how it is quantified in their experiments. They should also discuss the relationship between data complexity and likelihood, and why normalizing flows tend to assign higher likelihoods to OOD samples with low complexity. A more in-depth discussion of the underlying mechanisms would help to justify the proposed method. For example, the authors could discuss how the model's internal representations are affected by the complexity of the input data and how this affects the likelihood assigned to OOD samples. They could also discuss the limitations of using a simple measure of complexity, such as the length of the input sequence, and how these limitations could be addressed in future work.

The paper should include a more detailed analysis of the computational cost of the proposed method. The authors should provide a breakdown of the computational overhead associated with generating synthetic outliers and using the softplus-based penalty. They should also compare the computational cost of their method with existing OOD detection methods. A more thorough analysis of the computational cost is needed to assess the practicality of the proposed method. For example, the authors could discuss the scalability of their method to large datasets and the impact of the number of synthetic outliers on the computational cost. They should also discuss the memory requirements of their method and how these requirements scale with the size of the input data. A more detailed analysis of the computational cost would help to provide a more complete picture of the practical implications of the proposed method.

### Questions

- How does the proposed method compare to other OOD detection techniques, particularly those based on likelihood models?

- How is the complexity of the input data measured, and why is this important for OOD detection?

- What is the computational cost of the proposed method, and how does it compare to existing approaches?

- What are the limitations of the proposed method, and in what scenarios may it not perform well?

### Rating

5

### Confidence

3

**********
