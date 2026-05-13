# Unleashing the Potential of Unlabeled Data: Bidirectional Collaborative Semi-Supervised Active Learning for 3D Object Detection

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
To address the annotation burden in LiDAR-based 3D object detection, active learning (AL) methods offer a promising solution. However, traditional active learning approaches solely rely on labeled data to train an initial model for data selection, overlooking the potential of leveraging unlabeled data. Recently, attempts to integrate semi-supervised learning (SSL) into AL with the goal of leveraging unlabeled data have faced challenges in effectively resolving the conflict between the two paradigms, resulting in less satisfactory performance.
To tackle this conflict, we propose a Bidirectional Collaborative Semi-Supervised Active Learning framework, dubbed as BC-SSAL. Specifically, from the perspective of SSL, we propose a Collaborative PseudoScene Pre-training (CPSP) method that effectively learns from unlabeled data without introducing adverse effects. From the perspective of AL, we design a Collaborative Active Learning (CAL) method tailored for outdoor LiDAR scenes, which complements the uncertainty and diversity methods by model cascading, alleviating the dilemma of sampling rare classes. Extensive experiments conducted on KITTI and Waymo demonstrate the effectiveness of our BC-SSAL. Especially, on the KITTI dataset, utilizing only 2\% labeled data, BC-SSAL can achieve comparable performance to the model trained on the full set.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to reduce the annotation burden in LiDAR-based 3D object detection, the authors propose a Bidirectional Collaborative Semi-Supervised Active Learning framework (BC-SSAL). This framework combines Collaborative PseudoScene Pre-training (CPSP) to effectively utilize unlabeled data and Collaborative Active Learning (CAL) to enhance sampling, particularly for rare classes, in outdoor LiDAR scenes.

### Strengths
- The task setting is practical, combining active learning (AL) and semi-supervised learning (SSL) to enhance 3D detection performance while minimizing annotation requirements.
- Good exploration and analysis are conducted on various strategies for integrating SSL with existing AL frameworks.

### Weaknesses
 - The proposed Collaborative PseudoScene Pre-training (CPSP) module shares similarities with the approach in [A], in which high-quality, high-certainty bounding boxes are stored in a memory bank, and point clouds from these boxes are integrated into scenes. Could you clarify and compare the conceptual and empirical differences between CPSP and [A]?

 - The Active Learning (AL) sampling strategy lacks novelty, as entropy is a widely used general AL method. Moreover, the box diversity metric shows minimal improvement, as demonstrated in Table 4.

 - Some typos: In lines 177 and 179, there should be a space before "(TMU)" and "(USS)."

### Questions
The impact of varying thresholds for confident object extraction has not been studied. Given that the model was initially pretrained on a limited dataset, its predictions may contain noise, suggesting that thresholds should be carefully tuned and selected. Could you explain the process for determining the optimal thresholds and demonstrate the impact of different threshold values?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a Bidirectional Collaborative Semi-Supervised Active Learning (BC-SSAL) framework for 3D object detection in LiDAR data, aiming to reduce the annotation burden. BC-SSAL integrates semi-supervised learning (SSL) with active learning (AL) to leverage unlabeled data effectively. Experiments on KITTI and Waymo datasets show BC-SSAL achieves state-of-the-art performance.

### Strengths
This method combines active learning with semi-supervised learning, proposing a new scheme for efficient label learning. The idea is interesting. The proposed method achieves the best performance compared to multiple baseline methods on two datasets.

### Weaknesses
1. The Pre-train method proposed in this paper has limited novelty. The main content highly overlaps with SS3D[1]. Specifically, SS3D combines a pre-trained detector to mine potential instances in unlabeled scenes to generate an 'Instance Bank' and 'Broken Scene', and then uses gt-sampling to produce training data.
2. The effectiveness of the active learning module is missing validation. One of the main contributions of this paper is active learning, so it is necessary to supplement a separate performance comparison with the state-of-the-art (SOTA) active learning methods [2][3].
3. The method is called "Bidirectional Collaborative Semi-Supervised Active Learning," but no clear design addresses this specific collaboration. It is recommended that the authors clarify the specific conflicts between the two strategies, provide experimental data to demonstrate the consequences of such conflicts, and explain how these conflicts are resolved.
4. The semi-supervised scheme only employs HSSDA, lacking validation across different semi-supervised approaches. It is suggested that the authors validate the proposed bidirectional collaboration scheme across multiple representative semi-supervised methods.

### Questions
What are the differences between the design of the CPSP module and the related model design in SS3D? Please also respond to the comments in Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces BC-SSAL (Bidirectional Collaborative Semi-Supervised Active Learning) to enhance 3D object detection in LiDAR-based systems. The framework addresses the challenge of annotation burden by effectively leveraging unlabeled data through a combination of semi-supervised learning (SSL) and active learning (AL). Overall, this paper is technically detailed and the experiments are quite comprehensive. However, most of the designs in the paper are combinations of existing work, lacking novel designs, and the improvements in the experiments are not significant.

### Strengths
1. The paper is well-structured, with a clear abstract, introduction, methodology, experiments, and conclusion sections that logically flow from one to the next.
2. The paper provides extensive experimental results on the KITTI and WOD datasets and conducts a large number of ablation studies.
3. The paper provides a multitude of figures that clearly demonstrate the design details of each module, facilitating the reader's understanding or reproduction of the methods described in the paper.

### Weaknesses
1. It is not clear why the method is named ‘Bidirectional xx’, I cannot see any module design that is ‘bidirectional’.
2. I cannot see any special contributions from this paper. Most of the components are simple combinations of existing works. Such as the so-called CPSP is indeed a GT sampling data augmentation used in most of regular 3D object detectors.
3. The improvement of this method does not seem to be very significant. On the KITTI dataset, the most convincing category is the car, as there are enough objects in this category to make the conclusions more reliable. However, this method is not even as good as 3DIoUMatch.

### Questions
1. Why is the paper titled 'Bidirectional xx'? Where is the bidirectional operation reflected?
2. What are the core differences between CPSP and GT sampling?

### Soundness
2

### Presentation
2

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
This paper proposes an active learning and semi-supervised learning collaborative label-efficient 3D object detection method. By mining useful information from unlabeled data to enhance the performance of 3D detectors. The proposed method is experimentally validated on two widely used datasets.

### Strengths
1. The paper presents an ideal for 3D object detection that collaborates semi-supervised learning and active learning bidirectionally, which is novel and interesting.
2. The design of the active learning scheme is reasonable, and the experiments have successfully validated the performance improvement brought by this module to the entire method.

### Weaknesses
1. The proposed method has limited innovation; the CPSP module is highly similar to the 'Reliable Background Mining Module' presented in the existing SS3D[1]. The Reliable Background Mining Module employs a pre-trained detector to process unlabeled scenes, extracting foreground instances to construct a bank, and then uses gt-sampling data augmentation to generate new training data. The CPSP module follows the same procedure without any difference.

2. The motivation behind this paper is unclear, as there is no data proving the conflict between SSL and AL. It is suggested to provide experimental results of a naive combination of SSL  and AL  for 3D object detection, demonstrating that directly combining the two methods is unreliable. Additionally, the method does not offer a special design based on the proposed concept of 'bidirectional collaboration'.

3. The figures in the paper are sketchy and not aesthetically pleasing.

### Questions
see Weaknesses*.

### Soundness
2

### Presentation
2

### Contribution
2
