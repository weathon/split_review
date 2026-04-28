# DiffIR2VR-Zero: Zero-Shot Video Restoration with Diffusion-based Image Restoration Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
This paper introduces a method for zero-shot video restoration using pre-trained image restoration diffusion models. Traditional video restoration methods often need retraining for different settings and struggle with limited generalization across various degradation types and datasets. 
Our approach uses a hierarchical latent warping strategy for keyframes and local frames, combined with token merging that uses a hybrid correspondence mechanism that integrates spatial information, optical flow, and feature-based matching.
We show that our method not only achieves top performance in zero-shot video restoration but also significantly surpasses trained models in generalization across diverse datasets and extreme degradations (8$\times$ super-resolution and high-standard deviation video denoising). We present evidence through quantitative metrics and visual comparisons on various challenging datasets. Additionally, our technique works with any 2D restoration diffusion model, offering a versatile and powerful tool for video enhancement tasks without extensive retraining. 
See our project page for video results and source code: \href{https://jimmycv07.io/DiffIR2VR_web/}{jimmycv07.io/DiffIR2VR\_web}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a method for zero-shot video restoration using pre-trained image restoration diffusion models. It combines a hierarchical latent warping strategy for keyframes and local frames and token merging that integrates spatial information, optical flow, and feature-based matching.  The method acheives competitive results on zero-shot video restoration tasks such as super-resolution and denoising.

### Strengths
1. The method is training-free which makes it computationally practical.

### Weaknesses
1. To my understanding, the method relies on certain architectural heuristics inspired by the video-editing literature rather than on a solid mathematical framework. Since the method involves no training, there is no theoretical guarantee that it won't fail under certain conditions. Specifically, the hierarchical latent warping strategy, while intuitively appealing, lacks a rigorous justification for its specific design choices, such as the number of levels or the weighting of different scales. The token merging strategy also appears to be based on empirical observations rather than a principled approach, making it difficult to predict its behavior in unseen scenarios. The reliance on optical flow, which can be unreliable in cases of large motion or occlusions, further compounds this issue.

2. The method combines existing ideas from video editing, which on my opinion is still acceptable; however, this limits its novelty. The use of optical flow for temporal alignment and feature-based matching for correspondence are well-established techniques. The specific combination of these techniques, while potentially effective, does not introduce a fundamentally new concept or approach to the problem of video restoration. The token merging strategy, while presented as a novel contribution, appears to be a straightforward application of existing attention mechanisms.

3. The improvement over the baseline on some datasets, particularly in the case of denoising, is not significant. While the method demonstrates some improvements in super-resolution, the gains in denoising are marginal. This suggests that the method's effectiveness is highly dependent on the specific restoration task and the nature of the degradation. The lack of substantial improvement in denoising raises questions about the method's ability to handle complex noise patterns or low signal-to-noise ratios.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a zero-shot video restoration method using pre-trained image restoration diffusion models. The proposed approach introduces a hierarchical latent warping strategy and a hybrid flow-guided token merging approach to enhance both temporal consistency and visual detail. Experimental results demonstrate competitive performance in video super-resolution, denoising, showing advantages over state-of-the-art methods. An ablation study further highlights the importance of each proposed component.

### Strengths
- The paper is well-structured, making the methodology and findings easy to understand.
- The method achieves competitive results without requiring additional training.

### Weaknesses
 - Both the latent warping and hybrid flow-guided token merging approaches rely heavily on optical flow information, which could be a limitation in cases where optical flow estimation is challenging or inaccurate.
- The paper's novelty is somewhat limited, as it primarily combines two existing methodologies with minor modifications. Specifically, the contributions include adjusting the range of warping frames at global and local levels and introducing a flow-guided confidence criterion for token merging.

### Questions
- Degradations that are not encountered during optical flow training may introduce significant errors. How does the proposed method address this issue, and what motivated the choice of the GMFlow network for this approach?
- In Equation (5), is there a specific reason for including f_{src -> tar} (X(T_{src})) twice? 
- Including additional real-world datasets (e.g., [1, 2]) in the evaluation would help assess the method's generalization and robustness. 
- Could you provide a comparison of inference times with other methods?

Reference

[1] Towards Real-world Video Face Restoration: A New Benchmark, cvprw 2024

[2] Toward convolutional blind denoising of real photographs, cvpr 2019

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a versatile zero-shot video restoration approach leveraging pre-trained image restoration diffusion models. Unlike conventional methods that require retraining and often struggle with generalization, this method uses a hierarchical latent warping strategy for keyframes and local frames, along with a hybrid correspondence mechanism that merges tokens based on optical flow and token similarity. This approach demonstrates outstanding zero-shot performance, effectively generalizing across varied datasets and managing extreme degradations, including video super-resolution, denoising, and depth completion. Compatible with numerous 2D restoration diffusion models, the technique is validated through quantitative and visual benchmarks on challenging datasets, removing the need for extensive retraining.

### Strengths
The primary contribution of this approach is its ability to leverage conventional image generation models directly, without requiring modifications to network architecture or the need for retraining or fine-tuning. This is achieved through a straightforward yet effective technique: hierarchical token merging within the latent space, which ensures temporal consistency across generated video frames. By using this token merging strategy, the method successfully adapts static image models for dynamic video generation, maintaining coherence between frames without compromising quality. Furthermore, this approach reflects a well-engineered integration of recent advances in token merging, incorporating techniques from VidToMe and Upscale-A-Video. These advancement enhances the network’s capacity to address various video restoration challenges, effectively overcoming the limitations of traditional methods that struggle to maintain temporal consistency across frames.

### Weaknesses
First, the paper’s structure requires improvement, as the current organization makes it challenging to follow. 
A major concern is the lack of a comprehensive comparison between this approach and conventional methods, such as VidToMe and Upscale-A-Video. VidToMe introduces local and global token merging techniques, while Upscale-A-Video presents a flow-based merging approach—both key contributions relevant to this work. Please clarify how this approach differentiates itself from these methods, and refer to the “Questions” section for further details.

### Questions
1. VidToMe is implemented on top of Stable Diffusion. In Table 1, the proposed approach (based on Stable Diffusion (SD x4)) is compared with VidToMe, but it does not seem to demonstrate performance gains over VidToMe in terms of objective image quality (PSNR/SSIM) or temporal consistency (E_warp). On the other hand, perceptual quality metrics, such as LPIPS, show improved results. Could you clarify if there is a specific reason why perceptual quality metrics like LPIPS perform better? If there is a trade-off involved, would it be possible to show how performance varies with adjustments to the hyperparameters?
2. Although the proposed method emphasizes compatibility with any 2D image restoration diffusion model, the comparison results in Table 1—before and after applying the proposed method on SD x4—show only modest performance gains, whereas the improvements over the DiffBIR baseline are more substantial. Could you please clarify if there is a specific reason for this difference or if there is any dependence on specific network architecture?
3. It appears that the code for Upscale-A-Video is now available. Since this approach also aims to improve temporal consistency across video frames generated by image generation models, it would be beneficial to include a comparison of the results. If the code is still unavailable, could you instead provide results on the datasets used in Upscale-A-Video and compare them with the figures reported in the Upscale-A-Video manuscript?

### Soundness
3

### Presentation
3

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
This paper proposes a training-free method to leverage pre-trained image restoration diffusion models for zero-shot video restoration. Specifically, the proposed method employs hierarchical latent warping and an enhanced token merging strategy to maintain temporal consistency and restore details across video frames. Experimental results demonstrate the versatility of the method across various tasks, including denoising, super-resolution, and depth estimation.

### Strengths
1. The proposed method is pioneering in achieving zero-shot video restoration by leveraging pre-trained image restoration diffusion models, enabling multiple video restoration tasks without additional training.
2. The method presents strong quantitative and visual results compared with state-of-the-art methods, balancing temporal consistency and detail generation.

### Weaknesses
1. In line 267, the authors claim that the combination of hierarchical latent warping and hybrid flow-guided spatial-aware token merging could achieve adaptation to various degradation types. However, it is not sufficiently discussed that why the combination could handle various degradation types. Specifically, the paper lacks a detailed analysis of how different degradation characteristics (e.g., blur, noise, compression artifacts) are addressed by the proposed method's components. The interaction between the hierarchical warping and token merging is not clearly explained in the context of varying degradation types. For example, it is unclear how the method would adapt to severe blur versus high levels of noise.
2. While the use of optical flow guidance aligns with previous video restoration works [1,2], the paper introduces similarity-based guidance to capture correspondences distinct from optical flow. However, the specific benefits of similarity-based guidance over optical flow are not thoroughly discussed. The paper does not provide a clear explanation of when and why similarity-based guidance is more effective than optical flow, especially given that optical flow is a well-established technique for motion estimation. A more detailed analysis of the conditions under which each guidance method excels is needed.
3. Although recent video restoration methods, such as Shift-Net and FMA-Net, are included as baselines, some classic methods like BasicVSR++ and RVRT are not compared in the experiments. This omission makes it difficult to assess the proposed method's performance against established benchmarks. The lack of comparison with these classic methods, which are known for their strong performance in terms of PSNR and SSIM, raises questions about the method's overall competitiveness.

### Questions
1. Is there a comparison of inference efficiency with baselines?

### Soundness
3

### Presentation
3

### Contribution
3
