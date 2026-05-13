# AdvI2I: Adversarial Image Attack on Image-to-Image Diffusion models

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Recent advances in diffusion models have significantly enhanced the quality of image synthesis, yet they have also introduced serious safety concerns, particularly the generation of Not Safe for Work (NSFW) content. Previous research has demonstrated that adversarial prompts can be used to generate NSFW content. However, such adversarial text prompts are often easily detectable by text-based filters, limiting their efficacy. In this paper, we expose a previously overlooked vulnerability: adversarial image attacks targeting Image-to-Image (I2I) diffusion models. We propose AdvI2I, a novel framework that manipulates input images to induce diffusion models to generate NSFW content. By optimizing a generator to craft adversarial images, AdvI2I circumvents existing defense mechanisms, such as Safe Latent Diffusion (SLD), without altering the text prompts. Furthermore, we introduce AdvI2I-Adaptive, an enhanced version that adapts to potential countermeasures and minimizes the resemblance between adversarial images and NSFW concept embeddings, making the attack more resilient against defenses. Through extensive experiments, we demonstrate that both AdvI2I and AdvI2I-Adaptive can effectively bypass current safeguards, highlighting the urgent need for stronger security measures to address the misuse of I2I diffusion models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces AdvI2I, a framework that performs adversarial image attacks on image-to-image (I2I) diffusion models to generate NSFW content without modifying text prompts. It further proposes AdvI2I-Adaptive, which incorporates techniques to minimize resemblance to NSFW embeddings, enhancing robustness against conventional defenses. Extensive experiments demonstrate AdvI2I’s ability to bypass common safeguards in I2I models, signaling potential safety concerns and underscoring the need for improved defense mechanisms.

### Strengths
1. This paper expands the field of adversarial attacks in I2I diffusion models by targeting image conditioning rather than the commonly used text prompts.

2. The structure and explanations are well-organized, with a clear presentation.

### Weaknesses
1. The paper’s evaluation is limited to SDv1.5-Inpainting and InstructPix2Pix, both based on the SDv1.5 architecture. Expanding the analysis to include more advanced versions of Stable Diffusion or other models(not just in the transferability section) would enhance the assessment of AdvI2I’s generalization to state-of-the-art diffusion models.

2. The paper does not examine how varying benign prompts, including explicitly defensive ones that request safe content, might affect the success of the adversarial attack. Investigating whether different benign prompts, especially those aimed at reinforcing safe content, influence the attack's efficacy would offer a more comprehensive understanding of its generalization and robustness across diverse input conditions.

3. The results suggest reduced transferability of AdvI2I from SDv1.5 to SDv3.0, indicating that its effectiveness may be architecture-specific, potentially limiting the framework’s generalizability.

4. Since AdvI2I relies on adversarial noise as a primary mechanism, it would be beneficial to explore potential defense strategies beyond the current scope, such as DiffPure[1], to counteract adversarial image attacks more effectively.

[1] Diffusion models for adversarial purification.

### Questions
Please refer to the weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed a framework that can bypass safety check of NSFW generations by modifying the image input. It first points out the problems of previous prompt attacks to bypass NSFW checks, then it proposes to add noise to images to bypass the safety checker, which will make the attack more stealthy. The authors design a pipeline with some key design choices e.g. NSFW concept vector extraction, use a universal noise generator to avoid repeated generation. The paper is mostly well-written and easy to follow, the experiments are comprehensive and show that it is better than baseline methods.

### Strengths
- The paper is well-written and easy to follow.
- It revisits current prompt attacks and show critical insights that they can be easily defended.
- Based on the idea of concept vector extraction. The proposed novel pipeline is well-designed and effective, which shows strong performance compared with baseline methods. Also, the proposed pipeline is learning-based and can be used as one-pass noise generator.

### Weaknesses
Clarification:
- This paper is working with I2I diffusion models, which have additional encoded visual inputs as condition. The targeted I2I model is (1) different from the T2I diffusion models used in previous works (2) is not as good as popular T2I models e.g. SD-XL, FLUX. It poses challenges on the motivation of this paper, because the I2I model used in this paper is a sub-optimal choice if the malicious users want to generate high quality NSFW images.

Methods:
- The proposed method is restricted to a small subset of I2I models, which are not the main part of diffusion models.
- The choice of noise generator may not be optimal, ad-hoc noise generation for each image is also not that time-consuming e.g. sample timestep t and optimize for 100 steps takes for e.g. 1 min. It may show much stronger performance.


Adaptive Attack:
- The adaptive-attack assumes the white-box setting of the NSFW-detector, which may not be pratical.
- Some other defenses e.g. add noise / use purifier to remove the noise deserves more study.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper explores bypassing safety checkers of image editing models to generate NSFW content, using adversarial images.

The authors first show that previous methods using adversarial prompt are easily detectable, and then propose AdvI2I - that train a network $g_{\psi}$ to perturb image.

When this perturbed image is used with a neutral prompt as input for an img2img or inpainting model, it can influence the generation process, to generate some specific NSFW concept (nudity/violence).

To do so, AdvI2I slightly modify (perturb) the image, so that its latent after denoising with a neutral prompt, is close to the original image's latent but denoising with a NSFW prompt.

