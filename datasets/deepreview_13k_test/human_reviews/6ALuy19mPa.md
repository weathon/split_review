# DreamClean: Restoring Clean Image Using Deep Diffusion Prior

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
Image restoration poses a garners substantial interest due to the exponential surge in demands for recovering high-quality images from diverse mobile camera devices, adverse lighting conditions, suboptimal shooting environments, and frequent image compression for efficient transmission purposes. Yet this problem gathers significant challenges as people are blind to the type of restoration the images suffer, which, is usually the case in real-day scenarios and is most urgent to solve for this field. Current research, however, heavily relies on prior knowledge of the restoration type, either explicitly through rules or implicitly through the availability of degraded-clean image pairs to define the restoration process, and consumes considerable effort to collect image pairs of vast degradation types. This paper introduces DreamClean, a training-free method that needs no degradation prior knowledge but yields high-fidelity and generality towards various types of image degradation. DreamClean embeds the degraded image back to the latent of pre-trained diffusion models and re-sample it through a carefully designed diffusion process that mimics those generating clean images. Thanks to the rich image prior in diffusion models and our novel Variance Preservation Sampling (VPS) technique, DreamClean manages to handle various different degradation types at one time and reaches far more satisfied final quality than previous competitors. DreamClean relies on elegant theoretical supports to assure its convergence to clean image when VPS has appropriate parameters, and also enjoys superior experimental performance over various challenging tasks that could be overwhelming for previous methods when degradation prior is unavailable.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents DreamClean, a training-free method for high-fidelity image restoration without prior knowledge of degradation. DreamClean embeds the degraded image into pre-trained diffusion models, uses Variance Preservation Sampling (VPS), and outperforms previous methods, especially in challenging tasks without degradation priors.

### Strengths
1. The innovation is impressive, providing a fresh perspective on the field of image restoration。

### Weaknesses
1. Insufficient experiments. The performance needs to be tested on a broader range of real-world degradation data. The data used in the paper are all synthetic, which lacks convincing power.
2. The methods for comparison are insufficient. For example, other training-free methods like 'Generative Diffusion Prior for Unified Image Restoration and Enhancement' are also available.

### Questions
Refer to weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a novel unsupervised diffusion based approach called DreamClean, which does not rely on specific degradation types, for Image Restoration tasks. The superiority lies in restoring clean images without specific finetuning or assuming known degradation. Specifically, DreamClean exploits the approximately inversible property of DDIM to ensure faithfulness. For realness, the paper introduces Variance Preservation Sampling (VPS) to guide latents to nearby high probability region which conforms statistics of the pretrained diffusion model to produce high-quality images. The paper gives a solid theoretical support for the convergence of VPS. The experiments and analysis are sufficient and the results seems promising.

### Strengths
- The paper gives a simple but insightful conclusion for the existing IR methods and points out the advantage of unsupervised method for generalization. Based on this, DreamClean is proposed to mitigate the reliance on the underlying degradation model or data-specific finetuning, which is critical to improve the generalization and the practical. 
- DreamClean can improve image quality using pre-trained diffusion models without finetuning or assuming specific degradation formulation. This method fills this gap in IR field. The results on various degradation types and latent diffusion model seems to support its strong robustness. 
- The analysis of the paper is mathematically complete. The paper constructs a high probability set according to the diffusion’s statistical characteristic and proves that latents will converge to the high probability set under VPS. This perspective is interesting and novel.
- The experiments are sufficient enough to support the claims and the results are promising. In particular, the result in Figure 1 has much higher visual quality compared with previous methods. The paper validates the efficacy on various IR tasks including single and multiple degradation cases, and well compatibility with latent diffusion models.

### Weaknesses
- The proposed method leverages ODE inversion to ensure faithfulness with motivation that ODE can approximately reconstruct the input image. Given that, why is ODE inversion needed rather than directly conduct VPS on the input image y?
- The authors should explain the reason that fresh noise is need in VPS. In other words, without the noise, VPS returns latents with locally maximal probability density. Why do higher-density latents perform inferior compared to latents with noise?

### Questions
- In section 3.2, the authors should give a more detailed interpretation about  log⁡(q(x_t |x_0)) can be alternative score for log⁡(p_θ (x_t)).

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper works on unsupervised image restoration using the pre-trained diffusion models as deep diffusion prior. It relaxes the linear degradation model and extends to non-linear and bad weather degradation. The faithfulness of the image restoration is achieved via the rich image prior embedded in the pre-trained models and DDIM inversion. The realness is satisfied through the proposed variance preservation sampling, where the latents are driving to the high probability set. Experiments for classical super-resolution, deblurring, colorization, non-align JPEG compression, and bad weather restoration show the effectiveness of the proposed method.

