# Lossy Compression with Pretrained Diffusion Models

- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
We apply Theis et al. (2022)'s DiffC algorithm to Stable Diffusion 1.5, 2.1, XL, and and Flux-dev, and demonstrate that these pretrained models are remarkably capable lossy image compressors. A principled algorithm for compression using pretrained diffusion models has been understood since at least 2020 (Ho et al.), but challenges in reverse-channel coding have prevented such algorithms from ever being fully implemented. We introduce simple workarounds that lead to the first complete implementation of DiffC, which is capable of compressing and decompressing images using Stable Diffusion in under 10 seconds. Despite requiring no additional training, our method is competitive with other state-of-the-art generative compression methods at low ultra-low bitrates.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This submission presents a set of lossy compression method based on DiffC, with pretrained StableDiffusion1.5,2.1, and XL. To enable this utilization, a solution to the reverse-channel coding problem is proposed. This submission is also the first one to publicly release an implementation of the DiffC algorithm.

### Strengths
The paper implemented the SOTA stable diffusion for single image compression usage, and also released an implementation of DiffC to the public.

### Weaknesses
First, I don't think the main contribution is significant. The major idea had already been proposed several years ago. 
Second, I failed to find the comparisons of this idea with other SOTA image compression methods.

### Questions
Could you present the comparisons of this idea with other SOTA image compression methods?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper aims to solve the reverse channel coding remaining in DiffC and to accelerate the diffusion-based compression method under 10 seconds without additional training.

### Strengths
Originality: The authors try their best to implement the DiffC and apply it to existing pre-trained diffusion models, such as Stable Diffusion 1.5, 2, and XL. In addition, they propose a greedy optimization technique to speed up the diffusion process and to select the best denoising timestep schedule.

Quality: The manuscript is well organized and written.

Clarity: The authors have explained their method in detail.

Significance: The significance of this work is profound because it addresses the remaining problems in the DiffC algorithm, such as inference time and reverse-channel coding.

### Weaknesses
(1)The manuscript looks more like a technology report than an academic paper.

(2)The authors do not provide quantitative comparisons with state-of-the-art extreme image compression methods (VQ-based methods, diffusion-based methods) and show the advantages of the proposed method.  

(3) Although the main contribution of the paper is the implementation of the DiffC algorithm, the author should provide the model complexity of the proposed method (e.g., network parameters, FLOPs, encoding/decoding time, etc.).

### Questions
In Section 4.1, the prompts do not support image compression or reconstruction. This result contradicts many previous prompt-guided image compression methods. The author should add more analysis and explain why they do not work.

### Soundness
3

### Presentation
3

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
The paper applies the DiffC algorithm to pre-trained Stable Diffusion models (1.5, 2.1, and XL) for high-fidelity image compression at low bitrates. This approach leverages reverse-channel coding (RCC) to efficiently steer the denoising process toward realistic image reconstructions without additional training. By optimizing the denoising schedule and utilizing CUDA acceleration, the method achieves competitive reconstruction performance and compression times (under 10 seconds) compared to other state-of-the-art compression methods.

### Strengths
1. The paper extends DiffC to stable diffusion, provides an open-source implementation, and accelerates RCC with CUDA. These contributions promote the practicality of the method and pave the way for further exploration.

2. The paper is well written and easy to follow. Enough background information is provided to general readers.

3. The paper provides guidance on potential research directions in the Future Work section, offering insights for subsequent studies.

### Weaknesses
1. The paper lacks sufficient innovation and resembles more of an engineering improvement on existing methods.

2. The diffusion model requires multiple inference steps for both encoding and decoding, resulting in significant computational overhead.

3. Although the authors claim that their method is competitive with other state-of-the-art compression methods, no comparisons are provided in the paper. To substantiate this claim, the authors should compare their method with existing approaches such as PerCO [1], DiffEIC [2], and MS-ILLM [3] in terms of compression performance (e.g., PSNR, MS-SSIM, LPIPS, FID, etc.) and computational complexity (e.g., encoding/decoding time), presenting corresponding results in the paper.



### Questions
1. On page 2, line 100, the description of CDC appears to be inaccurate. CDC is trained from scratch rather than by fine-tuning conditional diffusion models.

2. In Section 4.2, why is there no R-D curve provided to illustrate the comparison between Stable Diffusion XL Base and Refiner?

3. In Section 3.5, it is mentioned, ``But in practice, we have found that just hard-coding a sequence of expected DKL values into the protocol based on their averages does not affect the performance of our method too much.`` Does this mean that the $D_{KL}$ values used in practice are manually set? Could the authors provide empirical results (e.g., R-D curves) to support the conclusion that this strategy does not affect the performance too much? Additionally, what impact would increasing or decreasing the preset $D_{KL}$ values have on performance? Could RD trade-offs be achieved by adjusting the $D_{KL}$ values?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a novel application of pretrained diffusion models, specifically Stable Diffusion versions 1.5, 2.1, and XL, for lossy image compression using the DiffC algorithm. The authors introduce practical workarounds to overcome challenges in reverse-channel coding, enabling efficient image compression and decompression within 10 seconds without additional training. The method is shown to be competitive with state-of-the-art compression techniques at low bitrates (0.005-0.05 bpp), demonstrating its efficacy and potential in real-world applications.

### Strengths
1) The paper introduces an innovative use of pretrained diffusion models for image compression, expanding the utility of these models beyond their typical generative applications.
2) The proposed method achieves competitive performance with state-of-the-art compression techniques at low bitrates, showcasing its practical value.
3) Implementation details and optimizations, such as the use of CUDA for reverse-channel coding, significantly enhance the efficiency and feasibility of the approach.
4) The publicly available implementation of the DiffC algorithm promotes transparency and facilitates further research and development in this area.

### Weaknesses
1) The method's performance is constrained by the fidelity limits of the Stable Diffusion models' variational autoencoders, affecting compression quality at higher bitrates.
2) The reverse-channel coding process, while optimized, still presents computational challenges, particularly for very large or very small DKL values.
3) The paper does not extensively explore the combination of DiffC with other conditional diffusion approaches, which could potentially enhance performance further.
4) The reliance on Stable Diffusion's image size limitations may affect the generalizability of the method to images outside the training distribution.

### Questions
1)  How does the performance of your method vary with image sizes that deviate from the training distribution of Stable Diffusion? Are there any strategies you are considering to mitigate performance degradation for such cases?
2) Can you provide a more detailed comparison between your method and other state-of-the-art compression techniques, particularly in terms of computational efficiency, quality metrics, and bitrate?
3) In the leftmost plot of Figure 3, could the authors explain why the performance of the 163-step is worse than that of the 54-step?

### Soundness
2

### Presentation
3

### Contribution
2
