# ClearSR: Latent Low-Resolution Image Embeddings Help Diffusion-Based Real-World Super Resolution Models See Clearer

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
We present \nameofmethod{}, a new method that can better take advantage of latent low-resolution image (LR) embeddings for diffusion-based real-world image super-resolution (Real-ISR). 
Previous Real-ISR models mostly focus on how to activate more generative priors of text-to-image diffusion models to make the output high-resolution (HR) images look better.
However, since these methods rely too much on the generative priors, the content of the output images is often inconsistent with the input LR ones.
To mitigate the above issue, in this work, we explore using latent LR embeddings to constrain the control signals from ControlNet, and extract LR information at both detail and structure levels.
We show that the proper use of latent LR embeddings can produce higher-quality control signals, which enables the super-resolution results to be more consistent with the LR image and leads to clearer visual results.
In addition, we also show that latent LR embeddings can be used to control the inference stage, allowing for the improvement of fidelity and generation ability simultaneously.
Experiments demonstrate that our model can achieve better performance across multiple metrics on several test sets and generate more consistent SR results with LR images than existing methods.
Our code will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper propose new diffusion-based method, named ClearSR, which can use the LR latent embedding to guide diffusion to generate better results. In particular, the author designs two modules to effectively use the information of LR embedding and propose a adjust strategy to balance the fidelity and detail of SR results.

### Strengths
This paper is clear in describing its contributions and methodology. 
The author analyzed the relationship between image fidelity and model generation capabilities, and attempted to propose a solution strategy.
The experimental arrangement is relatively reasonable, and the ablation study can prove the effectiveness of the strategies proposed by the author.

### Weaknesses
Some descriptions in the paper may lead to confusion. The authors classify detail information as high-frequency information and structural information as low-frequency information. However, edges can also represent structure and are actually considered high-frequency information. The authors should use more appropriate terminology to avoid ambiguity.

To balance the fidelity and details of results, the author propose Latent Space Adjustment (LSA) strategy. However, the experimental results do not clearly demonstrate that the proposed method performs better in terms of fidelity (PSNR, SSIM, LPIPS, etc). In addition, similar approaches have also appeared in DiffBIR and PASD, and the author should provide a thorough comparison with the strategies proposed by these other methods.

The LR latent embedding, which is the output of the VAE encoder, has a size of 4x64x64, while the input image is 3x512x512. Compared to the original image, the LR embedding loses a significant amount of spatial information. Therefore, the LR latent embedding may not be suitable for supplementing detail and structural information. 

Figure 2 shows that the proposed method has a low KL divergence value between the control signal and the low-resolution latent embedding. This suggests that the authors have introduced two modules to achieve a similar distribution between the LR latent embedding and the control signal. So why not use the LR latent embedding directly? Furthermore, from past work (DiffBIR, PASD, SeeSR), we know that the role of the control branch is primarily to remove degradation and bring it closer to the HR distribution. However, the method proposed by the authors results in the distribution of the control branch outputs being closer to the distribution of LR latent embedding, which is puzzling.

### Questions
The motivation is clear. However, there are some concerns regarding the proposed approach. Specifically, the LR latent embedding, which is the output of the VAE encoder, has a size of 4x64x64, while the input image is 3x512x512. Compared to the original image, the LR embedding loses a significant amount of spatial information. Therefore, the LR latent embedding may not be suitable for supplementing detail and structural information. 

Figure 2 shows that the proposed method has a low KL divergence value between the control signal and the low-resolution latent embedding. This suggests that the authors have introduced two modules to achieve a similar distribution between the LR latent embedding and the control signal. So why not use the LR latent embedding directly? Furthermore, from past work (DiffBIR, PASD, SeeSR), we know that the role of the control branch is primarily to remove degradation and bring it closer to the HR distribution. However, the method proposed by the authors results in the distribution of the control branch outputs being closer to the distribution of LR latent embedding, which is puzzling.

### Soundness
3

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
5

