### Summary

This paper proposes to use sparse autoencoders (SAEs) to decompose the attention outputs into sparse, interpretable features. The authors also propose a weight-based head attribution method to associate learned features with specific attention heads. The authors show that the SAEs find a sparse, interpretable decomposition and that they enable qualitative analyses to gain insight into the functioning of attention layers. The authors also use SAEs to analyze the computation performed by the Indirect Object Identification circuit and validate that the SAEs find causally meaningful intermediate variables.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow. The authors provide sufficient background information and clearly explain their methodology and results.
2. The authors propose a novel method to decompose attention outputs into sparse, interpretable features using SAEs. This method provides a new perspective on understanding the internal workings of attention layers and can be used to gain insights into the functioning of attention heads.
3. The authors propose a weight-based head attribution method to associate learned features with specific attention heads. This method provides a way to understand the role of each head in the model's computation and can be used to identify redundant or unnecessary heads.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a comprehensive evaluation of the proposed method. The authors only evaluate their method on a few models and tasks. A more comprehensive evaluation on a wider range of models and tasks is needed to fully assess the effectiveness of the proposed method.
2. The paper does not compare the proposed method to other existing methods for decomposing attention outputs. A comparison to other methods would help to better understand the strengths and weaknesses of the proposed method and its potential for practical applications.
3. The paper does not provide a detailed analysis of the computational complexity of the proposed method. A detailed analysis of the computational complexity would help to better understand the scalability of the proposed method and its potential for use in large-scale applications.

### Suggestions

The authors should expand their evaluation to include a more diverse set of models and tasks to demonstrate the generalizability of their approach. Specifically, they should consider evaluating their method on models with different architectures, such as those using different attention mechanisms or layer configurations. Furthermore, the evaluation should include a wider range of tasks, including tasks that involve different types of data, such as images or audio, to show the versatility of the proposed method. This would provide a more robust assessment of the method's effectiveness and its potential for practical applications. For example, evaluating on models trained on different datasets, or tasks with varying levels of complexity, would provide a more comprehensive understanding of the method's strengths and limitations.

In addition to expanding the evaluation, the authors should also compare their method to other existing methods for decomposing attention outputs. This comparison should include both quantitative and qualitative analyses. Quantitatively, the authors should compare the performance of their method to other methods in terms of metrics such as sparsity, reconstruction error, and the ability to identify meaningful features. Qualitatively, the authors should compare the interpretability of the features learned by their method to those learned by other methods. This would help to better understand the strengths and weaknesses of the proposed method and its potential for practical applications. For example, comparing against methods that use different decomposition techniques, such as PCA or ICA, would provide a more comprehensive understanding of the method's performance.

Finally, the authors should provide a detailed analysis of the computational complexity of their proposed method. This analysis should include both the time and memory requirements of the method. The authors should also discuss the scalability of their method and its potential for use in large-scale applications. This analysis should include a discussion of the factors that affect the computational complexity of the method, such as the size of the model, the number of attention heads, and the size of the input data. Furthermore, the authors should discuss potential optimizations that could be used to reduce the computational complexity of the method. This would help to better understand the practical limitations of the proposed method and its potential for use in real-world applications.

### Questions

1. How does the proposed method compare to other existing methods for decomposing attention outputs?
2. How does the proposed method scale to larger models and datasets?
3. What are the limitations of the proposed method?

### Rating

5

### Confidence

3

**********
