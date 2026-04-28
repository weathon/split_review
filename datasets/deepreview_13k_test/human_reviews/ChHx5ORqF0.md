# Transferring Labels to Solve Annotation Mismatches Across Object Detection Datasets

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
In object detection, varying annotation protocols across datasets can result in annotation mismatches, leading to inconsistent class labels and bounding regions. Addressing these mismatches typically involves manually identifying common trends and fixing the corresponding bounding boxes and class labels. To alleviate this laborious process, we introduce the label transfer problem in object detection. Here, the goal is to transfer bounding boxes from one or more source datasets to match the annotation style of a target dataset. We propose a data-centric approach, Label-Guided Pseudo-Labeling (LGPL), that improves downstream detectors in a manner agnostic to the detector learning algorithms and model architectures. Validating across four object detection scenarios, defined over seven different datasets and three different architectures, we show that transferring labels for a target task via LGPL consistently improves the downstream detection in every setting, on average by $1.88$ mAP and 2.65 AP$^{75}$. Most importantly, we find that when training with multiple labeled datasets, carefully addressing annotation mismatches with LGPL alone can improve downstream object detection better than off-the-shelf supervised domain adaptation techniques that align instance features.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper fuscous on object detection and tries to address the annotation mismatch issue among different datasets. 
This paper first formally defines the label translation problem and proposes a taxonomy that characterizes the annotation mismatches across object detection datasets. In addition, this paper  introduces a simple yet effective label-guided pseudo-labeling (LGPL) approach. The proposed LGPL method extends the concept of pseudo-labeling by leveraging source dataset bounding boxes and class information for label translation. Comprehensive experiments and analysis on four translation scenarios across seven datasets validate the effectiveness of the proposed method.

### Strengths
+ This paper is well organized and written. The overall motivation is clear and convincing.
+ The research problem defined in this paper is interesting and practical.
+ Promising results are achieved compared to several baselines.

### Weaknesses
- Although the introduced research problem is interesting. The technical contributions of this paper is somewhat limited. It would be better to further highlight the novelty and technical contributions.
- In Figure 4, the proposed method is compared to an unsupervised domain adaptive object detection method and an unsupervised image domain adaptive method. In my understanding, the two domain adaptive methods don’t have any labels in the target domain. It is not strange the proposed method achieves superior performance, as it uses more annotations. I’m wondering why the proposed method is not compared to some weakly supervised cross-domain object detection methods, such as "H2FA R-CNN: Holistic and Hierarchical Feature Alignment for Cross-Domain Weakly Supervised Object Detection, CVPR’22", where all the image-level annotations are available.
- The class-wise threshold $\sigma_c$ is ad hoc. How to choose the value? Is it sensitive to the final results?

### Questions
Please refer the Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper attempts to tackle annotation mismatches in multi-dataset training for object detectors. It points out that different datasets may have different definitions or annotation protocols to the same category, leading to annotation mismatches. Four kinds of annotation mismatches are highlighted, i.e. Class semantics, Annotation instructions, Human-machine misalignment, Cross-modality labels. To address those mismatches, it proposes to train a label translator to translate annotations of source datasets to the target datasets. The label translator follows the design of two-stage detector (e.g. faster rcnn) with a RPN and RoI head. During the training of the translator, the RPN is trained with source datasets and generates source-style boxes. The RoI head converts the generated source-style boxes to the target-style. During inference, the RoI head converts ground-truth annotations of the source dataset (both boxes and class labels) to the target-style. Experiments shows that the proposed label translator improves various detectors on certain pairs of datasets.

### Strengths
1. The task of annotation mismatches for the same category is interesting. Based on my knowledge, studies of multiple dataset training seldom explore annotation issues for the same category.

2. It's interesting to leverage RoI head to covert annotations of the source datasets to the target datasets.

3. The proposed translator achieves good performance on various detectors and datasets.

4. The paper is well written and easy to follow.