### Summary
This paper proposes a prior-based controlnet-like approach for image super-resolution. The motivation is to refine the conditional feature to improve the fidelity of the SR output while avoid the obvious degradation of generation ability. The proposed approach aims to achieve this goal from both the architecture design by introducing additional modules as well as cross-attention layers and the inference strategy by introducing proper guidance at difference inference steps. There are also some observations to support the design.

### Strengths
+ The motivation is clear and there are also some observations to provide the insights for the design of the approach.
+ The evaluation shows reasonable improvement of the proposed approach.
+ The paper is easy to follow.

### Weaknesses
- The additional modules introduced in this paper may also increase the cost of training and inference. Some evaluation on the complexity should be provided.
- The proposed Latent Space Adjustment strategy is somewhat tricky. How to choose ideal hyperparameters can be tough and case-by-case. Moreover, when the degradation is severe, adding LR guidance into the inference may leads to blurry outputs.
-Some strong baselines are missing ,e.g., SUPIR.

### Questions
My main concerns are as follows:

1. The author claims that ControlNet cannot preserve the LR information well in Figure 2. Is it because that ControlNet adds noise to the LR conditional during training and inference? Does the proposed approach also follows this setting as ControlNet? The authors should explicitly state whether they follow the same noise addition process as ControlNet, and if not, to explain how their approach differs.

2. The additional modules introduced in this paper may also increase the cost of training and inference. Some evaluation on the complexity should be provided, e.g., parameters, flops and inference time. The authors may consider provide some numerical comparison with existing baselines.

3. The proposed Latent Space Adjustment strategy is somewhat tricky. How to choose ideal hyperparameters can be tough and case-by-case. Moreover, when the degradation is severe, adding LR guidance into the inference may leads to blurry outputs. The authors should consider providing guidelines or heuristics for choosing hyperparameters, and discussing how their method performs under severe degradation conditions and the quality of the guidance under such cases.

4. SUPIR has more powerful generative ability then the baselines in the paper. The authors may want to explain why SUPIR was not included as a baseline, or to consider adding it to their comparisons if feasible.

5. Why choosing window cross-attention rather than full-attention and how to decide the window size? The authors should provide empirical or theoretical justification for using window cross-attention, and explain how they determined the optimal window size.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces ClearSR, a novel approach designed to enhance the utilization of LR image information in SR tasks. The DPM and SPM modules are designed, enabling the extraction of more LR details and structural information. The method also demonstrates that latent LR embeddings can be used to adjust the latent space during inference, improving both fidelity and generative quality. ClearSR outperforms existing SR models across multiple metrics on various test datasets, producing SR results with rich generated details while maintaining consistency with the LR images.

### Strengths
1. This paper proposes two modules to extract more LR details for structural and detail preservation.

2. In the inference stage, this paper proposes an LSA strategy, which performs different directional adjustments towards LR embeddings in the latent space in the earlier and later steps. This idea is reasonable and interesting.

3. The results look good, the writing is well, and the paper is easy to follow.

### Weaknesses
1. This paper introduces two modules (DPM and SPM) to enhance the utilization of LR image information, but these increase model parameters and inference time compared to ControlNet. However, algorithmic complexity is not discussed. The paper lacks a detailed analysis of the computational overhead introduced by the DPM and SPM modules, specifically how the number of parameters and floating-point operations per second (FLOPs) scale with image resolution and batch size. A comparison of the inference time, not just against ControlNet but also against other state-of-the-art SR methods, is crucial to assess the practical applicability of the proposed approach.

2. The description in Line 190 is confusing; PASD does not use the CLIP image encoder to extract LR features. The paper should clarify that PASD, and similar methods, typically use the CLIP text encoder for conditioning, rather than the CLIP image encoder for extracting low-resolution image features. This distinction is important because the CLIP image encoder is designed to process high-resolution images and extract semantic information, which is different from the low-level feature extraction needed for SR tasks. The paper should explicitly state which encoder is being used and why it is appropriate for the task.

