# SurFhead: Affine Rig Blending for Geometrically Accurate 2D Gaussian Surfel Head Avatars

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Recent advancements in head avatar rendering using Gaussian primitives have achieved significantly high-fidelity results. Although precise head geometry is crucial for applications like mesh reconstruction and relighting, current methods struggle to capture intricate geometric details and render unseen poses due to their reliance on similarity transformations, which cannot handle stretch and shear transforms essential for detailed deformations of geometry. To address this, we propose \ours, a novel method that reconstructs riggable head geometry from RGB videos using 2D Gaussian surfels, which offer well-defined geometric properties, such as precise depth from fixed ray intersections and normals derived from their surface orientation, making them advantageous over 3D counterparts. SurFhead ensures high-fidelity rendering of both normals and images, even in extreme poses, by leveraging classical mesh-based deformation transfer and affine transformation interpolation. SurFhead introduces precise geometric deformation and blends surfels through polar decomposition of transformations, including those affecting normals. Our key contribution lies in bridging classical graphics techniques, such as mesh-based deformation, with modern Gaussian primitives, achieving state-of-the-art geometry reconstruction and rendering quality. Unlike previous avatar rendering approaches, SurFhead enables efficient reconstruction driven by Gaussian primitives while preserving high-fidelity geometry.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a method for learning head avatars based on 2D Gaussian splatting. To make the Gaussian surfels better handle the stretch and shear deformation under extreme poses and facial expressions, this paper introduces affine transformation derived from Jacobian deformation gradient of the surface. Normal orientations are calculated accordingly. Moreover, the authors propose Jacobian blend skinning to interpolate these affine transformations to ensure surface smoothness. Results show that the proposed method is able to reconstruct drivable head avatars with high-quality geometry.

### Strengths
* This paper introduces better deformation modeling techniques for Gaussian surfels. Compared to existing works, the proposed method is more reasonable and can handle more extreme deformations such as stretching and shearing. The proposed technique could be useful in other related research topics beyond head avatar modeling. 

* The proposed method is able to reconstruct fine geometric details, outperforming existing baselines by a large margin. 

* The paper is overall well-written and easy to follow.

### Weaknesses
 * Missing comparison against Gaussian Head Avatar (GHA) [Xu et al. 2023], which is a state-of-the-art head avatar method in terms of image synthesis quality. Although the authors have already compared with SplattingAvatar and GaussianAvatar, I think an additional comparison against GHA is also necessary because GHA demonstrates high-resolution image synthesis with the assistance of a super-resolution module.

* It would be better if the authors report the training time and rendering speed. One important advantage of Gaussian splatting is its efficiency. I wonder whether the proposed techniques (such as Jacobian blend skinning) hinders this advantage or not.

* It is not clear how the proposed method performs for subjects wearing eye-glasses. NeRSemble dataset contains cases with eye-glasses, but they are suspiciously skipped in the experiments.

### Questions
See [Weaknesses].

### Soundness
3

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
4

### Summary
This paper aims at better geometry estimation in head modeling. It replaces the 3D Gaussian splatting with 2D Gaussian splatting to better model the surface. Moreover, it addresses three issues in existing works with three novel components: 1) To compensate for the incorrect deformation of 2D Gaussians due to the triangle's shear and stretch, it proposes the Jacobian deformation; 2) To mitigate the discontinuities in adjacent triangles, it improves linear blend skinning with Jacobian blend skinning; 3) To resolve hollow illusion in eyeballs, it replaces Spherical Harmonics with Anisotropic Spherical Gaussians. It demonstrates that it outperforms the state-of-the-art regarding normal similarity and remains comparable in rendering quality.

### Strengths
* It motivates each contribution properly.
* The use of Jacobian deformation and Jacobian blend skinning in the context of head modeling looks novel to me.
* The qualitative results and normal similarity evaluation demonstrate better geometry compared to baselines.
* The effectiveness of each component is well studied.

### Weaknesses
 * It is unclear how the deformation gradient $J$ in Sec 2.2 and the blended Jacobian $J_b$ in Sec 2.3 connect. In Line 258 to 261, it mentions that it replaces the original deformation in GaussianAvatar with a new deformation $J_b$, and $J$ appears only as a parameter of JBS in Eq. 2. What is the relationship between $J$ and $U_i, P_i$ in Eq. 2? Which transformation, $J$ or $J_b$, is used in the final method?  
* The paper measures the normal similarity between ground-truth normals and rendered normals from 2D Gaussians. However, since this work claims to achieve a better geometry, evaluating metrics that apply to meshes, such as Chamfer distance or normals rendered from the mesh is more informative when judging the geometry. Although previous methods use normals rendered from 2D Gaussians as proof of geometry, the link between it and the mesh quality still looks vague to me.
* As the rendering quality is only on par with state-of-the-art, e.g., GaussianAvatar, the comparison of training and rendering speed is missing.

### Questions
* It is unclear to me how Jacobian blend skinning improves upon linear blending skinning. It seems to me that $J_b$ introduces spatial smoothness to Gaussians' deformation matrices. Is the vertices of the mesh still transformed by linear blending skinning before the Jacobian blend skinning is applied? Also, could the author clarify Fig. 2(b)? What are the meanings of the green and yellow lines and the weights? How do they connect to the deformation of the triangle meshes?
* The paper mainly focuses on improving the geometry. Since 2D Gaussian splatting is known to produce better geometry than 3D Gaussians, how much does 2D Gaussians help improve the geometry, compared to the components proposed in the paper?

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
2

### Summary
This paper contributes a novel representation for geometrically accurate head avatars within the 3D Gaussian Splatting framework, a method for natural interpolation of affine transformations across adjacent deformations, and enhancements to the realism of corneal representations in head avatars. These contributions advance the state of the art in personalized head avatar construction and have the potential to improve various applications in computer graphics, virtual reality, and beyond.  The key contributions include:

