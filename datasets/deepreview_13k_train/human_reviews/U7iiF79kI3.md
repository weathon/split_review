# CALICO: Self-Supervised Camera-LiDAR Contrastive Pre-training for BEV Perception

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Perception is crucial in the realm of autonomous driving systems, where bird's eye view (BEV)-based architectures have recently reached state-of-the-art performance. The desirability of self-supervised representation learning stems from the expensive and laborious process of annotating 2D and 3D data.  Although previous research has investigated pretraining methods for both LiDAR and camera-based 3D object detection, a unified pretraining framework for multimodal BEV perception is missing. In this study, we introduce \titlename, a novel framework that applies contrastive objectives to both LiDAR and camera backbones. Specifically, \titlename incorporates two stages: point-region contrast (PRC) and region-aware distillation (RAD). PRC better balances the region- and scene-level representation learning on the LiDAR modality and offers significant performance improvement compared to existing methods. RAD effectively achieves contrastive distillation on our self-trained teacher model. \titlename's efficacy is substantiated by extensive evaluations on 3D object detection and BEV map segmentation tasks, where it delivers significant performance improvements. Notably, \titlename outperforms the baseline method by 10.5\% and 8.6\% on NDS and mAP. Moreover, \titlename boosts the robustness of multimodal 3D object detection against adversarial attacks and corruption. Additionally, our framework can be tailored to different backbones and heads, positioning it as a promising approach for multimodal BEV perception.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, a method for LiDAR-Camera BEV fusion is explored via contrastive and self-supervised training. Using currently fashionable machinery - Lift Splat Shoot type camera encoder, Voxelnet LiDAR encoder, Transfusion decoder, etc. - for feature processing in the BEV literature, the paper adapts contrastive learning ideas for the problem. At a high level, delineations are made between between point level and region level contrast, with heuristics (e.g. clustering) being applied to extract more discriminative features. 

Evaluations are presented to compare with other contrastive methods on the NuScenes and Waymo datasets. After contrastive (unsupervised/self-supervised) pretraining, the setup is fine tuned for object detection and segmentation tasks with varying amounts of training data to show efficacy of the pretraining step. Furthermore, they also investigate robustness to adversarial attacks (inserting fake objects at some distance from ego vehicle) and corruption of data (as might occur in bad weather, degraded sensors).

### Strengths
+ Contrastive training is generally less studied in the BEV perception literature. This work adds to the body of work present in the area. 
+ The methods are generalizable, and can be applied to any setup. 
+ Effectiveness is shown across modalities in camera, camera+lidar and lidar. This is convincing. I was particularly impressed with the saliency maps with and without pre-training.

### Weaknesses
 - The paper is entirely empirical, and is as such a purely application based work. One may or may not take this as a weakness, of course. 
- On the same lines as above, the paper is heavy on tables, but I feel that qualitative analysis of where the improvement comes from is light. Some analysis through carefully designed experiments that show improvement with and without various fittings would shed insight. It appears that semantic pooling (feature rich vs feature less regions) plays a part from the figure 5, but I would like more examples of failure cases.



### Questions
- Could the authors explain how adversarial robustness is relevant in this context? 
- The clustering methods look rather empirical. More experiments on how they work in different cases would be useful. 
- Calibration error analysis: I think it would help to learn if the system can demonstrate robustness against calibration error, a common occurrence in autonomous driving setups. 
- Superfluous lines from possible prior submission (Appendix C, under 'Visualization') 

"As we mentioned in the rebuttal,camera features trained from scratch are not salient to contribute to robustness improvement."

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a self-supervised learning method of Image and point-cloud input that consists of point-region contrast (PRC) and region-aware distillation (RAD). 
Differing from the previous works, PRC utilizes both point- and region-level contrastive learning on point cloud. RAD aligns the feature maps of Images and points.
The proposed method is evaluated and shows substantial performance improvement on 3D detection and BEV map segmentation tasks on nuScene and Waymo datasets.
Ablation studies and robustness tests are also thorough to demonstrate the effectiveness of the proposed method.
After the author discussion phase, I will adjust or fix my decision.

### Strengths
[Originality]
+ Differing from the previous works, the proposed method welly utilizes both point- and region-level contrastive learning on point cloud.

[Quality & Significance]
+ The proposed method is evaluated and shows substantial performance improvement on 3D detection and BEV map segmentation tasks on nuScene and Waymo datasets.
+ Ablation studies and robustness tests are also thorough to demonstrate the effectiveness of the proposed method.

### Weaknesses
[Quality]
- The proposed method adopts the BEVFusion architecture. Lidar backbone is PointPillars, and Image backbone is Swin-T. 
Evaluation of different Lidar/Image backbone models could have a high impact. It is unclear how much the performance gain is attributed to the proposed method itself, rather than the specific choice of backbones. For example, using a more powerful lidar backbone such as VoxelNet or a transformer-based image backbone could potentially lead to different conclusions about the effectiveness of the proposed method. Furthermore, the interaction between the proposed method and different backbones is not explored, which could reveal limitations or specific advantages of the approach.
- The necessity of negative samples of P_PLRC and P_RAPC is unclear. The ablation study (w/o negative samples in P_PLRC and P_RAPC) supports the necessity. However, the ablation study could be more detailed. For example, it would be beneficial to understand the impact of the number of negative samples and how the negative samples are selected. It is also unclear if the negative samples are truly 'negative' in the sense that they do not share any semantic information with the positive samples.

### Questions
Please see the weakness part.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors try to fill the hole in pre-training for Camera-LiDAR BEV perception. The authors apply contrastive learning on both LiDAR and camera modalities in two stages. The authors develop point-wise positive and negative pairs to balance both region- and scene-level contrasts.

### Strengths
In sum, I think the proposed solution is simple and straightforward. Thus, I think the proposed approach is easily reproducible. The particular strengths I see are the following:
1. Point-wise positive and negative pairs to balance both region- and scene-level contrasts.
2. Strong empirical results across many datasets compared to prior work.
3. The paper includes ablation experiments on several of the components

### Weaknesses
I have some concerns about the proposed method:
1. How does it identify the semantic-less and semantic-rich points? How does it calculate the 4th dimension of the points? What is the range of 4th dimension of the points?
2. Is T2 identity transform in Fig. 1? If not, how does it generate the images from the original images? Were any related augmentations applied to the images, when the lidar points were changed?

### Questions
See the weakness.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
