# Controllable Satellite-to-Street-View Synthesis with Precise Pose Alignment and Zero-Shot Environmental Control

- Decision: Accept
- Scores: 8, 6, 6, 5

## Abstract
Generating street-view images from satellite imagery is a challenging task, particularly in maintaining accurate pose alignment and incorporating diverse environmental conditions. While diffusion models have shown promise in generative tasks, their ability to maintain strict pose alignment throughout the diffusion process is limited. In this paper, we propose a novel Iterative Homography Adjustment (IHA) scheme applied during the denoising process, which effectively addresses pose misalignment and ensures spatial consistency in the generated street-view images. Additionally, currently, available datasets for satellite-to-street-view generation are limited in their diversity of illumination and weather conditions, thereby restricting the generalizability of the generated outputs. To mitigate this, we introduce a text-guided illumination and weather-controlled sampling strategy that enables fine-grained control over the environmental factors. Extensive quantitative and qualitative evaluations demonstrate that our approach significantly improves pose accuracy and enhances the diversity and realism of generated street-view images, setting a new benchmark for satellite-to-street-view generation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper focuses on generating street-view images from satellite imagery while preserving geometric consistency and capturing diverse environmental conditions.

To achieve precise geometric control, the authors propose a novel cross-view attention mechanism paired with an Iterative Homography Adjustment scheme. To address environmental variability, they introduce a Zero-Shot Environmental Control strategy.

Furthermore, the paper introduces new evaluation metrics to assess both semantic and geometric consistency between the generated images and corresponding ground truth images.

Extensive experiments validate the effectiveness of the proposed approach in producing diverse, realistic street-view images.

### Strengths
The paper clearly defines the problem by identifying two key challenges in Satellite-to-Street-View Synthesis: geometric consistency and environmental diversity. It effectively addresses these challenges by proposing corresponding solutions.

The innovative Iterative Homography Adjustment scheme stands out as a significant contribution. By iteratively refining the intermediate output based on relative pose differences, this approach corrects pose misalignments. I believe the "iterative adjustment" mechanism not only plays a crucial role in the Satellite-to-Street-View Synthesis task but also holds potential for broader applications in other controllable image synthesis tasks.

The introduction of the Zero-Shot Environmental Control (ZoEC) mechanism is another noteworthy highlight. Compared to existing methods like ControlNet, ZoEC demonstrates superior performance in synthesizing environmental variations through text-based control, enhancing the flexibility and realism of the generated outputs.

The paper is well-written and well-structured, making it easy to follow and understand. The clarity of presentation further strengthens the overall impact of the work.

### Weaknesses
Please provide an analysis of how the introduction of the Iterative Homography Adjustment (IHA) affects inference speed. Understanding the trade-off between accuracy and computational efficiency would enhance the practical value of the method.

The paper lacks an ablation study on the proposed Geometric Cross-Attention (GCA) mechanism. Including this analysis would help isolate and highlight the specific contribution of GCA to the overall performance.

While the rationale for introducing a new evaluation metric is understandable, for a fair comparison, it is important to also report results using the evaluation pipeline and metrics from previous works, such as RMSE, PSNR, and SD. This would provide a more comprehensive assessment of the method's performance relative to existing approaches.

The scholarship could be improved by referencing other relevant works in conditional street-view synthesis, such as SCP-Diff: Photo-Realistic Semantic Image Synthesis with Spatial-Categorical Joint Prior [ECCV 2024]. This would situate the proposed method more effectively within the broader research landscape.

### Questions
see weakness box.

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
This paper presents a new method for satellite-to-street view synthesis. This paper mainly achieves this goal by integrating Iterative Homography Adjustment to refine geometric alignment and Text-guided Zero-shot Environmental Control to provide flexible environmental control.

### Strengths
1. The proposed method is motivated and effective.

### Weaknesses
1. Many important works related to generation are missing in this paper, such as DreamFusion[1], Zero-1-to-3[2],  IM-3D[3] and CAT3D[4]. I strongly suggest that the author reorganize Related Works and make a detailed review and introduction to the development of the generation field.
2. The experimental results do not show notable advantages over previous baselines as reported in Table 1 and Table 2.

### Questions
1. Why choose the affine transformation to describe relative pose shift?
2. Is Clip Score enough it measure text-based generation ability?

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
This paper proposes an innovative approach for synthesizing street-view images from satellite imagery, addressing the challenges of geometric alignment and environmental diversity. The authors introduce a Geometric Cross-Attention mechanism (GCA) and Iterative Homography Adjustment (IHA) to ensure geometric consistency between the generated images and satellite views. Additionally, Zero-shot Environmental Control (ZoEC) is employed to flexibly adjust the environmental conditions of the generated images without the need for additional training data. Experimental results show that this method outperforms existing techniques in both geometric accuracy and environmental diversity, demonstrating potential for applications in urban modeling and virtual reality.

### Strengths
1. The Iterative Homography Adjustment mechanism iteratively adjusts the pose of the image during the generation process, significantly improving the geometric consistency between the generated image and the satellite image and ensuring the correct spatial alignment of objects in the scene.
2. The Zero-shot Environmental Control mechanism applies text prompts during inference to control environmental conditions without requiring additional training data. At the same time, ZoEC maintains the spatial structure of the image, ensuring that changes to environmental conditions do not affect the original geometric and semantic consistency of the generated image.
3. Extensive experiments have demonstrated the effectiveness of the proposed methods in the paper.

