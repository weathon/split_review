# GAUSSIANFLOW: SPLATTING GAUSSIAN DYNAMICS FOR 4D CONTENT CREATION

- Decision: Reject
- Scores: 5, 6, 5, 8, 6, 5

## Abstract
Creating 4D fields of Gaussian Splatting from images or videos is a challenging task due to its under-constrained nature. While the optimization can draw photometric reference from the input videos or be regulated by generative models, directly supervising Gaussian motions remains underexplored. In this paper, we introduce a novel concept, Gaussian flow, which connects the dynamics of 3D Gaussians and pixel velocities between consecutive frames. The Gaussian flow can be efficiently obtained by splatting Gaussian dynamics into the image space. This differentiable process enables direct dynamic supervision from optical flow. Our method significantly benefits 4D dynamic content generation and 4D novel view synthesis with Gaussian Splatting, especially for contents with rich motions that are hard to be handled by existing methods. The common color drifting issue that happens in 4D generation is also resolved with improved Guassian dynamics. Superior visual quality on extensive experiments demonstrates our method's effectiveness. Quantitative and qualitative evaluations show that our method achieves state-of-the-art results on both tasks of 4D generation and 4D novel view synthesis. \\
    Project page: \href{https://zerg-overmind.io/GaussianFlow.io/}{https://zerg-overmind.io/GaussianFlow.io/}  
    
  
  
  
  \keywords{4D Generation \and 4D Novel View Synthesis \and 3D Gaussian Splatting \and Dynamic Scene \and Optical Flow. }

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel method that enhances 4D Gaussians using flow supervision. The authors introduce dense optical flow as a strong prior to supervise 4D Gaussians, ensuring the accuracy of motion. They implement the method in CUDA and demonstrate its efficiency. Experiments show that Gaussian-flow has the potential to model fast and complex dynamic scenes.

### Strengths
1. The authors propose a novel theory that demonstrates the efficiency of flow supervision.
2. The authors propose both 4D reconstruction and generation experiments to demonstrate the efficiency of their method.
3. Experiments show that this paper outperforms some important baselines in certain benchmarks.

### Weaknesses
1. I know there are some concurrent works focusing on flow-based Gaussian splatting, such as: "GFlow: Recovering 4D Worlds from Monocular Video" and "Motion-aware 3D Gaussian Splatting for Efficient Dynamic Scene Reconstruction." Please consider citing, comparing, or discussing these concurrent works.

2. The authors mention "CUDA with minimal overhead." Please provide more ablation studies and evaluation metrics(PSNR, memory, GPU, training times) on the reconstruction dataset and some generation benchmarks to support this claim.

3. I just think using optical flow as supervision can only enhance the quality of 4D Gaussians. It didn't solve the failure cases of 4D Gaussians (and the improvement is not strong, just ~0.5 PSNR). Therefore, I just think the novelty and the application of this method are limited.

### Questions
1. There are many other methods that use tracking models as their strong 2D priors. How do the authors incorporate tracking priors for 4D reconstruction and generation? What is the difference between this approach and using optical flow? Which method might be better?

2. What about applying flow supervision to other dynamic 3D Gaussian representations, such as 4D-GS (Wu et al., CVPR 2024), space-time Gaussians (Li et al., CVPR 2024), or 4D-Rotor-GS (Duan et al., SGA 2024)?

Overall, my main concerns are the lack of experiments, discussions and the importance of contributions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a novel flow rendering algorithm compatible with Gaussian Splatting. The key technical contribution lies in its approach to computing optical flow: it first normalizes pixel coordinates relative to the previous frame's Gaussian positions, then maps these pixels to their corresponding locations in the current frame's moved Gaussians, and finally calculates flow values through alpha blending. The algorithmic simplicity is kept while maintaining effectiveness. It is also a natural integration with existing Gaussian Splatting frameworks. I believe that it has a broad applicability across multiple domains.

### Strengths
There are two compelling reasons to accept the paper:

1. The paper introduces a plug-and-play flow rendering algorithm for Gaussian Splatting that leverages existing flow estimators and video trackers. The proposed flow supervision is particularly valuable as it extends beyond dynamic reconstruction to static scenarios where camera poses are unknown. When COLMAP fails or camera poses are unavailable, robust flow estimators can provide the necessary prior for bundle optimization of 3D Gaussians and camera poses. This simple yet effective solution for rendering Gaussian Flow represents a significant contribution to the field.

2. The paper presents a framework for 4D generation that utilizes flow supervision. While generating a front-view video is straightforward, the key innovation lies in how this framework effectively supervises dynamic Gaussians through flow rendering and supervision, taking the best use of limited front-view ground truths. This approach, though conceptually simple, solves a non-trivial technical challenge in 4D generation. Such an exploration of using flow loss in 4D generation is inspiring.

### Weaknesses
While the paper is generally sound, I have a few minor suggestions for improvement:

1. The paper should acknowledge and cite the flow rendering implementation found in "SC-GS: Sparse-controlled Gaussian splatting for editable dynamic scenes." Although their approach simply renders Gaussian mean shifts for flow mapping, a proper citation would help contextualize the current work's contribution.

2. To strengthen the paper's evaluation, I recommend including additional comparisons:
   - A novel view synthesis (NVS) comparison with SC-GS, the current state-of-the-art in this domain
   - A 4D generation comparison with "SC4D: Sparse-Controlled Video-to-4D Generation and Motion Transfer" (ECCV '24), which is now publicly available
These additional comparisons would provide more comprehensive validation of the proposed method's effectiveness.

### Questions
The paper's flow-rendering algorithm for 3D Gaussian Splatting shows promising potential beyond its demonstrated applications. I suggest expanding the discussion section to explore additional use cases:

1. Camera pose estimation and bundle adjustment, particularly for scenarios where traditional methods struggle without a flow prior
2. Creation of pseudo-ground-truth flow data using static scenes with known camera poses (accurate enough), which could serve as a novel benchmark for evaluating optical flow estimators

While extensive experiments in these directions might be beyond the current scope, including these potential applications in the future work section would highlight the broader impact of the proposed method and inspire further research in the community.

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
4

### Summary
The paper presents a novel approach, GaussianFlow, that enhances 4D content creation and novel view synthesis through Gaussian Splatting dynamics supervised by optical flow. The authors propose a “Gaussian flow” model to bridge 3D Gaussian dynamics and pixel velocities between consecutive frames, thus providing a more effective way to manage scene dynamics in 4D content. This approach addresses limitations in previous methods, especially in handling rich motion content and mitigating color drift artifacts in 4D generation.

### Strengths
1. The introduction of Gaussian flow represents a significant innovation. The paper successfully demonstrates how this concept enables dynamic supervision using optical flow, which is novel in the realm of Gaussian Splatting for 4D tasks.
2. The authors conducted extensive evaluations, showing state-of-the-art results in both 4D content generation and 4D novel view synthesis on multiple challenging datasets (Plenoptic Video, NeRF-DS, and Consistent4D). Improvements in PSNR and SSIM values across dynamic regions underscore the effectiveness of GaussianFlow in handling complex motion.
3. The paper includes valuable ablation studies, demonstrating that Gaussian flow supervision directly contributes to improved visual consistency and reduced motion-appearance ambiguity. This reinforces the effectiveness of GaussianFlow’s design choices.

### Weaknesses
1. The paper lacks comparisons with state-of-the-art methods in 4D lifting tasks, such as STAG4D (ECCV 2024), DreamMesh4D (NeurIPS 2024), DreamScene4D (NeurIPS 2024), Animate3D (NeurIPS 2024), and 4Diffusion (NeurIPS 2024).
2. For the 4D reconstruction task, results on single-camera scenes (e.g., Nerfies and Dycheck) would strengthen the evaluation, as these scenarios are more suitable and reasonable for flow supervision.
3. The paper focuses on modeling the flow of 3DGS but does not compare it with other methods that also utilize flow in 3DGS, such as CompactDy3DGS (ECCV 2024).

[1] Zeng, Yifei, et al. Stag4d: Spatial-temporal anchored generative 4d gaussians. ECCV 2024.

[2] Li, Zhiqi, et al. DreamMesh4D: Video-to-4D Generation with Sparse-Controlled Gaussian-Mesh Hybrid Representation. NeurIPS, 2024.

[3] Chu, Wen-Hsuan, et al. Dreamscene4d: Dynamic multi-object scene generation from monocular videos. NeurIPS. 2024.

[4] Jiang, Yanqin, et al. Animate3d: Animating any 3d model with multi-view video diffusion. NeurIPS. 2024.

[5] Zhang, Haiyu, et al. 4Diffusion: Multi-view Video Diffusion Model for 4D Generation. NeurIPS. 2024.

[6] Katsumata, et al. A compact dynamic 3d gaussian representation for real-time dynamic view synthesis. ECCV. 2024.

### Questions
Please, see the weaknesses section.

Overall, the approach to modeling gaussian flow and supervising it with a pretrained flow model in this paper is interesting. However, the results are not entirely convincing, as the paper lacks comparisons with state-of-the-art methods.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces GaussianFlow to differentiable render image-space flows induced by 3D Gaussian dynamics. The induced flow could help both 4D generation and 4D novel view synthesize by utilizing the optical flow supervision from nearby frames in the video. Experimental results show superior results over existing methods on multiple datasets for both tasks.

### Strengths
**Differentiable flow from Gaussian**

The proposed technique is quite useful for bridging the GS dynamics with pixel movement in the image space. The author also integrate the technique into the cuda, thus could enable various application in the community beneficial for generation and reconstruction. 


**Good illustration and figures**

Figure 1 and figure 7 shows the correctness of the method and provide a good illustration of how the algorithm works. 


**Good experimental results**

From the attached video and all experiments in the paper, I could see the better quality compared against RT-4DGS and other methods. It demonstrate the effectiveness of using optical flow supervision.


**Overhead**

By using the proposed strategy, it did add extra cost to the current pipeline but it shows the cost is within reasonable range with better performance.

### Weaknesses
**flow assumption on long-term or large movement**

The work only apply flow supervision on nearby frames, in the case if the fps is small or scene with large movement, I wonder will the technique and assumption still holds. The author mention their method is not suitable for long-term flow, I wonder is the restriction coming from inaccurate flow estimation or the basic assumption. 


**Ambiguity of optical flow**

In practice, given video with both camera and object motions, the 2D optical flow will be ambiguous. Under such scenario, how could the method still benefit from the optical flow supervision to achieve good quality results. I wonder what is the corresponding contribution of with and without optical flow supervision signal in this cases.

### Questions
For input with both object and camera motion, will the formula becomes different? Will the flow-cam be different in terms of formula given there is only view point change without point movement? Could the method be further used to decompose the object motion (by Gaussian movements) and camera motion given a video input?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors present a novel framework for generating 4D scenes. First, they propose using a Gaussian flow loss supervised by optical flow to model scene dynamics. Building on this representation, they extend it with the SDS loss from a generative model to facilitate 4D content generation.

### Strengths
The idea of combining Gaussian dynamics with pixel velocities is interesing. This approach is innovative and has the potential to inspire research in other topics.

### Weaknesses
See below.

### Questions
Although the experiments demonstrate the effectiveness of the proposed method, several concerns arise:

1. How do the authors handle Gaussian densification and pruning? If fixed Gaussians are used, how can the optimal number of Gaussians be determined?

2. Since pseudo labels from optical flow are utilized, what happens if the prior model’s predictions are incorrect or inaccurate? Could this lead to failure or blurring in the proposed method?

3. Is the flow loss applied only to the input video? For novel views, do we solely rely on the SDS loss?

4. The statement on line 340 mentions, "Since our method benefits 4D Gaussian-based methods more in regions with large motions." Could the authors clarify this point? 1) What is the relationship between the degree of motion and the performance of the proposed method? 2) It would be beneficial for the authors to include more visualizations to enhance understanding.

