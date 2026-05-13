# CyberHost: A One-stage Diffusion Framework for Audio-driven Talking Body Generation

- Decision: Accept
- Scores: 8, 6, 6, 10, 8

## Abstract
Diffusion-based video generation technology has advanced significantly, catalyzing a proliferation of research in human animation. While breakthroughs have been made in driving human animation through various modalities for portraits, most of current solutions for human body animation still focus on video-driven methods, leaving audio-driven taking body generation relatively underexplored. In this paper, we introduce CyberHost, a one-stage audio-driven talking body generation framework that addresses common synthesis degradations in half-body animation, including hand integrity, identity consistency, and natural motion.
CyberHost's key designs are twofold. Firstly, the Region Attention Module (RAM) maintains a set of learnable, implicit, identity-agnostic latent features and combines them with identity-specific local visual features to enhance the synthesis of critical local regions. Secondly, the Human-Prior-Guided Conditions introduce more human structural priors into the model, reducing uncertainty in generated motion patterns and thereby improving the stability of the generated videos.
To our knowledge, CyberHost is the first one-stage audio-driven human diffusion model capable of zero-shot video generation for the human body. Extensive experiments demonstrate that CyberHost surpasses previous works in both quantitative and qualitative aspects. CyberHost can also be extended to video-driven and audio-video hybrid-driven scenarios, achieving similarly satisfactory results.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces CyberHost, an innovative one-stage audio-driven framework for generating talking body animations, addressing common issues such as hand integrity, identity consistency, and natural motion. Unlike multi-stage methods using intermediate representations like poses or meshes, CyberHost works end-to-end and supports zero-shot generation.

Key innovations like Region Attention Module and the usage of Human-Prior-Guided Conditions are proposed to improve the generation quality of local human regions and to address the motion uncertainty problem.

Experiments show CyberHost outperforms existing methods both qualitatively and quantitatively and works well in audio-driven, video-driven, and hybrid scenarios.

### Strengths
1. CyberHost introduces the first one-stage approach for audio-driven talking body generation, avoiding the complexity and inefficiencies of multi-stage systems that rely on intermediate representations.

2. The proposed Region Attention Module component effectively enhances critical areas such as hands and faces, improving the quality of local details and maintaining identity consistency.

3. By integrating motion constraints and structural priors via human-prior-guided conditions, the model mitigates the challenge of motion uncertainty, resulting in more stable and natural body animations.

4. The qualitative results in the supplementary materials are impressive. Also, compared to the previous state-of-the-art audio-driven half-body generation method, VLOGGER, CyberHost produces visibly superior results.

5. The paper is well-written and clearly presents its objectives, methodology, and findings.

### Weaknesses
1. Detailed Failure Analysis: The paper would benefit from a discussion of failure cases or limitations where CyberHost struggles, such as specific types of input audio or complex poses. This would provide a more balanced view of the model's capabilities. For instance, the paper could discuss how the model handles audio with significant background noise or singing, or how it performs with poses that involve extreme joint angles or occlusions. A more detailed analysis of these failure modes would be beneficial.

2. Scalability to Full-Body Generation: The paper focuses on half-body animation, but it does not discuss how well the architecture scales to full-body animation or if there are significant challenges in extending the framework. It is unclear if the current model architecture can effectively handle the increased complexity of full-body motion, including the coordination of legs and feet, or if the training data is sufficient to support full-body generation. The paper should address the potential limitations and challenges associated with this extension.

3. Lack of User Study for Subjective Evaluation: The paper does not include user studies or subjective evaluations to gather feedback on the perceived naturalness and quality of the generated videos. Such evaluations would provide valuable insights into how well the model meets human expectations for lifelike animation. The current quantitative metrics may not fully capture the perceptual quality of the generated animations, and a user study would be essential to validate the subjective quality of the results.

### Questions
1. Will the dataset used for training and evaluation be made publicly available? This would be valuable for reproducibility and further research by other researchers.

2. Failure Cases: What are the known limitations or specific scenarios where CyberHost struggles? Highlighting these would give a more complete picture of the model’s strengths and areas for improvement.

3. Full-Body Animation Scalability: Can the model be adapted for full-body animation, and if so, are there significant challenges or limitations to scaling up from half-body to full-body scenarios?

4. User Study Inclusion: Could authors conduct user studies for subjective evaluations to gather human feedback on the perceived quality of the generated videos?

