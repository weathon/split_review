# GSLoc: Efficient Camera Pose Refinement via 3D Gaussian Splatting

- Decision: Accept
- Avg Score: 6.40
- Scores: 8, 6, 6, 6, 6

## Abstract
We leverage 3D Gaussian Splatting (3DGS) as a scene representation and propose a novel test-time camera pose refinement framework, \sysname. This framework enhances the localization accuracy of state-of-the-art absolute pose regression and scene coordinate regression methods. The 3DGS model renders high-quality synthetic images and depth maps to facilitate the establishment of 2D-3D correspondences. \sysname obviates the need for training feature extractors or descriptors by operating directly on RGB images, utilizing the 3D foundation model, MASt3R, for precise 2D matching. To improve the robustness of our model in challenging outdoor environments, we incorporate an exposure-adaptive module within the 3DGS framework. Consequently, \sysname enables efficient one-shot pose refinement given a single RGB query and a coarse initial pose estimation. Our proposed approach surpasses leading NeRF-based optimization methods in both accuracy and runtime across indoor and outdoor visual localization benchmarks, achieving new state-of-the-art accuracy on two indoor datasets. The project page is available at \url{https://gsloc.active.vision}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a test-time refinement method, GSLoc, for improving camera localization accuracy. With a single RGB query, the method leverages ACT (exposure-adaptive affine color transformation) enhanced 3DGS and MASt3R to establish 2D-3D correspondences and then uses PnP + RANSAC for pose estimation. On two indoor and one outdoor datasets, the method achieved SOTA results.

### Strengths
++ The paper shows that, with introducing any new techniques, simply combining existing techniques can achieve state-of-the-art results for camera localization.

### Weaknesses
-- It appears that the authors misused \citep and \citet. This creates some difficulty when reading the paper.

-- Formulas should be followed by punctuation marks.

-- Please provide the detailed derivation of Eq. (3). It seems the translation part is incorrect.

-- Please provide analyses on the failure cases and potential limitations of the work.

-- The title is GSLoc, where GS stands for Gaussian Splatting, but the meaning of Loc is not mentioned in the paper. Since the focus of this work is on pose/localization refinement, Loc may not be the most suitable term.

### Questions
What are the failure cases and potential limitations of the work? Please provide some quantitative and qualitative results.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This method applies 3DGS to address the test-time camera pose refinement task. The manuscript first renders RGB and depth images from 3DGS, then matches the query image with the rendered images. To bridge the domain gap between the query image and 3DGS, an exposure-adaptive module is incorporated. Additionally, MASt3R is used as a training-free feature extractor for accurate matching. Extensive experiments demonstrate the effectiveness of the proposed GSLoc method.

### Strengths
S1 - The task appears meaningful, and the results presented in the manuscript are quite promising.

S2 - The Affine Color Transformation module is a noteworthy component, effectively addressing the RGB domain gap between the query image and the rendered images.

S3 - The experiments are well-designed and effectively demonstrate the superiority of the proposed GSLoc method over various baseline approaches.

### Weaknesses
W1 - The method appears to lack comparisons with state-of-the-art approaches, such as GLACE + GSLoc and ACE/GLACE + NeFes. Including these comparisons would provide a clearer benchmark for evaluating its performance.

W2 - I’m curious about the quality of the depth images rendered by 3DGS and whether they are consistent enough to serve as a reliable information source.

### Questions
Q1 - The sota comparision such as GLACE + GSLoc.

Q2 - The quality of the rendered depth image.

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
3

### Summary
This paper proposes a new approach to optimize the initial camera pose in visual localization. Using 3DGS as the scene representation, RGB images and depth maps are rendered based on the initial camera pose of the query image estimated by other methods. Then, 2D-2D matches between the query image and the rendered results are computed via MASt3R and elevated to 2D-3D matches using the depth maps. Finally, the relative pose is solved through PnP to optimize the initial camera pose. Compared to previous camera pose optimization methods based on cost functions and optimization, the GSLoc pipeline achieves one-shot pose optimization, offering advantages in both speed and accuracy. The effectiveness of GSLoc has been validated on indoor and outdoor visual localization datasets.

### Strengths
- The GSLoc pipeline combines the advantages of speed and accuracy. Through high-quality 3DGS reconstruction and rendering, it directly calculates optimized camera poses using image matching, which enhances the robustness and usability of the system compared to optimization methods based on specific cost functions.
- The writing of the paper is easy to follow.
- Comprehensive experiments have been conducted, demonstrating advantages over other camera pose optimization methods and traditional visual localization approaches.

### Weaknesses
 - The paper lacks certain experiments to demonstrate the necessity of the proposed method:
    - Table 2 shows the effectiveness of GSLoc compared to HLoc. However, it does not pair HLoc with an improved initial pose estimation method, such as ACE, as done for GSLoc. A reasonable baseline would be to use ACE to estimate the initial camera pose, retrieve the top-K images with the closest poses from the database, and then compute the localization result using HLoc and optionally refinet it with PixLoc. The comparison should isolate the impact of the pose optimization step, and not conflate it with the initial pose estimation.
- The novelty of the method is limited, as the effectiveness of the pipeline primarily relies on improvements in reconstruction and rendering quality provided by Scaffold-GS as the scene representation. The core idea of using rendered views for pose optimization is not entirely novel, and the paper does not sufficiently highlight the specific contributions beyond leveraging existing techniques.
- There is a lack of analysis on the method’s applicability:
    - Feasibility of high-quality 3DGS reconstruction: Reconstructing high-quality 3DGS to render the images needed for GSLoc requires densely sampled viewpoints. Moreover, modeling requires images with viewpoints very close to that of the query. How robust is GSLoc when there are no views close to the query viewpoint (i.e., in cases of wide baselines)? The paper does not explore the sensitivity of the method to the density of the training views used for 3DGS reconstruction.
    - Impact of significant appearance changes on the method (e.g., on datasets like Aachen-day-night or similar ones of smaller scenes). The method's reliance on appearance-based matching raises concerns about its robustness to significant changes in illumination, weather, or other environmental factors.
    - Feasibility of the method for large-scale visual localization (e.g., Aachen-day-night). The computational cost of rendering and matching, especially with high-resolution images, may limit the scalability of the method to large and complex environments.

### Questions
- What are the feature detector and matcher used by HLoc in the comparison shown in Table 2?
- In the runtime analysis, there seem to be some issues with the time calculation for GSLoc and GSLoc_rel.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper pays attention on camera pose refinement with 3D Gaussian Splatting as a scene representation, which aims to enhance the localization accuracy of state-of-the-art absolute pose regression and scene coordinate regression methods. A refinement framework, called GSLoc, is proposed to establish 2D-3D correspondences by an exposure-adaptive module. Experiments demonstrate that GSLoc improves the localization accuracy over different relocaliztion methods.

### Strengths
1 The paper proposes a novel test-time pose refinement framework, termed GSLoc, which employs 3D Gaussian Splatting for scene representation and utilizes the 3D vision foundation model MASt3R for precise matching.

2 GSLoc enhances the pose estimation accuracy of both APR and SCR methods across these benchmarks.

### Weaknesses
1 The main contribution is incremental.

(1)Firstly, the motivation of GSLoc is less interesting. From my viewpoint, the usage of feature matching for pose refinement is not novel. Meanwhile, the paper just uses 3D Gaussian Splatting for scene representation instead of traditional hand-crafted point cloud. Compared with Gaussian Splatting SLAM systems (like Gaussian SLAM [1, 2]), the idea of this paper is less innovative.

(2)Secondly, the innovative contributions are few. The paper seems a combination of current hot technologies, like 3D Gaussian Splatting and the 3D vision foundation model MASt3R.

[1]Gaussian Splatting SLAM, CVPR 2024

[2]GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting

[3]LoFTR: Detector-Free Local Feature Matching with Transformers, CVPR 2021

[4]DKM: Dense Kernelized Feature Matching for Geometry Estimation

2 The localization accuracy comparisons with feature matching based methods are missing. The core idea behind GSLoc is feature matching with 3D Gaussian Splatting. It is curious that whether GSLoc is also effective for pose refinement of leaned feature matching based methods, like LoFRT[3], DKM[4] or others. It is suggested to add these results.


3 The overlap of Figure 2 and 3 is somwhat high. It is suggested to modify Figure 3 to express the difference of GSLocrel in comparison with GSLoc.

### Questions
The question and suggestions are listed in the part of Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This proposes a novel visual localization method that utilizes 3D Gaussian Splatting. This approach replaces the point cloud in the pipeline of visual localization with a 3DGS model as the 3D representation. The camera pose of a query image is computed in a coarse-to-fine manner. The coarse pose is predicted by using a pretrained pose estimator. The pose refinement is carried out by neural rendering and image matching. The method is evaluated across indoor and outdoor datasets, outperforming state-of-the-art NeRF-based methods and traditional localization methods.

### Strengths
The idea of using 3DGS for visual localization is simple yet effective. It replaces the key components in the localization pipeline with advanced alternatives. For instance, the image retrieval module is replaced with a pose estimator for a coarse pose prediction. The 2D-3D matching is performed based on a prebuilt 3DGS model instead of the point cloud. The authors take the challenges, such as the appearance gap, into account and introduce an exposure adaption module, which enhances the appearance consistencies. The proposed method achieves more accurate camera pose estimates than the existing localization approaches on several datasets. The paper is well-written and easy to follow.

### Weaknesses
- The reliance of the proposed method on 3D Gaussian Splatting (3DGS) raises concerns about its scalability, particularly in large-scale and unbounded scenarios. While 3DGS offers advantages in rendering quality, its applicability to scenes typically requiring thousands of images for reconstruction, as seen in traditional localization pipelines, remains unclear. This potential limitation could restrict the method's practical use in real-world applications involving extensive environments.

- The authors contend that the top-1 retrieved image in Hierarchical Localization (HLoc) might exhibit limited overlap with the query. However, this appears to stem from limitations in current image retrieval techniques rather than being an inherent flaw in HLoc itself. The proposed pipeline employs an off-the-shelf pose estimator for coarse pose computation, potentially surpassing the capabilities of traditional image retrieval. This suggests that HLoc could similarly benefit from such an approach, for instance, by selecting references based on predicted camera poses. Thus, the purported advantage of 3DGS in this context is not entirely convincing.

- The evaluation metrics employed exhibit inconsistencies across different datasets. While accuracy is reported in some instances, pose error is presented in others. This lack of uniformity hinders a direct and fair comparison of the method's performance across various scenarios.

- A comparative analysis with traditional localization methods, such as HLoc, on the Cambridge Landmarks dataset is absent. Including this comparison would provide a more comprehensive evaluation of the proposed method's performance relative to established approaches.

### Questions
What is the major difference compared with 3DGS SLAM methods since they can also optimize the camera poses?

### Soundness
3

### Presentation
3

### Contribution
3
