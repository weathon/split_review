# IPSeg: Image Posterior Mitigates Semantic Drift in Class-Incremental Segmentation

- Decision: Reject
- Scores: 8, 5, 8, 5

## Abstract
Class incremental learning aims to enable models to learn from sequential, non-stationary data streams across different tasks without catastrophic forgetting. In class incremental semantic segmentation (CISS), the semantic content of the background class changes across incremental phases, which is known as \textbf{semantic drift}. Our research identifies two severe issues within semantic drift: separate optimization and noisy semantics, which significantly degrade CISS performance. Based on this insight, we propose a simple yet effective method, \textbf{I}mage \textbf{P}osterior and Semantics Decoupling for \textbf{Seg}mentation (IPSeg), designed to address these challenges through two specific mechanisms. First, IPSeg leverages image posterior probabilities as guidance to resolve the separate optimization issue. Second, IPSeg utilizes semantics decoupling to effectively handle noisy semantics and tailor the learning strategies for different types of knowledge. Experiment results on the Pascal VOC 2012 and ADE20K datasets demonstrate superior performance compared to previous state-of-the-art approaches, particularly in more realistic and challenging long-term scenarios. Furthermore, IPSeg exhibits excellent properties in terms of both learning plasticity and memory stability.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper indicates two key issues within semantic drift, separate optimization, and noisy semantics, for class-incremental segmentation. The authors propose a method called IPSeg, including image posterior probabilities and semantics decoupling. This paper conducts extensive experiments on replay-based and non-replay-based scenarios and shows significant improvement under extremely long incremental learning steps.

### Strengths
This paper identifies two issues in the semantic drift for class-incremental segmentation and proposes two components for each problem, respectively. Extensive experiments demonstrate the effectiveness of the proposed method.

### Weaknesses
The writing and clarification could be simplified in Section 3.3 and Section 3.4, especially for Equation 5. In Figure 2, the targets of the permanent and temporal branches are not clear.

This paper uses image posterior probability to rectify the class prediction. However, the subnetwork for image-level classification is trainable during different steps. I wonder why the classification subnetwork does not suffer from catastrophic forgetting. Is there any evaluation of the performance of the classification subnetwork during multiple steps?

In Figure 2, the feature extractor is frozen.  What is the pre-trained knowledge of the backbone from, the first training step or the ImageNet?

The mechanism of image posterior probability is similar to the way used in transformer-based mask prediction, like Incrementer [1]. Is there any comparison and discussion with it?

Because this work modifies the inference procedure of the mask, please report the training and inference costs, such as training time and memory.

This method uses salient maps derived from an off-the-shelf model as one of the targets. The salient maps are suitable and useful for the VOC dataset because most objects can be detected by the salient model. However, for the more challenged dataset, ADE20K, many semantic regions can not be identified by the salient model, such as grassland in the supplementary material Figure 9. Please study the effect of the salient maps supervision and the quality of the salient maps on the ADE20K dataset. A suggestion: you may replace the salient maps with the results of the SAM model [2].

In Table 2, why is the replay-based IPSeg (33.6) worse than data-free-based PLOP+NeST (34.8)? Is there any insight or explanation?

### Questions
- This paper uses image posterior probability to rectify the class prediction. However, the subnetwork for image-level classification is trainable during different steps. I wonder why the classification subnetwork does not suffer from catastrophic forgetting. Is there any evaluation of the performance of the classification subnetwork during multiple steps?
- In Figure 2, the feature extractor is frozen.  What is the pre-trained knowledge of the backbone from, the first training step or the ImageNet? 
- The mechanism of image posterior probability is similar to the way used in transformer-based mask prediction, like Incrementer [1]. Is there any comparison and discussion with it? 
- Because this work modifies the inference procedure of the mask, please report the training and inference costs, such as training time and memory.
- This method uses salient maps derived from an off-the-shelf model as one of the targets. The salient maps are suitable and useful for the VOC dataset because most objects can be detected by the salient model. However, for the more challenged dataset, ADE20K, many semantic regions can not be identified by the salient model, such as grassland in the supplementary material Figure 9. Please study the effect of the salient maps supervision and the quality of the salient maps on the ADE20K dataset. A suggestion: you may replace the salient maps with the results of the SAM model [2].
- In Table 2, why is the replay-based IPSeg (33.6) worse than data-free-based PLOP+NeST (34.8)? Is there any insight or explanation?

[1] Incrementer: Transformer for class-incremental semantic segmentation with knowledge distillation focusing on old class, CVPR 2023
[2] Segment Anything, ICCV 2023

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes IPSeg, an innovative framework for addressing semantic drift in Class-Incremental Semantic Segmentation (CISS). IPSeg leverages two main strategies: (1) Image Posterior (IP) guidance to mitigate errors from independent task optimization, and (2) Permanent-Temporary Semantics Decoupling to handle noisy semantics. These mechanisms allow IPSeg to retain past knowledge while learning new classes, achieving significant improvements in segmentation performance on Pascal VOC and ADE20K benchmarks.

### Strengths
1. This approach enhances pixel-level accuracy by leveraging global image-level predictions. Specifically, by introducing the image posterior guidance mechanism, IPSeg aims to mitigate the separate optimization issue in CISS.
2. The decoupling of stable and temporary semantic components is well-conceived and allows the model to handle both static background and dynamic foreground objects across incremental steps.
3. IPSeg outperforms various state-of-the-art methods across different incremental segmentation scenarios.

