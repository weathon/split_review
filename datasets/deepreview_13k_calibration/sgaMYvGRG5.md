# $\alpha$-OCC: Uncertainty-Aware Camera-based 3D Semantic Occupancy Prediction

- Decision: Reject
- Avg Score: 5.80
- Scores: 6, 5, 6, 6, 6

## Abstract
In the realm of autonomous vehicle (AV) perception, comprehending 3D scenes is paramount for tasks such as planning and mapping. Camera-based 3D Semantic Occupancy Prediction (OCC) aims to infer scene geometry and semantics from limited observations. While it has gained popularity due to affordability and rich visual cues, existing methods often neglect the inherent uncertainty in models. To address this, we propose an uncertainty-aware camera-based 3D semantic occupancy prediction method ($\alpha$-OCC). Our approach includes an uncertainty propagation framework (Depth-UP) from depth models to enhance geometry completion (up to 11.58\% improvement) and semantic segmentation (up to 12.95\% improvement) for a variety of OCC models. Additionally, we propose a hierarchical conformal prediction (HCP) method to quantify OCC uncertainty, effectively addressing the high-level class imbalance in OCC datasets. On the geometry level, we present a novel KL-based score function that significantly improves the occupied recall of safety-critical classes (45\% improvement) with minimal performance overhead (3.4\% reduction). For uncertainty quantification, we demonstrate the ability to achieve smaller prediction set sizes while maintaining a defined coverage guarantee. Compared with baselines, it reduces up to 92\% set size. Our contributions represent significant advancements in OCC accuracy and robustness, marking a noteworthy step forward in autonomous perception systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors focus on improving the Camera-based 3D semantic occupancy prediction (OCC) task by introducing the geometric the geometric uncertainty. 

Specifically, an uncertainty propagation network named Depth-UP is used to predict depth values and pixel-wise uncertainty as well. The predicted uncertainty, together with the depth map the image features are used for semantic occupancy prediction.

In order to effectively utilize the uncertainty, a hierarchical conformal prediction (HCP) method is proposed to quantity the OCC uncertainty, which effectively addresses the class im-balance in OCC datasets. 

Additionally, a KL-based score function is leveraged to improve the occupied recall of safety-critical classes.

Experiments on public SemanticKITTI and KITTI360 datasets demonstrate the effectiveness of the proposed uncertainty propagation and uncertainty quantification strategies.

### Strengths
1.	Interesting uncertainty propagation for geometric completion. The uncertainty exists in almost all computer vision tasks, and it is also very important to the OCC task. In this paper, the authors use the network to predict the uncertainty for each pixel is straightforward. The strategy of computing the uncertainty of each 3D voxel by accumulating all potential rays though the voxel makes sense. Experiments also show the improvements in the geometry completion task.

2.	Useful hierarchical conformal prediction (HCP). The proposed HCP, compared to SCP and CCP, are specially designed for vary and safety-critic classes from the perspective of both geometric and semantic levels. A KL-based score function enforces these classes to have a higher prediction during the training process. 

3.	Good performance. Experiments on SemanticKITTI and KITTI360 datasets show the proposed uncertainty propagation and uncertainty quantification strategies achieve significant improvements when they are applied to two basic models VoxFormer and OccFormer.

4.	The paper is well-organized and easy to read.

### Weaknesses
The proposed method is simple and easy to follow, so I don’t have many concerns about this paper. 

In L209, the authors say that the depth prediction model is retrained to allow to regress both depth values and uncertainties. I am curious about the performance of the newly trained depth model and the basic depth model. If the joint training improves the depth prediction？

Also in the experiments, do the two base models (indicated as Base) use the original depth prediction networks or the newly trained networks with uncertainty branch removed?

Other minor mistakes

a.	L051, (1 + beta%) -> (1 + beta)?

b.	L356-357, in Table 1, 55.78 (+2.34) -> 55.78 (+1.60)

### Questions
Overall, I think this is an interesting paper. The uncertainty propagation improves the geometry completion performance and the HCP improves the accuracy of the safety-critic classes in class im-balanced datasets. As I am not an expert in this area, it would also be very important to see other reviewers’ comments before making the final decision.

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
This paper proposes to incorporate uncertainty inherent in models for the camera-based semantic occupancy prediction. The presented framework integrates the uncertainty propagation (Depth-UP) from depth models to improve occupancy prediction performance in both geometry and semantics. A hierarchical conformal prediction (HCP) method is designed to quantify occupancy uncertainty effectively under high-level class imbalance. The extensive experiments demonstrate the effectiveness of proposed α-OCC.

### Strengths
(1) This paper leverages uncertainty to lift 2D features to 3D space and designs a post-processing module to improve the accuracy of the classification head. The motivation throughout the paper is strong, and the writing is relatively clear, with detailed explanations of the background knowledge and the proposed method.

(2) The paper presents experiments conducted on the SemanticKITTI and KITTI360 datasets, demonstrating improvements in both geometric and semantic predictions. Additionally, it provides relevant performance metrics for uncertainty quantification.

### Weaknesses
(1) The change in the number of parameters after adding the module should be provided in the ablation study section.

(2) The proposed Depth-Up and HCP modules appear to be relatively independent. I would like to understand the relationship between them.

(3) Could you provide an evaluation of how the estimated uncertainty varies with distance?

(4) I would like to know whether the uncertainty of the final predicted semantic occupancy has been improved, specifically with respect to ECE-related metrics, as provided in methods like PaSCo[1].

### Questions
(1) The change in the number of parameters after adding the module should be provided in the ablation study section.

