### Summary

This paper proposes a novel image compression framework named Control-GIC, which aims to address the limitations of existing generative image compression methods by enabling flexible and precise bitrate adaptation. The framework utilizes a VQGAN-based architecture with a granularity-informed encoder to control the compression rate by adjusting the granularity of the latent representations. The probabilistic conditional decoder is used to reconstruct hierarchical granular features in a conditional probability manner, which helps to improve reconstruction realism. The paper presents experimental results that demonstrate the effectiveness of the proposed method in achieving superior rate-distortion performance compared to state-of-the-art methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to image compression by leveraging the VQGAN framework and incorporating a granularity-informed encoder to achieve flexible bitrate control. This is a significant departure from traditional fixed-rate compression methods and allows for more precise control over the trade-off between compression rate and reconstruction quality.
2. The proposed method is well-motivated and addresses a key limitation of existing generative image compression methods, which often struggle to adapt to diverse compression requirements and scenarios. The use of a probabilistic conditional decoder is also a notable contribution, as it enables the reconstruction of hierarchical granular features in a more realistic manner.
3. The paper is well-written and easy to follow, with clear explanations of the proposed method and its components. The figures and tables are informative and effectively illustrate the key concepts and results.
4. The experimental results demonstrate the effectiveness of the proposed method in achieving superior rate-distortion performance compared to state-of-the-art methods. The ablation studies provide valuable insights into the impact of different components of the framework.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed method, which is an important factor for practical applications. Specifically, the paper lacks a breakdown of the computational cost associated with the granularity-informed encoder and the probabilistic conditional decoder. This makes it difficult to assess the feasibility of deploying the method on resource-constrained devices.
2. The paper does not discuss the limitations of the proposed method, such as its performance on different types of images or its robustness to noise and other distortions. The evaluation is primarily focused on clean images, and there is no analysis of how the method performs under adverse conditions, such as compression artifacts or image degradation. This limits the understanding of the method's practical applicability.
3. The paper does not provide a comparison with other state-of-the-art image compression methods, such as BPG, which is a widely used and high-performing codec. The absence of a comparison with BPG makes it difficult to assess the practical relevance of the proposed method, especially given that BPG is a strong baseline for image compression.

### Suggestions

The paper would benefit from a more thorough analysis of the computational complexity of the proposed method. The authors should provide a detailed breakdown of the computational cost associated with each component of the framework, including the granularity-informed encoder and the probabilistic conditional decoder. This analysis should include both time and memory complexity, and should be compared against existing methods. Furthermore, the authors should discuss the potential for optimizing the implementation to reduce computational overhead, such as using more efficient data structures or algorithms. This would provide a more complete picture of the practical feasibility of the proposed method and allow for a more informed assessment of its potential for real-world applications. It would also be beneficial to include a discussion of the trade-offs between compression rate, reconstruction quality, and computational cost, which would help users to make informed decisions about the appropriate settings for their specific needs.

To address the limitations regarding the evaluation of the proposed method, the authors should conduct experiments on a wider range of image types and under different conditions. This should include an analysis of the method's performance on images with varying levels of detail, texture, and complexity. Furthermore, the authors should evaluate the method's robustness to noise and other distortions, such as compression artifacts and image degradation. This could involve adding synthetic noise to the input images or evaluating the method's performance on images with real-world distortions. The authors should also compare the proposed method with other state-of-the-art image compression methods, such as BPG, to provide a more comprehensive assessment of its performance. This comparison should include both rate-distortion performance and computational complexity. The evaluation should also include a qualitative analysis of the reconstructed images, which would provide insights into the visual quality of the compression.

Finally, the authors should provide a more detailed discussion of the limitations of the proposed method, including its potential failure cases and its sensitivity to different parameters. This discussion should be based on the experimental results and should provide a clear understanding of the conditions under which the method performs well and the conditions under which it may fail. The authors should also discuss the potential for future research to address these limitations, such as exploring alternative encoder and decoder architectures or developing more robust training techniques. This would provide a more balanced and comprehensive assessment of the proposed method and help to guide future research in this area.

### Questions

1. How does the proposed method perform on different types of images, such as natural images, textures, and images with complex structures?
2. How robust is the proposed method to noise and other distortions in the input images?
3. How does the proposed method compare with other state-of-the-art image compression methods, such as BPG, in terms of rate-distortion performance and computational complexity?

### Rating

6

### Confidence

4

**********
