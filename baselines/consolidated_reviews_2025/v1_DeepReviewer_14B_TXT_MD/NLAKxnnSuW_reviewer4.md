### Summary

This paper proposes a memory-efficient framework for 4DGS. The authors streamline the color attribute by decomposing it into a per-Gaussian direct color component with only 3 parameters and a shared lightweight alternating current color predictor. The authors introduce an entropy-constrained Gaussian deformation technique that uses a deformation field to expand the action range of each Gaussian and integrates an opacity-based entropy loss to limit the number of Gaussians.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method achieves a significant reduction in storage requirements while maintaining comparable rendering speeds and scene representation quality.
2. The proposed method is evaluated on multiple datasets and compared with various competitive baselines, demonstrating its effectiveness and generalizability.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method relies on several hyperparameters, such as the trade-off parameters in the loss function and the threshold parameters for densification and pruning. The sensitivity of the method to these hyperparameters is not thoroughly explored, and the chosen values may not be optimal for all datasets or scenes. Specifically, the impact of varying the weight of the entropy loss on the final rendering quality and the number of Gaussians used is unclear. Furthermore, the threshold parameters for densification and pruning, which control the trade-off between rendering quality and the number of Gaussians, are not analyzed in detail, making it difficult to assess the robustness of the method.
2. The proposed method introduces additional computational overhead due to the deformation field and entropy loss. The computational cost of these components, particularly the deformation field, is not analyzed in detail. The paper does not provide a breakdown of the time spent on different parts of the algorithm, making it difficult to assess the impact of the deformation field and entropy loss on the overall training and rendering time. This lack of detailed analysis makes it hard to understand the practical implications of the proposed method in terms of computational resources.

### Suggestions

The paper should include a more detailed analysis of the hyperparameter sensitivity. Specifically, the authors should conduct experiments to evaluate the impact of varying the weight of the entropy loss on the rendering quality and the number of Gaussians. This could involve plotting the performance of the method across a range of entropy loss weights and analyzing the trade-offs between rendering quality and the number of Gaussians. Similarly, the authors should analyze the impact of the densification and pruning thresholds on the final results. This could involve varying these thresholds and evaluating the resulting rendering quality and the number of Gaussians. The analysis should also include a discussion of how these hyperparameters should be chosen for different datasets or scenes. This would provide a more complete understanding of the method's behavior and its robustness to different parameter settings.

To address the concern about computational overhead, the authors should provide a detailed breakdown of the computational cost of each component of the proposed method. This should include the time spent on the deformation field, the entropy loss, and the other parts of the algorithm. The authors should also compare the computational cost of the proposed method with that of the baseline 4DGS. This analysis should be conducted for both training and rendering. The authors should also discuss the scalability of the method in terms of computational resources. This would provide a more complete understanding of the practical implications of the proposed method and its suitability for different applications. Furthermore, the authors should consider providing a more detailed analysis of the memory footprint of the deformation field and the entropy loss, as these could also contribute to the overall computational overhead.

Finally, the authors should provide a more detailed explanation of the deformation field and its impact on the Gaussian primitives. The paper should include a visualization of the deformation field and its effect on the Gaussian primitives. This would help to understand how the deformation field expands the action range of each Gaussian and how it contributes to the reduction in the number of Gaussians. The authors should also discuss the limitations of the deformation field and its potential impact on the rendering quality. This would provide a more complete understanding of the proposed method and its limitations.

### Questions

1. How does the proposed method handle scenes with complex motion or transient content? Are there any limitations or challenges in representing such scenes?
2. How does the proposed method compare to other memory-efficient 4DGS methods in terms of storage reduction and rendering quality?
3. Can the proposed method be extended to other types of dynamic scene representations, such as neural radiance fields or implicit functions?

### Rating

6

### Confidence

4

**********
