# Fisher-aware Quantization for DETR Detectors with Critical-category Objectives

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
The impact of quantization on the overall performance of deep learning models is a well-studied problem. However, understanding and mitigating its effects on a more fine-grained level is still lacking, especially for harder tasks such as object detection with both classification and regression objectives. This work defines the performance for a subset of task-critical categories i.e. the critical-category performance, as a crucial yet largely overlooked fine-grained objective for detection tasks. We analyze the impact of quantization at the category-level granularity, and propose methods to improve performance for the critical categories. Specifically, we find that certain critical categories have a higher sensitivity to quantization, and are prone to overfitting after quantization-aware training (QAT). To explain this, we provide theoretical and empirical links between their performance gaps and the corresponding loss landscapes with the Fisher information framework. Using this evidence, we apply a Fisher-aware mixed-precision quantization scheme, and a Fisher-trace regularization for the QAT on the critical-category loss landscape. The proposed methods improve critical-category metrics of the quantized transformer-based DETR detectors. They are even more significant in case of larger models and higher number of classes where the overfitting becomes more severe. For example, our methods lead to 10.4\% and 14.5\% mAP gains for, correspondingly, 4-bit DETR-R50 and Deformable DETR on the most impacted critical classes in the COCO Panoptic dataset.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work investigated the impact of quantization on the fine-grained critical-category performance
of DETR-based object detectors.
This work formulated the critical performance via the logit-label transformation of the corresponding categories.

### Strengths
This work found that both the conventional PTQ and QAT cause disparate quantization effects on such critical performance.
They theoretically linked the disparate quantization effects with the sensitivity of critical objectives to the quantization weight perturbation and the sharpness of the critical loss landscape in the QAT.
This paper proposed the Fisher-aware mixed-precision quantization scheme and Fisher-trace regularization to improve the critical performance of interest.

### Weaknesses
 -- The performance improvements are marginal, as shown inTab. 3 and Tab. 4.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
• The paper formulates the critical-category performance for object detection applications and observe
disparate effects of quantization on the performance of task-critical categories.

• The paper provides analytical explanations of the quantization effects on critical-category performance for DETR-based models using a theoretical link to the Fisher information matrix.

• The paper proposes a Fisher-aware mixed-precision quantization scheme that considers the sensitivity
of critical-category objectives and improves corresponding detection metrics.

• The paper proposes Fisher-trace regularization for the loss landscape of our objectives during
quantization-aware training to further improve critical-category results.

### Strengths
1. The writing of the article meets academic standards;

2. Clear motivation;

3. Strong mathematical analysis

### Weaknesses
1. Lack of references to relevant studies

2. There are too few comparisons with other papers

### Questions
1. Are you the first to conduct this research? As far as I know Q-DETR （CVPR2023) is the first paper about QUANTIZATION FOR DETR. However, your research contents are different. Q-DETR focuses on how to enhance the performance of quantized DETRs. You focus on  CRITICAL-CATEGORY OBJECTIVES. I think you should cite Q-DETR.

2. I think you should compare it to Q-DETR. Q-DETR's model has been released on Git Hub. Although you are different, I think you are comparable.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors first argure that rather than the overall performance, the fine-grained critical-category performance should be more focused during quantization. They then link the fine-grained critical-category performance with the Fisher information and propose to perform quantization in a Fisher-information aware manner.

### Strengths
1. The problem that this paper points out seems to be reasonable and interesting.

2. The paper is easy to follow.

### Weaknesses
1. My major concern w.r.t. this paper is that, while I agree on the importance of the proposed problem that we should particularly focus on certain classes instead of all classes, I feel that this can be achieved in many ways. For example, during training, one can particularly control the loss weight for certain particular classes. Moreover, during quantization, one can perform input-aware bit assignment [1] to set higher bit for images in which critical classes are hardly distinguishable and lower bit for other images. Thus, while I admit that the Fisher information can be a feasiable perspective, I hope that the authors can discuss more on its advantages over other seems feasible ways.

[1] Instance-Aware Dynamic Neural Network Quantization

2. I am worried on the generalizability of the proposed method. On the one hand, in real-life scenarios, there are often cases that the user only know that there is an object detector but does not know that whether the object detector is based on DETR or based on other object detectors. Thus, if this method can only be used on DETR, this can limit its generalizability and usage. On the other hand, the observation and demonstration in this paper seem to be focus on COCO, which can also be limited especially when this paper emphasize on its solving of real-world problem. I guess a real-world problem can only be regarded as well-solved if it can be solved in a rather general manner.

3. The last concern I have is w.r.t. the experiment. Specifially, from my perspective, there can exist a mismatch between the experiment and the claim of this paper. In other words, the improvement of Fisher-Critical over Fisher-Overall or even Uniform is often limited. This made me have the feeling that, this paper fails to convince me that it proposes a good method for solving the "the fine-grained critical-category performance" problem.

### Questions
1. My major concern w.r.t. this paper is that, while I agree on the importance of the proposed problem that we should particularly focus on certain classes instead of all classes, I feel that this can be achieved in many ways. For example, during training, one can particularly control the loss weight for certain particular classes. Moreover, during quantization, one can perform input-aware bit assignment [1] to set higher bit for images in which critical classes are hardly distinguishable and lower bit for other images. Thus, while I admit that the Fisher information can be a feasiable perspective, I hope that the authors can discuss more on its advantages over other seems feasible ways.

[1] Instance-Aware Dynamic Neural Network Quantization

2. I am worried on the generalizability of the proposed method. On the one hand, in real-life scenarios, there are often cases that the user only know that there is an object detector but does not know that whether the object detector is based on DETR or based on other object detectors. Thus, if this method can only be used on DETR, this can limit its generalizability and usage. On the other hand, the observation and demonstration in this paper seem to be focus on COCO, which can also be limited especially when this paper emphasize on its solving of real-world problem. I guess a real-world problem can only be regarded as well-solved if it can be solved in a rather general manner.

3. The last concern I have is w.r.t. the experiment. Specifially, from my perspective, there can exist a mismatch between the experiment and the claim of this paper. In other words, the improvement of Fisher-Critical over Fisher-Overall or even Uniform is often limited. This made me have the feeling that, this paper fails to convince me that it proposes a good method for solving the "the fine-grained critical-category performance" problem.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
