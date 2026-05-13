# 3DGS-Drag: Dragging Gaussians for Intuitive Point-Based 3D Editing

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
The transformative potential of 3D content creation has been progressively unlocked through advancements in generative models. Recently, intuitive drag editing with geometric changes has attracted significant attention in 2D editing yet remains challenging for 3D scenes. In this paper, we introduce 3DGS-Drag, a point-based 3D editing framework that provides efficient, intuitive drag manipulation of real 3D scenes. Our approach bridges the gap between deformation-based and 2D-editing-based 3D editing methods, addressing their limitations to geometry-related content editing. We leverage two key innovations: deformation guidance utilizing 3D Gaussian Splatting for consistent geometric modifications and diffusion guidance for content correction and visual quality enhancement. A progressive editing strategy further supports aggressive 3D drag edits. Our method enables a wide range of edits, including motion change, shape adjustment, inpainting, and content extension. Experimental results demonstrate the effectiveness of 3DGS-Drag in various scenes, achieving state-of-the-art performance in geometry-related 3D content editing. Notably, the editing is efficient, taking 10 to 20 minutes on a single RTX 4090 GPU.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a drag-based 3D Gaussian editing method. The pipeline is divided into two steps. It first binds 3D Gaussians to nearby handle points, and copy-and-paste the handle points to the target position. Secondly, it leverage a diffusion model to correct artifacts caused by Gaussian movements. Specifically, it converts the rendered image to sketch level to help the diffusion model understand the complete the deformed part. It also use Dreambooth and iterative dataset updating to better ensure 3D consistency. The paper also extends from one-step editing to multi-step editing, providing a stable and reliable 3D Gaussian editing method.

### Strengths
This paper proposes a drag-based 3D Gaussian editing method, while previous methods focus on text-guided editing. It uses a fine-tuned diffusion model to provide view-consistent correction to the edited scene and unsure rendering quality through iterative dataset updates. It also introduces multi-step drag editing to allow long-distance editing operations.

### Weaknesses
The examples shown in the paper have small movements. Will the method fail if we move a large object to a large range of movement? I suggest the author to provide some failure cases, which will better illustrate the upper bound of the method and make the work more solid.

### Questions
No.

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
3

### Summary
This paper introduces a drag-based 3D editing framework for 3D Gaussian representations. The approach employs deformation guidance to deform 3D Gaussians (3DGS) from a specified handle point to a target point, followed by diffusion guidance to enhance visual quality. Experimental results demonstrate that this method outperforms existing baselines.

### Strengths
1. The paper presents an innovative drag-based approach for editing 3DGS.

2. The experiments are thorough and provide convincing evidence of the method’s effectiveness.

3. The paper is well-structured.

### Weaknesses
1. In the case where the wall is widened (bottom right in Fig. 1), there is a noticeable color discrepancy between the original and the widened sections. Additionally, leaves near the edited boundary on the wall appear blurry.

2. In the baseline comparison, authors claim that "there’s no exact previous work on intuitive 3D drag operation". However, this is inaccurate.  ARSP [1] implements drag-based 3D editing using mesh-based deformation techniques. Interactive3D [2] offers a set of deformable 3D point operations on 3DGS and utilizes SDS to optimize the deformed 3DGS.

### Questions
1. Can this method reposition the entire flowerpot (as in Fig. 2) rather than only elongating it?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a method for editing gaussian-splatting 3D representation of scenes. The GS-represented 3D objects can be moved by geometrical 3D arrows designated in 3D scenes. To compensate for degradation of the rendering quality of the deformed objects, the method incorporates image correction technique based on diffusion model and  LoRA methods.

### Strengths
The method deals with editing of GS-represented scenes. From the demo examples, the results of the method seem reasonable. 

The combination of GS-editing and diffusion-based image correction may be a practical solution. 

The method seems to work better than Instruct-NeRF2NeRF.

