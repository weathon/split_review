# RoDyn-SLAM: Robust Dynamic Dense RGB-D SLAM with Neural Radiance Fields

- Decision: Reject
- Scores: 5, 8, 5, 6

## Abstract
Leveraging neural implicit representation to conduct dense RGB-D SLAM has been studied in recent years. However, this approach relies on a static environment assumption and does not work robustly within a dynamic environment due to the inconsistent observation of geometry and photometry. 
To address the challenges presented in dynamic environments, we propose a novel dynamic SLAM framework with neural radiance field. Specifically, we introduce a motion mask generation method to filter out the invalid sampled rays. This design effectively fuses the optical flow mask and semantic mask to enhance the precision of motion mask. To further improve the accuracy of pose estimation, we have designed a divide-and-conquer pose optimization algorithm that distinguishes between keyframes and non-keyframes. The proposed edge warp loss can effectively enhance the geometry constraints between adjacent frames. Extensive experiments are conducted on the two challenging datasets, and the results show that RoDyn-SLAM achieves state-of-the-art performance among recent neural RGB-D methods in both accuracy and robustness. Our implementation of the Rodyn-SLAM will be open-sourced to benefit the community$^1$.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a method for dealing with dynamic environments for the purpose of rib d slam.  A motion mask appears to be created from the optical flow field and a semantic mask.  A neural radiance field is computed and sampled rays that are invalid are used to help generate the motion mask.

### Strengths
The paper presents the algorithm used with a clear description.  Results are presented comparing to other techniques in the field.

### Weaknesses
Only 2 datasets are used for testing.
Some acronyms are not provided what is ATE? in the results section.
It does not appear that the authors address the degenerate cases for computing the fundamental matrix, how does their method handle this?
With the comparisons, you should have compared to orb slam 3 and possibly DVO slam, an indirect and direct traditional method.
There is no mention of computation times, can this run in real time and what type of computing resources are required for such.  With the computation of a radiance field and the extra processes, it is hard to see this functioning in real time

### Questions
see weaknesses

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a implicit representation based RGB-D SLAM system, that is able to handle dynamic in the scene well. Two major features, namely 1) motion masking from both semantic and motion segmentation, and 2) per-frame tracking with edge consistency loss, are described in detail. Evaluation and ablation are sufficient, and the numbers seem pretty strong.

### Strengths
- This paper revisits an old topic in dynamic SLAM, i.e., getting rid of dynamic pixels before explicit / implicit optimization process. The idea of fusing motion segmentation mask over multiple keyframes is sound, and the evaluation reported are comprehensive and solid.
- As a system paper, the author did a great job covering both the overall system design, and the key components (masking and tracking) that contributes to the better performance of overall system. Writing and visualization are very clear to follow.

### Weaknesses
- While the overall writing is good, there are a few places that worthy of fix: e.g., in section 3.2 eq (4) there is no introduction on $j$ and $k$; also typos such as Camear in Fig 1. A thorough proofread is recommended.

### Questions
It's more of a general question on the subject of RGB-D only SLAM: modern visual-inertial solution has been proven to be very accurate and robust in providing highly accuracy 6DoF camera pose at a local scene. Therefore it sounds reasonable to formulate (implicit) mapping as a separate problem from pose tracking. How do you see this project going next on the mapping side?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a novel RGB-D dynamic SLAM system featuring a neural radiance representation. The system builds upon the open-sourced RGB-D neural SLAM Co-SLAM, introducing a motion mask (comprising optical flow and semantic information) to filter out invalid dynamic rays during training.

### Strengths
1. The exploration of dynamic SLAM with neural radiance field representation is a relatively new and promising avenue.
2. The paper is well-written and easy to follow.
3. The evaluation results are visually compelling and present a convincing case for the proposed method.

### Weaknesses
A key concern in this paper is the insufficiently explained rationale for incorporating neural radiance field representation in dynamic SLAM, along with a noticeable absence of robust baseline comparisons during the evaluation.

Please see questions for details.

### Questions
1. While the adoption of neural radiance fields in dynamic SLAM is a novel exploration, the motivation behind this choice is not entirely clear. A more detailed explanation of the potential benefits compared to existing dense dynamic SLAM methods would enhance the paper's clarity.
2. The evaluation primarily compares the proposed method against static neural SLAM, which may not be entirely fair. It would be beneficial to include related works as stronger baselines, including traditional SLAM methods like MID-Fusion[1] and Droid-SLAM[2], as well as NeRF SLAM methods like vMAP[3] and BundleSDF[4].
3. Although Fig. 3 displays TSDF fusion results, these results are not reported in tables. Comparing the results with and without the motion mask, as proposed in this paper, using TSDF fusion would be valuable and should be considered a baseline method.
4. The paper's visualization results are impressive; however, for a SLAM system, it would be preferable to include videos or real-world demonstrations as additional supplementary material.

[1]Mid-fusion: Octree-based object-level multi-instance dynamic slam. ICRA 2019.
[2]Droid-slam: Deep visual slam for monocular, stereo, and rgb-d cameras. NeurIPS 2021.
[3]vMAP: Vectorised object mapping for neural field slam. CVPR 2023
[4]BundleSDF: Neural 6-DoF Tracking and 3D Reconstruction of Unknown Objects. CVPR 2023

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Proposed a NeRF-based SLAM system (built upon Co-SLAM) to reconstruct the static 3D scene map in dynamic environments. To handle invalid sampling rays within dynamic objects, we filtered them out using a motion mask generation approach based on checking inliers and outliers using the fundamental matrix. Additionally, we introduced an Edge reprojection loss to remove the velocity constant assumption.

### Strengths
The paper is well-motivated and clearly written. It proposes techniques to address invalid sampling rays within dynamic objects, improving pose accuracy and robustness. Extensive evaluations support these claims, and the paper has a sufficient number of references.

### Weaknesses
Although I believe the paper is well-motivated and presents promising results in terms of both pose estimation and reconstruction, I have several concerns.
1. Doesn't introduce substantial architectural changes or novelty for NeRF-based SLAM. Such as multi-resolution hash encoding from instant ngp, joint optimization and store a subset of pixels to represent each keyframe from Co-SLAM, etc.
2. Enhancing additional losses (e.g., Edge reprojection loss) and masks to improve accuracy in dynamic object scenarios. How does the system's performance compare in terms of pose estimation and reconstruction in static scenes? Is it competitive with other SLAM systems?
3. I assume the GBA here is not an actual GBA like deployed in loop closure.

### Questions
The questions are listed in the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
