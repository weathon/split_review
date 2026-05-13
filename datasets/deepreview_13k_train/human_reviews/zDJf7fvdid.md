# Zero-shot Novel View Synthesis via Adaptive Modulating Video Diffusion Process

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
By harnessing the potent generative capabilities of pre-trained large video diffusion models, we propose a new novel view synthesis paradigm that operates \textit{without} the need for training. The proposed method adaptively modulates the diffusion sampling process with the given views to enable the creation of visually pleasing results from single or multiple views of static scenes or monocular videos of dynamic scenes. Specifically, built upon our theoretical modeling, we iteratively modulate the score function with the given scene priors represented with warped input views to control the video diffusion process. Moreover, by theoretically exploring the boundary of the estimation error, we achieve the modulation in an adaptive fashion according to the view pose and the number of diffusion steps. Extensive evaluations on both static and dynamic scenes substantiate the significant superiority of our method over state-of-the-art methods both quantitatively and qualitatively. The source code can be found on the anonymous webpage: https://github.com/PAPERID5494/VD_NVS. We also refer reviewers to the Supplementary Material for the video demo.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work introduces a diffusion model-based approach to achieve novel view synthesis. In particular, it leverages the depth-warped views as guidance to achieve adaptative modulation. Experiments on single-view images, multi-view images, and monocular video input-based novel view synthesis showcase the efficacy of the introduced methods.

### Strengths
* The idea of using depth-warped images as guidance for novel view synthesis is reasonable.
* It is interesting to see that the temporal consistent video diffusion model can be effectively reformulated to achieve geometrical consistent NVS in a training-free manner.
* Experiments on several challenging settings, including 360-degree NVS from a single view, verify the significance of the introduced method.

### Weaknesses
 * Accessing the geometry accuracy. For the 360-degree case, e.g., the truck, it would be better to apply mesh reconstruction on the rendered views, similar to Fig. 5(b) in latentSplat [Wewer et al. ECCV 2024]. The reconstructed mesh will provide a clearer understanding of how well the rendered views maintain correct geometry.

* Pixel-aligned metrics. For the NVS task, it would be better to report comparisons with state-of-the-part methods regarding pixel-aligned metrics, e.g., PSNR and SSIM. 

* Discussion with feed-forward 3DGS models. It might be interesting to see comparisons with detailed analysis between the introduced methods and those feed-forward 3DGS models, e.g., pixelSplat [Charatan et al., CVPR 2024], MVSplat [Chen et al., ECCV 2024]. And it would be better to consider adding these methods to the related work for better coverage of recent NVS works.

### Questions
Kindly refer to [Weaknesses].

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a NVS method that leverages large pre-trained video diffusion models without additional training. The approach adaptively modulates the diffusion sampling process using input views to produce high-quality results from single or multiple views of static scenes or dynamic videos. Theoretical modeling is used to iteratively adjust the score function based on scene priors, enhancing control over the diffusion process. The modulation adapts to view pose and diffusion steps.

### Strengths
1. The proposed approach is entirely training-free, meaning it directly leverages pre-trained large video diffusion models without requiring additional fine-tuning or retraining. This feature not only reduces computational demands but also makes it adaptable to a wide range of applications where time or resources for training may be limited. The flexibility of using pre-trained models enhances its practicality, allowing users to apply this method to various scenes and tasks with minimal setup.

2. The generated videos maintain high visual fidelity, delivering smooth results. This quality stems from the adaptive modulation of the diffusion process, which effectively incorporates scene details and structures from the given views, ensuring that outputs are kind of realistic.

3. The method is underpinned by theoretical modeling, which guides its adaptive modulation strategy. By iteratively adjusting the score function with scene priors and analyzing estimation error boundaries, the approach achieves both controlled and adaptive modulation of the diffusion process.

### Weaknesses
1. The comparison between this method and NeRF-based methods is fundamentally imbalanced. NeRF techniques incorporate an underlying 3D structure, enabling them to render any view with predictable performance, as the 3D structure informs which views are feasible and which are not. In contrast, the proposed method lacks an explicit 3D representation, limiting its view synthesis capabilities to specific views with no guarantee of consistent performance. This distinction is significant, as NeRF's inherent 3D information allows interpretable, reliable results across views, whereas this method’s output reliability is less predictable and may vary based on input views. The lack of a 3D structure also means that the method cannot reason about occlusions in the same way as NeRF, potentially leading to inconsistencies when generating views that require understanding of scene depth.