The authors also propose AdvI2I-Adaptive, that incorporate safety checker loss and added Gaussian noise augmentation when training $g_{\psi}$. It helps improving robustness when gaussian noise is added to the perturbed image, and AdvI2I-Adaptive also improves the bypass success rate over the posthoc safety checker.

Experiments were conducted on SDv1.5-Inpainting and InstructPix2Pix, with high success rate against Safe Latent Diffusion, Negative Prompt, added Gaussian Noise and the Safety checker. AdvI2I also shows transferability from SDv1.5 to SDv2.0 and v2.1 but not effective when test with SDv3.0.

### Strengths
While bypassing content filtering using adversarial images was proposed in MMA Diffusion, the method the author uses to quickly craft an adversarial image without optimization is a new contribution. The objective for training $g_{\psi}$ is also novel, and selecting components like which UNet or VAE to train, or the diffusion step to optimize, requires trial and error efforts. 

Both AdvI2I and AdvI2I-Adaptive show good results, and the success rate against the safety checker is strong. I’m also pleased with the included transferability test with SD2x and 3.

### Weaknesses
Experiments: Below are some experiments that the author can address to have a comprehensive view about AdvI2I
- Insufficient highlight the contribution of $g_{\psi}$, can add run time comparison with optimization approach
- SDXL-Turbo Image-to-Image transferability test, as it also uses the same VAE.
- Transferability test with recent models not just SD3.0, such as Pixart Alpha, Flux

Writing: The writing needs improvement. Please address these points:
- L070 confusing since there is no encoder
- L11 in algorithm 1 - $C_i$ and $M$ was not mentioned in require. Also the loss is cosine between a vector $C_i$ and output of $\mathcal{D}$ which I assume is an image, does it need an image encoder to turn it into a vector there, if so then what encoder?
- SLD Configuration - lacks details on the configuration that was used, is it Max/Strong/Medium?
- Clarify: prompts generated by gpt4-o are pair prompts or single prompt?
- Typo L607 - InstructionPix2Pix - InstructPix2Pix

### Questions
- **important** Can AdvI2I method apply for good use, like changing the target concept to e.g clothes (instead of NSFW/violence), so that $g_{\psi}$ now become a protection to help mitigate inappropriate image editing? Its application will be more like photoguard and faster, also only restrict on inappropriate editing
- How performance of AdvI2I vary, based on the neutral prompt. Specifically, given a perturbed image with prompt that specific mention e.g clothes, like "A photo of a girl in a beautiful dress" , can it still generate NSFW image?
- What hardware and how long to train AdvI2I?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a adversarial image attack framework that injects adversarial information into images rather than text prompts, inducing Image2Image Diffusion to generate NSFW content, therefore it has some novelty. However, the motivation is not clear, and the evaluation is not enough. Overall, my main concern is the insufficient evaluation, if the author can solve my concerns, I would be happy to change the rating.

### Strengths
1. The paper shows that the prompt-based attack can be simply defenced by some filters
2. This paper proposes a new framework which solely based on perturbating images to induce NSFW content. It can be regarded as the knowledge distillation of adversarial text prompt that could induce NFSW contents to image embedding. the proposed method can bypass these methods as the adversarial information is hidden in the images, i.e., the text prompt will not have and malign information.

### Weaknesses
1. The motivation is not clear. See Q1
2. lack of evaluations, e.g., IQAs, face verification rate. See Q2, 3, 4, 5

### Questions
1. The motivation is not clear. There are a lot of existing methods that could easily generate NFSW images such as deepnude, or I can just use the deepfake to swap face of a porn image with the clean image, why people will trouble themselves to use this method? Are the NSFW images generated by your method have higher image quality? If so, I would expect the authors to clarify how their method compares to or improves upon existing NSFW image generation techniques like deepnude or deepfake. More details see Q2.
2. Are the images generated with the proposed method of significant high quality comparing with previous methods? The quality of generated NSFW images should be evaluated by some IQAs:
    If my understanding is correct, the objective is to generate nude images which have same indentity as the clean image (i.e.com the target is a category of images rather than a certain image), FR IQAs may not work well. I would suggest to use some NR IQAs (FID, TOPIQ, etc). It is worth noting that, if the data volume is lower than 10k, the FID may not be meaningful.
3. The author did not compare IQAs with other baselines for clean and attacked images, i.e., we do not know if the perturbation is imperceptible enough. (I would suggest compare the PSNR, LPIPS, SSIM, etc between clean image and attacked image). I would expect a table comparing these metrics between the clean and attacked images for their method and baseline methods.
4. Will the generated NSFW images have same identity with clean images (especially for nude images)? I suggest the author to use several face verification methods or metrics to quantify identity preservation in their generated images.
5. The performance of AdvI2I against SC is poor, although the author admits this, and implement an adaptive version, I need to see more transferability evaluations, i.e., the author should demonstrate the ASR for SC_2 given "adversarial samples generated by adaptive AdvI2I with SC_1".
    I suggest the author to provide a table showing ASR results for different combinations of safety checkers (SC_1, SC_2, etc.) used during training and testing of their adaptive AdvI2I method.

### Soundness
2

### Presentation
2

### Contribution
2