### Weaknesses
1. The issue of separate optimization has been investigated by [2]. In that paper, the scale inconsistency issue "earlier incremental task heads may have larger output scales than the later heads, especially in similar classes" was alleviated by logit manipulation. Therefore, the claim that "separate optimization does not attract any attention" is inaccurate.
2. The introduction of additional components like the image posterior branch and decoupled semantics increases model complexity. This may hinder its applicability for real-time or resource-constrained applications. Efficiency comparisons, such as computational complexity, iterations required for convergence, and finetuning time cost, should be conducted. The reported computational cost of 137.1G compared to SSUL's 94.9G, a 44.5% increase, raises concerns about cost-efficiency.
3. Salient object detector is used to find out the foreground regions, which will incur additional computational costs. Moreover, it brings additional information and is unfair to other competing methods that do not use it.
4. The memory buffer may raise scalability and privacy concerns, especially when scaling to larger datasets and storing sensitive user data.
5. This paper missed several SOTA methods [1-2] in experimental comparison. Furthermore, the data-free version of IPSeg performs inferior compared to LGKD+PLOP on the three standard settings ADE20K 100-10, 100-50 and 50-50, when no memory is used. This raises concerns about the key contribution that "the image-level classification (IP) suffers less forgetting than the segmentation".

### Questions
1. The permanent branch aims to learn dummy labels representing “pure” background and unknown objects. However, the definition of unknown objects are ever-changing. For instance, "cat" can be an unknown class in step 1, and then a target class in step 2, and afterwards become a past seen class in step 3. I don't see the rationale why it is called the permanent branch. Generally, only consistent class definitions across all steps can be regarded as permanent semantics.
2. How are the final prediction maps generated from the permanent and temporary branches? The detail procedures should be elaborated.
3. The previous-class image labels are not available at the current step. How to supervise the image posterior in each step?
4. It seems like temporary branches predict pure background and other foreground regions in addition to the target classes at the current step. Does it contribute to the final prediction or just the target class scores are used to multiply by the corresponding confidence score from the image posterior branch?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper addresses the challenges of class incremental semantic segmentation (CISS), where models learn from sequential tasks with changing background semantics, a phenomenon known as semantic drift. The authors identify two key issues—separate optimization and noisy semantics—that significantly hinder CISS performance. To tackle these issues, they propose Image Posterior and Semantics Decoupling for Segmentation (IPSeg), which employs two main mechanisms: (1) Image Posterior Guidance: IPSeg uses image-wise posterior probabilities to guide pixel-wise predictions, mitigating separate optimization issues. (2) Semantics Decoupling: Noisy semantics are split into two groups, stable, static semantics and dynamic, temporary semantics, each handled by separate branches with distinct life cycles. Experiments on the Pascal VOC 2012 and ADE20K datasets show that IPSeg outperforms existing approaches, particularly in challenging long-term scenarios, and demonstrates improved balance between learning plasticity and memory stability.

### Strengths
## 1. Strong Motivation

The paper presents a well-defined and convincing motivation for addressing Separate Optimization, a challenge where earlier-trained task heads can produce disproportionately higher scores compared to later-trained heads for visually similar categories. This issue is thoroughly analyzed, with compelling visual support in Figures 1, 5, and 6.

## 2. Comprehensive Analysis

The authors provide a detailed ablation of each proposed component, supported by robust quantitative and qualitative analyses. This thorough exploration effectively demonstrates the contribution of each component to the overall method’s performance.


## 3. State-of-the-Art Performance

The proposed method, IPSeg, demonstrates state-of-the-art performance on the VOC2012 and ADE20K datasets, with results that convincingly surpass existing approaches.

## 4. Clear and Structured Presentation

The paper is well-written and carefully structured. The problem setting and motivation are clearly articulated, and each proposed component is thoroughly explained and ablated, enhancing the paper’s clarity and rigor.

### Weaknesses
Most of my concerns raised are addressed within the paper’s appendix, which provides comprehensive additional supportive analysis.

### Questions
N/A

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
To address the challenging Class incremental semantic segmentation (CISS), this paper proposes Image Posterior to attack the noisy semantics and Semantic Decoupling to cope with separate optimization, which both of these two issues refer to semantic drift and background shift problems in CISS. The proposed Image posterior supports with guidance to calibrate the error prediction and amplify the scale of correct prediction, hence solving the semantic drift issue when the model faces ambiguous categories between the past task and the current task. Semantic Decoupling implemented by Memory Bank manner is used to decouple the pure background, unknown foreground, past class pixels, and target class pixels. The authors employ a saliency estimator and filtering trick to improve the memory buffer while the memory buffer is an image-level corpus.

### Strengths
1. The paper writing is kind of good.

2. Supporting image posterior within the image-level to guide the CISS task sounds reasonable to resolve the semantic drift and works like error calibration.

3. The final CISS experimental results seem competitive and the ablative studies are extensive.

### Weaknesses
1. Decoupling the background into pure background and unknown foregrounds (utilizing the saliency model), I believe, has been widely studied. The decoupling implementation sounds complicated to understand in the main paper, but I think the authors could provide a more clear presentation of this part. I think the authors should make detailed comparisons with existing works, like Ssul.

2. Not sure how the authors construct the memory buffer with image-level samples. This plays an important role in this paper to obtain good guidance.

3. The figure presentations are inconsistent, Figure shows good quality while figures 2/4/5/6/7/8 display a blur effect. These should be presented by pdf, etc.

### Questions
Please refer to my weaknesses part. Moreover, the authors shall further make some comparisons in terms of training efficacy with the previous method, since they use a memory buff and constitute a two-branches architecture.

### Soundness
3

### Presentation
3

### Contribution
3
