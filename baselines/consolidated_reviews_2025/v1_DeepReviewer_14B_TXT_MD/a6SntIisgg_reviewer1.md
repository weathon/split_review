### Summary

This paper presents a novel approach to unsupervised domain adaptation (UDA) for time series data, addressing the challenge of extracting and aligning both global and local features. The authors propose the Local-Global Representation Alignment (LOGRA) framework, which utilizes a two-branch encoder to capture both global and local representations. The framework introduces a fusion module to integrate these representations, enhancing domain-invariant feature alignment from multiple perspectives. Experimental results on four time series datasets demonstrate that LOGRA outperforms strong baselines by up to 12.52%, highlighting its effectiveness in time series UDA tasks.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

1. The LOGRA framework is a novel approach that combines both global and local feature extraction, which is a significant advancement in the field of time series UDA.
2. The paper provides extensive experimental results, demonstrating the effectiveness of the LOGRA framework across various datasets.
3. The authors have clearly articulated the problem and their methodology, making the paper accessible to readers with a background in the field.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from more detailed explanations of the DTW alignment loss and its impact on the overall performance. Specifically, the paper lacks a clear explanation of how the DTW alignment loss is calculated and how it contributes to the domain adaptation process. The interaction between the DTW loss and other loss components, such as the classification loss and adversarial loss, is not sufficiently elaborated. It is unclear how the DTW loss helps in aligning the local and global features across domains, and what specific advantages it offers over other distance metrics.
2. The computational complexity and parameter count of the LOGRA framework are higher than some of the baselines, which might be a concern for practical applications. The paper does not provide a detailed analysis of the computational overhead introduced by the local and global feature extraction branches and the fusion module. The increased parameter count could lead to longer training times and higher memory requirements, which may limit the applicability of the proposed method in resource-constrained environments. A more thorough discussion of the trade-offs between performance gains and computational costs is needed.
3. The paper does not extensively discuss the potential limitations of the LOGRA framework or scenarios where it might not perform optimally. The paper lacks a discussion of the assumptions made by the framework and the conditions under which these assumptions might fail. For example, the paper does not address how the performance of the framework might be affected by noisy time series data or by significant differences in the temporal dynamics between the source and target domains. It is also unclear how the framework would perform on time series data with varying lengths or sampling rates.

### Suggestions

To enhance the paper, the authors should provide a more detailed explanation of the DTW alignment loss, including the specific mathematical formulation and its role in the overall objective function. A clear explanation of how the DTW loss is integrated with other loss components, such as the classification loss and adversarial loss, is crucial. The authors should also provide a more detailed analysis of the impact of the DTW loss on the learned representations, perhaps through visualization or ablation studies. This would help readers understand the specific contribution of the DTW loss to the domain adaptation process and how it helps in aligning local and global features across domains. Furthermore, the authors should discuss the limitations of using DTW, such as its sensitivity to time warping and its computational cost, and how these limitations might affect the performance of the framework.

Regarding the computational complexity, the authors should provide a more detailed analysis of the computational overhead introduced by the LOGRA framework. This analysis should include a breakdown of the computational cost of each component, such as the local and global feature extraction branches and the fusion module. The authors should also compare the computational cost of the LOGRA framework with that of the baselines, not only in terms of parameter count but also in terms of training time and memory requirements. A discussion of the trade-offs between performance gains and computational costs is essential for practical applications. The authors could also explore techniques to reduce the computational cost of the framework, such as model compression or pruning, to make it more suitable for resource-constrained environments. This would make the framework more practical and accessible to a wider range of users.

Finally, the authors should discuss the potential limitations of the LOGRA framework and scenarios where it might not perform optimally. This discussion should include the assumptions made by the framework and the conditions under which these assumptions might fail. For example, the authors should discuss how the performance of the framework might be affected by noisy time series data, significant differences in the temporal dynamics between the source and target domains, or time series data with varying lengths or sampling rates. The authors should also consider the impact of the choice of hyperparameters on the performance of the framework and provide guidelines for selecting appropriate values. A thorough discussion of these limitations would provide a more balanced view of the framework and help readers understand its applicability and limitations.

### Questions

1. Could the authors provide more insights into the choice of hyperparameters for the LOGRA framework and how they might affect the performance?
2. How does the LOGRA framework handle noisy time series data, and are there any preprocessing steps recommended?
3. Can the authors discuss the potential for extending the LOGRA framework to other types of sequential data beyond time series?

### Rating

5

### Confidence

4

**********
