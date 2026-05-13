# CasualHDR: Robust High Dynamic Range 3D Gaussian Splatting from Casually Captured Videos

- Decision: Reject
- Scores: 6, 3, 5

## Abstract
In recent years, thanks to innovations in 3D scene representation, novel view synthesis and photo-realistic dense 3D reconstruction from multi-view images, such as neural radiance field (NeRF) and 3D Gaussian Splatting (3DGS), have garnered widespread attention due to their superior performance. However, most works rely on low dynamic range (LDR) images and representations of scenes, which limits the capturing of richer scene details. Prior works have focused on high dynamic range (HDR) scene recovery, typically require repeatedly capturing of multiple sharp images with different exposure times at fixed camera positions, which is time-consuming and challenging in practice.For a more flexible data acquisition, we propose a one-stage method: \textbf{CasualHDR} to easily and robustly recover the 3D HDR scene from casual videos with auto-exposure (AE) enabled, even in the presence of severe motion blur and varying exposure time. CasualHDR contains a unified differentiable physical imaging model which jointly optimize (i.e. bundle adjust) exposure time, camera response function (CRF), continuous-time camera motion trajectory on $\mathbb{SE}(3)$, and the 3DGS-based HDR scene. Extensive experiments demonstrate that our approach outperforms existing reconstruction methods in terms of robustness and rendering quality. Three applications can be achieved after the 3DGS HDR scene reconstruction: novel-view synthesis, image deblurring (deblur input images) and HDR editing (adjust the exposure time thus brightness of the input images).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces CasualHDR, a high dynamic range (HDR) scene reconstruction method based on 3D Gaussian Splatting (3DGS). This approach can reconstruct 3D HDR scenes from casually captured videos, even if they include automatic exposure adjustments and motion blur. CasualHDR relies on a physical image formation model to jointly optimize exposure time, the camera response function (CRF), continuous camera motion trajectory, and HDR scene representation. The authors conducted extensive experiments, showing advantages in image quality and robustness, and demonstrated the potential of this method for applications like novel view synthesis, deblurring, and HDR editing.

### Strengths
1. CasualHDR does not require precise exposure times as input, which significantly reduces data collection costs and improves adaptability to various exposure conditions and blurry situations.
2. This method shows good image quality and can produce realistic HDR reconstructions even in scenes with uneven exposure and extreme lighting changes.
3. The method demonstrates versatility, including applications in novel view synthesis, deblurring, and exposure adjustment, showing potential value in real-world scenarios.
4. Extensive experiments on multiple synthetic and real datasets show its performance in image quality and positional accuracy, proving the method's practicality and robustness.

### Weaknesses
1. ***Limited novelty***: The method combines 3D Gaussian Splatting (3DGS) with a physical image formation model, mainly adapting HDR-NeRF’s MLP tone mapping for CRF handling and BAD-Gaussians' camera motion modeling. Although this integration is effective, it largely builds on existing techniques with limited original innovation. While CasualHDR’s addition of exposure time optimization could enhance flexibility in varying lighting, the lack of error analysis for these estimates raises concerns about the accuracy and robustness of this component.

2. ***High computational cost***: The method processes CRF on a per-pixel basis, which significantly increases computation, especially with high-resolution images or large datasets, potentially limiting its applicability in real-time scenarios.

3. ***Accuracy of exposure estimation***: Although the authors claim the optimization effectively estimates exposure time, they do not provide detailed error analysis or comparisons with ground truth exposure times, which raises questions about its robustness.

### Questions
1. Given that CRF is applied on a per-pixel basis, which increases computation time significantly for high-resolution or large-scale images, could the authors provide details on the training time and rendering speed for exposure editing? Additionally, are there optimization strategies to address this?

2. Could the authors include an error analysis comparing the optimized exposure times with the ground truth to demonstrate the effectiveness of the exposure time optimization?

3. Could the authors provide comparisons of the learned CRF curves with ground truth or typical CRF shapes from the literature to illustrate the effectiveness of the CRF modeling?

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
The authors of this paper propose a new problem: how to recover an HDR scene from a blurry LDR videos captured with a handheld camera under different exposures.

### Strengths
1. The authors propose a novel problem: how to recover an HDR scene from casual LDR videos that exhibit ghosting blur.  
2. To validate their method, the authors created their own dataset and conducted detailed experiments on it.

### Weaknesses
1. The authors do not propose a new method; they simply combine existing approaches. While this does present certain challenges, it is not novel.
2. The authors claim that their method is an HDR reconstruction method; however, I did not find any HDR measurement results, such as HDR-VDP, PUPSNR.
3. Line 36, "Prior works have focused on high dynamic range (HDR) scene recovery, typically require repeatedly capturing of multiple sharp images with different exposure times at fixed camera positions, which is time-consuming and challenging in practice" This statement raises a question, as current HDR reconstruction methods do not require capturing multiple clear images at fixed camera positions with different exposure times. For example, HDRNeRF can reconstruct an HDR radiance field using just a single image from 18 different viewpoints.
4. The teaser illustration contains errors: xxx(ours).
5. Providing the videos may be more convincing.

