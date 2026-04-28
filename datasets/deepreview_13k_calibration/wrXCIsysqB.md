# GaussianBlock: Building Part-Aware Compositional and Editable 3D Scene by Primitives and Gaussians

- Decision: Accept
- Avg Score: 5.60
- Scores: 6, 6, 6, 5, 5

## Abstract
Recently, with the development of Neural Radiance Fields and Gaussian Splatting, 3D reconstruction techniques have achieved remarkably high fidelity. However, the latent representations learnt by these methods are highly entangled and lack interpretability. %This entanglement nature not only hinders the understanding and analysis of the model but also discouraging precise controllable editing of the reconstructed assets. 
In this paper, we propose a novel part-aware compositional reconstruction method, called GaussianBlock, that enables semantically coherent and disentangled representations, allowing for precise and physical editing akin to building blocks, while simultaneously maintaining high fidelity.
Our GaussianBlock introduces a hybrid representation that leverages the advantages of both primitives, known for their flexible actionability and editability, and 3D Gaussians, which excel in reconstruction quality. Specifically, we achieve semantically coherent primitives through a novel attention-guided centering loss derived from 2D semantic priors, complemented by a dynamic splitting and fusion strategy. 
Furthermore, we utilize 3D Gaussians that hybridize with primitives to refine structural details and enhance fidelity. 
Additionally, a binding inheritance strategy is employed to strengthen and maintain the connection between the two. 
Our reconstructed scenes are evidenced to be disentangled, compositional, and compact across diverse benchmarks, enabling seamless, direct and precise editing while maintaining high quality.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper is on 3D part aware semantic editing of scenes using Gaussian Splatting . Similar to
previous work like GaussianAvatar the paper uses a prior for initializing the gaussians in the
form of super-quadratics . The paper proposes a 2 stage training process in order to obtain
semantically coherent and disentangled gaussians that can obtain high fidelity edited images
.The first stage optimizes the super-quadratics and the second stage uses these to initialize the
gaussians and rasterize images. The underlying super-quadratics can be used to edit the parts
of the object and reflect the changes subsequently in the gaussians the rasterized images .

### Strengths
- Using super-quadratics as a prior for part aware editing using gaussian splatting is a novel approach .
- Soft Dual rasterization for rasterizing the vertices and bounding boxes is novel, though this needs to be explained better in the paper.

### Weaknesses
 - The number of parts seems to be decided by the super-quadratics which implies there is
no control over the granularity of the parts?
- All results in the paper edit a single part of an object in the input image. 
- All results are shown for 360 multi-view scenes.
- The paper lacks a thorough explanation of the soft dual rasterization process, making it difficult to assess its novelty and effectiveness. The description should include more details on how the vertices and bounding boxes are rasterized and how this differs from standard rasterization techniques.
- The evaluation is limited by the choice of datasets. Showing results on DTU and BlendedMVS for the entire dataset while only showing a few scenes for TnT and Mip-Nerf360 raises questions about the generalizability of the method. The selection of scenes for TnT and Mip-Nerf360 seems arbitrary and not representative of the dataset's complexity.

### Questions
- Since performance of the method seems to be reliant on the super-quadratic primitives this places a limit on the number of parts that can be edited. Is there any way to control this while not losing fidelity ?
- What is the effect on editing multiple parts in the same object in a single pass?
- Can you show some results on more complex objects with more than 4-5 parts ?
- Show more results on some forward facing scenes (Shiny, LLFF etc) ?
- Why are the results for DTU and BlendedMVS shown for the whole dataset but for TnT and Mip-Nerf360 on a few scenes ? Why not the entire dataset ? or at least a few more scenes (2 scenes are not enough)
- What is the required time for training since it is a 2 stage process ? The mention of 6 hours for 1 scene seems high and which dataset task does that scene belong to? Training time for splatting varies across different datasets and scenes so it is important
to clarify that .

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a pipeline for part-aware compositional reconstruction with 3D Gaussians, enabling precise and physically realistic editing similar to building with blocks. The method involves two training stages: In the first stage, superquadric blocks are optimized using a reconstruction loss and an attention-guided centering loss, guided by the SAM model. In the second stage, Gaussians are bound to the triangles of primitives using localized parameterization and are further optimized with an RGB loss and a local position regularization. Experiments on various datasets demonstrate state-of-the-art part-level decomposition and controllable, precise editability while maintaining high rendering fidelity.

