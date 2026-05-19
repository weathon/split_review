### Summary

This paper proposes a temperature scaling function for contrastive learning. The proposed method is based on the observation that the tolerance of hard negative samples is often overestimated in contrastive learning. The proposed method is evaluated on several datasets and shows performance improvements.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to implement.
- The experiments are conducted on multiple datasets.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is motivated by the observation that the tolerance of hard negative samples is often overestimated in contrastive learning. However, the proposed method does not seem to directly address this issue. The proposed method is motivated by the observation that the tolerance of hard negative samples is often overestimated in contrastive learning. However, the proposed method does not seem to directly address this issue. The proposed method is motivated by the observation that the tolerance of hard negative samples is often overestimated in contrastive learning. However, the proposed method does not seem to directly address this issue. The proposed method is motivated by the observation that the tolerance of hard negative samples is often overestimated in contrastive learning. However, the proposed method does not seem to directly address this issue.

### Suggestions

The core issue lies in the lack of a clear, direct link between the proposed temperature scaling method and the mitigation of overestimated hard negative sample tolerance. While the method adjusts the temperature based on cosine similarity, it's not immediately obvious how this adjustment directly addresses the problem of hard negatives being treated as positives. A more detailed analysis is needed to show how the proposed method alters the loss landscape in a way that specifically reduces the influence of hard negatives. For instance, the authors could analyze the gradient of the loss function with respect to the embeddings of hard negative samples under different temperature settings. This would provide a more concrete understanding of how the proposed method affects the learning dynamics of hard negatives. Furthermore, visualizing the feature space and the decision boundaries before and after applying the proposed method could offer valuable insights into the method's impact on the distribution of samples and the separation of different classes.

To strengthen the paper, the authors should provide a more rigorous theoretical justification for their method. This could involve deriving the proposed temperature scaling function from first principles, or demonstrating its equivalence to a known optimization technique. The current explanation relies heavily on empirical observations, which is not sufficient to establish the method's theoretical soundness. Additionally, the authors should explore the sensitivity of their method to different choices of the temperature scaling function. It is possible that other temperature scaling functions could achieve similar or even better performance. A comparative analysis of different scaling functions would provide a more comprehensive understanding of the proposed method's strengths and limitations. The authors should also consider the computational overhead of their method, especially when dealing with large datasets. If the method introduces significant computational costs, it may not be practical for real-world applications.

Finally, the experimental evaluation should be expanded to include a wider range of datasets and model architectures. The current experiments are limited to a few specific datasets and a single model architecture. This makes it difficult to assess the generalizability of the proposed method. The authors should also consider comparing their method to other state-of-the-art contrastive learning techniques. This would provide a more comprehensive evaluation of the method's performance and its advantages over existing approaches. Furthermore, the authors should provide a more detailed analysis of the experimental results, including statistical significance tests and error bars. This would help to ensure the robustness and reliability of the reported performance improvements.

### Questions

- How does the proposed method affect the feature space distribution?
- How does the proposed method alleviate the alignment-failure dilemma?

### Rating

5

### Confidence

3

**********
