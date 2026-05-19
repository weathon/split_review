### Summary

This paper proposes a variable-rate image compression method based on VQGAN, which allows fine-grained bitrate adaptation across a broad spectrum while ensuring high-fidelity compression. The method is based on a VQGAN framework that encodes an image as a sequence of variable-length codes, which can be losslessly compressed and exhibits a direct positive correlation with the bitrates. The method correlates the information density of local image patches with their granular representations, enabling dynamic adjustment for VQ-indices to achieve desirable compression rates. The method further develops a probabilistic conditional decoder capable of retrieving historic encoded multi-granularity representations according to transmitted codes, and then reconstruct hierarchical granular features in the formalization of conditional probability, enabling more informative aggregation to improve reconstruction realism. The method allows highly flexible and controllable bitrate adaption where the results demonstrate its superior performance over recent state-of-the-art methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and effective.
3. The experimental results are promising.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational complexity and efficiency of the proposed method. While the experimental results demonstrate superior performance, it is important to understand the computational cost associated with the approach. Specifically, the paper should provide a breakdown of the computational cost associated with each component of the proposed method, including the encoder, decoder, and entropy coding modules. This analysis should include metrics such as the number of parameters, FLOPs, and memory requirements. Furthermore, a comparison of the computational cost with existing methods would be valuable to understand the trade-offs between performance and efficiency. This would help assess the practicality of the approach for real-world applications, especially in resource-constrained environments.
2. The paper does not provide a comprehensive evaluation of the proposed method on a diverse set of images. While the results on the Kodak dataset are promising, it is important to evaluate the method on a wider range of images with varying characteristics, such as different textures, lighting conditions, and object types. This would help assess the generalization ability of the proposed method and its robustness to different types of images. The evaluation should include both qualitative and quantitative results, and should consider metrics that are relevant to image compression, such as PSNR, SSIM, and perceptual metrics.

### Suggestions

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the computational cost associated with each component of their proposed method. This should include the number of parameters, FLOPs, and memory requirements for the encoder, decoder, and entropy coding modules. Furthermore, the authors should compare the computational cost of their method with existing state-of-the-art image compression techniques. This comparison should be performed on a standard hardware platform and should include metrics such as encoding and decoding time. This analysis would provide a clearer understanding of the trade-offs between performance and efficiency, and would help assess the practicality of the proposed method for real-world applications. For example, the authors could compare their method against both traditional codecs like JPEG2000 and H.265, as well as recent learned compression methods.

To improve the evaluation of the proposed method, the authors should conduct experiments on a more diverse set of images. This should include images with varying characteristics, such as different textures, lighting conditions, and object types. The evaluation should include both qualitative and quantitative results, and should consider metrics that are relevant to image compression, such as PSNR, SSIM, and perceptual metrics. The authors should also analyze the performance of their method on images with different levels of complexity, and should discuss any limitations or challenges that arise. For example, the authors could evaluate their method on datasets such as Set5, Set14, and BSD100, in addition to the Kodak dataset. This would provide a more comprehensive assessment of the generalization ability of the proposed method and its robustness to different types of images.

Finally, the authors should provide a more detailed explanation of the granularity-informed encoder and the probabilistic conditional decoder. This should include a discussion of the design choices and the rationale behind them. For example, the authors should explain how the information density of local image patches is correlated with their granular representations, and how this enables dynamic adjustment of VQ-indices. They should also explain how the probabilistic conditional decoder reconstructs hierarchical granular features in a conditional probability manner, and how this improves reconstruction realism. This would help the reader better understand the technical details of the proposed method and its advantages over existing approaches.

### Questions

Please refer to the Weaknesses.

### Rating

6

### Confidence

4

**********
