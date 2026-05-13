# VOVTrack: Exploring the Potentiality in Videos for Open-Vocabulary Object Tracking

- Decision: Reject
- Scores: 5, 6, 6, 5, 6

## Abstract
Open-vocabulary multi-object tracking (OVMOT) represents a critical new challenge involving the detection and tracking of diverse object categories in videos, encompassing both seen categories (base classes) and unseen categories (novel classes). This issue amalgamates the complexities of open-vocabulary object detection (OVD) and multi-object tracking (MOT). Existing approaches to OVMOT often merge OVD and MOT methodologies as separate modules, predominantly focusing on the problem through an image-centric lens.
    In this paper, we propose VOVTrack, a novel method that integrates object states relevant to MOT and video-centric training to address this challenge from a video object tracking standpoint. First, we consider the tracking-related state of the objects during tracking and propose a new prompt-guided attention mechanism for more accurate localization and classification (detection) of the time-varying objects. 
    Subsequently, we leverage raw video data without annotations for training by formulating a self-supervised object similarity learning technique to facilitate temporal object association (tracking). 
    Experimental results underscore that VOVTrack outperforms existing methods, establishing itself as a state-of-the-art solution for open-vocabulary tracking task.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces Tracking-state-aware prompt guided attention, enabling the network to learn the detection of objects in different tracking states. A self-supervised approach is adopted to train tracking, leveraging large-scale, unlabeled video data across various categories. The experimental results on TAO datasets indicate that the proposed method achieves advanced performance.

### Strengths
1. The paper offers a detailed explanation of the proposed method. Utilizing unlabeled data for self-supervision serves, to some extent, as an alternative to address the current scarcity of large vocabulary tracking data. 
2. The results show good performance in comparisons on the OVMOT benchmark.

### Weaknesses
1. The CIsA for basic categories in your method is lower than that of the baseline method OVTrack. Given that basic categories account for the majority of targets, the decrease on CIsA appears to reflect more than just typical fluctuation effects. Could this imply that your model's approach introduces a degree of conflict between tracking and classification based on the baseline? 
2. There is a lack of visualization and analysis for the prompt guided attention, which does not adequately demonstrate its direct impact.

### Questions
1. Considering CLIP's training process, is there a significant distinction in the representations output by CLIP when tracking-state-aware prompts, such as 'unoccluded' and 'occluded', are provided?
2. Why does your method improve the ClA for novel categories compared to the baseline OVTrack but decrease scores for base categories? Does this suggest that your model introduces a conflict between tracking and classification? 
3. Could you include a visual representation and analysis of the prompt guided attention? This would more intuitively demonstrate its role and effect.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Open-vocabulary multi-object tracking (OVMOT), a significant challenge that involves detecting and tracking various object categories in videos, including both known (base classes) and unknown (novel classes) categories. The authors critique existing OVMOT methods for treating open-vocabulary object detection (OVD) and multi-object tracking (MOT) as separate modules, primarily focusing on image-based approaches. To address this, they present VOVTrack, which integrates object states relevant to MOT with video-centric training, approaching the challenge from a video object tracking perspective. VOVTrack features a prompt-guided attention mechanism that enhances the localization and classification of dynamic objects, and it employs a self-supervised object similarity learning technique for tracking using raw, unlabeled video data. Experimental results demonstrate that VOVTrack outperforms current methods, establishing it as a leading solution for open-vocabulary tracking tasks.

### Strengths
1. This manuscript is standardized and the writing is fluent, and the content is easy to understand.

2. This manuscript proposes a new tracking-related prompt-guided attention for the localization and classification (detection) in the open vocabulary tracking problem. This method takes notice of the states of the time-varying objects during tracking, which is different from the open-
vocabulary object detection from a single image.

3. This manuscript develops a self-supervised object similarity learning strategy for the temporal association (tracking) in the OVMOT problem. This strategy, for the first time, makes full use of the raw video data without annotation for OVMOT training, thus addressing the problem of training data shortage and eliminating the heavy burden of annotation of OVMOT.

4. Experimental results on the public benchmark demonstrate that the proposed VOVTrack achieves the best performance with the same training dataset (annotations), and comparable performance with the methods using a large dataset (CC3M) for training.

### Weaknesses
1. The experimental tables lack details on model complexity. It would be helpful to include a table or section comparing FLOPs, parameters, model size, and FPS across the different methods evaluated, including the baseline OVTrack method and other state-of-the-art approaches.

### Questions
Please refer to the concerns and issues raised in the "Weaknesses".

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work presents a novel open-vocabulary multi-object tracking method that integrates object states based on prompt learning. Different from existing works, it combine OVD and MOT in a unified framework. Some self-supervised losses are designed to learning better object associations. Experiments on public dataset demonstrate the effectiveness of the proposed method.

