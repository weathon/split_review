# GS-VTON: Controllable 3D Virtual Try-on with Gaussian Splatting

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
\pl{
Diffusion-based 2D virtual try-on (VTON) techniques have recently demonstrated strong performance, while the development of 3D VTON has largely lagged behind.
Despite recent advances in text-guided 3D scene editing, integrating 2D VTON into these pipelines to achieve vivid 3D VTON remains challenging. 
The reasons are twofold.
First, text prompts cannot provide sufficient details in describing clothing.
Second, 2D VTON results generated from different viewpoints of the same 3D scene lack coherence and spatial relationships, hence frequently leading to appearance inconsistencies and geometric distortions.
To resolve these problems, we introduce an image-prompted 3D VTON method (dubbed \OM) which, by leveraging 3D Gaussian Splatting (3DGS) as the 3D representation, enables the transfer of pre-trained knowledge from 2D VTON models to 3D while improving cross-view consistency.
\textbf{(1)}~Specifically, we propose a personalized diffusion model that utilizes low-rank adaptation (LoRA) fine-tuning to incorporate personalized information into pre-trained 2D VTON models.
To achieve effective LoRA training, we introduce a reference-driven image editing approach that enables the simultaneous editing of multi-view images while ensuring consistency.
\textbf{(2)}~Furthermore, we propose a persona-aware 3DGS editing framework to facilitate effective editing while maintaining consistent cross-view appearance and high-quality 3D geometry.
\textbf{(3)}~Additionally, we have established a new 3D VTON benchmark, $\textit{3D-VTONBench}$, which facilitates comprehensive qualitative and quantitative 3D VTON evaluations.
Through extensive experiments and comparative analyses with existing methods, the proposed \OM has demonstrated superior fidelity and advanced editing capabilities, affirming its effectiveness for 3D VTON.
}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a novel approach for achieving 3D virtual try-on (VTON) that addresses current limitations in consistency and spatial relationships when extending 2D VTON methods to 3D. The method, GS-VTON, leverages 3D Gaussian Splatting (3DGS) as a 3D representation framework, combined with personalized diffusion model adaptation using LoRA (Low-Rank Adaptation) fine-tuning. This allows for multi-view image editing with consistency across different viewpoints and high-quality geometric and texture fidelity. Additionally, the paper introduces a benchmark, 3D-VTONBench, to support quantitative and qualitative evaluations for 3D VTON methods. The experiments show that GS-VTON outperforms state-of-the-art techniques, establishing a new benchmark for 3D VTON performance.

### Strengths
+ Effectively bridges the gap between 2D VTON and 3D applications by incorporating 3D Gaussian Splatting, which ensures consistency across multi-view images.
+ Uses a personalized diffusion model with LoRA fine-tuning, improving adaptability and customization for different subjects and garments.
+ Presents a new benchmark, 3D-VTONBench, which is an important addition for the comprehensive evaluation of 3D VTON performance.
They also demonstrates superior performance over existing methods, particularly in areas of realism, garment detail accuracy, and editing consistency.

### Weaknesses
 - The model is a very straightforward follow-up of 2D VTON models and inherits some biases from pre-trained 2D VTON models.

### Questions
From line 62-68, is the pink stuff on the rightmost edited images because of the artifacts of the proposed method? 

Personally, I think this paper is a good follow-up on 2D virtual try-on method and will be beneficial to this research area. Extensive experiments and comparisons with state-of-the-art techniques demonstrate the superiority of GS-VTON in terms of realism and multi-view consistency. This is validated not only through quantitative metrics but also through user studies. Therefore,  I don't have any major concerns.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This study proposes GS-VTON, a novel and potentially first-of-its-kind 3D virtual try-on method, based on a conditional diffusion model and 3D Gaussian Splatting. Unlike traditional 2D virtual try-on methods, GS-VTON enables users to visualize how clothing would appear on their bodies from different viewing angles, making it particularly promising for VR/AR applications. Moreover, the proposed reference-driven image editing and persona-aware 3D Gaussian Splatting techniques improves multi-view consistency in the virtual try-on experience in 3D.

### Strengths
1. GS-VTON is the first 3D virtual try-on method, showing more diverse real-world applications compared to 2D virtual try-on. It holds promising potential to transform online shopping and create positive social impact.
2. GS-VTON utilizes Reference-driven Image Editing and 3D Gaussian editing to ensure the try-on scene is consistent in both texture and geometry across multiple views. The design seems sound.

### Weaknesses
1) **Reference-driven Image Editing**: The authors propose this method to ensure texture consistency across multi-view images by integrating attention features from a reference image. However, if the reference image has incorrect textures, or contains artifacts such as blur or compression noise, it may negatively affect the consistency of subsequent images. The method lacks a mechanism to detect and correct such issues in the reference image, which could propagate errors throughout the try-on process.

2) **Questionable Experimental Setting**: 
   - All benchmark methods use text as input, while GS-VTON uses an image as a prompt. However, the user study criterion of clothing image similarity may not be ideal for comparing these approaches. The study should include a more direct comparison, such as evaluating the quality of the generated try-on images given the same target clothing, rather than relying solely on clothing image similarity.
   - Though the authors provide qualitative examples comparing GS-VTON with a baseline 2D VTON method, including this baseline in the user study for comprehensive quantitative analysis is essential. Most of the compared methods were not natively designed for virtual try-on applications, raising concerns about experimental fairness. The lack of a direct comparison with a state-of-the-art 2D VTON method in the user study limits the conclusions that can be drawn about the method's effectiveness.

3) **Limited View Coverage**: GS-VTON mainly shows the front of the clothing, without displaying how the back of the body would appear. This limits the practical application of the method, as users would typically want to see a full 360-degree view of the clothing on their body.

