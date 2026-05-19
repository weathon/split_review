### Summary

This paper proposes a method for unpaired image-to-image translation between pinhole and panoramic images. The authors propose a two-stage training scheme, a transformer-based translator, and a distortion-free discriminator to handle the large domain gap between pinhole and panoramic images. The authors also propose to inject spherical positional embedding into the translator and to use the deformable convolution in the encoder to improve the quality further. The authors show qualitative and quantitative results that outperform existing I2I methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to understand.
2. The proposed method is technically sound.
3. The results are promising and outperform existing I2I methods.

### Weaknesses

#### Some Related Works


#### comment

1. The authors do not provide information about the model size and inference speed. This information is crucial for understanding the practicality of the proposed method. The lack of details regarding the number of parameters, FLOPs, and actual inference time on a standard hardware setup makes it difficult to assess the computational cost and real-world applicability of the method, especially when compared to other I2I techniques.

2. The authors do not discuss the limitations of the proposed method. A thorough discussion of the method's shortcomings is essential for a balanced evaluation. This should include scenarios where the method might fail or produce artifacts, such as extreme geometric distortions, occlusions, or unusual lighting conditions. Without this, the reader lacks a complete understanding of the method's robustness.

3. The authors do not provide the implementation details of the proposed method. The absence of specific architectural details, such as the number of layers in the transformer, the kernel sizes in the deformable convolution, and the activation functions used, hinders reproducibility. This lack of detail makes it challenging for other researchers to replicate the results and build upon this work.

### Suggestions

The authors should provide a detailed analysis of the computational cost of their method, including the model size (number of parameters), FLOPs, and inference time on a standard hardware setup (e.g., a specific GPU model). This analysis should also compare these metrics with existing I2I methods to provide a clear understanding of the trade-offs between performance and computational efficiency. Furthermore, it would be beneficial to include a discussion on how the method's performance scales with different input resolutions and hardware configurations. This would allow readers to better assess the practical applicability of the proposed method in various real-world scenarios.

In addition to the computational analysis, the authors should include a comprehensive discussion of the limitations of their method. This discussion should go beyond simply stating what the method does well and should instead focus on identifying specific scenarios where the method might fail or produce suboptimal results. For example, the authors could investigate the method's performance on images with extreme viewpoints, significant occlusions, or unusual lighting conditions. They could also analyze the types of artifacts that the method might produce and discuss potential strategies for mitigating these issues. This would provide a more balanced and realistic assessment of the method's capabilities and limitations.

Finally, the authors should provide a detailed description of the implementation details of their method. This should include specific information about the architecture of the transformer, the deformable convolution, and the training procedure. For example, the authors should specify the number of layers in the transformer, the kernel sizes and padding used in the deformable convolution, and the activation functions used in each layer. They should also provide details about the training data, the loss functions used, and the optimization algorithm. This level of detail is essential for ensuring the reproducibility of the results and for allowing other researchers to build upon this work. The authors should also consider releasing their code to further enhance reproducibility and facilitate future research.

### Questions

1. The authors should provide the model size and inference speed of the proposed method.
2. The authors should discuss the limitations of the proposed method.
3. The authors should provide the implementation details of the proposed method.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
