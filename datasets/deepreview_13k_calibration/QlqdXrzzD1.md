# Towards Category Unification of 3D Single Object Tracking on Point Clouds

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
\vspace{-5pt}
Category-specific models are provenly valuable methods in 3D single object tracking (SOT) regardless of Siamese or motion-centric paradigms. However, such over-specialized model designs incur redundant parameters, thus limiting the broader applicability of 3D SOT task. This paper first introduces unified models that can simultaneously track objects across all categories using a single network with shared model parameters. Specifically, we propose to explicitly encode distinct attributes associated to different object categories, enabling the model to adapt to cross-category data. We find that the attribute variances of point cloud objects primarily occur from the varying size and shape (\textit{e.g.}, large and square vehicles \textit{v.s.} small and slender humans). Based on this observation, we design a novel point set representation learning network inheriting transformer architecture, termed \textit{AdaFormer}, which adaptively encodes the dynamically varying shape and size information from cross-category data in a unified manner. We further incorporate the size and shape prior derived from the known template targets into the model’s inputs and learning objective, facilitating the learning of unified representation. Equipped with such designs, we construct two category-unified models SiamCUT and MoCUT. Extensive experiments demonstrate that SiamCUT and MoCUT exhibit strong generalization and training stability. Furthermore, our category-unified models outperform the category-specific counterparts by a significant margin (\textit{e.g.}, on KITTI dataset, $\sim$12\% and $\sim$3\% performance gains on the Siamese and motion paradigms).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Existing 3D single object tracking (SOT) approaches mainly focus on category-specific model training and evaluation. Inspired by general 2D SOT, this paper proposes to use category-unified model for 3D SOT. Specifically, the paper proposes a point set network named AdaFormer to encode geometric information of different object categories in a unified manner. To further boost the performance, the unified model inputs and learning objective are introduced to facilitate the learning of unified representation. To verify the effectiveness, two category-unified models SiamCUT and MoCUT based on Siamese and motion-centric 3D SOT paradigms are proposed. Experiments on KITTI and NuScenes datasets show that the proposed approaches gain much performance improvements over the baselines.

### Strengths
- The paper written&&organization is good, which is easy to follow.
- I think the problem solved in this paper is valuable to the 3D SOT community, since current approaches mainly need to train multiple models corresponding to various training categories in the dataset in order to achieve higher performance. This paper shows competitive category-specific results by only learning a unified representation model (although I do not see the authors claim any training details about their unified training, e.g., training their models on all category samples on KITTI and then test it on category-specific KITTI).
- The paper is technically sound, which solves the above problem progressively by proposing multiple modules.

### Weaknesses
 - The proposed approach can track objects across all categories using a single network with shared parameters. But as I mentioned above, there is no training details about the unified training. Is the proposed only trained on the full KITTI and then test on it (the same for Nuscenes)? or the combination of KITTI and Nuscenes are used? Please all more illustration in the paper.
- The main concern in this paper is about the lack of Waymo dataset evaluation and missing recent approaches for comparison. Please also include the latest references below for comparison, in order to better verify the effectiveness of the proposed approach.

[1] Temporal-aware Siamese Tracker: Integrate Temporal Context for 3D Object Tracking. ACCV 2022.
[2] 3D Siamese Transformer Network for Single Object Tracking on Point Clouds. ECCV 2022.
[3] CXTrack: Improving 3D Point Cloud Tracking with Contextual Information. CVPR 2023.
[4] A Lightweight and Detector-Free 3D Single Object Tracker on Point Clouds. IEEE Transactions on Intelligent Transportation Systems. 2023.

### Questions
- The proposed approach can track objects across all categories using a single network with shared parameters. But as I mentioned above, there is no training details about the unified training. Is the proposed only trained on the full KITTI and then test on it (the same for Nuscenes)? or the combination of KITTI and Nuscenes are used? Please all more illustration in the paper.
- The main concern in this paper is about the lack of Waymo dataset evaluation and missing recent approaches for comparison. Please also include the latest references below for comparison, in order to better verify the effectiveness of the proposed approach.

[1] Temporal-aware Siamese Tracker: Integrate Temporal Context for 3D Object Tracking. ACCV 2022.
[2] 3D Siamese Transformer Network for Single Object Tracking on Point Clouds. ECCV 2022.
[3] CXTrack: Improving 3D Point Cloud Tracking with Contextual Information. CVPR 2023.
[4] A Lightweight and Detector-Free 3D Single Object Tracker on Point Clouds. IEEE Transactions on Intelligent Transportation Systems. 2023.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Previous 3D single object tracking models are all category-specific, incurring redundant parameters. In this paper, the authors propose to unify the different categories in a single model. A novel point cloud representation learning network based on transformers, named AdaFormer, is proposed to encode the dynamically varying shape and size information from cross-category data in a unified manner. Moreover, the authors construct two unified models following previous Siamese and motion-centric paradigms to compare. Performance gains validate the effectiveness of proposed method.

### Strengths
1. The motivation is great, category-unified model designing is meaningful and significant to SOT task and trying to unify them is of novelty.
2. The model achieves good performance on KITTI and nuScenes.

### Weaknesses
No obvious weakness from my perspective

### Questions
Are there any inference speed and FLOPs comparison for proposed method?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces an Adaformer to dynamically extract features of different categories with diverse object sizes. To this end, it can adapt to LiDAR-based 3D SOT tasks for unified training. Albeit the idea is relatively common, it can achieve the target of unified training with performance improvement.

### Strengths
- It is the first work to unified train all categories on the 3D SOT task.
- The proposed Adaformer can effectively learn adaptively ball region relative to different categories, which agrees with the motivation of this paper.
- The paper is well-written.

### Weaknesses
 - You should discuss relative works on your key idea (e.g., encoding shape- and size-changed geometric information). 
   Relative works include [a] (adaptive region learning), [b] (dynamic ball-query selection for size, dynamic foreground and background learning), [c], etc.

   [a] Pyramid r-cnn: Towards better performance and adaptability for 3d object detection.

   [b] DBQ-SSD: Dynamic Ball Query for Efficient 3D Object Detection.

   [c] RBGNet: Ray-Based Grouping for 3D Object Detection.

- The comparison of latency should include other methods that have been reported, e.g., [c], [d], etc. In addition, the recent SOTA SOT methods should also be included.

   [c] Beyond 3d siamese tracking: A motion-centric paradigm for 3d single object tracking in point clouds.

   [d] Implicit and Efficient Point Cloud Completion for 3D Single Object Tracking.

- Why not verify on Waymo dataset？

- Can Adaformer be extended to general detection？

- Can you conduct other statistical analysis to reveal diverse size of different categories to further support you motivation?

### Questions
Please see the Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