5. Scenes typically consist of dynamic foregrounds and static backgrounds. How does the proposed method affect these two types of regions? Can this method improve results for static scenes with optical flow supervision?

6. In the ablation studies, could the authors provide some quantitative analysis? Relying on demos is not sufficient to convincingly demonstrate the effectiveness of the proposed method.

7. Could the authors provide video visualizations and comparisons to illustrate the effectiveness of the proposed method more clearly?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Summary: This paper works on the task of video-to-4d, and the main contribution is adding optical supervision to the 4D generation and reconstruction task. To compute the 2D optical flow of dynamic gaussians, the authors carefully calculate the relationship between gaussian motions and 2D optical flows. They modify the original CUDA implementation of 3D Gaussian Splatting to achieve efficient optical flow rendering and loss back propogation. Experiments on 4D generation and reconstruction tasks validate the effectiveness of their designs.

### Strengths
1) It is natural to use 2D optical flow as supervison for 4D generation and reconstruction.
2) The paper is well-written and easy to follow
3) The authors validate their optical flow implementation on both generation and reconstruction tasks.

### Weaknesses
1) More comparison methods should be included in term of both 4D generation and 4D reconstruction. For example, 4DGen/STAG4D/Diffusion^2 for 4D generation and MotionGS for 4D reconstruction. Especially, MotionGS also adopts optical flow supervision for dynamic Gaussian, and I think it is necessary to point out how this work differ from that one.
2) The authors didn't provide the training time of the proposed method. For example, the comparison between training time w/ and w/o the proposed optical flow loss. This is important consindering efficiency of the proposed method.
3) Quantitative ablation on 4d generation task is suggested

### Questions
In related work part, L152, L4GM seems to be misclassified, it doesn't utilize text-to-video models.

### Soundness
2

### Presentation
2

### Contribution
2