### Strengths
1. The block-based, part-aware compositional reconstruction enables intuitive local editing compared to SAM-based decomposition methods, which I find particularly interesting.
2. To decompose a 3D scene into semantically coherent compositional primitives combined with Gaussians, the method proposes an effective two-stage optimization approach to tackle this challenging problem. It’s not straightforward to prevent sub-optimal decomposition, yet the results show compact, well-defined parts.
3. The paper demonstrates several types of local editing with the decomposed primitives, such as moving, duplicating, and rigging parts.
4. The paper is well-written, and the figures are beautiful and clear.

### Weaknesses
The reconstruction quality is not comparable to the original 3DGS and other baselines. On the DTU, Truck, and Garden datasets, the PSNR of this method is 5 points lower than that of the original 3DGS. This discrepancy in reconstruction quality raises concerns about the trade-off between editability and fidelity. While the method achieves impressive part-level decomposition and editability, the lower PSNR suggests a significant loss of detail in the reconstructed scenes. The use of level-1 superquadrics, with their limited geometric complexity (42 vertices and 80 faces), likely contributes to this issue, as they may not be able to accurately represent the intricate details present in the original scenes. This limitation is particularly noticeable in areas with fine structures or complex textures, where the coarse primitives may lead to a smoothed or simplified representation.

### Questions
1. Does the method have any failure cases on these datasets in the paper, aside from challenges with complex backgrounds?
2. The paper reports in the supplementary materials that the initial K is set to 10. How was this number determined, and how robust is the method to different initial values?

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
This paper proposes GaussianBlock, a part-aware compositional 3D scene representation that combines Gaussian splatting with superquadric primitives. Leveraging the strengths of both, the authors introduce Attention-guided Centering (AC) Loss and dynamic fusion/splitting modules to enhance semantic coherence and editability.

### Strengths
1. The paper is technically well-written, presenting ideas clearly and effectively.
2. Detailed experiments and visualizations demonstrate the method’s effectiveness.
3. The controllable editability feature is highly practical, enabling applications in diverse 3D scene settings.

### Weaknesses
1. Adding more multi-view visualizations in Figure 4 would provide clearer insights into the coherence of reconstructed scenes from various perspectives.
2. The reconstruction quality is lower than standard 3D Gaussian methods, potentially limiting fidelity in highly detailed scenes. Improvements here could enhance the method’s overall competitiveness.
3. Background handling, also a known limitation of DBW, is not fully addressed in this work, leaving room for further improvement in complex scenes where background elements are significant.

### Questions
Could you provide details on FPS and training times for both stages to clarify the overall running time? Real-time performance and faster training are also advantages of incorporating 3D Gaussians.

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
The paper proposes a new 3D reconstruction pipeline based on semantic primitives that facilitates 3D scene editing and animation. At the core of the proposed method is the 3D representation based on superquadrics that is derived from the pixel-aligned SAM features. By necessary attention-guided clustering and splitting&fusion strategy, the centroids are fused into part-wise primitives to represent the 3D object. In the second stage, 3D Gaussians are bound to the surface of primitives for photorealistic rendering while maintaining the ability for animation. Although the reconstruction quality of the proposed method cannot surpass previous non-editable methods for 3D reconstruction like 3DGS, it improves the performance against editable and primitive-based methods for 3D reconstruction like DBW by a large margin.

### Strengths
- To enable intuitive drag-based 3D editing and animation, the paper proposes a new hybrid representation based on superquadrics followed by 3DGS. It works well in terms of decomposing object-centric scenes into semantic primitives with a quality boost compared with previous SOTA DBW.
- The algorithm designed for semantic alignment of superquadrics from the semantic prior of SAM looks neat to me.
- The paper is well-structured and easy to follow.

### Weaknesses
 - Lack of necessary qualitative results to support the paper’s claim: As a method for 3D editing and animation, I personally hope to see qualitative results in multiple viewpoints and timestamps, especially dynamic results which could be better demonstrated by a demo video. Otherwise, there is no clue to support that the proposed method is a good fit for editing and animating 3D scenes.
