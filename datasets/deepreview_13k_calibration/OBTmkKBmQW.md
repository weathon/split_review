# MOTIONFLOW:Learning Implicit Motion Flow for Complex Camera Trajectory Control in Video Generation

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5

## Abstract
Generating videos guided by camera trajectories poses significant challenges in achieving consistency and generalizability, particularly when both camera and object motions are present. Existing approaches often attempt to learn these motions separately, which may lead to confusion regarding the relative motion between the camera and the objects. To address this challenge, we propose a novel approach that integrates both camera and object motions by converting them into the motion of corresponding pixels. Utilizing a stable diffusion network, we effectively learn reference motion maps in relation to the specified camera trajectory. These maps, along with an extracted semantic object prior, are then fed into an image-to-video network to generate the desired video that can accurately follow the designated camera trajectory while maintaining consistent object motions. Extensive experiments verify that our model outperforms SOTA methods by a large margin.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents MotionFlow, a camera-controllable image-to-video (I2V) model.
Specifically, MotionFlow uses a reference motion network to process a reference image and camera trajectory, generating motion feature map. A semantic encoder extracts semantic features, which are combined with the motion features and fed into a video diffusion model to generate videos that follow the specified camera trajectory. Experiments on the RealEstate10K and DL3DV-10ks datasets show MotionFlow’s effectiveness in precise motion control.

### Strengths
S1: The paper introduces a framework that iteratively uses a Reference Motion Network to guide the Video Generation Network for accurate camera control.
S2: Experiments demonstrate the model's effectiveness.

### Weaknesses
W1: The expression in the paper does not appear sufficiently formal, as evidenced by the use of "Conference submissions" in the title and the missing references in line 135.

W2：Both MotionCtrl and CameraCtrl utilize SVD (which generally ensures strong frame consistency) as the foundational architecture for camera control in video generation. However, based on the experimental results in Figure 4, I observed notable distortion in MotionCtrl and temporal inconsistencies in CameraCtrl, which diverge from my expectations. Could the authors please clarify these discrepancies?

W3: In Figures 1 and 3, it appears that most cases illustrate camera movement around static objects rather than emphasizing object motion, as stated in the abstract.

### Questions
Q1: This paper uses AnimateDiff as the foundational architecture. I’m curious why the authors chose not to directly use an existing I2V model, such as SVD, for this task. Additionally, when incorporating the reference image as a condition for AnimateDiff, I would like to know why the semantic features are added to the input noise. What is the motivation behind this design choice? Typically, in models like SVD, the reference image latent code is concatenated with the noise latent.
Q2: I hope the authors can address the concerns raised in the "Weaknesses" section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a framework for generating videos guided by camera trajectories, addressing the significant challenges of achieving consistency and generalizability, especially when both camera and object motions are involved. To tackle this, they propose an integrated approach that combines camera and object motions by translating them into corresponding pixel movements. Key techniques include a reference motion network that learns the reference motion map aligned with specified camera trajectories, and an object motion prior that aids in maintaining consistent object motions. This information is then utilized by the video generation network to produce videos that accurately follow designated camera trajectories.

### Strengths
1.	To introduce camera trajectory control information while avoiding the confusion between camera motion and object motion, this paper proposes a method that adopts a Reference Motion Network that progressively and synchronously interacts with both camera motions and image semantic features. These interactions are then injected into the main denoising network. In contrast to other methods that simply fuse camera trajectory features with the latent space of the denoising network, this approach achieves more effective camera control.

2.	The experimental results demonstrate that this method significantly improves camera trajectory control capabilities compared to other methods.

### Weaknesses
1.	Since it is mentioned in line 73 of the introduction that MotionCtrl has a problem: “Training the two types of motion separately while ignoring their relationship may lead to confusion regarding the relative positions of objects and the scene,” and in line 78, it is stated that CameraCtrl's “generalizability is still limited, as it struggles to generate videos that differ substantially from the training data,” visualizing these issues would enhance the persuasiveness of the argument. Specifically, the paper should show examples where MotionCtrl fails to maintain consistent object-scene relationships, leading to artifacts like objects detaching from the background or exhibiting unnatural relative movements. Similarly, for CameraCtrl, examples should demonstrate the limitations in generating novel scenes or object configurations, such as a change in object appearance or scene structure when the camera trajectory deviates from the training data. These visualizations would provide concrete evidence of the stated limitations.

2.	For the TRAJECTORY ENCODER in the proposed method, it would be beneficial to explicitly state that the same camera trajectory representation approach as CameraCtrl is used, rather than simply mentioning, "In order to better describe camera pose, we use xxx." Similarly, for the REFERENCE MOTION NETWORK, it should be clearly indicated that a UNet is employed as the reference model, as in ReferenceNet in AnimateAnyone, even though the trajectory encoder has also been integrated. The paper should specify the exact architecture of the trajectory encoder, including the number of layers, types of layers (e.g., convolutional, recurrent), and activation functions. For the Reference Motion Network, the specific UNet architecture should be detailed, such as the number of downsampling and upsampling blocks, the channel dimensions at each level, and the type of skip connections used. This level of detail is crucial for reproducibility and understanding the method's implementation.

