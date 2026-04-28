# On the Cost-Effectiveness of Partially-Annotating Methods for Multi-Label Learning

- Decision: Reject
- Avg Score: 5.50
- Scores: 8, 3, 5, 6

## Abstract
Precisely annotating instances with multiple labels is costly and has emerged as a significant bottleneck in the real-world multi-label learning tasks. To deal with this problem, the most straightforward strategy is partially-annotating, which aims to reduce the cost by annotating only a subset of labels. Existing works mainly includes label-level partially-annotating (LPA), where each instance is assigned a subset of positive labels, and instance-level partially-annotating (IPA), where all positive labels are assigned to an instance, but only a subset of instances are annotated. However, these methods tend to focus on improving model performance under each type of partial annotation, often neglecting a fundamental question: \textit{which method is the most cost-effective?} In this paper, we empirically evaluate which partially-annotating method achieves better model performance at the same annotation cost. To make a fair comparison, we manually annotated images in the MS-COCO dataset using two partially-annotating methods and recorded their averaging annotation time per image. This allows us to train models on two types of partial annotations with the same annotation cost and to compare their performance. Empirical results show that even when the number of examples annotated with IPA is only one-fifth that of LPA, models trained on IPA annotations significantly outperform those trained on LPA annotations, yielding that IPA is significantly more cost-effective than LPA. To explain the superiority of IPA, our causal reasoning framework shows that compared to LPA, IPA preserves complete co-occurrence relationships, enabling the model to capture correlative patterns, which is useful for improving model performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper addresses the challenge of costly and time-consuming annotation in multi-label learning tasks by evaluating the cost-effectiveness of two partially-annotating methods: label-level partially-annotating (LPA) and instance-level partially-annotating (IPA). Through empirical experiments on the MS-COCO dataset, the authors demonstrate that IPA significantly outperforms LPA in terms of model performance, despite requiring fewer annotated instances. The study provides insights into the benefits of preserving co-occurrence relationships in annotations, highlighting that the quality of data can outweigh the quantity in training effective models.

### Strengths
I like this paper. I think this paper effectively underscores "the importance of data quality over quantity in the multi-label learning domain"
, backed by robust experimental design. 

The methodology for comparing partially-annotating methods and the associated annotation costs is well thought out and executed, leading to convincing results that align with the "quality over quantity" insight.

### Weaknesses
More of a discussion point than a weakness. 

While low-quality data generally yields subpar results, previous work [1,2] has shown that large-scale partially-annotated datasets can be created without annotation costs from image-text pairs, leading to strong generalization (zero-shot performance). Consequently, pretraining on such large-scale partially-annotated data followed by fine-tuning on fully-annotated data may be an appropriate approach towards powerful tagging models.

I encourage the authors to consider exploring in the context of such larger dataset settings in future work.

### Questions
No specific questions

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
Becasue fully annotating multi-label datasets is often impractical, this paper focuses on partial annotations. There are two primary types: (1) label-level partially-annotating (LPA), which annotates only a subset of the labels for each instance. (2) instance-level partially-annotating (IPA), which annotates a subset of the instances. This paper empirically evaluates LPA and IPA at the same annotation cost. Extensive experiments indicate that IPA preserves co-occurrence relationships, resulting in better performance.

### Strengths
This paper introduces three distinct variants of LPA, which have different randomness.

This paper compares LPA and IPA, finding that IPA performs better given the same annotation cost.

### Weaknesses
This paper explores two annotation settings that deviate from the mainstream partial multi-label setting. Please see Table 1 of DualCoOp: Fast Adaptation to Multi-Label Recognition with Limited Annotations.

A major issue in partial multi-label is the infeasibility of complete labeling due to the high number of categories, leading to potential omissions and errors. However, IPA annotates all labels for selected images, meaning it does not fully address such issue. Additionally, this work does not introduce a new approach.

Partial multi-label settings extend beyond LPA and IPA. Most mainstream methods annotate only a subset of labels per image, a topic this study does not discuss or analyze.

Table 1 should include fully labeled experimental results.

The benchmark used is limited. commonly datasets like VOC, NUSWIDE, and CUB should be included for comparison.

### Questions
Please see the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper compares label-level partial annotation (LPA) and instance-level partial annotation (IPA) in multi-label learning tasks to determine which is more cost-effective. The authors manually annotated MSCOCO images using both methods and found that IPA, despite annotating fewer examples, yielded significantly better model performance than LPA. The paper suggests IPA's superiority is due to its preservation of label co-occurrence relationships, which helps models capture correlative patterns.

### Strengths
1. The study of the cost-effectiveness of different labeling methods sounds quite interesting and has significant guidance and meaning for industry applications.

2. The experimental results are relatively comprehensive.

### Weaknesses
1. The paper only discusses two labeling methods. Can other labeling methods be included for discussion, such as in reference [1]?

2. LPA adopts a single positive label labeling method, which is not the traditional partial label setting [2]. If it were the traditional partial label setting which is more practical than the single positive label setting, would the analysis and conclusions of this paper still hold?

3. Defining the cost of different labeling methods is highly uncertain because, in the actual labeling process, in addition to process design, the proficiency and fatigue level of the labelers must also be considered, which can cause uneven costs. How did the authors consider this issue?

### Questions
See the weakness above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Unlike existing studies, the authors explore an intriguing question in multi-label learning: should we partially annotate at the label level or the instance level? Through extensive experiments and a proposed causal reasoning framework, they demonstrate that instance-level partial annotation (IPA) maintains complete co-occurrence relationships, which proves more beneficial for enhancing multi-label regression (MLR) model performance compared to label-level partial annotation (LPA).

### Strengths
1. This work offers a compelling and important motivation, providing essential guidance for future multi-label regression (MLR) research.
2. A comprehensive analysis of extensive experimental results reveals the underlying reasons in detail.

### Weaknesses
1. The discussion of MLR-PL is not sufficient, ignoring some recent work (e.g., SARB[1], DualCoOp++[2], HST[3]).
2. Comparison algorithms are somehow outdated.

### Questions
1. Do the paper's conclusions still apply to other contemporary algorithms, e.g., SARB[1], DualCoOp++[2], HST[3]?

### Soundness
3

### Presentation
3

### Contribution
3
