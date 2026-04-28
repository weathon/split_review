# Geometry Image Diffusion: Fast and Data-Efficient Text-to-3D with Image-Based Surface Representation

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Generating high-quality 3D objects from textual descriptions remains a challenging problem due to computational cost, the scarcity of 3D data, and complex 3D representations.
    We introduce \textbf{Geometry Image Diffusion} (GIMDiffusion), a novel Text-to-3D model that utilizes geometry images to efficiently represent 3D shapes using 2D images, thereby avoiding the need for complex 3D-aware architectures.
    By integrating a Collaborative Control mechanism, we exploit the rich 2D priors of existing Text-to-Image models such as Stable Diffusion.
    This enables strong generalization even with limited 3D training data (allowing us to use only high-quality training data) as well as retaining compatibility with guidance techniques such as IPAdapter.

    In short, GIMDiffusion enables the generation of 3D assets at speeds comparable to current Text-to-Image models.
    The generated objects consist of semantically meaningful, separate parts and include internal structures, enhancing both usability and versatility.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies how to generate high quality mesh of objects with GIM.

The 3D objects are parameterized into 2D chart geometry image. This representation is compact where the prior of 2D SD model can be exploited and maintains good geometry and semantic properties. The generation happens vis modifying standard SD with cross attention between different attributes of the chart.

### Strengths
- The reviewer loves the elegant idea very much. I personally believe this is the correct way in a long-term to generate usable (industry level) and high-quality assets for objects. Because most generative model for objects now depends on large synthetic dataset, with known geometry.
- The system is simple and effective.
- Also, the semantically meaningful parameterization has much more space in the future for editing and manipulation.

### Weaknesses
 - My main concern is maybe the diffusion overfit the proposed UV chart distribution. But we know that there is uncertainty of how an object can be parameterized into a chart. Is there any measurement of how good the chart is in the proposed preprocessing pipeline? e.g. it maintains the surface area or local differential properties? Can the proposed method generate different chart pattern for the exact same object? And how diverse is the chart?
- There are some small artifacts in the boundary of the mesh, which may due to the boundary of the chart. I believe this can be fixed in future works, but an analysis of this artifacts may provide more intuition of the future work.
- Maybe one or two applications like relighting .etc will future demonstrate the strength of generating object via GIM.

### Questions
Please see the first two questions in the weakness: the chart quality and diversity; and the artifacts on the boundary.

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
4

### Summary
The paper introduces Geometry Image Diffusion (GIMDiffusion), a novel Text-to-3D generation model that uses geometry images to represent 3D shapes in a 2D format. This approach leverages the priors of pre-trained image diffusion models, allowing efficient 3D object generation without complex 3D-aware architectures. By retaining pre-trained weights, GIMDiffusion is compatible with tools like IP-Adapter, enabling flexible style control and broad applicability. The use of multi-chart geometry images further enhances the model’s ability to represent complex shapes, offering a scalable and versatile solution for text-driven 3D generation.

### Strengths
1. Geometry images provide a low-complexity 3D representation, allowing GIMDiffusion to fully leverage pre-trained 2D diffusion models for 3D generation.
2. The model preserves the weights of the pre-trained image diffusion model, making it compatible with plugins like IP-Adapter for style transfer and customization.

### Weaknesses
1. My primary concern with multi-chart geometry images is the variable layout configurations that a single 3D shape can produce. That means a single 3D shape may correspond to many different geometry images, potentially complicating the training process and impacting consistency across different shapes. Is any technique used to standardize the conversion from mesh to geometry image. Specifically, the lack of a canonical mapping between a 3D surface and its 2D representation could lead to inconsistencies in the learned feature space, making it difficult for the model to generalize across different parameterizations of the same shape. This variability could manifest as artifacts or inconsistencies in the generated 3D models.
2. Generated results in the paper often show lower quality around shape edges, possibly due to the geometry image representation. This limitation affects the clarity and sharpness of complex geometries. The issue likely stems from the discrete nature of the geometry image representation, where the edges of the 3D model are mapped to the boundaries of the 2D charts. This discretization can lead to aliasing and other artifacts, particularly when the chart boundaries do not align well with the underlying 3D geometry. The paper should investigate the impact of different chart layouts on edge quality.
3. The model freezes the pre-trained Stable Diffusion (SD) model for generating albedo textures. However, SD has known limitations in UV space, and freezing this branch could compromise RGB quality. Providing experiments to validate this decision would help substantiate the model’s robustness. Specifically, the fixed SD model might not be able to adapt to the specific UV parameterizations used by the geometry image, potentially leading to texture distortions or inconsistencies. The authors should explore the impact of fine-tuning the SD model on the quality of generated textures, even if it requires a more complex training procedure.

### Questions
1. How does the variability in multi-chart geometry image layouts impact GIMDiffusion’s training stability and scalability?
2. The quality of shape edges appears to be suboptimal in the generated results. Is this a known limitation of the geometry image representation, and are there potential solutions to address this?
3. The authors freeze the albedo generation branch based on the pre-trained SD model, but SD’s performance in UV space is often limited. Could the authors provide experimental evidence to show that this decision does not compromise the quality of generated RGB textures?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
1. GIMDiffusion uses geometry images to represent the surface of 3D shapes in a 2D format. This method, unlike traditional 3D meshes, can utilize the extensive 2D image generation capabilities of diffusion models like Stable Diffusion. This approach results in faster generation times, lower data requirements, and the elimination of the need for complex 3D-specific model architectures, which are often cumbersome and data-hungry.

