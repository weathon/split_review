# LatentWarp: Consistent Diffusion Latents for Zero-Shot Video-to-Video Translation

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
Leveraging the generative ability of image diffusion models offers great potential for zero-shot video-to-video translation.
The key lies in how to maintain temporal consistency across generated video frames by image diffusion models. 
Previous methods typically adopt cross-frame attention, \emph{i.e.,} sharing the \textit{key} and \textit{value} tokens across attentions of different frames, to encourage the temporal consistency. 
However, in those works, temporal inconsistency issue may not be thoroughly solved, rendering the fidelity of generated videos limited.
In this paper, we find the bottleneck lies in the unconstrained query tokens and propose a new zero-shot video-to-video translation framework, named \textit{LatentWarp}. 
Our approach is simple: to constrain the query tokens to be temporally consistent, 
we further incorporate a warping operation in the latent space to constrain the query tokens. 
Specifically, based on the optical flow obtained from the original video, we warp the generated latent features of last frame to align with the current frame during the denoising process. As a result, the corresponding regions across the adjacent frames can share closely-related query tokens and attention outputs, which can further improve latent-level consistency to enhance visual temporal coherence of generated videos. Extensive experiment results demonstrate the superiority of \textit{LatentWarp} in achieving video-to-video translation with temporal coherence.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper employs a straightforward strategy to maintain temporal consistency in query tokens by introducing a warping operation in the latent space. This operation aligns the generated latent features of the previous frame with the current one during the denoising process, utilizing optical flow from the original video. As a consequence, adjacent frames share closely-related query tokens and attention outputs, fostering latent-level consistency and thereby enhancing the visual temporal coherence of the generated videos. Extensive experimental results underscore the effectiveness of LatentWarp in accomplishing video-to-video translation while preserving temporal coherence.

### Strengths
1. The propose method is well-motivated.
2. The paper is well-structured, capable of clearly elucidating its core ideas.
3. The conducted experiments adequately showcase the efficacy of the method being proposed.

### Weaknesses
1. It is hard for me to see the improvement of temporal consistence from the images. Therefore, it is strongly advised to incorporate the video in the supplementary materials.

2. Section 4.2.  r^{i}|wrap(I^{i-1}, m^{i->i-1})-I^{i}| should be r^{i}|wrap(I^{i-1}, m^{i-1>i})-I^{i}| ?

3. I understand  that warped query can enhance the temporal consistence but why does it improve visual details(Figure 5) as well?

4. Since there are lots of open-sourced video diffusion models, which can naturally ensure the temporal consistence, what's the benefit of using Image diffusion model for video editing?   Longer video? 

5. For different video, the hyperparameters of Eq.(6) should be selected differently?

### Questions
Please see the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces optical flow for video-to-video translation by warping the latent codes in diffusion’s sampling process and achieves the SOTA performance on V2V.

### Strengths
1. The motivation is well presented,  the analysis of constrained query tokens would lead to consistent output, making the choice of warping the latent code convinced. 

2. The method is straightforward, and the results seem good.

### Weaknesses
1. Introducing the optical flow into diffusion-based video processing has been studied by Rerender-A-Video, though it is not applied to the latent. 
2. While this is video processing work, there are no video results, which makes it hard to distinguish the visual quality.
3. Authors introduce the occlusion mask for indicating the warped region and unwrapped region, but how to guarantee the consistency on the unwrapped region?
4. Some related works are not compared, such as Edit a Video, Rerender-A-Video, and etal.

### Questions
please present the video comparisons.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the author studies the task of zero-shot video editing and addresses the problem of temporal consistency for the edited videos. The author points out that existing methods only consider the K/V tokens in the cross-attention mechanism and ignore the Q token which plays a more important role in preserving temporal consistency. Specifically, the author proposes to adopt optical-flow to warp the latent feature from the previous frame. The overall idea is interesting and the experimental results look good.

### Strengths
1. The idea of considering the consistency of query tokens in cross-attention to generate consistent videos is interesting.
2. The writing is clear and easy to follow and the experimental results are promising.

### Weaknesses
 1. In section 5.1, the overall denoising step number is set to 20 and the proposed method is only applied to the first 16 steps. It would be good if there could be an ablation study about the two stages of the denoising steps. Specifically, it is unclear how the transition between the warped latent features and the unwarped features is handled. Does the model learn to ignore the warped features in the last 4 steps, or is there a blending mechanism? An ablation study should explore the impact of applying the warping to different numbers of initial steps, such as 8, 12, and 20. It would also be beneficial to investigate the effect of applying the warping in the last few steps instead of the initial ones. 
2. Is the proposed method sensitive to the hyper-parameters \alpha and threshold as well as the optical-flow methods? I would like to see some ablation studies on that. The paper should include a sensitivity analysis of the \alpha parameter, which controls the blending between the warped and unwarped features, and the threshold used to determine when to apply the warping. Furthermore, it is important to understand how the choice of optical flow algorithm affects the overall performance. The authors should compare the performance using different optical flow methods, especially with respect to the computational cost and accuracy.
3. Is it possible to edit/add some specific object to the video? Like adding a hat on a running dog? It seems most of the cases shown in the paper are about style changes. I would like to see some complex cases. The current method seems limited to style transfer, and it is unclear whether the method can handle structure deviations. For example, can the method handle adding a new object or changing the shape of an existing object? The paper lacks experiments that involve significant structural changes, and it would be beneficial to see how the proposed method would perform in such scenarios.

### Questions
Please refer to the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces LatentWarp, a framework for zero-shot video-to-video translation using image diffusion models. It addresses the challenge of maintaining temporal consistency in generated video frames. LatentWarp focuses on constraining query tokens for temporal consistency. It achieves this by warping the latent features from the previous frame to align with the current frame using optical flow information.  Extensive experiments confirm the superiority of LatentWarp in achieving high-quality video-to-video translation with temporal coherence.

### Strengths
The introduction of the LatentWarp framework offers a novel approach to zero-shot video-to-video translation. LatentWarp  emphasizes on preserving temporal consistency during video frame generation, achieved through optical flow and warping operations, significantly enhances temporal coherence,  which is a crucial aspect of video generation. The writing is good, and the structure of the paper is clear.

### Weaknesses
I find this method to be quite intuitive. My concerns mainly pertain to the experimental aspects:

1. Data-related issues: The authors do not compare their method to datasets used in their previous work like "tune-a-video." This omission may undermine the fairness of the experimental results.

2. Base model choice: The authors employ ControlNet as the base model instead of using LDM directly. ControlNet offers strong structural control, which might make the improvement from LatentWarp seem relatively small. It would be beneficial to provide experimental configurations with LatentWarp combined with LDM or Tune-a-Video to showcase this point.

3. Quantitative data details: The authors seem to have omitted reporting the sizes of the datasets used in their quantitative experiments.

4. Compared methods: It is advisable for the authors to compare their method with a broader range of existing approaches, such as Video-P2P and more recent methods.

5. Supplementary material: The authors have not provided corresponding video supplementary materials to visually assess temporal consistency.

6. User surveys: The authors did not provide user surveys as prior works have done. This is important to evaluate the visual effect.

7. Running costs: Editing time and GPU resource consumption, should be reported and compared to help readers understand the resource requirements and efficiency.

### Questions
See weaknesses. I will rejudge the rating according to the rebuttal.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
