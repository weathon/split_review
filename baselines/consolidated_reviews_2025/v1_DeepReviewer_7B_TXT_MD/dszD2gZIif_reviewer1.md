### Summary

This paper introduces the Swin4TS algorithm for long-term time series forecasting. The algorithm incorporates two key designs from the Swin Transformer to model time series data: window-based attention and hierarchical representation. The authors claim that Swin4TS can effectively adapt to both channel-dependent and channel-independent strategies, resulting in two variants: Swin4TS/CD and Swin4TS/CI. The paper asserts that these variants complement each other and achieve state-of-the-art performance on 8 benchmark datasets.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough experimental evaluation on 8 benchmark datasets, demonstrating the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works

[1] Rethinking the time–frequency transformation in the frequency domain for time series forecasting
[2] Cross-Scale Transformer Pyramid Networks for Multivariate Time Series Forecasting
[3] Cross-Scale Transformer Pyramid Networks for Multivariate Time Series Forecasting
[4] Multi-Scale Transformer Pyramid Networks for Multivariate Time Series Forecasting
[5] Multi-Scale Transformer Pyramid Networks for Multivariate Time Series Forecasting

#### comment

1. The novelty of the proposed method is limited. The core idea of applying Swin Transformer to time series forecasting is not new, and the paper does not adequately differentiate itself from existing approaches. The use of window-based attention and hierarchical representation, while beneficial, is not a novel contribution in itself, and the paper does not provide sufficient justification for why these specific techniques are particularly well-suited for time series data compared to other attention mechanisms or hierarchical methods.
2. The paper lacks a comprehensive literature review. The authors should include more recent studies, such as [1], [2], [3], [4], and [5], in their literature review and discuss how their method differs from these recent works. The absence of a detailed comparison with these methods makes it difficult to assess the true contribution of the proposed approach. Specifically, the paper should discuss how the proposed method addresses the limitations of existing approaches, such as the computational cost of full attention mechanisms or the limitations of fixed-scale hierarchical representations.
3. The paper does not provide a detailed analysis of the computational complexity and efficiency of the proposed method. A thorough analysis of the computational cost, including training and inference time, and memory usage, is necessary to evaluate the practical applicability of the method. The paper should also compare the computational efficiency of the proposed method with other state-of-the-art time series forecasting methods.
4. The paper does not provide a detailed analysis of the limitations of the proposed method. The authors should discuss the potential drawbacks of the proposed method, such as its sensitivity to hyperparameter settings, its performance on different types of time series data, and its robustness to noise or outliers. A thorough discussion of these limitations is necessary to provide a balanced assessment of the proposed method.

### Suggestions

The paper should provide a more detailed explanation of the specific design choices made in the Swin4TS architecture. For example, the authors should elaborate on the rationale behind using a window-based attention mechanism instead of other attention mechanisms, such as global attention or local attention. They should also provide a detailed explanation of how the hierarchical representation is constructed and how it captures multi-scale temporal dependencies. Furthermore, the authors should discuss the specific parameters of the Swin Transformer, such as the number of layers, the size of the embedding, and the number of attention heads, and justify their choices with empirical evidence. A more thorough analysis of these design choices would significantly strengthen the paper's contribution and provide a better understanding of the proposed method.

The paper needs a more comprehensive comparison with existing state-of-the-art time series forecasting methods. The authors should not only compare the performance of their method with other methods on benchmark datasets but also discuss the differences in methodology and computational complexity. For example, the paper should compare the proposed method with other methods that use similar attention mechanisms or hierarchical representations. The authors should also discuss the advantages and disadvantages of their method compared to these existing methods. A more detailed comparison would help to clarify the unique contributions of the proposed method and its potential impact on the field. The paper should also include a discussion of the limitations of the proposed method and suggest potential directions for future research.

The paper should include a more detailed analysis of the computational complexity and efficiency of the proposed method. The authors should provide a theoretical analysis of the time and space complexity of the proposed method, as well as empirical results on the training and inference time and memory usage. The paper should also compare the computational efficiency of the proposed method with other state-of-the-art time series forecasting methods. The authors should also discuss the scalability of the proposed method to large-scale time series datasets. A more thorough analysis of the computational complexity and efficiency would provide a more complete picture of the practical applicability of the proposed method.

### Questions

See weakness.

### Rating

3

### Confidence

4

**********
