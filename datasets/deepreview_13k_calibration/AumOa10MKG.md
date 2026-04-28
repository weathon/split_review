# DisPose: Disentangling Pose Guidance for Controllable Human Image Animation

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 6, 8

## Abstract
Controllable human image animation aims to generate videos from reference images using driving videos. Due to the limited control signals provided by sparse guidance (e.g., skeleton pose), recent works have attempted to introduce additional dense conditions (e.g., depth map) to ensure motion alignment. However, such strict dense guidance impairs the quality of the generated video when the body shape of the reference character differs significantly from that of the driving video. In this paper, we present DisPose to mine more generalizable and effective control signals without additional dense input, which disentangles the sparse skeleton pose in human image animation into motion field guidance and keypoint correspondence. Specifically, we generate a dense motion field from a sparse motion field and the reference image, which provides region-level dense guidance while maintaining the generalization of the sparse pose control. We also extract diffusion features corresponding to pose keypoints from the reference image, and then these point features are transferred to the target pose to provide distinct identity information. To seamlessly integrate into existing models, we propose a plug-and-play hybrid ControlNet that improves the quality and consistency of generated videos while freezing the existing model parameters. Extensive qualitative and quantitative experiments demonstrate the superiority of DisPose compared to current methods. Project page: https://anonymous.4open.science/r/DisPose-AB1D.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a novel method for animating static human images into realistic videos using driving videos, without relying on additional dense inputs such as depth maps or DensePose. The authors present DisPose, which disentangles pose guidance into motion field estimation and keypoint correspondence. Specifically, they generate a dense motion field from a sparse motion field derived from skeleton poses and the reference image, providing region-level dense guidance while maintaining generalization. Simultaneously, they extract diffusion features corresponding to keypoints in the reference image and transfer these features to the target pose, enhancing appearance consistency and identity preservation. This approach is implemented as a plug-and-play hybrid ControlNet, allowing integration into existing human animation models without additional modifications to model parameters. Extensive qualitative and quantitative experiments demonstrate that DisPose outperforms current methods in both motion alignment and appearance consistency, effectively balancing generalizability and control effectiveness in pose-driven human image animation.

### Strengths
The strengths of this paper lays in the following several three folds:

1. The paper provides a clear and detailed explanation of the proposed method, including the construction of the tracking matrix from skeleton poses, Gaussian filtering, conditional motion diffusion, and the hybrid control network architecture. As well, the paper is well-organized, guiding the reader logically through the introduction, related work, methodology, experiments, and conclusions. This structure facilitates comprehension and highlights the contributions of the work.

2. The paper introduces DisPose, a novel framework that disentangles pose control into motion field guidance and keypoint correspondence. This innovative approach departs from traditional methods that rely heavily on dense control inputs, offering a new perspective on pose-guided human animation.

3. The DisPose module is designed as a plug-and-play component that can be seamlessly integrated into existing human image animation models. This versatility enhances the performance of baseline models without the need for extensive retraining.

### Weaknesses
The weakness of this paper lays in the following several three folds. My final rating is based on the discussion, and I would like to raise my score if some of the major concerns can be solved.

1. The experimental evaluation is primarily conducted on the TikTok dataset and an additional unseen dataset comprising 30 human videos. The reliance on these datasets raises concerns about the method's generalizability. e.g. the full body, side view.

2. The impact of the hybrid control network architecture, conditional motion diffusion process, and other auxiliary modules is not analyzed.
The figures shows promising visual results, such as the complete fingers and vivid facial expressions, so what proposed components lead to such enhanced visual details and visual improvements?

3. The evaluation employs VBench metrics and Fréchet Video Distance (FVD), which may not fully capture perceptual quality. The paper does not report other standard metrics such as Structural Similarity Index (SSIM) or Peak Signal-to-Noise Ratio (PSNR) for a more objective assessment.

### Questions
See the weakness section.

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
The paper presents DisPose, a ControlNet utilizing optical flow/motion fields to condition Latent Diffusion Models (LDM) for image animation and motion retargeting. Instead of using dense, template-based body pose signals like SMPL and OpenPose, DisPose leverages sparse keypoints and dense optical flow fields to better handle body shape variations between the reference and the target. 

Experimental results show improvement over prior work on VBench metrics.

### Strengths
The paper has the following strength:
- Simple, intuitive design to disentangle motion representation, and achieves better synthesis quality and appearance consistency.
- Plug-and-play potential: DisPose, when combining with previous approaches, improves the performance on the evaluated metrics.

Overall, the paper is well-written and easy to follow.

