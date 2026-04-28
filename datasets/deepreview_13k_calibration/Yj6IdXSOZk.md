# CF-GISS: Collision-Free Generative 3D Indoor Scene Synthesis with Controllable Floor Plans and Optimized Layouts

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 8, 6, 3

## Abstract
We introduce CF-GISS, a novel framework for generative 3D indoor scene synthesis that ensures collision-free scene layouts by incorporating an image-based intermediate layout representation. In contrast to existing methods that directly construct the scene graph or object list, our approach facilitates substantially more effective prevention of collision artifacts as out-of-distribution (OOD) scenarios during generation. Furthermore, CF-GISS conditions layout generation on floor plans controllable via images or textual descriptions, enabling the production of coherent, house-wide layouts that are robust to variations in geometric and semantic structures. Our framework demonstrates state-of-the-art performance on the 3D-FRONT dataset, delivering high-quality, collision-free scene synthesis while offering flexibility in accommodating a range of floor plan structures. Additionally, we propose a novel dataset with significantly expanded coverage of household items and room configurations, as well as improved data quality.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a 3D indoor scene layout generation method based on 2D diffusion models. Instead of directly denoising parameterized objects and location features, this method uses 2D floor plan images as an intermediate representation to train a 2D diffusion model. Then, the authors use an object detection model to extract scene graphs from the generated layout image and reconstruct the 3D scene from it. The authors also constructed a new indoor scene dataset which is 1.4 times larger than 3D-FRONT dataset.

### Strengths
1. The authors constructed a new dataset which is 1.4 times larger than 3D-FRONT, with expanded household item categories with 26 super-categories and includes more scenarios like kitchen, bathrooms, and balconies. They also reduced several problems like empty scenes, object exceeding boundaries and overlapping compared to 3D-FRONT.

2. Incorporating the 2D layout image and 2D diffusion model during the generation enhances the model capacity of understanding the spacial relationships of each object and the floor plan.

### Weaknesses
1. The overall writing can be improved, some expressions are not clear enough.

2. I am quite confused that the authors append an extra object detector to detect objects from the generated layout images. Why not directly generate a segmentation map since they are basically trained from a segmentation map? Why not directly train on a quantized segmentation mask? What is the purpose of an additional object detector as it may introduce additional noise to the process? And it may further improve the ability to reduce collisions.

2. Is the scene graph extraction really necessary when you already have a 2D layout map? Scene graphs are necessary in those 1D diffusion-based works since there are no explicit representations of the spatial relationships, but what does scene graphs contributes when you already have an explicit 2D layout map?

3. The captions of Figure 3 are confusing. It seems that the authors were trying to explain the existing problems in the 3D-FRONT dataset, but the captions given are "Qualitative comparison of CF-dataset (ours) with 3D-FRONT." However, there is no comparison between the two datasets, just some demonstration of erroneous cases.

4. In table 2, the authors compared DiffuScene and InstructScene with the proposed method only on 3D-FRONT but not on the proposed CF-dataset, as I checked, both these method have released their codes, so why not compare the results on the proposed CF-dataset？

5. The authors proposed two conditions, image floor plan or text descriptions for the generation procedure as alternatives. However, these two conditions are not exclusive， it is more reasonable to use both the conditions together when you have a floor plan and use text prompts to describe the furnitures in the rooms.

5. No ablation studies are included in the experiments.

### Questions
1. Sometimes collision/occlusions in the vertical top views may not indicate wrong layouts, like part of the chairs can be put under the table, is it really necessary to exclude all the collision/occlusion during the generation?

### Soundness
2

### Presentation
2

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
This paper introduced a new framework, CF-GISS, for creating generative 3D indoor scenes that prevents collisions in scene layouts by using an image-based intermediate representation. This method mitigates collisions during generation, even in out-of-distribution scenarios. It allows for layout generation based on floor plans that can be controlled via images or text, and gives coherent layouts that adapt to different geometric and semantic structures.

The framework achieves state-of-the-art results on the 3D-FRONT dataset, and gives high-quality, collision-free scenes, accommodating various floor plan designs. Besides, it introduces a novel dataset with enhanced coverage of household items and room configurations, along with improved data quality.

The paper is well-written and easy to follow. I enjoy reading it.

### Strengths
I think the major contribution of this paper is the new framework that supports multimodal conditions - it synthesizes collision-free generative 3D indoor scenes with customizable floor plans based on images or text prompts, optimized room configurations, and photorealistic rendering.

To support training, they synthesized a new dataset with floor plans and scene layouts.

The performance on 3D-FRONT achieves the state-of-the-art.

### Weaknesses
The weakness of this paper is the relative long and non-differentiable pipeline. e.g., for the object retrieval module, it means the pipeline should come with a large object dataset to finish the whole process of scene synthesis. However, I know that most current scene synthesis works have an object retrieval phase.

Another suggestion is - Since existing scene datasets are much smaller than concurrent 3D object datasets for generative tasks, it is easy to overfit during synthesis. It would be more informative to compare the synthesized scenes with their nearest neighbours in the training set, to compare and evaluate if the methods overfit, and to evaluate if the scale of the datasets is enough.

