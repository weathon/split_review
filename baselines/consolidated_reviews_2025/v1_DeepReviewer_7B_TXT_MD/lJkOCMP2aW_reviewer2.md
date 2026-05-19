### Summary

This paper proposes a multi-scale transformer architecture for time series forecasting. The proposed architecture consists of a multi-scale division module that divides the time series into patches of different sizes, a multi-scale transformer block that performs intra-patch and inter-patch attention, and an adaptive pathway module that dynamically selects the optimal patch sizes for each time series. The proposed model is evaluated on several benchmark datasets and shows improved performance over existing time series forecasting models.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The proposed model is able to capture multi-scale temporal dynamics in time series data, which is an important aspect of time series forecasting.
- The proposed model achieves state-of-the-art performance on several benchmark datasets, which demonstrates the effectiveness of the proposed approach.
- The proposed model is able to adaptively select the optimal patch sizes for each time series, which is an important aspect of time series forecasting.

### Weaknesses

#### comment

- The paper does not provide a clear explanation of why the proposed multi-scale transformer architecture is better than existing multi-scale transformer architectures for time series forecasting. The authors should provide a more detailed comparison of their approach with existing multi-scale transformer architectures and explain the specific advantages of their approach.
- The paper does not provide a detailed analysis of the computational complexity of the proposed model. The authors should provide a detailed analysis of the computational complexity of the proposed model and compare it with existing time series forecasting models.
- The paper does not provide a detailed analysis of the interpretability of the proposed model. The authors should provide a detailed analysis of the interpretability of the proposed model and explain how the model can be used to gain insights into the underlying temporal dynamics of the time series data.
- The paper does not provide a detailed analysis of the limitations of the proposed model. The authors should provide a detailed analysis of the limitations of the proposed model and discuss potential directions for future research.

### Questions

- How does the proposed model handle time series data with multiple seasonalities?
- How does the proposed model handle time series data with missing values?
- How does the proposed model handle time series data with non-stationary trends?
- How does the proposed model handle time series data with high levels of noise?

### Rating

5

### Confidence

4

**********
