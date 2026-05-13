# Uncertainty Estimation for 3D Object Detection via Evidential Learning

- Decision: Reject
- Scores: 5, 8, 3, 3

## Abstract
3D object detection is an essential task for computer vision applications in autonomous vehicles and robotics. 
However, models often struggle to quantify detection reliability, leading to poor performance on unfamiliar scenes.
We introduce a framework for quantifying uncertainty in 3D object detection by leveraging an evidential learning loss on Bird's Eye View representations in the 3D detector.
These uncertainty estimates require minimal computational overhead and are generalizable across different architectures.
We demonstrate both the efficacy and importance of these uncertainty estimates on identifying out-of-distribution scenes, poorly localized objects, and missing (false negative) detections; our framework consistently improves over baselines by 10-20\% on average.
Finally, we integrate this suite of tasks into a system where a 3D object detector auto-labels driving scenes and our uncertainty estimates verify label correctness before the labels are used to train a second model. Here, our uncertainty-driven verification results in a 1\% improvement in mAP and a 1-2\% improvement in NDS.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper discusses the importance of 3D object detection from LiDAR and camera images and how deep neural networks, while excellent at detections, struggle with assessing reliability. The authors propose a computationally efficient framework motivated by Evidential Deep Learning (EDL), which outputs parameters for a distribution over class probabilities, referred to as a second-order distribution. This allows the model to estimate both the probability of an object's presence and the associated uncertainty.

The authors extend this framework to 3D object detection by adapting the model architecture and loss function to generate uncertainty estimates. They replace the standard heatmap head with an EDL head, which predicts both object presence probabilities and uncertainty. The loss function is designed to address class imbalance and focuses on harder, misclassified examples during training.

The authors conduct the experiments on three downstream applications: detecting out-of-distribution scenes, assessing the quality of predicted bounding boxes, and identifying missed objects. The authors also integrate these tasks into an auto-labeling pipeline where uncertainty estimates are used to verify label correctness before training a second model, resulting in improvements in mAP and NDS.

### Strengths
The paper is well-organized and clearly written. The introduction effectively outlines the problem and the motivation behind the work. The methodology section is detailed, providing clear explanations of the EDL framework, the model architecture, and the loss function. The results are presented in a manner that is easy to understand, with comprehensive tables and figures that clearly illustrate the performance improvements.

### Weaknesses
The proposed methodology integrates an advanced annotation phase to augment object detection capabilities. However, it does not adequately address the limitations of traditional approaches, necessitating continued extensive re-annotation efforts without a significant leap in detection efficiency. Moreover, the key to enhancing performance in real-time robotics applications, particularly in autonomous driving, lies in the effective management of uncertainty during the detection phase, rather than the re-annotation process. This is crucial for applications such as motion planning, which requires sophisticated algorithms capable of adapting to dynamic and unpredictable environments.

The authors have conducted three downstream experiments to validate their approach: detecting out-of-distribution scenes, assessing the quality of predicted bounding boxes, and identifying missed objects. These experiments are essential for understanding the robustness of the detection system. However, the paper does not provide clear evidence on how the uncertainty estimation directly benefits real autonomous driving applications, such as motion planning. Therefore, while the experiments conducted are valuable, there is a need to demonstrate how uncertainty estimation translates into tangible benefits for autonomous driving, particularly in the context of motion planning and real-time decision-making.

======
 
**Post-rebuttal**:

- High-Quality Annotation's Essential Role in Object Detection: The precision of object detection models is fundamentally contingent upon the quality of the annotations they are trained on. This manuscript innovatively incorporates uncertainty estimation to curtail the number of objects necessitating re-annotation, thereby optimizing the annotation process. However, it is crucial to acknowledge that while uncertainty estimation aids in this optimization, the ultimate accuracy of object detection models is still predicated on the fidelity of the re-annotation efforts.

