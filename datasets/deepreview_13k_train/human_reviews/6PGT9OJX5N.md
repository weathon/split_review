# Noisy Data Pruning by Label Distribution Discrimination

- Decision: Reject
- Scores: 5, 3, 3, 1

## Abstract
Data pruning aims to prune large-scale datasets into concise subsets, thereby reducing computational costs during model training.
While a variety of data pruning methods have been proposed, most focus on meticulously curated datasets, and relatively few studies address real-world datasets containing noisy labels. In this paper, we empirically analyze the shortcomings of previous gradient-based methods, revealing that geometry-based methods exhibit greater resilience to noisy labels. Consequently, we propose a novel two-stage noisy data pruning method that incorporates selection and re-labeling processes, which takes into account geometric neighboring information. Specifically, we utilize the distribution divergence between a given label and the predictions of its neighboring samples as an importance metric for data pruning. To ensure reliable neighboring predictions, we employ feature propagation and label propagation to refine these predictions effectively. Furthermore, we utilize re-labeling methods to correct selected subsets and consider the coverage of both easy and hard samples at different pruning rates. Extensive experiments demonstrate the effectiveness of the proposed method, not only on real-world benchmarks but also on synthetic datasets, highlighting its suitability for practical applications with noisy label scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studied a task combination of label noise and core-set selection. The proposed method, RoP, is a graph-like sample selection strategy that integrates feature propagation and label propagation. The experiment is extensive.

### Strengths
- Introduces an innovative NLI-Score for identifying noisy samples by leveraging neighboring sample consistency.  
- Combines feature and label propagation effectively to reduce selection bias in noisy data scenarios.

### Weaknesses
 - The presentation of this paper is poor according to the following aspects:
  - Lacking in-depth analysis of the difference between the proposed method and previous SOTA Pr4ReL, since Pr4ReL also follows a selection and relabeling paradigm and uses neighborhood information. It is important to explain the superiority of the proposed method. Also, authors are encouraged to add noisy data pruning methods in the section of related work.
  - The motivation for feature propagation and label propagation is unclear. Besides, what if directly applying label propagation without feature propagation?
- Line 237 mentions that a model is required to be trained on the noisy label datasets. Since the purpose of dataset pruning is to reduce the training cost, is it reasonable and fair to access the trained model? If so, please refer to some related works.
- The process of pruning and re-labeling actually follows existing works, i.e., a SOTA noisy label learning method SOP+ and Coverage Coreset Sampling strategy, limiting the novelty of the proposed method.
- Typo: In line 309 "retaining retaining"

### Questions
see weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors propose a novel geometry-based noisy data pruning method. It consists of two stages and uses feature propagation and label propagation for reliable neighboring predictions. Experiments demonstrated quite good results.

### Strengths
- It proposes a novel two-stage noisy data pruning method.
- It employs novel feature propagation and label propagation to refine neighboring predictions.

### Weaknesses
1. I find this paper completely unoriginal; it merely applies existing techniques from the noisy label learning task to the domain of data pruning. The "FEATURE PROPAGATION" proposed by the authors is present in many works on noisy label learning [1-4]. The authors additionally utilize Equation 5, which involves fusing a sample's own features with those of surrounding samples to improve its own features; however, this may not be very meaningful. Many studies have shown that, in noisy label learning, while model predictions may be misled by noisy labels, the learned features tend to remain reliable. The "LABEL PROPAGATION" proposed by the authors is also found in many works on noisy label learning [5-6]. For the re-labeling part, the authors even explicitly mention using the existing state-of-the-art method, SOP+.

2. Why are methods related to noisy label learning not compared in the experiments? Many existing methods can be easily adapted to the scenarios presented in this paper.

