# 3DIS: Depth-Driven Decoupled Instance Synthesis for Text-to-Image Generation

- Decision: Accept
- Scores: 8, 8, 6, 6, 8

## Abstract
The increasing demand for controllable outputs in text-to-image generation has spurred advancements in multi-instance generation (MIG), allowing users to define both instance layouts and attributes. However, unlike image-conditional generation methods such as ControlNet, MIG techniques have not been widely adopted in state-of-the-art models like SD2 and SDXL, primarily due to the challenge of building robust renderers that simultaneously handle instance positioning and attribute rendering. In this paper, we introduce \textbf{D}epth-\textbf{D}riven \textbf{D}ecoupled \textbf{I}nstance \textbf{S}ynthesis (3DIS), a novel framework that decouples the MIG process into two stages: (i) generating a coarse scene depth map for accurate instance positioning and scene composition, and (ii) rendering fine-grained attributes using pre-trained ControlNet on any foundational model, without additional training. Our 3DIS framework integrates a custom adapter into LDM3D for precise depth-based layouts and employs a finetuning-free method for enhanced instance-level attribute rendering. Extensive experiments on COCO-Position and COCO-MIG benchmarks demonstrate that 3DIS significantly outperforms existing methods in both layout precision and attribute rendering. Notably, 3DIS offers seamless compatibility with diverse foundational models, providing a robust, adaptable solution for advanced multi-instance generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work focuses on controllable image generation and points out the unified adapter challenge of multi-instance generation (MIG) methods: current MIG methods uses a single adapter to simultaneously handle instance positioning and attribute rendering. Such a unified structure complicates the development of detail renderers because it requires a large number of high-quality instance-level annotations. To this end, this work proposes a two-stage generation paradigm: (1) generating a coarse-grained depth map from layout; (2) rendering fine-grained instance details from depth map. This design enables the MIG adapter to be seamlessly integrated into various foundational models such as SD2 and SDXL without specific training. Extensive experiments demonstrate the effectiveness and flexibility of the proposed method.

### Strengths
1. This paper has a very clear motivation and solves the pointed problems very well. Although the idea of ​​using depth map as a coarse-grained scene guidance is simple, it effectively solves the limited adaptability challenge in existing MIG methods. Extensive qualitative and quantitative results (e.g., Table 2, Figure 3, and Figure 4) demonstrate that the proposed method has strong flexibility and can be applied to a variety of foundational models.
2. The presented results are promising, achieving state-of-the-art performance on instance attributes and locations. In particular, the proposed method can be further combined with other controllable image generation methods such as GLIGEN and MIGC to improve their performance for multi-instance generation..
3. The paper is well written and clearly structured.

### Weaknesses
1. The proposed framework depends on many existing models. For example, a) the text-to-depth model is obtained by fine-tuning LDM3D; b) a pretrained depth-conditioned ControlNet is required for depth layout injection; c) the detailed renderer relies on SAM to segment instances from depth. These dependencies weaken the originality of the paper and may compromise the robustness of the proposed framework.
2. The paper does not discuss depth ambiguity when multiple bounding boxes overlap. For example, given two partially overlapping instances, how can the model tell which is in front and which is behind?

### Questions
1. How does the layout adapter connect to the text-to-depth model? Does it work like ControlNet?
2. Now that depth information is introduced, can this method control the front-back relationship of overlapping instances?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Depth-Driven Decoupled Instance Synthesis (3DIS), a novel framework aimed at enhancing multi-instance generation (MIG) in text-to-image generation. 3DIS addresses the limitations of existing MIG methods by decoupling the generation process into two distinct stages: generating a coarse scene depth map for accurate instance positioning and rendering fine-grained attributes without additional training. This two-stage approach allows for greater control over both layout and attribute details, leading to improved scene composition and integration with various foundational models. The extensive experimental results demonstrate that 3DIS significantly outperforms existing techniques in layout accuracy and fine-grained attribute rendering across established benchmarks.

### Strengths
- **Innovative Framework:** The 3DIS framework effectively decouples the multi-instance generation process, allowing for improved accuracy in scene composition and instance positioning.

- **Training-Free Approach:** The ability to render fine-grained attributes without additional training is a significant advantage, making the model more accessible and easier to integrate with existing systems.

- **Robust Performance:** Extensive experiments on benchmarks such as COCO-Position and COCO-MIG show that 3DIS consistently outperforms state-of-the-art methods in both layout precision and attribute rendering, indicating its effectiveness in practical applications.

### Weaknesses
- **Limited Dataset Scope**: The experiments relied on the LAION-art dataset and COCO benchmarks, which may not fully represent the diversity of real-world images or scenarios. Expanding the evaluation to include a broader range of datasets could provide a more comprehensive assessment of the model's generalizability.

