# Diffusion-based Extreme Image Compression with Compressed Feature Initialization

- Decision: Reject
- Scores: 3, 3, 6, 5

## Abstract
Diffusion-based extreme image compression methods have achieved impressive performance at extremely low bitrates. However, constrained by the iterative denoising process that starts from pure noise, these methods are limited in both fidelity and efficiency. To address these two issues, we present \textbf{R}elay \textbf{R}esidual \textbf{D}iffusion \textbf{E}xtreme \textbf{I}mage \textbf{C}ompression (\textbf{RDEIC}), which leverages compressed feature initialization and residual diffusion. Specifically, we first use the compressed latent features of the image with added noise, instead of pure noise, as the starting point to eliminate the unnecessary initial stages of the denoising process.
Second, we design a novel relay residual diffusion that reconstructs the raw image by iteratively removing the added noise and the residual between the compressed and target latent features. Notably, our relay residual diffusion network seamlessly integrates pre-trained stable diffusion to leverage its robust generative capability for high-quality reconstruction. Third, we propose a fixed-step fine-tuning strategy to eliminate the discrepancy between the training and inference phases, further improving the reconstruction quality. Extensive experiments demonstrate that the proposed RDEIC achieves state-of-the-art visual quality and outperforms existing diffusion-based extreme image compression methods in both fidelity and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces RDEIC, a novel diffusion model for extreme image compression that accelerates the denoising process through compression feature initialization. It draws on techniques from several papers, e.g., the codec framework scheme in GLC[1], and the control net in deffeic[2].The results provide evidence that the proposed scheme achieves SOTA performance.

### Strengths
1.	The paper is well-written and easy to follow, and the experiments are detailed and comprehensive.
2.	This paper reduces computational complexity by reducing the denoising step, which is valuable for resource-constrained environments.

### Weaknesses
1.	The paper has limited innovation. Its pipeline looks like a simple combination of GLC[1] and deffeic[2], utilizing the codec framework of GLC[1] and the generative model of deffeic[2]. However, the paper does not compare performance with GLC[1].
2.	This paper adopts a better performance generative model RDD instead of stable diffusion, and with the stronger generative ability of RDD, better performance is obtained. So if DiffEIC-50 also adopts RRD, will it achieve better performance?
3.	The conclusions of some visualization experiments are not rigorous enough. For example, in Fig. 1, despite the obvious subjective quality improvement of RDEIC, its bit rate is 7.5% higher than deffeic[2]. A similar problem can be observed in Figure 5.
4.	Some analysis needs to be included to show why RDEIC is worse than MS-ILLM on the NIQE metric.

### Questions
See weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes Relay Residual Diffusion Extreme Image Compression method to achieve fidelity and efficiency. In particular, this paper use latent feature with added noise as the start point and employ residual diffusion to improve the fidelity. And this paper proposes a fixed-step fine-tuning strategy to reduce the number of steps.

### Strengths
This paper is clear in describing its contributions and methodology. 
The experimental arrangement is relatively reasonable, and the ablation study can prove the effectiveness of the strategies proposed by the author.

### Weaknesses
The novelty is limited. Firstly, adding noise to the latent features is a common operation, which is used in many papers [1,2]. Secondly, the proposed residual diffusion is similar to ResShift[3]. The author should fully research the diffusion-based methods on low-level vision tasks published in the past two years and analyze the differences between them better. 
[1] SeeSR: Towards Semantics-Aware Real-World Image Super-Resolution CVPR23
[2] Pixel-Aware Stable Diffusion for Realistic Image Super-Resolution and Personalized Stylization ECCV24
[3] ResShift: Efficient Diffusion Model for Image Super-resolution by Residual Shifting NIPS23

The motivation is not clear. In the third paragraph of Sec. 1, the author analysis the limitations of diffusion-based methods. The first limitation is ‘these methods rely on an iterative denoising process to reconstruct raw images from pure noise which is inefficient for inference’. The second limitation is ‘initiating the denoising process from pure noise introduces significant randomness, compromising the fidelity of the reconstructions.’ In addition to adding noise to the latent features, the author also employs a residual diffusion process and employ pre-trained stable diffusion to address these limitations. It is not clear remains unclear how residual diffusion and pre-trained stable diffusion can resolve the randomness caused by pure noise and improve the fidelity of the reconstructions.

There are two doubts about controllable detail generation. Firstly, the pre-trained stable diffusion is used to obtain low-frequency information. Since the pre-trained stable diffusion has not seen the inputs in the authors' task, why can it produce the expected results? Secondly, why did the authors choose to use pre-trained stable diffusion instead of directly using CFG?

