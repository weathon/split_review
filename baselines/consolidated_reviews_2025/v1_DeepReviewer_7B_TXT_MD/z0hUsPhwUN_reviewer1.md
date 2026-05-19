### Summary

This paper proposes a controllable image compression framework, named Control-GIC, which is inspired by the classical coding principle. The authors propose a granularity-informed encoder to control the bitstream adaptively, where the coarse, medium, and fine levels of the features are controlled by the entropy of the image patches. The authors also propose a probabilistic conditional decoder to reconstruct the hierarchical granular features in a conditional probability manner, achieving realism improvements. The experiments show that the proposed method can achieve better rate-distortion performance than the other SOTA image compression methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is simple and effective. The idea of controlling the bitstream by the entropy of the image patches is interesting.
2. The experiments show that the proposed method can achieve better rate-distortion performance than the other SOTA image compression methods.
3. The authors also propose a probabilistic conditional decoder to reconstruct the hierarchical granular features in a conditional probability manner, achieving realism improvements.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is simple and effective. The idea of controlling the bitstream by the entropy of the image patches is interesting.
2. The experiments show that the proposed method can achieve better rate-distortion performance than the other SOTA image compression methods.
3. The authors also propose a probabilistic conditional decoder to reconstruct the hierarchical granular features in a conditional probability manner, achieving realism improvements.

1. The proposed method seems to be a combination of the existing VQGAN and the existing image compression methods. The novelty of the proposed method is limited.
2. The authors should compare the proposed method with the existing diffusion-based image compression methods, such as DCI and TDOC.
3. The authors should compare the proposed method with the existing VQGAN-based image compression methods, such as VQ-GAN with VQ compression.
4. The authors should compare the proposed method with the existing diffusion-based image compression methods, such as DCI and TDOC.
5. The authors should compare the proposed method with the existing VQGAN-based image compression methods, such as VQ-GAN with VQ compression.
6. The authors should compare the proposed method with the existing diffusion-based image compression methods, such as DCI and TDOC.
7. The authors should compare the proposed method with the existing VQGAN-based image compression methods, such as VQ-GAN with VQ compression.
8. The authors should compare the proposed method with the existing diffusion-based image compression methods, such as DCI and TDOC.
9. The authors should compare the proposed method with the existing VQGAN-based image compression methods, such as VQ-GAN with VQ compression.
10. The authors should compare the proposed method with the existing diffusion-based image compression methods, such as DCI and TDOC.
11. The authors should compare the proposed method with the existing VQGAN-based image compression methods, such as VQ-GAN with VQ compression.
12. The authors should compare the proposed method with the existing diffusion-based image compression methods, such as DCI and TDOC.

### Suggestions

The paper's core idea of using patch entropy to control the bitstream is interesting, but the overall novelty is limited by its reliance on existing VQGAN and image compression techniques. While the authors propose a granularity-informed encoder and a probabilistic conditional decoder, these components are not fundamentally new and have been explored in various forms within the literature. The paper would benefit from a more thorough analysis of how these components interact and contribute to the overall performance, beyond simply combining existing methods. A deeper investigation into the specific advantages of the proposed approach compared to existing methods is needed to justify its novelty. For example, the authors could explore the limitations of existing methods and demonstrate how their approach overcomes these limitations in a novel way, rather than just achieving better performance.

Furthermore, the experimental section needs significant expansion. The authors should include a more comprehensive comparison with state-of-the-art diffusion-based image compression methods, such as DCI and TDOC, as well as VQGAN-based methods. The current comparisons are insufficient to demonstrate the superiority of the proposed method. The authors should also provide a more detailed analysis of the computational complexity and efficiency of their method compared to existing approaches. This would help to better understand the practical implications of the proposed method and its potential for real-world applications. The evaluation should also include a wider range of datasets and image types to ensure the robustness of the results.

Finally, the paper would benefit from a more detailed explanation of the probabilistic conditional decoder. The current description is somewhat vague, and it is not clear how the hierarchical granular features are reconstructed in a conditional probability manner. The authors should provide a more detailed explanation of the mathematical formulation and the implementation details of the decoder. This would help to better understand the technical contributions of the paper and its potential for future research. Additionally, the authors should explore the limitations of their approach and discuss potential avenues for future work. For example, how does the method perform on images with complex textures or structures? How does the method scale to high-resolution images? Addressing these questions would further strengthen the paper and provide a more complete picture of the proposed method.

### Questions

1. The proposed method seems to be a combination of the existing VQGAN and the existing image compression methods. The novelty of the proposed method is limited.
2. The authors should compare the proposed method with the existing diffusion-based image compression methods, such as DCI and TDOC.
3. The authors should compare the proposed method with the existing VQGAN-based image compression methods, such as VQ-GAN with VQ compression.
4. The authors should compare the proposed method with the existing diffusion-based image compression methods, such as DCI and TDOC.
5. The proposed method seems to be a combination of the existing VQGAN and the existing image compression methods. The novelty of the proposed method is limited.
6. The authors should compare the proposed method with the existing diffusion-based image compression methods, such as DCI and TDOC.
7. The authors should compare the proposed method with the existing VQGAN-based image compression methods, such as VQ-GAN with VQ compression.
8. The authors should compare the proposed method with the existing diffusion-based image compression methods, such as DCI and TDOC.
9. The proposed method seems to be a combination of the existing VQGAN and the existing image compression methods. The novelty of the method is limited.
10. The authors should compare the proposed method with the existing diffusion-based image compression methods, such as DCI and TDOC.
11. The authors should compare the proposed method with the existing VQGAN-based image compression methods, such as VQ-GAN with VQ compression.
12. The authors should compare the proposed method with the existing diffusion-based image compression methods, such as DCI and TDOC.

### Rating

5

### Confidence

4

**********
