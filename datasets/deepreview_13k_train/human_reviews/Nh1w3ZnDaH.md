# Unsupervised Point Cloud Completion through Unbalanced Optimal Transport

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
Unpaired point cloud completion explores methods for learning a completion map from unpaired incomplete and complete point cloud data. In this paper, we propose a novel approach for unpaired point cloud completion using the unbalanced optimal transport map, called Unbalanced Optimal Transport Map for Unpaired Point Cloud Completion (UOT-UPC). We demonstrate that the unpaired point cloud completion can be naturally interpreted as the Optimal Transport (OT) problem and introduce the Unbalanced Optimal Transport (UOT) approach to address the class imbalance problem, which is prevalent in unpaired point cloud completion datasets. Moreover, we analyze the appropriate cost function for unpaired completion tasks. This analysis shows that the InfoCD cost function is particularly well-suited for this task. Our model is the first attempt to leverage UOT for unpaired point cloud completion, achieving competitive or superior results on both single-category and multi-category datasets. In particular, our model is especially effective in scenarios with class imbalance, where the proportions of categories are different between the incomplete and complete point cloud datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper an unpaired point cloud completion approach based on the unbalanced optimal transport map. The key idea is to formulate the unpaired point cloud completion task as the optimal transport problem and investigate the optimal cost function for this task, and introduce an unbalanced optimal transport framework for addressing the class imbalance problem. Experimental results show the proposed method achieves state-of-the-art performance in unpaired point cloud completion.

### Strengths
1.	I like the 3D shape completion topic, and the pipeline is carefully designed.
2.	The proposed method is evaluated on the dataset proposed in USSPA and performs better than SOTAs, although some important SOTAs are missing.
3.	The paper is clear and easy to follow.

### Weaknesses
1.	The authors should test more categories to explore the effects of class imbalance. It's not clear how the method would perform with more diverse and challenging class imbalances beyond the tested pairs. The current experiments are limited to a few object categories, which might not fully reveal the robustness of the proposed method under various imbalance conditions.
2.	The authors should conduct more datasets for demonstrating the effectiveness of the proposed mehtods, such as PCN datasets. The evaluation is primarily on a single dataset (USSPA), which limits the generalizability of the findings. Testing on PCN or other datasets would provide a more comprehensive assessment of the method's performance across different data distributions and complexities.
3.	Some important SOTA methods for 3D shape completion are missing. The authors should compare and discuss them with the proposed method. Specifically, the paper should include a comparison with methods such as ASFM-Net: Asymmetrical Siamese Feature Matching Network for Point Completion [1] and 3D Shape Generation and Completion Through Point-Voxel Diffusion [2]. These methods represent significant advancements in the field, and a discussion of their performance relative to the proposed method is necessary.
4.	The computational cost should be analyzed and compared with the other methods. The paper lacks a detailed analysis of the computational resources required by the proposed method, which is crucial for practical applications. A comparison of training and inference times with other state-of-the-art methods is needed to assess the method's efficiency.
5.	The authors are encouraged to provide code for reimplementation. The absence of publicly available code hinders reproducibility and makes it difficult for other researchers to validate and build upon the proposed method.

### Questions
1.	Compared with the diffusion based mehtods, what are the advantages of the proposed mehtod?
2.	Compared with USSPA, the proposed method has comparable (lower) performance in some categories. What is the reason?
3.	Is it possiable to complete unseen categories?
4.	Do the authors think the CD or F_score are the best metrics for evaluating 3D shape completion?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces UOT-UPC, an unpaired point cloud completion model based on the unbalanced optimal transport (UOT) map. The key idea is to train a model that learns the UOT map between the distribution of incomplete point clouds and the distribution of complete point clouds. This approach leverages the UOT framework's ability to address the class imbalance problem commonly found in unpaired point cloud completion datasets. The paper also identifies the InfoCD cost function as particularly well-suited for unpaired point cloud completion tasks. Experiments show that using InfoCD leads to better performance compared to other cost functions like l2, L2-Chamfer distance, and one-directional L2-Chamfer distance.

### Strengths
1. Novelty: UOT-UPC is the first model to apply the unbalanced optimal transport map to unpaired point cloud completion.

2. Robustness to Class Imbalance: The UOT framework allows UOT-UPC to effectively handle class imbalance. Experiments demonstrated that UOT-UPC maintained consistent performance across various class imbalance ratios, better than other models like USSPA and OT-UPC.

3. Better Performance: UOT-UPC achieves better performance on both single-category and multi-category settings on the dataset proposed by Ma et al. 2023.

### Weaknesses
1. Limited Cost Function Exploration: The paper's claim of identifying the "optimal" cost function can be challenged. While the authors compare four different cost functions (l2, L2-Chamfer distance (cdl2), one-directional L2-Chamfer distance (cdl2fwd), and InfoCD), this is a relatively small selection of potential options. Other cost functions, such as those incorporating learned feature spaces or adaptive weighting schemes, might exist that could yield even better performance. The study primarily relies on the ShapeNet dataset for evaluating these cost functions, which may not fully capture the nuances of different cost functions across diverse 3D shapes.

2. Dataset Dependence: The experiments primarily focus on a single dataset proposed in Ma et al. 2023, despite the availability of other datasets in the field, such as the PCN dataset or the Completion3D dataset. This raises concerns about the generalizability of UOT-UPC's performance to other datasets with varying levels of complexity, point cloud density, and object categories. Evaluating the model on a wider variety of datasets would strengthen the paper's conclusions and provide a more comprehensive understanding of UOT-UPC's capabilities and limitations, particularly in scenarios with different types of missing data or noise.

### Questions
According to the weakness part, please clarify the choice of cost function and report more results on other datasets. Besides, the source mixture trick seems interesting but not well-explained. Can you give more explanation and/or more insights about this trick?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper propose an unbalanced optimal transport for unpaired point cloud completion. They treat the completion problem as mapping incomplete set to complete set and utilize InfoCD for cost function. They show results for single-category and multiple-category unpaired point cloud completion and conducted many ablation study.

### Strengths
1. They propose to deal with the unbalance problem in point cloud completion.
2. They present better results than the competitors.

### Weaknesses
1. Optimal Transport Map is utilized to map the incomplete set to complete set. However, this assume the set of incomplete point cloud and the set of complete set should be complete set. For instance, this work utilized the complete point cloud from ShapeNet and partial point cloud from ScanNet. The original dataset only align the ShapeNet model with the real scans, however, the assumption in Optimal Transport is hard to be satisfied.
2. Experiments are only conducted in data from Scan2CAD. More experiments should be conducted on MatterPort3D or KITTI like "ACL-SPC: Adaptive Closed-Loop system for Self-Supervised Point Cloud Completion" and ModelNet or 3D-FUTURE like "CloudMix: Dual Mixup Consistency for Unpaired Point Cloud Completion".
3. More related works like "ACL-SPC: Adaptive Closed-Loop system for Self-Supervised Point Cloud Completion" and "CloudMix: Dual Mixup Consistency for Unpaired Point Cloud Completion" should be compared.

### Questions
Whether the assumption in optimal transport map is satisfied by the given data should be discussed.

### Soundness
2

### Presentation
2

### Contribution
2
