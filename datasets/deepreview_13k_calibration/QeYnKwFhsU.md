# Point Cloud Dataset Distillation

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
This study introduces dataset distillation (DD) tailored for 3D data, particularly point clouds. DD aims to substitute large-scale real datasets with a small set of synthetic samples while preserving model performance. Existing methods mainly focus on structured data such as images. However, adapting DD for unstructured point clouds poses challenges due to their diverse orientations and resolutions in 3D space. To address these challenges, we theoretically demonstrate the importance of matching rotation-invariant features between real and synthetic data for 3D distillation. We further propose a plug-and-play point cloud rotator to align the point cloud to a canonical orientation, facilitating the learning of rotation-invariant features by all point cloud models. Furthermore, instead of optimizing fixed-size synthetic data directly, we devise a point-wise generator to produce point clouds at various resolutions based on the sampled noise amount. Compared to conventional DD methods, the proposed approach, termed DD3D, enables efficient training on low-resolution point clouds while generating high-resolution data for evaluation, thereby significantly reducing memory requirements and enhancing model scalability. Extensive experiments validate the effectiveness of DD3D in shape classification and part segmentation tasks across diverse scenarios, such as cross-architecture and cross-resolution settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
In point cloud dataset distillation, this paper addresses the challenge of diverse orientations and resolutions of point clounds.
Specifically, this paper proposes the first 3D distillation framework , which can be trained with low-resolution point clouds and generates high-resolution data for evaluation.
It also validate the effectiveness of matching the rotation-invariant features in preserving the principal components of real data.

### Strengths
1. This paper is the first to propose dataset distillation framework in point cloud data.
2. The paper is well written and fully describes the research area and proposed methods.

### Weaknesses
1. The proposed method requires different distillation algorithms for different tasks, so it may be troublesome to use in practice.
2. The table 2，the improvement is limited compared with coreset-based methods,  and far behind the full dataset. I have concerns about the practicality of the proposed method.
3. The figure 7 and figure 9 demonstrate that the synthetic point clouds have poor quality.

