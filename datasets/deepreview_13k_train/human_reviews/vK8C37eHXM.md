# Sample what you can't compress

- Decision: Reject
- Scores: 6, 3, 1, 3, 3

## Abstract
For learned image representations, basic autoencoders often produce blurry results. Reconstruction quality can be improved by incorporating additional penalties such as adversarial (GAN) and perceptual losses. Arguably, these approaches lack a principled interpretation. Concurrently, in generative settings diffusion has demonstrated a remarkable ability to create crisp, high quality results and has solid theoretical underpinnings (from variational inference to direct study as the Fisher Divergence). Our work combines autoencoder representation learning with diffusion and is, to our knowledge, the first to demonstrate  jointly learning
a continuous encoder and decoder under a diffusion-based loss
and showing that it can lead to higher compression and better generation.. 
We demonstrate that this approach yields better reconstruction quality as compared to GAN-based
autoencoders while being easier to tune. 
We also show that the resulting representation is easier to model
with a latent diffusion model as compared to the representation obtained from a state-of-the-art GAN-based loss.
Since our decoder is stochastic, it can generate details not encoded in the otherwise deterministic latent representation; we therefore name our approach ``Sample what you can't compress'', or SWYCC for short.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work adds a diffusion loss to the autoencoder training and shows better reconstructoin quality than the prior GAN-based autoencoder. Specifically, the proposed method first has a coarse reconstruction, that is supervised by MSE and LPIPS loss, then a diffusion model refines the coarse reconstruction (jointly trained). The authors show improvement for both reconstruction in different compression rates and generation.

### Strengths
**Update after rebuttal:**

```
The authors have addressed my questions. I agree with other reviewers that more visual samples and discussions about related works can be helpful. I will keep my rating as this work shows promising results for the strength of diffusion autoencoders for general images.
```

---


1. Diffusion loss for autoencoder training is an important direction to explore. This work is one of the first works that show promising results.
2. The proposed method outperforms prior GAN-based autoencoder on ImageNet with common metrics CMMD and FID. The trend of compression ratio also shows the advantage of the diffusion loss.
3. The variance visualization is interesting and provides more insights about the what information are sampled.

### Weaknesses
1. The 2-stage pipeline makes the propose method a bit less compelling. The autoencoder is still supervised by MSE + LPIPS loss while the diffusion loss is more like for refinement (although it is joint training).
2. The authors claim that the coarse reconstruction is just for speeding-up the training as the diffusion decoder "should converge to true distribution" (L209), I did not find in the paper for neither: (i) experiments that show without LPIPS loss, the model converges to similar performance; (ii) a theory that guarantees autoencoder with only diffusion loss learns similar representation as LPIPS autoencoder. The theory of diffusion models guarantees p(x|z) can be correctly modeled, but LPIPS should have impact on the latent representation z and thus may change the distribution p(x|z). Thus the claim is not well-justified to me.
3. It would be better to have more qualitative visual comparisons. For example, for different compression rates, and with more diverse samples, to justify the improvement of the proposed method. FID may be overly-related to the LPIPS weight.

### Questions
What are the number of trainable parameters for the baseline GAN-based method and the proposed method? Is the baseline GAN autoencoder retrained on the same setting? It would be helpful to provide more details about the baseline method.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a diffusion-based loss for improving the quality of VAE modeling and reconstruction. The authors proposed the new VAE decoder that consists of two main parts, including a Diffusion UNet. The training was conducted with additional diffusion loss. The proposed model was compared with GAN-based loss methods and the authors demonstrate that proposed method yields better results, especially at higher compression rates. Additionally the authors emphasize the importance if the decoder's stochasticity for better details in generated samples.

### Strengths
1. The authors provide full explanation of technical detail, including all architecture details and training process. 

2. Wide and well-explained ablation studies was conducted to explore the importance of various components of the model. The experiments devoted to exploration of number of denoising steps and cfg sclaes helps to understand the importance of correct choice of these parameters for quality improvements.

