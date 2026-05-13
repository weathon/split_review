# PrML: Progressive Multi-Task Learning for Monocular 3D Human Pose Estimation

- Decision: Reject
- Scores: 6, 6, 3

## Abstract
The lifting-based framework has dominated the field of monocular 3D human pose estimation by leveraging the well-detected 2D pose as an intermediate representation. However, it neglects the different initial states between 2D pose and per-joint depth and encodes the well-detected 2D pose feature and unknown per-joint depth feature in an entangled feature space. To address this limitation, we present a novel progressive multi-task learning pose estimation framework named PrML. Firstly, PrML introduces two task branches: one is to refine the well-detected 2D pose feature and the other is to learn the per-joint depth feature. This dual-branch design reduces the explicit influence of uncertain depth features on 2D pose features. Secondly, PrML employs a task aware decoder to supplement the complementary information between the refined 2D pose feature and the well-learned per-joint depth feature. This step establishes the connection between 2D pose and per-joint depth, compensating for the lack of interaction caused by the dual-branch design. We also conduct theoretical analysis from the perspective of mutual information and arrive at a loss to constrain this feature complementary process. Finally, we use two regression heads to regress the 2D pose and per-joint depth respectively, and concatenate them to obtain the final 3D pose. Extensive experiments show that PrML outperforms the conventional lifting-based framework with fewer parameters on two widely used datasets: Human3.6M and MPI-INF-3DHP. Code is available at https://anonymous.4open.science/r/PrML and we hope our effort can provide a new framework for monocular 3D human pose estimation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The manuscript proposes a multi-task learning method that independently models and regresses 2D pose and depth features, achieving good performance on 3D HPE benchmarks. Its advantages and weakness are as follows:

Advantages:
1. The motivation of the proposed method is solid. 
2. The manuscript is well written and clearly presented.
3. The multi-task learning method with two separate regression heads demonstrates effectiveness when applied to other approaches.

Weakness:
1. The difference between the descriptions/ theoretical analysis in the paper and the provided source code, particularly regarding the model architecture and the key proposal of mutual information loss.
2. The effectiveness of the mutual information loss requires further validation.
3. Lack of related comparison method.

### Strengths
1. The motivation of the proposed method is solid. 3D pose estimation lifted from detected 2D joints is inherently an ambiguous problem, since the output 2D pose has a well-detected 2D pose as initialization but the depth is learned from scratch. The authors suggest that the unknown depth may erode the 2D pose in the entangled feature space. To tackle this problem, they propose a PrML model with two separate branches to learn 2D pose and joint depth. On this basis, a task-aware decoder is developed to connect the 2D pose features and joint depth features. The decoded features are then regressed with two separate heads to obtain the 2D pose and depth coordinates.
2. The manuscript is well written. Combining the visualization analysis, the authors clearly present the rationale behind the motivation and demonstrate the model's improvements in relevant aspects.
3. The effectiveness of the multi-task learning concept is validated on other methods. Significant performance improvements are obtained by setting up two separate regression heads to independently optimize 2D and depth coordinates.

### Weaknesses
However, after reading the code provided by the authors, I have several questions, mostly about the difference between the code and the descriptions in the manuscript.
1) The architecture of shared bottom in PrML. From the code, the shared bottom follows the main architecture of MotionBert, of which spatial and temporal blocks are differently ordered to form two distinct branches, with the output features adaptively fused with an attention regressor. It is a typical architecture rather than the simple description of “Vanilla self-attention” in the manuscript. The authors should provide a more detailed and accurate description of the shared bottom architecture.
2) Difference in the Mutual Information Loss. In the code, the mutual information comprises two parts: a. the KL Divergence between pose label Y2D and pose support feature S2D; b. the KL Divergence between depth label YD and depth support feature SD. However, the descriptions in equations 5-7 which introduce the distribution dependency between support features (S2D/SD) and bias features (B2D/BD) are not implemented in the source code. The authors should address this inconsistency to improve the paper's clarity and reproducibility.
3) The impact of Mutual Information Loss. In the code, the KL Divergence losses for pose and depth are assigned small coefficients of 0.005 and 0.05, respectively, and are further multiplied with a 0.01 factor in the final loss function, resulting in a very small overall contribution. Thus, the impact of Mutual Information Loss should be further verified to demonstrate its importance as one of the key contributions in the paper.
4) The results on Human3.6M are based on 2D pose detected by SH, which is in consistency with MotionBERT. However, SH-detected 2D poses from Human3.6M are not widely used currently, as most lifting-based methods rely on CPN-detected poses. Therefore, the other competitor MotionAGFormer[1] which also utilizes the SH detected 2D poses should be presented for a more comprehensive comparison of properties.
[1] MotionAGFormer: Enhancing 3D Human Pose Estimation With a Transformer-GCNFormer Network, WACV2024

