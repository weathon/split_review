# NeRM: Learning Neural Representations for High-Framerate Human Motion Synthesis

- Decision: Accept
- Scores: 8, 8, 5, 8

## Abstract
Generating realistic human motions with high framerate is an underexplored task, due to the varied framerates of training data, huge memory burden brought by high framerates and slow sampling speed of generative models. Recent advances make a compromise for training by downsampling high-framerate details away and discarding low-framerate samples, which suffer from severe information loss and restricted-framerate generation. In this paper, we found that the recent emerging paradigm of Implicit Neural Representations (INRs) that encode a signal into a continuous function can effectively tackle this challenging problem. To this end, we introduce NeRM, a generative model capable of taking advantage of varied-size data and capturing variational distribution of motions for high-framerate motion synthesis. By optimizing latent representation and a auto-decoder conditioned on temporal coordinates, NeRM learns continuous motion fields of sampled motion clips that ingeniously avoid explicit modeling of raw varied-size motions. This expressive latent representation is then used to learn a diffusion model that enables both unconditional and conditional generation of human motions. We demonstrate that our approach achieves competitive results with state-of-the-art methods, and can generate arbitrary framerate motions. Additionally, we show that NeRM is not only memory-friendly, but also highly efficient even when generating high-framerate motions.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the challenge of generating realistic human motions at high framerates, a task made difficult by inconsistent training data framerates, memory constraints, and the slow performance of generative models. Current solutions downsample high-framerate details or discard low-framerate samples, leading to information loss. The authors propose NeRM, a generative model utilizing Implicit Neural Representations (INRs) to harness varied-size data for high-framerate motion synthesis without explicitly modeling raw motions. NeRM not only outperforms other methods but also efficiently produces motions at any desired framerate while remaining memory-efficient.

### Strengths
1. The paper proposes to use a novel variational INR to generate arbitrary framerate motion. The experimental results support this claim that NeRM outperforms other methods in different framerate generation. 

2. It enables to generalize INR to the new data without retraining by introducing the latent code to the INR input. 

3. The presentation is overall clear. The core idea as well as the technical details are well presented and easy to follow. 

4. The performance outperforms other baselines.

### Weaknesses
1.  As for the generation part, the part of the input for INR is z, it seems that the model heavily depends on the quality of the latent representation z. 

2. The idea of using time INR has been use in NeMF: Neural Motion Fields for Kinematic Animation, which may limit the novelty contribution of this paper.

### Questions
1. Two-stage training gives good performance. It would be good to give more details on training the auto-encoding of the latent code.

2. In order to avoid retraining of INR, some other methods choose to use latent code to modulate the weights of INR. Is there any insight for the choice in the paper? 

3. How do you determine the number of codes in the codebook?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a neural representation, i.e., NeRM, for representing continuous human motions. NeRM directly learns a continuous motion field over temporal coordinates without explicit modeling, making the training with varied-framerate motions and high-framerate motion generation possible. The authors leverage the proposed representation to (un-)conditional motion generation with diffusion models, showing the efficiency and effectiveness of high-quality motion generation.

### Strengths
The primary contribution of this work is the proposed neural continuous motion representation, NeRM, which I find both interesting and innovative. It effectively represents continuous motion sequences at any framerate level. This representation addresses limitations observed in previous works, such as MLD, which necessitates the input motion sequence to have the same framerate and fails to capture high-frequency details. The experiments conducted on various conditional and unconditional motion generation tasks are thorough and robust. The paper is well-organized and clearly presented.

### Weaknesses
My main concern revolves around the motivation of representing and directly generating high-framerate human motions. As discussed in the introduction, the authors present two key points: (1) high-framerate motion generation is inefficient, and (2) training with a fixed framerate cannot adequately utilize the dataset. However, I believe that training with fixed, low-framerate data might suffice to produce high-framerate results through interpolation. Hence, there might be no imperative need to use per-frame human poses during training.
The related discussion in the introduction appears to be not highly convincing. Specifically, the argument that fixed framerate training is limiting is not fully supported. While it is true that a fixed framerate might not capture all the nuances of motion, it is not clear that this limitation is significant enough to warrant the complexity of a continuous representation. The paper does not provide sufficient evidence to demonstrate that the performance gain from using a continuous representation is substantial enough to justify the added complexity, especially considering the potential for interpolation to achieve similar results.