5. DiffGesture Baseline: In the experiments section, the authors mentioned that they trained DiffGesture on the collected dataset, how did the authors get the SMPLX annotations for the collected dataset? It would also be good if the authors can quantitatively and qualitatively assess the generated SMPLX quality of the trained DiffGesture.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces an end-to-end audio-driven human animation framework, which is designed to generate realistic and natural upper body human videos from a single image and control signals such as audio, ensuring hand integrity, identity consistency, and natural motion.

### Strengths
1. Cyberhost can generate cospeech videos with very natural motions and clear hand/body structures.
2. It employs various control training methods, including codebook , hand clarity, pose-aligned reference, and also key point supervision. Experimental results indicate that these methods effectively enhance the clarity of hands and the correctness of body structures in the generated objects.

### Weaknesses
1. The generated videos exhibit insufficient facial clarity and detail, resulting in a noticeable discrepancy between the generated object and the characteristic features of the person in the reference image.
2. Unlike the codebook in VQ-VAE, which is specifically used for the reconstruction of designated features, the codebook in Cyberhost lacks supervisory signals during training, making it unable to ensure that the codebook effectively guides the model to generate correct hand shapes and facial features.
3. It would be good to visualize the ablation study for the two main contribution components: “Motion codebook” and "ID Descriptor".

### Questions
1. There are issues with the injection of the codebook during inference, and the paper does not clearly explain how to accurately detect the hand position from the noisy latent space when the timestep corresponds to a higher noise level.

### Soundness
3

### Presentation
2

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
This paper proposes a one-stage audio-driven talking body video generation framework, addressing issues in half-body video generation such as blurred hand details, inconsistent identity, and unnatural motion. Specifically, it introduces a Region Attention Module (RAM) to enhance the quality of local regions. Additionally, it proposes a human-prior-guided condition to improve motion stability in generated videos. A new dataset was collected for experimentation, with results verifying the effectiveness of the proposed method and the improvements contributed by each component.

### Strengths
1.	The proposed method demonstrates a certain degree of generalization, allowing it to adapt to multiple tasks, such as video-driven generation or multimodal-driven generation, while also enabling open-set generation.
2.	Based on the experimental results, the proposed method surpasses both the baseline and state-of-the-art methods across multiple metrics.

### Weaknesses
1.	Although the proposed method achieves promising results overall, it introduces many components. As shown in Table 1, there are nine components, but the experiments lack in-depth analysis of these. For example, the impact of the size of the latent bank in RAM. The results of using alternatives in the Region Attention Module (RAM), such as not using spatial latents, were not examined. Additionally, the effect of not decoupling the latent bank into spatial and temporal latents—instead using a single 3D latent bank—was not investigated. Furthermore, it remains unclear what specific aspects of video information are captured by the spatial and temporal latents, lacking justification and explanation.
3.	The use of the Laplacian operator to compute the hand clarity score requires justification, as the rationale behind this choice is not explicitly discussed. Additionally, the influence of the hand clarity score on the experimental results is not demonstrated in the experiments. It is essential to clarify whether this score is necessary and how it contributes to the overall performance of the proposed method.
4.	The method [1] is also a one-stage audio-driven half-body video generation model, but this paper does not discuss or compare it.

5.	The dataset used in [2] was not employed in experiments for comparison with previous methods. Additionally, the beat consistency metric [3] was not reported in the experiments.

6.	Some typos, such as in line 313 feference -> reference

### Questions
1.	When using full-body keypoints instead of the body movement map for video-driven generation, is it necessary to further fine-tune the entire model?
2.	How can hand pose templates be combined within the framework to achieve multimodal-driven generation? Does this process require fine-tuning the model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
This paper proposes a novel and elegant one-stage audio-driven human diffusion model. The authors primarily focus on the most challenging problems of existing body animation models, which are details underfitting and motion uncertainty. To address details underfitting, the authors introduce a region attention module, and to tackle motion uncertainty, they design a series of human-prior-guided conditions. The paper is well-written and enjoyable to read. The final video results demonstrate high-quality rendering and natural motion driving.

### Strengths
1. This paper addresses two important and challenging problems in the body animation field, and the proposed approaches are novel and effective.
2. The proposed method supports multi-modalities driving
3. The driving results show really good rendering quality and natural motion fidelity.
4. The paper is well-organized and well-written.