### Weaknesses
The paper has the following weaknesses:
- Lack of diversity in qualitative results. Both the figures, and the supp. videos focus mainly on re-animating generated/synthetic characters. These synthetic characters often have simplified, smoothed-out details, with very similar appearances and aesthetics. It is therefore unclear how the proposed method works on enhancing/improving realistic details. Particularly, since the paper already includes TikTok videos (that have real humans) for training and evaluation, it would be great if the paper can include those results. The absence of real-world human examples makes it difficult to assess the method's robustness to complex textures, lighting, and occlusions.
- Using optical flow is a good idea, but it may only work for static background. For noisy background, such as swaying trees and leaves, the motion field would likely capture those motion, and thus the model may incorrectly associate these background noises with the input motion. This could lead to artifacts in the generated video, where background elements appear to move along with the foreground character, or the character's motion is distorted by the background noise. The paper does not adequately address how the method handles such scenarios.
- Evaluation section can be further improved. It makes sense to use VBench due to the generative nature of DisPose. But at the same time, it is possible to check the appearance consistency by using the TikTok videos. One can split the video for the same subject into training and testing part, and examine whether DisPose/baselines can transfer the testing pose while preserving the subject identity. The current evaluation lacks a specific metric to quantify the identity preservation, which is crucial for animation tasks.

### Questions
My main concerns regarding this submission is the rigorousness of the qualitative and quantitative results, as stated above in the weakness section.

Please discuss these issues accordingly, and I will update my scores accordingly if the problems are sufficiently addressed or discussed. Note that the method/DisPose does not need to be perfect, but it is important to provide a comprehensive view of the proposed method.

### Soundness
2

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
4

### Summary
This paper proposes a plug-and-play method to disentangle pose guidance, which extracts robust control signals from only the skeleton pose map and reference image without additional dense inputs. The proposed method generates a dense motion field from a sparse motion field and the reference image, and extracts diffusion features corresponding to pose keypoints from the reference image. Extensive qualitative and quantitative experiments validate the effectiveness of the proposed method.

### Strengths
1. The topic of controllable human animation is valuable and the control signals without additional dense input is promising to improve the generalizability of generation model.

2. The authors have conducted extensive and thorough experiments of different baselines on several datasets to validate the effectiveness of the proposed method.

### Weaknesses
1.  The key idea of the paper is to disentangle motion field guidance and keypoint correspondence from pose control. However, the authors just combine motion field and keypoint extraction to empower the generation ability of the original animation diffusion model. The detailed disentanglement operation is missing.

2.  For the dense motion field of Section 4.1, the authors choose to sample the sparse optical flow Pd from the forward optical flow obtained from existing optical flow estimation models, and then predict the dense motion field using CMP. However, why not directly use the dense motion field obtained by existing methods? Please give a detailed explanation of the reasons for sampling before predicting and the benefits of this way. In addition, why do authors calculate Pd differently for training and inference?

3.  The point correspondence is extracted according to the keypoint coordinates of pose and how can this kind of correspondence be helpful to maintain a consistent appearance? The authors are suggested to provide more ablation study results and visual comparison results to validate the effectiveness of multi-scale point correspondence.

4.  For the part of Point Encoder of Section 4.2, the descriptions of the U-Net encoder and multi-scale intermediate features are confusing. The authors are suggested to emphasize that the intermediate feature is from hybrid ControlNet in this part.

5.  The reference image used of the paper is realistic, however, the provided demo video is a little cartoon-style and not realistic enough.

### Questions
Please refer to the questions and suggestions in the “Weaknesses” part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposed DisPose, a human pose retargeting framework with high-quality motion control. The core of the proposed method is to disentangle control guidance from skeleton poses and reference images.

### Strengths
The paper is well-written and easy to understand. The motivation for extracting sparse and dense motion fields makes much sense for this task and the DIFT feature provides content correspondence of key points as guidance. The plug-in module follows the ControlNet architecture and provides flexibility for using the pre-trained weight for other customized SD-UNet. I found Figure 7 extremely helpful for understanding the keypoint correspondences.

### Weaknesses
1. Is there any discussion or comparison of the efficiency, e.g., trainable parameters and inference time for a single batch?

2. Metric for video generation evaluation. I understand the authors follow previous works and adopt FVD as the video evaluation metric. However, this metric has recently been widely criticized by the community because of its inaccuracy in reflecting the overall quality. I wonder what the performance comparison would be if debiased FVD is used for evaluation. From [here](https://content-debiased-fvd.github.io/)

3. I appreciate the authors for providing video visualizations in the supp. Are there any side-by-side video comparisons between this work and recent baselines? It would be better to judge the temporal consistency of the video quality and the effectiveness of motion control.

4. How does the model generalize to out-of-domain real human identities? E.g. Old people?

5. (Minor) For the input of the reference image, did the authors utilize ReferenceNet for the SD-1.5-based model and the same setting of SVD for comparison to MimicMotion?

6. (Minor) L78 There's a mistake in the cited works with an additional reference network. DisCo didn't adopt this architecture but MagicPose and Champ did.

### Questions
Please see the weakness section.

### Soundness
3

### Presentation
3

### Contribution
3
