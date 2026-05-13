# Geometry-aware Score Distillation via 3D Consistent Noising and Gradients

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Score distillation sampling (SDS), the methodology in which the score from pretrained 2D diffusion models is distilled into 3D representation, has recently brought significant advancements in text-to-3D generation. However, this approach is still confronted with critical geometric inconsistency problems such as the ``Janus problem''. We provide a novel insight into this problem, hypothesizing that the incorporation of 3D awareness into the 3D noising process and gradient distillation process may bring about enhanced consistency between gradients, leading to improved fidelity and geometric consistency. To achieve this, we propose a simple yet effective approach to achieve a 3D consistent, geometry-aware noising process, leveraging the advantages that 3D Gaussian Splatting possesses as an explicit 3D representation. Combined with our geometry-based gradient warping and our novel gradient dissimilarity loss, we demonstrate that our method significantly improves performance by addressing geometric inconsistency problems in text-to-3D generation with minimal computation cost and being compatible with existing score distillation-based models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on optimization based text-to-3D generation. The authors propose a geometry-aware score distillation method to address the multi-view consistency issue in SDS. 
Specifically, the authors propose to use 3D consistent noising by warping noises of nearby views with the current 3D modelling parameters. Based on this, a correspondence-aware gradient consistency loss is introduced to encourage the multiview consistency of SDS gradients between nearby viewpoints.

### Strengths
The paper addresses an important issue - multi-view inconsistency in SDS. 
The method is well-motivated, and the design is intuitively sound.
The proposed method is shown to work well with various SDS variants, including 3DFuse, GaussianDreamer and ProlificDreamer.

The presentation is clear.
Good visualizations in Fig. 3, Fig. 4 and Fig. 5.

### Weaknesses
No video demos were shown to validate the generated 3D results.
Some of the generated results still appeal oversmoothness and unrealistic (Fig. 6, Fig. 11).

Adding an algorithm highlighting the differences from the original SDS would help readers better understand the optimization process.

Since the paper claims to introduce minimal additional computational cost compared to SDS, more details regarding this cost should be included.

In addition to SDS-like optimization methods, there is another line of text-to-3D generation approaches that directly train on large-scale 3D datasets to enable feedforward generation, such as [1, 2]. Although these approaches are not directly comparable, clarifying this distinction in the related work section would be helpful.

Considering similar efforts to restrict the noise sampling space, a noise recalibration scheme was introduced in [3]. A discussion on the similarities and differences is recommended.

### Questions
Adding an algorithm highlighting the differences from the original SDS would help readers better understand the optimization process.

Since the paper claims to introduce minimal additional computational cost compared to SDS, more details regarding this cost should be included.

In addition to SDS-like optimization methods, there is another line of text-to-3D generation approaches that directly train on large-scale 3D datasets to enable feedforward generation, such as [1, 2]. Although these approaches are not directly comparable, clarifying this distinction in the related work section would be helpful.

Considering similar efforts to restrict the noise sampling space, a noise recalibration scheme was introduced in [3]. A discussion on the similarities and differences is recommended.

ref:

    [1] LGM: Large Multi-View Gaussian Model for High-Resolution 3D Content Creation.
    [2] 3DTopia: Large Text-to-3D Generation Model with Hybrid Diffusion Priors.
    [3] Diverse and Stable 2D Diffusion Guided Text to 3D Generation with Noise Recalibration.

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
This paper introduces a method called Geometry-aware Score Distillation. The experimental results demonstrate that the proposed approach can improve performance and address geometric inconsistencies in SDS-based text-to-3D generation tasks.

### Strengths
1. Efficient Incorporation of 3D Consistency: The paper directly adjusts the gradients of Score Distillation Sampling (SDS) without requiring 3D data to fine-tune a 2D diffusion model. This allows for the incorporation of 3D consistency with minimal computational overhead.

2. Significant Improvement over Baselines: The proposed method shows noticeable enhancements in both 3D consistency and appearance details when compared to baseline models such as GaussianDreamer, ProlificDreamer, and MVDream.

### Weaknesses
1. Dependency on Initial Point Cloud: The method requires establishing correspondences between different views, necessitating an initial point cloud. The paper primarily compares against Gaussian splatting-based methods like GaussianDreamer. According to previous literature [1], when shape initialization is used as a constraint, the Janus problem is substantially mitigated. Therefore, the effectiveness of the proposed method requires more rigorous justification. Specifically, the reliance on an initial point cloud, even if derived from a relatively simple method, introduces a potential bias. The method's performance could be heavily influenced by the quality and density of this initial point cloud, which is not thoroughly explored in the paper. A more comprehensive analysis of how different point cloud initialization strategies affect the final 3D reconstruction is needed to validate the robustness of the approach.

2. Comparative Evaluation Concerns: In comparing their method with ProlificDreamer, the authors use 3D-Fuse—originally designed to address the Janus problem—as a baseline. This choice potentially diminishes the perceived effectiveness of the proposed method. Additionally, as observed in Figure 7, the method does not significantly enhance 3D consistency compared to ProlificDreamer; it primarily reduces floating artifacts in the background. Similar issues have been discussed in prior work [2] and can be addressed by adjusting the Classifier-Free Guidance (CFG) in diffusion models. Thus, further experimental evidence is needed to substantiate the authors' claim of enhanced 3D consistency. The comparison with ProlificDreamer using 3D-Fuse is not a direct comparison of the core methods, but rather a comparison of the proposed method against a baseline that already incorporates a technique to mitigate the Janus problem. This makes it difficult to isolate the specific contribution of the proposed method. Furthermore, the observation that the primary improvement is the reduction of floating artifacts, rather than a fundamental improvement in 3D consistency, raises questions about the actual novelty and impact of the method.