2. The model introduces a Collaborative Control mechanism to integrate 2D Text-to-Image models with geometry images. Through this mechanism, the geometry and texture generation processes are interconnected, allowing each to influence the other. This setup ensures that the textures generated align well with the 3D shape, facilitating realistic and coherent representations even when there is limited 3D data available.

3. Efficiency and Performance: GIMDiffusion achieves faster-than-average generation times, producing complex 3D assets in approximately 10 seconds. Moreover, the model avoids intermediate 3D processing stages like iso-surface extraction, further streamlining the pipeline.

### Strengths
1. Innovative 2D-Based Approach for 3D Generation: By using geometry images, GIMDiffusion avoids the need for specialized 3D architectures, simplifying the overall system and reducing the computational resources required.
2. The paper introduces a Collaborative Control mechanism, which allows two parallel diffusion models to communicate effectively. This cross-model communication lets the geometry generation model inform and guide the 2D texture model, a unique architectural contribution that enhances model efficiency and adaptability.
3. Rapid and Resource-Efficient Processing: The generation time is highly competitive, making this model a viable choice for real-time applications and scalable deployment.

### Weaknesses
1. In figure 9, the paper observes artifacts, such as visible seams between geometry images, which could compromise visual quality, especially in high-precision applications requiring seamless textures and continuous surfaces. These seams are likely due to discontinuities at chart boundaries, where the geometry image representation fails to maintain consistent surface normals and texture coordinates across different charts. This can lead to noticeable breaks in the rendered surface, particularly when textures are applied that do not align perfectly at these boundaries.

2. While the paper highlights the efficiency and practicality of geometry images, it doesn’t fully address potential limitations of this 2D representation for complex or high-genus shapes. Multi-chart geometry images mitigate some challenges, but further analysis is needed on cases where this approach may fail, such as in scenarios with high geometric distortion or disconnected regions. The method's reliance on a fixed 2D grid structure may struggle with objects that have significant self-occlusion or intricate topological features that cannot be easily unfolded onto a 2D plane without substantial distortion. This could lead to artifacts or loss of detail in these areas.

3. Limited Comparison with Recent Methods: The paper's evaluation lacks comprehensive comparisons with the latest advancements, instead focusing on older benchmarks like DreamFusion, ProlificDreamer, and Shap-E. Expanding comparisons to include recent approaches, such as MVDream, CRM, DreamGaussian, and Text-to-3D using Gaussian Splatting, would clarify where GIMDiffusion specifically excels or encounters limitations. The absence of these comparisons makes it difficult to assess the true competitive edge of GIMDiffusion against state-of-the-art techniques that have demonstrated superior performance in terms of visual fidelity and geometric accuracy.

### Questions
1. Could you include comparisons with more recent Text-to-3D approaches, such as MVDream, CRM, DreamGaussian, and other fast, high-quality methods based on Gaussian Splatting? Including comparisons to more recent approaches would offer readers a clearer understanding of where GIMDiffusion stands relative to current advancements.

2. How does GIMDiffusion perform with diverse object types, especially those with intricate internal structures or shapes? Could you provide more detail on potential methods to mitigate visible seams or artifacts between geometry images? It would be helpful if you could discuss or experiment with approaches for reducing these seams, such as stitching algorithms or blending techniques that could improve texture continuity, especially for high-fidelity applications.

3. The visual quality of this method is not obviously better than some other recent methods, which raises concerns about its competitive edge. While GIMDiffusion offers efficiency and compatibility with 2D architectures, it would benefit from additional improvements or evaluations to enhance the clarity, realism, and continuity of generated textures and geometry.

### Soundness
3

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
4

### Summary
This paper presents a method to generate geometry images with diffusion models, which represents meshes with texture maps with images. Specifically, the authors finetuned stablediffusion to generate the albeda images and use collaborative control to generate the geometry images, which can then be unfolded to 3D meshes. The authors evaluated their method on T^3 bench and shows that it can generally well beyond training data and also have better geometry.

### Strengths
- The idea of using pretrained diffusion models for native 3D generation is interesting and novel
- The proposed method is straightforward and easy to understand. The proposed components are also well validated in the ablation study.
- The generated 3D meshes have semantic information and can be decomposed into several parts, make it potential for downstream editing tasks. It also directly generates UV maps and is directly relightable.

### Weaknesses
 - Although the generated meshes are quite sharp and have details, there are obvious discontinuous artifacts, which can be observed in the video. The reason might be that during reconstructing the ground truth geometry images, these parts are already disconnected. Also, in Fig. 7, the boundaries of the mesh also have noticeable artifacts. What is the reason behind these artifacts? Are these artifacts solvable by improving the current pipeline? Is it possible to apply some post-processing techniques to deal with that?
- The details of the evaluation is not that clear: how many prompts are used during evaluation and what are they? The authors may provide the number of prompts and some examples of that.
- I would like to see more comparison with two-stage mesh methods, e.g. first multi-view and then reconstruct mesh, especially CRM, which works faster and have better quality than LGM to my knowledge. It can also produces UV maps. Besides, the authors should also show more examples of comparison in the paper. It would be great if the authors could provide the same comparisons similar to what have been shown in Table 1 for CR.

### Questions
I noticed that the albedo branch used the pretrained VAE, buth GIM is trained from scratch. Have the authors considered also using the pretrained model for GIM? What is the reason of not using the pretrained model? Is there any comparison for that?

### Soundness
3

### Presentation
3

### Contribution
3