- Is Superquadrics + 3DGS a good design? Basically, the superquadrics used in the paper have two roles: 1) offering a good initialization for the latter 3D Gaussians and 2) providing group-wise semantic correspondence of each Gaussian centroid which facilitates animation and editing. However, this two-stage pipeline inherits the downside of 3D Gaussians when generalizing to unseen “poses” of objects. As shown in Figure 4, the animated results contain severe artifacts when the animated part is moved.
- Worthy discussion against another primitive-based representation: It is worth mentioning Mixture-of-Volumetric-Primitives as an alternative representation for the target task in this paper. It naturally has the properties for both stages in the proposed method: 1) semantic correspondence alignment and 2) photorealistic differentiable rendering. It would be great to see authors’ discussions and even experiments for this representation. Ideally, the only thing to do is to apply semantic alignment for all primitives without involving the second stage 3DGS training.
- There is prior work in deforming and animating a well-trained 3D scene representation, which could be treated as a top-down approach (the proposed method could be treated as a bottom-up approach) to solve similar tasks:
    - **Deforming Radiance Fields with Cages. ECCV 2022**
    - **CageNeRF: Cage-based Neural Radiance Fields for Generalized 3D Deformation and Animation. NeurIPS 2022.**

### Questions
- The proposed method requires bounding box and point prompts along with input posed images. This difference should be highlighted as a vanilla 3D reconstruction method does not require such information. Additional information introduced into the pipeline could lead to unfair comparisons. An interesting baseline would be using 3DGS to reconstruct the semantic scenes where the SAM segmented images are used as training images. The semantic correspondence could be further introduced into the original 3DGS by finding minimum distance based on world coordinates.
- Is the proposed method (especially for the first stage) sensitive to segmentation failure? Some scenes like forward-facing scenes in LLFF have complicated scene geometry (e.g., leaves and flowers), which could be difficult for accurate segmentation.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a 3D scene reconstruction approach that achieves high fidelity, editability, and part-awareness by combining superquadric primitives and 3D Gaussians.

### Strengths
1. Novel Hybrid Representation: The paper proposes a novel hybrid model combining superquadric primitives for part-awareness and 3D Gaussians. This hybrid design achieves high-quality 3D reconstructions while supporting precise part-level editing.

2. Semantic Coherence Through Attention-Guided Centering Loss: It ensures that each superquadric primitive aligns semantically with different parts of the object. By clustering attention maps, this loss encourages disentanglement, making each part more coherent and interpretable.

### Weaknesses
1. The datasets used in the experiments are limited to DTU, BlendedMVS, Truck, and Garden, which makes it challenging to assess the generalizability of the proposed method. A broader range of data, including more complex and diverse scenes, would better demonstrate its robustness across various scenarios. The current selection is insufficient to validate the method's performance on intricate geometries and textures.

2. As shown in Table 2, the method exhibits a noticeable drop in rendering quality compared to the 3DGS baseline and does not demonstrate a clear advantage over baseline methods. The authors do not provide a detailed analysis to explain this performance gap, particularly regarding the impact of the superquadric primitive initialization on the final rendering quality. While editability is an attractive feature, it should not come at the cost of compromising fundamental rendering quality, and the trade-off needs to be more thoroughly investigated.

3. High Computational Cost: This approach takes around 6 hours for the training time, which is time-consuming. This paper lacks the rendering frame rate and the information related to the time cost during the editing process. The absence of detailed timing metrics for both training and editing makes it difficult to evaluate the practical applicability of the method, especially in real-world scenarios where efficiency is crucial.

### Questions
1. In Line 078-083, this paper discuss about the problem of "lacking controllable editability". However, multi-grained decomposition has already been achieved in lots of previous works for both GS-based or NeRF-based, such as [1, 2]. Besides, "waving arms or shaking heads" as mentioned are common editing demonstration in the field of dynamic gaussian works based on my knowledge, such as [3]. As an evidence, for the editing results in Fig.4, I believe they can be achieved by [1] or [2]. Therefore, a straightforward method for "controllable editability" defined in this paper might be combining existing works. I suggest the authors make the claims clearer for the motivation of the design.


[1] Garfield: Group anything with radiance fields, CVPR 2024

[2] Total-Decom: Decomposed 3D Scene Reconstruction with Minimal Interaction, CVPR 2024

[3] Sc-gs: Sparse-controlled gaussian splatting for editable dynamic scenes, CVPR 2024

### Soundness
2

### Presentation
3

### Contribution
3