### Strengths
A novel method that integrates object states based on prompt learning is proposed to combine OVD and MOT for open-vocabulary multi-object tracking.

Some self-supervised losses are designed to learning better object associations.

Experiments are conducted on public dataset.

### Weaknesses
The following details are unclear. Are the designed prompts only used in training procedure? It would be better if visualized results are provided to validate the effectiveness of these prompts in handling challenging frames with occlusions or motion blur.

There is no comparison with works published in 2024, and the effectiveness of the proposed method is thus not fully validated. The relevent and recent trackers including both closed-set and open-vocabulary ones should be included in comparison.

The results suggest that the proposed method performs abnormal under ClsA metric in both result comparison and ablation study. Though it is better than all methods in most metrics, but it performs worse than OVTrack and OVTrack+RegionCLIP in a clear margin, and also worse than other methods in some cases. The reasons behind these results are not well explained.

Some errors:

Line 256:  into ore framework model

Line 456: Our method

### Questions
Some important details and explanations should be provided for clarity.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work proposes a series of improvements to the existing OV MOT framework (OVTrack), including a novel prompt-guided attention mechanism and a self-supervised object similarity learning method. With the support of additional video data, these enhancements achieve superior performance on the TAO dataset compared to OVTrack.

### Strengths
1. Competitive OV tracking performance on TAO.
2. Self-supervised object similarity learning is compatible with unlabeled video data.

### Weaknesses
1. Novelty is limited: The overall architecture of the proposed OVOTrack is based on OVTrack. The specific implementation within the tracking-state aware prompt approach does not exhibit a clear association with the tracking state. Moreover, this method does not assess object quality specifically for tracking scenarios, as it remains overly limited to factors such as occlusion and blurriness. On the other hand, the self-supervised object similarity learning proposed in this work closely resembles QDTrack, with no significant differences observed.
2. Writing requires further improvement: The overall writing is somewhat scattered and lacks coherence, with inconsistencies between the motivation of the paper and the proposed approach, raising concerns of possible over-claim. There is considerable redundancy in language, with some sections being overly simplistic while others are unnecessarily verbose. Additionally, certain assumptions and notations in the methodology are not rigorously standardized (e.g., line 218). Therefore, I believe there is substantial room for improvement in the writing.  
3. Experimental setting: The training process described in the paper involves four stages, which makes it overly complex and cumbersome. Compared to OVTrack, this work utilizes a substantial amount of additional TAO video data for training; however, the classification performance on the base categories in the TAO benchmark has declined. Moreover, the ablation study results indicate that the OVOTrack model consistently underperforms in classification metrics, yet no reasonable explanation is provided for this issue. The examples provided in the visualization results are overly simplistic, failing to showcase the model’s true capabilities.

### Questions
1. The primary assertion of the paper is that existing OV tracking methodologies do not take into account the states of objects. However, the proposed approaches appear to be largely unrelated to tracking object states, and the introduced prompt, .e.g., occuded, and complete, seems overly naive in my view.
2. The proposed classification method only focuses on the high-quality object. However, exclusively training the classifier on high-quality targets may result in the neglect of low-quality targets that are blurred or occluded. This seems inconsistent with the paper’s claim of addressing issues related to blurring and occlusion in object tracking. Furthermore, could this be the reason for the model’s lower classification performance on the base?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed a new tracking-related prompt-guided attention for the localization and classification, and develops a self-supervised object similarity learning strategy for the temporal association in OVMOT. Experiments demonstrate that the proposed method achieves state-of-the-art tracking performance compared to previous methods.

### Strengths
1. This paper propose a new tracking-related prompt-guided attention for the localization and classification in OVMOT​.
2. The self-supervised learning strategy leverages unlabeled video data for the temporal association, addresses the challenge of training data shortage.
3. Extensive experimental results, demonstrating that VOVTracker outperforms existing methods on TAO benchmark.

### Weaknesses
1. Lack of novelty. The self-supervision is common and there are some considerable work in vision tasks. However, this paper just applies it to OVMOT, and does not compare the proposed method with previous methods. What's the main difference and contributions for OVMOT.
2. While VOVtrack leverages unlabeled video data, its performance seems to depend on the quality and representativeness of the videos, which could affect its robustness across different real-world conditions​.
2. The authors should conduct on the ablation sduty of different parameter settings. Such as parameters related to training and inference.

### Questions
1. VOVTrack lacks of a clear definition, what's the full name?
2. For Table 1, the propsed VOVtrack performs worse than OVTrack in terms of ClsA metric. What is the reason behind it?
3. For Table 2, it demonstrate the effectiveness of Prompt-guided attention. But the baseline with the self-supervised association module fail to obtain obvious improvements, so that the contribution can not be effectively convinced.

### Soundness
2

### Presentation
3

### Contribution
2
