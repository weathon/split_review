# PerLDiff: Controllable Street View Synthesis Using Perspective-Layout Diffusion Model

- Decision: Reject
- Scores: 6, 6, 3

## Abstract
Controllable generation is considered a potentially vital approach to address the challenge of annotating 3D data, and the precision of such controllable generation becomes particularly imperative in the context of data production for autonomous driving. Existing methods focus on the integration of diverse generative information into controlling inputs, utilizing frameworks such as GLIGEN or ControlNet, to produce commendable outcomes in controllable generation. 
However, such approaches intrinsically restrict generation performance to the learning capacities of predefined network architectures.  
In this paper, we explore the integration of controlling information and introduce PerLDiff (\textbf{Per}spective-\textbf{L}ayout \textbf{Diff}usion Models), a method for effective street view image generation that fully leverages perspective 3D geometric information.
Our PerLDiff employs 3D geometric priors to guide the generation of street view images with precise object-level control within the network learning process, resulting in a more robust and controllable output. 
Moreover, it demonstrates superior controllability compared to alternative layout control methods. Empirical results justify that our PerLDiff markedly enhances the precision of generation on the NuScenes and KITTI datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces PerLDiff, a method aimed at enhancing control in street view image generation, which is crucial for efficient data annotation in autonomous driving applications. PerLDiff incorporates layout-based masking maps as geometric priors and introduces a PerL-based Cross-Attention Mechanism within the Control Module (PerL-CM). This mechanism facilitates precise alignment of objects and scene details by integrating scene-wide and object-specific information derived from BEV annotations. Empirical evaluations on NuScenes and KITTI datasets suggest that PerLDiff achieves improved control and realism compared to baseline models such as BEVControl and MagicDrive.

### Strengths
* The overall paper writing is clear and is easy to follow.
* The introduced PerL-based Cross-attention sounds reasonable and performs well on some detailed experiments.
* PerLDiff demonstrates better object position controllability in scene generation compared to methods like BEVControl and MagicDrive.

### Weaknesses
* The authors use a mask-based representation in the PerL-based Cross-Attention mechanism. However, this type of representation lacks sufficient 3D priors, which may contribute to the orientation generation issues for vehicles mentioned in the limitations. Did the authors consider using the depth information of multiple vehicles with ControlNet to enhance object controllability? Specifically, it would be insightful to explore the benefits of Depth + ControlNet vs Mask + PerL-based Cross-Attention in improving object controllability.
* Has the PerL-based Cross-Attention been tested on other baselines beyond BEVControl to examine its potential improvements in controllability and perception tasks? For instance, would applying it to a baseline like MagicDrive yield similar gains?
* Is there any ablation study on the ConvNext for encoding the road map? How about other choices for the road map encoding? And why the ConvNext is frozen?

### Questions
* The term "train + Syn. val*" in Table 3 is not clearly defined.
* In Table 1, why the FID metric of PerLDiff is worse than the baseline BEVControl? Moreover, why the performance with BEVFormer is better than the one with multi-modal BEVFusion?
* In Table 2, why PerLDiff is significantly better than the BEVControl? I want to know the true reason behind the method perspective.

### Soundness
3

### Presentation
4

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
This paper presents a novel method for controllable street view generation utilizing a perspective layout diffusion model. The control factors are formulated as bounding boxes, lane structures, and scene descriptions. Subsequently, a cross-view framework, grounded in stable diffusion, is crafted to synthesize the desired multi-view images. Experimental results across various settings (i.e. generation quality, 3D object detection, and lane segmentation performance)—demonstrate the efficacy of the proposed approach.

### Strengths
+  solution for the data hungry autonomous driving. Meanwhile, the authors also conduct experiments to demonstrate the generated data can improve perception models' performance.

+ The writing is clear and the paper is easy to follow.

+ The authors conduct multiple experiments under different settings to demonstrate the proposed method can outperform the previous view synthesis methods.

### Weaknesses
+ The first question is whether the proposed method can ensure temporal consistency for the generated images. The paper doesn't discuss this problem and displays the image in different timestamps. However, the detection and segmentation models used, particularly StreamPETR, require temporal inputs. If the synthesized images do not achieve good temporal consistency, how can they improve the performance of temporal-based methods?


+ In Section 3, it appears that all input data comes from 2D space (with boxes and roadmaps projected onto images and a general scene description). Another question is whether the proposed method can effectively disentangle the camera's intrinsic and extrinsic parameters compared to BEVGen and BEVControl.


+ Cross-view attention: Could the authors explain the differences between view cross-attention and text cross-attention in PerlDiff compared to BEVControl and MagicDrive?


+ Object rotation controllability: Could the authors clarify how the proposed method achieves object rotation controllability? In Section 3, it seems that the box information is represented as eight corners in the image space, where the rotation information is not explicitly presented.

### Questions
+ Could the authors provide the details of the experimental setting on the nuScenes dataset? One point of confusion is that,  compared to the training set, the validation set is not very large. Why does adding it to the training data lead to such a significant improvement in model performance?

+ What is the meaning of * in Table 3?

### Soundness
3

### Presentation
3

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
This paper introduces a controllable image generation framework specifically tailored for autonomous driving applications. It employs a modified attention module that enhances instance controllability by incorporating an instance binary mask, thereby improving the precision of instance manipulation within the generated images.

### Strengths
1. PerLDiff improves upon the controllability of previous work, enabling more effective control over vehicle pose and map segments.
2. This study validates its framework across diverse datasets and settings, encompassing the NuScenes dataset, the KITTI dataset, as well as 3D detection and map segmentation tasks.

### Weaknesses
1. The reason for selecting ConvNext as the feature extraction network requires further exploration, particularly given the training objective of image classification on the ImageNet dataset. This raises questions about the appropriateness of utilizing ConvNext in this context. Additionally, it is essential to conduct an ablation study comparing ConvNext with other image backbone architectures, such as the CLIP image encoder, to provide a comprehensive understanding of their relative performance.
2. The formulation of this work is not novel to me; rather, it represents a combination of several existing methodologies. The framework closely resembles that of Panacea and MagicDrive, with the key modification being the introduction of an attention mask.
3. Lack of quantitative comparison with Panacea [a], which similarly uses the perspective layout.

[a] Panacea: Panoramic and Controllable Video Generation for Autonomous Driving

### Questions
1. I suggest not using the word BEV annotations. Both 3D box annotations and map annotations exist within 3D space rather than BEV space.
2. Section 3.2 is hard to read. I suggest to include a dedicated diagram to effectively illustrate the PerL-based cross-attention mechanism. The bottom of Figure 2 need to be refine.
3. Why is the attention mask not multiplied into A_s in Equation 5? Adding a binary mask into the feature seems unconventional.
4. Given that using perspective-Layout, why not use controlnet framework for more straightforward interaction?
5. Can this method be applied to occupancy control?

### Soundness
3

### Presentation
2

### Contribution
2
