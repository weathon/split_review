### Summary

This paper investigates the theoretical foundation of contrastive learning for multimodal data, specifically focusing on the scenario where certain modalities are unpaired. The authors introduce the "Law" of the Unconscious Contrastive Learner, which posits that under specific assumptions, the dot product or negative squared distance between representations of unpaired modalities can recover the correct marginal density ratio. The paper provides a theoretical analysis of this phenomenon and proposes a practical algorithm based on Monte Carlo approximation to estimate the marginal probability ratio between unpaired modalities. The authors validate their theory through experiments on synthetic and real-world datasets, demonstrating the effectiveness of their approach in multimodal alignment tasks.

### Soundness

4

### Presentation

3

### Contribution

4

### Strengths

1. The paper presents a novel theoretical framework for understanding the behavior of contrastive learning in multimodal settings, particularly when dealing with unpaired modalities. The "Law" of the Unconscious Contrastive Learner is a significant contribution to the field.

2. The authors provide a rigorous mathematical analysis of their theory, including proofs for their main results. The use of Bayesian reasoning and the connection to probabilistic graphical models are particularly insightful.

3. The paper introduces a practical algorithm based on Monte Carlo approximation, which can be applied to real-world scenarios where the assumptions of the theory may not perfectly hold. The experiments on synthetic and real-world datasets demonstrate the effectiveness of this approach.

4. The paper explores interesting applications of the theory, such as combining pre-trained models and handling language ambiguity in reinforcement learning. These applications highlight the potential impact of the proposed framework.

### Weaknesses

#### Some Related Works


#### comment

1. The theoretical framework relies on several assumptions, such as conditional independence of modalities given a bridge modality and specific properties of the representation distribution. The paper could benefit from a more detailed discussion of the limitations of these assumptions and when they might not hold in practice. For instance, the conditional independence assumption is quite strong and may not be valid in scenarios where modalities share common underlying factors or have complex interdependencies. The assumption of a specific representation distribution, such as a uniform distribution on the hypersphere, may not accurately reflect the actual distribution of learned representations, which could be more complex and multimodal. The paper should also discuss the implications of these assumptions on the practical applicability of the proposed method.

2. While the paper provides a theoretical analysis of the contrastive learning process, it could benefit from a more detailed discussion of the practical implications of the theory. For example, how can the theoretical analysis guide the design of new contrastive learning algorithms or the selection of appropriate modalities for a given task? The paper should provide concrete examples of how the theoretical findings can be used to improve existing methods or develop new approaches. For instance, how can the derived marginal probability ratio be used to inform the choice of loss functions or the architecture of the encoders?

3. The experiments, while demonstrating the effectiveness of the proposed approach, could be expanded to include more real-world datasets and a wider range of modalities. This would help to further validate the robustness and generalizability of the method. The current experiments primarily focus on synthetic data and a limited set of real-world datasets. It would be beneficial to see results on more diverse and challenging datasets, including those with noisy or incomplete data, to better assess the practical utility of the proposed approach.

### Suggestions

The paper should delve deeper into the limitations of the conditional independence assumption, exploring scenarios where this assumption is likely to be violated and discussing the potential impact on the theoretical results. For example, in many real-world multimodal datasets, modalities are often correlated due to shared underlying factors or complex interdependencies. The paper should discuss how these correlations might affect the accuracy of the estimated marginal probability ratio and propose potential strategies to mitigate these effects. Furthermore, the paper should investigate the sensitivity of the proposed method to violations of the representation distribution assumption. It would be beneficial to explore alternative distributional assumptions and analyze how they affect the theoretical results and the performance of the Monte Carlo approximation algorithm. This could involve conducting experiments with different types of representation distributions and comparing the results with those obtained under the assumed distribution.

To enhance the practical implications of the theoretical analysis, the paper should provide concrete examples of how the derived marginal probability ratio can be used to guide the design of new contrastive learning algorithms. For instance, the paper could discuss how the marginal probability ratio can be used to develop new loss functions that explicitly encourage the alignment of representations across modalities. The paper should also explore how the theoretical analysis can inform the selection of appropriate modalities for a given task. For example, the paper could discuss how the choice of modalities should be guided by the conditional independence assumption and the distribution of representations. Furthermore, the paper should provide a detailed discussion of how the theoretical results can be used to improve existing contrastive learning methods. For example, the paper could discuss how the theoretical analysis can be used to identify the limitations of existing methods and develop new approaches that address these limitations. This could involve proposing modifications to existing loss functions or encoder architectures based on the theoretical insights.

The experimental section should be significantly expanded to include more real-world datasets and a wider range of modalities. The current experiments, while illustrative, do not fully capture the complexity and variability of real-world data. The paper should include experiments on datasets with more complex relationships between modalities, such as datasets with multiple modalities that are not directly related to each other. The paper should also include experiments with a larger number of samples to better assess the robustness of the proposed method. Furthermore, the paper should provide a detailed analysis of the experimental results, including a discussion of the limitations of the proposed method and potential directions for future research. The paper should also compare the performance of the proposed method with existing methods on real-world datasets to demonstrate its practical utility.

### Questions

1. How sensitive are the theoretical results to the assumptions made about the distribution of representations? Are there any alternative distributions that could be considered?

2. Can the theoretical analysis be extended to more than three modalities? If so, how would the marginal probability ratio be computed?

3. How does the proposed Monte Carlo method compare to other methods for combining pre-trained models or handling language ambiguity in reinforcement learning?

### Rating

8

### Confidence

3

**********