- Uncertainty Estimation's Dual Role: The authors have overlooked a pivotal aspect of uncertainty estimation—its role in risk management. This component is particularly significant for autonomous driving systems, where it can significantly bolster safety by providing a measure of confidence in detection outcomes. The initial submission underplays this aspect, which diminishes the perceived value of uncertainty estimation in practical applications.

- Enhancing the Contribution of Uncertainty Estimation: To rectify this oversight, I suggest that the authors expand on how uncertainty estimation can be integrated into risk assessment protocols for autonomous vehicles. By doing so, they can highlight the dual benefits of their approach: not only does it streamline the annotation process, but it also enhances the reliability and safety of autonomous systems through robust risk management.

### Questions
1. Please provide details in the auto-label pipeline: no reference and description referring to the auto-label pipeline.

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper tackles the crucial issue of uncertainty estimation in 3D object detection for autonomous driving. It applies Evidential Deep Learning (EDL) to Bird’s Eye View (BEV) representations to provide efficient uncertainty estimates. Experiments show that this approach improves detection reliability, especially in challenging cases like out-of-distribution scenes and missed objects.

### Strengths
S1：The theoretical foundation is solid, with a novel adaptation of Evidential Deep Learning to 3D detection.

S2：Experimental results are promising and show meaningful improvements in several key tasks for autonomous driving.

S3：The approach appears innovative and applicable to real-world challenges in autonomous driving.

### Weaknesses
W1: The method mainly focuses on providing uncertainty estimates without apparent direct improvement in detection accuracy itself.

W2: While experiments cover LiDAR and LiDAR+Camera setups, a significant portion of current detection models are Camera-only; hence, the framework lacks some supportion in experiment to demenstrate the generality in this area.

W3: The paper claims efficiency advantages over traditional methods, suggesting suitability for real-time applications like driving; however, it does not provide a direct comparison in terms of computational efficiency. It remains unclear how much this added uncertainty estimation slows down the original model.

### Questions
Q1: It's well understood that traditional methods like MC Dropout and Deep Ensembles have high computational costs due to repeated inference, which is why they’re increasingly less popular in uncertainty quantification for autonomous driving. Given this shift, the question is: compared to existing UQ directly modeling methods, such as [1], does your evidential learning approach offer any distinct advantages?

[1] Uncertainty Quantification of Collaborative Detection for Self-Driving

Q2: Is it possible to extend your approach to other BEV-based perception tasks, such as occupancy prediction?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose a new method to quantify the uncertainty in 3D detection. By applying evidential learning on a bird's eye view feature map to predict the probability distribution of each Cell category, the uncertainty of the predicted bounding box can be obtained. The method is easy to implement and can be easily integrated into a 3D detector. The authors applied the uncertainty to several downstream tasks, comparing it with different baselines.

### Strengths
This paper investigates an important problem - uncertainty quantification for 3D detection results. The use of evidential learning enables a good efficiency in the inference stage, which meets the requirements of autonomous driving. A prior-based regularization term is added to the loss function to correct the Beta distribution, which is able to reduce the overconfidence of the model.

### Weaknesses
This paper lacks novelty, the method of quantifying uncertainty is not much different from that in paper [1]. Although the paper [1] is quantifying the uncertainty in the predictions of 2D detection models, quantifying uncertainty based on BEV features in this paper is not much different from that based on 2D image features. And also the quantification of uncertainty in the bounding box size is missing compared to the paper [1].

The experimental setup in this paper lacks transparency and lacks sufficient description for comparing methods. The 3D detection output is a bounding box defined by multiple parameters, each containing uncertainty. It is not clear in this paper which parameter uncertainties are included in the uncertainty generated by the comparison methods. Is it only the uncertainty of the center position as in the method proposed in this paper? The sampling-based approach to obtaining uncertainty in the predicted bounding boxes suffers from the problem of alignment, i.e., the outputs of the bounding boxes from different networks differ in number, location, and size, and the authors do not explain how it aggregates multiple predicted bounding boxes to derive the uncertainty.

