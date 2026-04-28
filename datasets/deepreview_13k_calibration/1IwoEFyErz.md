# Shallow Diffuse: Robust and Invisible Watermarking through Low-Dimensional Subspaces in Diffusion Models

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
The widespread use of AI-generated content from diffusion models has raised significant concerns regarding misinformation and copyright infringement. Watermarking is a crucial technique for identifying these AI-generated images and preventing their misuse. In this paper, we introduce \textit{Shallow Diffuse}, a new watermarking technique that embeds robust and invisible watermarks into diffusion model outputs. Unlike existing approaches that integrate watermarking throughout the entire diffusion sampling process, \textit{Shallow Diffuse} decouples these steps by leveraging the presence of a low-dimensional subspace in the image generation process. This method ensures that a substantial portion of the watermark lies in the null space of this subspace, effectively separating it from the image generation process. Our theoretical and empirical analyses show that this decoupling strategy greatly enhances the consistency of data generation and the detectability of the watermark. Extensive experiments further validate that our \textit{Shallow Diffuse} outperforms existing watermarking methods in terms of robustness and consistency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed Shallow Diffuse, a watermarking technique for diffusion models. The method is well-motivated and with proper theoretical justification. The proposed Shallow Diffuse has several key advantages compared to existing diffusion watermarks, 1) It is a training-free watermark but simultaneously maintains the consistency between watermarked and original images. 2) It is more robust than existing baselines, achieving nearly no performance drop under different robustness tests. Shallow Diffuse also considers two scenarios including the server (protect generated image) and user (protect existing image) scenarios for injecting the watermark.

### Strengths
1. Shallow Diffuse's primary strength lies in its utilization of the low-rank property of the PMP's Jacobian matrix to minimize the visual impact of watermarks, thereby attaining visual consistency within a training-free watermark framework.
2. The injected watermark is more robust against several image distortions than existing baselines.

### Weaknesses
1. The presentation of this paper is poor, for instance, the ablation studies (Appendix C) and index of experimental results (Table 4) are incomplete. Therefore, this leads to a shortage of critical ablation studies.
2. What is the performance of multi-key identification, specifically, is it possible for the Shallow Diffuse to inject multiple watermarks and distinguish between them?
3. The image distortions are less than that in previous studies, such as Tree-Ring, where they apply 6 distortions.
4. Can DiffPure purify the watermarked patterns?
5. The findings in Table 4 are confusing. It appears that employing channel averaging enhances robustness against image distortions. However, channel averaging involves averaging clean and watermarked images across specific channels. As per my understanding, this process might reduce watermark robustness. Can you explain this observation?

### Questions
Please see the weaknesses part.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a watermarking technique Shallow Diffuse. Unlike existing approaches that integrate watermarking throughout the entire diffusion sampling process,  Shallow Diffuse decouples these steps by leveraging the presence of a low-dimensional subspace in the image generation  process. This method ensures that a substantial portion of the watermark lies in the null space of this subspace,  effectively separating it from the image generation process.

### Strengths
The originality of this paper is not great, but its quality, clarity and significance are good. It has the support of rich theoretical basis and has advantages in theoretical proof.

### Weaknesses
The originality of this paper is not great, but its quality, clarity and significance are good. It has the support of rich theoretical basis and has advantages in theoretical proof.

The table in the paper is not very well drawn, it is very difficult to read, especially the header. At the same time, the experimental part is not detailed enough. For example, should the comparison method reproduce the results or use the pre-training model?

In Table 1, for the CLIP-Score index, yours is 0.3285, which seems to be the worst. Please explain further.

Please explain why the filter size in the Gaussian blurring is 8 × 8 and how the standard deviation is selected.

As can be seen from Table 2, the PSNR and SSIM of most methods are very low, so it is easy for human eyes to find modification traces, which easily leads to the risk of watermarked images being maliciously broken. Please further explain the visual quality of the generated watermarked image.

### Questions
1. The table in the paper is very difficult to read clearly.

