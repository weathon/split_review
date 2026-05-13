# InstaRevive: One-Step Image Enhancement via Dynamic Score Matching

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Image enhancement finds wide-ranging applications in real-world scenarios due to complex environments and the inherent limitations of imaging devices. Recent diffusion-based methods yield promising outcomes but necessitate prolonged and computationally intensive iterative sampling. In response, we propose InstaRevive, a straightforward yet powerful image enhancement framework that employs score-based diffusion distillation to harness potent generative capability and minimize the sampling steps. To fully exploit the potential of the pre-trained diffusion model, we devise a practical and effective diffusion distillation pipeline using dynamic noise control to address inaccuracies in updating direction during score matching. Our noise control strategy enables a dynamic diffusing scope, facilitating precise learning of denoising trajectories within the diffusion model and ensuring accurate distribution matching gradients during training. Additionally, to enrich guidance for the generative power, we incorporate textual prompts via image captioning as auxiliary conditions, fostering further exploration of the diffusion model. Extensive experiments substantiate the efficacy of our framework across a diverse array of challenging tasks and datasets, unveiling the compelling efficacy and efficiency of InstaRevive in delivering high-quality and visually appealing results.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper propose a one-step diffusion framework called InstaRevive which employs score-based diffusion distillation with dynamic noise control and dynamic loss control. Dynamic noise control is to control the max noise level during training according to the difference of LQ and GT, and the dynamic loss control is to adjust the loss weights of fidelity and distribution. Then, this paper verifies the effectiveness of the framework on several enhancement tasks and generally performs well.

### Strengths
1. This paper proposes a dynamic control method to constrain the optimization process according to the image distribution, which effectively improves the performance of the present method.
2. The writing of the article is good, making the whole article clear and easy to understand
3. This paper verifies the effectiveness of the method on some different enhancement tasks.

### Weaknesses
1. The paper does not mention some important pre-work (e.g., img2img-turbo and OSEDiff), which may exaggerate some contributions of this work. In fact, the methods (Reduce the steps by distillation) have been used before, and the proposed innovation core of this paper should be the dymic control.
2. Due to the lack of reference to some previous work, in the comparison of other methods in the article are not new enough. For example, the visual effects and quantitative results of OSEDiff, SUPIR should be included.
3. The ablation of dynamic control in the experiment shown in Figure 7 is not detailed enough. Because the main contribution is dynamic control, I suggest to draw two lines for the dynamic control of noise and the dynamic control of loss, instead of coupling them together, so that we can see which method is actually taking effect.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This method improves image enhancement by utilizing a distillation approach, which significantly reduces time and computational resources. It introduces a dynamic score matching framework that effectively guides models to generate realistic (using KL divergence) and well-resolved (using regression) images from low-quality inputs. Additionally, the method is adaptable to various applications beyond BFR and BSR, including style transfer, low-light enhancement, inpainting, and more.

### Strengths
1. "Introducing one-step restoration using diffusion models" is a compelling topic for researchers in the field of image processing.

2. The experimental results strongly support the authors' claims and demonstrate impressive restoration outcomes for real degraded images.

3. Dynamic score matching can be valuable for various distillation studies to address potential inaccuracies at large timesteps.

### Weaknesses
1. While the method demonstrates impressive results, my main concern is that recent diffusion-based image restoration methods primarily focus on a zero-shot approach. My concerns are as follows:

* The proposed method initially relies on a restorer, such as SwinIR-GAN, to enhance low-quality images. This approach implies that degradation types vary, requiring the model to use different restoration modules depending on the specific degradation family. This dependence on a pre-trained restorer limits the method's flexibility and introduces a potential bottleneck, as the quality of the final output is inherently tied to the performance of this initial stage. Furthermore, the need for a specific restorer for each degradation type adds complexity to the overall pipeline and may not be practical for real-world scenarios with diverse and unknown degradations.
* Additionally, the model is trained in a supervised manner using paired low-quality and high-quality datasets. This supervised training approach limits the model's ability to generalize to unseen degradation types and real-world scenarios where paired data is often unavailable. The reliance on paired data also introduces a potential bias, as the model may overfit to the specific characteristics of the training dataset, leading to suboptimal performance on out-of-distribution data.


2. More comparisons with the original restorer are needed.

* From my perspective, the initial restorer recovers most of the information, while the distilled model further refines it to appear more realistic. If this is the case, it is crucial to compare the method with the initial restorer, especially using traditional metrics like PSNR, SSIM, and LPIPS. However, most experimental results do not provide this comparison. The lack of such comparisons makes it difficult to assess the true contribution of the distilled model and whether the improvements justify the added complexity of the distillation process. A thorough comparison should include not only visual results but also quantitative metrics to provide a comprehensive evaluation.

### Questions
1. Why is it necessary to use a restorer-fused method rather than zero-shot diffusion-based restoration methods, such as DPS, PSLD, or GDP?

2. If possible, please provide additional comparisons with the restorer using traditional metrics.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
InstaRevive presents a novel and efficient approach to image enhancement, leveraging score-based diffusion models for impressive results. The framework introduces dynamic score matching to refine the training process and incorporates textual prompts for enhanced guidance. Experimental results demonstrate superior performance across various tasks, including blind face restoration and blind image super-resolution.

### Strengths
* **Clear and concise presentation:** The paper is well-structured and easy to follow, making the proposed method accessible to a wide audience.
* **Strong performance:** InstaRevive consistently outperforms baseline methods on challenging image enhancement tasks, highlighting its effectiveness.
* **Innovative approach:** The dynamic score matching technique and incorporation of textual prompts offer a unique and promising direction for image enhancement.

### Weaknesses
While the paper demonstrates excellent results on face restoration and image super-resolution, it would benefit from exploring its applicability to other degradation types, such as deraining, dehazing, deblurring, and salt and pepper noise.

The paper's focus on face cartoonization as an image-to-image translation task could be expanded to include other types of image-to-image translations, such as real image to real image translation. Furthermore, the current approach to face cartoonization appears to struggle with preserving facial identity, which is a significant limitation for practical applications where identity consistency is crucial.

### Questions
- How might InstaRevive need to be adapted to handle deblurring or dehazing tasks? Are there any particular challenges you foresee in extending the framework to these degradation types?

- Have you considered applying InstaRevive to style transfer tasks between real images? What modifications, if any, would be necessary to adapt the framework for tasks like day-to-night image conversion or season transfer?

### Soundness
3

### Presentation
4

### Contribution
3