### Weaknesses
1. Some details are not provided:  
a) Which specific layers of Wav2Vec features were used? (line 191)  
b) How to constrain the basis vectors of the latents bank to be orthogonal? (line 242)  
c) There is a lack of loss description for regional mask predictor. (line 260)  
2. Authors claim that the hand clarity score can enhance the model's robustness to blurry hands during training and enable control over the clarity of hand images during inference. They conducted ablations on hand clarity, but they did not demonstrate to what extent this score can control hand clarity during inference. I would like to know this result.
3. The explanation of how the proposed 'Pose-aligned Reference Feature' works has not convinced me for two reasons:  
a) Although the ablation on pose-aligned ref shows a lower HKC score compared with Cyberhost, this method was proposed to solve the case of challenging initial poses, and the authors did not demonstrate its effectiveness in that scenario.  
b) The authors claimed that the skeleton map provides topological structure information, which improves the quality of hand generation. However, they did not explain how this structural information actually contributes to generating higher-quality hand images.  
4. Some spelling mistakes: 'feference' should be corrected to 'reference' in line 313.

### Questions
1. The authors claimed that the two-stage methods are mainly limited by the capability of the pose or mesh detectors, this limitation constrains the model's ability to capture subtle human nuances. I wonder if there exists, for example, a mesh detector that provides accurate and nuanced results. What are the advantages of a one-stage method compared to a two-stage method?
2. The authors presented various driving results, including video-driven body reenactment and multimodal-driven video generation. Was the model retrained when performing these two types of driving cases? If not, why can the body movement map be directly replaced by a skeleton or hand pose template?
3. Is the regional mask predictor embedded in all layers? Because different layers learn different kinds of features to serve different roles in the network. Therefore, I wonder about the effectiveness of predicting regional masks in all layers. Perhaps predicting the mask from the most effective layer could perform better.

Considering the good results and novelty, I would be very willing to raise my rating if my questions are answered.

New after rebuttal: The authors provide solid extended experiments, more implementation details, and reasonable explanations about the proposed questions. Taking the good results and novelty into consideration, I think this is really a good paper. Therefore, I decide to raise my rating to 10.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces CyberHost, audio-driven human animation framework based on diffusion models. It addresses the less explored area of full-body human animation driven by audio signals, focusing on enhancing the generation quality of critical regions like the hands and face. The authors propose a Region Codebook Attention mechanism, along with a suite of human-prior-guided training strategies. The paper aims to bridge the gap in audio-driven human animation by improving hand clarity and overall natural motion.

### Strengths
The authors aimed to tackle two significant challenges in audio-driven body generation and achieved progress in:
1. Improving the synthesis quality of critical regions (hands and face)
2. Reducing motion uncertainty caused by weak correlations.

Specifically, this paper successfully addresses the challenge of generating high-quality hand and facial features using proposed modules including RAM.

In addition, comprehensive experiments were conducted. Comparisons were made to evaluate not only audio-to-body generation methods but also video-to-video and audio-to-face methods, demonstrating its expandability.

### Weaknesses
While most parts are understandable, some details and explanations are missing. The questions regarding the missing information are listed under "Questions." Additionally, as the methods utilize many well-known architectures and frameworks while introducing several modules—including the Latent Bank, Pose Encoder, Heatmap Estimator, and Mask Predictor—some missing information limits the paper’s reproducibility and clarity of the paper. If the concerns or questions listed on "Questions" are addressed, this paper would be worthy of a higher rating.

### Questions
1. In Section 3.2, how was the hand heatmap estimator trained? Was it trained jointly with Equation 6 during stage 1, stage 2, or was it pretrained former to Equation 6? Also, when training the hand heatmap estimator, were all weights shared across timesteps?

2. Are the Pose Encoder in the Body Movement Map and the Pose-Aligned Reference Feature shared? If they are, why are the rectangular box and human pose encoded using a shared network? What are the advantages of using a shared network compared to using different networks that share the latent space? If they are not shared, they should not be described as using the same Pose Encoder or abbreviated as "P."

3. Were the diffusion models initialized with pretrained weights or trained from scratch? At first, it seemed they were being trained from scratch, but in Line 191, it states, "we extend the 2D version to 3D by integrating the pretrained temporal module from AnimateDiff." Could you clarify how all the components were initialized?


Simpler Questions

4. What are the dimensions of L_spa and L_temp in Latent bank?

5. Starting from Line 855, how will this review system be incorporated into practical applications and future research?

6. Is Laplacian standard variance sufficient for "Hand clarity score?"

### Soundness
3

### Presentation
3

### Contribution
3
