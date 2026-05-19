### Summary

The paper proposes a novel approach to solving the Schrödinger Bridge problem using adversarial learning. The authors formulate the SB problem as a sequence of conditional generation problems, which allows them to leverage advanced discriminators and regularization techniques. The proposed method, called Unpaired Neural Schrödinger Bridge (UNSB), is evaluated on various image translation tasks, demonstrating its scalability and effectiveness compared to existing unpaired image translation methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel formulation of the Schrödinger Bridge problem that allows for adversarial learning, which is a significant advancement in the field.
2. The authors provide a solid theoretical foundation for their method, which adds credibility to their approach.
3. The paper is well-written and easy to follow, making it accessible to a wide audience.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be beneficial to understand how the computational cost scales with the size of the input data and the complexity of the model.
2. The paper does not compare the proposed method with other state-of-the-art methods for image translation. It would be helpful to see how the proposed method performs against other methods in terms of both quantitative and qualitative metrics.
3. The paper does not discuss the limitations of the proposed method. It would be beneficial to understand the scenarios where the proposed method may not perform well or may have limitations.

### Suggestions

The paper should include a more thorough analysis of the computational cost associated with the proposed method. Specifically, the authors should provide a breakdown of the time and memory requirements for each stage of the algorithm, including the adversarial training and the conditional generation steps. This analysis should consider how these costs scale with the size of the input images, the number of training samples, and the complexity of the neural network architectures used. For example, providing a table showing the training time per epoch, memory usage during training, and inference time for different image resolutions and dataset sizes would be very helpful. Furthermore, it would be beneficial to compare the computational cost of the proposed method with that of existing image translation methods, such as GANs and diffusion models, to provide a clear understanding of the trade-offs involved.

In addition to the computational cost, the paper needs a more comprehensive comparison with state-of-the-art image translation methods. The authors should not only compare the quantitative metrics, such as FID and KID scores, but also provide a qualitative comparison by showing visual examples of the generated images. This comparison should include a variety of datasets and image types to demonstrate the robustness of the proposed method. Furthermore, it would be beneficial to analyze the strengths and weaknesses of the proposed method compared to other methods, highlighting the specific scenarios where it excels or falls short. For example, the authors could discuss how their method performs on datasets with complex textures or high levels of noise, and compare it to methods that are specifically designed for these types of datasets. This would provide a more nuanced understanding of the method's capabilities and limitations.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. The authors should discuss the scenarios where the method may not perform well, such as when the source and target distributions are very different or when the data is highly complex. For example, the authors could discuss the limitations of the adversarial training process, such as the potential for mode collapse or the difficulty of training stable GANs. They should also discuss the limitations of the conditional generation step, such as the potential for generating artifacts or inconsistencies in the generated images. Furthermore, the authors should discuss the limitations of the theoretical framework, such as the assumptions made about the underlying distributions and the potential for the method to fail when these assumptions are violated. This would provide a more balanced and realistic assessment of the method's capabilities and limitations.

### Questions

1. How does the proposed method handle the curse of dimensionality in high-dimensional data?
2. How does the proposed method compare with other state-of-the-art methods for image translation in terms of both quantitative and qualitative metrics?
3. What are the limitations of the proposed method, and in which scenarios may it not perform well?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
