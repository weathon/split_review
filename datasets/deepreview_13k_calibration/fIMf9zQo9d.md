# GeoDream: Disentangling 2D and Geometric Priors for High-Fidelity and Consistent 3D Generation

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 6, 3, 3

## Abstract
Text-to-3D generation by distilling pretrained large-scale text-to-image diffusion models has shown great promise but still suffers from inconsistent 3D geometric structures (Janus problems) and severe artifacts. The aforementioned problems mainly stem from 2D diffusion models lacking 3D awareness during the lifting. In this work, we present \Ours, a novel method that incorporates explicit generalized 3D priors with 2D diffusion priors to enhance the capability of obtaining unambiguous 3D consistent geometric structures without sacrificing diversity or fidelity. Specifically, we first utilize a multi-view diffusion model to generate posed images and then construct cost volume from the predicted image, which serves as native \textbf{3D geometric priors}, ensuring spatial consistency in 3D space. Subsequently, we further propose to harness 3D geometric priors to unlock the great potential of 3D awareness in 2D diffusion priors via a disentangled design. Notably, disentangling 2D and 3D priors allows us to refine 3D geometric priors further. We justify that the refined 3D geometric priors aid in the 3D-aware capability of 2D diffusion priors, which in turn provides superior guidance for the refinement of 3D geometric priors. Our numerical and visual comparisons demonstrate that \Ours generates more 3D consistent textured meshes with high-resolution realistic renderings (i.e., 1024 $\times$ 1024) and adheres more closely to semantic coherence. Our code and evaluation of 3D metric are available at: \href{https://mabaorui.io/GeoDream_page}{GeoDream}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
GeoDream presents an innovative approach to 3D asset generation by integrating disentangled 3D priors with 2D diffusion models. This method leverages a multi-view diffusion model to generate posed images, subsequently constructing a cost volume as a 3D prior to ensure spatial consistency. By separating 2D and 3D priors, GeoDream allows iterative refinement of these priors, enhancing the model’s 3D awareness without compromising the diversity or fidelity of generated 3D models.

### Strengths
1. The disentangled approach to handling 2D and 3D priors effectively addresses the Janus problem, resulting in improved 3D consistency.
2. The framework supports rendering up to 1024x1024, surpassing most SDS-based methods in resolution.
3. GeoDream demonstrates robustness across a wide range of prompts and asymmetric structures.

### Weaknesses
1. The paper only compares with works from 2023 and does not include comparisons with more recent papers from CVPR 2024 and ECCV 2024. I have observed that some papers have better visualization results than this paper, such as One-2-3-45++. It would be beneficial for the paper to include these comparisons to demonstrate its standing in the current research landscape.
2. I do not understand the rationale behind the second phase, which is the optimization of the texture decoder using the SDS loss. In my view, if the multi-view diffusion model performs well, the SDS loss would be unnecessary, as evidenced by some recent papers. Is it because the multi-view diffusion model trained in this paper does not generate satisfactory results?
3. The use of cost volume to define the 3D representation seems odd. While I understand that cost volume adds 3D regularization, it has several drawbacks, including: (a) The cost volume essentially fuses multi-view features. If the input images have occlusion relationships, the cost volume cannot fuse to obtain the correct feature volume. (b) The spatial complexity of cost volume is quite large, which limits the resolution.
4. Overall, the paper's design shows some technical improvements compared to 2023's work, but it seems somewhat outdated compared to the work presented at CVPR 2024 and ECCV 2024. Although the ablation studies are complete, I still do not believe this paper is suitable for acceptance by ICLR.
5. The paper should present more generation results from the multi-view diffusion model to demonstrate its effectiveness, as this model is the core technology of the paper. It is also necessary to clarify how this diffusion model improves upon MVDream. Personally, I do not believe that improvements in 3D representation or training methods can bring about fundamental enhancements. The essence of 3D generation is to learn a stronger 3D prior, which may be represented by a multi-view diffusion model or a direct 3D generative model.

### Questions
1. Table 2 appears to have a formatting issue—could you clarify the template used?
2. Why does Figure 3 present the generated mesh using rendered RGB rather than pure mesh? This choice limits the ability to assess mesh quality directly.

Please see more questions in the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper disentangles 2D and 3D priors on text-to-3D generation and can generation up to 1024 resolution.

### Strengths
1. Higher resolution text-to-3D generation
2. Disentangled 2D and 3D representation
3. Results are good
4. They combined Neus and DMTet as 3D representation

### Weaknesses
1. There are still some artifacts on the extracted mesh.

### Questions
It would be better if the authors can show comparison with baseline methods in the videos.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper tackles the task of Text-to-3D generation, addressing the technical challenge of the Janus problem that previous methods have encountered. The key insight and motivation is to leverage 2D diffusion priors to enhance the generation quality. The approach involves using a multi-view diffusion model to generate multi-view images, representing the 3D object with a cost volume, and then optimizing the 3D object using differentiable rendering from the generated multi-view images. In the second stage, the geometry decoder is fixed, and the texture decoder is optimized based on the SDS loss, resulting in improved 3D object generation from textual descriptions.

### Strengths
1. The ablation studies are sufficient to validate the effectiveness of the proposed components.
2. The paper is well written and easy to read.

### Weaknesses
1. The paper only compares with works from 2023 and does not include comparisons with more recent papers from CVPR 2024 and ECCV 2024. I have observed that some papers have better visualization results than this paper, such as One-2-3-45++. It would be beneficial for the paper to include these comparisons to demonstrate its standing in the current research landscape.
2. I do not understand the rationale behind the second phase, which is the optimization of the texture decoder using the SDS loss. In my view, if the multi-view diffusion model performs well, the SDS loss would be unnecessary, as evidenced by some recent papers. Is it because the multi-view diffusion model trained in this paper does not generate satisfactory results?
3. The use of cost volume to define the 3D representation seems odd. While I understand that cost volume adds 3D regularization, it has several drawbacks, including: (a) The cost volume essentially fuses multi-view features. If the input images have occlusion relationships, the cost volume cannot fuse to obtain the correct feature volume. (b) The spatial complexity of cost volume is quite large, which limits the resolution.
4. Overall, the paper's design shows some technical improvements compared to 2023's work, but it seems somewhat outdated compared to the work presented at CVPR 2024 and ECCV 2024. Although the ablation studies are complete, I still do not believe this paper is suitable for acceptance by ICLR.
5. The paper should present more generation results from the multi-view diffusion model to demonstrate its effectiveness, as this model is the core technology of the paper. It is also necessary to clarify how this diffusion model improves upon MVDream. Personally, I do not believe that improvements in 3D representation or training methods can bring about fundamental enhancements. The essence of 3D generation is to learn a stronger 3D prior, which may be represented by a multi-view diffusion model or a direct 3D generative model.

### Questions
Authors should compare with SOTA baseline methods and demonstrate the advance of method design.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the challenge of text-to-3D reconstruction with GeoDream, a method that integrates explicit 3D priors with 2D diffusion priors to capture clear, 3D-consistent geometric structures. The approach uses a multi-view diffusion model to generate posed images, then constructs a cost volume from these images as native 3D geometric priors. The 3D priors are integrated with 2D diffusion priors through a disentangled design. Comparisons with existing methods show that GeoDream generates more 3D-consistent textured meshes with strong semantic coherence.

### Strengths
- The method constructs a cost volume as native 3D priors by aggregating predicted multi-view 2D images in 3D space, enhancing multi-view consistency in the generated 3D models.
- By refining geometric priors through a 2D diffusion model, this work shows an improvement in rendering quality and geometric accuracy.
- Comparisons with baselines highlight the method's effectiveness in generating 3D-consistent textured outputs.

### Weaknesses
The proposed method design seems incremental compared to the existing work like One-2-3-45 and has several key limitations:

- Generation Quality: The method's quality does not appear to surpass existing approaches. The visual results, even in the teaser of Fig. 1, reveal artifacts around object boundaries and inconsistencies in geometry, especially visible in mismatched normal maps and images. In the supplementary video, examples like the EAGLE, MUSHROOM, and GIRAFFE also exhibit incomplete geometry, likely due to limitations in the generated cost volume. A comparison with RichDreamer (CVPR 2024), which uses a normal-depth diffusion model as a geometry prior, would be valuable.

- Training of 3D Priors: The generalizabilty and quality of the 3D prior rely on the model for multi-view generation and cost-volume construction, raising questions about its generalizability and robustness for diverse prompts. The paper does not describe in detail how the 3D prior model is trained. The tested prompts cover a narrow range, making it difficult to assess performance across broader scenarios.

- Evaluation and Analysis: The evaluation could be stronger. For example, the user study had only 20 to 30 participants, which may be too small for reliable comparisons. Additionally, the ablation study lacks quantitative metrics to substantiate the design choices.

- Optimization Time: The method requires a significant optimization time, taking around 8 hours per instance, which limits its practicality for broader applications.

### Questions
- Clarification of the novelty.
- clarification of  the sources of artifacts and inaccuracies in the generated geometry? These issues are visible in Fig. 1 and more pronounced in the video examples.
- How does GeoDream compare to RichDreamer (CVPR 2024) in terms of geometric detail and model accuracy?
- Could the authors provide a more thorough user study and ablation study to validate their approach across a broader range of metrics and prompts?

### Soundness
3

### Presentation
3

### Contribution
2
