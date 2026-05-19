### Summary

This paper studies the performance of OOD generalization under different degrees of distribution shifts. The authors show that the robustness of models trained on data with different degrees of distribution shifts is brittle and inconsistent. The authors also show that pre-trained models like CLIP are sensitive to novel distribution shifts.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The authors provide a comprehensive set of experiments to study the brittleness of robustness under different degrees of distribution shifts.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear conclusion or actionable insights. The findings are interesting but do not offer a solution or guidance for improving model robustness to distribution shifts.
- The paper lacks a theoretical analysis to explain the observed brittleness of robustness under different degrees of distribution shifts. It would be beneficial to explore potential theoretical frameworks that could shed light on the underlying mechanisms causing this behavior.
- The paper does not investigate the impact of different types of distribution shifts. The authors primarily focus on noise and rotation, but it would be valuable to examine other types of shifts, such as changes in color, style, or object appearance, to understand the generalizability of the findings.
- The paper does not explore the effectiveness of different model architectures in handling distribution shifts. It would be interesting to see if certain architectures are more robust than others to varying degrees of distribution shifts, and if so, what architectural properties contribute to this robustness.

### Suggestions

The paper would significantly benefit from a more in-depth analysis of the observed brittleness in robustness. While the experiments are comprehensive, the lack of a clear conclusion leaves the reader with a sense of incompleteness. The authors should consider framing their findings within a specific context, perhaps by focusing on a particular type of distribution shift or model architecture. For example, they could investigate whether the observed brittleness is more pronounced for models trained with specific regularization techniques or for certain types of data. Furthermore, the authors could explore the relationship between the degree of distribution shift and the model's internal representations. Techniques like activation analysis or feature visualization could provide insights into how models are affected by different shift magnitudes. This would move beyond simply observing the phenomenon and towards a more mechanistic understanding.

To address the lack of theoretical analysis, the authors could explore potential theoretical frameworks that could explain the observed brittleness. For instance, they could investigate whether the phenomenon is related to the model's sensitivity to specific features or the geometry of the loss landscape. It would be valuable to explore if the observed brittleness is a consequence of the model's overfitting to specific shift magnitudes or if it is a more fundamental property of the learning process. The authors could also consider using information-theoretic measures to quantify the amount of information about the distribution shift that is encoded in the model's parameters or activations. This could provide a more principled way to understand the relationship between the degree of shift and the model's performance. Furthermore, the authors could investigate the role of the training data distribution in the observed brittleness. For example, they could explore whether models trained on datasets with a wider range of shift magnitudes exhibit different robustness patterns.

Finally, the paper should expand its investigation to include a wider range of distribution shift types and model architectures. The current study focuses primarily on noise and rotation, but it would be valuable to examine other types of shifts, such as changes in color, style, or object appearance. This would help to determine the generalizability of the findings and identify which types of shifts are most challenging for models. Additionally, the authors should explore the effectiveness of different model architectures in handling distribution shifts. It would be interesting to see if certain architectures are more robust than others to varying degrees of distribution shifts, and if so, what architectural properties contribute to this robustness. For example, the authors could investigate the impact of different normalization techniques, regularization methods, or architectural designs on the model's robustness to distribution shifts. This would provide valuable insights for practitioners seeking to build more robust models.

### Questions

- What are the implications of the findings for real-world applications where distribution shifts are common?
- How can the observed brittleness of robustness be mitigated in practical scenarios?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
