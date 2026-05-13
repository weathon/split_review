# Image Inpainting via Tractable Steering of Diffusion Models

- Decision: Accept
- Scores: 5, 6, 6, 5

## Abstract
Diffusion models are the current state of the art for generating photorealistic images. Controlling the sampling process for constrained image generation tasks such as inpainting, however,  remains challenging since exact conditioning on such constraints is intractable. While existing methods use various techniques to approximate the constrained posterior, this paper proposes to exploit the ability of Tractable Probabilistic Models (TPMs) to exactly and efficiently compute the constrained posterior, and to leverage this signal to steer the denoising process of diffusion models. Specifically, this paper adopts a class of expressive TPMs termed Probabilistic Circuits (PCs). Building upon prior advances, we further scale up PCs and make them capable of guiding the image generation process of diffusion models. Empirical results suggest that our approach can consistently improve the overall quality and semantic coherence of inpainted images across three natural image datasets (\ie CelebA-HQ, ImageNet, and LSUN) with only $\sim\! 10 \%$ additional computational overhead brought by the TPM. Further, with the help of an image encoder and decoder, our method can readily accept semantic constraints on specific regions of the image, which opens up the potential for more controlled image generation tasks. In addition to proposing a new framework for constrained image generation, this paper highlights the benefit of more tractable models and motivates the development of expressive TPMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to use TPM for conditional image generation, specifically image inpainting, in diffusion models. Previous methods usually use a hard pixel reset or gradient backward to enforce the image to be coherent with the input image for image inpainting using pre-trained diffusion models. This paper, on the other hand, attempts to utilize the TPM along with the diffusion models to enforce the image to be coherent. At each timestep, the proposed method reconstructs the $x_0$ with both the diffusion model and TPM and takes the geometric mean to get the output. Results are compared on multiple datasets including CelebA, LSUN-Bedroom, and ImageNet.

### Strengths
1. The use of TPM for the conditional generation of diffusion models is interesting.
2. The overall quantitative results look good compared to previous methods.

### Weaknesses
1. The comparison only contains six different masks. In real application, the cases where the images are masked by some texts or patterns are also very common. It would be ideal to see more comparisons of such masks in arbitrary shapes.
2. The table only contains LPIPS for quantitative measurement, however, as image inpainting is an ill-posed problem, a user study would be beneficial in this case as previous works such as [1][2] perform.

### Questions
From Figure 1 and Table 3, there are some hyper-parameters specifically tuned for different datasets especially $t_{cut}$ which has also been applied in many previous works, could the authors provide an ablation study over the selection of the hyper-parameters?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel method that integrates Tractable Probabilistic Models, particularly Probabilistic Circuits, to address the challenges in controlling diffusion models for image inpainting tasks. This approach aims to achieve more precise and efficient inpainting by leveraging the exact computation of constrained posteriors provided by TPMs.​

### Strengths
The paper appears to present a novel approach to the problem of image inpainting using diffusion models. The integration of Tractable Probabilistic Models (TPMs), specifically Probabilistic Circuits (PCs), to guide the denoising process of diffusion models is an inventive combination of existing ideas. 
This creative synergy seems to address the intractability issue inherent in exact conditioning required for tasks like inpainting. Additionally, the paper builds upon prior advances to scale up PCs for guiding the image generation process, which could be considered an original contribution in terms of improving and extending existing methodologies.

### Weaknesses
1. The TPMs seem to be a general design, while this work constrain the application to image inpainting only, I am not sure about the intuition of this specific application. How about the potential of this method for general conditional generation? 

2. In section 6.2, it says "we only need to incorporate guidance from the TPM in the early denoising stages to control the global semantics of the image; fine-grained details can be later refined by the diffusion model. As a result, TPM is only required in the first ∼20% denoising steps". Here, more experimental analysis of the TPM steps are expected, including the effect on generation quality, semantic coherence, and computational efficiency.

3. Limitations and Failure Cases: A discussion of the method's limitations and failure cases are not addressed in this research, which would be beneficial for the application of this work.

