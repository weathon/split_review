# Text-Based Person Search in Full Images via Semantic Context Disentangling and Prototype Learning

- Decision: Reject
- Avg Score: 2.50
- Scores: 3, 3, 3, 1

## Abstract
Text-based Person Search (TBPS) in full images aims to locate a target pedestrian within uncropped images based on natural language descriptions. Existing TBPS methods typically rely on candidate region generation and cross-modal matching. However, in complex scenes,especially those with multiple pedestrians in the image.It is often challenging to distinguish the target pedestrian from the background or other individuals. This leads to limited generalization capabilities.
 To address these issues, we propose a new TBPS framework named ProtoDis-TBPS, which integrates three key components: Semantic Context Decoupling (SCD), Prototype Embedding Learning (PEL), and a Cross-modal Person Re-identification (ReID) module. Specifically, SCD enhances cross-modal feature discrimination by separating background and irrelevant contextual information. PEL improves the model's robustness in complex scenes by learning prototype features for pedestrian categories. Finally, the ReID module, based on a Transformer architecture, further boosts the accuracy of both text-based pedestrian detection and re-identification in full images.Experiments demonstrate that our proposed method presents a significant challenge to existing approaches in this field.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on tackling the problem of cluttered backgrounds/multiple pedestrians in TBPS, which have been considered by a few works. To solve this problem, the authors propose an end-to-end learning framework named ProtoDis-TBPS, which integrates three key components: Semantic Context Decoupling (SCD), Prototype Embedding Learning (PEL), and a Cross-modal Person Re-identification (ReID) module.
However, the solution lacks innovation and has limited experiments.

### Strengths
The topic is about how to deal with cluttered backgrounds or multiple pedestrians in TBPS, which is worth studying.

### Weaknesses
This work is far from satisfying, especially in the following points:

1. This paper lacks a detailed introduction to the proposed method. The introduction of the proposed modules is so rough that we can get limited information about how it works. Especially the Prototype Embedding Learning (PEL).

2. This paper lacks detailed experiments to demonstrate all these proposed components make sense. There is no ablation study, no comparison, and no discussion in this paper.

3. This paper's performance is far from satisfying. From the only two tables, the performance of this work seems much lower than the recent works~[1].

### Questions
How to understand Table 1 and Table 2?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work improves the text-based person search (TBPS) with three modifications. Firstly, a Semantic Context Decoupling (SCD) module for interaction between the image and text, a Prototype Embedding Learning (PEL) for prototype-based metric learning, and a Cross-modal Person Re-identification (ReID) module for the task. Experimental results only show the final performance of the whole network.

### Strengths
I feel sorry but from my perspective, this is an unfinished work. Even with all of the contributions, there are no experiments to demonstrate they make sense in this topic. So, I can not find something interesting in this paper.

### Weaknesses
This work is far from satisfying, especially in the following points:

1. This paper lacks a detailed introduction to the proposed method. The introduction of the proposed modules is so rough that we can get limited information about how it works. Especially the Prototype Embedding Learning (PEL).

2. This paper lacks detailed experiments to demonstrate all these proposed components make sense. There is no ablation study, no comparison, and no discussion in this paper.

3. This paper's performance is far from satisfying. From the only two tables, the performance of this work seems much lower than the recent works~[1]. 

[1] Zhang, Shizhou, et al. "Text-based person search in full images via semantic-driven proposal generation." Proceedings of the 4th International Workshop on Human-centric Multimedia Analysis. 2023.

### Questions
Please kindly refer to the weakness. In summary, this work at least should add a detailed introduction of each component. How do they work? Detailed experiments to show whether the proposed components make sense also should be added to this paper.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a novel framework named ProtoDis-TBPS for locating a target pedestrian within uncropped images based on natural language descriptions. The framework addresses the challenges of distinguishing the target pedestrian from the background or other individuals in complex scenes, which is a common issue in Text-based Person Search (TBPS). ProtoDis-TBPS integrates three key components: Semantic Context Decoupling (SCD), Prototype Embedding Learning (PEL), and a Cross-modal Person Re-identification (ReID) module. SCD enhances feature discrimination by separating background and irrelevant information, PEL improves model robustness by learning prototype features for pedestrian categories, and the ReID module, based on a Transformer architecture, boosts the accuracy of text-based pedestrian detection and re-identification.

### Strengths
1. The paper introduces a new end-to-end learning framework for TBPS in full images.
2. The proposed method specifically targets the challenge of distinguishing the target pedestrian in scenes with multiple pedestrians and complex backgrounds, which is a significant advancement over existing methods.

### Weaknesses
1. The introduction to each part is so concise that it is hard not to doubt the author's attitude.
2. The introduction of each module of the proposed method is too brief. It should be clear how to do it, why to do it, and why it is effective. The appendix in the current version is unnecessary and should be integrated into the main text.
3. The experimental section mentions comparison with other methods, where are the comparison results?
4. Insufficient experiments. There is a lack of ablation studies to demonstrate the effect of each module.

### Questions
Please see Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper presents a novel framework called ProtoDis-TBPS, which integrates three core components: Semantic Context Decoupling (SCD), Prototype Embedding Learning (PEL), and a Cross-modal Person Re-identification (ReID) module. Specifically, SCD enhances cross-modal feature discrimination by separating background and irrelevant contextual information, while PEL learns prototype features for pedestrian categories to aid the inference process. Moreover, the ReID module supervises the prediction of bounding boxes and IDs, as well as the extraction of pedestrian features.

### Strengths
The paper is well-structured, with clear and coherent logic, and appropriate use of methodologies. It innovatively proposes three modules that progressively address the challenges of TBPS, starting from separating background and irrelevant information, to integrating features and prototype extraction, and finally to supervising the prediction results.

### Weaknesses
1. The paper falls short of the required page count, with the main text comprising less than 4 pages, while the submission guidelines require 6-10 pages.
2. The proposed method is not compared with existing approaches. Current state-of-the-art (SOTA) performance on the PRW-TBPS and CUHK-SYSU-TBPS datasets stands at 22.17% mAP and 36.78% Rank-1, and 59.62% mAP and 55.35% Rank-1, respectively (MACA: Memory-aided Coarse-to-fine Alignment for Text-based Person Search). In contrast, the proposed method achieves only 5.43% mAP and 4.10% Rank-1 on PRW-TBPS, and 6.45% mAP and 14.48% Rank-1 on CUHK-SYSU-TBPS, which is significantly lower than the SOTA performance.
3. The paper lacks clarity in several key details. For instance, the specific structures of PrototypeExtractor (PE) and Bounding Box Prediction Module (BBP) are not clearly described, and the formulas for the various loss functions are also missing.
4. The paper lacks ablation studies for its components and does not include experiments analyzing the impact of hyperparameters.

### Questions
Why does this paper fail to meet the mandatory page count requirement, and why is the performance in the experimental section so poor, with low results and no comparison to existing methods?

### Soundness
1

### Presentation
2

### Contribution
1