- **Evaluation Metrics Limitations**: The selected evaluation metrics, while informative, may not capture all aspects of image quality or user satisfaction. Additional metrics could enhance the evaluation of the generated images' visual appeal and usability.

### Questions
1. How does the proposed 3DIS framework handle the challenges of noisy annotations in the input data?

2. The training procedure relied on the LAION-art dataset, which may not fully represent the diversity of real-world images or scenarios.

3. What strategies could be employed further to improve the robustness of the generated depth maps? 

4. Given the dependence on pre-trained models for the training-free detail rendering process, how might variability in these models' performance impact the overall effectiveness of the 3DIS framework?

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
3

### Summary
The paper proposes a two-stage framework for multiple instance generation, which is 1)  generating a depth map conditioned on the layout map, 2) generating the image conditioned on the generated depth map with pretrained ControlNet.  Some techniques are also proposed to improve the results, such as using low-pass filter on the depthmap, using segment model for detail renderer.  The claimed improvements are on layout accuracy, instance accuracy and image quality.

### Strengths
1. The two stage framework for MIG seems to be novel, and the findings that depth map can be utilized as an intermediate product for  layout conditioned generation. 
2. Some practical techniques are proposed, which may be useful in practical  applications.

### Weaknesses
1. Compared to one-stage methods, the proposed one can be computionally inefficient, the extra computation cost should be clearly evaluated and presented. 
2. The paper heavily based on previous works, the novelty can be limited. 
3. It seems that the key contribution to the improvement of MIOU is the depth map, especially as shown in Fig.3 and Fig. 4, the depth map already demonstrats advantage compared to MIGC results. Further discussion on why the depth map can better align with the layout can be added.

### Questions
1. How does the occlusion of the layout impact the depth map generation? Since there is no clue of which one is nearer. It is better to evaluate the generation quality of the depth map, and how the depth map impact the final generation.
2. The parameters of the low pass filter, and how to choose it are missing.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces 3DIS for multiple instance generation(MIG) tasks in text-to-image generation. 3DIS decouples the image generation process into two stages. First, 3DIS generates a coarse scene depth map that accurately positions instances and aligns their coarse attributes. Second, it renders fine-grained instance attributes using pre-trained ControlNet on any foundation diffusion model without additional training. This approach enables seamless integration with diverse foundational models with a Depth-Controlled method, providing a robust and adaptable solution for advanced multi-instance generation.

### Strengths
1. Proposed a novel approach for MIG task with Depth control, the proposed method shows good generalizability and performance on different MIG benchmarks.

2. The proposed 3DIS can be seamlessly integrated into various pre-trained diffusion models, without requiring fine-tuning processes for each pretrained diffusion model.

3. The incorporation of 3D depth information can provide a better understanding of instances' attributes, thus benefiting the generation process of 2D images.

### Weaknesses
1. This pipeline is largely dependent on the fine-tuned Layout-to-Depth generation model, and the final output uses the foundation diffusion model to render instances in a strictly confined region(depth). There might be inconsistencies between the layout-to-depth generation model and the renderer model, thus hindering the final performance.

2. The slightest artifacts in the depth map might cause great changes in the final generation results, like unwanted additional objects or background depth.

### Questions
1. Can the layout-to-depth model generate diverse depth maps for the same layout? Like changing the pose, shape, and other attributes of instances?

2. It seems that sometimes the background scene can be blurry or unpleasant. Does that have something to do with the instance-wise rendering step?

3. Are there any failure cases that can make analyses on the Layout-to-depth model?

4. How long will it take to generate a single image?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors propose a novel multi-instance generation method, which uses a depth map as the intermediate generation step to decouple the whole process into two stages. Based on the depth map, the following rendering process only applies existing models, such as SAM, ControlNet, SD, and so on. Experiments show that the generated image is more in line with the given layout and description.

### Strengths
1. The proposed method is flexible and can combine many existing generation models.
2. The location improvement is pretty obvious compared to previous SoTA methods.

### Weaknesses
1. The locations of the cat and lamp are not correct in Figure 1.
2. The details of the comparison should be clarified. For example, it mentions that MIGC only supports SD1.5 in Figure 1, but the visual results of the proposed method in Figures 3 and 4 are based on SD2 and SDXL. In addition, it's unclear which version of SD is used in Table 1.
3. It's better to provide some inference efficiency analysis since the proposed method contains multiple steps.
4. The visual quality is not very satisfactory. It's better to apply user study to evaluate user preferences.
5. It's better to add the image quality metrics to the ablation study in Tables 3 and 4.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

### Contribution
3
