# Warm Diffusion: Recipe for Blur-Noise Mixture Diffusion Models

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
Diffusion probabilistic models have achieved remarkable success in generative tasks across diverse data types. While recent studies have explored alternative degradation processes beyond Gaussian noise, this paper bridges two key diffusion paradigms: hot diffusion, which relies entirely on noise, and cold diffusion, which uses only blurring without noise. We argue that hot diffusion fails to exploit the strong correlation between high-frequency image detail and low-frequency structures, leading to random behaviors in the early steps of generation. Conversely, while cold diffusion leverages image correlations for prediction, it neglects the role of noise (randomness) in shaping the data manifold, resulting in out-of-manifold issues and partially explaining its performance drop. To integrate both strengths, we propose Warm Diffusion, a unified Blur-Noise Mixture Diffusion Model (BNMD), to control blurring and noise jointly. Our divide-and-conquer strategy exploits the spectral dependency in images, simplifying score model estimation by disentangling the denoising and deblurring processes. We further analyze the Blur-to-Noise Ratio (BNR) using spectral analysis to investigate the trade-off between model learning dynamics and changes in the data manifold. Extensive experiments across benchmarks validate the effectiveness of our approach for image generation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes Warm Diffusion, a unified Blur-Noise Mixture Diffusion Model (BNMD), to control blurring and noise jointly.

### Strengths
The paper is well-written

### Weaknesses
1.An improvement of 1-2 points in FID does not result in any noticeable change in visual effects. In fact, the actual visual quality may not be better than those with lower FID scores.

2.I hope the authors can present results that are sufficiently stunning or impactful. There are currently many papers in this area, and everyone is focused on slightly improving FID and IS, but the visual quality is still much worse than the current FLUX. This leaves me with no motivation to decide whether to accept any of these papers.

### Questions
see above

### Soundness
2

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
3

### Summary
The paper proposes a new diffusion framework named "Warm Diffusion," which introduces a unified Blur-Noise Mixture Diffusion Model (BNMD) to bridge the gap between hot diffusion (using noise) and cold diffusion (using blurring) models. The authors argue that both hot and cold diffusion paradigms have inherent limitations: hot diffusion ignores the correlation between image structures, while cold diffusion neglects the importance of noise in modeling the data manifold. Warm Diffusion leverages a Blur-to-Noise Ratio (BNR) to integrate both noise and blurring in a "divide-and-conquer" approach, enhancing model learning and image quality. Extensive experiments show that the method outperforms existing diffusion-based generative models on several benchmarks.

### Strengths
1. The idea of combining Blur and Noise is impressive as it exploits spectral dependencies of images while preserving the data manifold.

2. The proposed BNMD framework is evaluated across several benchmarks, including CIFAR-10, FFHQ, and LSUN-church datasets, sufficiently verifying the effectiveness of the proposed method.

### Weaknesses
1. I think the motivation of the work is not very clearly presented in the introduction section. The exact necessity of introducing blurring into the diffusion model should be given, which is the most important motivation of this work. Figure 5 shows that a lower BNR brings better FID results, which somehow seems to say that “blur” does not help to improve the quality of the generated image.

2. For the sampling process presented in algorithm 2, the sampling starts from a zero-mean Gaussian distribution. How can this be revealed from Eq. 4 (at time T)?

3. As shown in Table 5, there exist large deviations among the results produced by different parameterizations. More explanation need to be provided.

### Questions
Q1. Although the authors repeatedly mention “spectral dependency”, the definition of this term is not clear. I can't clearly understand what exactly the “strong correlation” between high-frequency and low-frequency structures is. In Figure 3, why “shifting more responsibility to the deblurring task” means “effectively utilizing the spectral dependency of images”?

Q2. In regard to blur-to-noise-ratio (BNR) defined by this work, it seems that the noise level and the blur level do not change for all time t. I want to further confirm that mentioning the effects of BNR, does the proposed diffusion model actually have a sequence of (a_1,…,a_T) and (b_1,…,b_T) or just one a and b for all timesteps?

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
3

### Summary
The authors analyze the characteristics and limitations of hot diffusion (noise-based) and cold diffusion (blur-based) and propose a unified framework that combines both diffusion processes. This approach effectively mitigates the shortcomings of each model, achieving complementary advantages. The authors also conduct extensive experiments and data analyses to demonstrate the superiority of the proposed method.

### Strengths
1. The authors analyze the characteristics and limitations of both hot and cold diffusion, leading to a unified diffusion architecture that combines both approaches.
2. The authors introduce the new concept of Blur-to-Noise Ratio (BNR), which enables better analysis of diffusion models.
3. Extensive quantitative and qualitative analyses, including comparisons with state-of-the-art methods and detailed data analysis, are provided.
4. Experimental results demonstrate the effectiveness of the proposed method in image generation.

### Weaknesses
1. In Figure 1, the authors do not sufficiently explain the meaning of each module. For example, the significance of different-sized circles in the left chart is unclear, as well as the meaning of “Data manifold (indexed by noise level)” and the images depicted. It is suggested that the caption be revised to simplify understanding.
2. The authors use the improved DDPM++/NCSN++. However, it would be beneficial to experiment with the proposed approach on other baseline architectures, such as the original DDPM [1]. This would help demonstrate the generalizability of the method beyond specific model improvements.

### Questions
1. Please provide a more detailed explanation of the images in Figure 1.
2. Provide experimental results using DDPM as a baseline, showing the performance improvements of the proposed method compared to the original model and alternative approaches.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes warm diffusion to bridge hot diffusion, which relies entirely on noise, and cold diffusion, which uses only blurring without noise. This paper claims that noise prediction has the property of good diversity and data manifold, and the blur prediction has the advantage of better spectral dependency and convergence. Then, the blur-to-noise ratio problem in proposed unified Blur-Noise Mixture Diffusion Model (BNMD) is discussed. The performance on the choosen datasets is promissing.

### Strengths
1. The concept of blur-noise mixture is interesting. The analyses of cold diffusion and hot diffusion are insightful. It is also suggested to verify the claims about these two diffusion paradigms with supporting evidence or visualization, which is missing in the current paper.
2. The analyses of the blur-to-noise ratio are clearly discussed, which is an important aspect in the proposed mixture paradigm. 
3. The results on the conducted small-scale datasets are promissing.

### Weaknesses
1. This paper claims to decompose the training object into two parts: deblurring and denoising. However, the training target of the deblurring part is the residual, which is the difference between the clean image and the blurred image. This is quite confusing, since this "deblurring" transition also involves denoising and is not even doing the deblurring job in a traditional sense. The network is not learning to directly reverse a blur operation, but rather to predict high-frequency details given a blurred input, which is a different task.
2. This two training target operation enforces the network to simultaneously model the distribution of the blur and the residual. Besides, the blur also has various levels depending on the diffusion timestep. These factors may make the distribution modeling task significantly harder than just predicting the noise or the clean data, especially when the data scale is large. The network has to learn a complex mapping from noisy inputs to both blurry versions and high-frequency residuals, which could lead to optimization challenges.
3. The experimental results on large-scale datasets are missing, e.g., ImageNet. Since the recent state-of-the-art diffusion models usually conduct experiments on ImageNet and even larger-scale datasets, the absence of results on these datasets makes the actual performance and the superiority of this method ambiguous. It is unclear how well this method would scale to more complex and diverse datasets.

### Questions
My question mainly focuses on the training target and the corresponding optimization diffuculty. Refer to the weakness for details. 
My final score depends on the response and I am willing to raise the score with convincing responses.

### Soundness
3

### Presentation
3

### Contribution
3
