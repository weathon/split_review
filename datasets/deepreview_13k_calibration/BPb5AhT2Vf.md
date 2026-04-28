# FreeReg: Image-to-Point Cloud Registration Leveraging Pretrained Diffusion Models and Monocular Depth Estimators

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Matching cross-modality features between images and point clouds is a fundamental problem for image-to-point cloud registration.
However, due to the modality difference between images and points, it is difficult to learn robust and discriminative cross-modality features by existing metric learning methods for feature matching.
Instead of applying metric learning on cross-modality data, we propose to unify the modality between images and point clouds by pretrained large-scale models first, and then establish robust correspondence within the same modality. 
We show that the intermediate features, called diffusion features, extracted by depth-to-image diffusion models are semantically consistent between images and point clouds, which enables the building of coarse but robust cross-modality correspondences.
We further extract geometric features on depth maps produced by the monocular depth estimator. By matching such geometric features, we significantly improve the accuracy of the coarse correspondences produced by diffusion features.
Extensive experiments demonstrate that \hp{without any training on the I2P registration task}, direct utilization of both features produces accurate image-to-point cloud registration. 
On three public indoor and outdoor benchmarks, the proposed method averagely achieves a $20.6\%$ improvement in Inlier Ratio, a $3.0\times$ higher Inlier Number, and a $48.6\%$ improvement in Registration Recall than existing state-of-the-arts. 
The code and additional results are available at \url{https://whu-usi3dv.io/FreeReg/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the image-to-point-cloud registration problem. The idea is to utilize a diffusion model and ControlNet to generate diffusion features from input point cloud. For images and point clouds, the final features used for matching are composed of both a diffusion part and a geometric part in a weighted average fashion. The latter is extracted from FCGF to serve as geometric features. The pixel-to-point correspondences are then obtained by a NN matching with mutual check. Experiments show the empirical improvements in I2P matching in several benchmark datasets.

### Strengths
- High-quality writing: The content is well-written, with a focus on clarity, coherence, and precision.

- Improved results over baselines: The results outperform standard models, demonstrating significant enhancements in performance and accuracy.

- Efficient feature distillation and cross-modality matching: Large model features are distilled effectively, facilitating feature matching across different modes for improved system performance.

### Weaknesses
 - The paper primarily focuses on the design of an improved feature that serves as a unifying element for both the image and depth map domains. While this feature has shown remarkable efficacy within this specific context, it may not be directly transferable to other cross-modality problems. Adapting it to different cross-modality tasks would necessitate careful and tailored design to ensure its successful application.

- Efficiency is indeed a concern as pointed out in the limitation section, as feature extraction via stable diffusion and ControlNet is a costly computation.

### Questions
1. Can the method work with only diffusion features from RGB and point clouds? e.g. Can the weighting between F_d and F_g be either 1 or 0?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a image-to-point cloud registration framework. The key idea is to generate RGB image from point cloud and reconstruct depth image from RGB so that correspondences can be established between images of the same modality. Though the image generation of both directions are well studied, a naive implementation does not work well. For this reason, the authors first generate depth image from point cloud and then use intermediate feature maps in the depth-to-image ControlNet to establish semantic correspondence with the original image. At the same time, a depth map is generated from the original image and local geometric features extracted from the depth map are combined with the semantic features for better correspondences. Experiments are conducted on three datasets, including both indoor and outdoor scenes.

### Strengths
1.The idea of first generating images and point clouds from the other modality and then find correspondence in the same modality is interesting and the authors find practical ways to implement this idea.

2.The performance is promising even without training on the target task with ground-truth correspondence.

3. The paper is well written and the adequate ablation studies are conducted.

### Weaknesses
1. As mentioned by the author, inference speed is a limit of the proposed method and 11s per image is quite slow.  I hope that the author can provide their thoughts for further improvement of speed.

2. Another limitation is that the performance is only comparable with the concurrent work 2D3D-MATR on the dataset RGBD-Scene-v2, while  I think that this is not a big problem and the proposed method has its own value. 

3. The residual rotation error seems quite large. I'd like to know what's the initial rotation error before registration?

### Questions
1. Is there any way that can are readily to be tried for speed improvement?

2. The residual rotation error is quite high. From a practical point of view, is the rotation error of 10 or 20 degrees a good threshold for recall?  What's the requirements of rotation accuracy in different application areas?

3. The authors "analyze" the limitation of straightforward/direct implementations in the 4th and 5th paragraph of Introduction, but did not provide any experimental results to support supporting the conclusion.  For the task of this paper and the fusion of two kinds of features, these straightforward may also work well.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Overall, the core idea of the paper is interesting, which considers leveraging diffusion networks to achieve feature enhancing in the task of image-point-cloud registration.

### Strengths
Overall, the core idea of the paper is interesting, which considers leveraging diffusion networks to achieve feature enhancing in the task of image-point-cloud registration.

### Weaknesses
1. The idea of using diffusion networks is interesting, but the way to use diffusion networks is to some extent trivial. It is not well-motivated  why you choose to use diffusion networks instead of any other pretrained feature extractor, such as those vision foundation backbones (DINO, SAM, CLIP, ...)? The paper lacks a clear explanation of the specific advantages of diffusion models for this task compared to other feature extractors. It's unclear what inherent properties of diffusion models make them superior for cross-modal feature alignment in image-to-point cloud registration. The choice seems more like an arbitrary selection rather than a well-justified design decision.

2. In Related Work (Image-to-point cloud registration), "In contrast, FreeReg does not require task-specific
training and finetuning and exhibits strong generalization ability to both indoor and outdoor scenes". It seems this description is not solid, as you feature extractors (diffusion networks and depth estimation networks) are already trained on some datasets. The claim of not requiring task-specific training is misleading since the method relies on pre-trained models, which have been trained on other datasets. The statement should be more nuanced to reflect the fact that while no training is done on the registration task itself, the method is still dependent on pre-existing training.

3. The baseline comparison is a little bit weak. More recent and related works should be considered. And in Table S1, the proposed approach seems not solid outperform the counterpart 2D3D-Matr.
[1] Corri2p: Deep image-to-point cloud registration via dense correspondence. TCSVT 2022.
[2] EP2P-Loc: End-to-End 3D Point to 2D Pixel Localization for Large-Scale Visual Localization. ICCV 2023.
[3] CFI2P: Coarse-to-Fine Cross-Modal Correspondence Learning for Image-to-Point Cloud Registration. arXiv 2023.
[4] CoFiI2P: Image-to-Point Cloud Registration withCoarse-to-Fine Correspondences for Intelligent Driving. arXiv 2023.
[5] End-to-end 2D-3D Registration between Image and LiDAR Point Cloud for Vehicle Localization. arXiv 2023.


4. In Table 4, what is the performance under w=0 and w=1.0 ? The paper does not provide a clear analysis of the impact of the weighting parameter 'w' on the performance of the proposed method. The absence of results for the extreme cases (w=0 and w=1) makes it difficult to understand the role of this parameter in the overall performance.

5. The run time speed/memory comparison with other models is missing. The paper lacks a thorough analysis of the computational cost of the proposed method. It is important to compare the runtime and memory usage of FreeReg with other baseline methods to assess its practical applicability.

### Questions
Please refer to Weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