### Questions
- It’s hard to understand the so-called “intuitive method” in line 70: Since the clean samples are found in the first stage, why do you need to relabel them?
- Are the gradient-based method in line 15 and the loss-based method in line 51 the same thing?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies the problem of noisy data pruning which aims to prune noisy large-scale datasets into concise subsets. The authors first reveal that geometry-based methods exhibit greater resilience to noisy labels compared to gradient-based methods. Then, a discrimination, pruning, and re-labeling method is proposed to conduct noisy data pruning. Specifically, noisy label discrimination is achieved by neighborhood label inconsistency estimation, after feature and label propagation. Then, the pruned set is selected by ensuring coverage on both easy and hard samples. Finally, re-labeling is achieved by SOTA noisy label learning methods. Experiments show the effectiveness of the proposed method.

### Strengths
- This paper addresses the issue of noisy data pruning, which is crucial in real-world applications.
- The proposed method achieves SOTA results against existing baselines.

### Weaknesses
- The presentation of this paper is poor according to the following aspects:
  - Lacking in-depth analysis of the difference between the proposed method and previous SOTA Pr4ReL, since Pr4ReL also follows a selection and relabeling paradigm and uses neighborhood information. It is important to explain the superiority of the proposed method. Also, authors are encouraged to add noisy data pruning methods in the section of related work.
  - The motivation for feature propagation and label propagation is unclear. Besides, what if directly applying label propagation without feature propagation?
- Line 237 mentions that a model is required to be trained on the noisy label datasets. Since the purpose of dataset pruning is to reduce the training cost, is it reasonable and fair to access the trained model? If so, please refer to some related works.
- The process of pruning and re-labeling actually follows existing works, i.e., a SOTA noisy label learning method SOP+ and Coverage Coreset Sampling strategy, limiting the novelty of the proposed method.
- Typo: In line 309 "retaining retaining"

### Questions
In line 250, how to get the ground-truth label of the sample?

### Soundness
2

### Presentation
1

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
This paper introduces a novel two-stage robust data pruning method (RoP) aimed at datasets with noisy labels. The first stage identifies clean samples using a Neighborhood Label Inconsistency Score (NLI-Score), followed by a second stage that re-labels the selected samples. RoP employs feature and label propagation to enhance the accuracy of neighboring predictions and uses density-based coverage sampling to balance the number of easy and hard samples across different pruning rates. Extensive experiments demonstrate the effectiveness of RoP on both synthetic noisy datasets and real-world benchmarks.

### Strengths
1. The paper is well-organized, with clear presentations of methodology, experiments, and conclusions that effectively guide the reader through the research.

2. The authors conduct extensive experiments across various datasets, including real-world noisy datasets and synthetic noise datasets, which helps to validate the robustness and applicability of the method.

### Weaknesses
1. I find this paper completely unoriginal; it merely applies existing techniques from the noisy label learning task to the domain of data pruning. The "FEATURE PROPAGATION" proposed by the authors is present in many works on noisy label learning [1-4]. The authors additionally utilize Equation 5, which involves fusing a sample's own features with those of surrounding samples to improve its own features; however, this may not be very meaningful. Many studies have shown that, in noisy label learning, while model predictions may be misled by noisy labels, the learned features tend to remain reliable. The "LABEL PROPAGATION" proposed by the authors is also found in many works on noisy label learning [5-6]. For the re-labeling part, the authors even explicitly mention using the existing state-of-the-art method, SOP+. 

2. Why are methods related to noisy label learning not compared in the experiments? Many existing methods can be easily adapted to the scenarios presented in this paper.

[1] Multi-Objective Interpolation Training for Robustness to Label Noise. CVPR 2021

[2] Selective-Supervised Contrastive Learning with Noisy Labels. CVPR 2022

[3] RankMatch: Fostering Confidence and Consistency in Learning with Noisy Labels. ICCV 2023

[4] Learning with Neighbor Consistency for Noisy Labels. CVPR 2024

[5] Jo-SRC: A Contrastive Approach for Combating Noisy Labels. CVPR 2021

[6] UNICON: Combating Label Noise Through Uniform Selection and Contrastive Learning. CVPR 2022

### Questions
See weaknesses.

### Soundness
1

### Presentation
2

### Contribution
1
