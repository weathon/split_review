# Image Super-Resolution via Latent Diffusion: A Sampling-Space Mixture of Experts and Frequency-Augmented Decoder Approach

- Decision: Reject
- Scores: 6, 3, 3, 5

## Abstract
The recent use of diffusion prior, enhanced by pre-trained text-image models, has markedly elevated the performance of image super-resolution (SR). To alleviate the huge computational cost required by pixel-based diffusion SR, latent-based methods utilize a feature encoder to transform the image and then implement the SR image generation in a compact latent space. Nevertheless, there are two major issues that limit the performance of latent-based diffusion. First, the compression of latent space usually causes reconstruction distortion. Second, huge computational cost constrains the parameter scale of the diffusion model. To counteract these issues, we first propose a frequency compensation module that enhances the frequency components from latent space to pixel space. The reconstruction distortion (especially for high-frequency information) can be significantly decreased. Then, we propose to use Sample-Space Mixture of Experts (SS-MoE) to achieve more powerful latent-based SR, which steadily improves the capacity of the model without a significant increase in inference costs. These carefully crafted designs contribute to performance improvements in largely explored 4$\times$ blind super-resolution benchmarks and extend to large magnification factors, i.e.,  8$\times$ image SR benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Sampling-Space MoE to enlarge the diffusion model without necessitating a substantial increase in training and inference resources. To address the issue of information loss caused by the latent representation of the diffusion model, the author further presents a frequency-compensated decoder to refine the details of super-resolution images. Experimental results on both Blind and Non-Blind SR datasets demonstrate that the proposed method obtain good performance.

### Strengths
1. Appealing visual results are obtained with the proposed method.
2. The paper is well-written and organized, making it easy to understand the proposed framework and its contributions.

### Weaknesses
1. Ablation studies lack qualitative results, and the results in Table 5 do not offer strong evidence for the effectiveness of the proposed FCD.
2.The visual results are sometimes good but with severe hallucination, and quantitative results are not always good on LPIPS and NIQE (These two metrics are generally more convincing in real image restoration).
3. Since the compared methods including GAN-based methods and Diffuison-based method, it is insufficient to evaluate these methods only based on restoration metrics. The author should also make a comparison on model complexity, inference speed, and GPU usage.

### Questions
see the Weaknesses part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors proposed a new diffusion-based SR approach, the authors propose a sample-space mixture of experts strategy to improve the sampling quality and propose a frequency compensation module to reduce high-frequency reonstruction distortion.

### Strengths
1) The author introduce sampling-space MOE to improve the image quality of diffusion-based SR, and provide detailed ablation experiments to validate the effectiveness of the adopted strategy.
2) The authors propose a frequency loss to emphasize high-frequency distortion.
3) The authors validated the proposed method on several benchmark datasets.

### Weaknesses
1) The novelty of this paper is not significant. The major framework and the major modifications were proposed in other works and the authors just combine these method to establish a new method. Using the MOE strategy to enhance sampling quality and introduce high-frequency loss to enhance SR results are straight-forward operations and the authors just combine the two methods without any modification.
2) To evaluate photo-realistic SR, it is highly suggested to conduct subjective evaluation to compare different methods.
3) Based on Table 1, the advantage of the proposed method over the competing approaches are not significant.
4) The authors utilized 5 or 6 metrics to evaluate different methods, but did not discuss the results carefully. The numbers in Table 5 can not clearly validate the effectiveness of the proposed FFL and AFF-Net.

### Questions
Please refer to the weakness part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper summarizes two issues in using the diffusion model to address image super-resolution, namely distortion caused by the compression of latent space and the huge computational cost. This work proposes a frequency compensation module to enhance
the frequency components and use Sample-Space Mixture of Experts (SS-MoE) to improve the capacity of the SR model. The visual results provided in the paper appear to have clearer details compared to other methods, and it also demonstrates certain advantages in some quantitative metrics.

### Strengths
1. The paper provides a comprehensive and clear analysis and summary of the current methods and issues in super-resolution.

### Weaknesses
1. The results in the paper do not stand out significantly when compared to other methods, and they are not the best in terms of the metrics, making it challenging to demonstrate the superiority of this method over other super-resolution methods.
2. The reason for designing SS-MoE in this way is not explicitly explained. Initially, multiple MoEs were designed to separately handle different noise sources. However, during inference, an averaging step is performed to parameterize the weights, which conflicts with the original motivation.
3. In the experimental ablation study of FCD, the results show variations in the metrics, with some being high and others low. This inconsistency in the results makes it difficult to determine whether the approach used in the paper is the best one.
4. There are several typographical errors in this paper. I recommend conducting a more thorough proofreading.

### Questions
Refer to weakness

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel latent-diffusion-based framework for image super-resolution. Experiments achieve state-of-the-art of x4 and x8 super-resolution among the latest competing diffusion-based SR models.

### Strengths
Quantitative and qualitative results all reveal the superiority of the proposed model compared to the latest diffusion-based models.

### Weaknesses
1.	The point of compensating for the information loss in the autoencoder is interesting, but the novelty is limited. The newly proposed components are weak in cohesion and continuity in solving the information loss problem of the AE space and information compression. 
2.	The purpose of SS-MoE seems not to be designed specifically for information loss, i.e., the motivation is not clearly written in the paper. Though the performance can be slightly upgraded with the component, the parameters are multiple times larger than the model without the component (according to Table 6 and Table 3, and the paper didn’t show the parameter increase of each component). There may be other efficient designs with the increased parameters of SS-MoE.
3.	Missing comparisons with some new baselines: DiffIR [1], DIffBIR [2], ResShift [3]

### Questions
Please explain in detail the motivation of SS-MoE. Others please refer to the weaknesses part.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
