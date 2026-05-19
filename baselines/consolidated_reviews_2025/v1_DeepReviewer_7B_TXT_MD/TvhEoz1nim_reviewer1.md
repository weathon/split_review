### Summary

This paper proposes a novel model inversion attack (MIA) method that leverages diffusion models to generate synthetic data that closely resembles private training data. The proposed method is evaluated on CelebA and FFHQ datasets and shows improved performance compared to existing GAN-based MIAs.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed method is simple and easy to implement.
2. The proposed method is evaluated on two datasets and shows improved performance compared to existing GAN-based MIAs.

### Weaknesses

#### Some Related Works

[1] Inversion attacks against image generative models.

#### comment

1. The proposed method is not evaluated on large-scale datasets such as ImageNet. It is unclear whether the proposed method can scale to large datasets.
2. The proposed method is not evaluated on more advanced generative models such as SD and FLUX. It is unclear whether the proposed method can scale to more advanced generative models.
3. The proposed method is not evaluated on more advanced GAN-based MIAs such as [1]. It is unclear whether the proposed method can scale to more advanced GAN-based MIAs.
4. The proposed method is only evaluated on classification models. It is unclear whether the proposed method can be extended to other types of models.
5. The proposed method is only evaluated on CLIP. It is unclear whether the proposed method can be extended to other types of models.

### Suggestions

The paper introduces a novel model inversion attack (MIA) using diffusion models, which is a promising direction. However, the evaluation is limited in scope, and the paper should address these limitations to fully demonstrate the potential of the proposed method. Specifically, the authors should evaluate their method on larger and more diverse datasets, such as ImageNet, to assess its scalability. Furthermore, the evaluation should include more advanced generative models like Stable Diffusion (SD) and FLUX, as these models have become the state-of-the-art in image generation. The current evaluation is limited to simpler models, and it is unclear if the proposed method can effectively handle the complexities of these more advanced models. Additionally, the comparison with other GAN-based MIAs should be expanded to include more recent and advanced methods, such as the one mentioned in the original review, to provide a more comprehensive understanding of the proposed method's performance relative to the current state-of-the-art. 

To address the lack of evaluation on diverse model architectures, the authors should explore the applicability of their method to other types of models beyond classification models. For instance, evaluating the method on object detection models or segmentation models would provide a more complete picture of its generalizability. Similarly, the evaluation should be extended to other types of multimodal models, such as large language models (LLMs), to assess its effectiveness in different contexts. The current focus on CLIP models limits the understanding of the method's potential impact. The authors should also consider evaluating the method on models with different architectures and training procedures to ensure its robustness and adaptability. This would involve testing on models trained with different loss functions and optimization techniques, which would provide a more comprehensive evaluation of the method's performance. 

Finally, the paper should provide a more detailed analysis of the computational cost and efficiency of the proposed method. While the method is presented as simple and easy to implement, the computational requirements for training diffusion models can be substantial. The authors should provide a detailed analysis of the training time, memory usage, and inference time of their method, and compare it with other existing MIAs. This analysis should also include a discussion of the trade-offs between performance and computational cost, which would help readers understand the practical implications of using the proposed method. Furthermore, the authors should explore potential optimizations to reduce the computational overhead of their method, making it more accessible for practical applications.

### Questions

See above.

### Rating

5

### Confidence

4

**********
