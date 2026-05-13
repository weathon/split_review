# Dual-level Adaptive Self-Labeling for Novel Class Discovery in Point Cloud Segmentation

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
We tackle the novel class discovery in point cloud segmentation, which discovers novel classes based on the semantic knowledge of seen classes.
Existing work proposes an online point-wise clustering method with a simplified equal class-size 
constraint on the novel classes to avoid degenerate solutions. However, the inherent imbalanced distribution of novel classes 
in point clouds typically violates the equal class-size constraint. Moreover, point-wise clustering ignores the rich spatial context information of objects, which results in less expressive representation for semantic segmentation.
To address the above challenges, we propose a novel self-labeling strategy that adaptively generates high-quality pseudo-labels for imbalanced classes during model training. In addition, we develop a dual-level representation that incorporates regional consistency into the point-level classifier learning, reducing noise in generated segmentation. Finally, we conduct extensive experiments on two widely used datasets, SemanticKITTI and SemanticPOSS, and the results show our method outperforms the state of the art by a large margin.
 \keywords{Novel class discovery \and Point clouds semantic segmentation \and Long-tailed learning}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the task of novel class discovery in point cloud segmentation. It addresses two major issues that were present in the previous work NOPS (Riz et al. 2023): the equal class-size constraint and the omission of spatial context information during point-wise clustering. The authors introduce an adaptive self-labeling method. This method relaxes the optimal transport problem by transforming it into a semi-relaxed optimal transport (OT) problem with an annealing-like regularization strategy. Moreover, the proposed approach includes a region-level branch by clustering points into regions and generating region-level features via pooling, complementing the point-level features for prediction. The proposed method is evaluated on two outdoor datasets, and it demonstrates impressive performance compared to the baseline method NOPS.

### Strengths
1. The proposed method is technically sound and is well-motivated.
2. Notably, the results on the SemanticPOSS dataset are remarkable and demonstrate the effectiveness of the proposed approach.
3. This paper includes comprehensive ablation studies that thoroughly validate the impact of various components within the framework. This provides a strong basis for the proposed method's effectiveness.

### Weaknesses
1. The utility of the novel class discovery setting, where the number of novel classes is predetermined, is a valid point for consideration. In an open-world scenario, the number of novel classes is often dynamic and not known in advance.
2. Adding more specific details about the clustering process would provide a better understanding. This could include parameters for the DBSCAN algorithm, visual examples of the resultant regions, and how variations in DBSCAN parameters may impact the results. Additionally, clarification on whether "K" is a fixed value for different scenes and how these "K" regions are generated during clustering is needed.
3. Elaborating on the initialization and updating process for class prototypes would be beneficial to better understand the methodology.
4. Discussing the applicability of the proposed framework in indoor scenarios, where there are typically more novel classes to discover, would enhance this paper's practical relevance.
5. Conducting an ablation study on a split of the SemanticKITTI dataset, which is known to be more challenging than SemanticPOSS, would strengthen this paper's findings.

A minor point: In Table 3, adding a column that indicates the split index, similar to Table 1, would improve clarity.

### Questions
Please refer to the comments in the weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents a novel method for novel class discovery in point cloud segmentation. Specifically, the authors proposed a self-labeling strategy for addressing imbalanced classes and introduced a dual-level representation to enhance regional consistency. The experiments demonstrate that this method leads to a significant improvement in performance.

### Strengths
1. The proposed method is well-motivated, addressing the issues of imbalanced classes and regional consistency. 
2. The experimental results are comprehensive and meticulously detailed. The impact of different settings and various components of the method is considered and discussed.

### Weaknesses
1. The paper's content lacks a smooth organization and its order creates confusion regarding the key method modules. Figure 1 is incomplete, with unexplained symbols. 
2. The analysis of the experimental results is not very sufficient.

### Questions
1. Does the parameters of DBSCAN have an impact on the final result? 
2. In the ablation results, the application of region-level learning results in a decrease in the IoU value for 'Building.' Why does this phenomenon occur, and is this method more beneficial for smaller objects?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies an interesting problem of novel class discovery in 3D point cloud.
Targeting the weakness of the existing method, this paper proposes two strategies to improve in two directions:
- To improve the ability to cope with class imbalance for novel class discovery, this paper proposes a self-labeling learning procedure that leverages prototypical pseudo-labels. The class distribution of pseudo-labels is regularized under the framework of relaxed Optimal Transport (OT).
- To improve the ability to utilize the spatial relations among points, the authors propose to utilize both point-level and region-level features for pseudo-label generation.

