## Human Reviewer 1

### Summary
The paper proposes Stylos, a feed-forward 3D Gaussian stylization framework. Given one or more unposed RGB views of a scene plus a single style reference image, Stylos directly predicts a stylized 3D Gaussian scene in a single forward pass, without per-scene optimization or known camera intrinsics/extrinsics. Stylos explicitly separates geometry and style: geometry is inferred by a VGGT-like alternating-attention backbone, while style is injected through a Style Aggregator that applies global cross-attention from the style tokens to all content-view tokens. The paper also introduces a voxel-based 3D style loss: instead of matching style statistics (mean/variance in VGG feature space) per-frame, Stylos fuses multi-view features into a shared voxel grid and aligns those 3D features to the style distribution, which the authors argue enforces cross-view consistency and preserves geometry. Experiments on CO3D, DL3DV-10K, and Tanks and Temples report improved multi-view consistency (LPIPS/RMSE) and competitive perceptual/artistic quality (ArtScore) compared to per-scene stylization baselines such as StyleRF and StyleGS, and include ablations on cross-attention design and style loss variants.

### Strengths
- Practical significance. Single-forward stylization of an entire 3D Gaussian scene (poses + Gaussians + colors) without per-scene finetuning or known camera parameters could be transformative for content pipelines. This is not just incremental NeRF/3DGS stylization but closer to the real situation, like “instant turn-this-video-into-stylized-3D-assets.”
- Architectural clarity. Clean separation between a geometry backbone and a Style Aggregator branch (global cross-attention conditioning on the style image). The ablation across “frame-only,” “hybrid,” and “global-only” variants is convincing and shows why global conditioning improves structure and texture coherence.
- Breadth of evaluation. The paper reports not only reconstruction-like metrics (PSNR/SSIM/LPIPS) but also temporal / multi-view consistency metrics (LPIPS & RMSE at different frame gaps) and ArtScore for perceptual “artness,” and demonstrates cross-category and cross-scene generalization.

### Weaknesses
- 3D style loss justification is empirical. The 3D voxel-statistics loss gives better LPIPS/RMSE consistency, but the paper does not analyze potential side effects such as global color bleeding or loss of local style detail in poorly observed regions. Some intuition or failure-case visualization would strengthen the argument that voxel-statistics matching is fundamentally better than 2D scene-level matching.
- Scalability limits. Although Stylos is advertised as handling up to “hundreds of views,” the scaling experiment shows visible degradation beyond ~32 views per batch (edge artifacts, instability in the Gaussian representation). The method may still be quite useful, but this practical constraint, probably brought by VGGT, should be communicated more prominently.

### Questions
- Failure cases of the 3D style loss.
Are there any visual failure cases where voxelized style statistics hurt local detail (e.g., oversmoothing, texture bleeding in occluded regions)? Right now we only see success cases and quantitative gains.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
3

---

## Human Reviewer 2

### Summary
The paper introduces StylOS, an efficient framework for view-consistent 3D style transfer using 3D Gaussian Splatting (3DGS). The main technical contribution is a single-forward inference model, built upon VGGT and AnySplat, that directly predicts the stylized 3DGS representation. This approach enables optimization-free, geometry-aware synthesis from unposed content views (from a single image to a multi-view collection) and a reference style image. By bypassing time-consuming per-scene optimization, StylOS achieves fast processing and superior generalization to unseen scenes and styles.

### Strengths
1. **Single-Forward Efficiency**: The most compelling contribution is the ability to perform high-quality 3D style transfer in a single forward pass without per-scene optimization. This drastically reduces processing time and makes 3D stylization scalable for real-time or large-scale applications.

2. **Transformer Integration and Unposed Capability**: By utilizing a Transformer architecture (built upon VGGT) to directly predict the parameters of the stylized 3D Gaussian Splatting representation, the method bypasses the traditional optimization pipeline and simultaneously enables robust handling of unposed content (single or multi-view). This significantly lowers the barrier to entry for users, as complex camera pose estimation is not required.

3. **Generalization and Robustness**: The method demonstrates excellent generalization capabilities across unseen content scenes, object categories, and style images, suggesting robust learning of disentangled style and geometry features.

### Weaknesses
1. **Limited Technical Novelty in Overall Framework**: The overall conceptual framework of achieving fast, optimization-free 3D stylization by integrating a feed-forward 3D reconstruction model (VGGT/AnySplat) with cross-attention for style injection is highly similar to previous works like Styl3R (NeurIPS 2025, published on arXiv in May 2025), which uses Dust3R. While StylOS's integration of VGGT allows it to process a wider and more flexible range of input views, the core technical contribution of the idea of a single-forward 3D stylization framework is substantially weakened by this conceptual overlap. The authors should better address this overlap and clearly articulate how their specific implementation of the style injection and 3DGS prediction provides unique advantages over Styl3R's architecture.

2. **Style Fidelity vs. Optimization**: Although the speed advantage is clear, a deeper discussion or visual comparison is needed to evaluate the potential trade-off in style fidelity against state-of-the-art optimization-based 3D style transfer methods like 𝒢‐Style: Stylized Gaussian Splatting or ARF. Are there certain styles (e.g., fine-grained texture styles) where the feed-forward approach visibly struggles compared to optimization?

3. **Minor Formatting Concern (Font)**: It appears the authors may have modified the default font used in the ICLR style configuration.

### Questions
1. **Style Control and Blending**: Can the authors demonstrate fine-grained control over the stylization process? Specifically:
a. Can the system adjust the content-style trade-off weight post-inference to control the strength of the stylistic transfer?
b. Can the model perform multi-style blending by interpolating or averaging the style embeddings from two or more distinct style images?

