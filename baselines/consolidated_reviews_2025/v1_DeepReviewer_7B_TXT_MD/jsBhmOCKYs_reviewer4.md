### Summary

This paper introduces a novel approach for domain adaptation in image restoration by leveraging the noise space of diffusion models. The proposed method, termed denoising as adaptation, aims to bridge the domain gap between synthetic and real-world degraded images. The authors demonstrate the effectiveness of their approach through experiments on denoising, deblurring, and deraining tasks, showing improvements over existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel approach for domain adaptation in image restoration by leveraging the noise space of diffusion models. This is a creative and innovative idea that has the potential to advance the field of image restoration.
2. The authors provide a clear and detailed explanation of their method, including the diffusion loss, channel-shuffling layer, and residual-swapping contrastive learning strategy. The paper is well-written and easy to follow.
3. The proposed method is evaluated on three classical image restoration tasks: denoising, deblurring, and deraining. The results demonstrate the effectiveness of the method and its potential for practical applications.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not efficient. The proposed method requires training a diffusion model to compute the diffusion loss. The training of the diffusion model is time-consuming and requires a large amount of memory. The inference process also requires a large number of steps to generate a clean image, which makes the method less practical.
2. The proposed method is not generalizable to other tasks. The proposed method is only evaluated on denoising, deblurring, and deraining tasks. It is not clear if the method can be applied to other image restoration tasks, such as super-resolution or inpainting.
3. The proposed method is not robust to different types of degradation. The proposed method is evaluated on synthetic degradations. It is not clear if the method can be applied to real-world degradations, such as compression artifacts or sensor noise.

### Suggestions

The authors should investigate methods to reduce the computational cost of the diffusion model. One approach could be to explore lightweight diffusion models or to investigate techniques for accelerating the diffusion process, such as using fewer sampling steps or employing more efficient sampling algorithms. Another direction could be to investigate if the diffusion model can be trained in a more efficient manner, for example, by using a smaller dataset or by employing techniques like knowledge distillation. Furthermore, a detailed analysis of the computational cost of the method, including training time, memory requirements, and inference time, should be provided and compared to other domain adaptation methods. This would help to better understand the practical limitations of the proposed method.

To address the limited generalizability of the method, the authors should evaluate it on a wider range of image restoration tasks, including super-resolution and inpainting. This would provide a more comprehensive assessment of the method's applicability. Additionally, the authors should investigate the impact of different types of degradation on the performance of the method. This could involve evaluating the method on datasets with real-world degradations, such as compression artifacts or sensor noise. The authors should also explore techniques to make the method more robust to different types of degradation, such as using data augmentation or adversarial training. Furthermore, a detailed analysis of the performance of the method on different tasks and degradations, including quantitative results and qualitative examples, should be provided.

Finally, the authors should provide a more detailed analysis of the limitations of the proposed method. This should include a discussion of the scenarios where the method is likely to fail and the potential reasons for these failures. For example, the authors should discuss the limitations of the method in handling severe degradations or in adapting to very different types of real-world data. The authors should also discuss the potential impact of the choice of the diffusion model on the performance of the method. This would help to better understand the strengths and weaknesses of the proposed method and to identify areas for future research.

### Questions

Please see the weakness.

### Rating

8

### Confidence

4

**********
