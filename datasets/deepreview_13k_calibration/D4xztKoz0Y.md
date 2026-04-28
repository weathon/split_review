# Learning Shape-Independent Transformation via Spherical Representations for Category-Level Object Pose Estimation

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Category-level object pose estimation aims to determine the pose and size of novel objects in specific categories. Existing correspondence-based approaches typically adopt point-based representations to establish the correspondences between primitive observed points and normalized object coordinates. However, due to the inherent shape-dependence of canonical coordinates, these methods suffer from semantic incoherence across diverse object shapes. To resolve this issue, we innovatively leverage the sphere as a shared proxy shape of objects to learn shape-independent transformation via spherical representations. Based on this insight, we introduce a novel architecture called SpherePose, which yields precise correspondence prediction through three core designs. Firstly, We endow the point-wise feature extraction with $\mathrm{SO(3)$-invariance, which facilitates robust mapping between camera coordinate space and object coordinate space regardless of rotation transformation. Secondly, the spherical attention mechanism is designed to propagate and integrate features among spherical anchors from a comprehensive perspective, thus mitigating the interference of noise and incomplete point cloud. Lastly, a hyperbolic correspondence loss function is designed to distinguish subtle distinctions, which can promote the precision of correspondence prediction. Experimental results on CAMERA25, REAL275 and HouseCat6D benchmarks demonstrate the superior performance of our method, verifying the effectiveness of spherical representations and architectural innovations.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper addresses the challenge of object pose estimation in 3D space, specifically overcoming the limitations of existing methods that rely heavily on 3D model shapes. It proposes an approach called SpherePose, which utilizes spherical representations to create shape-independent transformations, thereby improving correspondence prediction accuracy. The method incorporates three core innovations: SO(3)-invariant feature extraction, spherical feature interaction using attention mechanisms, and a hyperbolic correspondence loss function for precise supervision. This paper mainly introduces a new proxy shape for objects and a robust architecture for category-level pose estimation. Empirical validation shows superior performance against state-of-the-art methods.

### Strengths
- This paper uses a sphere as a proxy to implement category-level object pose estimation. It transforms the 3D shape to a uniform sphere via HEALPix spherical representations, which leads the network to focus on the semantic consistency between different objects instead of shape deviation.
- The architecture for category-level object pose estimation that achieves precise different objects in one category correspondence prediction.
- The experiments show that the proposed methods achieve the SOTA results on 6D pose estimation tasks in several datasets.

### Weaknesses
 - The point cloud patches are occluded. The center of a point cloud patch may not be the corresponding object's center. The projection results changed a lot when the center moved. Besides, different object point cloud patches have various occlusions. The correspondence by the spherical proxy, whether a real semantic correspondence of objects, could have more evidence or qualitative results.
- The positional encoding of the anchors needs more explanation. The way to describe the anchor position is vague, spherical coordinates or something else. The position of an anchor could influence the rotation invariance, making the results sensitive to rotation.

### Questions
- Given that the method relies on SO(3)-invariant feature extraction and RGB-based features, how robust is the approach to diverse lighting conditions and texture variations across different objects?
- Can the spherical feature interaction using attention mechanisms generalize well to objects with high self-occlusion or cluttered environments, and how is this tested?
- The hyperbolic correspondence loss function is designed to improve gradient behavior near zero. How does this compare quantitatively with traditional loss functions in terms of convergence speed and accuracy?

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
This paper addresses the challenge of category-level object pose estimation by proposing a shape-independent representation using spherical features. Starting with an RGB-D image and instance masks, the method processes "N" partial point clouds to estimate object pose parameters: rotation R \in SO(3), translation t \in R^3, and size s \in R^3 of the observed instance. The spherical feature construction on the SO(3) HEALPix grid, combined with a hyperbolic correspondence loss, significantly improves pose estimation performance. The paper categorizes pose estimation into correspondence-based vs. regression-based and point-based vs. spherical-based approaches. The proposed method, correspondence-based/spherical-based SpherePose, demonstrates state-of-the-art results on REAL275 and HouseCat6D benchmarks.

### Strengths
1. Strong motivation: The proposed shape-independent proxy representation addresses a crucial need in category-level pose estimation, enhancing generalizability across different object instances.

2. Good analysis of correspondence errors: The method effectively identifies correspondences, as shown in Table 3, where accurate correspondence significantly enhances pose estimation accuracy. 
However, consistency of correspondence errors should be validated on another dataset, such as HouseCat6D.

3. Comprehensive Ablation Studies: 	The authors provide a detailed analysis of different feature extractors (DINOv2, ColorPointNet++) and loss functions (L2 vs. hyperbolic L2). While not the primary contribution, Table 4 highlights the role of backbone networks in performance improvement. Table 6 effectively isolates the impact of the hyperbolic L2 loss, validating its importance. 
However, the authors should clearly differentiate the contribution of the backbone networks from the main innovations of the paper (spherical-based proxy and correspondence-based loss), by comparing with existing methods under the same configurations.

### Weaknesses
1. Justification for Spherical Proxy: 
Why is the 2-sphere an optimal proxy shape for this task? While the paper adopts the spherical representation, a more thorough explanation of the choice of spherical shapes would be helpful. The justification for using a spherical proxy in this paper is not sufficiently established solely based on its usage in other works.

2. Size Estimation Despite Normalization:
Section 3.1 mentions that the point cloud utilizes normalized coordinates, yet the method predicts the size parameter “s”.  How is accurate size estimation achieved despite normalization? Clarification on this aspect is necessary. The reliance on off-the-shelf models for estimating S increases the overall model complexity.

3. Focus on SO(3) Over SE(3):
The method predicts rotation “R” and translation “t”, focusing on SO(3) invariance. Why is roto-translation-invariance (SE(3)) not considered? (and scale-invariance) This oversight could limit the method’s robustness in varying spatial contexts.

4. SO(3)-Invariant Features and Rotation Discrimination:
In Section 3.1, if point-wise features are SO(3)-invariant, how does the method differentiate between different rotations? Wouldn't rotation-“invariant” features cause the model to lose rotational information? An explanation on how SO(3)-equivariant features are maintained would be insightful.

5. Shape-Independence and HEALPix Projection:
In section 3.1. HEALPix Spherical projection, does that anchor-based projection guarantee to preserve shape-independence? Even if the spherical projection is already proposed in VI-Net (Lin et al., 2023), ensuring its effectiveness in preserving shape-independence is critical in this framework. When projecting onto the HEALPix-based spherical proxy, there is no clear guarantee that objects of the same category will be consistently projected.

6. Correspondence-Based Loss in Linear Space:
In lines 357-358, the paper claims that learning correspondence-based loss is easier in linear space. Why is this the easier case? Would direct regression provide a better supervisory signal? Providing supporting evidence would strengthen this claim.

7. HEALPix vs. Other Grids:
It is convinced that the choice of the HEALPix grid over random rectangular SO(3) grids is explained by the drawbacks of equirectangular grids near the poles. 
However, could a random SO(3) grid serve as a viable alternative? 
Additionally, in Table 7, evaluating other SO(3) spherical grids, such as SuperFibonacci spirals [A], would provide a comprehensive comparison, given its fast construction properties.

[A] Super-Fibonacci Spirals: Fast, Low-Discrepancy Sampling of SO(3) (Marc Alexa, CVPR 2022)

8. Clarification of this paper’s contribution: Please organize Sections 3 and 4 to focus on the main contribution of this paper.

### Questions
1. Rotational Invariance/Equivariance in HEALPix Projection:
How does the HEALPix spherical projection in Section 3.1 maintain rotational invariance or equivariance between input and output?

2. Related Work and Citations: There are two concurrent works leveraging spherical grids for pose estimation—correspondence-based [B] and regression-based [C]. Please cite and discuss these works to position your method within the broader context.

[B] Improving Semantic Correspondence with Viewpoint-Guided Spherical Maps (Mariotti et al., CVPR 2024 ): https://arxiv.org/abs/2312.13216

[C] 3D Equivariant Pose Regression via Direct Wigner-D Harmonics Prediction (Lee et al., NeurIPS 2024 ): https://arxiv.org/abs/2411.00543

### Soundness
3

### Presentation
2

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
This paper addresses the task of category-level object pose and size estimation, introducing a novel method called SpherePose. This method uses a sphere as a shared proxy shape for objects, enabling the learning of shape-independent transformations from spherical representations. To enhance the precision of correspondences on the sphere, SpherePose incorporates three core components, including  SO(3)-invariant point-wise feature extraction, spherical feature interaction, and a hyperbolic correspondence loss function. Experiments conducted on the CAMERA25, REAL275, and HouseCat6D datasets validate the effectiveness of SpherePose.

### Strengths
- Unlike point-based representations, SpherePose uses a sphere as a shared proxy shape for objects and employs spherical representations to learn shape-independent transformations.

- Three core components are introduced based on spherical representations to enhance the precision of correspondences.

- SpherePose achieves state-of-the-art results on the CAMERA25, REAL275, and HouseCat6D datasets.

### Weaknesses
 - Are the spherical NOCS coordinates derived by normalizing the original NOCS coordinates to unit vectors? If so, it would be beneficial to provide results for regressing the original NOCS coordinates. It is unclear how the normalization impacts the final pose estimation accuracy and whether directly regressing the original NOCS coordinates would lead to better performance.

- Are the resulting poses obtained from the observed anchors or all sampled anchors on the sphere? If it’s the former, how can we verify that the spherical feature interaction aids in reasoning about the features of occluded anchors? The paper should clarify whether the feature interaction is robust enough to handle occluded regions and how this is validated. A more detailed analysis of the contribution of the spherical feature interaction, especially in occluded scenarios, is needed.

- Unlike most existing methods that use the Umeyama algorithm, SpherePose incorporates RANSAC for solving rotations. For a fair comparison, results without RANSAC for SpherePose should be included in Table 1. It is important to isolate the impact of RANSAC to ensure that the performance gains are not solely due to this outlier rejection technique. The paper should provide a more detailed ablation study on the effect of RANSAC.

- It is recommended to include results that do not use RGB or radius values as inputs in Table 4. This would help to understand the contribution of each input modality and the robustness of the method to different input data. The paper should provide a more comprehensive analysis of the impact of different input modalities on the final performance.

### Questions
See Weaknesses.

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
4

### Summary
This paper introduces a new method for category-level object pose estimation. The authors argue that the shape-dependent representations in previous approaches lead to semantic inconsistencies across different objects within the same category. To handle this issue,  a shape-independent transformation is presented, transforming features to a sphere. The authors also introduce the importance of SO(3)-invariant features for category-level object pose estimation. Multiple SO(3)-invariant features extracted from RGB images and point clouds are combined to learn the NOCS coordinates on a sphere. Experimental results show SpherePose outperforms state-of-the-art methods on benchmarks like CAMERA25, REAL275, and HouseCat6D, showing its effectiveness in handling category-level pose estimation challenges.

### Strengths
The idea of leveraging an object-agnostic representation to handle the problem of semantic inconsistencies is technically sound and interesting. The authors propose to combine multiple deep feature extractors, and its effectiveness is demonstrated in the ablation studies. The paper conducts extensive experiments on multiple benchmarks, showing better performance compared with existing methods. The paper is well-written and easy to understand.

### Weaknesses
- The presented ColorPointNet++ architecture, while functional, does not represent a significant advancement in the field. The reliance on a modified PointNet++ architecture raises concerns about the novelty of this component. Several alternative approaches for extracting SO(3)-invariant features exist in the literature, such as those proposed in [1,2,3], which could potentially offer superior performance or efficiency.

- The claim that DINOv2 features are "approximately" SO(3)-invariant is not sufficiently substantiated. While the authors suggest an intuitive understanding of this property, a more rigorous analysis is needed. Specifically, providing quantitative or qualitative experimental results demonstrating the degree of invariance to various 3D rotations would significantly strengthen this claim.

- The paper lacks a clear and concise comparison with previous methods that also utilize spherical representations for pose estimation. While the authors state that their method, SpherePose, outperforms others, they do not explicitly define the key differences in methodology or the specific advantages that lead to this improved performance. A more detailed discussion highlighting the unique aspects of SpherePose in the context of existing spherical representation-based methods is necessary.

- The paper omits crucial ablation studies that would provide deeper insights into the proposed method's effectiveness. For instance, the spherical feature interaction module is introduced to address self-occlusion challenges. However, without an ablation study directly evaluating this module's impact, its contribution remains unclear. Furthermore, a dedicated experiment explicitly demonstrating the importance of SO(3)-invariant features for category-level object pose estimation is missing. This could involve comparing the performance with and without the use of such features, providing empirical evidence for their necessity.

### Questions
-	I am a bit confused about the SO(3)-invariant features in the field of object rotation estimation. We could formulate the rotation estimation problem as R = f(g(x)|w). g(x) means the feature extractor. If the extracted features are rotation-invariant, it would be g(R(x))=g(x). If this is the case, it means f(.) would be unaware of the rotation information. Why is the network able to make the prediction related to rotations? To me, SO(3)-equivariant features seem more reasonable. 
-	The proposed spherical representation is designed to be object-agnostic across different categories. What factors limit the method’s ability to generalize to objects from novel categories?
-	Why is the IoU75 worse than that of a point-based method AG-Pose on REAL275?

### Soundness
3

### Presentation
3

### Contribution
3
