### Summary

This paper introduces Pathformer, a multi-scale transformer model designed for time series forecasting. The model incorporates multi-scale temporal resolution and temporal distance to capture global and local patterns. It also includes an adaptive pathway mechanism that dynamically selects and aggregates multi-scale characteristics based on the temporal dynamics of the input data. The authors claim that Pathformer outperforms existing models in terms of accuracy and generalization capabilities across various real-world datasets.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-organized and clearly written, making it easy to follow the proposed methodology and experimental results.
2. The authors provide a thorough review of related work, which helps to contextualize the contributions of Pathformer within the existing literature.
3. The experimental results demonstrate that Pathformer achieves state-of-the-art performance on several benchmark datasets, indicating its effectiveness in time series forecasting.

### Weaknesses

#### comment

1. The paper lacks a detailed discussion of the computational complexity of Pathformer, which is an important consideration for practical applications, especially with large-scale datasets.
2. The paper does not provide a comprehensive comparison of Pathformer with other state-of-the-art models, such as PatchTST and TimeMixer, in terms of computational efficiency and memory usage.
3. The paper does not include a discussion of the limitations of Pathformer, such as its sensitivity to hyperparameter settings or its performance on specific types of time series data.
4. The paper does not provide a clear explanation of the rationale behind the choice of patch sizes and how they are determined for different datasets.

### Questions

1. How does the performance of Pathformer vary with different patch sizes, and what is the optimal range of patch sizes for different types of time series data?
2. What is the computational complexity of Pathformer, and how does it compare to other state-of-the-art models in terms of training and inference time?
3. How does Pathformer handle time series data with missing values or irregular sampling intervals?
4. What are the limitations of Pathformer, and how can they be addressed in future work?

### Rating

5

### Confidence

4

**********
