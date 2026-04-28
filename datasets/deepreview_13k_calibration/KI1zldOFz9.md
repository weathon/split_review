# Training-free Camera Control for Video Generation

- Decision: Accept
- Avg Score: 5.80
- Scores: 6, 6, 6, 6, 5

## Abstract
We propose a training-free and robust solution to offer camera movement control for off-the-shelf video diffusion models. Unlike previous work, our method does not require any supervised finetuning 
on camera-annotated datasets or self-supervised training via data augmentation. Instead, it can be plugged and played with most pretrained video diffusion models and generate camera controllable videos with a single image or text prompt as input. 
\tcg{The inspiration of our work comes from the layout prior that intermediate latents hold towards generated results, thus rearranging noisy pixels in them will make output content reallocated as well.} 
As camera move could also be seen as a kind of pixel rearrangement caused by perspective change, videos could be reorganized following specific camera motion if their noisy latents change accordingly. 
Established on this, 
we propose our method \textbf{CamTrol}, which enables robust camera control for video diffusion models. It is achieved by a two-stage process. First, we model image layout rearrangement 
\tcg{through explicit camera movement in 3D point cloud space. Second, we generate videos with camera motion using layout prior of noisy latents formed by a series of rearranged images.}
Extensive experiments have demonstrated the robustness our method holds in controlling camera motion of generated videos. 
Furthermore, we show that our method can produce impressive results in generating 3D rotation videos with dynamic content. 
Project page at \href{https://lifedecoder.io/CamTrol/}{https://lifedecoder.io/CamTrol/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces a method named CamTrol to enable controllable camera movements for video generation using off-the-shelf video diffusion models. The innovation lies in its training-free approach—no need for additional supervised or self-supervised training. The method employs a two-stage process:
1. 3D Camera Motion Modeling: It use a single view image as input to regressive a 3D point cloud, then gradually rendering, refining the 3D point cloud. The rendering process adopt the camera poses to simulate camera motion. The generated image sequence is later used to guide the perspective and layout in generated video sequences.
2. Noise Prior Guidance: It utilizes the “layout prior” of noisy latents, first adding noise of the image sequence, injecting the camera motion prior to the noisy latents. Then, providing the noisy latents into a pretrained video generation model to generation a reasonable and camera viewpoint alignment video.

### Strengths
1. CamTrol is a training-free solution, it does not need additional training, making it computationally efficient and easy to integrate with existing video diffusion models.
2. It investigate the feasibility to adopt the “noise prior of latent” technique to control the camera viewpoint without direct supervision.
3. CamTrol outperforms competing methods in both perceptual quality and motion alignment, particularly in complex camera movements, as demonstrated in both quantitative and qualitative experiments.

### Weaknesses
1. Since the whole pipeline is complex (depth estimation -> point cloud lifting -> rendering -> inpainting -> depth coefficient optimization), CamTrol’s quality is vulnerable. A problem at each of the current steps will have a bad effect on the next step. For example, if the depth estimation model cannot give the precise results, the structure of the entire scene may be strange when viewed from the different perspectives. If the inpainting model is not good enough, the generated videos may have much inconsistency. The reliance on a cascade of models, each with its own potential failure modes, introduces a significant fragility to the overall system. Small errors in depth estimation, for instance, can propagate through the pipeline, leading to substantial distortions in the final video. The lack of robustness in the face of imperfect intermediate results is a major concern.
2. For different videos (and different camera trajectories), the best timestep t_0 may be inconsistent. It is hard to design a rule to choose the best t_0. The selection of the optimal timestep t_0 appears to be highly dependent on the specific input video and desired camera trajectory. This lack of a systematic approach to determining t_0 introduces a significant hyperparameter tuning challenge, making the method less practical for general use. The absence of a clear heuristic or adaptive strategy for t_0 selection is a notable limitation.
3. The inpainting model is designed for single images, which may lead to inconsistent content and difficulty in generating reasonable new content. Additionally, the noisy latent not only provides layout priors but also carries some semantic information, which is unfavorable for the video generation model when creating new content. This makes CamTrol potentially unsuitable for generating long videos. The use of a single-image inpainting model for video generation raises concerns about temporal consistency. The model's inability to understand temporal relationships between frames can lead to flickering and other artifacts. Furthermore, the presence of semantic information in the noisy latents, while providing layout guidance, may also interfere with the video generation model's ability to create novel content, potentially limiting the method's applicability for long-form video generation.

### Questions
1. What is the evaluation dataset for the Table.1 ? If the references are come from the RealEstate10K dataset (Line 322), it is strange that the Video quality metrics of MotionCtrl and CameraCtrl are worse than the CamTrol, since both MotionCtrl and CameraCtrl are fine-tuned on the RealEstate10K dataset.
2. What is the base video generation models of MotionCtrl and CameraCtrl in Table.1 ? If the base video generators are not SVD, this comparison in Table.1 is unfair. Besides, can you provide the Video Quality of the vanilla SVD model for a reference?
3. Since the ParticleSFM may fail sometimes, a natural question is: how accurate is the camera computed ParticleSFM on the ground truth videos? It would be good to have some reference number on the ground truth dataset to show the lower bounds of Motion Accuracy metrics in Table.1 
4. In some cases of the provides webpage,  with the same camera trajectory (especially on complex trajectories), different videos do not have the same camera movement. For example, the complex trajectory II, the first video shows downward at the end of the video, the third video shows upward, the last video ignores the last camera movement. However, MotionCtrl and CameraCtrl do not have this kind of inconsistency. Can the author provide some quantitative results on complex camera trajectories?

### Soundness
2

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
This work proposes a training-free solution for camera control in video generation, requiring no supervised fine-tuning. A given image is first projected into 3D point cloud space and a sequence of views are then rendered given the camera trajectory. The latter serves as a structure condition for generation through inversion.

### Strengths
The writing is pretty clear, starting from the observation that camera movement could be regarded as one latent layout rearrangement. 
The two-stage framework is well-presented and easy to understand. 
The ablation study is comprehensive for multiple designs of proposed methods.

### Weaknesses
There are multiple major concerns:
- The novelty of this pipeline is limited which combines point cloud reconstruction and inversion. For example, Infinite Nature [a] also uses a RGBD image together with rendering to generate novel views and then refine. 
- The claim for training-free could be further clarified since depth coefficient optimization is also adopted (as mentioned at L190). Although the base model is not tuned, this optimization could be empirical and time-comsuming, preventing it from the practical applications. Specifically, the optimization process, while not directly training the base model, still requires iterative adjustments of depth parameters, which can be computationally expensive and may not generalize well across different scenes. The lack of a systematic approach to this optimization could lead to inconsistent performance and hinder real-world deployment.
- As stated at L210, video should be encouraged with more dynamics, which is quite important. Yet, we do not find any design/modification for this. The method seems to rely on the inherent dynamics of the base model, without explicitly encouraging motion or temporal coherence. This could result in videos that lack the desired level of dynamism and appear static or unnatural. The absence of a mechanism to control or enhance motion is a significant limitation.
- From one side, inversion provides the trade-off between fidelity and diversity (L261). From the other, it is challenging to choose which timestep should be used for the generation with given camera conditions. The selection of the timestep t_0 directly impacts the balance between fidelity to the input image and the diversity of the generated video, but the paper lacks a clear strategy for choosing this parameter. This makes the method difficult to use in practice, as users are left to experiment with different values without clear guidance.
- How the proposed method tackle text-to-video generation tasks? Fig.1 suggests that an input image is always given.

### Questions
Please check the weaknesses

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
This paper proposes a framework to control the camera viewpoints of the video generation process. This frame work is training free, utilizing some existing pre-trained models, like depth estimation model, and the depth coefficient optimization model. It can be used on many different base video generators. Given a real or T2I-generated images, this frame first generate a series of images according to the camera trajectories, with the point clouds as the middle 3d representation. Then, these images are noised to a certain degree. After that, these noised latents are denoised with the video generator, getting the videos with desired camera trajectory.

### Strengths
1. The framework is totally training free, combining some pre-trained models.
2. The written is easy to follow.
3. Visualization results demonstrate the effectiveness of each part in this pipeline.

### Weaknesses
1. In Table.1 , some quantitative comparison between the SVD and CamTrol+SVD is lacked, using the FVD, FID, IS, and CLIP-SIM, metrics. This comparison can reflect the impact of using proposed pipeline on the pretrained video generators.
2. In the demo video, there are some obvious consistency or unreasonable on objects in generated videos. One possible reason is the in painting model cannot handle some situation well, for example, when the camera motion is large, leading much holes in the images, the inpainting model cannot get enough context to generate reasonable contents for the holes.
3. Continue with the second point, this pipeline may have some difficulty in properly use the pre-trained video generator to generate consistent and reasonable videos.

### Questions
Besides the first point in the weakness, I have the following questions.
1. In Table 1, what are the base video generator for MotionCtrl and CameraCtrl? Can you use the same base video generator for Motion, CameraCtrl, and CamTrol, like SVD to quantitatively evaluate them?
2. In the camera motion modeling step, from the same first image, it seems that the CamTrol can generate different image sequences, according to the camera trajectories. If seeding these image sequence into the second step (layout prior of noise). Can we get some videos with similar appearance but different camera trajectories? Can you have some comparisons with the CVD (Collaborative Video Diffusion: Consistent Multi-video Generation with Camera Control) method?
3. How to find the best trade-off of t_0 for each videos?

### Soundness
4

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
This paper propose a training-free camera movement control for off-the-shelf video diffusion models. Firstly, the image is converted to 3D point cloud space using depth estimator, and the video frame is re-rendered using the camera motion trajectory. In this process, inpaint is used to repair the vacant part of the point cloud in the rendering result, and finally, generate videos using layout prior of noisy latents(inversion from the rendering result). The experiments and demo show good results.

### Strengths
The presentation of this paper is clear. The proposed method is reasonable, effectively generating videos with camera trajectories from a higher-dimensional space (3D point cloud). Notably, the proposed method is training-free, allowing for easy adaptation to new fundamental video generation models and related research.

### Weaknesses
1. While the overall pipeline is effective, it is relatively complex, including depth estimation, rerendering, 2D image inpainting, video fundamental model redrawing, and other processes. Additionally, the integration of these various components is not particularly seamless. This complexity can lead to reduced generation efficiency and may result in inconsistencies between the different stages, which could ultimately compromise the quality of the output. Specifically, the reliance on a depth estimator introduces potential inaccuracies, and the subsequent re-rendering process may amplify these errors. The inpainting step, while necessary, can also introduce artifacts, particularly when dealing with large occluded regions. The final video generation relies on the layout prior, which may not fully capture the nuances of the re-rendered frames, leading to temporal inconsistencies.
2. The presentation of the experimental part was poor, and the comparison with the relevant work and the combination with the latest video base model were not seen in the demo web page, although they mentioned it in the paper.

### Questions
1. In the quantitative evaluation, could you clarify the differences in the experimental settings for MotionCtrl, CameraCtrl, and other related papers? I noticed that there does not appear to be a uniform experimental setup in the field of camera control video generation.
2. The paper states that it compares CamTrol with state-of-the-art works, including AnimateDiff, MotionCtrl, and CameraCtrl. While it mentions that "AnimateDiff is excluded from quantitative analysis due to its incapacity to handle complicated trajectories," I still have not seen a qualitative comparison with AnimateDiff. Additionally, could you consider comparing your work with other relevant studies, such as CamCo[1] and Vd3d[2]?
3. The current results are excellent in terms of trajectory control, but they do not satisfy me in terms of video quality. Given the availability of a superior fundamental video model (with larger resolution and longer duration), and considering the combination with CogVideoX presented in this paper, I would appreciate it if you could provide some generated samples or comparisons for a more thorough evaluation. I will adjust the final score based on these results.

[1] Xu, Dejia, et al. "CamCo: Camera-Controllable 3D-Consistent Image-to-Video Generation." arXiv preprint arXiv:2406.02509 (2024).
[2] Bahmani, Sherwin, et al. "Vd3d: Taming large video diffusion transformers for 3d camera control." arXiv preprint arXiv:2407.12781 (2024).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes CamTrol, a training-free method for camera control in pre-trained video diffusion models. While previous works mainly train a camera control module using a fine-tuning dataset with camera annotations, this work does not require any external dataset to control the camera. The pipeline uses 3D point clouds and inversion to guide the generation process, enabling flexible camera control. CamTrol outperforms previous works which rely on external data, while enabling metric scale control based on the metric depth estimator.

### Strengths
- Control over motion strength: The method can synthesize videos with different camera motion strengths. Previous methods struggle due to having no knowledge of scale. Because the method uses a metric depth estimator, this problem should be fixed.

### Weaknesses
 - Scene inconsistency: The scene changes when the camera moves. When looking at the supplementary website, “Tilt Down” changes the top part of the scene or “Pedestal Down” changes the whole arrangement of the scene. But the point of camera control is that the scene remains intact, so in the best case the scene could be reconstructed from the video.
- Inaccurate camera: When looking at the supplementary website, the cameras are not that accurate. E.g., “Pan Left” also moves forward in the scene and doesn’t look like panning but rotating on the spot.
- Missing computational costs analysis: The approach seems very expensive. The authors motivate that previous works fine-tune some camera control modules on a camera annotated dataset which requires additional training. However, those approaches can do inference with basically zero computational overhead after training. This optimization-based approach requires computational overhead for each inference run and it is not clear how significant that is. E.g., if a user has to wait tens of minutes to hours to generate one result, there is a trade-off reached after a few prompts where it is more practical to train a camera control module once and then use it without overhead. It’s important to analyze both optimization time and memory usage.
- Missing quantitative ablations: The ablations mentioned in Sec. 4.3 are missing quantitative comparisons. The depth optimization seems to change nearly nothing in Tab. 2. When looking at relative differences between metrics, the metrics differences are basically 0.
- Writing quality: While the paper starts ok in terms of grammar, it gets worse throughout the paper and it makes the paper hard to read, especially the method section. I recommend putting the paper through some grammar correction tool.
- Unclear motivation of generalizability: The paper mentions in the introduction that methods fine-tuned on RealEstate10K suffer from generalizability issues. But there are no experiments or visuals which demonstrate this. Does the method really work better when cameras totally different from the training distribution are used?

### Questions
I currently rate this paper below the acceptance threshold. I have some concerns about the result quality and moreover it is not clear how large the computational overhead at inference time is compared to just having some simple embedding module as in MotionCtrl and CameraCtrl.
I would like authors to address following questions:
- Why does the scene often change with camera movement?
- Why is the camera often not that accurate even for simple movements?
- What is the computational overhead at inference time?

I am open to adjusting my rating based on the rebuttal.

### Soundness
3

### Presentation
2

### Contribution
2
