### Summary

The paper presents a controllable image compression model based on VQGAN. The model is trained to compress images at different bitrates by adjusting granularity ratios of the quantized latent codes. The authors claim that the proposed model outperforms recent state-of-the-art methods in terms of rate-distortion performance, flexibility, and compression efficiency.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough literature review, which helps to contextualize their work within the broader field of image compression.

### Weaknesses

#### Some Related Works

[1] DiffBIR: Towards Blind Image Restoration with Generative Diffusion Prior
[2] DiffBIR++: Improved Diffusion Prior for Blind Image Restoration

#### comment

1. The novelty of the proposed method is limited. The main contribution is the granularity-informed encoder, which is based on the existing VQGAN architecture. The probabilistic conditional decoder is also a straightforward extension of existing techniques. The core idea of using quantized latent codes for compression is not new, and the paper does not introduce any significant modifications to the VQGAN framework itself beyond the granularity control mechanism. The method essentially applies a rate control mechanism to a VQGAN-based compression pipeline, which is a relatively minor extension of existing work.

2. The paper lacks a comprehensive comparison with state-of-the-art diffusion-based image compression methods. The authors should include a comparison with methods such as DiffBIR [1] and DiffBIR++ [2], which have demonstrated strong performance in image compression tasks. The absence of these comparisons makes it difficult to assess the true performance of the proposed method relative to the current state-of-the-art. Specifically, the paper should compare against methods that also leverage diffusion models for compression, as these are the most relevant baselines for this work.

3. The paper does not provide a detailed analysis of the computational complexity of the proposed method. It would be beneficial to include a comparison of the computational cost (e.g., encoding time, decoding time, memory usage) with other state-of-the-art methods. This is crucial for understanding the practical applicability of the proposed method, especially in resource-constrained environments. The analysis should include a breakdown of the computational cost of each component of the model, such as the encoder, decoder, and entropy coding.

4. The paper does not discuss the limitations of the proposed method. It would be helpful to include a discussion of the scenarios where the proposed method may not perform well, such as images with complex textures or high levels of noise. The paper should also discuss the potential impact of the granularity control mechanism on the quality of the compressed images, especially at very low or very high bitrates. A thorough discussion of limitations is essential for a balanced assessment of the proposed method.

### Suggestions

The authors should focus on demonstrating the novelty of their approach by highlighting the specific modifications made to the VQGAN architecture and the encoder-decoder design. They should clearly articulate how their method differs from existing VQGAN-based compression techniques and what unique advantages it offers. This could involve a more detailed analysis of the granularity control mechanism, including how it is implemented and how it affects the compression performance. The authors should also provide a more thorough ablation study to show the impact of each component of their method, such as the probabilistic conditional decoder, on the overall performance. This would help to justify the design choices and demonstrate the effectiveness of the proposed approach.

To address the lack of comparison with diffusion-based methods, the authors should include a comprehensive experimental evaluation against state-of-the-art diffusion-based image compression techniques. This evaluation should include a wide range of datasets and bitrates to provide a thorough comparison. The authors should also discuss the trade-offs between their method and diffusion-based methods in terms of performance, computational cost, and memory usage. This would help to position their work within the broader landscape of image compression methods and highlight its unique contributions. Furthermore, the authors should consider comparing against methods that use similar latent representations or compression techniques to better isolate the impact of their proposed approach.

Finally, the authors should provide a detailed analysis of the computational complexity of their method, including a breakdown of the encoding and decoding times, as well as the memory usage. This analysis should be compared with other state-of-the-art methods to provide a clear understanding of the computational overhead of the proposed approach. The authors should also discuss the potential for optimizing their method to reduce its computational cost, such as using more efficient data structures or algorithms. Additionally, the authors should discuss the limitations of their method in terms of the types of images it can effectively compress and the scenarios where it may not perform well. This would provide a more balanced and realistic assessment of the proposed method.

### Questions

1. How does the proposed method compare to state-of-the-art diffusion-based image compression methods, such as DiffBIR [1] and DiffBIR++ [2]?
2. What is the computational complexity of the proposed method compared to other state-of-the-art methods?
3. What are the limitations of the proposed method, and in which scenarios may it not perform well?

[1] DiffBIR: Towards Blind Image Restoration with Generative Diffusion Prior. Xue, Y., et al. ICCV, 2023.

[2] DiffBIR++: Improved Diffusion Prior for Blind Image Restoration. Xue, Y., et al. CVPR, 2024.

### Rating

5

### Confidence

4

**********
