# SC-OmniGS: Self-Calibrating Omnidirectional Gaussian Splatting

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
360-degree cameras streamline data collection for radiance field 3D reconstruction by capturing comprehensive scene data. However, traditional radiance field methods do not address the specific challenges inherent to 360-degree images. We present SC-OmniGS, a novel self-calibrating omnidirectional Gaussian splatting system for fast and accurate omnidirectional radiance field reconstruction using 360-degree images. Rather than converting 360-degree images to cube maps and performing perspective image calibration, we treat 360-degree images as a whole sphere and derive a mathematical framework that enables direct omnidirectional camera pose calibration accompanied by 3D Gaussians optimization. Furthermore, we introduce a differentiable omnidirectional camera model in order to rectify the distortion of real-world data for performance enhancement. Overall, the omnidirectional camera intrinsic model, extrinsic poses, and 3D Gaussians are jointly optimized by minimizing weighted spherical photometric loss. Extensive experiments have demonstrated that our proposed SC-OmniGS is able to recover a high-quality radiance field from noisy camera poses or even no pose prior in challenging scenarios characterized by wide baselines and non-object-centric configurations. The noticeable performance gain in the real-world dataset captured by consumer-grade omnidirectional cameras verifies the effectiveness of our general omnidirectional camera model in reducing the distortion of 360-degree images.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes an extension of 3D Gaussian splatting (GS) for omnidirectional images and enabling self-calibration. GS for omnidirectional images is previously studied (OmniGS), but it assumes the pre-computed camera positions. The proposed method refines the camera poses during gradient-based optimization. Experiments show that the proposed method improves the vanilla OmniGS. A main technical contribution of the paper is to derive the backward gradient for pose refinement of spherical images.

### Strengths
### Self calibration + omnidirectional images
The proposed method would be the first attempt to combine the self-calibration and omnidirectional GS.

### Backward gradient for spherical images
For pose refinement of spherical images, the paper derives the gradients in Eqs. (13--14). This would be a technical novelty in this paper.

### Weaknesses
### Limited technical improvement
Self-calibration of GS has been well-studied so far. Also, omnidirectional GS is existing. The proposed system would be practical, but the scientific motivation for combining those two is not quite large, i.e., the technical novelty is limited.

### Gradient derivation
The key technical part of the paper, the derivation of gradients on camera poses of spherical images (Eqs. (13--14)), is rather straightforward. This would be naturally extended from perspective cases. 

While the paper describes "converting 360-degree images to cube maps..." this is just about the camera models.
Although in different contexts, for example, Metashape and OpenMVS support spherical camera models for the SfM problem, which involves bundle adjustment (i.e., non-linear optimization using first-order derivative), so they should compute gradients in somewhat similar ways to Eqs. (13--14).

### Questions
I would appreciate it if the authors emphasized the technical (or scientific) novelty of the proposed method again.

### Soundness
3

### Presentation
2

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
This paper proposes a system for self-calibrating omnidirectional radiance fields, aiming to optimize 3D Gaussians, omnidirectional camera poses, and camera models in tandem. While the authors describe this as the first system of its kind, the contribution can largely be seen as an engineering effort to integrate multiple optimized parameters within a single framework. The primary novelty in the work appears to lie in the introduction of a differentiable omnidirectional camera model that enables ray-wise distortion handling and in the derivation of gradients for pose optimization.

### Strengths
- The paper is well-structured and easy to follow, making the methodology and findings accessible to readers.
- The introduction of a differentiable omnidirectional camera model that enables ray-wise distortion and the derivation of gradients for pose optimization are valuable innovations that expand the applicability of the system.
- The use of spherical weights in the photometric loss ensures spatially balanced optimization, which enhances the robustness and accuracy of the optimization process.
- The experiments and results demonstrate superior performance compared to previous methods, highlighting the effectiveness of the proposed approach.

### Weaknesses
Misleading Terminology in Title: While the title suggests "self-calibrating omnidirectional Gaussian splatting," the approach relies on initialization from a structure-from-motion (SfM) pipeline rather than directly calibrating intrinsic parameters from the images alone. This approach is more accurately an optimization process rather than an auto-calibration technique in the classical sense (e.g., auto-calibration from absolute dual quadrics in multiple-view geometry).



### Questions
- The paper reports PSNR results to demonstrate performance, but since it also optimizes camera poses, it would be beneficial to include a comparison of the optimized extrinsic parameters against ground truth values.

- Given the emphasis on self-calibration, could the paper also show improvements in the intrinsic parameters after optimization?

