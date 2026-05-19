### Summary

The paper provides a theoretical analysis of contrastive learning for unpaired modalities. The authors show that under certain assumptions, the commonly used heuristic of comparing representations of unpaired modalities via the dot product is theoretically justified. They also introduce a practical algorithm for estimating the marginal probability ratio between unpaired modalities, which can be used for combining pre-trained models or handling language ambiguity in reinforcement learning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a theoretical grounding for a commonly used heuristic in contrastive learning, which is a significant contribution to the field.

2. The authors introduce a practical algorithm based on their theoretical analysis, which has potential applications in combining pre-trained models and handling language ambiguity in reinforcement learning.

3. The paper is well-written and clearly explains the theoretical concepts and their practical implications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper relies on several assumptions, such as the conditional independence of modalities and the distribution of representations. It would be beneficial to discuss the limitations of these assumptions and when they might not hold in practice. For example, the conditional independence assumption may not hold if there are shared underlying factors influencing both modalities, or if the modalities have complex non-linear relationships. The assumption about the distribution of representations, while common, may not be valid for all types of data or contrastive learning objectives, and the paper should discuss the potential impact of deviations from this assumption.

2. The paper could benefit from a more detailed discussion of the practical implications of the theoretical results. For example, how can the theoretical analysis guide the design of new contrastive learning algorithms or the selection of appropriate modalities for a given task? The paper should provide concrete examples of how the theoretical findings can be used to improve existing methods or develop new approaches, rather than just stating that the analysis has practical implications. For instance, how does the derived marginal probability ratio inform the choice of loss functions or the architecture of the encoders?

3. The experiments could be expanded to include more real-world datasets and a wider range of modalities. This would help to demonstrate the robustness and generalizability of the proposed method. The current experiments, while illustrative, do not fully capture the complexity and variability of real-world data. It would be beneficial to see results on datasets with more complex relationships between modalities and with a larger number of samples, to better assess the practical utility of the proposed approach.

### Suggestions

The paper should delve deeper into the limitations of the conditional independence assumption. Specifically, it should discuss scenarios where this assumption is likely to be violated, such as when there are shared latent factors influencing multiple modalities or when the relationship between modalities is non-linear. For example, in a scenario where both image and text describe the same object, the shape of the object could be a shared latent factor influencing both modalities. The paper should also explore the implications of these violations on the theoretical results and discuss potential ways to mitigate these issues, such as by incorporating techniques that explicitly model dependencies between modalities. Furthermore, the paper should provide a more detailed analysis of the sensitivity of the theoretical results to the choice of representation distribution. While the authors mention the use of a Gaussian distribution, they should also discuss the implications of using other distributions and how the theoretical results might change under different distributional assumptions. This would provide a more comprehensive understanding of the theoretical framework and its applicability to different types of data.

To enhance the practical implications of the theoretical results, the paper should provide concrete examples of how the derived marginal probability ratio can be used to guide the design of new contrastive learning algorithms. For instance, the paper could discuss how the marginal probability ratio can be used to develop new loss functions that explicitly encourage the alignment of representations across modalities. The paper should also explore how the theoretical analysis can inform the selection of appropriate modalities for a given task. For example, the paper could discuss how the choice of modalities should be guided by the conditional independence assumption and the distribution of representations. Furthermore, the paper should provide a detailed discussion of how the theoretical results can be used to improve existing contrastive learning methods. For example, the paper could discuss how the theoretical analysis can be used to identify the limitations of existing methods and develop new approaches that address these limitations.

The experimental section should be significantly expanded to include more real-world datasets and a wider range of modalities. The current experiments, while illustrative, do not fully capture the complexity and variability of real-world data. The paper should include experiments on datasets with more complex relationships between modalities, such as datasets with multiple modalities that are not directly related to each other. The paper should also include experiments with a larger number of samples to better assess the robustness of the proposed method. Furthermore, the paper should provide a detailed analysis of the experimental results, including a discussion of the limitations of the proposed method and potential directions for future research. The paper should also compare the performance of the proposed method with existing methods on real-world datasets to demonstrate its practical utility.

### Questions

1. How sensitive are the theoretical results to the assumptions made about the distribution of representations? Are there any alternative distributions that could be considered?

2. Can the theoretical analysis be extended to more than three modalities? If so, how would the marginal probability ratio be computed?

3. How does the proposed Monte Carlo method compare to other methods for combining pre-trained models or handling language ambiguity in reinforcement learning?

### Rating

6

### Confidence

3

**********
