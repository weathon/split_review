# Diffusion Models for 4D Novel View Synthesis

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
We present 4DiM, a cascaded diffusion model for 4D novel view synthesis (NVS), supporting generation with arbitrary camera trajectories and timestamps, in natural scenes, conditioned on one or more images. With a novel architecture and sampling procedure, we enable training on a mixture of 3D (with camera pose), 4D (pose+time) and video (time but no pose) data, which greatly improves generalization to unseen images and camera pose trajectories over prior works which generally operate in limited domains (e.g., object centric).
4DiM is the first-ever NVS method with intuitive metric-scale camera pose control enabled by our novel calibration pipeline for structure-from-motion-posed data. Experiments demonstrate that 4DiM outperforms prior 3D NVS models both in terms of 
image fidelity and pose alignment, while also enabling the generation of scene dynamics. 4DiM provides a general framework for a variety of tasks including single-image-to-3D, two-image-to-video (interpolation and extrapolation), and pose-conditioned video-to-video translation, which we illustrate qualitatively on a variety of scenes.
See https://anonymous-4d-diffusion.github.io for video samples.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents "4DiM", a novel cascaded diffusion model aimed at 4D novel view synthesis (NVS) and able to generate scenes that can be viewed from arbitrary camera trajectories and timestamps. The model envolves several techniques to achieve this goal, including a super resolution model, Masked FiLM layers and different CFG params for conditioning variables. The model is trained on a combination of posed and 3D, 4D and video data, including RealEstate10K calibrated with a monocular depth estimation model. The design of training dataset improve the fidelity of generation and generalization ability to unseen images and camera pose trajectories. The proposed model is evaluated on in-distribution and out-of-distribution datasets with multiple metrics, some of which are proposed by the authors.

### Strengths
The task of unposed 4D novel view synthesis is a challenging one, and the paper presents a novel approach to tackle it. Compared to previous works, the proposed model has two strengths:
- The sampling method is well designed. The multi-guidance sampling enables controls on images; camera poses, and timestamps.
- The dataset combination enhances the generalization ability of the model. The authors also give experimental results to explain the effectiveness of the dataset.
- The authors propose novel metrics such as keypoint distance to measure temporal dynamics and improved TSED for 3D consistency, which are well-suited to evaluate the complex requirements of 4D NVS.
Moreover, the ablation study is well-designed, and the results are well-explained. The paper is well-written and easy to follow.

### Weaknesses
Although the paper has several strengths, there are some weaknesses that need to be addressed:
- The sampling resolution is not high enough. Compared with SOTA methods, ViewCrafter generates videos with higher resolution (576x1024), while the proposed method only generates 256x256 resolution videos even with a super resolution model. Is it possible to generate higher resolution videos with shorter sequence length or smaller training batch size?
- The discussion of 360-degree videos is not enough. The model is not evaluated on 360-degree datasets, MipNeRF360 for example, which is a common task in NVS.


### Questions
There are some questions that need to be clarified:
- The sampling efficiency and cost of the proposed model is not clear. How long does it take to generate a video compared to other methods? How much GPU memory is needed?
- In appendix F, the authors mention the gray padding for MotionCtrl LLFF samples in Figure 3. I don't understand the purpose of "in order to preserve the aspect ratio of LLFF" since the sampling resolution is 567\*1008. Why is it necessary to add gray padding as the sampling resolution is already higher than 256\*256? Does the gray padding affect the metrics of the model?
- gw, tgw and pgw in appendix Figure 7 are not explained in the main text.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes 4DiM, a cascaded diffusion model for 3D and 4D novel view synthesis. By a specially designed network architecture and sampling procedure, 4DiM enables joint training with posed and unposed video data, which results in better generalization and output fidelity. This also allows joint camera pose and time control in 4D novel view synthesis, making 4DiM a general model for various tasks like image-to-3D, two-image-to-video (interpolation and extrapolation), and pose-conditioned video-to-video translation. Qualitative and quantitative results show that the 4DiM performs favorably against priors art on static and dynamic scene generation.

### Strengths
S1: General model
4DiM enables joint training with posed and unposed video data, which not only improves the generalization and output fidelity, but also allows joint camera pose and time control in 4D novel view synthesis. It is shown to perform well on various tasks such as image-to-3D, two-image-to-video (interpolation and extrapolation), and pose-conditioned video-to-video translation.

S2: Better 3D consistency and pose alignment
Both qualitative and quantitative results show a consistent improvement over prior methods in terms of 3D consistency and camera pose alignment. Although it is a bit surprising that joint training with unposed video data leads to some worse metrics on in-domain data like cRE10k and ScanNet++ (Table 3).

S3: Good writing
The paper is well-written and easy to follow. The ablation studies also give good insights on where the performance gain comes from.

### Weaknesses
W1: Motion realism and temporal consistency
While the model shows great 3D consistency and pose alignment, the fidelity and temporal consistency of dynamic objects seems less impressive. In most dynamic scene results, the moving objects (cars, tires, animals, etc) either have unrealistic motion or temporal artifacts. Specifically, the motion often appears jerky or discontinuous, lacking the smooth transitions expected in real-world dynamic scenes. Furthermore, the temporal consistency is often broken, with objects flickering or changing shape abruptly between frames. This is particularly noticeable in longer sequences, where these artifacts accumulate and become more distracting. This can probably be improved by including dynamic object data like Objaverse for training. It would also be good to show more results on single-image-to-4D.

W2: Cartoonish texture
Some results (especially in single-image-to-4D and long trajectory generation) have quite cartoonish texture. The textures lack fine details and appear overly smooth, often resembling a painting rather than a photorealistic rendering. This is especially apparent when compared to the input images, where the textures are much sharper and more detailed. This issue is not only limited to single-image-to-4D scenarios but also appears in long trajectory generation, suggesting a limitation in the model's ability to maintain high-frequency texture details over extended sequences.