3.	How the reference network is implemented during the T-step denoising process is not clearly explained. Is the reference image added noise at each time step t and then denoised? This part seems to be unclear in the paper, and it would be best to include some formulas for better description, as well as for the Object Attention section. The paper should clarify whether the reference motion map is computed once at the beginning of the denoising process or if it is recomputed at each time step. If it's computed once, the paper should explain how the network handles the changing noise levels during the denoising process. If it's recomputed, the paper should specify the exact process and the input at each step. For the Object Attention section, the paper should provide a mathematical formulation of how the attention map is calculated and applied, including the specific operations used to combine semantic information and the output of the reference attention.

### Questions
None

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces MotionFlow, a camera-controllable image-to-video (I2V) model. Technically, MotionFlow first utilizes a reference motion network, which takes a reference image and camera trajectory as input to obtain a feature map of the video motion. Next, to incorporate the image condition into the T2V model, the authors employ a semantic encoder to extract semantic features. These semantic features, along with the motion feature map, are injected into a video diffusion model to generate the desired video that accurately follows the designated camera trajectory. Extensive experiments conducted on the RealEstate10K and DL3DV-10ks datasets demonstrate the effectiveness of MotionFlow for precise camera control.

### Strengths
S1: The paper proposes a novel feature extraction and injection method for video generation models to enable precise control of camera trajectories (e.g., using a reference motion network to extract motion maps). 

S2: The paper presents good qualitative and quantitative results.

### Weaknesses
W1: The expression in this paper appears somewhat informal, which may lead to inconvenience and confusion for readers. Here are a few examples, though not exhaustive: for instance, the phrase "Conference submissions" is inadvertently included in the fifth line of the title; there are missing references in lines 135 and 315; a new term, "motion extractor," is introduced in line 316, yet this module is not discussed elsewhere in the paper. Furthermore, the experimental settings are explained in both Section 3.6 and Section 4, which may seem somewhat redundant. 

W2：Based on the abstract (lines 47-51), my initial understanding was that the extracted object motion from existing videos would be used, and the generated video would "follow the designated camera trajectory while maintaining consistent object motions." However, upon reviewing the technical details, it seems that the approach essentially uses a reference image as a condition, effectively turning the T2V model into an I2V model. There is no actual extraction of motion priors as implied, which makes this claim somewhat overstated and potentially confusing for readers. Similar statements appear in line 80 ("with the reference image to get the reference motion priors") and line 243 ("The goal is to generate the scene according to the specified camera trajectory while preserving the original motion trajectories of the moving objects"). 

W3: In line 300, it is mentioned that the semantic information obtained from the semantic encoder can address potential moving foreground objects and stationary backgrounds. I do not fully understand how this works and would appreciate a more detailed and clearer explanation from the authors.

W4: The experimental details in Tables 1, 2, and 3 should be more comprehensive. For example, it would be helpful to specify the number of videos used for evaluation and the principles applied to classify trajectories as basic or difficult.

W5: Based on the results in Table 1, the reported values seem to differ from those in the original CameraCtrl paper. While this paper evaluates basic and difficult trajectories separately, it might be useful to provide results that align more closely with CameraCtrl for a clearer comparison.

### Questions
Q1: I hope the authors can address the concerns raised in the "Weaknesses" section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces MotionFlow, a video generation model designed for multi-view video synthesis with control over camera trajectories and object motion. Unlike prior approaches that treat camera and object motions separately, MotionFlow integrates them by converting both into pixel motion. Key components of the model include the Reference Motion Network, which guides the video generation process by aligning camera trajectory with pixel movements, and the Semantic Encoder, which ensures moving objects maintain coherence across frames. Controlled video generation could be useful for applications in 3D reconstruction, film production, VR, and AR.

### Strengths
The paper addresses a gap in video generation by focusing on complex camera trajectory control alongside object motion, which is a requirement for applications in film production, VR, and AR. The approach of combining camera and object motion into pixel motion is more useful than previous separate-learning approaches.

The description of the proposed MotionFlow model, its Reference Motion Network, and Trajectory and Semantic Encoder components is clear. The paper explains the modifications over existing frameworks- AnimateDiff and Stable Diffusion.

The experiments section is good, with a comparison against state-of-the-art methods (CameraCtrl, MotionCtrl).

### Weaknesses
It seems that the main novelty of the paper is in the reference motion network , but it is not clear whether this has been completely proposed from the authors or are their other papers that have been used as a baseline.

Although well-explained, the Trajectory Encoder and Semantic Encoder sections could use an expanded diagram of these components in Figure 2, or even a separate figure, for clarity of how these integarte and contribute to the overall network.

The introduction could frame the significance of the problem more compellingly, particularly for applications where camera control is crucial, such as interactive media and virtual environments. This might better capture the impact of the contribution.

The metrics are comprehensive, but adding a brief explanation of why each metric is important to the discussion could improve clarity. For instance, briefly discussing how Rotation Error and Translation Error relate to real-world camera control applications would make the results more meaningful.

Additional qualitative comparisons with other methods would be beneficial, particularly if the authors could include more challenging scenarios, such as multiple moving objects or varying light conditions. Highlighting specific failure cases or limitations of the model, perhaps as a "Limitations" subsection, would enhance transparency.

### Questions
Please see above.

### Soundness
2

### Presentation
3

### Contribution
2