### Questions
Same with the weakness.

### Soundness
2

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
This paper points out the problem of current lifting-based 3D human pose estimation: encoding the well-detected 2D pose and uncertain depth will erode the 2D pose. Based on such intuition and some experimental observations, the authors propose to predict 2D pose and per-joint depth using two disentangled branches as a Multi-task learning task to solve the raised problem. 
The authors adopt a task-aware decoder to share the 2D pose and depth features. Two types of support features are achieved by combining two corresponding learnable 2d pose and depth biases. The supervising and unsupervised mutual information losses are leveraged to train the model.
The extensive experiments show the proposed method gains improvements over SOTA lifting-based methods. And the ablations validate the effectiveness of each component. Feature distributions and pose visualization show significant results.

### Strengths
1. The paper is well-written and easy to follow.
2. The paper proposes a novel perspective for solving the 2d-3d lifting problem of 3d human pose estimation. It significantly focuses on the uncertainty problem of per-joint depth estimation. Predicting 2D pose and per-joint depth in a disentangled manner reduces the difficulty of prediction and may have a less negative impact on the regression of 2D pose coordinates.
3. The experiments and demonstrations are thorough and persuasive, and the effectiveness of each proposed module has been validated.
4. The experiments involving noisy 2D poses demonstrate the model's improved robustness, which aligns with the motivations behind the model design.

### Weaknesses
1. Although the modeling of 2D-3D lifting is significantly improved in this paper, the per-joint depth information implicitly contained in the 2D pose sequence remains limited.  As performance approaches the theoretical limit, the accuracy upper bound of depth prediction may become less related to the model architecture, due to the inherent information entropy of the input 2D pose sequence.
2. The accuracy gain brought by the mutual information loss is limited, as shown in Table 4. 
3. The feature distribution visualization in Figure 6 reveals the disentangled states of pose and depth features within their feature space. However, since the 2D XY coordinates and the Z coordinate of the 3D pose have different value distributions, it is natural to see their original features distributed across each other. Some comparisons with other lifting-based methods may be needed.

### Questions
1. Did the authors attempt to use image features as input to improve the depth prediction capability, given that the lifting problem is still ill-posed?
2. What is the meaning of the statement regarding the different initial states of the 2D pose and per-joint depth? Does this indicate an error in the detected 2D pose?
3. The qualitative examples of the inaccurate projected 2D poses in Figure 2 may be insufficient. Some quantitative metrics comparing the accuracy of the projected 2D poses versus existing methods could provide stronger evidence.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a 3D human pose estimation system that takes a 2D pose as an input. Different from previous works that output 3D pose using a single module, the proposed one estimates refined 2D pose and depth using respective modules. The motivation for this is to preserve well-detected input 2D pose as much as possible and prevent the depth estimation module from making the encoded 2D pose bad. In addition, the task-aware decoder is introduced to minimize the gap between 2D and depth modules.

### Strengths
An attempt to preserve well-detected 2D poses makes sense.

### Weaknesses
1. Novelty is not enough. The main idea of this work is to preserve well-detected 2D pose when doing the 3D pose estimation. First, the idea of separately estimating 2D pose and depth have been tried many times. For example, “Hand Pose Estimation via Latent 2.5D Heatmap Regression” (ECCV 2018). Second, how the authors achieved this is too straightforward by simply designing separate branches. The architecture of each branch simply follows existing Transformer-based ones. The task-aware decoder is introduced to complement relevant information; however, Table 4 shows that introducing TAD improves the 3D errors less than 1 mm.

2. Not reliable ablation studies. Table 4 shows that the baseline has MPJPE 50, which is worse than any methods in Table 1. It seems the baseline is too weak and this exaggerates the effectiveness of the proposed contributions, such as multi-task learning. Table 7 shows that the improvement is more or less 1 mm. I’m not sure the 1 mm improvement is meaningful.

3. Old benchmarks. The authors use Human3.6M and MPI-INF-3DHP benchmarks. They are good, but old. They were published more than 10 years ago. The authors should have reported results on newer ones as well, including 3DPW, AGORA, BEDLAM, EMDB.

### Questions
No questions.

### Soundness
2

### Presentation
2

### Contribution
2
