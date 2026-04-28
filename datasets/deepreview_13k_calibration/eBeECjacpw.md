# PORF: POSE RESIDUAL FIELD FOR ACCURATE NEURAL SURFACE RECONSTRUCTION

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 5, 6

## Abstract
Neural surface reconstruction is sensitive to the camera pose noise, even if state-of-the-art pose estimators like COLMAP or ARKit are used. 
More importantly, existing Pose-NeRF joint optimisation methods have struggled to improve pose accuracy in challenging real-world scenarios. To overcome the challenges,
we introduce the pose residual field (\textbf{PoRF}), a novel implicit representation that uses an MLP for regressing pose updates.
This is more robust than the conventional pose parameter optimisation due to parameter sharing that leverages global information over the entire sequence.
Furthermore, we propose an epipolar geometry loss to enhance the supervision that leverages the correspondences exported from COLMAP results without the extra computational overhead.
Our method yields promising results. 
On the DTU dataset, we reduce the rotation error by 78\% for COLMAP poses,
leading to the decreased reconstruction Chamfer distance from 3.48mm to 0.85mm. 
On the MobileBrick dataset that contains casually captured unbounded 360-degree videos, our method refines ARKit poses and improves the reconstruction F1 score from 69.18 to 75.67,
outperforming that with the dataset provided ground-truth pose (75.14).
Moreover, we integrate our method into the Nerfstudio library, consistently improving performance in diverse challenging scenes.
These achievements demonstrate the efficacy of our approach in refining camera poses
in real-world scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a novel approach in refining the inaccurate camera pose and thereby improving neural surface reconstruction. 

The paper presents two key innovations: Pose Residual Field (PoRF) and a robust epipolar geometry loss. PoRF, an implicit pose representation, uses an MLP network to learn pose residuals, considering global information across all frames for enhanced performance. The epipolar geometry loss, used for better supervision, relies on feature correspondences.

The method shows significant improvements in accuracy and efficiency in camera pose refinement. It outperforms existing methods like BARF and SPARF, particularly in datasets like DTU and MobileBrick.

### Strengths
- The utilization of global data across all frames by PoRF marks a notable advancement compared to techniques that individually optimize each image. This approach significantly enhances the refinement of camera poses, thereby achieving greater accuracy and efficiency in reconstructions. 
- Additionally, the method proves to be highly effective in adjusting poses from various sources, such as COLMAP and ARKit, demonstrating top-tier performance in practical, real-world dataset applications.

### Weaknesses
I've noticed that the concept of applying Epipolar Constraints in situations involving inaccurate or absent poses has been previously examined in [1]. It would be interesting to see if there's any discussion or comparison of this aspect in the context of PoRF's approach.

### Questions
Considering that reference [1] is already available, I would appreciate it if you could provide some insight into how the PoRF Epipolar Geometry loss presents a novel approach compared to the 3D loss mentioned in [1].

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript introduces the use of an additional small MLP to refine the poses given to neural reconstruction methods jointly with the standard neural reconstruction objective. An additional epipolar loss derived from sparse feature matching (like SIFT matches from COLMAP) is used to effectively supervise this residual pose network.
This small addition if a learned shared pose residual update has big impacts on the quality of the reconstruction as demonstrated in the experiments. Notably it outperforms considerably the direct optimization of the poses with the standard reconstruction loss formulation.

### Strengths
The addition of the pose residual learning with a small MLP is a straight forward addition to any neural representation learning method. 
The fact that sparse correspondences needed for the epipolar loss are available from COLMAP without additional cost is an added benefit that makes it easy to incorporate into existing methods.

The quantitative experiments are high quality and compare the proposed approach against a diverse set of existing methods. They clearly show the improvements in reconstruction quality and pose estimation.

The additional ablations wrt to different algorithm settings are illustrative and help clarify that both PORF and epipolar line loss are needed to achieve high performance (Fig 5). As well as that the method can be used together with NERF (instead of just NeuS) and that SIFT matches are sufficient for the epipolar loss (vs more expensive deep learned LOFTR).

The qualitative results in Fig 1 and 6 very clearly show the ability of the poses residuals to correct for very noisy surfaces.

The manuscript is clear and well written and easy to follow except some details (see weaknesses).

### Weaknesses
The use of L1-L6 is unclear and not well introduced. To my knowledge this notation is not common to denote different experiments or ablations. I highly recommend introducing it upfront or using short acronyms to denote different configs. This would improve readability of the manuscript.

The effects of training the additional MLP and computing the additional epipolar loss is likely not significant when compared to training without them but it would still be good to quantify any difference in terms of overall time to convergence. If this additional time is negligible it could further support the use of PORF as a no-brainer. 

Its a minor thing but I am curious as to how much the time/frame id input is used by PORF. Ablating with and without time input would show whether PORF mostly compensates for global shifts or whether it can learn to fix individual poses. Furthermore, it is unclear if the time input is simply an integer index or if it is encoded in some way before being fed to the MLP.

### Questions
The axis angle formulation for pose is a common way to parameterize updates to poses. It would be good to also clarify how the algorithm goes back from these to the full 4x4 (or 3x4) pose matrix used for transformations in the rest of the method.