### Questions
Please see the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to address the well-known Janus problem of the SDS loss. Specifically, it proposes modifying the noise sampling process of the SDS loss by replacing random noise with 3D-consistent noise. The 3D-consistent noise is generated by extending the integral noise method of Chang et al. (2024) using an intermediate point cloud representation.

### Strengths
1. The paper is well-organized, easy to follow, and clearly presented.
2. The proposed method offers a fresh perspective on the multi-face Janus problem of the SDS loss, particularly from the standpoint of random noise sampling.
3. Although the solution is an extension of existing work, it is still novel in the 3D generation field.

### Weaknesses
1. My primary concern lies in the use of latent diffusion models, as all experiments in the paper are conducted on latent diffusion models. While I do not doubt that the proposed method could be effective on pixel-space diffusion models, the entire analysis may not be applicable to latent diffusion models.

- **First,** 3D-consistent noise in latent space does NOT equate to consistent gradients in pixel space. Imagine a simple case where the latent map is shifted to the right or left by a few pixels—the VAE would not decode the same image with the same shift in pixel space. In the case of SDS combined with latent diffusion, the gradient at the latent space needs to pass through a VAE encoder composed of multiple convolutional layers and activation functions. As a result, simply keeping the gradient of a portion of the latent map unchanged does not ensure that the corresponding image regions will also receive an unchanged gradient. The non-linear nature of the VAE encoder, with its convolutional layers and activation functions, introduces a complex mapping that makes it difficult to predict how changes in the latent space will translate to the pixel space. This is especially problematic when considering the fine-grained details that are crucial for 3D consistency.

- **Second,** this limitation has already been highlighted in the original work of Chang et al. (2024) (see their Appendix E). The authors of the integral noise method in Chang et al. (2024) noted that their method does NOT perform well in latent diffusion models and provided three reasons for this. Could the authors clarify why integral noise fails in the temporal domain but succeeds in the 3D case using LDM?

2. The paper does not address the limitations of the proposed method.

### Questions
My major concern is the applicability of the proposed method in latent diffusion models. Please refer to the weaknesses outlined above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a method to enhance SDS-based 3D generation through 3D consistent noising and geometry-aware gradient warping. The authors presented an algorithm that could warp the gaussian noise at different camera view while maintaining Gaussian properity for one camera view. The 3D consistent noising aims to improve gradient consistency, while the geometry-aware gradient warping seeks to reduce geometric artifacts.

### Strengths
1. The proposed noising method establishes a correlation between camera views. The noising methods can generate i.i.d. Gassian noise correctly while maintaining correlation properities.

2. The introduction of the *correspondence-aware gradient consistency loss* serves as a regularization technique to mitigate geometry artifacts.

### Weaknesses
1. The motivation behind *3D consistent noising* lacks clarity. Although the authors reference its similarity to $\int$-noise [1] for improving texture consistency in video generation, the discussion on its application in 3D generation is insufficient. This omission raises questions about how 3D consistent noising can enhance 3D generation specifically. The introduction of 3D consistent noising appears unrelated to the 3D score interpretation of SJC, raising concerns about its relevance and application within this context. Thus, I suggest the authors to provide a more detailed explanation of how 3D consistent noising specifically addresses challenges in 3D generation.

2. The noising method is confined to point cloud (3D GS) representation, limiting its applicability to other forms such as NeRF or Mesh. Additionally, the algorithm appears to overlook occlusion; for instance, a Gaussian particle not visible from the current camera view may still influence noise computation, resulting in questionable correlations compared to surface warp (optical flow) as in $\int$-noise [1].

3. The experimental evaluation is weak, with qualititive results from both the baselines and proposed methods showing low quality (Fig. 6, 7, 11). The results strongly underperform SoTA implementations like ProlificDreamer (VSD) and LucidDreamer (ISM), undermining the validity of the user study. Furthermore, this paper is lack of quantitative metrics. For the CLIP score in Fig. 13, details on the number of prompts and seeds used in the experiments are missing, and a more thorough experimentation (with at least 25 prompts) is needed.

4. The *correspondence-aware gradient consistency loss* remains difficult to grasp despite the explanations in Sec. 4.4. The rationale behind why sharp changes are likely artifacts needs clarification. I suggest the authors to provide a more intuitive explanation of why sharp changes are likely to be artifacts. Additionally, the ablation study in Fig. 8 fails to effectively illustrate its impact; more results with varied seeds or prompts would strengthen the argument.

### Questions
1. I recommend including a pseudo-algorithm to enhance comprehension. Is the noise regenerated after each batch of gradient updates? Does the computation of correlation occur solely within the same batch?

2. Are noise particles not visible considered in the computation? If so, why not focus on visible particles, aligning more closely with the computation in $\int$-noise [1]?

3. There are missing experimental details as noted in weakness 3. How many prompts do you experimented with?

[1] How I Warped Your Noise: a Temporally-Correlated Noise Prior for Diffusion Models (https://warpyournoise.github.io/)

### Soundness
2

### Presentation
2

### Contribution
2
