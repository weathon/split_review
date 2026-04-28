# Learning Structured Universe Graph with Outlier OOD Detection for Partial Matching

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 5, 8, 5, 6

## Abstract
Partial matching is a kind of graph matching where only part of two graphs can be aligned. This problem is particularly important in computer vision applications, where challenges like point occlusion or annotation errors often occur when labeling key points.  Previous work has often conflated point occlusion and annotation errors, despite their distinct underlying causes. We propose two components to address these challenges: (1) a structured universe graph is learned to connect two input graphs $X_{ij} = X_{iu} X_{ju}^\top$, effectively resolving the issue of point occlusion; (2) an energy-based out-of-distribution detection is designed to remove annotation errors from the input graphs before matching. We evaluated our method on the Pascal VOC and Willow Object datasets, focusing on scenarios involving point occlusion and random outliers. The experimental results demonstrate that our approach consistently outperforms state-of-the-art methods across all tested scenarios, highlighting the accuracy and robustness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel approach for partial graph matching. The proposed method introduces a complete and universal graph as the complete set for all the cases. By decomposing the one step matching problem into two steps: First, matching with the universal graph. Then filter out the outliers and match the second time. The proposed method achieve robust and accurate matching results. The proposed method is validated on several popular benchmarks.

### Strengths
1. The proposed latent universal graph is novel and effectiveness.

### Weaknesses
1. The proposed method can only be applied in closed set problem. It is not a general graph matching solver. Though introducing the class embedding, it cannot generalize to unseen class in inference time.
2. How to define the OOD data in eqn.9? If we can see the OOD data in training, how can they treat as OOD? Does the method generalize well to indeed OOD data (not seen in training)?

### Questions
1. EdgeID in eqn.6 needs to be defined.
2. It is not clear how eqn.4 is applied in generating GT for X_{iu}. First, the number of nodes in universal graph is larger the N, then the factorization is not unique, which one to pick? Second, X^{GT} is in {0, 1}. It is not clear X_{u} is continuous or discrete. If it is continuous, in eqn.6, the authors choose argmax as the label, does this approximation affect the performance?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes Latent Universe Graph Learning and out-of-distribution detection for point occlusion and annotation error in graph matching problems. The paper evaluates the proposed method on the Pascal VOC and Willow Object datasets. The method achieves SOTA performance and the ablation study shows the components are effective.

### Strengths
- The motivation is good. The proposed method can be easy to follow because of the intuitive motivation.
- The paper is well-written, clear, and full of details.
- SOTA performance and good ablation studies.

### Weaknesses
 - No qualitative results are provided. Especially for the represented successful cases that cannot be solved in the baseline method. Besides, as mentioned in discussion subsection, some failure cases should be shown to let the readers better understand the margin of the proposed method.

### Questions
See weaknesses above. My main concerns are about the experiments.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a method to match graphs with a mechanism to deal with outliers (i.e., query nodes w/o an actual matching reference node). The proposed approach learns embeddings for both nodes and edges and uses supervised learning via affinity matrices. To deal with outliers, the proposed method calculates an energy based on the affinity scores to filter out query nodes w/o matching reference nodes. The paper presents experiments on visual semantic matching using Pascal VOC and Willow Object datasets where the proposed method often outperforms baseline methods.

### Strengths
1. The proposed approach considers both nodes and edge information in the graph. In its presentation, it looks like a general formulation. I think this is interesting as edges can help the matching process in many aspects.
2. The mechanism to deal with outliers is needed given that in practice they occur very often and can decrease performance in a considerable manner.

### Weaknesses
1. Clarity of the approach is poor. The most important weakness is the presentation of the proposed approach in Section 3.1. This lowers the chances of the proposed approach to reproduce the results. First, there is no high-level description of the proposed approach, and as a reader we have to figure out from the mathematical description and non-informative narrative. For instance, in line 197, the term “ground truth universe matching” and symbol X^gt_iu is never properly defined, and ultimately the paragraph says that it uses ground truth pairwise matching X^gt_ij. Second, lines 224-227 states that “keypoints from different categories are mapped to the same universe node”. I don’t think this makes sense, because this will make the network confuse categories. Right? Lastly, it is also unclear why an attention-based approach could not be used. Attention can be useful also in rejecting outliers. In fact there are previous approaches derived for feature matching (e.g., LoFTR [C]).

2. The proposed formulation requires the use of class information. This prevents the generalization to other matching problems (e.g., feature matching for geometric problems such as in 3D reconstruction or stereo matching).

3. Outlier detection mechanism is weak. This is because it is based on thresholding the similarity information which can cause it to reject correct matches; consider the case where a wheel from a bike gets confused with a wheel from a car. This mechanism seems to be ad-hoc. Why not learn a function to detect these? I can imagine learning a function that turns off the similarity entry in the affinity matrix. The ground-truth could be easily generated by assigning a node of class A to class B, and perhaps more fruitful if A and B share visual similarities.