### Questions
See above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper investigated image inpainting using a pre-trained diffusion model by using the proposed TPM approach to enforce the inpainting constraints. Unlike repaint or copaint that either enforce the inpainting constraints through the time travel technique or gradient-based methods to optimize, this paper proposes to model p_\theta{x_0} by PC, which turns the computation into a normalized multiplication of the model weight based on the graph. The proposed method was combined with copaint and compared with existing methods. The LPIPS value got slightly improved on three commonly used datasets: CelebA-HQ, ImageNet, LSUN-Bedroom. Visual examples were presented and computing cost was discussed.

### Strengths
- Inpainting using pre-trained diffusion is an interesting direction to explore and modeling p_\theta{x_0} provides an alternative angle to look into this problem. 
- The presentation is clear and results show the potential of the proposed method. On the three datasets, CelebA-HQ, ImageNet, LSUN-Bedroom, with masks of different shapes or at different positions, the proposed approach achieved higher LPIPS scores mostly. 
- A practical approximation to apply the proposed methods for high-resolution imprinting was discussed and proposed.

### Weaknesses
 - The computing cost is related to the size of the hole as well as the network architecture. As authors have mentioned, it also related to resolution. So instead of claiming 10% additional computation overhead, a detailed analysis is more helpful. Specifically, the analysis should consider the computational complexity with respect to the number of pixels in the masked region, and how this scales with different network architectures, such as varying the number of layers or the width of the feature maps. It would also be beneficial to see a breakdown of the computational cost, showing the time spent on the proposed TPM method versus the standard diffusion steps.
- Number-wise the improvement on LPIPS value compared to CoPaint, or even RePaint is minor. How about other metrics? Or user studies? The LPIPS metric, while useful, doesn't fully capture perceptual quality. It would be beneficial to include metrics that assess structural similarity (SSIM) or other measures that better align with human perception. Furthermore, a user study would provide valuable insights into the subjective quality of the inpainting results, as it is possible that the LPIPS improvements do not translate to a noticeable improvement in visual quality.
- Section 4.2 reads slightly disconnected from Section 4.1, especially the introduction of the equation 7. The transition from the general TPM framework to the specific implementation details in Section 4.2 is abrupt. The connection between the theoretical formulation and the practical application of Equation 7 is not clearly established. It would be helpful to provide more context and motivation for the introduction of this equation, explaining how it directly relates to the computation of  $p_{TPM} (\tilde{\mathbf{x}}_0 | \mathbf{x}_t, \mathbf{x}_0^k)$ as described in Section 4.1.

### Questions
Will code be released upon publication of this work?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a method of incorporating Probabilistic Circuits (PCs) into diffusion models, with the authors claiming that this approach can encourage diffusion models to generate structurally more coherent images in image inpainting.

### Strengths
In this paper, the Tractable Probabilistic Models (TPMs) are first introduced into the task of controllable image inpainting. Experimental results demonstrate that this approach encourages the model to generate higher-quality samples with only a limited computational cost increase.
The experimental results seem visually plausible.

### Weaknesses
1) The readability of this paper is relatively low. We believe that the author should explain in the introduction and method sections whether the method proposed is training or non-training. If it is the former, the loss function and the parts of the network that need to be updated should be stated explicitly. If it is the latter, the pseudo-code of the algorithm should be given.

2) The experimental section lacks metrics. Specifically, the paper only uses LPIPS, which is a perceptual metric, but does not include metrics that measure the quality of the generated images, such as FID or U-IDS. This makes it difficult to assess the actual performance of the proposed method compared to existing approaches.

3) Have the authors tried irregular masks?

### Questions
1) I cannot fully understand the details of the method proposed in this paper (e.g., how were the weights in the PC obtained). I would appreciate it if the authors could provide pseudocode to enhance the method's readability further.

2) LPIPS alone may not be sufficient to assess the quality of generated images. We recommend that the authors report metrics such as FID, U-IDS, etc.


If I have misunderstood, please point it out.

I am very willing to improve the rating after reading your rebuttal and considering the opinions of other reviewers.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