- Are the optimizations of focal length and distortion parameters shared across all views, or are they optimized per view? Clarifying this would be help.

### Soundness
3

### Presentation
4

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
The paper proposes a self-calibrating Gaussian splatting method for reconstructing omnidirectional radiance fields from 360-degree images without poses or with noisy poses. In this framework, scene representation, camera poses, and camera models are jointly optimized by minimizing a weighted spherical photometric loss. Additionally, a differentiable omnidirectional camera model is introduced to learn camera distortion. Experimental results show that the proposed method effectively recovers high-quality radiance fields from 360-degree image inputs.

### Strengths
(1) The paper proposes a novel self-calibrating method that extends the omnidirectional Gaussian splatting to handle unposed or noisy 360-degree images.

(2) The paper introduces a differentiable omnidirectional camera model, which uses trainable focal length and angle distortion coefficients to represent camera distortion. 

(3) The proposed method achieves state-of-the-art performance in novel view synthesis.

### Weaknesses
(1) The method estimates camera poses but lacks comparisons of pose accuracy. I think that comparing only rendering quality, especially with NeRF-based calibration methods, is insufficient to determine whether the superior performance of this paper is due to pose optimization, the camera model, or the scene representation using 3D GS. Therefore, I suggest adding quantitative and qualitative comparisons of camera poses on two datasets. 

(2) The experiment only compared with NeRF-based calibration methods and lacks comparisons with 3D GS-based baselines, such as COLMAP-free 3D GS. Besides, these NeRF-based calibration methods are originally designed to address noisy poses, rather than unposed images. I think it would be fairer to compare with poes-prior-free methods, such as NoPE-NeRF or LocalRF.

References:

A1. Fu, Y., Liu, S., Kulkarni, A., et al. COLMAP-Free 3D Gaussian Splatting, CVPR, 2024.

A2. Bian, W., Wang, Z., Li, K. et al. Nope-NeRF: Optimising neural radiance field with no pose prior, CVPR, 2023.

A3. Meuleman A, Liu Y L, Gao C, et al. Progressively optimized local radiance fields for robust view synthesis, CVPR, 2023.

(3) The paper does not include an ablation study of the anisotropy regularizer loss.

### Questions
(1) It would be better to provide the experimental results mentioned in the weaknesses.

(2) In Table 1, the paper does not provide results with random initialization and estimated depth in the comparison of perturbed poses.

(3) The paper states that it can address scenes with wide baselines. However, the method cannot be trained from scratch on real-world multi-room scenes, even though real-world datasets have more views than synthetic datasets. I recommend including a detailed analysis and results of the failure cases to better understand the reasons behind this limitation.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduce the first system capable of self-calibrating omnidirectional radiance fields, by simultaneously optimizing 3D Gaussians, omnidirectional camera poses, and camera models. Unlike previous works that project  360-degree images onto cube maps, this study preserves the integrity of 360-degree images by directly modeling the 360-degree camera. Additionally, this approach does not rely on precise camera calibration, allowing it to flexibly adapt to various downstream tasks, such as omnidirectional SLAM, by optimizing both intrinsic and extrinsic 360-degree camera parameters. This method achieves the best results among omnidirectional and self-calibration approaches based on NeRF and Gaussians.

### Strengths
1. The motivation of the paper is sound. Omnidirectional images have varying information densities across different pixels. Using cube maps-based projection combined with traditional perspective analysis is bound to introduce distortion (or aliasing). By directly modeling the 360-degree camera projection, the method leverages the continuity of 3D space, which can mitigate distortion and provide higher fidelity.
2. I like the chain rule-based derivation of the pose gradient in Equations 13 and 14, as it makes the camera optimization more reasonable.
3. The experiments are very thorough. The authors compare two datasets and cutting-edge methods (OmniGS), while also discussing the experimental results under different camera and point cloud initializations (Tab. 1), as well as the results after adding various perturbations (Fig. 5). This supports it to be a well-rounded work.

### Weaknesses
1. Some figure captions are too brief (Fig.2, Fig.3), requiring readers to refer back to the main text for clarification on several unclear points, which disrupts the reading flow.
2. In the visualizations, it seems that only the rendered results are compared, lacking some geometric information, such as depth visualizations and point cloud reconstructions.

### Questions
I have some confusion regarding the input. I notice that in datasets like the 360Roam dataset, there are 110 training views and 37 test views. Are these views entirely omnidirectional data, or are there some additional perspective camera images used as auxiliary data?

### Soundness
3

### Presentation
3

### Contribution
3
