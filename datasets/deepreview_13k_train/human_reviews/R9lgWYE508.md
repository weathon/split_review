# Relaxing Accurate Initialization Constraint for 3D Gaussian Splatting

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
\vspace{-5pt}
3D Gaussian splatting (3DGS) has recently demonstrated impressive capabilities in real-time novel view synthesis and 3D reconstruction. However, 3DGS heavily depends on the accurate initialization derived from Structure-from-Motion (SfM) methods. When the quality of the initial point cloud deteriorates, such as in the presence of noise or when using randomly initialized point cloud, 3DGS often undergoes large performance drops. To address this limitation, we propose a novel optimization strategy dubbed \textbf{RAIN-GS} (\textbf{R}elaxing \textbf{A}ccurate \textbf{IN}itialization Constraint for 3D \textbf{G}aussian \textbf{S}platting). Our approach is based on an in-depth analysis of the original 3DGS optimization scheme and the analysis of the SfM initialization in the frequency domain. Leveraging simple modifications based on our analyses, \textbf{RAIN-GS} successfully trains 3D Gaussians from sub-optimal point cloud~(e.g., randomly initialized point cloud), effectively relaxing the need for accurate initialization. We demonstrate the efficacy of our strategy through quantitative and qualitative comparisons on multiple datasets, where \textbf{RAIN-GS} trained with random point cloud achieves performance on-par with or even better than 3DGS trained with accurate SfM point cloud.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This submission investigates the initialization strategy commonly used in existing 3D Gaussian Splatting (3DGS) optimization schemes. The authors present some technical insights towards the question of why the 3DGS optimizers tend to perform poorly when the centers of the 3D Gaussians are initialized from random values. They coin a new term in the paper and call the phenomena “low Gaussian transportability”. The authors also argue that the sole use of photometric error leads to the aforementioned limitation.

To address the observed limitations in optimizing 3DGS representations from noisier initialization, the authors have proposed some remedies, such as a) starting with fewer Gaussians with significantly larger covariances, applying low pass filtering progressively, introducing heuristics for reducing the gaussian size as the optimization progresses and the number of Gaussians in the scene increase, new splitting criteria.

Empirically these ideas lead to incremental improvements on the popular datasets (Mip-NeRF 360, RealEstate 10K, Tanks & Temples, Deep Blending) in terms of standard metrics (pSNR, SSIM, LPIPS, etc.). An ablation study was also reported to measure the benefit of each of the proposed modifications in isolation.

### Strengths
The authors propose certain modifications to the initialization steps prior to optimizing 3D Gaussian splatting representations. It leads to small but consistent improvements in the reconstruction quality on several datasets especially when the optimizer is started with noisy or random initialization of the 3D point coordinates. In general, the arguments and insights they present sounds reasonable in theory and seems to be helping in practice as shown in the empirical results.

### Weaknesses
The authors try to improve 3DGS performance when the Gaussians are initialized from random 3D points. While their results show some promise towards that end, they however assume that the camera poses are accurate. Typically, a full SfM pipeline must be executed to obtain accurate camera poses – must run bundle adjustment till completion. When running a full BA, accurate points are typically obtained as a by-product and no extra computation is needed. So, in other words, I don’t see a compelling situation where the 3DGS optimizer must be initialized from a random 3D point cloud when accurate camera poses are already available. In case of Re10K, the 3D points could be initialized using triangulated feature matches where both matching and triangulation could leverage the accurate poses.

However, it becomes much more interesting and relevant when camera poses are obtained from a different source and not necessarily extremely accurate.

While the paper is readable, the main paper lacks sufficient technical detail. The authors introduce the idea of limited Gaussian portability but in Section 4.2 there is an empirical study on the Mip-NeRF360 dataset without any deeper insights. Notably other authors have already investigated the issue of local minima in the optimization landscape. So I am not convinced that this paper extends the insight beyond what is already known in the literature. So I would argue against the first claimed contribution on page 2 “For the first time, we conduct an in-depth analysis and identify … “.

The ideas of improving the initialization seem reasonable but none of these modifications guarantees escaping local minima. For example, the authors state in Section 5.1 “To prevent the Gaussians from falling into local minima, we propose a simple yet effective modification to the original random initialization”. Even though some benefits of the proposed scheme are shown in the empirical evaluation, in the absence of any formal guarantees, the claims should be toned down a bit. Similarly, the specific split heuristic describes here (called ABE-Split) is a variation of existing splitting strategies and there is not much detail why this specific criteria should be used.

### Questions
I have a few comments .. 

Typo: 
page 2, were propose -> we propose

* Pan et al. 2024 accelerates the SfM pipeline but does not use learnable modules.
* In the abstract and in Section 1, the authors argue that solely using photometric loss is the main cause for poor optimization performance with noisy initialization. However, throughout the paper, the standard photometric loss continues to be used in the optimization objective without any modifications. Thus, it would help to put less emphasis on the particular point when motivating the problem.

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
5