### Questions
How efficient of this current model in inference? I noticed that there are many off-the-shelf modules, e.g., object detection, retrieval and rendering. It is quite a long pipeline.

### Soundness
3

### Presentation
3

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
CF-GISS present a novel scene synthesis idea: (1) generate the top-down view of the indoor scene where the objects are shaded in the color related to their semantic label, (2) retrieve specific model for each object and fill them into the place. To train the image generative model in (1), the author creates a nicer scene dataset with more scenes and better object layout. The scene synthesis method addresses the object intersecting problem, which is more visual in the scene’s top-down view comparing to the numerical recording of each bounding box.

### Strengths
The idea of solving “object intersection” through the top-down image is elegant and sound. As we have already trained diffusion models for understanding so much visual information, current techniques surely perform well in telling whether there are objects overlapping in the scene. Plenty of experiments also proves this. Furthermore, the method won’t be restricted with the “maximum object in the scene” and larger scenes (such as the entire house).can be generated for once. Providing a better scene dataset also brings more convenience to other researcher.

### Weaknesses
Let alone the accuracy of YOLO and the result of image generation training, I still have a trivial worry about whether addressing the generating issue with image may break the inner structure of object. Because when rendering the top-down view and generating these top-down views from the diffusion model, the objects are all presented in pixels. What would the pixels doesn’t form objects?
Furthermore, the valid intersections through the top-down view can never be presented with the method, e.g. the pendant lamp above other furniture, or a vase on a nightstand, or some chairs are put under the table. Would that strongly effect the synthetic results?

### Questions
No

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents CF-GISS, a novel framework for generative 3D indoor scene synthesis that guarantees collision-free scene layouts by leveraging an image-based intermediate layout representation. By treating collision artifacts as out-of-distribution (OOD) scenarios during generation, CF-GISS effectively prevents such artifacts. The framework takes floor plans or textual descriptions as input conditions to generate a coherent and realistic room layout. Moreover, this paper introduces a new indoor scene dataset that offers expanded coverage of household items and room configurations.

### Strengths
1. Novel approach. The use of an intermediate RGB image representation for scene layout is a clever way to leverage image processing tools for collision detection and avoidance.
2. Good performance. The paper claims and demonstrates significant improvements over existing methods on the 3D-Front dataset, particularly in the elimination of object collisions, which is a notable achievement.
3. Dataset Contribution. The introduction of a new, larger dataset with improved quality and expanded coverage is a substantial contribution to the field, providing a valuable resource for future research.
4. Clear presentation. The paper presents the methodology in a clear and coherent manner, consistently emphasizing the significant contribution of collision-free scene generation.

### Weaknesses
1. The proposed image-based intermediate layout representation lacks a theoretical guarantee of zero collision, as the authors fail to provide rigorous proof to support their claim. While the method leverages image processing for collision detection, the inherent limitations of pixel-based representations in capturing the full complexity of 3D object interactions are not addressed. Specifically, the transformation from a 2D image to a 3D scene introduces potential ambiguities and approximations, which could lead to undetected collisions or unrealistic object placements. The paper does not discuss the specific image resolution used and how it impacts the accuracy of collision detection, nor does it address the potential for aliasing or discretization errors that could arise from this representation.
2. Misaligned results. The renderings presented in Figure 2, depicting living rooms, bedrooms, and other scenes, exhibit significant misalignment with the corresponding floor plans above. Furthermore, the furniture within these renderings is also misaligned with the retrieved objects below. Similarly, the renderings in Figure 7 lack corresponding floor plans, which raises concerns about the authenticity of the results. The lack of clear correspondence between the 2D floor plans, the 3D renderings, and the object retrieval process makes it difficult to verify the accuracy and consistency of the generated scenes. The paper does not provide sufficient detail on how the 2D layout is translated into a 3D scene, which further exacerbates these concerns.
3. Incomplete comparison. Previous work PhyScene [1] also explored the collision problem while generating the indoor scenes.
4. Invalid room layout. The room layouts presented in Figure 8 contain enclosed areas, which raises questions about the feasibility of entering these rooms without doors. This indicates a failure in the scene generation process to adhere to basic architectural principles, which is a significant limitation. The paper does not discuss any mechanisms to enforce connectivity or accessibility within the generated layouts, which is critical for realistic scene generation.
5. Duplicate furniture. The authors claim that their new dataset, CF-dataset, comprises diverse furniture with improved quality. However, upon closer inspection, repetitive furniture (such as beds and coffee tables) is evident in Figures 2, 7, and 10, which contradicts their assertion. The lack of variation in furniture styles and models undermines the claim of improved diversity and raises questions about the dataset's overall contribution.
6. As described in Section 3.2, some object properties are obtained based on predefined standards, which may compromise the diversity of scene generation. The use of predefined standards for object properties limits the potential for generating novel and varied scenes. The paper does not discuss the impact of these predefined standards on the overall diversity of the generated scenes, nor does it explore alternative methods for object property assignment that could lead to more creative and varied results.

### Questions
In Line 244, the paper mentions that wall and floor materials are procedurally sampled. Could the authors provide a more detailed explanation of this process? How does this method ensure style and aesthetic coherence within the generated indoor scenes?

### Soundness
2

### Presentation
3

### Contribution
2
