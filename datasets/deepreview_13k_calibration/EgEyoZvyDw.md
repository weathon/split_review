# Long-Term 3D Point Tracking By Cost Volume Fusion

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Long-term point tracking is essential to understand  non-rigid motion in the physical world better. Deep learning approaches have recently been incorporated into long-term point tracking, but most prior work predominantly functions in 2D. Although these methods benefit from the well-established backbones and matching frameworks, the motions they produce do not always make sense in the 3D physical world. In this paper, we propose the first deep learning framework for long-term point tracking in 3D that generalizes to new points and videos without requiring test-time fine-tuning. Our model contains a cost volume fusion module that effectively integrates multiple past appearances and motion information via a transformer architecture, significantly enhancing overall tracking performance. In terms of 3D tracking performance, our model significantly outperforms simple scene flow chaining and previous 2D point tracking methods, even if one uses ground truth depth and camera pose to backproject 2D point tracks in a synthetic scenario.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a new deep learning framework specifically designed for long-term 3D point tracking, capable of functioning without test-time optimization. Recognizing the limitations of previous 2D tracking methods, the authors have developed a coarse-to-fine tracking approach that leverages a transformer architecture and a cost volume fusion module at each level of processing. This allows for effective integration of multiple past appearances and motion information, significantly enhancing tracking accuracy and performance, particularly through periods of occlusion.

### Strengths
1. The paper introduces a deep learning-based framework for long-term 3D point tracking, a first in its domain according to the authors' claims. This approach is impressive how it combines various techniques to address a complex problem. 
2. The authors provided extensive experimental results over various benchmarks to verify their claims.

### Weaknesses
1. The authors claim this is the first method for 3D point tracking. However, a highly related work SpatialTracker [A] is neither discussed or compared here. Although SpatialTracker works on 2D images and depths instead of directly on 3D points, its input and output are exactly the same to this work. The authors should discuss and compare with SpatialTracker to verify their points. This is also related to another question, "is it really necessary to lift depths to 3D points for 3D tracking?"

2. The reviewer is quite curious about the 2D projection accuracy of the method. The paper provides Table 4, but this is not very convincing because Kubric is a super simple synthetic dataset and the proposed model has been trained on Kubric. The reviewer recommends testing the proposed method on TAP-Vid DAVIS or other real-world datasets with complex point tracks and occultation to verify its effectiveness.

### Questions
Reviewers would recommend that the authors provide necessary comparison to SpatialTracker and test the proposed method on TAP Vid DAVIS.


(Not important): the paper mentions "then train and test on two separate datasets, TAPVid-Kubric (Doersch et al., 2022) and PointOdyssey (Zheng et al., 2023).". Does this mean the model was trained on the combination of Kubric and PointOdyssey?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a novel deep learning framework for long-term 3D point tracking, leveraging cost volume fusion with a transformer architecture. Designed to track dynamic points without test-time optimization, the model incorporates multiple past appearance and motion cues, outperforming existing 2D tracking approaches when projected to 3D.

### Strengths
Utilizes a transformer-based cost volume fusion module to handle occlusions and integrate long-term appearance and motion information.

Extensive performance evaluation demonstrates superiority over 2D methods, especially in occluded scenarios.

### Weaknesses
As the paper claimed that it is the first method to achieve 3D point tracking without test-time optimization, to the reviewer's best of knowledge, some works such as FlowNet3D could also predict point cloud tracking results without test-time optimization. The difference between the proposed method and these methods is not clear.

As the paper strengthens that it does not need test-time optimization, a brief comparison of runtime performance would enhance the practical applicability discussion.

The model relies heavily on synthetic datasets (e.g., TAPVid-Kubric, PointOdyssey), which may limit generalizability to real-world, varied environments.

The paper conducts qualitative comparisons only with CoTracker, which is insufficient and somehow weak. It may need to include more qualitative comparisons in the paper.

### Questions
There are some unclear expressions in the paper. For example, what is the meaning of (-26.2) (-15.3) in Table 2? It is not clear why novel view in Figure 3 is black and inconsistent with the original view color.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a feed-forward approach for tracking points in 3D space across long video sequences. While previous methods mostly work in 2D and can produce physically implausible motions when projected to 3D, this method directly tracks in 3D space and works without test-time optimization. The key technical contributions are a coarse-to-fine approach with cost volume fusion at each level (using transformers to combine past appearance and motion information) and explicit occlusion handling. The authors show their method outperforms both scene flow chaining and 2D tracking methods that are projected into 3D, even when those methods have access to ground truth depth and camera poses (all experiments performed on synthetic data).

### Strengths
- I like the paper's idea and the problem it tackles. The problem setting is quite close to scene flow - while there have been many scene flow papers recently, it remains an unsolved problem. The paper's main novelty lies in its network architecture. Although its individual components aren't novel (the overall architecture resembles recent point tracking papers like PIPs, Harley et al.), applying it to long-term 3D tracking is a nice contribution.

- The paper is well-written and well-structured, with clearly described technical details. I especially appreciate the well-written related work section, which helps readers who don't work directly in scene flow/tracking.

- The paper demonstrates good quantitative improvements over SOTA methods.

### Weaknesses
 * Missing evaluations on real data: Although the paper has extensive evaluations against recent scene flow methods, it lacks any evaluation or even qualitative results on real data (I checked the supplementary material as well). While I understand that real data doesn't always provide good ground truth, especially for dynamic objects, making evaluation challenging, the absence of results on common benchmarks like the KITTI Scene Flow dataset is unfortunate. The complete lack of real-data results, even qualitative ones, makes it difficult to assess the paper's practical impact. I would like to see more results on real data in the rebuttal.

* Missing discussion about online tracking: The paper doesn't compare to test-time optimization methods like Wang et al. (2023) and Luiten et al. (2023), arguing that their method "tracks points online without test-time optimization." While I agree it's a feed-forward method that's potentially less computationally expensive than test-time optimization, "online" is a strong claim. There's no discussion or computational cost analysis comparing their method to existing approaches. (There is some runtime information in the supplementary, but no comparison against other methods).

### Questions
I'm optimistic about the paper overall, but would like to see more results on real data to complement the synthetic data presented in the paper.

Final review after rebuttal: I thank the authors for addressing some of my concerns and correcting some terminology misunderstanding. That being said, I agree with other reviewers about the writing quality could be improved, and I'm not completely convinced about the novelty of the proposed method. Given these reasons, I improved the rating to 6 (slightly above acceptance).

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
The paper presents a novel deep-learning method for long-term point tracking in 3D, which generalizes to new points and videos without test-time fine-tuning. Using a coarse-to-fine approach with cost volume fusion modules and transformers, the model effectively integrates appearance and motion information, allowing it to handle occlusions and outperform prior 2D methods and scene flow chaining in 3D tracking accuracy.

### Strengths
1. The paper tackles an important problem in computer vision.

2. The proposed method outperforms the 2D tracking and Scene Flow Chaining baselines in 3D point tracking, and surpasses scene flow methods in scene flow estimation on the FlyingThings dataset.

3. The authors provide ablation studies of their design choices.

### Weaknesses
1. The paper could benefit from improved writing, especially in the sections describing the method.

2. The method claims to be the first online deep learning-based tracking framework capable of tracking any point in 3D point clouds. However, both SpatialTracker [a] (CVPR24) and SceneTracker [b] also propose generalizable 3D tracking methods. The authors should cite, discuss, and compare their method to these works.

3. While you propose a learning-based method, comparing it with optimization-based 3D trackers as a reference would be beneficial.

Note: You should define the EPE3D metric, which is used in Table 1, in the text.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