### Weaknesses
1.There is lack of sufficient metrics for evaluation. It would be better to provide some editional metrics calculation such as LPIPS (https://richzhang.github.io/PerceptualSimilarity/) or Inception Score (https://arxiv.org/abs/1606.03498).
2. Furthermore the authors provided limited evaluation datasets and comparison models. Additional comparisons with some state-of-the-art methods, such as DC-VAE (https://arxiv.org/pdf/2011.10063) or VAEBM (https://arxiv.org/abs/2010.00654) on some other datasets, such as LSUN (https://arxiv.org/abs/1506.03365) or CelebA-HQ-256  , would provide a better understanding of the quality of the model.
3. Only low-resolution data. Conducting further experiments with higher resolution images would be beneficial to understand the capabilities of the model.
4. The suggested decoder of the model consists of two main parts, including the additional UNet. Is it possible that your method provides better results because it utilizes a larger model?

### Questions
1. It might be important to mention “DiffuseVAE: Efficient, Controllable and High-Fidelity Generation from Low-Dimensional Latents” paper? Could you explain the main difference between this work and your approach? Is it possible to compare your model to DiffuseVae?

2. Is it necessary to train the UNet? Is it possible to use a pre-trained diffusion model without additional training in the refinement part?

3. Nowadays it is important to be able to work with high-resolution images. Can you scale your method to produce high-resolution images?

4. The suggested decoder of the model consists of two main parts, including the additional UNet. Is it possible that your method provides better results because it utilizes a larger model?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
In this paper, the authors propose to use a U-Net to further refine the results of the traditional discriminative autoencoders to alleviate the blury output and get crisp and high quality results. Experiments show that the method does improve the visual appearance of the reconstructed images.

### Strengths
Adding an additional U-Net and using diffusion model to improve the performance is promising, it should be able to get better results.

### Weaknesses
- What's the difference between the proposed method and those utilizing diffusion models for super resolution? I cannot see a big difference. It appears that the method is using a diffusion model to refine an initial reconstruction, which is conceptually similar to how diffusion models are used for super-resolution, where a low-resolution image is upsampled and refined. The core idea of iterative refinement using a learned model is shared between these two approaches, and the paper does not sufficiently highlight the novelty of the proposed method in this context.
- Yet the training method is not well explained, do you need to train $E$ and $D_{Initial}$? Or just $D_{refine}$ is trained? The training procedure for the different components of the model is unclear. Specifically, it is not specified whether the encoder ($E$) and the initial decoder ($D_{Initial}$) are trained jointly with the refinement decoder ($D_{refine}$), or if they are pre-trained and then frozen. The lack of clarity on this point makes it difficult to understand the overall training strategy and how the different parts of the model interact.
- In Sec. 3.1, it is said that the impact of $D_{Initial}$ is investigated in Table 1, which is not. The paper claims that the impact of the initial decoder ($D_{Initial}$) is analyzed in Table 1, but this table does not provide any specific information about the role or effect of $D_{Initial}$. This discrepancy between the text and the table makes it difficult to evaluate the contribution of $D_{Initial}$ to the overall performance of the model.
- When displaying the reconstruction results, the raw inputs are necessary to see the difference. The reconstruction results are shown without the corresponding raw inputs, making it difficult to assess the quality of the reconstruction. Without the raw inputs, it is impossible to determine how much the proposed method improves the visual quality of the images.
- Besides the figures, more quantitative metrics are necessary to justify the method. The paper relies mainly on visual inspection to evaluate the performance of the proposed method. While visual inspection is important, it is not sufficient to justify the method. More quantitative metrics, such as PSNR, SSIM, or LPIPS, are necessary to provide a more objective evaluation of the method.

### Questions
- Overall, the method is trivial and cannot match the high standard of ICLR.
- This is more like an unfinished paper.
- The footnote leaks part of the author information.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents SWYCC, a VAE trained with diffusion loss. It optimizes performance by adjusting loss weights and sampling steps. The authors then compare it to VQGAN-based methods, demonstrating improved image reconstruction.

### Strengths
- The paper provides extensive detail on the architectural design of SWYCC, including the detail structure of the encoder and decoder. However, while this information is valuable for understanding the framework, it is not the primary contribution of the paper and does not introduce novel architectural concepts.
    
- The inclusion of a classifier-free guidance experiment is a notable strength, as this approach introduces a new aspect to the diffusion-based decoder. However, it is important to note that the classifier-free technique employed significantly increases computation time during the sampling stage, effectively doubling it, which also poses challenges in practical applications.

### Weaknesses
 - The paper provides extensive detail on the architectural design of SWYCC, including the detail structure of the encoder and decoder. However, while this information is valuable for understanding the framework, it is not the primary contribution of the paper and does not introduce novel architectural concepts.
    
- The inclusion of a classifier-free guidance experiment is a notable strength, as this approach introduces a new aspect to the diffusion-based decoder. However, it is important to note that the classifier-free technique employed significantly increases computation time during the sampling stage, effectively doubling it, which also poses challenges in practical applications.

- The paper includes too few image comparisons. It does not show many comparisons between different model compressions, making it difficult to evaluate how SWYCC stands relative to other approaches.
    
- There is no comparison with Stable Diffusion XL's VAE, which is one of the widely used VAE models.
    
- The method relies solely on matrices for image generation, which is not common in image reconstruction compression. While it is acceptable for the authors to report measurements they find appropriate, it is also important to include other widely used metrics in the field, such as PSNR, LPIPS, and rFID.
    
- The paper lacks mention and discussion of previous diffusion-based autoencoders, such as DiffusionAE and DiVAE. Care should be taken not to claim to be the first when there are multiple works prior to this.
    
- Training the decoder under diffusion loss is a concept introduced in 2022. Although the idea of using diffusion as a decoder has been recognized for its benefits, it has not gained popularity compared to GAN-based training primarily due to its higher computational cost. This concern is not adequately addressed in the paper.

### Questions
- What does "favorable Hessian" mean? It doesn't seem to relate to MSE.
- How does this approach differ from fine-tuning a standard VAE and using diffusion for upscaling?
- How does "speed up training" be versify?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes to use a diffusion model for image compression. Specifically, the diffusion model is an encoder-decoder architecture, where the encoder encodes the given clean image, and the decoder generates a high-quality image from pure noise (as in standard diffusion methods) while being conditioned on the encoded image. The encoder and the decoder are trained jointly using the standard MSE diffusion loss, together with some tweaks such as adding a perceptual loss after an intermediate decoding step.

### Strengths
1. The proposed approach for image compression is simple and effective. It makes sense that it should work better than GAN based methods, as diffusion models beat GANs in many different applications. GANs are indeed incredibly difficult to train.
2. The paper is overall clear and written well.
3. There are several ablation studies.

### Weaknesses
1. As far as I understand, the proposed approach is not novel. See [1] for example. The only differences that I see are some optimization/loss tweaks. If the authors could clarify the differences and why their approach is novel, that would be great. Currently, [1] is not discussed in the manuscript.

2. A comparison with several previous methods is missing, specifically a comparison on the rate-perception-distortion plane [2]. When designing compression methods that only aim for minimal distortion (e.g., MSE), we usually compare them on the rate-distortion plane, as the authors did in figure 8. However, when designing high-perceptual-quality compression methods, we usually compare them on the rate-perception-distortion plane, as these three desired forces are at odds with each other [2].

3. The authors only demonstrate their method on ImageNet. But what about simpler data sets, such as CelebA,CIFAR, etc.? Is the proposed approach still more effective than GANs?

4. The limitations section is very limited. The authors discuss only the limitation of almost all diffusion methods: requiring a large number of inference steps to produce high-quality images. What about model size, training time, required data set size, etc., as compared to GAN based methods?

### Questions
1. Can the authors please explain the differences between the proposed approach and [1]?
2. Can the authors explain why there is no comparison with additional methods, and in particular why there is no comparison on the rate-perception-distortion plane [2]?


[1] Konpat Preechakul et al., "Diffusion Autoencoders: Toward a Meaningful and Decodable Representation", CVPR 2022.

[2] Yochai Blau and Tomer Michaeli, "Rethinking Lossy Compression: The Rate-Distortion-Perception Tradeoff", ICML 2021

### Soundness
2

### Presentation
2

### Contribution
2