(2) The proposed Depth-Up and HCP modules appear to be relatively independent. I would like to understand the relationship between them.

(3) Could you provide an evaluation of how the estimated uncertainty varies with distance?

(4) I would like to know whether the uncertainty of the final predicted semantic occupancy has been improved, specifically with respect to ECE-related metrics, as provided in methods like PaSCo[1].

[1] Cao A Q, Dai A, de Charette R. Pasco: Urban 3d panoptic scene completion with uncertainty awareness[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024: 14554-14564.

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
3

### Summary
The paper introduces α-OCC, an uncertainty-aware camera-based 3D semantic occupancy prediction method designed for autonomous vehicle (AV) perception systems. The method aims to enhance the understanding of 3D scenes, which is crucial for tasks like planning and mapping. It addresses the limitations of existing methods that often overlook the inherent uncertainty in models. The paper achieves uncertainty modeling by incorporating a depth distribution in the initialization process of the ocupancy prediction process. The paper concludes that by integrating uncertainty quantification into OCC tasks, significant advancements in accuracy and robustness can be achieved, particularly for rare safety-critical classes, thus reducing potential risks for AVs.

### Strengths
1. The authors propose Depth-UP to improve geometry completion and semantic segmentation by propagating uncertainty from depth models to occupancy prediction models. This framework enhances the performance of various OCC models.
2. To tackle class imbalance in OCC datasets, the paper introduces HCP, which quantifies the uncertainty of OCC and improves the recall of safety-critical classes like pedestrians and bicyclists.
3. The paper demonstrates significant improvements in OCC accuracy and robustness. Depth-UP achieves up to 11.58% improvement in geometry completion and 12.95% in semantic segmentation. HCP improves the occupied recall of safety-critical classes by 45% with only a 3.4% reduction in performance overhead.
4. The paper shows the ability to achieve smaller prediction set sizes while maintaining a defined coverage guarantee, reducing set size by up to 92% compared to baselines.
5. Extensive experiments on two OCC models (VoxFormer and OccFormer) and two datasets (SemanticKITTI and KITTI360) validate the effectiveness of the proposed α-OCC approach.

### Weaknesses
1. The paper incorporates uncertainty modeling into occupancy prediciton. Despite its good preformance, the paper does not provide an explicit illustration of what uncertainty means in occupancy prediction, and why it is important, and how it could benefit occupancy prediction.
2. The paper does not compare against state of the art methods on SemanticKITTI and KITTI360.

### Questions
1. Could you please explain what uncertainty means in occupancy prediction, and why it is important, and how it could benefit occupancy prediction as raised in weakness 1.
2. Why do you not compare against SOTA methods on the two datasets?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents an uncertainty-aware camera-based method for 3D semantic occupancy prediction called $\alpha$-OCC. This approach includes Depth-UP that propagates depth uncertainty, and HCP that quantifies the uncertainty of the OCC model, which enhance the performance of geometry prediction and semantic segmentation, while also improving the recall of rare safety-critical classes. The authors test their methods using the SemanticKITTI and KITTI360 datasets based on VoxFormer and OccFormer.

### Strengths
This paper is well-written and presents the ignore of depth uncertainty hinder the performance of geometry and semantics in OCC models. The authors conduct extensive experiments to demonstrate the effectiveness of their uncertainty propagation and quantification.

### Weaknesses
1. Table 1 shows improved scores across each metric, while Figure 4 provides better visualizations for the safety-critical class. In Table 4, the mIoU for the "person" category decreases slightly, and the mIoU for "bicyclist" also declines a bit on SemanticKITTI datasets. Could the authors explain the relationship between the higher recall and some decreasing mIoU?
2. the authors take experiments mainly on SemanticKITTI and KITTI360, Could it keep the performance of the methods for propagate uncertainty in multi-cameras datasets, such as NuScenes or Waymo?

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

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
This paper proposes an uncertainty-aware camera-based 3D semantic occupancy prediction method, named α-OCC. Specifically, it addresses two key challenges in occupancy prediction: depth estimation uncertainty and high-level class imbalance. To tackle these challenges, it introduces uncertainty propagation (Depth-UP) from depth models to enhance occupancy prediction performance and proposes a novel hierarchical conformal prediction (HCP) method to improve the recall of rare classes. The effectiveness of the proposed approach is validated through experiments on two methods (VoxFormer and OccFormer) and two datasets (SemanticKITTI and KITTI360).

### Strengths
1. The paper is well-structured, clearly identifying two key challenges and outlining corresponding solutions.
2. Although rare classes have little impact on the performance, they hold significant value for real-world safety.
3. This work makes the first attempt to propose the uncertainty propagation framework, Depth-UP, to improve OCC performance.

### Weaknesses
1. Considering that the challenges addressed in the paper are reflected across almost all datasets, the experiments conducted solely on the KITTI dataset lack some persuasiveness. In the camera-based occupancy prediction field, more recent methods tend to evaluate on the nuScenes occupancy dataset. Therefore, performance results on nuScenes would be more compelling.
2. How was the value of alpha determined in the experiments, and how should it be decided in practical applications?
3. From Figure 2, it seems that the semantic prediction is directly based on the depth prediction as input, which appears somewhat odd.

### Questions
1. It seems that the ground truth in the third row of Figure 4 appears to be incorrect. Why is the entire middle row filled with cars?
2. In the text, does "Hierarchical" in HCP refer to first distinguishing whether it is occupied and then identifying the specific category?
3. From Figure 2, it seems that the semantic prediction is directly based on the depth prediction as input, which appears somewhat odd.

### Soundness
3

### Presentation
2

### Contribution
3
