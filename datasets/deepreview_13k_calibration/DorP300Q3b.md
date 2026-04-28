# Learning Pseudo 3D Representation for Ego-centric 2D Multiple Object Tracking

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 6, 8

## Abstract
Data association is a knotty problem for 2D Multiple Object Tracking due to the object occlusion. However, in 3D space, data association is not so hard. Only with a 3D Kalman Filter, the online object tracker can associate the detections from LiDAR. In this paper, we rethink the data association in 2D MOT and utilize the 3D object representation to separate each object in the feature space. Unlike the existing depth-based MOT methods, the 3D object representation can be jointly learned with the object association module. Besides, the object’s 3D representation is learned from the video and supervised by the 2D tracking labels without additional manual annotations from LiDAR or pretrained depth estimator. With 3D object representation learning from Pseudo 3D (P3D) object labels in monocular videos, we propose a new 2D MOT paradigm, called P3DTrack. Extensive experiments show the effectiveness of our method. We achieve state-of-the-art performance on the ego-centric datasets, KITTI and Waymo Open Dataset (WOD). Code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduce a pipeline for solving 2D multiple object tracking by learning 3D object representation, 2D object appearance feature and an object association model.
The 3D object representation is learnt from Pseudo 3D object labels created from monocular videos using structure-from-motion approach.
The object association model consists of two components: GNN-based feature aggregation and a differentiable matching.
The experiments conducting on KITTI and Waymo Open Dataset demonstrate the effectiveness of the method.

### Strengths
1. Paper is well written with extensive experiments to support the proposed method.
2. A 2D MOT method that can leverage the power of 3D representation without LiDAR data or a depth estimation model.

### Weaknesses
1. The novelty of the paper is limited. The main idea is to generate pseudo 3D object labels from monocular videos so that it can be used to train the model to obtain 3D location / representation. There are main issues and details need to address about the process of generating these pseudo labels. Thus, in terms of the methodology for MOT, there is not much new development in this paper, e.g. GNN-based aggregation, association model learning and appearance using reID feature, etc. are the existing techniques in MOT literature.
2. The impact of the paper is limited given the ego-centric datasets with LiDAR data widely available.

### Questions
1. The author should provide more details on how to filter low speed of ego-motion videos and moving objects. It is also not clear how tracklet of those moving objects being handle.
2. How can the model learn if there is only loss to supervised static object? The output o^t_j can be any values.
3. I would like to see how is the quality of pseudo 3D object labels impact on the performance of learned 3D representation. One ablation study can be done is to use real 3D object labels to train the model and compare.
4. In table 3, there is an increase of ID Sw when using Baseline + 3D representation. How do you explain this behaviour? Is it suppose for 3D representation to help reduce ID Sw.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
A 2D multiple object tracker is proposed that consists of 3 steps, an object detector, a 3d descriptor and then an associator consisting of matching 3d features.   The paper provides good results on datasets from KITTI and Waymo and compares to other tracking algorithms.

### Strengths
The paper provides results on 2 driving datasets.  There is a 3 stage process, the first is acquiring depth values using SFM which is an offline process.  The 2nd stage uses a MLP to derive a 3d representation which is based on clusters of 3d points.  The third stage is the data association.  The results are good, slightly better than the other algorithms compared to.

### Weaknesses
W1. 2 data driving sets are used for testing, this is limiting to make general comments about applicability to MOT in general.
W2.  I am familiar with the datasets, they are 2 driving datasets.
W3. To make general MOT claims, there should be other datasets besides driving ones.
W4. You use SFM Colmap to get a depth estimate.  SFM only provides estimates to scale, this is not mentioned however since everything is to scale it would not matter.  I am not sure what your 3D representation adds, what if you just used the SFM clustered depth estimate as your representation, I would bet the results would be the same.
W5.  Why not?  The paper should be clear on what datasets this method works on, the authors hint that it is a general MOT solution so why not demonstrate this.
W6. Yes no relation to the pseudo 3d representation, however it should be referenced as another approach.
Q1.  the pseudo representation has not been demonstrated to add more than an average depth in your ablation studies or elsewhere.
Q2. Ok, same as DeepSort, I guess you use a graph matching.
Q3.  Ok, you are not using Kalman filter.  I did find the paper a bit difficult to follow and hard to read.
Q4.  See my previous comments.

### Questions
Is this more than just a simple tracking by detection?  You do not appear to do a predict and correct by detection or observation as would be necessitated by a kaman filter.
For all your examples, the objects are well separated by depth, what happens when they are not?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to jointly learn 3D features and their tracking association on top of existing 2D detector.
The supervision is provided via 3D MVS reconstruction of the static scene from moving camera, which allows extraction of 3D object locations and associate them with corresponding views.
This is shown to marginally improve MOTA accuracy on standard datasets.

### Strengths
The paper is well structured and readable.
The review of state of the art appears complete and up to date.
The central idea of joint association via auxiliary depth loss  and its learning approach are novel. The representation itself uses standard building blocks, but the specific architecture is of interest for the computer vision community.
Ablation study is included to validate parameter and component choices. 
Implementation details appear sufficient for replication of results.

### Weaknesses
Quantitative results constitute only incremental improvements over SOTA.
There is no analysis of failure cases, especially w.r.t non-static classes, which can be missed in the pseudo GT association due to rigid scene assumption.

### Questions
Provide class based results, i.e. for pedestrians and cars to show there is no significant static bias.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work addresses the difficult problem of data mapping in 2D multiple object tracking (MOT), particularly in the context of object occlusions. While this problem is complicated in 2D, it is much easier to handle in 3D space using a 3D Kalman filter. The authors propose a new approach that uses 3D object representations to improve data mapping in 2D MOT.

In their method, referred to as P3DTrack, they use 3D object representations learned from monocular video data and monitored by 2D tracking labels, eliminating the need for manual annotation from LiDAR or pre-trained depth estimators. This approach differs from existing depth-based MOT methods in that it learns the 3D object representation along with the object association module.

The authors conduct extensive experiments and demonstrate the effectiveness of their approach by achieving the best performance on popular egocentric datasets such as KITTI and Waymo Open Dataset (WOD). They also commit to publishing the code for their method to make it accessible for further research and practical implementation.

### Strengths
+The study presents a novel approach to the task
+The proposed method is based only on RGB 2D input, which has the advantage that the hardware required is very simple and basic.  
+Methods are evaluated on two public datasets. Choice of dataset is motivated and explained 
+The paper is well structured and written. Study is well motivated
+Clear description of implementation and methods allows reproduction of experiments
+Authors perform ablation study with various experiments showing advantages of proposed architecture over other SOTA methods.

### Weaknesses
-Not clear in which dataset the ablation was performed? Is it for both or just one? It should be done for both datasets
-The paper lacks qualitative results. Instead, there is a figure in the supplementary material that clearly explains the problem and the improvement. The paper would benefit from more qualitative results like this. This could be done as a teaser figure on the first page, giving the reader a good overview of the topic and the contribution. 
-It is not stated on which device the inference times are measured. Is it on the same GPU on which it was trained? One GPU or more? How far is it from working in real time? It is not clear and SLAM related applications require working in real time.

### Questions
1. Why do authors use the specified object detection method instead of something newer like DETR or YOLOv8?
2. How does the system work at night when visibility is reduced? Does the ability of 3D reconstruction remain the same or does it decrease?
The last "-" could be placed as question too.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
