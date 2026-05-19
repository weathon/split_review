### Summary

This paper proposes a unified framework for understanding the design principles of state-of-the-art watermarking methods in diffusion models. The authors introduce a training-free watermarking approach that embeds watermarks directly into the latent space of diffusion models, minimizing visual quality impact and enhancing robustness against attacks. The proposed method is evaluated on both text-to-image and image-to-image diffusion models, demonstrating superior performance in preserving image quality and robustness against a range of adversarial attacks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper presents a unified framework that identifies and connects the key design principles of state-of-the-art watermarking methods, providing a systematic approach to understanding the strengths and limitations of existing techniques.

2. The proposed method is training-free and operates directly on the latent space of diffusion models, which reduces computational overhead and avoids the need for extensive model retraining.

3. The method demonstrates strong robustness against various adversarial attacks, including geometric transformations, noise addition, and cropping, while maintaining high image quality as measured by FID and CLIP scores.

4. The paper provides extensive experimental results and ablation studies that validate the effectiveness of the proposed method across different diffusion models and attack scenarios.

### Weaknesses

#### Some Related Works


#### comment

1. The paper mentions that the method is training-free and operates directly on the latent space of diffusion models, which reduces computational overhead and avoids the need for extensive model retraining. However, it does not provide a detailed analysis of the computational cost compared to existing watermarking methods. Specifically, the paper lacks a breakdown of the time and memory requirements for watermark embedding and detection, making it difficult to assess the practical advantages of the proposed method. A comparison with methods that require fine-tuning or additional training steps would be beneficial.

2. The paper claims that the proposed method is robust against various adversarial attacks, including geometric transformations, noise addition, and cropping. However, it does not provide a comprehensive evaluation of the method's robustness against more sophisticated attacks, such as adversarial perturbations designed to specifically remove or disrupt the watermark. The evaluation should include a more diverse set of attacks, including those that target the specific watermark embedding strategy, to fully validate the robustness claims.

3. The paper does not discuss the limitations of the proposed method in detail. For example, it is unclear how the method performs under extreme conditions, such as very high levels of noise or aggressive cropping. The paper should also address potential vulnerabilities of the watermarking scheme, such as the possibility of watermark removal through specific post-processing techniques. A thorough discussion of these limitations is crucial for understanding the practical applicability of the method.

### Suggestions

The paper would benefit from a more detailed analysis of the computational cost associated with the proposed watermarking method. The authors should provide a breakdown of the time and memory requirements for both watermark embedding and detection, and compare these metrics with existing watermarking techniques. This analysis should include a discussion of the scalability of the method to larger images and more complex diffusion models. Furthermore, the authors should investigate the impact of different parameter settings on the computational cost, such as the size of the latent space and the complexity of the watermark embedding process. This would provide a more comprehensive understanding of the practical trade-offs associated with the proposed method.

To strengthen the robustness claims, the authors should conduct a more comprehensive evaluation of the method's performance against a wider range of adversarial attacks. This should include not only geometric transformations, noise addition, and cropping, but also more sophisticated attacks designed to specifically target the watermark embedding strategy. For example, the authors could explore attacks that attempt to remove or disrupt the watermark by manipulating the latent space or by introducing adversarial perturbations. The evaluation should also consider the impact of different attack parameters on the watermark's detectability. This would provide a more rigorous assessment of the method's robustness and its ability to withstand real-world adversarial scenarios. The authors should also consider evaluating the method's performance on a wider range of diffusion models and datasets to ensure its generalizability.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method. This should include an analysis of the method's performance under extreme conditions, such as very high levels of noise or aggressive cropping. The authors should also investigate the potential vulnerabilities of the watermarking scheme, such as the possibility of watermark removal through specific post-processing techniques. For example, the authors could explore the use of techniques such as image compression or filtering to remove the watermark and evaluate the method's robustness against such attacks. A detailed discussion of these limitations is crucial for understanding the practical applicability of the method and for identifying areas for future research.

### Questions

1. How does the proposed method compare to existing watermarking techniques in terms of computational efficiency, particularly in terms of encoding and decoding time?

2. Can the proposed framework be extended to other types of generative models beyond diffusion models, such as GANs or VAEs?

3. What are the limitations of the proposed method, and in which scenarios might it fail to detect watermarks or exhibit reduced robustness?

### Rating

6

### Confidence

3

**********