### Questions
1. Why did you choose to model the CRF using an MLP instead of an explicit method? An explicit method would likely be faster.

### Soundness
2

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
5

### Summary
This work proposes a method, dubbed CasualHDR, for 3D HDR scene reconstruction from casual videos with auto-exposure (AE) enabled, even in the presence of severe motion blur and varying exposure time. The camera's continuous motion trajectory is introduced to initialize the 3DGS point clouds. The physical camera formation imaging model is used to simulate the motion blur and exposure change. The CasualHDR framework can jointly optimize continuous-time camera trajectory, CRF, exposure time, and 3DGS-based HDR representation.

A dataset including synthetic and real scenes is collected.

### Strengths
(1) The idea of jointly optimizing the camera trajectory, CRF, exposure times, and 3DGS is interesting and fancy. Because the error of the camera poses sometimes causes pixel misalignment on 2D renderings, which is usually ignore by previous methods. Besides, using the physical image formation model to jointly fit the motion blur of camera movement and exposure change is also interesting. Although using cumulative $\mathbb{SE}$(3) B-spline is a widely used continuous-time trajectory representation in robotics, it has been less studied in 3D reconstruction, especially in HDR imaging. The authors explore this part.


(2) The layout of this paper is good and clear. The teaser figure and pipeline figure are attractive. I like this style. 

(3) The ablation study results in Table 6 are sufficient to validate the effectiveness of the proposed techniques. The visual comparison is also sufficient to demonstrate the advantage of the proposed method.

### Weaknesses
(1) The writing should be improved. Some sentences are redundant. For example, in Line 56 - 58, the authors use multiple present continuous tenses, which makes the sentence hard to read. There are also many writing typoes, such as "impoving" in Line 97 should be rectified to "improving". "$\hat{C}k(x)$" should be modified to "$\hat{C}_k(x)$". Most importantly, the method part is a mess. The first three sections seem like three independent techniques. The authors should write the relationship between them. How do they correlate and cooperate with each other? What is the pipeline? But unfortunately, I did not find this, which makes the pipeline hard to follow and incomprehensible.

(2) Some statements in this paper are confusing and even non-convincing. For instance, in Line 75 - 76, the authors claimed, " accurate exposure time is usually expensive due to the use of professional equipment". However, most of common digital cameras can easily read or just directly set the exposure time of the photos. Meanwhile, the authors themselves use the exposure time in their proposed CasualHDR. In Eq.(1), what does $\mathbf{R}_c$ represent? In Section 3.2, what does the $\mathbb{SE}(3)$ mean? It is very confusing to directly use it without any introductions. 

(3) In the loss function of Eq.(8), I did not see any HDR supervision. Previous works usually use HDR supervision to constrain the rendered HDR images like HDR-NeRF. But why this work does not use HDR constraints? I check all the visual comparisons in the paper and find that the so-called HDR images have very limited luminance intensities. For example, the results in Figures 3, 4, and 5 still suffer from under- and over-exposure problems. Especially in figure 4. The details in the over-exposure area cannot be seen.  In general, the render images in this work are low-resolution and low-quality.

(4) The novelty is poor. The core technique - 3D Gaussian Splatting for HDR imaging has been explored by HDR-GS [1], which has been published by NeurIPS 2024. The techniques are similar in using tone-mapping, SfM for initialization, exposure time adapting, 3DGS rasterization, etc. However, this paper does not discuss and compare HDR-GS, which makes the contributions weaker. The motion blur estimation in the physical imaging model has been proposed and studied in Deblur-NeRF [2] and Deblur-GS [3]. However, the authors did not mention this and also did not compare with these two methods. This is not good.

[1] HDR-GS: Efficient High Dynamic Range Novel View Synthesis at 1000x Speed via Gaussian Splatting. In NeurIPS 2024.

[2] Deblur-nerf: Neural radiance fields from blurry images. In CVPR 2022.

[3] Deblur-GS: 3D Gaussian Splatting from Camera Motion Blurred Images. In ACM I3D 2024.

(5) By the way, the results of HDR editing seem like LDR results. It would be better if the main table could report the HDR and LDR results under different exposures, respectively, just like HDR-NeRF. The running time comparison is also very important.

(6) The source code and pre-trained models are not submitted. The reproducibility cannot be checked.

### Questions
I am curious about the results on the datasets collected by HDR-NeRF, especially the comparison (PSNR, SSIM, LPIPS, running time) with HDR-GS.

Why did you collect another dataset? Is this because of the requirement of continuous-camera trajectory?

### Soundness
2

### Presentation
1

### Contribution
2