### Weaknesses
1. The assumption is too strong that the source and the target datasets have the same categories. In multi-dataset training, it is a common case that different datasets not only have overlapped categories but also have unique categories. I believe it's more important to handle unique categories that are annotated in one dataset but not in the others. That's because unannotated objects in the other datasets will be regarded as background by mistake. It's better to have a solution to handle both overlapped and unique categories.

2. RoI head is able to refine various region proposals to the target-style boxes. Is it necessary to train a RPN as box generator that generates source-style boxes? It's better to compare the proposed solution with a only-RPN solution. That is, train a RPN (probably together with the two-stage architecture) with the target dataset and use it on different source datasets so that we don't need to train RPNs for different pairs of source-target datasets.

3. I'm not sure how to use the label translator to handle target datasets with more than one categories. Based on the experiments, it seems that the label translator only handles one category ('cyclist' in  Synscapes, Cityscapes, MVD, nuImages and Waymo). Probably, with the increase of categories, the label translator may introduce the noisy pseudo labels and negatively impact the performance.

4. Evaluations on widely used object detection datasets are missing. How about COCO, Objects365, and OpenImages? It seems that the experiments only include detection datasets for driving scenarios.

5. Based on Sect. 5.3, translation-mAP is not strongly correlated with downstream-mAP, and visually analyzing the translated labels is insufficient to judge label translation. Why is translation-mAP reported?

6. The proposed label translation seem to require training between every source and target datasets, which is costly to scale up.

### Questions
See Weakness.

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
In this paper, the authors study the problem of addressing bounding-box annotation mismatches across different datasets. For this end, they propose training a "translator" network that converts the bounding box annotations in the source dataset into the target dataset.

### Strengths
+ Annotation mismatch across datasets is a severe problem in OD.
+ Good results.

### Weaknesses
1. I had problem following the scope of the paper.

1.1. The paper introduces a very general alignment setting in Introduction + Figure 1, which is not matched with what is really performed. I had to make several loops between Method & Introduction + Figure 1 to understand what is going on.

1.2. "1) We consider scenarios where the class label spaces are matched but the annotation protocols are different, therefore, leading to annotation mismatches (see Section 3). 2) We optimize the target performances, while multi-dataset detection optimizes the average performances of all datasets considered." => The authors should provide convincing arguments + results on why this narrowed-down scope of the mismatch problem is significant.

1.3. "In this work, we assume that (1) the class labels are the same between the source and the target labeling functions and (2) the source labeling function either detects or over-detects all the objects specified in the target labeling function." => Again, the validity of these assumptions should be justified.

1.4. "We optimize the target performances, while multi-dataset detection optimizes the average performances of all datasets considered." => Why is it not better to have a multi-dataset version?

1.5. "label translation" is misleading. With the general coverage in the Introduction, I expected language translation to be performed in the method. "Recall from our main assumption that label translation does not require generating a correct class label, but only determining whether the object should be labeled as well as the corresponding bounding box." => I have difficulty calling this translation.

1.6. Section 3: It would be worthwile to extend this section with analyses. As such, it is rather weak.

2. Experimental evaluation is limited. It is not clear why YOLOv3 is chosen, compared to its newer versions or other one-stage detectors?

3. Most importantly, as bbox localization changes through the proposed method, the paper should quantify localization directly and evaluate performance with such a measure. I would recommend the localization term of the Localization Recall Precision metric.


Minor comments:
- Fig 1 left: Cyclist => rider for the MVD dataset.
- Introduction: "This work characterizes four types of annotation mismatches," => It would be nice to briefly summarize here what these four types are.
- Figure 3: The figure gives a feeling that the 'cyclist' label belongs to both datasets, which makes it difficult to understand what is being translated into what.

**After the rebuttal**

The authors have been able to partially address my concerns about the significance of the taxonomy and the experimental evaluation. For taxonomy to be considered a contribution, I expect more analyses & justifications. The experiments with a SOTA model should also be more comprehensive as YOLOv8-nano is hardly a SOTA model. However, the authors did the best of what could be done in a short amount of time and I find the extended discussion on the taxonomy and the new results promising. Therefore, I would like to increase my original recommendation.

### Questions
See Weaknesses.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
