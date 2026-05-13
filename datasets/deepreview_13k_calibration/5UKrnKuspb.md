# NeuralPlane: Structured 3D Reconstruction in Planar Primitives with Neural Fields

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 6, 10, 8

## Abstract
3D maps assembled from planar primitives are compact and expressive in representing man-made environments, making them suitable for a spectrum of applications. In this paper, we present **NeuralPlane**, a novel approach that explores **neural** fields for multi-view 3D **plane** reconstruction. Our method is centered upon the core idea of distilling geometric and semantic cues from inconsistent 2D plane observations into a unified 3D neural representation, which unlocks the full leverage of plane attributes. This idea is accomplished by NeuralPlane via several key designs, including: 1) a monocular module that generates geometrically smooth and semantically meaningful segments as 2D plane observations, 2) a plane-guided training procedure that implicitly learns accurate plane locations from multi-view plane observations, and 3) a self-supervised feature field termed *Neural Coplanarity Field* that enables the modeling of scene semantics alongside the geometry. Without relying on plane annotations, our method achieves high-fidelity reconstruction comprising planar primitives that are not only crisp but also well-aligned with the semantic content. Comprehensive experiments on ScanNetv2 and ScanNet++ demonstrate the superiority of our results in both geometry and semantics.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents a neural 3D reconstruction system on 3D plane reconstruction of indoor scenes. Inspired by the recent success of neural radiance field and image foundation models (SAM2), this paper presents a multi-view 3D reconstruction pipeline leveraging these techniques. The training scheme consists of three phases: Initializing plane segments and parameters -> optimizing a neural feature field for plane-specific feature representation (encouraged by a list of geometry-guided loses) -> plane extraction by grouped features and RANSAC. Experiments are conducted extensively on two representative indoor datasets: ScanNet and 7-scenes and are compared with a group of competitve baseline methods.

### Strengths
1. The unique advantage of the system is the association of geometry and semantic features for plane reconstruction problem, which requires both geometry-aware perception and semantic-aware grouping.
2. The paper leverages foundation models to achieve plane segment initializaing and utilize geometry-driven losses to optimize the system. There is no groundtruth plane segmentation or geometry label required. 
3. Overall the paper and diagrams are well written and presented.
4. The experimental comparison and thorough and convincing on both plane geometry reconstruction and segmentation.

### Weaknesses
1. I think the major advantage of this paper is the unsupervised learning paradigm on the plane reconstruction problem. However, since both ScanNet and ScanNet++ has groundtruth images, this unique advantages seems not to be fully enjoyed and reflected. So I suggest authors to apply the proposed system on some outdoor scenes containing plane structures (such as autonomous driving dataset or street view datasets), to verify the adaptability of the method. Specifically, the method should be tested on datasets with varying scales and complexities of planar structures, such as those found in urban environments, to truly assess its generalizability beyond controlled indoor settings. The current evaluation, while thorough on indoor datasets, does not fully leverage the potential of the unsupervised approach.

2. I have tested PlaneRecon in my previous projects. It can incrementally reconstructs planes in an online and real-time manner. Besides, it can trains over multiple scenes and directly test without any test-time optimization. Although its precision should fall behind than the neural reconstruction papers, the generalizability and speed is higher than the proposed method. I am curious on whether the paper has such potential to tackle these limitations. The paper should discuss the computational cost of the optimization process, especially in comparison to methods like PlaneRecon, which offer real-time performance. A detailed analysis of the time complexity and memory requirements would be beneficial, along with potential strategies for improving efficiency, such as parallelization or model compression techniques.

3. Missing a few related works: (1) Recovering 3d planes from a single image via convolutional neural networks (2) PlaneMVS: 3D Plane Reconstruction From Multi-View Stereo (3) Single-image piece-wise planar 3d reconstruction via associative embedding.

4. On quantitative evaluation, it is unclear that what is the groundtruth is here. Does it stand for the groundtruth planar part only or the entire mesh? As a plane reconstruction paper, I think the former one should be more reasonable. If so, the first several methods listed in Table 1 cannot directly be compared with the proposed method. Authors should make it clearer on this part. The evaluation section needs to clearly define what constitutes the ground truth for plane reconstruction. If the ground truth is indeed only the planar parts, the comparison with methods that reconstruct the entire mesh is misleading and should be presented with appropriate context. A separate evaluation focusing solely on planar regions would provide a more accurate assessment of the proposed method's performance.