### Questions
It seem that there is another method  (https://github.com/kghandour/dd3d/blob/main/assets/Report.pdf) in dataset distillation of point clouds using GM,
Why is there no mention of this method?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces DD3D, a method for condensing large 3D point cloud datasets into smaller, efficient sets while maintaining performance. Unlike older methods made for images, DD3D addresses 3D-specific challenges like different orientations and resolutions. It uses a point cloud rotator to align data consistently and a point-wise generator to create flexible, high-resolution synthetic point clouds. Experiments show DD3D is effective, scalable, and memory-efficient, making it suitable for tasks like shape classification and part segmentation.

### Strengths
1） The paper backs its approach with solid mathematical explanations, showing why the proposed techniques work.
2）The authors test DD3D thoroughly across different datasets and scenarios, showing that it consistently outperforms traditional methods.

### Weaknesses
1.  The authors only verify the effectiveness of classification tasks on very small datasets.
Therefore, my biggest concern is the generalization of the proposed method for detection tasks on large dataset(nuscenes or waymo).
2.  Why adopt data distillation? Data distillation will cause some information loss compared with raw data.
3.  While the paper compares DD3D to several distillation methods, it could strengthen its claims by including more comparisons with state-of-the-art rotation-invariant models.
4.  Although the paper mentions some drawbacks, such as convergence challenges when not initialized with real data, a deeper exploration of these limitations and potential mitigation strategies would add more balance to the work.

### Questions
See the weaknesses.

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
3

### Summary
This paper introduces DD3D, the first dataset distillation framework specifically designed for 3D point cloud data. The method addresses two fundamental challenges in point cloud distillation: handling different orientations and varying resolutions. The authors make several key contributions. The authors develop a theoretical foundation that demonstrates the importance of matching rotation-invariant features for 3D distillation. And this paper introduces a plug-and-play point cloud rotator that resolves both rotation and sign ambiguity issues. The framework includes a novel rotator to align point clouds to a canonical orientation and employs a point-wise generator to produce point clouds at arbitrary resolutions, significantly advancing the field of dataset distillation for 3D data.

### Strengths
1. The paper introduces the dataset distillation framework specifically designed for point cloud data, filling a gap in the field where previous DD methods were primarily focused on structured data like images, videos, and text. This work opens up possibilities for efficient point cloud model training.

2. The authors provide a theoretical analysis demonstrating why matching rotation-invariant features is crucial for 3D point cloud distillation. They formally prove that random rotations weaken the principal components of real data, leading to degraded distillation performance, which strongly motivates the rotator of their approach.

3. The method consistently demonstrates superior performance over traditional dataset distillation methods across multiple benchmarks, validating its effectiveness and practical utility.

### Weaknesses
1. The method shows limited performance on fine-grained tasks such as part segmentation compared to shape classification, indicating a potential limitation in capturing detailed geometric features.

2. The computational overhead introduced by the generation process is higher compared to traditional DD methods, which could be a significant limitation for complicated and large-scaled datasets.

3. The significant performance drop compared to using the full dataset, while expected in dataset distillation, still represents a considerable limitation for applications requiring high accuracy. While the paper demonstrates notable improvements over existing dataset distillation methods, there are significant concerns about potential performance degradation when scaling to larger, more complex datasets or more sophisticated tasks.

### Questions
1. How does the choice of the noise distribution in the point-wise generator affect the quality of generated point clouds? Have you experimented with different distributions (i.e., Gaussian) beyond uniform?

2. The paper shows that training with low-resolution point clouds can achieve similar performance to high-resolution ones. Could you elaborate on the theoretical reasons behind this result?

3. While the point-wise generator offers resolution flexibility, I have concerns about its inherent limitations in generating complex geometric shapes. How does the performance of the generator architecture affect the observed performance gap in more detailed tasks?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a dataset distillation method for 3D point clouds. The paper begins by showing that an ideal dataset distillation process should preserve the variance of the underlying dataset and that orientation-misaligned samples introduce undesirable variance perturbations. Based on this observation, the paper uses a rotator to align the point clouds to canonical orientations. Experiments on shape classification and segmentation tasks demonstrate that the proposed DD3D outperforms existing baseline approaches.

Caveat: I am not familiar with dataset distillation. Please interpret my reviews with caution.

### Strengths
1. The rotator addresses the sign ambiguity problem associated with PCA. The key idea is to wrap the projected point clouds using a series of sine functions.
2. In addition to the rotation invariancy, DD3D is robust to point cloud resolutions. This is achieved with a point generator that decodes 3D coordinates following a pointwise paradigm. The number of output points is the same as the dimension of the input noise.
3. Ablation studies, particularly Table 5, demonstrate the effectiveness of the proposed design.

### Weaknesses
1. While Section 5.6 provides some representative visualizations of the DDD3D-generated synthetic point clouds, it is unclear how they compare with the baseline-generated ones. As such, it is unclear how the visualization should be interpreted. I recommend the authors include side-by-side comparisons of point clouds generated by DD3D and baseline methods. This would allow readers to visually assess the differences and better interpret the visualizations.

2. The proposed method appears to be limited to shape-level tasks. It is not straightforward to apply DD3D to large-scale scene-level tasks. In particular, there may not be a well-defined canonical frame for the diverse scene-level point clouds.

### Questions
- Theorems 1 and 2 are built upon several assumptions. Does the actual experiment follow all the assumptions? I understand that the most important assumption is that $f_\theta$ must be rotation-equivalent. The fundamental design of this paper relies on addressing the fact that existing models are not rotation-equivalent. What about the other assumptions? For example, the classifier is assumed to be linear and the classification loss is assumed to be MSE. I do not believe the actual experiment follows these assumptions. It would be great if the authors could provide some clarification on whether the theoretical results can be easily transferred. Rigorous proofs are not necessary but some insightful analysis will be great.

- To follow up on the previous point, perhaps a toy example can be beneficial to illustrate the concept. Consider generating a small collection of 3D shapes and comparing the performance of a shape classification model trained with aligned and misaligned orientations. Can we gain any insights from this toy example?

- Nit: On line 122, $V$ is likely a vector of integers instead of generic real numbers.

### Soundness
3

### Presentation
3

### Contribution
2