### Strengths
- The paper works on an important problem: unsupervised image restoration.
- The paper proposes a method to drive the latent variables to a high probability set to generate high-quality restoration results and provide theatrical analysis.
- The proposed method generalizes to non-linear degradation and bad weather as well as applies to diffusion models with latent space, e.g., Stable Diffusion.
- Well written and easy to follow.

### Weaknesses
- For the proposed variance preservation sampling (VPS), the latent variables fall into the high probability set with a strong assumption that $M$ is sufficiently large (Theorem 2.2). However, $M$ is empirically set to $1$ in this paper, and there is no detailed discussion about this important parameter.
- The qualitative results are only shown for the proposed method, and there are no visual comparisons to existing methods.
- For the bad weather degradation, there are no quantitative measurements. The only evidence is a set of visual examples in Fig. 2.
- The ablation study is only conducted on one type of degradation and is insufficient.
- The paper should discuss and compare with more recent blind image restoration works, e.g., GDP.

Fei, Ben, et al. "Generative Diffusion Prior for Unified Image Restoration and Enhancement." CVPR. 2023.

### Questions
- Is the proposed method sensitive to some parameters, e.g., $\gamma$ and strength?
- The paper should give more visual illustrations for the sampling algorithm of different timesteps to understand the effectiveness of the two steps in the proposed VPS.
- For the bad weather, the training of diffusion models often encounters such images in high image quality. It is not evident that the images with bad weather are categorized as degenerated or clean from the perspective of the diffusion prior.
- The authors should provide more implementation details.
- It is better to explain $x$ and $y$ in Fig. 2.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel generic image restoration (IR) approach called DreamClean that recovers degraded images back to high-quality reconstructed images without heavily relying on or knowing degraded models. The DreamClean method consists of two essential steps to restore corrupt images (e.g., noisy images, low-resolution images, or artifacts generated by JPEG compression)to the reconstructed images. First, the method utilizes a pre-trained diffusion model to encode the corrupt image images to latent embeddings in the diffusion models. The paper then presents a novel sampling strategy, Variance Preservation Sampling (VPS), mimicking a process of generating clean images to guide low-probability latent toward nearby high-probability regions for high-quality image synthesis. The contribution of this paper is threefold: 1. the paper introduces a novel aspect of restoring clean images without knowing prior degraded model information. The proposed method could be an IR technique for image restoration applications with variations of camera devices. 2. the proposed method could be generalized to diverse degraded images without training multiple neural network models. 3. the paper evaluates the proposed method on multiple datasets and types of degraded images. The experiment shows DreamClean achieves competitive quantitative results compared with other IR methods.

### Strengths
The strengths of this paper are as follows:

1. This paper proposes a generic IR method that can tackle corrupt images generated by variations of degraded models without training multiple network models. The paper provides theoretical and empirical proof to demonstrate the DreamClean method can synthesize high-quality clean images given the corrupt images.

2. The paper proposed a novel sampling strategy, the VPS method, in diffusion-based models to improve the chance of yielding clean images. The paper demonstrates the capability of VPS through theoretical proof and empirical results. The experimentation shows that DeamClean achieves higher quantitative results under different image quality metrics.

3. This paper contains comprehensive quantitative results on image quality comparisons for distinct IR methods. The DreamClean method outperforms other methods on most degraded models on different datasets.

### Weaknesses
This paper contains two weaknesses in terms of the proposed method:

1. The DreamClean method can synthesize clean images given the corrupt images; however, the proposed method does not consider consistency between the corrupt images and the reconstructed clean images due to a lack of prior degraded models. The proposed method can fail some restored images by synthesizing unexpected clean images.

2. The proposed method utilizes the pre-trained diffusion model on a particular large-scale dataset (i.e., ImageNet) to embed the corrupt images to the latent embeddings. Then, the method applies VPS to sample clean images during the sampling phase in diffusion models. Due to using the pre-trained model, the proposed method can generate unexpected images.

### Questions
There is a question I would like to ask to clarify all doubts in the paper:

1. In section 3.3, which is quantitative experiments, the paper uses 100 NFEs rather than a configuration in the original paper for DDRM. Does it affect the quantitative comparisons because 100 NFEs may not be the configuration for DDRM?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
