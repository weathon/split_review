### Summary

This paper proposes a federated learning setting called modality-collaborated federated learning (MCFL), where clients only possess data of a single modality. The paper also proposes FedCola, a framework based on modality-agnostic transformers, to address the challenges of model heterogeneity and modality gaps in MCFL.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The proposed MCFL setting is interesting and practical. 
2. The paper is well-organized and easy to follow. 
3. The proposed FedCola framework is simple and effective.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks novelty in terms of the proposed framework. The proposed FedCola framework is a combination of existing techniques, such as attention sharing and modality compensation, and does not introduce any new concepts or methods. The modality compensation strategy, while presented as novel, appears to be a heuristic approach to address the issue of varying numbers of trained parameters across modalities, and does not offer a principled solution to the underlying problem of modality gaps.
2. The paper lacks theoretical analysis. While the paper presents empirical results, it does not provide any theoretical guarantees or insights into the convergence or optimality of the proposed method. This makes it difficult to assess the robustness and reliability of the approach, especially in complex multi-modal scenarios.
3. The paper lacks a comprehensive evaluation of the proposed method. The experiments are limited to two modalities (vision and language) and do not explore the performance of the method in more complex scenarios with a larger number of modalities or more diverse data types. The paper also does not compare the proposed method with other state-of-the-art federated learning algorithms, making it difficult to assess its relative performance.

### Suggestions

The paper should explore more innovative approaches to address the challenges of model heterogeneity and modality gaps in the proposed MCFL setting. Instead of relying on a combination of existing techniques, the authors should investigate novel methods that can effectively leverage cross-modal knowledge and adapt to diverse model architectures. For example, they could explore techniques such as meta-learning or adversarial training to enable clients to learn shared representations across modalities, even when the models they use are not identical. Furthermore, the modality compensation strategy should be refined to provide a more principled approach to handling the issue of varying numbers of trained parameters. This could involve developing a more sophisticated method for aligning the parameters of different modalities, rather than relying on a simple copy-paste approach.

To address the lack of theoretical analysis, the authors should consider incorporating theoretical frameworks that can provide insights into the convergence and optimality of the proposed method. This could involve analyzing the properties of the modality-agnostic transformer architecture and deriving theoretical bounds on the performance of the method. Furthermore, the authors should consider conducting more extensive experiments to evaluate the performance of the proposed method in a wider range of scenarios. This should include experiments with more complex data types, a larger number of modalities, and more diverse model architectures. The experiments should also include comparisons with other state-of-the-art federated learning algorithms to provide a more comprehensive evaluation of the proposed method.

Finally, the paper should provide a more detailed discussion of the limitations of the proposed method and potential directions for future research. This should include a discussion of the assumptions made by the method and the conditions under which it is expected to perform well. The authors should also consider exploring the robustness of the method to different types of data heterogeneity and model heterogeneity. This would help to provide a more complete understanding of the strengths and weaknesses of the proposed approach and guide future research in this area.

### Questions

1. How does the proposed method handle the issue of model heterogeneity when clients use different model architectures? 
2. What are the limitations of the proposed modality compensation strategy, and how can they be addressed?

### Rating

3

### Confidence

4

**********