5. Is the proposed method robust to the hyperparameters listed in the paper especially (1) to,tn and m in the push loss during training and (2) the parameters selected in RANSAC during plane fitting? Some ablation studies on hyper-parameter robustness are expected to make the method more generalizable across most indoor scenes, since the geometric scale and semantic distribution can have large variance among scenes. The paper lacks a thorough analysis of the sensitivity of the method to its hyperparameters. Specifically, the impact of the push loss parameters (to, tn, and m) and RANSAC parameters on the final reconstruction quality should be investigated. Ablation studies varying these parameters would demonstrate the robustness and generalizability of the method across different indoor scenes with varying geometric scales and semantic distributions.

### Questions
I am impressed by the technical contribution made by authors for this work. However, there also exist a few major concerns for me at this time which discourage me to grant this paper a higher value. 

Please try to address my concerns listed in the weakness part. I will accordingly consider to improve my overall rating if the concerns are well solved.

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
3

### Summary
This paper presents NeuralPlane, a method for reconstructing 3D scene plane primitives via neural fields without GT plane labelling. The method is divided into three main stages: firstly, it combines pre-trained normal prediction and SAM to generate initial 2D planar segments and estimates their 3D parameters using SfM keypoints. Secondly, it optimises two neural fields, a density field based on planar geometric constraints, and a coplanar neural field that understands the semantic relationships between regions . The neural coplanar field is followed by a neural parser module that helps to model the learned coplanar relations. Finally, the optimised neural representations are converted into explicit 3D planes through point sampling, feature-based clustering and RANSAC fitting. The method is evaluated on the ScanNetv2 and ScanNet++ datasets, and the results show that it outperforms both the learning-based method and the Geometry+RANSAC method in terms of geometric and semantic metrics.

### Strengths
- This paper is well-written and easy to understand.
- The proposed method does not require ground-truth plane annotations, as it can learn effectively from noisy monocular model outputs.
- The method demonstrates SOTA performance and achieves clean plane segmentation results.

### Weaknesses
 - The proposed method involves numerous hyperparameters, including balancing parameters for loss, the number of semantic prototypes, and parameters listed in Lines 850-863.
- As a complex system, it is important to discuss and present failure cases to help readers understand the method’s limitations.
- The evaluation is limited to a small number of scenes (only 12), which raises concerns about the generalizability of the results. The method's performance on more diverse and challenging datasets needs to be assessed.

### Questions
Since it is a complex system paper, making it hard to reproduce, will the code be publicly avaliable?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The paper presents NeuralPlane, a novel approach to 3D plane reconstruction that utilizes neural fields for generating structured 3D maps from multi-view images without the need for plane annotations. The method emphasizes two main aspects: geometry and semantics. Key contributions include:
1. Monocular Plane Segmentation: A monocular module extracts geometrically smooth (based on off-the-shelves Surface Normal Predictor) and semantically meaningful 2D plane observations (based on Segmenet Anything Model). 
2. Plane-Guided Neural Representation: The model utilizes these 2D segments to train a neural field that captures accurate 3D plane locations. A surface normal regularization and pseudo-depth regularization terms are proposed.
3. Neural Coplanarity Field: This self-supervised feature field enables semantic consistency within the 3D reconstruction by grouping planar regions that share coplanar relationships. A contrastive loss is proposed to distinguish between planes with similar geometric properties but different semantic properties. 
The method demonstrates superior performance on ScanNetv2 and ScanNet++ datasets, indicating its effectiveness in indoor environments.

### Strengths
1. Novelty in Combining Geometry and Semantics: The method’s approach to merging geometry with semantic information through a neural coplanarity field is innovative, enhancing the semantic consistency of 3D reconstructions. A complex system with multiple stages is proposed to estimate/reason the local planar regions and the associated parameters, to associate the planes in 3D using radiance field, to resolve semantic conflicts using Neural Coplanarity Field.
2. High-Quality Reconstruction: Experimental results indicate that NeuralPlane achieves fine-grained and coherent plane reconstructions, outperforming existing methods in most of the metrics. 
3. Efficiency: NeuralPlane’s volume density representation allows for faster training compared to implicit methods, an important practical advantage.
4. Extensive ablation studies: the authors include sufficient ablation studies to support the effectiveness of the proposed modules.
5. Good writing: the paper is clearly written that the technical details are clearly presented.

