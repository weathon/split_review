### Summary

This paper proposes a novel method to improve the performance of zero-shot quantization (ZSQ) by using proxy data instead of the original data. The authors introduce a simple and effective method for selecting proxy data based on batch normalization statistics (BNS) and demonstrate that using proxy data can significantly enhance the performance of existing ZSQ methods. The paper also provides a systematic understanding of the role of proxy data in ZSQ and shows that the proposed method can achieve state-of-the-art performance on multiple computer vision datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors clearly explain the motivation, methodology, and experimental results of their proposed method.
2. The paper provides a systematic understanding of the role of proxy data in ZSQ. The authors conduct extensive experiments to demonstrate the effectiveness of their proposed method and show that using proxy data can significantly enhance the performance of existing ZSQ methods.
3. The proposed method is simple and effective. The authors introduce a simple and effective method for selecting proxy data based on batch normalization statistics (BNS) and demonstrate that using proxy data can significantly enhance the performance of existing ZSQ methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear explanation of how the proposed method can be applied to different types of models and datasets. The authors only demonstrate the effectiveness of their method on a few specific models and datasets, and it is unclear how the method can be generalized to other scenarios. Specifically, the paper lacks a discussion on the sensitivity of the BNS-based proxy selection to the architecture of the quantized model. It is not clear if the method would be equally effective for convolutional neural networks (CNNs) and vision transformers (ViTs), or other architectures, given that the batch normalization statistics might behave differently across these models.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method. The authors do not discuss the time and memory requirements of the BNS-based proxy selection process, which could be a concern for large-scale datasets or complex models. The paper should include a breakdown of the computational overhead, including the time taken for calculating BNS and the impact on the overall quantization time. Furthermore, the memory footprint of storing and processing the proxy data should also be considered, especially when dealing with large datasets.
3. The paper does not provide a comparison of the proposed method with other state-of-the-art methods. The authors only compare their method with a few existing ZSQ methods, but it is unclear how the proposed method compares to other recent advances in the field. A more comprehensive comparison with a wider range of state-of-the-art methods is needed to fully evaluate the contribution of the proposed method. The comparison should include methods that use different approaches to zero-shot quantization, such as those based on knowledge distillation or adversarial training.

### Suggestions

The authors should provide a more thorough investigation into the applicability of their method across diverse model architectures. Specifically, they should conduct experiments on a wider range of models, including both CNNs and vision transformers, to demonstrate the generalizability of their approach. It would be beneficial to analyze the behavior of batch normalization statistics (BNS) across different architectures and discuss how the proxy data selection process might need to be adapted for different model types. For example, the authors could explore whether the optimal proxy dataset varies depending on the model architecture, and if so, how this variation can be accounted for in their method. Furthermore, the authors should provide a detailed analysis of the computational cost associated with their method, including the time and memory requirements for BNS calculation and proxy data selection. This analysis should be performed on different datasets and model architectures to provide a comprehensive understanding of the computational overhead. The authors should also discuss potential strategies for reducing the computational cost of their method, such as using more efficient proxy data selection algorithms or approximating BNS calculations. 

To strengthen the paper, the authors should include a more comprehensive comparison with other state-of-the-art zero-shot quantization methods. This comparison should not be limited to a few existing methods but should include a wider range of recent advances in the field. The authors should clearly articulate the advantages and disadvantages of their method compared to these other approaches, highlighting the specific scenarios where their method excels or falls short. This comparison should include methods that use different techniques, such as knowledge distillation, adversarial training, or other data-free quantization strategies. The authors should also discuss the limitations of their method and identify potential areas for future research. This would provide a more complete picture of the current state of the art and the contribution of their work.

Finally, the authors should provide a more detailed explanation of the relationship between the proxy data and the original data. While the paper mentions that the proxy data is used to capture latent properties of the original data, it does not provide a clear definition of what these latent properties are or how they are related to the original data distribution. The authors should provide a more rigorous analysis of the information captured by the proxy data and how it contributes to the performance of the quantized model. This analysis should include a discussion of the potential limitations of using proxy data and the conditions under which it might not be effective. The authors should also explore the possibility of using multiple proxy datasets to capture a more comprehensive representation of the original data.

### Questions

1. How does the proposed method perform on different types of models and datasets? Are there any limitations or challenges in applying the method to other scenarios?
2. What is the computational cost of the proposed method? How does it compare to other state-of-the-art methods in terms of time and memory requirements?
3. How does the proposed method compare to other state-of-the-art methods in terms of performance? Are there any scenarios where the proposed method is not effective?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
