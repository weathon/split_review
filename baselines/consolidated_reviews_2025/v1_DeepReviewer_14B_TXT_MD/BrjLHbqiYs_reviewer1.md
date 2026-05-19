### Summary

This paper addresses the challenge of quantifying multimodal interactions in a semi-supervised setting, where labeled unimodal data and unlabeled multimodal data are available. The authors derive lower and upper bounds on the amount of multimodal interactions using information-theoretic measures.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper provides a precise information-theoretic definition of multimodal interactions and derives lower and upper bounds to quantify these interactions in a semi-supervised setting. This theoretical analysis contributes to a deeper understanding of multimodal interactions.

2. The authors demonstrate how the theoretical results can be used to estimate multimodal model performance, guide data collection, and select appropriate multimodal models for various tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes finite sample spaces for features and labels, which may limit its applicability to real-world datasets that are often continuous and high-dimensional. The authors propose discretization as a solution, but the effectiveness of this approach depends on the choice of discretization method and the inherent structure of the data. For instance, naive discretization can lead to a loss of information and poor approximation of the underlying distributions, especially when dealing with high-dimensional data. The paper does not provide sufficient details on how to choose appropriate discretization parameters or how to mitigate the potential information loss.

2. While the bounds are theoretically sound, their practical utility in guiding data collection and model selection needs further empirical validation. The paper does not provide clear guidelines on how to interpret the bounds in practice, and how the magnitude of the bounds relates to the actual benefits of using multimodal models. For example, it is unclear what range of values for the lower and upper bounds would indicate a strong synergy between modalities, and what range would suggest that a unimodal approach is sufficient. The paper also lacks a systematic evaluation of how the bounds perform across different datasets and tasks.

### Suggestions

The paper should provide a more detailed discussion on the practical implications of the proposed bounds. Specifically, the authors should investigate the relationship between the magnitude of the lower and upper bounds and the actual performance gains achieved by multimodal models. This could involve conducting experiments on a variety of datasets with different characteristics and analyzing how the bounds correlate with the improvement of multimodal models over unimodal baselines. For instance, the authors could explore whether a larger lower bound consistently translates to a greater performance boost from multimodal learning. Furthermore, the paper should provide clear guidelines on how to interpret the bounds in practice. This could include defining ranges of values for the lower and upper bounds that indicate different levels of synergy between modalities, and providing recommendations on how to use these ranges to guide data collection and model selection. For example, the authors could suggest that if the lower bound is above a certain threshold, it is likely that a multimodal approach will be beneficial, and if the upper bound is below a certain threshold, a unimodal approach might be sufficient. 

To address the limitations of discretization, the authors should explore alternative methods for handling continuous and high-dimensional data. This could involve investigating the use of kernel density estimation or other non-parametric methods for estimating the probability distributions of the modalities. The authors should also provide a more detailed analysis of the impact of different discretization methods on the accuracy of the bounds. This could involve comparing the performance of different discretization techniques, such as uniform discretization, k-means discretization, and decision tree-based discretization, and analyzing how the choice of discretization method affects the tightness of the bounds. The authors should also discuss the computational complexity of the proposed approach, especially when dealing with high-dimensional data, and provide recommendations on how to reduce the computational cost. For example, the authors could explore the use of dimensionality reduction techniques or approximation algorithms to speed up the computation of the bounds.

Finally, the paper should include a more comprehensive empirical evaluation of the proposed bounds. This could involve conducting experiments on a wider range of datasets and tasks, and comparing the performance of the proposed approach with existing methods for quantifying multimodal interactions. The authors should also investigate the robustness of the bounds to different types of noise and perturbations in the data. This could involve adding noise to the input data and analyzing how the bounds change. The authors should also provide a more detailed analysis of the limitations of the proposed approach and discuss potential directions for future research. For example, the authors could discuss the challenges of applying the proposed approach to more complex multimodal scenarios, such as those involving more than two modalities or those with complex temporal dependencies.

### Questions

1. How does the choice of discretization method affect the accuracy of the bounds, and are there recommended approaches for discretizing high-dimensional data?

2. What are the computational requirements for calculating the bounds, and how do they scale with the size of the dataset and the dimensionality of the modalities?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