### Questions
Figure 4 shows that the authors' method does not achieve the best results on metrics such as PSNR, MS-SSIM, and SSIM, and there is a significant gap compared to other methods. Noting that PSNR MS-SSIM, and SSIM are metrics used to evaluate fidelity. This is inconsistent with the authors' motivation. In the abstract, the authors mention that the proposed method aims to address the limitations of fidelity and efficiency.

The authors mention in their experiments that they trained five models, each corresponding to different λ_r values. However, in the comparative experiments (e,g, Tab.1, Tab. 2, Tab. 3, Fig. 4, Fig.5, Fig. 6, Fig.7, etc.), the authors do not specify which model's results were used. In addition, the author did not mention the guidance scale values used for these experimental results.

In Tab. 3, the author uses 2/5 in the DS column, so it is unclear whether the performance in the table refers to the 2-step model or the 5-step model. In addition, just using distortion of BD-rate or perception of BD-rate is not clear. The distortion includes PSNR, and SSIM, etc. and perception includes DISTS, FID, and LPIPS, etc. It is not clear which metrics distortion and perception represent respectively. The author should provide detailed results for metrics such as PSNR, SSIM, and LPIPS. Meanwhile, in the paper comparing the methods (PerCo, MS-ILLM), they did not use the bd-rate metric. Therefore, it is a good choice that the author just employs the values of PSNR, SSIM or LPIPS to demonstrate the performance and not use BD-rate.

In Tab. 2, the BD-rate of RDEIC with 2 DS is 0, while the BD-rate of RDEIC with 2 DS is also 0. So, which is the anchor in Tab. 2.

### Soundness
2

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
The paper presents a novel approach called Relay Residual Diffusion Extreme Image Compression (RDEIC), which improves upon traditional diffusion-based image compression methods. By leveraging compressed latent features and a residual diffusion process, RDEIC enhances fidelity and efficiency, addressing limitations of iterative denoising processes that typically begin with pure noise. Experimental results indicate significant performance gains in compression rates while maintaining image quality.

### Strengths
1) Introduces an innovative framework (RDEIC) that improves image compression efficiency.
2) Effectively addresses the fidelity issues present in existing diffusion-based methods.
3) Provides strong experimental results demonstrating the advantages of the proposed approach.

### Weaknesses
1) Limited discussion on the computational complexity of the new method.
2) Insufficient comparison with a broader range of existing compression techniques.
3) Potential overfitting concerns not addressed within the experimental analysis.

### Questions
1) Include a detailed analysis of the computational efficiency and resource requirements of RDEIC.
2) Expand the comparative analysis to include more baseline models and state-of-the-art techniques.
3) Address the possibility of overfitting by incorporating additional validation datasets or robustness tests.

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
This paper introduces Relay Residual Diffusion Extreme Image Compression (RDEIC), a method for high-quality image compression at extremely low bitrates. RDEIC has three main components: (1) it begins denoising with compressed latent features plus noise instead of pure noise, reducing steps and improving fidelity; (2) it introduces a relay residual diffusion process, iteratively removing noise and residuals between compressed and target features, leveraging a pre-trained stable diffusion model for quality reconstruction; and (3) it applies a fixed-step fine-tuning strategy to minimize discrepancies between training and inference, further enhancing quality. Experimental results show that RDEIC achieves state-of-the-art visual quality, surpasses existing diffusion-based methods in fidelity and efficiency, and provides controllable detail generation to balance smoothness and sharpness.

### Strengths
1. Given the effectiveness and complexity of diffusion models, fast diffusion sampling as a practical research approach holds significant value and positively impacts the community.

2. The balance between smoothness and sharpness mentioned in the paper provides practical insights into this area. In a given compression state, determining how to map it to the sampling step 
𝑁 can directly affect reconstruction quality. This mapping relationship is crucial to the model's effectiveness and stability, which the authors have explored in detail.

