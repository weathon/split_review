### Summary

This paper proposes a new model inversion attack method by leveraging the diffusion model. Specifically, the authors first train a diffusion model and then perform model inversion on the trained diffusion model. The authors also extend the proposed method to the multimodal model, CLIP. The experiments show that the proposed method can achieve better performance than existing methods based on GAN.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The authors conduct extensive experiments to show the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not novel enough. The proposed method simply replaces the GAN with a diffusion model to achieve better performance. The core idea of using a generative model to guide the inversion process is not new, and the paper does not sufficiently articulate the specific challenges or innovations in adapting diffusion models for this task, beyond simply stating that GANs are problematic. The paper lacks a detailed explanation of why diffusion models are inherently better suited for this task, beyond empirical results.
2. The authors claim that the proposed method can be applied to the multimodal model, CLIP. However, the proposed method is still based on the single objective of the target model. The authors should clarify the motivation of applying the proposed method to CLIP. The paper does not clearly define what constitutes a privacy leak in the context of CLIP, and how the proposed method addresses this specific type of vulnerability. The connection between reconstructing an image from a text prompt and a genuine privacy leak is not well-established.
3. The authors should also compare the proposed method with more recent methods, such as [a]. The lack of comparison with recent state-of-the-art methods makes it difficult to assess the true contribution of the proposed method. The paper should include a more comprehensive evaluation against contemporary techniques to demonstrate its relative advantages and limitations.

### Suggestions

The paper should provide a more in-depth analysis of why diffusion models are better suited for model inversion attacks compared to GANs, beyond simply stating that GANs are difficult to train. A detailed discussion of the theoretical properties of diffusion models, such as their ability to generate high-quality samples and their stability during training, would be beneficial. The authors should also explore the limitations of diffusion models in this context, such as the computational cost of the iterative sampling process, and how these limitations are addressed in the proposed method. Furthermore, the paper should include a more detailed explanation of the optimization process, including the specific loss functions used and the hyperparameter settings. This would allow for a better understanding of the method's inner workings and facilitate reproducibility.

To address the concerns regarding the application of the proposed method to CLIP, the authors should clearly define what constitutes a privacy leak in the context of multimodal models. The paper should explain how the ability to reconstruct an image from a text prompt can lead to a privacy violation, providing concrete examples to illustrate this point. The authors should also discuss the limitations of this approach, such as the potential for generating unrealistic or nonsensical images, and how these limitations can be mitigated. Furthermore, the paper should explore the potential for using the proposed method to extract other types of sensitive information from CLIP models, such as text data associated with images. This would demonstrate the broader applicability of the method and its potential impact on the security of multimodal models.

The paper should include a more comprehensive evaluation against recent state-of-the-art methods, including a detailed comparison of the performance of the proposed method with these techniques. The authors should also discuss the limitations of the proposed method, such as its computational cost and its sensitivity to hyperparameter settings. The paper should also explore the potential for combining the proposed method with other techniques, such as adversarial training, to further improve its performance. Finally, the authors should provide a more detailed analysis of the results, including a discussion of the statistical significance of the observed differences in performance. This would allow for a more robust assessment of the method's contribution and its potential impact on the field.

### Questions

Please see the weaknesses.

### Rating

5

### Confidence

4

**********
