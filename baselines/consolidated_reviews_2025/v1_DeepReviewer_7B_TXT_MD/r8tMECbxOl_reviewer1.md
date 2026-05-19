### Summary

The paper proposes TDTransformer for tabular data tabular learning, which overcomes the limitations of the transformer-based architecture in learning the heterogeneous nature of tabular data. Specifically, the paper proposes three embedding processes for different types of columns (categorical, numerical, binary). The paper conducts experiments on 76 OpenML datasets to show the effectiveness of the proposed method.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-organized and easy to follow.
2. The paper provides a comprehensive review of the literature on tabular data learning.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the paper is limited. The proposed method is a combination of existing techniques, such as embedding, positional encoding, and the PLE. The paper does not provide a clear explanation of how these components are adapted or modified for tabular data. The specific adaptations of these techniques for tabular data are not sufficiently detailed, making it difficult to assess the true novelty of the approach.
2. The paper lacks theoretical analysis. The paper does not provide any theoretical justification for the proposed method, such as convergence analysis or generalization bounds. This makes it difficult to understand why the method works and under what conditions it is expected to perform well.
3. The paper does not compare the proposed method with some recent transformer-based methods, such as TabLLM and TableLLama. The absence of these comparisons makes it difficult to assess the relative performance of the proposed method against state-of-the-art transformer-based approaches for tabular data.
4. The paper does not provide a detailed analysis of the computational complexity of the proposed method. The paper should include a discussion of the time and space complexity of the method, as well as a comparison with other methods. This is important for understanding the scalability of the method to large datasets.
5. The paper does not provide an ablation study to evaluate the contribution of each component of the proposed method. The paper should include an ablation study to determine the impact of each component (e.g., the different embedding processes for categorical, numerical, and binary columns) on the overall performance of the method. This is important for understanding the importance of each component and for identifying potential areas for improvement.

### Suggestions

The paper should provide a more detailed explanation of how the proposed method adapts existing techniques for tabular data. Specifically, the paper should explain how the embedding, positional encoding, and PLE are modified to handle the unique characteristics of tabular data, such as the mixed data types and the lack of a natural ordering of rows. For example, the paper should explain how the PLE is adapted to handle numerical values that do not fall within the [0,1] range, and how the column-type-aware positional encoding is implemented. The paper should also provide a more detailed explanation of the tokenization process for categorical columns, including how the tokens are generated and how they are used to create embeddings. The paper should also discuss the limitations of the proposed method and identify potential areas for future research.

The paper should include a theoretical analysis of the proposed method, including a discussion of its convergence properties and generalization bounds. This analysis should provide a theoretical justification for why the method works and under what conditions it is expected to perform well. For example, the paper could analyze the impact of the different embedding processes on the convergence rate of the model. The paper should also provide a more detailed discussion of the assumptions underlying the proposed method and how these assumptions affect its performance. This theoretical analysis would help to establish the validity of the proposed method and provide a deeper understanding of its behavior.

The paper should include a more comprehensive experimental evaluation of the proposed method, including comparisons with recent transformer-based methods such as TabLLM and TableLLama. The paper should also include an ablation study to evaluate the contribution of each component of the proposed method. This ablation study should systematically remove each component and evaluate the impact on the overall performance of the method. For example, the paper could evaluate the performance of the method with and without the column-type-aware positional encoding, or with different embedding processes for numerical and categorical columns. This would help to identify the most important components of the proposed method and to understand their relative importance. The paper should also include a discussion of the computational complexity of the proposed method and compare it with other methods.

### Questions

See Weaknesses.

### Rating

5

### Confidence

4

**********