2. To achieve a fair comparison between the proposed method and NeRF-based techniques, the authors should first reconstruct a 3D model from the output video of this method and then re-render the scene from that reconstructed model. This process would allow for a direct assessment of both methods’ rendering consistency and quality, ensuring that comparisons consider the 3D structure NeRF inherently leverages. Also, reconstruction error like PSNR should be reported. The absence of a 3D reconstruction step makes it difficult to assess the geometric accuracy of the proposed method's output, and without metrics like PSNR, it's hard to quantify the quality of the reconstruction.

3. The video results of the proposed method exhibit visible flickering artifacts, which could substantially affect reconstruction quality and consistency. A deeper analysis is needed to assess how these artifacts impact overall reconstruction accuracy and to identify potential mitigation strategies. This might include tuning reconstruction parameters to minimize flickering, which would help improve the method’s output stability and robustness, especially for applications sensitive to temporal consistency. The flickering suggests instability in the diffusion process, and a more thorough investigation into the causes of this instability is needed.

4. A major contribution is the derivation of the parameter $\lambda$ in Section 4.2, which aims to minimize the estimation error upper bound in Equation 15. However, a gap remains between this upper bound and the actual estimation error represented in the left side of Equation 15. To strengthen the theoretical foundation, the authors should provide a more comprehensive analysis of how reducing the upper bound affects the actual estimation error. This could be achieved through statistical analysis and empirical evidence showing how well the method reduces estimation error in practice, thereby validating the theoretical assumptions. The theoretical analysis needs to be more tightly coupled with the empirical results to demonstrate the practical impact of minimizing the error bound.

### Questions
For dynamic scene comparison, it is said "For monocular video-based NVS, we downloaded nine videos from YouTube, each comprising 
frames and capturing complex scenes in both urban and natural settings." 

Why not just following the dynamic nerf settings? They have well aligned ground-truth for measuring the reconstruction performance.
Generation metrics like FID are not that reliable.