2. **Input and Output Resolution**: What is the range of resolutions for the input content views (single or multi-view) and the output rendering that the model is designed to support? Are there inherent limitations or scaling constraints related to the Transformer architecture or 3DGS representation density?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
4

---

## Human Reviewer 3

### Summary
The paper introduces a feedforward stylized Gaussian method to achieve efficient, high-quality, and visually pleasing 3D scene reconstruction and stylization in a single step of model inference. The proposed approach is built upon VGGT, taking multi-view scene images and a style exemplar image as input. The model predicts the depth and camera poses for each view, while the predicted pixel Gaussian attributes are merged into voxels using confidence-based weights following the AnySplat framework. The results, as demonstrated in the figures and supplementary video, are remarkable.

This feedforward stylized Gaussian model has the potential to significantly impact the field. Artistic stylization, a cornerstone of human creativity throughout history, plays a vital role in bridging the technical and emotional aspects of visual representation. In the context of 3D world reconstruction, artistic stylization becomes even more critical, as it encapsulates the essence of reality through the lens of human emotion, emphasizing mood, character, and individuality. By enabling stylized 3D scene reconstruction without the need for test-time training, this model addresses a significant challenge and represents a major step forward in both technical and artistic innovation.

### Strengths
The technical strengths of the paper can be summarized as follows:

1. This work is the first to achieve a stylized 3D world in a fully feedforward manner. From the early days of this field, StylizedNeRF introduced the concept of reconstructing 3D scenes using NeRF, accompanied by a conditional stylization module. While it generalized across styles, it required per-scene optimization. ARF, on the other hand, achieved superior results using a style-matching loss and a deferred backward strategy, but it was not generalized across scenes or styles. Both methods, being NeRF-based, faced limitations due to the high GPU demands during training, requiring solutions like mutual learning and deferred optimization to mitigate these challenges. Similarly, StyleRF was also restricted to per-scene optimization. 

   In the era of 3DGS, StylizedGS achieved impressive results in 3D stylization but remained constrained by per-scene fitting. This paper, however, marks a significant milestone by creating a stylized 3D world using a tuned foundation model like VGGT, combined with a generalized stylization module, enabling a fully feedforward pipeline. This eliminates the need for lengthy optimization processes. There is no more waiting hours to transform multi-view images into an artistic 3D world. This breakthrough paves the way for future research to focus on achieving even faster and higher-quality stylizations using similar feedforward approaches.

2. The results presented in the paper are both impressive and inspiring. The examples, particularly in the supplementary video, showcase how realistic 3D scenes can be transformed into artistic styles such as cartoon, sketch, and painting. The stylization maintains consistency across views without any flickering artifacts, which is a significant achievement. Moreover, obtaining such high-quality results in a single feedforward inference is truly remarkable and highlights the potential for real-time applications in this domain.

### Weaknesses
1. The most significant contribution of this work is the introduction of a feedforward 3D stylization model, whose core advantages lie in faster inference and reduced memory usage. However, these critical metrics are not evaluated in the experiments. The paper should include a comparison of stylization time across prior works, from the earliest StylizedNeRF, ARF, and StyleRF to the more recent StyleGaussian and StylizedGaussian. For methods requiring per-scene fitting, the stylization time should account for both training and rendering times. Such comparisons would provide readers with a clearer perspective on how this work advances the field in terms of efficiency and practicality.

2. The comparison between NeRF-based and Gaussian-based stylization approaches is not adequately addressed. While StyleRF focuses on zero-shot stylization, its stylization quality is not the strongest. A detailed comparison with stylization examples from StylizedNeRF and similar NeRF-based methods is essential to highlight the advantages of the proposed approach. Moreover, StylizedGS, which outperforms StyleGS, should be included as the representative Gaussian-based stylization method in the comparisons. Incorporating these comparisons would strengthen the paper by demonstrating the superiority of the proposed method over both NeRF-based and Gaussian-based approaches.

### Questions
1. **Include Inference Speed Comparisons**:  
   Adding a comparison of inference speed would highlight the advantages of the proposed method and make the paper more compelling. Demonstrating faster processing times would provide a stronger justification for the model's practical contributions to the field.

2. **Compare with StylizedNeRF and StylizedGaussian**:  
   Include comparisons with StylizedNeRF and StylizedGaussian, as their stylization results are superior to those of StyleRF and StyleGaussian, respectively. The latter two methods primarily focus on zero-shot and fast stylization but rely on a CNN decoder, which means they are not strictly stylized **radiance** fields but rather stylization **feature** fields.

### Soundness
4

### Presentation
4

### Contribution
4

### Rating
8

### Confidence
5

---

## Human Reviewer 4

### Summary
This paper presents StylOS, a single-forward 3D style transfer framework based on 3D Gaussian Splatting. The method employs a Transformer backbone with a dual-pathway design that separates geometry prediction from style injection: the geometry pathway maintains self-attention mechanisms to preserve geometric fidelity, while style is injected via global cross-attention to ensure multi-view consistency.

### Strengths
1. Proposes the first single-forward-pass 3D style transfer framework that requires no camera pre-calibration, offering significant practical value.

2. The method demonstrates strong scalability, supporting processing from a single view to hundreds of views.

### Weaknesses
1. Lacks fair comparison with per-scene optimization methods under the same computational budget.

2. Critical implementation details are missing regarding the voxelization operation: What is the voxel resolution? How are occlusions handled? What is the specific implementation of confidence weighting? Do these factors have significant impact on the results?

3. The weight parameters for each loss term are not provided.

4. The specific architecture of the Gaussian Adapter is not described in detail.

5. There is insufficient discussion on which scene types or style categories the method performs poorly on.

6. Why does global cross-attention not only improve style consistency but also enhance geometric fidelity? This seems counterintuitive and requires deeper analysis.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3