3. The explanation of image-level feature $\textbf{p}$ in Figure 3 is unclear. How is $\textbf{p}$ integrated into SD Unet, and what is its role in the framework? The paper needs to provide a more detailed explanation of how the image-level feature $\textbf{p}$ is incorporated into the Stable Diffusion UNet architecture. It is unclear whether $\textbf{p}$ is concatenated, added, or used in a cross-attention mechanism. The paper should also explain the specific role of $\textbf{p}$ in the diffusion process, such as whether it is used to guide the denoising process or to provide additional context to the UNet.

4. DPM and SPM are designed to extract LR information at detail and structure levels, both of which should contribute to fidelity. However, Table 2 suggests that SPM improves fidelity, while window-based cross-attention layers in DPM weaken fidelity. More explanation is required. The paper should provide a more in-depth analysis of why the window-based cross-attention in DPM appears to degrade fidelity, as measured by PSNR, while SPM improves it. The paper should also include an ablation study that removes DPM entirely to better isolate the contribution of each module. It is crucial to understand whether the cross-attention mechanism is not well-suited for this task or if the window size or other parameters need to be tuned. Furthermore, the paper should discuss the trade-off between fidelity and perceptual quality when using DPM and SPM.

### Questions
1. The authors need to compare the complexity of ClearSR with that of the other methods, including the model parameter counts, inference time, and inference timestep.

2. The authors should double-check the understanding of PASD in Line 190.

3.  The authors should add a clearer description of the image-level feature $\textbf{p}$ in Figure 3. How is $\textbf{p}$ integrated into SD Unet, and what is its role in the framework?

4. The authors should explain more clearly in Table 2. Why does the SPM improve fidelity, while window-based cross-attention layers in DPM weaken fidelity? In addition, the ablation study that includes a model without DPM should also be provided for a more complete picture of each module's contribution.

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
5

### Summary
This paper introduces ClearSR, a novel method for real-world image super-resolution (Real-ISR) using pretrained T2I diffusion models. ClearSR leverages LR embeddings to constrain ControlNet's control signals,  extracting LR information at detail and structure levels. The authors design DPM and SPM modules, which enhance image details and maintain structural integrity, respectively. Additionally, they propose an LSA strategy during inference to balance fidelity and generative capabilities. Extensive experiments demonstrate that ClearSR outperforms existing methods across multiple benchmarks and metrics.

### Strengths
A key challenge in RealSR tasks using powerful T2I models is generating fine details while maintaining fidelity, which presents a trade-off. ClearSR explore this by using a pre-trained VAE encoder as an initial feature extractor for LR images to preserve fidelity as much as possible, and designing DPM and SPM to handle specific control tasks. Additionally, ClearSR observed that the added realistic details largely come from the final inference steps. Therefore, it introduced the LLA mechanism to move away from the LR latent space in the final stages, enhancing generative capability and improving model flexibility.

### Weaknesses
1. Lacks more detailed comparisons, such as inference time, parameter count, and computational cost.
2. Missing some key details, like the number of inference steps, and Figure 10 doesn't provide the names of the comparison methods.
3. While the motivation is good, the novelty of the solution seems relatively weak.

### Questions
[1] Selection of α and β Parameters:

a. How were the values for α and β in the LSA strategy chosen? Did you perform a systematic parameter search or optimization? Are these parameters required to be tuned for different datasets or image types, and is there a way to automate their selection?

[2] Implementation of LoRA Layers

How does the choice of LoRA rank (set to 16) impact model performance, and was this rank value optimized experimentally?


[3] Something about classfier-free guidance, cfg

During the inference stage, by adjusting the CFG value, RealSR methods based on pre-trained T2I diffusion models can also balance fidelity and perception. The authors did not report the CFG settings during inference, such as the CFG value and negative prompt. Additionally, the proposed LSA control method needs to be compared in detail with the CFG control method to highlight the differences.

If the main concerns are well addressed, I will consider increasing the score.

### Soundness
3

### Presentation
3

### Contribution
3