### Weaknesses
1. Complexity of Methodology: The proposed method involves several stages, including monocular plane segmentation, neural coplanarity field training, and plane extraction. In each stage, there are several submodules and I believe there are some hyperparameters decisions in each stage. While effective, this complexity (especially the combination of submodules and associated parameters) may impact its scalability to larger scenes or generalizability. For example, K-means clustering on predicted normal map, mask size threshold in SAM, thresholds to form negative pairs in Neural Coplanarity Field, Loss balancing parameters, etc. It would be great if the authors could share the insights on the impact of these hyperparameter settings on different scenes. For example, is a universal set of hyperparameters applied to all the test scenes? It would be great if the authors could provide a sensitivity analysis or ablation study on key hyperparameters across different scenes. This would help clarify how robust the method is to parameter changes and whether a universal set of parameters is feasible.

2. Dependence on Initial 2D Plane Segmentation Quality: As the regularizations are based on the quality of initial local plane geoemtry, the method’s success can depend on the quality of 2D plane segments obtained from monocular priors, which may introduce inaccuracies in challenging environments for monocular predictors. As the authors mentioned , the local planar primitives can result in severe inconsistency across views (Line 194). Specifically, the reliance on a pre-trained surface normal predictor and SAM introduces a potential bottleneck, as these models may not generalize well to unseen environments or exhibit biases that propagate through the pipeline. The method does not explicitly address how to mitigate the impact of inaccurate normal predictions or over-segmentation from SAM, which could lead to suboptimal 3D plane reconstruction.

3. Over-Segmentation Issue: As highlighted in the paper, the Segment Anything Model (SAM) tends to over-segment planes, resulting in multiple smaller plane segments for a single surface. Although this is managed in the training process, it may require further refinement to avoid segmentation inconsistencies in complex scenes. From the visualization on the GitHub page, it seems to me that some of the small segments usually resulted in inaccuracy. The method does not provide a clear strategy for merging these over-segmented regions into coherent planes, which could lead to fragmented and less semantically meaningful reconstructions. This issue is particularly relevant in scenarios where large planar surfaces are common, such as walls and floors.

### Questions
1. Eqn 4: n_i is not defined, is it the surface normal of the selected local planar primitive? Please explicitly define n_i in the text or equation, and confirm if it refers to the surface normal of the local planar primitive.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposed a framework called NeuralPlane to reconstruct 3D indoor scenes as planar primitives from posed 2D images. The author first employs 2D prior models to generate local planar primitives, then uses the geometric and semantic priors to guide the NeRF-style reconstruction learning. Finally, a decoding algorithm is designed to extract the global explicit plane mesh from the learned neural field.
Extensive experiments are conducted to evaluate the performance on ScanNetv2 and ScanNet++ datasets.

### Strengths
This paper proposed a comprehensive 3D reconstruction framework with plane primitives. 

* Compared to some of the similar works that only focus on detecting the planes, this work also utilizes the detected planes to guide neural field learning.

* The presentation of this paper is clear and concise. 

* The qualitative and quantitative results look promising.

### Weaknesses
 * This work involves a lot of submodules, especially the neural field with geometric, semantic, and coplanar features could be computationally expensive. The combination of these features within the neural field, while potentially beneficial for reconstruction quality, introduces significant overhead in terms of both memory and processing time. The geometric features, semantic features, and coplanar features each require separate processing and storage, and their combined use within the neural field could lead to a substantial increase in computational cost, which is not thoroughly addressed in the paper.

* A concurrent work is very relevant to this paper and could be discussed in the related works section:
Chen, Zheng, et al. "PlanarNeRF: Online Learning of Planar Primitives with Neural Radiance Fields." arXiv preprint arXiv:2401.00871 (2023).

* The text illustration and conceptual figure of Neural Parser could be improved, current version is not clear enough and easy to follow. Specifically, the mechanism by which the Neural Parser identifies and groups coplanar segments is not clearly explained. The current description lacks sufficient detail on how the feature centroids are learned and how they contribute to the decomposition of the scene into planar primitives. A more detailed explanation of the mathematical formulation and the practical implementation of this module is needed.

### Questions
* What's the computation complexity of this work? Like the GPU memory usage and training time? How's it compared to related works?

### Soundness
3

### Presentation
3

### Contribution
3