### Summary
This paper aims to alleviate the initialization/densification problem in the original 3DGS, where regions are under-reconstructed in SfM. To solve the issue, the paper proposes initializing 3D Gaussians with larger variances so that Gaussians can cover more regions of the image and learn more about the global structure of the scene. Moreover, the paper proposes progressive low-pass filtering techniques to encourage Gaussians to receive more gradients during training. The paper also uses an adaptive bound-expanding split algorithm to overcome the limitation that the variance of Gaussians becomes small after multiple splitting steps. The experiments on the MipNeRF360 dataset and tanks-and-temples dataset show the effectiveness of the proposed method.

### Strengths
(1) The proposed method is simple to add to the existing 3DGS method

(2) The authors provide exhaustive experiments to verify the effectiveness of the proposed method

(3) The proposed method improves the original 3DGS clearly on the tanks-and-temples and the MipNeRF360 dataset.

### Weaknesses
(1) The ideas are intuitive and the contributions are not significant.

(2) While I appreciate their improvements to the original 3DGS methods, there are more variants of 3DGS, and I wonder would the same strategies proposed in this paper can improve the other 3DGS methods(such as scaffold-gs, etc).

(3) The method can improve 3DGS on the tanks-and-temples and MipNeRF360 dataset, I would like to see the effectiveness of this method on texture-less areas. And I would like to raise my score if the authors do so.

### Questions
The authors proposed the progressive low-pass filter to ensure 3D Gaussians receive more gradients during training. I wonder if is this equivalent to training 3D Gaussians from low-resolution images to high-resolution images in a coarse-to-fine manner. I would appreciate the authors to provide a fair comparison between the progressive low-pass filter and coarse-to-fine training strategy/

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to reconstruct Gaussian scenes using randomly initialized point clouds. The designs guide the Gaussian scenes to first establish a global structure, thereby avoiding local optima. Although relatively simple, this method even achieves superior reconstruction results in certain scenes compared to Colmap+3DGS. However, more experiments and analysis are needed to support the motivation.

### Strengths
1. This paper proposes to reconstruct Gaussian scenes using randomly initialized point clouds. In some cases, the proposed method surpasses Colmap+3DGS, which is impressive.
2. The proposed method encourages Gaussian scenes to first learn global structural information before focusing on detailed information.
3. The analysis in this paper is well-organized and clearly written.

### Weaknesses
1. The design in this paper mainly comes from experimental results. While the approach is simple and effective, it lacks theoretical novalities, and many hyperparameters require tuning. It would be beneficial for the authors to provide more detailed ablation experiments on these hyperparameters.

2. The paper assumes known multi-view image poses without point cloud reconstruction, but further analysis and explanation are needed regarding in which case this setting makes scene:
- If the image poses are obtained from sensors, how does the method handle pose errors? How much error can it handle? Should the poses being optimized to improve robustness? 
- If the multi-view images are generated from generative models, such as text-to-3D models, please validate the effectiveness of the proposed method in these cases.



### Questions
1. In Line 431, the authors mention that the reconstruction results are based on poses from sensors. Does the the pose errors impact the final reconstruction performance, and can the proposed method mitigate this issue?

2. As shown in Figures 1 and 3, why does the improvement mainly occur in edge regions or distant areas?

3. Some further discussions: With the recent advancements in monocular reconstruction algorithms, such as Dust3R and DepthPro, which allow for effective 3D reconstruction without relying on Colmap or even poses, would the proposed method conflict with or complement these approaches? Could case studies be conducted to explore this?

I might raise my rating if my concerns are addressed.

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
4

### Summary
This paper aims to alleviate the critical requirements for accurate initialization for 3DGS. The proposed RAIN-GS attributes the problem to limited Gaussian transportability. Based on this observation, it introduces a novel initialization strategy and adaptive density control strategy, as well as a progressive Gaussian low-pass filtering to resolve the problem.

### Strengths
1. Significance. Relaxing the initialization constraint of 3DGS is a critical and meaningful problem. The RAIN-GS realizes an impressive performance without the need of SfM points, proving it is an efficient solution.

### Weaknesses
1. As a submission to ICLR, it's not reasonable to only include 3DGS and Mip-Splatting for comparison. 2DGS sacrifices representation ability for more accurate geometry. Thus it's meaningless and unfair to compare with it purely on rendering quality. A more reasonable choice should be ScaffoldGS [CVPR24] or other improvements on ECCV24 or NIPS24, especially when they are randomly initialized.
2. The authors claim limited Gaussian transportation as a reason for the problem, and provide the analysis on movement of Gaussians as evidence. However, it remains unclear where do RAINGS's improvement comes from. The author should compare their method in both Table 2 and Figure 2 to validate the motivation and effectiveness of their method.

### Questions
1. The author claims that the limited Gaussian transportability is mainly due to suboptimal performance caused by exclusive reliance on image photometric loss. However, is there any possibility that the suboptimal results are from batch size 1 optimization? Can this problem be well resolved by simply using a parallel training paradigm like GrendelGS?
2. In Table 5, the author claims that when combined with the low-pass filter and ABE-Split algorithm, SLV initialization shows the best performance. However, there seems to be a lack of an experiment combining the proposed low-pass filter, N=100K, and ABE-Split to provide a comparison.

### Soundness
2

### Presentation
2

### Contribution
3