### Weaknesses
1. The English expression is inconsistent, and the organization of the paper needs improvement. Some academic terms are used inconsistently, such as "pose correction" and "pose alignment," which should be uniformly applied throughout the paper. The lack of consistent terminology makes it difficult to follow the technical details and understand the specific contributions of the proposed method. For example, the paper should clearly define whether the pose is being corrected or aligned, and use the chosen term consistently. Furthermore, the overall structure of the paper could be improved to enhance readability and logical flow.
2. There are some errors in the manuscript's presentation, for example: Figures 1–3 are not properly referenced or explained in the main text; Tables 9–10 lack corresponding table header explanations; and the parameter τ in Equation 9 is not adequately explained, making it difficult to read. The absence of clear references to figures and tables within the text makes it challenging to follow the experimental setup and results. The lack of explanation for the parameter τ in Equation 9 hinders the understanding of the underlying mathematical formulation and its impact on the model's behavior.
3. As far as I know, the CVUSA dataset contains numerous images taken in rural scenes, with many street-view images that include roads or buildings. The author’s displayed images seem to lack discussion on reconstruction results related to these elements. The paper focuses on general scene reconstruction but does not provide specific analysis of how the method performs on complex elements like roads and buildings, which are crucial for evaluating the practical applicability of the approach. The lack of specific examples and analysis for these elements is a significant omission.

### Questions
1. The authors should discuss how the Zero-shot Environmental Control (ZoEC) performs under different languages or diverse text descriptions. Can the model maintain environmental adjustment accuracy in multilingual scenarios?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Overall, this paper propose a method for satellite-to-street-view synthesis. The authors propose “CROSS-VIEW CONDITIONING MECHANISM” for better geometry consistency, and propose “ITERATIVE POSE ALIGNMENT DURING INFERENCE” at inference stage to further improve the results by utilizing the gradient values between the projected generated image and satellite image. Besides, “TEXT-GUIDED ZERO-SHOT ENVIRONMENTAL CONTROL” utilized the gradient values of CLIP alignment loss to enhance the text controlling.

### Strengths
This paper is well-organized and the proposed approach can improve the geometric consistency and textual controlling ability of generative method.

### Weaknesses
1. This article lacks a strong motivation and fails to clearly convey the significance of achieving geometric consistency and more accurate street views from satellite images. It doesn't specify under what circumstances a model with enhanced geometric consistency would be preferred. I believe this paper is quite similar to a series of works such as BEVGen[1] and BEVControl[2], which tell the story of geometric consistency with respect to the data augmentation. The author may benefit from expanding this point.
[1]. BEVGen: Street-View Image Generation from a Bird's-Eye View Layout
[2]. BEVControl: Accurately Controlling Street-view Elements with Multi-perspective Consistency via BEV Sketch Layout

2. Some typos: There is a blank line before almost every line of Equation. They should be deleted. In Line-459, it should be Table 1.

3. In Method, the proposed “CROSS-VIEW CONDITIONING MECHANISM” injects the controlling information into the diffusion model. Actually, it is like to introduce a query to extract the features from the satellite image. However, the authors’ statement makes me a little confused. Firstly, the authors state that \mathbf{A} represents the confidence. \delta{h} represents the height offset, but there is no evidence shown here. If they are indeed what the author says they are, at least some visualization should be displayed or some reasons should be explained. Besides, the detail of sampling operation should be given. Secondly, this module is named Geometric Cross-Attention (GCA), but there is no ‘attention’ mechanism here, equation (7) even does not contain a softmax symbol. Thirdly, what is the benefit of this mechanism brings as compared to the naive cross-attention?

4. In “ITERATIVE POSE ALIGNMENT DURING INFERENCE”, equation (8) and Line-277 also have the sampling operation defined in Line-251, please elaborate it. Why the symbol in equation (8) is different in Line-273? 

5. In “TEXT-GUIDED ZERO-SHOT ENVIRONMENTAL CONTROL”, why choosing “\epsilon” to controlling the generative precess with respect	to text prompt? It is weird for “potent satellite image prompts significantly undermine the influence of text prompts during training”. Have you applied the CFG scheme?

### Questions
1. In Equation (4) and (5), could you please provide a comprehensive derivative process? Due to space limitations, I suggest that the detailed process can be placed in the supplementary materials. Besides, it is recommended for the authors to provide more details for the meaning of the derived results. What benefits does this derivation bring to subsequent model design? How do model design and formula derivation relate to each other?

2. In Method, the proposed “CROSS-VIEW CONDITIONING MECHANISM” injects the controlling information into the diffusion model. Actually, it is like to introduce a query to extract the features from the satellite image. However, the authors’ statement makes me a little confused. Firstly, the authors state that \mathbf{A} represents the confidence. \delta{h} represents the height offset, but there is no evidence shown here. If they are indeed what the author says they are, at least some visualization should be displayed or some reasons should be explained. Besides, the detail of sampling operation should be given. Secondly, this module is named Geometric Cross-Attention (GCA), but there is no ‘attention’ mechanism here, equation (7) even does not contain a softmax symbol. Thirdly, what is the benefit of this mechanism brings as compared to the naive cross-attention? 

3. In “ITERATIVE POSE ALIGNMENT DURING INFERENCE”, equation (8) and Line-277 also have the sampling operation defined in Line-251, please elaborate it. Why the symbol in equation (8) is different in Line-273? 

4. In “TEXT-GUIDED ZERO-SHOT ENVIRONMENTAL CONTROL”, why choosing “\epsilon” to controlling the generative precess with respect	to text prompt? It is weird for “potent satellite image prompts significantly undermine the influence of text prompts during training”. Have you applied the CFG scheme?

### Soundness
2

### Presentation
1

### Contribution
2
