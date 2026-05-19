### Summary

This paper proposes AdaMerging, a novel approach for multi-task learning (MTL) that leverages entropy minimization to adaptively learn task merging coefficients without requiring original training data. By utilizing unlabeled test samples, AdaMerging optimizes coefficients to minimize prediction loss, achieving improved performance, generalization, and robustness compared to existing task vector-based methods. The method is evaluated across eight tasks using ViT-B/32 and ViT-L/14 architectures, demonstrating significant gains over state-of-the-art techniques.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The experiments are comprehensive and well-organized.

### Weaknesses

#### Some Related Works


#### comment

1. The motivation is unclear. The authors claim that AdaMerging can operate without original training data, but this claim is misleading. The method requires labeled test samples from each task to compute task-specific entropy, which contradicts the claim of not needing original training data. The use of labeled test samples, even if unlabeled, still constitutes a form of data dependency and limits the applicability of the method in scenarios where such data is unavailable or expensive to obtain. Furthermore, the paper does not adequately address the potential impact of the size and quality of these labeled test samples on the performance of AdaMerging.
2. The novelty is limited. The proposed method is essentially a fine-tuning method, which adjusts the merging coefficients of the task vectors. The core idea of using task vectors for multi-task learning is not new, and the proposed method does not introduce a fundamentally novel approach to multi-task learning. The method essentially performs a weighted average of task vectors, where the weights are learned through entropy minimization. This is a relatively straightforward application of existing techniques, and the paper does not provide a strong justification for why this specific approach is superior to other possible methods for learning task merging coefficients.

### Suggestions

The authors should clarify the claim regarding the use of original training data. The current description is inaccurate, as the method relies on labeled test samples from each task to compute task-specific entropy. A more precise description should acknowledge that while the method does not require retraining on the original training data, it does require labeled test samples, which may not always be available. The authors should also discuss the implications of the size and quality of these labeled test samples on the performance of AdaMerging. For example, how does the performance of the method vary with the number of labeled test samples available for each task? How does the quality of these labeled test samples affect the learned merging coefficients? A sensitivity analysis of these factors would be beneficial.

To address the limited novelty, the authors should provide a more in-depth analysis of the proposed method and compare it to other existing approaches for learning task merging coefficients. Specifically, they should discuss the advantages and disadvantages of using entropy minimization as the optimization objective compared to other potential objectives. For example, how does the performance of AdaMerging compare to methods that use gradient-based optimization or other forms of regularization? The authors should also explore alternative approaches for learning task merging coefficients, such as using a meta-learning framework or a reinforcement learning approach. A more thorough comparison with existing methods would help to better position the proposed method within the existing literature and highlight its unique contributions.

Finally, the authors should provide a more detailed explanation of the experimental setup and the evaluation metrics used. For example, how were the labeled test samples selected for each task? What were the specific hyperparameters used for the entropy minimization process? How were the merging coefficients initialized? A more detailed description of the experimental setup would allow for a more thorough evaluation of the proposed method and facilitate reproducibility. The authors should also consider including additional experiments to further validate the robustness and generalizability of the proposed method. For example, they could evaluate the performance of AdaMerging on a wider range of tasks and datasets, or they could investigate the sensitivity of the method to different choices of task vectors.

### Questions

Please see the weakness.

### Rating

5

### Confidence

4

**********