The experiments presented in Table 2 should also be compared to the AUC metric of the original detector itself, i.e., the AUC of Confidence-IoU. In practice we usually use confidence to distinguish between correct and incorrect predictions. Whereas the experiments in Table 2 are designed to demonstrate that after quantifying uncertainty, using the uncertainty can better distinguish between correct and incorrect predictions. Therefore a comparison of confidence-IoU AUC is needed. Uncertainty needs to exceed the discriminative ability of the confidence to prove its suitability for this task.

In the missed object detection task proposed by the authors, the metric for judging the correctness of the predictions is not aligned with the previous section, i.e., IoU0.3. Using only the center distance to judge the correctness of the detection box is too lenient. In the authors' proposed method, all the cells with a prediction probability less than 5% are taken for missed object detection, which will make the network deal with a large number of background cells and will lead to a great sacrifice in computational efficiency. The low precision, recall, and F1-score in Table 3 illustrate that the improvement in the overall detection performance of the network is not significant. In practice, the simplest way to improve recall is to relax the confidence threshold, and whether the authors' proposed method is better than this simplest method needs to be proved experimentally.

The experimental results in Table 4 do not reflect that the method proposed by the authors provides significant enhancement. Moreover, the data in this table are not the average results of multiple experiments, which cannot provide a good convincing argument.

### Questions
In lines 427-428, why is the uncertainty of the predicted bounding box taken from the minimum value in the set?

The experiments in Table 2 present the quality of uncertainty quantification only from the perspective of AUC, can you add the results of the ECE metrics to provide proof from the calibration perspective?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper focuses on uncertainty estimation in 3D object detection. Three tasks are used to testify to the effectiveness of evaluation uncertainty: (1) Out-of-distribution (OOD) scene detection, (2) Bounding-box quality assessment, and (3) Missed objects detection. The uncertainty estimation is conducted by doubling the output channel of existing methods and using the extra channel to estimate the uncertainty value in the BEV. Experimentally, uncertainty estimation is demonstrated for the three tasks mentioned above. Also, an auto-labeling pipeline using uncertainty improves performance on the 3D detection task.

### Strengths
- The paper's motivation is interesting, as most existing works only focus on improving model performance. Uncertainty estimation should play an important role in safety-critical applications, such as autonomous driving.

### Weaknesses
 - The paper is a bit hard to follow. Most of the content describes different settings for different subtasks. However, the key contribution is hard to find, rather than applying uncertainty estimation to 3D object detection.
- Experimentally, conducting experiments simultaneously on camera-only, LiDAR-only, and fusion-based methods seems unnecessary. The input modality is unlikely to affect the main conclusion of the paper.
- Including the Waymo data set is only for constructing out-distribution data, which seems unnecessary (see Questions).
- The improvement is very marginal for the experimental results in section 4.5, which might also result from different random seeds.

### Questions
- In lines 366-368, the authors treat data from nuScenes as in-distribution data and data from Waymo as out-distribution data. This setting is quite doubtable since the number of cameras, camera settings, LiDAR settings, etc. are completely different. Differing from the paper cited in line 369 ([1]), which uses LiDAR-only detectors, this paper uses also camera-only and fusion-based methods. It is curious how the authors handle different numbers of cameras. As for the construction of OOD data, a straightforward method that comes to my mind is to treat daytime data from nuScenes as in-distribution data and nighttime data from nuScenes as out-distribution data. Why did the authors choose this setting mentioned in the paper?
- In line 459, the authors choose 15 as the number of potential missing objects. However, as discussed in the first paragraph in section 4.4, the uncertainty value identifies missing objects. It is double the choice of the number 15, and also, why not using the thresholds on uncertainty to estimate the locations of missing objects?
- The only experiment directly related to 3D object detection is section 4.5, where the experimental settings are a bit complicated. Does some kind of standard process exist in previous work? And why did the author choose these experimental settings?

[1] Wang, Yan, et al. "Train in germany, test in the usa: Making 3d object detectors generalize." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020.

### Soundness
1

### Presentation
2

### Contribution
1
