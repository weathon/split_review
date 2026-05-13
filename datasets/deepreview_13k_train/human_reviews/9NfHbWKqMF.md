# SplatFormer: Point Transformer for Robust 3D Gaussian Splatting

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
3D Gaussian Splatting (3DGS) has recently transformed photorealistic reconstruction, achieving high visual fidelity and real-time performance. However, rendering quality significantly deteriorates when test views deviate from the camera angles used during training, posing a major challenge for applications in immersive free-viewpoint rendering and navigation. In this work, we conduct a comprehensive evaluation of 3DGS and related novel view synthesis methods under \textit{out-of-distribution (OOD) test camera scenarios}. By creating diverse test cases with synthetic and real-world datasets, we demonstrate that most existing methods, including those incorporating various regularization techniques and data-driven priors, struggle to generalize effectively to OOD views. To address this limitation, we introduce \textit{SplatFormer}, the first point transformer model specifically designed to operate on Gaussian splats. SplatFormer takes as input an initial 3DGS set optimized under limited training views and refines it in a single forward pass, effectively removing potential artifacts in OOD test views. To our knowledge, this is the first successful application of point transformers directly on 3DGS sets, surpassing the limitations of previous multi-scene training methods, which could handle only a restricted number of input views during inference. Our model significantly improves rendering quality under extreme novel views, achieving state-of-the-art performance in these challenging scenarios and outperforming various 3DGS regularization techniques, multi-scene models tailored for sparse view synthesis, and diffusion-based frameworks. Project page: \url{https://sergeyprokudin.io/splatformer/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces SplatFormer, a point transformer model for refining 3D Gaussian Splatting (3DGS) representations under out-of-distribution (OOD) view conditions (with initialized Gaussian Splats). This is motivated by 3DGS struggles with quality degradation when test views differ significantly from training views. SplatFormer addresses this by learning to refine Gaussian splats, leveraging attention mechanisms to maintain consistency across viewpoints and removing artifacts in OOD scenariosl, with the collected large-scale object-centric data. The approach outperforms prior methods in robustness on several test datasets.

### Strengths
- The paper introduces a novel and important direction for rendering at unseen, highly relevant test views, addressing a significant gap in current 3D rendering research.
- By employing point transformers for aggregating Gaussian splats, the method offers a sound and efficient approach to achieve improved detail and visual fidelity.

### Weaknesses
 - The paper does not explore the potential of utilizing generative priors for OOD-NVS, particularly by introducing diffusion models to assist in hallucinating unseen views, which could enhance performance in novel view synthesis in a more reasonable way.
- The study is primarily focused on object-centric cases, despite the availability of scene-level 3D datasets (scannet, scannet++, blendedmvs, megascene, megadepth, mvsimgnet). Expanding the scope to scene-wise data could provide a broader basis for extrapolation and robustness in more complex environments.
- For object-centric cases, single-image-to-3D methods may suffice for preserving geometric consistency and hallucinating texture details. It is unclear why some introduced baselines, including generalizable GS and sparse-view GS, underperform in these scenarios relative to expectations.

### Questions
Please refer to the questions in the weaknesses section concerning the problem-solving approach and dataset scope. The reviewer strongly suggests that the authors include a video comparison, as novel view synthesis is highly dependent on visual assessment.



--------------------
Thank you for the detailed explanation and for addressing my concerns. After reviewing the comments from other reviewers and considering your explanation regarding the broader scope of your work, I agree that the merit of addressing OOD challenges in neural rendering using a large-scale model is valuable.

I appreciate the clarification and the balance you’ve struck in presenting the scope of your contributions, the promised clarification in the future abstract and introduction. As a result, I will raise my score to support the acceptance of your submission.

### Soundness
2

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
3

### Summary
Although existing 3D representations such as 3DGS or Nerf can achieve novel view synthesis, their rendering performances on OOD views with relatively large elevations are relatively limited. This may come from the large differences between training and evaluation OOD views. In this work, the authors propose a framework, named SplatFormer, using transformer to refine the optimized 3DGS for better performances under OOD views. Benefited from the training under both normal and OOD views, SplatFormer can indeed improve the rendering under OOD views.

### Strengths
1. The core contribution of this work to refine 3D Gaussians with a genelizable transformer is meaningful;
2. The authors construct training and evaluation sets for the claimed OOD problem, from ShapeNet and Objaverse dataset.
3. Extensive experiments with different baselines on multiple datasets confirm that the proposed method can obviously improve the rendering performances under poses with large elevations.

### Weaknesses
My major concerns lie on that some comparisons between the proposed method and baselines  may be not so fair. For example, the optimization of the proposed method use 32 low-elevation views, while the results of some methods, e.g., LaRa, take only 4 views for input. The lack of training views may naturally affect its performances. Can we apply the proposed framework to the 3D Gaussian primitives generated by LaRa directly? In this way, the performances of proposed refinement might be evaluated more fairly.

Except the mentioned problem in the weakness section, I have some other problems.
 1. As the method is mainly proposed to address the problems of rendering under relatively large elevations, the limitation of performances may come from the lack of corresponding training views. Could we just use some novel view synthesis baselines, such as Zero123, SV3D to generate pseudo images from such poses with large elevations, and then optimize 2DGS, 3DGS, etc. for reconstruction? Would this also improve the performances under poses with large elevations?
 2. What is the specific settings for the training of the Gaussian primitive transformer? Would it select input views and OOD views randomly? Does different selection strategies have influences on the final performances?
 3. How is the efficiency of the transformer? As the density of Gaussian primitives might be quite high after optimization, wouldn't it take great time and memory cost to incorporate such a transformer framework?

### Questions
Except the mentioned problem in the weakness section, I have some other problems.
 1. As the method is mainly proposed to address the problems of rendering under relatively large elevations, the limitation of performances may come from the lack of corresponding training views. Could we just use some novel view synthesis baselines, such as Zero123, SV3D to generate pseudo images from such poses with large elevations, and then optimize 2DGS, 3DGS, etc. for reconstruction? Would this also improve the performances under poses with large elevations?
 2. What is the specific settings for the training of the Gaussian primitive transformer? Would it select input views and OOD views randomly? Does different selection strategies have influences on the final performances?
 3. How is the efficiency of the transformer? As the density of Gaussian primitives might be quite high after optimization, wouldn't it take great time and memory cost to incorporate such a transformer framework?

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
4

### Summary
This paper presents SplatFormer, a novel zero-shot model for 3DGS refinement trained on large datasets, in order to enhance the synthesized appearance robustness observed from OOD views. The presented problem OOD-NVS it aims to solve is valuable. Extensive experiments show it achieves SOTA performance on various object-centric datasets.

### Strengths
- The presented new problem OOD-NVS is of great value.
- Experiments are extensive, which can well validate the performance of the proposed method.
-  SplatFormer achieves SOTA performance on various object-centric datasets in OOD-NVS task compared to current related methods.

### Weaknesses
 - Although some experiments using real-world datasets are conducted, all involved datasets are still mainly object-centric. It is still a problem that if this learning-based method can be applied to real-world and non-object-centric scenes with more complex foreground and background. The corresponding data are much more difficult to collect than the object-centric data, and also more difficult to process and use in training.
- Lack of reporting geometry results. Although there are many comparisons in appearance, it's another important problem that how much can the refinement benefit the reconstructed geometry. However, there are no results like depth and surface normal are shown.

### Questions
- Would like to see some discussion and exploration for non-object-centric scenes.
- Would like to see more comparisons on geometry, like surface normal and depth.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a method towards enhancing the 3DGS performance on out-of-distribution views. This paper leverages a transformer-based point cloud backbone to encode and refine per-scene optimized 3DGS, and supervise on both interpolated views and out-of-distribution views. The empirical results show that this method leads to signficantly improved quality on OOD views.

### Strengths
1. The task of enhancing OOD views quality is important and with good motivation. 
2. The idea of training a point cloud backbone to learn priors of OOD views for 3DGS refinement is novel and promising.
3. The experiments are extensive and the results are attractive.
4. The paper is well-written.

### Weaknesses
I did not find obvious weaknesses of this paper.

### Questions
1. It seems that this method is focused on object-centric scenes with specific camera trajectories (mainly difference in elevations). In both the training datasets and the testing datasets, the input views and OOD views are captured similarly. I'm curious about the results when the trainig views and OOD views are not captured similarly to the training data? For example, if the training views are high-elevation and testing views are low-elevation, or if the training and testing views are with similar elevation but are distant.

### Soundness
3

### Presentation
3

### Contribution
3