4. Experiments are incomplete. First, the experiments are missing recent benchmarks: IMC-PT-SparseGM benchmark [A] and only showing two benchmarks in my opinion falls short of truly showing convincing evidence of the proposed method performance. Second, some of the baselines on the presented benchmarks do not contain the SOTA methods (e.g., [B]) and report different metrics from those reported in [B], where the COMMON method achieves a high accuracy rating on the Willow dataset. Lastly, the ablation studies are quite small. They are missing threshold value performance, m_in, and m_out, as well as temperature T. What values were used for the ablation and experiments?

### Questions
1. What values of temperature, m_in, m_out, and threshold were used for the experiments?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This work proposes a new method for partial matching in graph-based keypoint alignment tasks. It introduces Structured Universe Graph Learning to address point occlusion by linking input pairs through a learned latent graph, leveraging both node features and structural information for enhanced robustness. Additionally, an Energy-based Out-of-Distribution Detection is used to filter out annotation errors before matching, improving quality. Extensive evaluations on the Pascal VOC and Willow Object datasets show that this method outperforms state-of-the-art techniques, especially in challenging scenarios with point occlusion and random outliers, proving its effectiveness and robustness.

### Strengths
1. This work addresses a classic, significant problem in the literature by applying a modern deep-learning approach.

2. The proposed method outperforms both classical and learning-based methods, demonstrating robustness even in the presence of 
outliers and out-of-distribution (OOD) key points.

3. The authors discuss the limitations of their approach.

4. The paper includes ablation studies to analyze the impact of their design choices.

### Weaknesses
1. The paper would benefit from improved writing, particularly in the abstract and introduction, to make it more accessible to readers who are not familiar with this specific problem.

2. While the authors report the F1 score, it would be helpful to include the Accuracy metric, as done in some previous works, for a more comprehensive comparison.

### Questions
Typos:

- The URL paper is mis-cited in line 351/352.

- There is a typo in line 108

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses two key challenges in graph matching: (1) the partial matching problem, where not all nodes are visible in both graphs being matched, and (2) the issue of out-of-distribution outliers. To tackle the first problem, the paper reformulates the matching process between two graphs (A → B) by introducing a universal graph (U), such that matching is performed between each input graph and this universal graph (A → U, B → U). The results are then combined to obtain the final matching (A → B). This approach effectively decomposes the ambiguous partial matching problem into two well-defined subgraph matching tasks. For the second problem, a margin loss is applied to increase the energy distribution difference between in-distribution and out-of-distribution data.

### Strengths
The paper is well-organized, and the concept of a universal graph is intriguing. This approach has the potential to inspire future research in this area.

### Weaknesses
- The universal graph

  The paper states that all input graphs are subsets of the universal graph. However, input graphs could represent different structures, such as those for cars, dogs, and TVs, so how is this ensured? Can authors provide specic details on how the universal graph is consructed to accommodate diverse object categories, including its size and the process of creating ground truth matches between input and the universal graph?

- The generalization issue

  The proposed universal graph is crucial to this method, as its structure is determined by the training data. So it may not generalize well to unseen categories. Please discuss how the method might perform on unseen categories or provide experiments demonstrating its generalization capabilities to new object classes not seen during training.

- In Figure 2, how are the node/edge features extracted from the image feature maps? Maybe the authors should describe it more concretely (step-by-step) for better understanding.

- Could you clarify what EdgeID(0) and EdgeID(1) represent in Equation 6?
- Please add training details in the paper.
- I see codes for the comparative method URL (ICCV23) are available here. https://github.com/XLearning-SCU/2023-ICCV-COMMON

### Questions
Please address my concerns in weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on partial matching problems in computer vision, aiming to address the problems of point occlusion and annotation errors. This paper proposes two components to address these challenges: 1) a structured universe graph is learned to connect two input graphs for point occlusion; 2) an energy-based out-of-distribution detection is designed to remove annotation errors from the input graphs before matching.

### Strengths
1) The paper is well written and the theoretical and experimental analysis is basically complete

2) The paper proposes two novel and effective approaches to address point occlusion and annotation errors in partial matching task

3) The proposed method outperforms state-of-the-art methods, showing the effectiveness and robustness.

### Weaknesses
1) The computational complexity of the algorithm is not compared.

2) The paper lacks the visualization of results, including the visualization of ablation experiments.

3) Universe Graph Matching essentially decomposes the ambiguous partial matching problem into two well-defined subgraph  matching problems. Universe Graph Matching can better deal with the occlusion phenomenon, but for the general situation, whether the matching accuracy will be improved. It might be better to do an analysis.

### Questions
1) The computational complexity of the algorithm is not compared.

2) The paper lacks the visualization of results, including the visualization of ablation experiments.

3) Universe Graph Matching essentially decomposes the ambiguous partial matching problem into two well-defined subgraph  matching problems. Universe Graph Matching can better deal with the occlusion phenomenon, but for the general situation, whether the matching accuracy will be improved. It might be better to do an analysis.

4) Limitations and future work are not discussed.

### Soundness
3

### Presentation
3

### Contribution
2
