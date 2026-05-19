### Summary

This paper proposes a new training-free conditional generation framework called Manifold Preserving Guided Diffusion (MPGD) that leverages pretrained diffusion models and off-the-shelf neural networks with minimal additional inference cost for a broad range of tasks. The authors leverage the manifold hypothesis to refine the guided diffusion steps and introduce a shortcut algorithm in the process. They also propose two methods for on-manifold training-free guidance using pre-trained autoencoders and demonstrate that their shortcut inherently preserves the manifolds when applied to latent diffusion models. The experiments show that MPGD is efficient and effective for solving a variety of conditional generation applications in low-compute settings, and can consistently offer up to 3.8× speed-ups with the same number of diffusion steps while maintaining high sample quality compared to the baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The idea of manifold preserving guided diffusion is novel and interesting.
3. The proposed method is simple and effective.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method requires a pre-trained autoencoder, which may not be available for all tasks or datasets. This dependency limits the applicability of the method, especially in scenarios where suitable pre-trained autoencoders are not readily accessible or when the target domain significantly differs from the domain on which the autoencoder was trained. The performance of MPGD is thus inherently tied to the quality and relevance of the chosen autoencoder, potentially leading to suboptimal results if the autoencoder's latent space does not align well with the desired conditional generation task.

2. The authors only provide qualitative results for the style guidance with Stable Diffusion. More quantitative results are needed to better evaluate the proposed method. The lack of quantitative metrics makes it difficult to objectively assess the performance of MPGD in style transfer tasks. It is unclear how well the generated images match the target style in terms of specific features or statistical properties. Without such metrics, it is hard to compare MPGD with other style transfer methods or to determine the extent to which it achieves the desired style transfer.

3. The authors should provide more details about the training process and the hyperparameters used in the experiments. The absence of detailed training information makes it challenging to reproduce the results and to understand the sensitivity of the method to different hyperparameter settings. It is important to know the specific optimization algorithms, learning rates, batch sizes, and other training details to ensure the robustness and reliability of the proposed approach.

### Suggestions

To address the limitation of requiring a pre-trained autoencoder, the authors could explore methods to reduce the dependency on specific autoencoders or investigate techniques to adapt existing autoencoders to new domains. For instance, they could investigate fine-tuning the autoencoder on a small set of images from the target domain or explore methods to learn a more robust latent space that is less sensitive to domain shifts. Additionally, the authors could explore the possibility of using a combination of different autoencoders or learning a shared latent space across multiple autoencoders to improve the generalization capability of the method. This would make the method more versatile and applicable to a wider range of tasks and datasets.

To improve the evaluation of the style guidance task, the authors should include quantitative metrics that measure the similarity between the generated images and the target style. This could involve using metrics such as perceptual similarity scores, style loss functions, or feature-based metrics that capture the statistical properties of the style. For example, they could use a pre-trained style classifier to measure the probability that the generated image belongs to the target style. Furthermore, the authors should compare the performance of MPGD with other state-of-the-art style transfer methods using these quantitative metrics. This would provide a more objective and comprehensive evaluation of the proposed method and allow for a better understanding of its strengths and weaknesses.

To enhance the reproducibility and understanding of the proposed method, the authors should provide detailed information about the training process and the hyperparameters used in the experiments. This should include the specific optimization algorithms, learning rates, batch sizes, and other relevant training details. The authors should also investigate the sensitivity of the method to different hyperparameter settings and provide guidelines for choosing appropriate values. This would allow other researchers to reproduce the results and to adapt the method to new tasks and datasets. Furthermore, the authors could consider releasing their code and trained models to facilitate further research and development in this area.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
