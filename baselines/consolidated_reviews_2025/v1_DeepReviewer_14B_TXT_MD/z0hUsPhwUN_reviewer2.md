### Summary

This paper presents a new image compression framework called Control-GIC. The framework is based on a VQGAN model and allows for fine-grained bitrate adaptation across a wide range of compression rates. The key idea is to correlate the information density of local image patches with their granular representations, enabling dynamic adjustment of VQ-indices to achieve desired compression rates. A probabilistic conditional decoder is also developed to reconstruct hierarchical granular features in a conditional probability manner, improving reconstruction realism. The paper demonstrates that Control-GIC outperforms recent state-of-the-art methods in terms of flexibility, perceptual quality, and compression efficiency.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper proposes a novel and innovative approach to image compression by introducing a controllable generative model that allows for fine-grained bitrate adaptation. This is a significant advancement over existing methods that either require separate models for different compression ratios or support only limited ranges of bitrates.

The experimental results demonstrate the superior performance of Control-GIC compared to recent state-of-the-art methods, including generative, progressive, and variable-rate compression methods. The proposed method achieves better perceptual quality, flexibility, and compression efficiency using a single unified model.

The paper is well-written and clearly explains the proposed method, including the granularity-informed encoder, statistical entropy coding, and probabilistic conditional decoder. The figures and illustrations effectively convey the key concepts and design choices.

### Weaknesses

#### Some Related Works


#### comment

The paper lacks a detailed analysis of the computational complexity and efficiency of the proposed method. While the experimental results demonstrate superior performance, it is important to understand the computational cost associated with the approach. Specifically, the paper should provide a breakdown of the computational cost associated with each component of the proposed method, including the encoder, decoder, and entropy coding modules. This analysis should include metrics such as the number of parameters, FLOPs, and memory requirements. Furthermore, a comparison of the computational cost with existing methods would be valuable to understand the trade-offs between performance and efficiency. This would help assess the practicality of the approach for real-world applications, especially in resource-constrained environments.

The paper does not provide a comprehensive evaluation of the proposed method on a diverse set of images. While the results on the Kodak dataset are promising, it is important to evaluate the method on a wider range of images with varying characteristics, such as different textures, lighting conditions, and object types. This would help assess the generalization ability of the proposed method and its robustness to different types of images. The evaluation should include both qualitative and quantitative results, and should consider metrics that are relevant to image compression, such as PSNR, SSIM, and perceptual metrics.

### Suggestions

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the computational cost associated with each component of their proposed method. This should include the number of parameters, FLOPs, and memory requirements for the encoder, decoder, and entropy coding modules. Furthermore, the authors should compare the computational cost of their method with existing state-of-the-art image compression techniques. This comparison should be performed on a standard hardware platform and should include metrics such as encoding and decoding time. This analysis would provide a clearer understanding of the trade-offs between performance and efficiency, and would help assess the practicality of the proposed method for real-world applications. For example, the authors could compare their method against both traditional codecs like JPEG2000 and H.265, as well as recent learned compression methods.

To improve the evaluation of the proposed method, the authors should conduct experiments on a more diverse set of images. This should include images with varying characteristics, such as different textures, lighting conditions, and object types. The evaluation should include both qualitative and quantitative results, and should consider metrics that are relevant to image compression, such as PSNR, SSIM, and perceptual metrics. The authors should also analyze the performance of their method on images with different levels of complexity, and should discuss any limitations or challenges that arise. For example, the authors could evaluate their method on datasets such as Set5, Set14, and BSD100, in addition to the Kodak dataset. This would provide a more comprehensive assessment of the generalization ability of the proposed method and its robustness to different types of images.

Finally, the authors should provide a more detailed explanation of the granularity-informed encoder and the probabilistic conditional decoder. This should include a discussion of the design choices and the rationale behind them. For example, the authors should explain how the information density of local image patches is correlated with their granular representations, and how this enables dynamic adjustment of VQ-indices. They should also explain how the probabilistic conditional decoder reconstructs hierarchical granular features in a conditional probability manner, and how this improves reconstruction realism. This would help the reader better understand the technical details of the proposed method and its advantages over existing approaches.

### Questions

Can you provide more details on the computational complexity and efficiency of the proposed method? How does it compare to existing methods in terms of computational cost?

Have you evaluated the proposed method on a more diverse set of images? What are the results and how do they compare to existing methods?

### Rating

6

### Confidence

4

**********