2. In Table 1, for the CLIP-Score index, yours is 0.3285, which seems to be the worst. Please explain further.

3. Please explain why the filter size in the Gaussian blurring is 8 × 8 and how the standard deviation is selected.

4. As can be seen from Table 2, the PSNR and SSIM of most methods are very low, so it is easy for human eyes to find modification traces, which easily leads to the risk of watermarked images being maliciously broken. Please further explain the visual quality of the generated watermarked image.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposed a new image watermarking method that embeds a watermark into the null space of a specific step during image denoising in diffusion model. It shows that the proposed watermarking method have smaller impact on the generated images compared to the existing methods like Stable Signature and Tree-Ring. Additionally, the proposed method shows good robustness to image processing methods like JPEG and Gaussian blur.

### Strengths
1. The proposed method has smaller impact on the generated images compared to the existing watermarking methods designed for diffusion models.
2. Experiments are carried on several image-prompt datasets to show the effectiveness of the proposed methods.
3. The robustness of the propsoed method is evaluated.

### Weaknesses
1. Compared to Tree-Ring, the technical contribution of the proposed method is limited.
2. In the experimental part, the authors mainly compare their method with the watermarking methods that embed watermark into the semantic space like Tree-Ring which changes the image a lot. More other watermarking methods should be evaluated.
3. In the robustness part, the authors only evaluate the robustness of the proposed method on some common perturbation.

### Questions
1. Besides Tree-Ring and Stable Signature, I think there are more existing watermarking methods that introduce small perturbation to the image to embed watermark, like StegaStamp. To show the proposed method actually preserves image quality, I think the authors should compare the method with some watermarking methods that watermark the image after image generation with a small perturbation.
2. In the robustness part, I think the regeneration attacks and some adversarial perturbation should be evaluated on the proposed method to see whether the proposed method is actually robust under various attacks.
3. Since the authors mention the user scenario, if multiple users rewatermark the same image with the proposed method, can the watermark embeded by the specific user be detected in this circumstance?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Current watermarking techniques based on diffusion models often embed watermarks directly into the initial noise，which can alter the data distribution. This paper proposes "Shallow Diffuse," a method that disentangles the watermark embedding from the generation process by leveraging low-dimensional subspaces. This approach supports watermark embedding for both server-side and user-side applications while maintaining high robustness and consistency. Additionally, experiments were designed to validate robustness and conduct ablation studies across multiple datasets.

### Strengths
1. The method utilizes the local linearity of low-dimensional subspaces. As a watermarking method based on diffusion models, it maintains the consistency of generated images.

2. This paper provides rigorous theoretical proof and presents a substantial number of computational formulas.

### Weaknesses
1. The attack experiments are limited, consisting of only four fixed-parameter attacks, which do not demonstrate the method's robustness. For instance, the method can be viewed as a variant of treering, could experiments with additional attacks, such as rotation、regeneration be included?

2. The theoretical assumptions of the method are built upon [1], but the experimental results yield a different range of t values compared to the theoretical analysis in [1]. Although this can be explained by the errors introduced by DDIM-Inv, it remains perplexing.

3. The method relies on the properties of DDIM and DDIM-inverse, which may lack certain generalizability. It might not perform well for attacks executed in the latent space.

### Questions
1. Shouldn't the formula $\hat{\boldsymbol{x}}_{0, t}:=\boldsymbol{f}_{\boldsymbol{\theta}, t}\left(\boldsymbol{x}_{t}+\lambda \Delta \boldsymbol{x}\right)$ on line 360 be  $\hat{\boldsymbol{x}}_{0, t}:=\boldsymbol{f}_{\boldsymbol{\theta}, t}\left(\boldsymbol{x}_{t}\right)$

2. Could you specify the parameters used in the Shallow Diffuse method in Section 5, such as the embedding channels and watermark radius?

3. The experiments in Appendix C only provide results, could you include some analysis?

### Soundness
2

### Presentation
2

### Contribution
2