4) **Pipeline Presentation Issue**: Figure 2 shows Reference-driven Image Editing as the first step, followed by the Personalized Diffusion Model via LoRA Fine-tuning. However, the main text introduces these components in reverse order, which caused some confusion initially.

### Questions
1. Could the authors provide more details on how the $G_{src}$ point cloud was collected in Figure 2? Since RGB-D sensors or other 3D sensors are less accessible compared to standard cameras, this may limit the method's real-world applicability. A more practical scenario might involve capturing multi-view images with a camera, but in that case, the lack of camera pose information could limit the feasibility of training the 3D GS model.

2. Could the authors provide more information about the response processing in the user study? Was a crowdsourcing platform used for data collection?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces a novel image-prompted 3D virtual try-on method that leverages 3D Gaussian Splatting for fine-grained editing of human garments within a 3D scene. The authors propose a personalized diffusion model adapted via LoRA fine-tuning to incorporate personalized information into pre-trained 2D VTON models. They also introduce a persona-aware 3DGS editing framework to maintain consistent cross-view appearance and high-quality 3D geometry. The paper establishes a new benchmark, 3D-VTONBench, for comprehensive 3D VTON evaluations and demonstrates through extensive experiments that the proposed GS-VTON method outperforms existing techniques in terms of fidelity and editing capabilities.

### Strengths
* The paper presents a groundbreaking method for 3D virtual try-on by extending pre-trained 2D VTON models to 3D using 3DGS, addressing the challenge of cross-view consistency and spatial relationships in 3D scenes.
* The establishment of the 3D-VTONBench dataset is a valuable resource for the research community, facilitating more comprehensive evaluations and fostering further advancements in 3D VTON.
* The method demonstrates superior performance over existing techniques.

### Weaknesses
 * In some cases, such as the first row in Fig. 1, there are noticeable artifacts on the sleeves and edges of the garments.

* The statements about the effects of persona-aware 3DGS editing are inconsistent between the abstract and introduction. The abstract states "maintain consistent cross-view appearance," while the introduction says "enhancing multi-view consistency."
* What are the differences or advantages of your methods compared to RelFill in "Personalized Diffusion Model via LoRA fine-tuning"? Some experiments may be needed to demonstrate this.
* The hyperparameter in persona-aware 3DGS editing seems tricky.
* To demonstrate the ability to maintain 3D consistency, the following works should be discussed.

  * Geometry-Aware Score Distillation via 3D Consistent Noising and Gradient Consistency Modeling
  * MaTe3D: Mask-guided Text-based 3D-aware Portrait Editing
  * ConsistNet: Enforcing 3D Consistency for Multi-view Images Diffusion
* Need more detailed descriptions of the proposed benchmark.

* In line 110, the claim that LoRA "extend its learned distribution" requires further clarification and justification. The mechanism by which LoRA modifies the learned distribution should be explicitly stated, and supporting evidence or citations should be provided.
* I need more details about ControlNet. Is it from the original repository? Specifically, what version of ControlNet is used, and are there any modifications to the architecture or training procedure?

### Questions
* In line 110, does LoRA "extend its learned distribution"? Are there any citations?
* I need more details about ControlNet. Is it from the original repository?

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
4

### Summary
This paper introduces an image-prompted 3D VTON method (dubbed GS-VTON) which, by leveraging 3D Gaussian Splatting (3DGS) as the 3D representation, enables the transfer of pre-trained knowledge from 2D VTON models to 3D while improving cross-view consistency. Specifically, they propose a personalized diffusion model that utilizes low-rank adaptation (LoRA) fine-tuning to incorporate personalized information into pre-trained 2D VTON models. Moreover, they introduce a reference-driven image editing approach that enables the simultaneous editing of multi-view images while ensuring consistency. Furthermore, they propose a persona-aware 3DGS editing framework to facilitate effective editing while maintaining consistent cross-view appearance and high-quality 3D geometry. Additionally, they proposed a new 3D VTON benchmark, 3D-VTONBench, which facilitates comprehensive qualitative and quantitative 3D VTON evaluations. The experiments demonstrate the superior fidelity and advanced editing capabilities of GS-VTON.

### Strengths
1. The paper is well-written and easy to understand.
2. This paper introduces a new perspective on persona-aware editing which effectively improves the performance of the 3D VTON task.
3. The limitations of the proposed method are well-discussed.

### Weaknesses
1. There are concerns about the contribution of the proposed module, as it mainly adopts LoRA and a pre-trained diffusion model. For example, the X_train is not explained clearly in Line 339. Does it only refer to the results of the pre-trained IDM-VTON model? The use of LoRA for fine-tuning, while effective, might not represent a significant conceptual leap, and the paper should more clearly articulate the novel aspects of its application within this specific 3D VTON context. The explanation of how the pre-trained diffusion model is adapted for multi-view consistency is also not sufficiently detailed, making it difficult to assess the true innovation of the approach.
2. I noticed that the paper does not provide evaluation metrics (e.g., LPIPS, FID). Including these metrics would improve the evaluation of the GS-VTON method. The absence of standard metrics makes it challenging to compare the proposed method against existing techniques in a quantitative manner. While qualitative results are presented, the lack of numerical evaluation leaves a gap in the assessment of the method's performance, particularly regarding the fidelity of the generated 3D models and the quality of the texture transfer.
3. There are some writing errors: a) Line 31: "GS-VTONhas" is missing a space. b) Missing commas in Functions 7 and 10.

### Questions
1. It is better to discuss the reproducibility.

### Soundness
3

### Presentation
3

### Contribution
2
