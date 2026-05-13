# Learning 3D Perception from Others' Predictions

- Decision: Accept
- Scores: 5, 6, 6, 6, 6

## Abstract
Accurate 3D object detection in real-world environments requires a huge amount of annotated data with high quality. Acquiring such data is tedious and expensive, and often needs repeated effort when a new sensor is adopted or when the detector is deployed in a new environment.
We investigate a new scenario to construct 3D object detectors: \textit{learning from the predictions of a nearby unit that is equipped with an accurate detector.} For example, when a self-driving car enters a new area, it may learn from other traffic participants whose detectors have been optimized for that area.
This setting is label-efficient, sensor-agnostic, and communication-efficient: nearby units only need to share the predictions with the ego agent (\eg, car).
Naively using the received predictions as ground-truths to train the detector for the ego car, however, leads to inferior performance.  
We systematically study the problem and identify viewpoint mismatches and mislocalization (due to synchronization and GPS errors) as the main causes, which unavoidably result in false positives, false negatives, and inaccurate pseudo labels.
We propose a distance-based curriculum, first learning from closer units with similar viewpoints and subsequently improving the quality of other units' predictions via self-training. We further demonstrate that an effective pseudo label refinement module can be trained with a handful of annotated data, largely reducing the data quantity necessary to train an object detector.
We validate our approach on the recently released real-world collaborative driving dataset, using reference cars' predictions as pseudo labels for the ego car. Extensive experiments including several scenarios (\eg, different sensors, detectors, and domains) demonstrate the effectiveness of our approach toward label-efficient learning of 3D perception from other units' predictions.\footnote{Project website: \textbf{\texttt{\url{https://jinsuyoo.info/rnb-pop}}}}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a novel approach for training 3D object detectors by utilizing predictions from nearby agents with accurate detectors. This approach addresses the challenges of acquiring large amounts of annotated data. Validated on a real-world collaborative driving dataset, the proposed method demonstrates effective label-efficient learning and substantially improves the AP.

### Strengths
- The quality of the paper's figures is high and relatively clear and explicit.
- This method ensures the accuracy of the detector while reducing the cost of annotation, and its effectiveness has been verified on both real and simulated datasets.

### Weaknesses
1. This paper introduces a variant of the offboard 3D object detection method. It only selects an unsupervised scheme as a baseline, which is inappropriate. For a fair comparison, the proposed paper should be compared with offboard 3D object detection methods with similar experimental settings. These methods also rely on an accurate detector to label unannotated scenes. The authors should select the correct baselines[1] [2] for comparison.
[1] DetZero: Rethinking Offboard 3D Object Detection with Long-term Sequential Point Clouds, ICCV 2023. 
[2] Offboard 3D Object Detection from Point Cloud Sequences. CVPR 2021.

2. Compared to traditional offboard 3D object detection, the proposed solution not only uses full data annotation to train an accurate detector but also provides partial manual labeling for unannotated scenarios. This approach of adding extra manual labeling diminishes the contribution of the method. The authors emphasize that when an autonomous vehicle enters a new scene, it can obtain scene information from an established intelligent agent, which is an online process. However, the method itself is offline, which creates a contradiction. What are the proposed method's contributions in light of these concerns?
3. The proposed method provides pseudo-labels for the ego vehicle by directly passing the predicted results of the reference vehicle, which is a very naive approach. A semi-supervised learning framework is more flexible. What kind of performance effects would a semi-supervised learning framework have in this experimental setup? For example, train a teacher network using data from labeled reference vehicles, and then use the teacher network to generate pseudo-labels for unlabeled point clouds to train the student network further.
4. The ground truth of the reference vehicle is completely discarded in the subsequent method design, which is undoubtedly regrettable. Even if the center position of the ground truth has a deviation for the ego vehicle, the size of the bounding box is entirely correct, and this information is also very important. Therefore, why not use the reference vehicle's ground truth in their method?

### Questions
The proposed method provides pseudo-labels for the ego vehicle by directly passing the predicted results of the reference vehicle, which is a very naive approach. A semi-supervised learning framework is more flexible. What kind of performance effects would a semi-supervised learning framework have in this experimental setup? The ground truth of the reference vehicle is completely discarded in the subsequent method design, which is undoubtedly regrettable. Even if the center position of the ground truth has a deviation for the ego vehicle, the size of the bounding box is entirely correct, and this information is also very important. Please also respond to the comments in  Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper aims to develop a label-efficient approach for training 3D object detectors in autonomous vehicles by leveraging predictions from nearby vehicles equipped with accurate detectors. The main technical contribution is the proposed R&B-POP pipeline, which refines detection results from neighboring cars using a box ranker and a distance-based curriculum self-training approach. This method addresses challenges like viewpoint mismatches and localization errors that arise when integrating predictions from external sources. In experiments, the authors validated their approach on a collaborative driving dataset; they showed that with a small set of labeled data, this approach achieves performance close to that of fully supervised models.

This is an interesting exploration of new formulation for label-efficient 3D object detection. However, it is unclear how well the proposed method performs compared to other data-efficient domain adaptation or fine-tuning strategies, as relevant comparisons with SOTA are lacking. Additionally, the problem setting feels somewhat artificial, relying on several assumptions that may limit its practical applicability. 
My rating is a weak reject.

### Strengths
+ The paper introduces an interesting problem formulation for 3D object detection in resource-limited settings, suggesting a new collaborative information-sharing approach to reduce labeling costs.
+ The ablation study is well designed. Results demonstrate the contribution of different design components to the overall performance, sharing valuable insights into the effectiveness of these different components in the proposed pipeline.

### Weaknesses
-	Practicality and applicability of the problem setting. One of my main concerns is the practicality of the proposed problem setting. First, the approach relies heavily on the assumption that neighboring cars with accurate detectors are always available when needed, but this may not always be feasible. The paper does not adequately address scenarios where no such vehicles are present, or if the available vehicles have unreliable detection capabilities, which would severely limit the applicability of the proposed method. Moreover, the assumption that detection sharing is inherently safe is a significant oversimplification. The system needs to account for malicious actors or faulty sensors, which could lead to incorrect or even dangerous pseudo-labels. This lack of robustness in the face of real-world uncertainties is a major weakness. Additionally, the paper does not discuss the communication overhead required for sharing detection results between vehicles, which could be a bottleneck in real-time applications.
-	Technical comparisons. If the primary technical goal is to enable fine-tuning with minimal data, it should include comparisons with existing/ SOTA data-efficient training and fine-tuning methods. Demonstrating how this method compares with these techniques/models, will better clarify its advantages and limitations. Such a comparison is currently lacking. The absence of comparisons with established methods like few-shot learning, domain adaptation, or semi-supervised approaches makes it difficult to assess the true novelty and effectiveness of the proposed method. It is unclear if the gains observed are due to the novel approach itself or if they could be achieved by applying existing data-efficient techniques.
-	Another minor issue: when comparing with the fully supervised models, please also include comparisons with SOTA models. Additionally, consider testing how the accuracy changes if fewer data are selected/used for training. This comparison would better illustrate the proposed pipeline’s advantage over simply having a road-side transmitter providing local data to passing vehicles.

### Questions
please see my major concerns in the weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates a new scenario for constructing 3D object detectors in autonomous driving by leveraging predictions from nearby units equipped with accurate detectors. The paper addresses the challenges of viewpoint mismatches and mislocalization due to synchronization and GPS errors. The authors propose a learning pipeline called Refining & Discovering Boxes for 3D Perception from Others' Predictions (R&B-POP). This pipeline includes a distance-based curriculum that starts by learning from closer units with similar viewpoints and then improves the quality of predictions from other units through self-training. In general, while there are no surprising design elements in the methodology, the problem addressed in the paper is a new issue in this field. Learning new knowledge from the predictions of other agents appears to have significant practical application value.

### Strengths
1. The paper is well-structured, with a clear abstract, introduction, methodology, experiments, and conclusion sections that logically flow from one to the next.
2. The proposed  Refining & Discovering Boxes for 3D Perception from Others’ Predictions (R&B-POP) method is simple and effective.
3. The paper has extensive experiments and the figures are very professionally made.

### Weaknesses
1. The scenario assumed in the paper has great limitations, that is, learning knowledge from nearby agents to achieve detection. Theoretically, the learning process needs to be fast enough so that the current vehicles can predict new objects. However, I did not see the authors' analysis of the algorithm's training speed and discussion of actual deployment limitations.
2. Box ranker seems to be just an IoU scoring method, which is adopted in most detectors, such as Voxel-RCNN, PV-RCNN, they are not fundamentally different, why not directly use or discuss the limitations of existing IoU scoring method in this application?

### Questions
1. It is possible that the method can learn knowledge from other vehicles in real-time, which would expand the scope of practical applications?
2. What's the key difference between Box ranker and IoU scoring in traditional detectors?

### Soundness
3

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
4

### Summary
This papers proposes the novel idea of "learning from others predictions", i.e. using pseudo-labels from a detector deployed on another agent in the scene to train an ego agent perception model. The approach can be summarized in three parts: first, the reference detector is pre-trained on a human-annotated labels offline, and a box ranker is pre-trained on a small number of human-annotated ego frames. Next, the reference detector's pseudo-labels are generated for frames in which the reference agent is below some threshold distance from the ego agent, and are used to train the ego detector after undergoing a course-to-fine box refinement module with the box ranker. Lastly, self-training is performed using the ego detector's predictions on all available frames. Their approach, dubbed R&B-POP, is able to significantly improve AP from naively using the reference detector predictions, nearly equaling performance of training with human-annotated labels on V2V4Real Collaborative Perception dataset.

### Strengths
1. The setting introduced in this paper is novel and creative, and will inspire future work in this new research direction.
2. The method is well-explained and intuitive. Using a set of thoughtful approaches for improving psuedo-label quality and training, the authors are able to significantly improve performance over the baseline and other heuristic approaches.
3. Experiments are very thorough, and many ablation studies have been performed. 
4. The paper is well-written and organized.

### Weaknesses
1. Although the results are impressive on V2V4Real, the experiments are performed on the case where there is minimal domain shift between the two vehicle detectors (e.g. they both have the same sensors, both survey the scene from the street, etc). It would be a more interesting experimental setting with two drastically different object detectors, e.g. one on a LiDAR mounted car, and one on a stationary security camera. The authors suggest scenarios such as these as possible applications, although it's not clear that the method demonstrated in this work can be easily applied to such a scenario. Specifically, the current method relies on a shared 3D space between the reference and ego agents, which may not be easily achievable with drastically different sensor modalities and viewpoints. Furthermore, the box refinement module may not generalize well to pseudo-labels generated from a detector with a significantly different error profile than the reference detector used in the experiments. However, I understand experiments are limited by available data, so these may not be feasible in practice.
2. The authors utilize a small number of human-annotated frames from the Ego vehicle sensor data to train the box ranker, so the need for a human labeler is not completely eliminated. It would also be compelling to include experiments comparing to other semi-supervised learning approaches for 3D object detection using a similar number of labeled ego frames, to demonstrate that R&B-POP works better than conventional SSL approaches for this level of annotator budget. The current experiments only compare against a baseline of directly using the reference detector's predictions, which is not a strong comparison against other methods that also leverage unlabeled data.

### Questions
Have the authors tried training the ranker without using any annotated ego frames? As mentioned previously, it would be compelling if the need to label any of the ego data was completely eliminated.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper designs a new strategy to train the 3D object detector, i.e. learning from the detection results of a nearby unit equipped with a  pretrained detector. There are two main challenges, mis-localization and viewpoint mismatching, resulting in the inferior performance of naive self-training. To this end, this paper proposes a rank-based pseudo-label refinement module and a distance-based curriculum learning scheme. Experiments are conducted on V2V4Real and OPV2V datasets to evaluate the proposed algorithm.

### Strengths
1. This paper proposes a creative and interesting strategy for the training of object detectors. It can exploit existing pretrained detector in a flexible way regardless of their input formats and deployment compatibility. The authors provide detailed explanation about their motivation and sound justification of the feasibility.

2. The algorithm includes a relatively complex pipeline. However, each module inside it is well-motivated and has a clear role. The step-by-step improvement brought by each module is also demonstrated clearly through extensive experiments.

3. The paper is well-written. The authors organize everything well to make it easy to follow. The illustrations are also very clear, helpful for  readers to understand the content.

### Weaknesses
1. The authors are targeted for LiDAR sensors. However, if we apply this setting in practice, the camera sensors are much more ubiquitous such as the surveillance. I am wondering whether the algorithm would still work if the reference car is using camera-based detector. Given camera-based detectors are weaker, this may require high robustness of the proposed algorithm.

2. In the experiments, it may be helpful to include some baselines using other strategies for the training of detector. For example, since the algorithm requires a small number of annotated frames to train the ranker, it may alternatively apply some semi-supervised strategies to train the detector directly.

### Questions
Please consider replying to the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