* Introduction of SurFhead Model: The paper introduces SurFhead, the first geometrically accurate head avatar model within the Gaussian Splatting framework. This model is designed to capture the deformation of head geometry using intricate affine rigging that combines Gaussians and their normals solely from RGB videos.

* Jacobian Blend Skinning Algorithm: To address the issue of discontinuities between adjacent triangles in head deformations, the paper proposes the Jacobian Blend Skinning (JBS) algorithm. This algorithm blends adjacent transformations while avoiding geometric distortions by linearizing the non-linear matrix interpolation space, leveraging classical matrix animation techniques and geometrically smooth polar decomposition.

* Enhancement of Corneal Convexity and Specularity: The paper addresses the hollow illusion in the cornea by regularizing corneal convexity and enhancing specularity using computationally efficient Anisotropic Spherical Gaussians (ASGs). This improvement ensures a more realistic representation of the cornea in the head avatar.

### Strengths
The paper introduces SurFhead, a novel model within the Gaussian Splatting framework that captures geometrically accurate head deformations. This representation utilizes intricate affine rigging combined with Gaussians and their normals, solely based on RGB videos, which is a significant advancement in achieving realistic and detailed head avatars.  The proposed Jacobian Blend Skinning (JBS) Algorithm is technically sound.  The paper tackles the problem of the hollow illusion in the cornea, where a concave surface appears convex due to the prioritization of photometric losses during training. 

The methods presented in the paper are demonstrated to achieve superior results across a variety of subjects, including real and synthetic data. They excel in challenging scenarios such as sharp reflections on convex eyeballs, fine geometric details, and exaggerated deformations, showcasing the robustness and effectiveness of the proposed approach.

### Weaknesses
The method is built upon the foundation of 2D Gaussian Splatting, and I believe that the proposed method's success in recovering a superior surface geometry owes much to this solid groundwork. Indeed, the authors introduced several improvements on this basis, such as intricate affine rigging, but I consider these innovations to be more incremental improvements rather than groundbreaking advancements.

The geometric accuracy of the experimental results appears to exhibit significant variation: some achieve hair-level geometric detail, while others fail to recover the structure of the hair. Consequently, whether this variation stems from instability in the algorithm or differences in the data quality of various training datasets arises. I hope the author can provide more analysis and discussion on this issue.

### Questions
As elaborated in the "weaknesses", the geometric accuracy of the experimental results exhibits considerable variation,  and we hope that the authors can further enhance their analysis and discussion on this crucial point.

In terms of experimental design, the NeRSemble dataset, while containing accurate 3D mesh models, lacks sufficient detail, and obtaining such precise models can often be challenging in practical applications.     In this regard, we eagerly inquire whether the proposed method heavily relies on such relatively accurate 3D mesh models, and how it would perform in their absence.     To validate this, the authors could consider using videos they have shot or sourced from the internet as input, employing monocular facial 3D reconstruction algorithms (such as DECA) to obtain mesh sequences, or directly bypassing the use of 3D mesh models altogether.     We are anticipating and curious about the results of such experimental setups.    We encourage the authors to actively explore and propose potential strategies for adapting their proposed approach to scenarios where detailed 3D mesh models are unavailable.

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
The paper proposes a method that handles stretch and shear transforms essential for detailed deformations of geometry utilizing intricate deformations driven by the affine Jacobian gradient instead of similarity transformation and corresponding normal adjustments.

### Strengths
1) Jacobian Blend Skinning (JBS): The use of Jacobian Blend Skinning (JBS) enables natural interpolation of affine transformations across adjacent deformations, effectively reducing discontinuities in transitions.

2) Cornea Opacity Constraint: To address the specular highlights in the eyeball region, the method constrains the corneal regions to remain opaque by regularizing the opacity of the respective Gaussians.

### Weaknesses
1) Detail Representation: In Figure 5 (bottom row), there seems to be a lack of finer details, such as wrinkles and skin pores. The method's ability to capture high-frequency geometric details appears limited, particularly when compared to methods that explicitly model surface normals and high-resolution displacement maps. The absence of these details makes the reconstructed geometry appear overly smooth, which is a noticeable limitation for high-fidelity head avatars. Adding more visual comparisons, especially with close-up views of these high-frequency features, would be beneficial to understand the limitations of the proposed method.

2) Rendering Speed and FPS: While the paper mentions the use of Gaussian splatting, it does not provide a clear comparison of rendering speed with other state-of-the-art methods. Given that methods like 3DGS/2DGS achieve real-time rendering, the speed of deformable-driven methods may be a limitation for applications requiring real-time animation. The lack of quantitative data on FPS, especially when compared to other methods, makes it difficult to assess the practical applicability of this method in time-sensitive scenarios. A detailed benchmark of rendering time and FPS would be necessary to clarify performance.

### Questions
1) Related Works: I think some related works of static reconstruction could be further discussed, such as H3DS [1], deformable model-driven approaches [2], and Implicit Neural Deformation methods [3]. These methods leverage 3D points from SfM, multi-scans, or multi-view data from various identities to enhance reconstruction under sparse-view conditions, although they primarily focus on static human face or head geometry reconstruction.

Ref:

[1] Ramon, Eduard, et al. "H3d-net: Few-shot high-fidelity 3d head reconstruction." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2021.

[2] Xu, Baixin, et al. "Deformable model-driven neural rendering for high-fidelity 3D reconstruction of human heads under low-view settings." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.

[3] Li, Moran, et al. "Implicit Neural Deformation for Sparse‐View Face Reconstruction." Computer Graphics Forum. Vol. 41. No. 7. 2022.

### Soundness
3

### Presentation
3

### Contribution
3
