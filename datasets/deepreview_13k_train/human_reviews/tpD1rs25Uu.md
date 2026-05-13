# Hydra-SGG: Hybrid Relation Assignment for One-stage Scene Graph Generation

- Decision: Accept
- Scores: 5, 6, 8

## Abstract
DETR introduces a simplified one-stage framework for scene graph generation (SGG). However, DETR-based SGG models face two challenges: \textbf{i) Sparse supervision}, as each image typically contains fewer than 10 relation annotations, while the models employ over 100 relation queries. This sparsity arises because each ground truth relation is assigned to only one single query during training. \textbf{ii) False negative samples}, since one ground truth relation may have multiple queries with similar matching scores. These suboptimally matched queries are simply treated as negative samples, causing the loss of valuable supervisory signals. As a response, we devise Hydra-SGG\footnote{Hydra is an abbreviation for ``\textbf{Hy}bri\textbf{d} \textbf{R}elation \textbf{A}ssignment". The name is chosen because it reflects the multi-branch structure of our model, which resembles the multiple heads of the Hydra in Greek mythology.}, a one-stage SGG method that adopts a new Hybrid Relation Assignment. This assignment combines a One-to-One Relation Assignment with a newly introduced IoU-based One-to-Many Relation Assignment. Specifically, each ground truth is assigned to multiple relation queries with high IoU subject-object boxes. This Hybrid Relation Assignment increases the number of positive training samples, alleviating sparse supervision. Moreover, we, for the first time, empirically show that self-attention over relation queries helps reduce duplicated relation predictions. We, therefore, propose Hydra Branch, a parameter-sharing auxiliary decoder without a self-attention layer. This design promotes One-to-Many Relation Assignment by enabling different queries to predict the same relation. Hydra-SGG achieves state-of-the-art performance with \textbf{10.6} mR@20 and \textbf{16.0} mR@50 on VG150, while only requiring \textbf{12} training epochs. It also sets a new state-of-the-art on Open Images V6 and GQA.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The manuscript introduces Hydra-SGG, a novel one-stage Scene Graph Generation (SGG) method designed to address the challenges of sparse supervision and false negative samples inherent in DETR-based SGG models. The authors propose a Hybrid Relation Assignment strategy that combines One-to-One and IoU-based One-to-Many Relation Assignments to increase positive training samples and mitigate sparse supervision issues. Additionally, the paper introduces Hydra Branch, an auxiliary decoder without self-attention layers, to enhance the One-to-Many Relation Assignment by promoting duplicate relation predictions among different queries. The model achieves state-of-the-art performance on multiple datasets, including VG150, Open Images V6, and GQA, with a significant reduction in training epochs compared to previous methods.

### Strengths
**1.Clear Explanation of Methodology:** The paper does an excellent job of explaining the methodology in a step-by-step fashion. The One-to-One Assignment, One-to-Many Assignment, and HydraBranch are each discussed with sufficient detail, making it easier for readers to follow the technical contributions. Furthermore, the inclusion of pseudocode and diagrams helps clarify how each component interacts within the framework.

**2.Comprehensive Experimental Validation:** The paper provides extensive experiments on two widely-used datasets, Visual Genome, OpenImage, GQA, and demonstrates that Hydra-SGG, consistently outperforms existing baselines. The authors also conduct detailed ablation studies, examining the impact of various components (Threshold T, Training Epoch, Number of Relation Queries). The results substantiate the claim that the framework is a substantial improvement over current model.

### Weaknesses
 **1.Lack of Novelty:** The motivation and methodology of this work closely resemble those presented in [3], raising questions about its originality and distinct contributions. In particular, [3] introduced the one-to-many relation query matching technique, known as Quality-Aware Multi-Assignment, which enhances training efficiency by allowing a single ground truth (GT) to correspond to multiple sufficiently close predictions or queries. While this work makes a slight modification by removing self-attention among relation queries, this adjustment alone does not constitute a significant advancement in one-stage SGG research. Specifically, the core idea of using multiple queries to match a single ground truth relation, and the use of an auxiliary branch to encourage diverse predictions, are both present in [3]. The removal of self-attention, while potentially simplifying the architecture, does not fundamentally alter the underlying approach to relation assignment and training. As a result, it is difficult to regard this work as a notably innovative contribution. Further discussion is warranted to clarify how this work differentiates itself from existing approaches.

**2.Perverse Experimental Results:** The rationale for assigning ground truth (GT) to multiple sub-optimal queries is based on label softening and knowledge distillation. However, applying this approach to scene graph datasets with long-tailed distributions (e.g., Visual Genome, OpenImage, PSG) introduces significant challenges. This method tends to overemphasize common relationships (e.g., on, of, has) in the annotations, which can lead to model overfitting on these frequent relationships. Consequently, this emphasis on common relationships undermines the model’s ability to accurately capture rare relationships (e.g., standing on, walking on, lying on), ultimately lowering average recall performance. Given these limitations, a decline in mRecall performance would be expected for such datasets. Surprisingly, however, the experimental results in Table 1 show the opposite. Since this study does not incorporate any specific solutions to address data imbalance, the observed improvement in mRecall is unexpected. This outcome appears to contradict the foundational assumptions of the proposed Hydra-SGG approach, indicating a need for further analysis.

**3.Inadequate Model Performance:** Despite showing a substantially lower R@100 score than the DSGG method [6], the Hydra-SGG model demonstrates a corresponding improvement in the mR@100 metric. Based on prior research [5], incorporating the F-Recall metric would provide a more comprehensive assessment of Hydra-SGG’s effectiveness relative to state-of-the-art approaches. Additionally, the paper lacks a thorough comparison with other relevant studies [2].

### Questions
please refer to the weakness part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper addresses key challenges in the field of one-stage Scene Graph Generation (SGG), particularly focusing on sparse supervision and false negatives samples.To tackle these challenges, the authors propose two main contributions:
(1) Hybrid Relation Assignment: This method combines One-to-One and One-to-Many Relation Assignment strategies, increasing the number of positive samples during training and thus enhancing supervision.
(2) Hydra Branch: An auxiliary decoder branch without self-attention layers, designed to further support the One-to-Many Relation Assignment by promoting consistent relation predictions across queries.
Above methods jointly improve the training efficacy and performance of DETR-based SGG models, leading to state-of-the-art results on multiple benchmarks with significantly fewer training epochs. Overall, this paper’s motivation is clear, and the proposed method iseffective.

### Strengths
(1) Innovative Method Design: The proposed Hybrid Relation Assignment effectively combines One-to-One and One-to-Many matching strategies. This design helps mitigate the sparse supervision issue in existing methods and improves model convergence speed and learning efficiency.
(2) Efficient Auxiliary Branch: The Hydra Branch supports One-to-Many assignment by promoting consistent relation predictions across queries, all without adding inference-time computational costs. 
(3) Good Experimental Results: The experimental results show that Hydra-SGG achieves state-of-the-art performance across multiple datasets (VG150, Open Images V6, and GQA), reaching these results in significantly fewer training epochs.

### Weaknesses
(1) Lacking theory/analysis, technical solutions appear to be intuitive and empirical. Faster convergence may come from more diverse samples or more training data within an epoch, because the proposed method is likely to give 16 images, but will generate more relation training pairs for training.

(2) Limited Exploration. Why removing Self-Attention benefits the One-to-Many Relation Assignment. The paper introduces the Hydra Branch without self-attention to support the One-to-Many relation assignment. However, the explanation of why removing self-attention aids this assignment is somewhat surface-level, lacking an in-depth analysis of the interaction between self-attention and One-to-Many assignment.

### Questions
Does faster convergence come from more diverse samples or more training data within an epoch, because the proposed method is likely to give 16 images, but will generate more relation training pairs for training?

It would be better to compare the methods with unbiased SGG methods or adopted unbiased strategies, considering the higher performance of mean Recall.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new method called Hydra-SGG for Scene Graph Generation (SGG), which addresses the challenges of sparse supervision and false negatives in one-stage SGG. To this end, it employs a one-to-many assignment strategy and a transformer decoder without self-attention called a hydra-branch. Through comprehensive experiments across various datasets and detailed ablation studies, the paper confirms the efficiency and effectiveness of this method.

### Strengths
1. This paper pinpoints the critical problems in one-stage SGG, which are sparse supervision and false negatives. By addressing this problem, the proposed method is superior on efficiency and effectiveness.
2. The author conducts extensive experiments, including effectiveness on diverse datasets and ablation studies, thereby validating the superiority of the proposed method. Especially, it significantly reduces the training epoch compared to the baselines.
3. The proposed method is simple yet effective.

### Weaknesses
The paper lacks discussion on its limitations and future works.

There are no critical points for rejection.

### Questions
1. While the One-to-Many alignment approach helps mitigate sparse supervision, there is a concern that it may introduce significant noise, potentially leading to an increase in false positives. What are some strategies to manage this noise effectively?
2. How would performances be impacted if the weights for One-to-One and One-to-Many alignment losses were changed? For example, I'm curious how performance would change if the weight of One-to-Many alignment loss were increased or decreased.

### Soundness
4

### Presentation
3

### Contribution
4
