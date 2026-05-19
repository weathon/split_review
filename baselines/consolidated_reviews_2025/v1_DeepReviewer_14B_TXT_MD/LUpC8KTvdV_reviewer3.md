### Summary

This paper introduces a novel self-supervised learning approach for transformer architecture search. The proposed method, termed MaskTAS, leverages masked image modeling (MIM) to avoid the expensive costs of data labeling required by supervised learning methods. MaskTAS employs a teacher-student architecture where the teacher network provides strong supervision for efficient training of the student branch. The paper also introduces an unsupervised evaluation metric for the evolutionary search algorithm, which rates candidate architectures based on their consistency with the teacher network. The experimental results demonstrate that the searched architectures achieve state-of-the-art accuracy on various datasets without using manual labels.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper introduces a novel self-supervised learning approach for transformer architecture search, which eliminates the need for expensive data labeling.
- The proposed MaskTAS framework employs a teacher-student architecture that enables efficient training of transformer supernets.
- The paper designs a novel unsupervised evaluation metric for the evolutionary search algorithm, which rates candidate architectures based on their consistency with the teacher network.
- The experimental results demonstrate that the searched architectures achieve state-of-the-art accuracy on various datasets without using manual labels.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the proposed method compared to existing approaches.
- The paper does not discuss the potential limitations of the proposed method, such as its sensitivity to hyperparameter settings or the choice of teacher network.

### Suggestions

The paper should include a more thorough analysis of the computational demands of MaskTAS. Specifically, the authors should provide a breakdown of the FLOPs and memory usage for each stage of the method, including the teacher pre-training, student training, and architecture search phases. This analysis should be compared against existing supervised and self-supervised NAS methods to provide a clear understanding of the computational trade-offs. Furthermore, the authors should investigate the scalability of MaskTAS with respect to the size of the search space and the number of candidate architectures. This would help to determine the practical limitations of the approach and identify potential bottlenecks.

To address the sensitivity of the method, the authors should conduct a more comprehensive hyperparameter study. This should include a systematic exploration of the impact of different masking ratios, learning rates, and batch sizes on the performance of the searched architectures. The authors should also investigate the effect of different teacher network architectures and pre-training strategies on the final performance. It would be beneficial to provide a sensitivity analysis that shows how the performance of MaskTAS varies with different hyperparameter settings. This analysis should also include a discussion of the optimal hyperparameter ranges for different datasets and tasks. The authors should also consider using techniques like Bayesian optimization to automatically tune the hyperparameters of the method.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. This should include a discussion of the potential challenges in applying MaskTAS to different types of data, such as medical images or satellite imagery. The authors should also discuss the potential impact of the choice of the teacher network on the performance of the searched architectures. It would be beneficial to provide a theoretical analysis of the convergence properties of the proposed method and to discuss the potential for instability during the training process. The authors should also consider the potential for bias in the searched architectures and discuss how this bias can be mitigated.

### Questions

- How does the computational cost of MaskTAS compare to existing supervised and self-supervised NAS methods?
- How sensitive is the performance of the searched architectures to the choice of hyperparameters, such as the masking ratio and the learning rate?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