### Questions
Q1: I’m wondering if the authors have any explanation for why adding unposed video data lead to worse performance on certain metrics (see S3).

Q2: Following W2, do the authors have any ideas on how to improve the texture fidelity in these cases?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduce a new video generative model that has both camera and time control. This is achieved by carefully assembling static/dynamic training data and a model design that help leverage missing condition signals (e.g., camera poses / time variation). The qualitative results are promising, showing good disentanglement between camera and time. The quantitative result is better than existing methods on RE10k/LLFF on novel view synthesis and camera controllability.

### Strengths
- They introduce masked FiLM layers, which avoids misusing 0 conditions (1) during conditioning signal dropout and (2) due to missing data.
- They introduce cRealEstate10K dataset to unify the scale of camera extrinsics, which reduces ambiguities during training and leads to more reliable camera control.
- The qualitative results are promising, showing good disentanglement between camera and time. 
- The quantitative result is better than existing methods on RE10k/LLFF.

### Weaknesses
 - It's unclear whether the problem should be called 4D NVS. One common interpretation of 4D is 3D+time. Under this interpretation, I don't think the proposed model can do 4D. With camera control, it can do 3D. With time control, it can do 2D+time. However, combining both is not equivalent to 3D+time. 3D+time would require generating multiple videos that are synchronized in time, or multiple "frozen" time videos with different t.
- Data: The model is trained on mostly static data. The only source with non-static content is 1000 Google street views. How diverse is the data, and how much dynamic contents are there?  Does it include human motion and scene motion (e.g., tree, cars)?
- Result/eval: The reported metrics are mostly for 3D NVS. The only metric related to dynamics is keypoint distance, which however, only assess how large the motions are, but not how good the motions are. Additionally, the evaluation protocol is not clear enough -- is camera parameters the same for all the frameds when generating the videos? Otherwise, the camera motion would produce large keypoint distance.
- Disentanglement. The ability of disentangling camera motion and scene dynamics is not fully tested. It would help to report metrics that quantitatively measures the disentanglement. For example, whether fixing camera and changing t would introduce background motion; whether fixing t and changing camera will introduce object motion (e.g., through epipolar geometry).
- Some claims can be supported by experiments. 
  - The benefit of masked FiLM layers.
  - In the supplement, "Unlike Plucker coordinates, rays additionally preserve camera positions which is key to deal with occlusions in the underlying 3D scene."

### Questions
- The paper compared to MotionCtrl and found it has trouble following pose controls. Is there a hypothesis for this observation? Is it due to lack of metric scale training poses, or are there other underlying factors? What happens if MotionCtrl is trained on cRE10K that has metric scale poses?
- What is the difference between the proposed multi-guidance and InstructPix2Pix [B] Eq 3.
- Will the data/model be open-sourced?
- Related works. [A] can be discussed as the setup is close although they do not claim time control.

[A] VD3D: Taming Large Video Diffusion Transformers for 3D Camera Control
[B] InstructPix2Pix Learning to Follow Image Editing Instructions.

### Soundness
2

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
3

### Summary
The paper proposes a two-stage diffusion model that generates image sequences conditioned on camera pose and time. To address the lack of pose-aware image sequence datasets, the paper trains the model on a mixture of datasets (posed and unposed) with additional data preprocessing steps and a modified architecture. The qualitative results demonstrate that the model achieves better generalizability across both in-domain and out-of-domain scenes with better alignment with the input camera parameters.

### Strengths
1. The qualitative results look promising, showing generalizability to new scene types and arbitrary camera trajectories while outperforming the baselines.
2. The paper incorporates different sources of dataset to achieve generalizability of the model. 
3. The paper proposes a model architecture, Masked FiLM, to incorporate CFG training with incomplete conditional inputs.
4. The evaluation metrics comprehensively assess various aspects of a pose-aware generative model.

### Weaknesses
1. In Tab.1, 4DiM shows discrepancy in reconstruction-based metrics (LPIPS, PSNR, SSIM) between in-domain (RE10K) and out-of-domain (LLFF) samples. While the authors mention that the reconstruction metrics favor the blurry images generated by the baseline method, this implies that the proposed method cannot accurately reconstruct images at specific camera poses. This can be seen as contradicting the claims in the main text, such as "precise camera control" and "accurate control over camera pose." Similar trend is observed in Tab.2. The reasoning and explanations for the results on out-of-domain data could be presented in more detail.

2. Training on a mixed dataset is not a novel approach and has been proposed in previous works on different domains: MiDaS for depth estimation and dust3r in 3D reconstruction. Highlighting the key differences could help the readers to better understand the novel contributions.

3. Comparisons to previous works on multi-frame conditioning could be strengthened. When more than a single input image is given, one can consider generating sequence of images using frame-to-video generative models (e.g., FILM) or autoregressive models (e.g., Show-O). Similarly, comparisons to previous works in image-to-panorama generation (e.g., MVDiffusion, PanoDiff) are not presented. The effectiveness of the proposed method would be more convincing with the addition of relevant baselines for each application.

4. The ablation study in Table 3 shows that the effect of co-training with video is not significant, and qualitative comparisons between the two cases are not presented ("see Supplementary Material H for more samples"). The authors could provide the more explanations for interpreting the ablation study.

Some missing relevant works: Multi-Guidance (e.g., Instruct-Pix2Pix, StyleCrafter), Training on a Mixture of Datasets (eg., MiDaS, dust3r).

### Questions
1. It appears that 4DiM is trained from scratch rather than fine-tuned on a pre-trained diffusion model. Is there a particular reason for this choice?

### Soundness
2

### Presentation
2

### Contribution
3