In figure 4 there is a clear point at which the errors start growing linearly where before they were sub-linear. I am curious why the authors think this happens.

Is any position encoding used for the time/frame id input to PORF?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper targets the optimization of camera pose for neural surface reconstruction. For handling the camera pose noise and intensive-view scenarios, this paper introduces PoRF, which learns the pose residuals (i.e., offset) by the frame index and initial camera pose. Moreover, the epipolar geometry loss is used to enhance supervision for camera pose estimation.  Along with the volume rendering and reconstruction loss in NeuS as the baseline, the proposed method shows high accuracy and robustness in intensive-view scenarios and a noisy initial camera pose. The proposed method is validated on the DTU and MobileBrick datasets, respectively. It uses the COLMAP and ARKit poses as the initial camera poses and achieves better camera poses and reconstruction results compared to other SOTA.

### Strengths
- The proposed method is simple yet effective for joint optimization of camera pose and neural surface reconstruction.
- The results are impressive. Tabs. 1-4 show the proposed method achieves high-quality camera pose estimation and neural surface reconstruction. Moreover, Figs. 3-5 show the proposed method is robust to noise.
- The paper is well organized and easy to follow.

### Weaknesses
[Fig.2] Based on Eq.6, $\alpha$ should multiply the residuals. However, Fig.2 shows $\alpha$ multiply the input.

[Ablation of PoRF]
- [Shared MLP] The paper claims that the shared MLP captures the underlying global information and therefore boosts performance. However, this is not discussed in Fig.S5 or ablation study.
- [$\alpha$] It would be better to discuss the use of $\alpha$ like w/ and w/o the fixing factor $\alpha$ and its value. This is not discussed in Fig.S5.

[Design of PoRF] The PoRF formulates camera pose estimation as a pose refinement procedure, which takes initial poses as input and predicts the offsets. The final prediction is the initial poses plus the offsets. This paper claims the PoRF was inspired by Nerf and can be treated as one of its main contributions. However, similar modules like recurrent pose refinement or iterative offset regression are a standard module in pose estimation, including 6D object[1,4] or human pose estimation[2,3]. Compared to existing modules, PoRF only introduces an additional index as input. This makes the novelty incremental. It would be better to highlight the difference or advantage of PoRF compared to those existing modules.


[Epipolar] Similar Epipolar geometry contraints are also used in multi-view tasks like [5,6]. They all extract keypoints and then use Sampson distance. The framework is like a combination, which limits its novelty.

### Questions
See Weaknesses. My main concern is the novelty.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes an approach called PoRF for robust neural surface reconstruction with noisy camera pose initialization. The method leverages an MLP for regressing pose updates, which is more robust and accurate than conventional pose parameter optimization. The proposed method also includes an epipolar geometry loss to enhance supervision, which leverages correspondences exported from COLMAP results without limited computational overhead. The paper presents experiments on the DTU and MobileBrick datasets, demonstrating the efficacy of the proposed approach in refining camera poses and improving the accuracy of neural surface reconstruction in real-world scenarios.

### Strengths
1. The proposed method is claimed to be more robust than conventional methods due to parameter sharing that leverages global information over the entire sequence.
2. The paper presents extensive experiments on the DTU and MobileBrick datasets, demonstrating the efficacy of the proposed approach in refining camera poses and improving the accuracy of neural surface reconstruction in different scenarios.
3. This paper is well-written and easy to understand, with clear explanations of the proposed method and experimental results.

### Weaknesses
1. It is a little unclear to me why using a single MLP for pose regression can improve pose optimization performance. Did you try to use multiple MLPs (one MLP for one frame)? Although it is claimed that one single MLP can leverage the global context information, it is not very convincing to me. Specifically, the mechanism through which a single MLP, trained across the entire sequence, implicitly learns and corrects pose errors is not well-explained. The paper lacks a clear justification for why parameter sharing across the sequence leads to better pose estimation than optimizing each pose independently or using a separate MLP per frame. This needs further clarification and potentially a more detailed theoretical explanation or ablation study.
2. Why should your method even outperform NeuS in Table 2 with GT poses? Does it mean your optimized pose is better than GT's or GT poses are also erroneous? If the GT poses are indeed accurate, then the result suggests that the pose optimization is somehow overfitting to the training data or the surface reconstruction is biased by the pose refinement, which would be a concern. The paper should clarify this counterintuitive result.
3. The proposed method was only evaluated on two ideal object-centric datasets, which cannot demonstrate the generalization ability to different types of real-world data. I suggest the authors consider testing their performance on datasets like KITTI and mipnerf 360's dataset. The lack of evaluation on more diverse and challenging datasets raises questions about the robustness and applicability of the method in less controlled environments.
4. In Eq. (7), the square of the inlier rate is used to weigh the loss terms. Why did you just simply use squares rather than other forms, e.g., cubic? Is this just an intuitive design or a careful selection after experiments? The paper does not provide any ablation study or justification for this specific choice of squaring the inlier rate, which makes it seem like an arbitrary design decision.

### Questions
Please refer to the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