Soma example datasets are HyperNerf, DyCheck (https://hangg7.com/dycheck/)

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
3

### Summary
1. This paper proposes a novel view synthesis pipeline without any training. The pipeline can take single or multiple views of static scenes or monocular videos of dynamic scenes as input.
2. This paper modulates the score function with the warped input views to control the video diffusion process and generate visually pleasing results. They achieve the modulation in an adaptive fashion based on the view pose and the number of diffusion steps.
3. They conduct extensive results on both static and dynamic scenes and show promising results with both evaluation numbers and visualizations.

### Strengths
1. The proposed adaptive modulation of the score function in the diffusion process is novel.
2. The proposed method achieves better results in various scenarios compared to baselines.
3. The authors provide the code with an anonymous link, ensuring the applicability of the results.

### Weaknesses
My primary concerns are with the references and experimental details:

1. Some key references on diffusion-based NVS are missing [1,2,3,4,5,6,7]. Among these, [3] specifically focuses on scenes and has released its code. Is there a particular reason it was not included in the comparison? The absence of a comparison with this method, especially given its focus on scene-level synthesis, raises questions about the thoroughness of the experimental evaluation. Furthermore, the lack of discussion on how the proposed method compares to the specific architectural choices and training strategies employed by [3] makes it difficult to assess the relative strengths and weaknesses of the proposed approach.
2. How is the synthesized view pose calculated in this paper? In Line 364, it states that 'current depth estimation algorithms struggle to derive absolute depth from a single view or monocular video, resulting in a scale gap between the synthesized and ground truth images.' When calculating pose error, does the proposed method account for this scale gap? The paper should clarify whether the pose error is calculated using absolute or relative pose. If relative pose is used, the paper should explain how the scale ambiguity is resolved. If absolute pose is used, the paper should provide details on how the absolute scale is recovered, given the limitations of current depth estimation algorithms.

**Minor Points:**

1. In Table 1, it is stated that MotionCtrl [Wang et al., 2023b] and 3D-aware [Xiang et al., 2023] do not require training. However, as I understand, they do require fine-tuning.

### Questions
Line 415 mentions that the proposed method can achieve 360-degree NVS. Would it be possible to include a comparison with ZeroNVS [7] to better demonstrate its effectiveness?


[7] Sargent, Kyle, et al. "ZeroNVS: Zero-Shot 360-Degree View Synthesis from a Single Image." *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*. 2024.

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
4

### Summary
The authors propose a training free novel view synthesis paradigm based on video diffusion model. Specificcally, warped depth maps are utilized and certain sampling methods are proposed to ensure high quality NVS.

### Strengths
1. The work is complete and results seem to be good quantitively.

### Weaknesses
1. The work is complete, but the novelty and the contribution are not strong enough to meet the quality of ICLR. A good training-free is not that appealing after previous works like MotionCtrl, and it highly relys on the capability of SVD. It is hard to know about it generalizability around various video generation methods.
2. It is recommended to show "Directly guided sampling" and "Posterior sampling" clearly in the view of practical implementation. Some illustration would be appreciated.
3. Some equations should be displayed more clearly. For instance in eq.8, I(P_0) should not be related to the pose index i, but in eq.9 it is related to i. Maybe in eq.9 the I(P_0) should be revised as I(P_i)?

### Questions
Please refer to Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a training-free sampling method that generates image sequences conditioned on input camera trajectories. The input view is warped onto the target views, serving as pseudo-GT variables. To condition the reverse process, the paper re-computes the predicted mean of a reverse step with an interpolation between the predicted mean of the current noisy latent and the warped samples. It further explores calculating the optimal interpolation weight and two guidance methods (replacement and gradient). Both quantitative result and qualitative results show the proposed method can generate smooth, high-fidelity image sequences.

### Strengths
1. The paper presents a training-free method that enables a pre-trained diffusion model to generate image sequences based on given camera trajectories.
2. The qualitative videos demonstrate that the proposed method generates plausible outputs.

### Weaknesses
1. The paper's reliance on an off-the-shelf depth estimation network to warp input images raises concerns about potential scale inconsistencies across frames. Specifically, the use of a monocular depth estimation method like Depth-Anything introduces inherent ambiguity in the absolute scale, which can lead to inconsistencies when warping images across different viewpoints. These inconsistencies could propagate through the reverse process, ultimately affecting the fidelity of the generated image sequences. The authors should more thoroughly address the potential impact of depth estimation errors, particularly in the context of scale ambiguity, on the final outputs.

2. The paper does not adequately explain how occluded regions are handled during the depth-warping process. When the camera pose variation is large, the forward warping operation can create significant holes in the target image due to occlusions. The paper states that Eq. 12 is applied to unmasked regions, but it does not specify how the diffusion process generates content for the masked, occluded regions. This is a critical aspect, as naive handling of occlusions could lead to degenerate outputs in $\tilde{\mathbf{\mu}}_{t, \mathbf{p}_i}$, especially when significant portions of the target view are occluded.

3. The qualitative results primarily showcase camera trajectories with relatively small variations or 360-degree circular poses. While these examples are helpful, they do not fully demonstrate the robustness of the proposed method to larger camera variations. In scenarios with significant camera movement, the scale ambiguity from the depth estimation network could become more pronounced. To better evaluate the method's performance under challenging conditions, the paper should include examples with more substantial camera trajectories and diverse viewpoints.

4. The toy experiment in Fig. 2 (a) indicates that $\mathcal{E}_D$ decreases during the diffusion reverse process. However, it is unclear how the predicted means converge to the ground truth image (loss=0) when it is highly improbable to have sampled an $\mathbf{X}_t$ that would lead to the desired ground truth. A more detailed explanation of the experimental setup, including the specific steps of the reverse process and the relationship between $\mathbf{X}_t$, the predicted mean, and the ground truth, would enhance the understanding of this critical aspect.

5. The computation of the optimal interpolation weight $\lambda(t, \mathbf{p}_i)$ in Sec. 4.2 involves several assumptions. The paper lacks a comprehensive ablation study on the choice of this weight, presenting results only for the case where $\lambda(t, \mathbf{p}_i) = \infty$. To validate the proposed weight schedule, the authors should compare it against other reasonable alternatives, such as linear, constant, or exponential weight functions. Furthermore, the dependence of the interpolation weight on hyperparameters $\{ v_1, v_2, v_3 \}$ introduces a potential need for manual tuning on new scenes, which could limit the method's practicality. A more thorough investigation into the sensitivity of these hyperparameters is necessary.

6. While the paper presents promising results, the number of scenes used for evaluation is limited and differs from previous state-of-the-art methods. This raises concerns about the generalizability of the proposed method. A more extensive evaluation, encompassing a wider variety of scenes and conditions, is needed to fully validate the method's effectiveness.

### Questions
1. The proposed method sets the number of inference step to 100, which is quite large. Do other diffusion-based baselines also use the same number of inference step?
2. The paper mentions the camera trajectory is estimated (L.360). Could you provide more details on how the pose metrics (ATE, RPE) are computed?

### Soundness
2

### Presentation
2

### Contribution
2
