# Adaptive Self-training Framework for Fine-grained Scene Graph Generation

- Decision: Accept
- Scores: 6, 8, 5

## Abstract
\looseness=-1
Scene graph generation (SGG) models have suffered from inherent problems regarding the benchmark datasets such as the long-tailed predicate distribution and missing annotation problems. In this work, we aim to alleviate the long-tailed problem of SGG by utilizing unannotated triplets. To this end, we introduce a \emph{Self-Training framework for SGG} (\proposed) that assigns pseudo-labels for unannotated triplets based on which the SGG models are trained. While there has been significant progress in self-training for image recognition, designing a self-training framework for the SGG task is more challenging due to its inherent nature such as the semantic ambiguity and the long-tailed distribution of predicate classes.
Hence, we propose a novel pseudo-labeling technique for SGG, called \emph{Class-specific Adaptive Thresholding with Momentum} (\proposedmethod), which is a model-agnostic framework that can be applied to any existing SGG models. Furthermore, we devise a graph structure learner (GSL) that is beneficial when adopting our proposed self-training framework to the state-of-the-art message-passing neural network (MPNN)-based SGG models. Our extensive experiments verify the effectiveness of~\proposed~on various SGG models, particularly in enhancing the performance on fine-grained predicate classes

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed the ST-SGG framework to address the long-tailed predicate issue in Scene Graph Generation (SGG). It incorporates the CATM pseudo-labeling method and a Graph Structure Learner (GSL). Experimental results confirm improved performance on fine-grained predicate classes.

### Strengths
- ST-SGG serves as a model-agnostic framework, meaning it can be applied to various existing SGG models. This aspect has the potential to expand the applicability of the self-training in SGG.
- Based on experimental results, the proposed framework seems to effectively alleviate the issues of long-tailed distribution. The performance improvements are primarily concentrated on fine-grained predicate classes.

### Weaknesses
- In some experiments, the R@k values significantly decreased after employing the proposed framework. The paper lacks some explanations for this phenomenon.
- There's a concern if the proposed framework might, in some scenarios, sacrifice a considerable amount of overall performance to achieve improvement in fine-grained predicates.
- The paper lacks a clear depiction of the overall framework structure. Please clearly demonstrate how the different components interact and how pseudo-labels are generated and applied.

### Questions
See the Weaknesses.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a novel self-training algorithm of training scene graph models based on un-annotated triplet loss. The distinction between un-annotated and background relationship class is drawn with the help of a class-specific dynamic threshold. Proposed method has been validated in Visual Genome dataset with two classic SGG baseline (MOTIF and VCTREE) and with four recent-most SGG baselines (Resam. IT-SGG, BGNN, and HetSGG). Proposed method increases the performance of the minority classes with slight decrease of majority classes.

### Strengths
This paper has the following strengths

**1. Well-motivated:** The paper's motivation is well-stated and clearly disseminated to the reader. Exploring vast un-annotated triplets in the image databases is one of the desired direction of open-set annotation dataset and Visual Genome is one of the most useful resources for conducting such exploration. This paper successfully established this motivation in their introduction. 

**2. Novel self-training loss:** The proposed simple yet novel and effective loss is one of the major strengths of the paper. The discussion regarding challenges of fixed-threshold based distinction between background class and un-annotated class is interesting and highly relevant. The proposed class-specific thresholding solves the problem efficiently and demands further exploration. 

**3. Less worsening of majority classes:** Traditional debiasing schemes of SGG usually hurt the recall classes significantly while improving the minority classes. However, this paper hurts the recall minimally, especially with the baseline MOTIF and VCTree. 

**4. Detailed ablation study on thresholding:** Since the main contribution of this paper is a threshold-based self-training algorithm, authors have performed detailed analysis on how to choose appropriate threshold.

### Weaknesses
This paper has the following weaknesses

**1. Comparison with other debiasing methods missing.** The paper demonstrated that their method can improve the diversity of the baseline models. However, such improvement of baseline models is prevalent in SGG literature now. Therefore, a direct comparison with other debiasing methods would shed light more on their performances. For example,  VCTree+ST-SGG should be compared with VCTree+Resample. With that comparison, the readers would have better understanding of their methods performance. 

**2. Zero-shot evaluation missing.** Since unannotated triplets are being accounted in the training, this method might improve the zero-shot performance of the baseline model as well. A separate study with zero-shot evaluation would strengthen the claim of the paper.

### Questions
The authors determine the threshold in an object-agnostic fashion considering only the relationship classes. However, the same relationship label has different semantic meaning to different pair and therefore an object-conditional viewpoint of relationship distribution may improve the result more. 

To clarify more, in the loss calculation phase, if we consider the viability of a prediction conditioned on its object, we might have better choice on the threshold. For example, the prediction probability of 'on' will be higher for 'building-window' pair, however, it will be extremely low for 'man-pizza' pair. Is it possible to use such commonsense knowledge in the threshold choice of the loss equation?

**Post-rebuttal rating:** My concerns and queries have been properly addressed and therefore, I keep my original rating of 8.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a self-training framework for the SGG task, which uses the unannotated triplets for imbalanced SGG. With the class-specific adaptive thresholding with momentum algorithm, their model can obtain some pseudo labels to deal with the missing annotations problem. Finally, they verify the effectiveness of ST-SGG on VG and OI-V6 datasets.

### Strengths
1. The idea is well-motivated and intuitive. They provide an in-depth analysis of long-tailed SGG.
2. The paper is well written and easy to understand.
3. Extensive experiments and ablations verify the effectiveness of enhancing the performance of tail classes.

### Weaknesses
1.The technical contribution of this paper might be limited. The self-training framework is used for image classification, the adaptive thresholding is used to obtain accurate pseudo labels in many tasks, and the GSL is also not new. The authors should take more discussion about their novelty and variant in SGG.

2.There are some SOTA SGG methods which might get higher performance than this paper. These methods should also be included for comparisons and analyses, such as VETO[1], GCL[2], PE-Net-Reweigh[3], and so on.
[1] Vision Relation Transformer for Unbiased Scene Graph Generation, ICCV2023.
[2] Stacked Hybrid-Attention and Group Collaborative Learning for Unbiased Scene Graph Generation, CVPR 2022.
[3] Prototype-based Embedding Network for Scene Graph Generation, CVPR 2023.

### Questions
See Strengths and Weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
