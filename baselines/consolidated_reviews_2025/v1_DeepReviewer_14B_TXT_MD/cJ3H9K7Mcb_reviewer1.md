### Summary

This paper studies the robustness of models under different degrees of distribution shifts. It finds that models that are robust to a moderate degree of distribution shift are not robust to a higher degree of distribution shift. Also, models that are robust to a higher degree of distribution shift are not robust to a lower degree of distribution shift. The paper also studies the robustness of CLIP under different degrees of distribution shifts and finds that CLIP is not robust to even mild degrees of distribution shifts on downstream tasks.

### Soundness

2 fair

### Presentation

3 good

### Contribution

1 poor

### Strengths

1. The paper is easy to read. The claims made in the paper are clear.
2. The paper presents results on several datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The observations made in the paper are obvious. It is expected that a model trained on a particular distribution is not robust to a higher degree of distribution shift. Also, a model trained on a higher degree of distribution shift may not be robust to a lower degree of distribution shift. Thus, the contribution of the paper is minimal.
2. The paper does not provide any insights into why this happens. It does not provide any analysis of the models to justify the claims.
3. The paper does not propose any solution to the problem.
4. The experiments in the paper are done on simple datasets such as MNIST and CIFAR10. Thus, the claims in the paper may not hold for more complex datasets such as ImageNet.

### Suggestions

The paper's central claim, that models robust to moderate distribution shifts are not necessarily robust to higher shifts, and vice-versa, lacks sufficient novelty to warrant publication. While the authors explore this concept across different shift degrees, the core idea is not surprising. The field already understands that robustness is not a monolithic property and that models can exhibit varying degrees of sensitivity to different types and magnitudes of distribution shifts. The paper would be significantly strengthened by a more in-depth investigation into the underlying mechanisms causing this brittleness. For example, analyzing the feature representations learned by the models at different shift levels could provide valuable insights. Techniques like feature visualization or probing could reveal how the models' internal representations change as the degree of shift increases, and why this leads to a breakdown in robustness. Furthermore, the paper should explore the relationship between the model's architecture and its robustness properties. Are certain architectures more prone to this kind of brittleness than others? This would add a layer of technical depth that is currently missing.

To address the lack of analytical insights, the authors should consider incorporating techniques from the field of interpretability. For instance, they could investigate whether the models rely on spurious correlations that are only valid within a narrow range of shift degrees. This could involve analyzing the model's attention maps or feature importance scores to identify which parts of the input are most influential for prediction at different shift levels. Furthermore, the paper should explore the role of the training data in the observed brittleness. Are there specific characteristics of the training data that make the models more susceptible to this kind of behavior? For example, the authors could experiment with different training data distributions and analyze how this affects the models' robustness properties. This would provide a more nuanced understanding of the problem and move beyond the simple observation that robustness is not transferable across shift degrees. The paper should also consider the impact of different training techniques, such as data augmentation or adversarial training, on the observed brittleness.

Finally, while the authors acknowledge the limitation of using relatively simple datasets, the lack of experiments on more complex datasets like ImageNet significantly limits the generalizability of their findings. The authors should consider including experiments on more challenging datasets to demonstrate that their observations are not specific to MNIST and CIFAR10. Furthermore, the paper should explore the practical implications of their findings. How does the observed brittleness affect the deployment of machine learning models in real-world applications? What steps can practitioners take to mitigate this problem? The paper should also consider the computational cost of the proposed approach. Are there more efficient ways to evaluate the robustness of models across different shift degrees? Addressing these practical concerns would make the paper more relevant and impactful.

### Questions

1. Can the observations made in the paper be used to propose a new metric for robustness? Say, robustness at degree d can be defined as the worst performance between degree d-1 and d+1. If yes, then why is this metric better than the ones used currently?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
