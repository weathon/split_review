# EventRPG: Event Data Augmentation with Relevance Propagation Guidance

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 5, 6

## Abstract
Event camera, a novel bio-inspired vision sensor, has drawn a lot of attention for its low latency, low power consumption, and high dynamic range. Currently, overfitting remains a critical problem in event-based classification tasks for Spiking Neural Network (SNN) due to its relatively weak spatial representation capability. Data augmentation is a simple but efficient method to alleviate overfitting and improve the generalization ability of neural networks, and saliency-based augmentation methods are proven to be effective in the image processing field. However, there is no approach available for extracting saliency maps from SNNs. Therefore, for the first time, we present Spiking Layer-Time-wise Relevance Propagation rule (\texttt{SLTRP}) and Spiking Layer-wise Relevance Propagation rule (\texttt{SLRP}) in order for SNN to generate stable and accurate CAMs and saliency maps. Based on this, we propose \texttt{EventRPG}, which leverages relevance propagation on the spiking neural network for more efficient augmentation. Our proposed method has been evaluated on several SNN structures, achieving state-of-the-art performance in object recognition tasks including N-Caltech101, CIFAR10-DVS, with accuracies of $85.62\%$ and $85.55\%$, as well as action recognition task SL-Animals with an accuracy of $91.59\%$.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the problem of event-based data augmentation for Spiking Neural Networks by computing saliency. Two methods are presented with different levels of overhead on training; these methods are incorporated in two augmoentation schemes that either drop events or mix two event streams. A number of SNNs was evaluated on both object and action recognition datasets, and improvement in accuracy was demonstrated - especially on action recognition datasets.

### Strengths
1) The authors mention that the code will be released; to me this is important as it enables other researchers to easily build on top of this paper.

2) I particularly enjoyed the theoretical introduction into the SNNs, this makes the rest of the paper much easier to read.

### Weaknesses
1) If anything, I would like to notice here that the improvements compared to competing methods are generally small. It would be interesting to see an apples-to-apples comparison in therms of compute overhead (which is mentioned, but I do not see numberical benchmark results); or, another compelling reason to use the presented methods vs e.g. second best.

2) Also see 'questions': it would be good to show that saliency on motion-related datasets is more than just event density. This could be done e.g. by correlating saliency to raw optical flow magnitude, or evaluating on actions that are slower.

### Questions
1) In abstract, expand SNN as 'Spiking Neural Networks', for the benefit of readers unfamiliar with the abbreviation.

2) Fig. 1 highlights a failure case of one of the augmentation methods; it would be great to see a citation that explains why this limitation is difficult to alleveiate (e.g. by considering correct label classes). The image also seems excessive, and a single-sentence explanation should be enough.

3) I am curious if the better performance / saliency on action-related datasets is an artifact of the event camera itself - since the density of the events correlates with motion and SNN may get more cues on regions with faster motion.

4) It would be beneficial, in tables 3 and 4 to mention that all of the datasets are 'native' event-based datasets (unless I am mistaken). What would be the comparison if a classic camera dataset was converted to events, especially on action classification tasks?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes two efficient and practical methods, SLTRP and SLRP, for generating CAMs and saliency maps for SNNs for the first time. Based on these, the authors propose EventRPG to achieve data augmentation, which drops events and mixes events with Relevance Propagation Guidance.

### Strengths
This paper proposes Spiking Layer-wise Relevance Propagation(SLRP) rule and Spiking Layer-Time-wise Relevance Propagation(SLTRP) rule, the layer-wise relevance propagation method of SNNs for the first time, which can obtain the feature contribution at each pixel. RGBDrop and RGBMix are established to achieve data augmentation based on the generated CAMs. The results of experiments prove the usefulness of SLRP and SLTRP both for accuracy and efficiency. The EventRPG shows good performance in object recognition and action recognition tasks.

### Weaknesses
1. The description of RPGMix is quite simple and unclear. Section 4.3 fails to clearly illustrate the algorithm flow of RPGMix. Many operations in Fig 3(b) are not carefully analyzed, such as sample position in the Nonoverlapping Region, which makes it hard to understand. I think Fig3 is the main figure of this paper and Fig 3(b) accounts for the most part of Fig3, hence the authors need to spend more space to describe it. Otherwise, the readers may feel confused about RPGMix.
2. Equation 15 lacks physical meaning and theoretical basis. It needs more explanations for researchers to make further progress.
3. The objective faithfulness of SLRP and SLTRP is not outstanding enough. In N-Cars,  DVSGesture, and SL-Animals datasets, the proposed methods have similar or even inferior performance compared to other algorithms.

### Questions
The author should carefully illustrate RPGMix and the performances of SLRP and SLTRP are challenged in the metric of the objective faithfulness.

### Soundness
3 good

### Presentation
2 fair

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
This paper proposes a mixup-based data augmentation method for training Spiking Neural Networks (SNNs). Inspired by saliency-based augmentation in RGB image vision such as Puzzle Mix and SaliencyMix, the authors derive the Class Activation Map (CAM) and saliency map for SNNs, and then mix two samples based on them. Experimental results show that the proposed EventRPG consistently improves the classification accuracy on various datasets.

### Strengths
- The derivation of the CAM and saliency map of SNNs itself is a clear contribution. The results in Table 1 prove the correctness of this
- EventRPG is able to consistently improve performance across event datasets
- The time cost of EventRPG is comparable to similar augmentations in conventional vision

### Weaknesses
My main concern is regarding the experiments:
- The paper motivates the need for event data augmentation with the statement that "the lack of huge event-based datasets similar to Imagenet prevents us from improving the model performance on relatively small datasets using a Pretrain-Finetune paradigm". However, there is an event camera version of ImageNet available [1], and its paper shows that pre-training on N-ImageNet can greatly improve the accuracy on other datasets via transfer learning. Therefore, this statement in the Introduction is wrong
- Since N-ImageNet is available, I would like to see results on this dataset. This is similar to conventional vision research on data augmentation, where ImageNet is the best testbed. If the authors are not able to train on N-ImageNet, the mini subset can be considered, though I do not think that is a comprehensive benchmark
- The authors compare EventRPG with conventional vision methods such as Grad-CAM in Table 1. Thus, I wonder if it is possible to compare with Puzzle Mix and SaliencyMix in Table 3?
- NDA applies the method to unsupervised contrastive learning and shows promising results. Is it possible to conduct such experiments using EventRPG?

### Questions
See Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
