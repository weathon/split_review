### Summary

This paper proposes a novel Transformer-based method for long-term time series forecasting. It incorporates the window-based attention and hierarchical representation techniques from the Swin Transformer to address the quadratic computational complexity issue in Transformer models. The authors introduce two variants of Swin4TS: Swin4TS/CD and Swin4TS/CI, which can adapt to channel-dependent and channel-independent strategies, respectively. The proposed method demonstrates state-of-the-art performance on 8 benchmark datasets, outperforming the latest baselines.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method achieves state-of-the-art performance on 8 benchmark datasets, demonstrating its effectiveness in long-term time series forecasting.
3. The authors provide a thorough experimental evaluation, including ablation studies and comparisons with various baselines.

### Weaknesses

#### Some Related Works

[1] Crossformer: Transformer utilizing cross-dimension dependency for multivariate time series forecasting.
[2] Cross-Scale Transformer Pyramid Networks for Multivariate Time Series Forecasting.

#### comment

1. The novelty of the proposed method is limited. The core idea of applying Swin Transformer to time series forecasting is not new, and the paper does not adequately differentiate itself from existing approaches. The use of window-based attention and hierarchical representation, while beneficial, is not a novel contribution in itself, and the paper does not provide sufficient justification for why these specific techniques are particularly well-suited for time series data compared to other attention mechanisms or hierarchical methods. The paper lacks a detailed analysis of how the proposed method addresses the unique challenges of long-term time series forecasting, such as capturing long-range dependencies and handling non-stationarity, beyond the general applicability of Swin Transformer.
2. The paper lacks a comprehensive literature review. The authors should include more recent studies, such as [1] and [2], in their literature review and discuss how their method differs from these recent works. The absence of a detailed comparison with these methods makes it difficult to assess the true contribution of the proposed approach. Specifically, the paper should discuss how the proposed method addresses the limitations of existing approaches, such as the computational cost of full attention mechanisms or the limitations of fixed-scale hierarchical representations.
3. The paper does not provide a detailed analysis of the computational complexity and efficiency of the proposed method. A thorough analysis of the computational cost, including training and inference time, and memory usage, is necessary to evaluate the practical applicability of the method. The paper should also compare the computational efficiency of the proposed method with other state-of-the-art time series forecasting methods.
4. The paper does not provide a detailed analysis of the limitations of the proposed method. The authors should discuss the potential drawbacks of the proposed method, such as its sensitivity to hyperparameter settings, its performance on different types of time series data, and its robustness to noise or outliers. A thorough discussion of these limitations is necessary to provide a balanced assessment of the proposed method.

### Suggestions

The paper would benefit from a more in-depth analysis of the specific adaptations made to the Swin Transformer architecture for time series data. While the use of window-based attention and hierarchical representation is mentioned, the paper lacks a detailed explanation of how these components are tailored to capture the unique characteristics of time series, such as temporal dependencies and seasonality. For example, the paper could discuss how the window size is chosen and how it affects the model's ability to capture both short-term and long-term patterns. Furthermore, the hierarchical representation could be further elaborated by explaining how different levels of the hierarchy capture different temporal scales, and how this is beneficial for long-term forecasting. A more detailed discussion of these aspects would strengthen the paper's contribution and justify the choice of the Swin Transformer architecture for time series forecasting.

To address the lack of a comprehensive literature review, the authors should include a more thorough discussion of recent time series forecasting methods, particularly those that utilize attention mechanisms and hierarchical representations. The paper should not only cite these methods but also provide a detailed comparison of their methodologies and performance characteristics. For instance, the paper could discuss how the proposed method compares to other approaches that use similar attention mechanisms but with different window sizes or hierarchical structures. A more detailed comparison would help to highlight the unique advantages of the proposed method and clarify its contribution to the field. The discussion should also include a critical analysis of the limitations of existing methods and how the proposed method addresses these limitations.

Finally, the paper needs a more rigorous evaluation of the computational complexity and efficiency of the proposed method. The authors should provide a detailed analysis of the time and space complexity of the model, including both training and inference time. This analysis should be compared with other state-of-the-art time series forecasting methods to demonstrate the practical applicability of the proposed approach. Furthermore, the paper should include a discussion of the memory usage of the model, which is particularly important for large-scale time series datasets. The authors should also discuss the scalability of the proposed method to larger datasets and longer time horizons. This analysis would provide a more complete picture of the method's performance and its suitability for real-world applications.

### Questions

1. How does the proposed method handle the potential overfitting issue in long-term time series forecasting, especially when using a large number of parameters in the Swin Transformer architecture?
2. How does the proposed method perform on datasets with different characteristics, such as varying levels of noise, seasonality, and trend?
3. How does the proposed method compare to other recent time series forecasting methods that also utilize Transformer-based architectures, such as those mentioned in the weaknesses section?

### Rating

3

### Confidence

4

**********
