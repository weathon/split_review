### Summary

This paper proposes a method for zero-shot quantization (ZSQ) that leverages proxy data instead of original data. The authors introduce a selection method based on batch normalization statistics (BNS) to choose the most suitable proxy data. The experimental results demonstrate that using proxy data can enhance the performance of existing ZSQ methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough analysis of the impact of different proxy data on ZSQ performance.
3. The proposed method is simple and effective.

### Weaknesses

#### Some Related Works


#### comment

1. The motivation behind using proxy data in ZSQ is not clearly explained. The authors should provide a more detailed explanation of why proxy data can be a better alternative to original data in ZSQ, especially given the potential domain gap between proxy and original data. Specifically, the paper lacks a rigorous justification for why a proxy dataset, which is likely to be significantly different from the original data distribution, would lead to improved quantization performance. The argument that proxy data captures 'latent properties' is not sufficiently substantiated with concrete examples or theoretical analysis. It is unclear how these 'latent properties' translate to better quantization, and the paper does not explore the potential negative impacts of this domain shift on the quantized model's accuracy.
2. The selection method for proxy data is based on batch normalization statistics (BNS). However, the authors do not provide a detailed explanation of why BNS is effective for proxy data selection. It is unclear why BNS, which is a per-layer statistic, would be a reliable indicator of the suitability of a proxy dataset for a given task. The paper should delve deeper into the relationship between BNS and the quality of the proxy data, and provide a more thorough analysis of the underlying mechanisms that make BNS a suitable selection metric. For example, it is not clear if BNS captures the most relevant information for quantization, or if it is simply a proxy for other, more complex measures of data similarity.
3. The paper does not explore the impact of different proxy data selection strategies. The authors only use BNS for proxy data selection, and do not investigate other potential selection methods. This limits the generalizability of the proposed method and makes it difficult to assess the true potential of the approach. The paper should explore alternative selection strategies, such as clustering-based methods or methods based on domain adaptation, to determine if BNS is indeed the optimal choice.

### Suggestions

The paper should provide a more rigorous justification for using proxy data in zero-shot quantization (ZSQ). The authors should explore the theoretical underpinnings of why a proxy dataset, which is likely to be different from the original data distribution, can lead to improved quantization performance. This could involve analyzing the relationship between the proxy data and the original data distributions, and demonstrating how the proxy data captures relevant information for quantization. Furthermore, the authors should investigate the potential negative impacts of the domain gap between proxy and original data, and propose methods to mitigate these negative effects. For example, they could explore techniques to align the feature spaces of the proxy and original data, or use domain adaptation methods to adapt the quantized model to the original data distribution. The paper should also include a more detailed analysis of the impact of different proxy data selection strategies, and explore alternative methods beyond BNS. This could involve comparing BNS with other selection metrics, such as clustering-based methods or methods based on domain adaptation. The authors should also investigate the sensitivity of the proposed method to the choice of proxy data, and provide guidelines for selecting appropriate proxy datasets for different tasks. 

To strengthen the paper, the authors should provide a more detailed explanation of why batch normalization statistics (BNS) are effective for proxy data selection. The paper should delve deeper into the relationship between BNS and the quality of the proxy data, and provide a more thorough analysis of the underlying mechanisms that make BNS a suitable selection metric. For example, the authors could investigate whether BNS captures the most relevant information for quantization, or if it is simply a proxy for other, more complex measures of data similarity. The paper should also explore the limitations of using BNS for proxy data selection, and discuss potential alternative approaches. This could involve analyzing the correlation between BNS and the performance of quantized models, and identifying cases where BNS is not a reliable indicator of proxy data quality. The authors should also provide a more detailed analysis of the computational cost of using BNS for proxy data selection, and compare it with other potential selection methods.

Finally, the paper should include a more comprehensive experimental evaluation of the proposed method. This should include a wider range of datasets and tasks, and a more thorough analysis of the performance of the proposed method under different conditions. The authors should also compare the proposed method with other state-of-the-art ZSQ methods, and provide a detailed analysis of the strengths and weaknesses of each method. The paper should also include a more detailed analysis of the impact of different proxy data selection strategies, and explore alternative methods beyond BNS. This could involve comparing BNS with other selection metrics, such as clustering-based methods or methods based on domain adaptation. The authors should also investigate the sensitivity of the proposed method to the choice of proxy data, and provide guidelines for selecting appropriate proxy datasets for different tasks.

### Questions

1. What is the motivation behind using proxy data in ZSQ? How can we ensure that the proxy data is similar to the original data?
2. Why is batch normalization statistics (BNS) effective for proxy data selection? Is BNS a reliable indicator of the quality of the proxy data?
3. How does the proposed method perform when the proxy data is significantly different from the original data?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
