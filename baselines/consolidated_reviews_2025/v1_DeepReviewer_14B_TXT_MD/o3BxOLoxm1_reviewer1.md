### Summary

This paper introduces a training-free framework for conditional generation using pre-trained diffusion models. The proposed method, Manifold Preserving Guided Diffusion (MPGD), aims to address the limitations of previous training-free guidance methods, which often require extensive sampling time optimization or a large number of diffusion time steps to produce satisfactory samples. The authors start with the manifold hypothesis and introduce a shortcut algorithm to save time and memory while improving sample quality in low-resource settings. They also present two approaches for manifold projection using off-the-shelf, unconditionally pre-trained autoencoders for pixel-space diffusion models. Furthermore, they demonstrate that applying the shortcut to latent diffusion models naturally preserves the manifold, enhancing sample quality and inference speed. In various conditional generation tasks, MPGD consistently outperforms training-free guided diffusion baselines in terms of the trade-off between fidelity and controllability while achieving up to 3.8× speed-ups with the same number of diffusion steps and maintaining high sample quality.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The motivation is well explained, and the proposed method is state-of-the-art compared to other training-free conditional diffusion methods.

### Weaknesses

#### Some Related Works

[1] Adding Conditional Control to Text-to-Image Diffusion Models

#### comment

The authors assume that the data lies on a low-dimensional manifold, which is a common assumption in many generative models. However, it is unclear how well this assumption holds in practice, especially for complex real-world data distributions. The authors could provide empirical evidence to support this assumption, such as visualizing the manifold structure of the generated data or quantifying the dimensionality of the learned manifold. Furthermore, the reliance on a pre-trained autoencoder introduces a dependency on the quality of its learned latent space. If the autoencoder does not effectively capture the underlying data manifold, the proposed method's performance will likely suffer. The paper should include an analysis of how the choice of autoencoder impacts the final results, especially in cases where the autoencoder is not perfectly trained or is trained on a different dataset than the diffusion model.

### Suggestions

The authors should investigate the sensitivity of their method to the choice of autoencoder. Specifically, they could experiment with different autoencoder architectures and training datasets to assess how these factors affect the quality of the generated samples. It would be beneficial to include a quantitative analysis of the latent space of the autoencoder, such as measuring its dimensionality and the distribution of the latent codes. This would provide more insight into how well the autoencoder captures the underlying data manifold and how this impacts the performance of the proposed method. Furthermore, the authors could explore techniques to mitigate the impact of a poorly trained autoencoder, such as incorporating a regularization term that encourages the latent codes to lie on a well-defined manifold.

To further validate the manifold assumption, the authors could perform experiments to visualize the manifold structure of the generated data. For example, they could use dimensionality reduction techniques like t-SNE or UMAP to project the high-dimensional latent codes into a 2D or 3D space and visualize the resulting manifold. This would allow them to assess whether the generated samples lie on a well-defined manifold and how the proposed method affects the manifold structure. Additionally, the authors could quantify the dimensionality of the learned manifold by measuring the intrinsic dimensionality of the latent codes. This would provide a more rigorous evaluation of the manifold assumption and help to identify the limitations of the proposed method.

Finally, the authors should provide a more detailed comparison of their method with other training-free conditional diffusion methods, including a discussion of the trade-offs between sample quality, inference speed, and computational cost. While the paper claims state-of-the-art performance, it would be beneficial to include a more thorough analysis of the strengths and weaknesses of the proposed method compared to existing approaches. This would help the reader to better understand the practical implications of using the proposed method and its potential limitations. Specifically, a comparison with methods like ControlNet [1] would be valuable, even if ControlNet requires training, as it is a widely used method for conditional image generation.

### Questions

1. The authors assume that the data lies on a low-dimensional manifold. How valid is this assumption in practice, especially for complex real-world data distributions? The authors could provide empirical evidence to support this assumption.

2. The proposed method requires a pre-trained autoencoder. How does the choice of autoencoder affect the performance of the proposed method? What are the trade-offs between different autoencoders in terms of sample quality, inference speed, and computational cost?

3. How does the proposed method compare to other state-of-the-art conditional generation methods, such as ControlNet [1]? The authors could provide a more detailed comparison of the strengths and weaknesses of their method compared to existing approaches.

[1] Adding Conditional Control to Text-to-Image Diffusion Models. https://arxiv.org/abs/2108.12449

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