### Weaknesses
1. The novelty of this work is relatively modest, though it provides a valuable practical application in image compression. Many recent studies have explored similar approaches, starting the diffusion process from low-quality images rather than pure noise to enhance efficiency and accelerate sampling. Integrating degraded image embeddings into a pre-trained diffusion model as a plug-and-play module is also a relatively well-explored approach in the field of image processing. Prior works include:
   - [1] Lin, X., He, J., Chen, Z., Lyu, Z., Dai, B., Yu, F., ... & Dong, C. (2023) in "DiffBIR: Towards Blind Image Restoration with Generative Diffusion Prior",
   - [2] Wang, Y., Yu, Y., Yang, W., Guo, L., Chau, L. P., Kot, A. C., & Wen, B. (2023) in "ExposureDiffusion: Learning to Expose for Low-Light Image Enhancement" (ICCV),
   - [3] Ma, J., Zhu, Y., You, C., & Wang, B. (2023) in "Pre-trained Diffusion Models for Plug-and-Play Medical Image Enhancement" (MICCAI).

2. The Text-Sketch in Figure 1 and Figure 5 shows significant deviations in chroma reconstruction. I am unsure whether this is due to the baseline itself or if there was a mix-up between RGB and BGR channels during the experimental preprocessing stage. Additionally, the brightness of PerCo-20 in Figure 1 appears to be slightly biased compared to the ground truth. It is recommended to carefully examine the methods used for comparison, especially when the baselines are highly novel, and when results show noticeably unusual behavior, to ensure a fairer comparison.

3. Potential issue with variable control in the entropy model. The paper employs unusual entropy models (i.e., VQ-E and VQ-D) without adequate control or detailed explanation. This may lead to comparison results that do not accurately reflect the primary contribution of the proposed approach when contrasted with other algorithms, given that the precision of entropy models directly impacts compression efficiency and reconstruction quality.

4. Ambiguity in baseline selection. In Table 1 and Line 354, using “Ours” as the baseline results in a row of zeros, which may lead to ambiguity and does not align with traditional statistical practices (which typically use a control group as the baseline). It is advisable to clarify the baseline in the caption or table notes. Additionally, selecting a well-recognized baseline (e.g., JPEG, BPG, or a state-of-the-art compression method) for BD-rate comparison would provide a more straightforward understanding of the relative performance of each method.

5. Scoring issue with implementation versions. In Lines 442-443, the authors mention two implementation versions, yet both report a BD-rate of 0, which may cause confusion. It is recommended to provide a detailed explanation of the different implementations and clarify the reason for the BD-rate of 0 in each case.

6. Suggestions for improving formula clarity:  
   - Clarity in the derivation from Eq.2 to Eq.4. The derivation from Eq.2 and Eq.3 to Eq.4 is crucial for the model’s structure but is not immediately clear. This derivation could directly impact the model's efficiency and accuracy. It is recommended to provide a more detailed explanation of these key steps in the main text to enhance understanding.
   
   - Ambiguity in the Definition of Eq.11. In traditional diffusion models (e.g., DDPM and Stable Diffusion), the noise estimator typically predicts total noise rather than noise at specific frequency bands. Interpreting $ \epsilon_{sd}(z_n, n) $ directly as a "low-frequency component" may lack theoretical support, especially without a clear basis for frequency division. The decomposition of predicted noise into low- and high-frequency components might be a heuristic approach, but further justification is needed to establish its rigor.
   
   - Undefined $ l_p $ in Eq.9. The definition of $l_p $ in Eq.9 is unclear. To improve understanding, it would be helpful for the authors to clearly specify the meaning of $ l_p $ and provide relevant context.

7. Minor formatting and typographical suggestions.  
   - Line 100: Add commas before and after "i.e." for clarity.
   - Lines 220, 229, and 238: Add commas at the end of formulas to improve readability.

### Questions
1. Definition of "Extremely Low Bitrates". The standard for "extremely low bitrates" lacks a precise definition. Given varying content distributions (scenes) and the amount of high-frequency details, might "extremely low" have different thresholds? How would one define this threshold? Could the authors discuss the broader application potential of encoding methods in bandwidth-constrained scenarios? Additionally, does diffusion lose its value in compression at higher and medium bitrates?

2. Codebook Details. The approach involving "vector-quantized latent image representations" is intriguing. Could the authors elaborate on the learning and training process of the codebook loss? Specifically, how is the codebook initialized, and what is the interaction between the codebook and $ l_p$?

3. Since the multi-step sampling mechanism in diffusion leads to increased computational complexity in decoding, would placing diffusion in the encoding part or within the hyperprior yield different conclusions regarding complexity?

4. Role of the diffusion mechanism. Is diffusion effective mainly as a post-processing module to enhance perceptual quality, or does it also contribute to compact representation? A deeper analysis of the role of diffusion in improving perceptual quality versus compact representation would be insightful.

### Soundness
2

### Presentation
2

### Contribution
2