### Strengths
The formulation of relaxed OT is interesting and the paper shows how the adaptive regularization strategy is effective in annealing its regularization on class balance/imbalance with both theoretical meaning and empirical studies.

The empirical results are promising compared to previous methods.

This paper is well-written and easy to follow.

### Weaknesses
In Fig 1, the method requires 2 views of the same point cloud. Though not quite mentioned, I guess it indicates two independently augmented views of the same point cloud. This is however quite abnormal considering that the pseudo-label is based on prototypes. The paper does not really explain how the augmentation is used alongside all these proposed strategies, which is quite concerning: How  such augmentations affect the method? Does the method really need such augmentations to function? And how does it compare to the method in comparison, eg fairness?

The paper uses heavy notations but most of them are not quite explained and I would recognize some of the notation as unnecessary, especially the overly used sub/superscripts, which hinders the readability of this paper. For example, the notations in 3.1 and 3.2.

Regarding the relaxed OT, the author adds an entropy term to Eq 4 to enable the use of fast scaling algorithms. However, this detail is not explained, regarding how it affects the OT solution and thus pseudo-label generation. In Appendix A, the discussion seems to be more focused on time complexity but not the class implance aspects.
Considering that the authors claim novelty in such formulation of relaxed OT, more discussion and analysis is required, especially regarding how OT captures the class balance/imbalance and its impact.

Besides, since the authors emphasize the dynamic nature of weight r, which seems to be a key difference to previous methods, it's nice to see how this relaxed OT reduces to the original OT for a balanced class by controlling the r, if possible.

Also, how r affects the pseudo-label deserves more discussion and analysis. For example, a visualization on pseudo-labels of larger/smaller r, or theoretical analysis, would be desired.

### Questions
see weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper effectively addresses the problem of novel class discovery in point cloud segmentation. The proposed method includes a novel self-labeling strategy and a dual-level representation. A regularization technique is also introduced for the self-labeling process. From the experiment, the proposed method is shown to be promising and effective.

### Strengths
New methodology for the novel class discovery in point cloud segmentation. 
Well-formulated problem.
Promising experimental performance.

### Weaknesses
I would say that this paper suffers from a lack of clarity a lot. 
The readability is also limited, making readers difficult to get to the point. 
The contributions are quite scattered. 
There are errors in the presentation.

There are many questions and problems on this paper. 
(1) Motivation is not straightforward. More specifically, the relation between self-labeling and dual-level representation is not clear. It seems that this study addresses two individual problems of the point-wise clustering method. The background of the point-wise clustering should be more informative to improve the readability. 
(2) I am not quite sure what the "degenerate solution" means for the point-cloud segmentation. It is also quite unclear why we need a semi-relaxed optimal transport problem definition from the introduction. What is the role of data-dependent annealing in the self-labeling process and dual-level representation? This is also not clear in the introduction. 
(3) For the Figure 1, the presentation is quite confusing, and there are even errors. For example, what do different colors represent? Which component represents the novel pseudo-label generation process? Where is the dual-level representation? The arrows among p and y on the right-most part of the figure are quite difficult to understand as well. The "Encoder f_theta" has been occluded...
(4) In the experiment, especially Table 4, I found that the "Region" design only makes a minor contribution to the final performance, while the "dual-representation" is one of the major claimed contributions, making me feel that this paper is quite scattered. There is not a clear focus on tackling a specific problem, making me quite doubtful about the contribution of this paper. I agree that the studied topic is of great importance, but I believe the paper requires thorough refinement before publication.

### Questions
There are many questions and problems on this paper. 
(1) Motivation is not straightforward. More specifically, the relation between self-labeling and dual-level representation is not clear. It seems that this study addresses two individual problems of the point-wise clustering method. The background of the point-wise clustering should be more informative to improve the readability. 
(2) I am not quite sure what the "degenerate solution" means for the point-cloud segmentation. It is also quite unclear why we need a semi-relaxed optimal transport problem definition from the introduction. What is the role of data-dependent annealing in the self-labeling process and dual-level representation? This is also not clear in the introduction. 
(3) For the Figure 1, the presentation is quite confusing, and there are even errors. For example, what do different colors represent? Which component represents the novel pseudo-label generation process? Where is the dual-level representation? The arrows among p and y on the right-most part of the figure are quite difficult to understand as well. The "Encoder f_theta" has been occluded...
(4) In the experiment, especially Table 4, I found that the "Region" design only makes a minor contribution to the final performance, while the "dual-representation" is one of the major claimed contributions, making me feel that this paper is quite scattered. There is not a clear focus on tackling a specific problem, making me quite doubtful about the contribution of this paper. I agree that the studied topic is of great importance, but I believe the paper requires thorough refinement before publication.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
