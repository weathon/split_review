### Summary

This paper introduces Ablated Learned Temperature Energy (AbeT), a novel method for out-of-distribution (OOD) detection that combines learned temperature scaling and an energy score. AbeT addresses limitations in existing OOD detection methods by effectively distinguishing between in-distribution (ID) and OOD samples, even when OOD samples are not explicitly encountered during training. The method is evaluated on classification, semantic segmentation, and object detection tasks, demonstrating significant improvements in OOD detection performance.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- AbeT is a simple yet effective modification to existing OOD detection methods, requiring minimal changes to the training process.
- The paper provides a clear and well-structured explanation of the proposed method, making it accessible and understandable.
- The experimental results demonstrate the effectiveness of AbeT across multiple tasks and datasets, showcasing its potential for real-world applications.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a thorough comparison with other state-of-the-art OOD detection methods, particularly those that are more recent and have demonstrated superior performance. This makes it difficult to assess the true novelty and effectiveness of AbeT.
- The evaluation is limited to a few datasets and tasks, which may not fully capture the generalizability of the proposed method. A broader range of datasets and tasks would strengthen the claims made in the paper.
- The paper does not provide a detailed analysis of the computational cost of AbeT, which is an important factor for practical applications. A comparison of the computational overhead with other methods would be beneficial.

### Suggestions

The paper would significantly benefit from a more comprehensive comparison with existing state-of-the-art OOD detection methods. Specifically, the authors should include a comparison with methods that have demonstrated strong performance on similar tasks and datasets. This should include a detailed analysis of the performance differences, highlighting the specific scenarios where AbeT excels or falls short compared to these methods. For example, a comparison with methods that utilize adversarial training or more sophisticated feature representations would provide a more complete picture of AbeT's capabilities. Furthermore, the comparison should not only focus on overall performance metrics but also on the behavior of the methods under different types of distributional shifts. This would help to understand the robustness of AbeT in various real-world scenarios. The authors should also consider including a discussion of the limitations of AbeT in comparison to these methods, which would provide a more balanced view of the proposed approach.

To strengthen the claims regarding the generalizability of AbeT, the authors should expand the evaluation to include a wider range of datasets and tasks. This should include datasets that are more diverse in terms of domain and complexity, as well as tasks that are more challenging and realistic. For example, the authors could consider evaluating AbeT on datasets with different types of image corruptions or on tasks that require more complex reasoning. This would help to demonstrate the robustness of AbeT across different scenarios. Additionally, the authors should consider evaluating AbeT on tasks that are more closely aligned with real-world applications, such as anomaly detection or fraud detection. This would provide a more practical assessment of the method's potential impact. The evaluation should also include a detailed analysis of the performance of AbeT under different hyperparameter settings, which would help to understand the sensitivity of the method to different configurations.

Finally, the paper should include a detailed analysis of the computational cost of AbeT, including a comparison with other methods. This should include a breakdown of the computational overhead associated with each component of the method, such as the learned temperature scaling and the energy score. The authors should also discuss the memory requirements of AbeT and how they compare to other methods. This analysis should be conducted on a range of hardware platforms to provide a more comprehensive understanding of the computational cost. Furthermore, the authors should discuss the scalability of AbeT to larger datasets and models, which is an important factor for practical applications. This analysis should include a discussion of the potential bottlenecks and how they can be addressed. A thorough analysis of the computational cost would help to assess the practical feasibility of AbeT and its suitability for real-world applications.

### Questions

- How does AbeT compare to other state-of-the-art OOD detection methods in terms of performance and computational cost?
- Can AbeT be effectively applied to other tasks, such as anomaly detection or fraud detection, and what modifications might be necessary?
- What are the limitations of AbeT, and how can these limitations be addressed in future work?

### Rating

3

### Confidence

4

**********