### Questions
1. How can we determine if the feet sliding shown in Figure 4 is a result of training with a low framerate?

2. Does the use of variational INR, i.e., normalizing the latent code $\mathbf{z}_i$ to a normal distribution with KL loss, affect the preservation of high-framerate details? Such normalization typically leads to a smoother representation space?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the human motion synthesize for frame rate scenarios. It recognizes the limitations of previous efforts of generating high-frame-rate human motion sequences. The key idea is to fuse the data of different framerates into training by normalizing the time positions into relative and centerized time indices with a continuous mapping from time position to the pose configurations. A progressive training is leveraged to relieve the pressure of learning motion patterns under different frame rates by bootstrapping from the fixed frame rate. The generation of motion sequences is done by a conditional diffusion model where the latent code is the motion code from encoders and a codebook-based attention module.

### Strengths
- The proposed method can accept training data in arbitrary frame rate while supporting human motion generation in high frame rate.
- The proposed method is flexible to support human motion generation of different schemes, such as unconditional, or conditional to different constraints, such as action label or text descriptions.
- Leveraging the latent code for diffusion model and integrating the codebook-based attention module, the method is designed in a whole to support different modalities for conditions and good expressiveness.

### Weaknesses
- Question: Eq 2 is confusing to me. Normalizing the clip length from the standard seconds to the relative length has been commonly adopted. In Eq 2, given both the relative time position and the frame rate, the input information to the generation function f_\theta is exactly the same as what previous works input. Could the authors elaborate more about their differences here?
- Question: with different frame rates for the target motion sequence, is the number of time steps in diffusion, i.e. k in Eq 5, the same? I understand that they are two different “time steps” but I still would like to get a sense that whether the diffusion model is able to capture the motion of different frame rates or it is only to recover the pose in a single time step, static.
- In my understanding the claim that “NeRM can generate motions with arbitrary framerates s and durations l by setting appropriate temporal coordinates.” may be inaccurate. Technically, by the design of the method, the claim can be partially correct. But given the training data captured under certain frame rates, without considering the motion speed and sensitiveness of capture sensor etc, the model is unlikely to learn motion patterns in frame rates exceeding the highest frame rate contained in the training data.
- Question: is there any reason that a close baseline Nemf (He et al 2022) is not included in the benchmarking comparisons?
- The method is constructed with multiple components and requires settings of many introduced hyper-parameters, such as the normalizing of time positions, the codebook-coordinate attention and etc. The authors may need to provide corresponding ablation studies to support the effectiveness of these modules and the help readers understand the resources of performance gains more clearly.

### Questions
Please see my questions above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces NeRM, a generative model for high-framerate human motion synthesis using Implicit Neural Representations (INRs).
NeRM can handle varied-size data and capture the variational distribution of motions for high-framerate motion synthesis.

### Strengths
The paper provides a clear and concise description of the problem statement, methodology, and evaluation metrics. The paper addresses the underexplored task of generating realistic human motions with high framerates. By leveraging the advantages of INRs and diffusion models, NeRM offers a memory-friendly and efficient solution for high-framerate motion synthesis.

### Weaknesses
 * The paper could provide more detailed explanations and insights into the limitations and challenges of using Implicit Neural Representations (INRs) for high-framerate motion synthesis. This would help readers understand the potential trade-offs and constraints associated with the proposed approach.

* The paper could benefit from a more extensive discussion on the generalizability of NeRM to different datasets and motion types. It would be valuable to explore the performance of NeRM on diverse motion datasets and evaluate its ability to handle complex and varied motion patterns

* Some more motion synthesis literatures can be included in this paper, such as:
[a] A unified 3d human motion synthesis model via conditional variational auto-encoder
[b] Towards diverse and natural scene-aware 3d human motion synthesis.

### Questions
It would be beneficial to include more detailed explanations and insights into the proposed clip-FID metric for evaluating the quality of high-framerate generative details. How does clip-FID preserve target framerates without downsampling and how does it capture local details and artifacts such as foot sliding?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