### Weaknesses
Explanation of the diffusion guidance step in section 3.4 was not clear to me.  The difference from [Haque et al. 2023] is written as equation (5). Since all the information is in equation (5) and Figure 2, I'm not sure whether the proposed method is very similar to [Haque et al. 2023] or not (although there are of course differences between NeRF and GS).

I would like more detailed explanation for Annealed Dataset Editing, because it should be the center of the contribution. Specifically, please explain how the method differs from Instruct-NeRF2NeRF [Haque et al. 2023].

Small comments:

Line 197: $c \in R^d$:     What is $d$?

Lines 240-241: Here, $k$ is used for two different meanings. In "top-k (k=2)"    and  as a "temporal" index in $\{p_h^k| k \n N_h^i\}$. It is misleading.

Equations (1) and (2):  Minus ("-" ) symbols are used right after sigma symbols (summation). It seems odd. I think the minus symbols normally goes right before the sigma symbols. 

Figure 4: Maybe figure 4 is not referenced from the text.

### Questions
I would like more detailed explanation for Annealed Dataset Editing, because it should be the center of the contribution. Specifically, please explain how the method differs from Instruct-NeRF2NeRF [Haque et al. 2023].

Small comments:

Line 197: $c \in R^d$:     What is $d$?

Lines 240-241: Here, $k$ is used for two different meanings. In "top-k (k=2)"    and  as a "temporal" index in $\{p_h^k| k \n N_h^i\}$. It is misleading. 

Equations (1) and (2):  Minus ("-" ) symbols are used right after sigma symbols (summation). It seems odd. I think the minus symbols normally goes right before the sigma symbols. 

Figure 4: Maybe figure 4 is not referenced from the text.

### Soundness
3

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
This work introduces a novel framework for point-based 3D content editing, addressing the limitations of existing 2D editing tools when applied to 3D scenes. The method enables users to intuitively edit 3D scenes by specifying 3D handle and target points, with the system automatically adjusting the geometry while preserving visual details. The approach combines two key innovations: deformation guidance, using 3D Gaussian splatting for geometric changes, and diffusion guidance for correcting content and enhancing visual quality. A multi-step editing strategy further ensures smooth and consistent results. Experiments show that 3DGS-Drag outperforms existing methods in various tasks, including motion changes, shape adjustments, and inpainting, achieving state-of-the-art results with significant efficiency, requiring only 10-20 minutes per edit on an RTX 4090 GPU.

### Strengths
The paper is well-written and easy to follow.

* The proposed multi-step progressive editing strategy enables higher-quality edits while maintaining detail and multi-view consistency, addressing limitations found in previous 3D Gaussian Splatting (3DGS)-based editing methods like GaussianEditor and viCA-NeRF.

* The framework uniquely integrates 3D Gaussian Splatting for geometric deformation with diffusion models for content correction. This combination helps maintain visual consistency across views and supports versatile editing capabilities.

* Through qualitative and quantitative comparisons with baseline methods, the paper demonstrates that the proposed method achieves superior results in terms of editing quality, user preference, and performance across different scenarios.

### Weaknesses
1. The study introduces user preference and GPT evaluations for quantitative assessment. However, it does not clearly address potential biases in the user study, such as participant selection. Additionally, the sample size of 19 subjects may be insufficient to support the evaluation's conclusions. Recognizing that quantitative evaluation of diffusion-based methods can be challenging, as is the case with GPT evaluations, it is important to acknowledge these limitations.

2. The qualitative figures do not clearly demonstrate the effectiveness of local editing. The proposed method appears to perform relatively well when editing small objects or areas. It is recommended to highlight the specific changes in the figures to better illustrate the differences.

### Questions
The results presented in this work primarily demonstrate edits on small objects or minor scene adjustments. It would be beneficial to evaluate the method’s ability to handle larger object edits within the scene, such as moving a table or a truck.

### Soundness
3

### Presentation
2

### Contribution
2
