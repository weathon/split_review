# 3D Feature Prediction for Masked-AutoEncoder-Based Point Cloud Pretraining

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Masked autoencoders (MAE) have recently been introduced to 3D self-supervised pretraining for point clouds due to their great success in NLP and computer vision. Unlike MAEs used in the image domain, where the pretext task is to restore features at the masked pixels, such as colors, the existing 3D MAE works reconstruct the missing geometry only, i.e, the location of the masked points. In contrast to previous studies, we advocate that point location recovery is inessential and restoring intrinsic point features is much superior. To this end, we propose to ignore point position reconstruction and recover high-order features at masked points including surface normals and surface variations, through a novel attention-based decoder which is independent of the encoder design. We validate the effectiveness of our pretext task and decoder design using different encoder structures for 3D training and demonstrate the advantages of our pretrained networks on various point cloud analysis tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a pre-training task for 3D encoders, so, later, can lead to improved performance when fine-tuned on a downstream task. The pre-training objective is the prediction of point-surface properties such as normal or surface variation from masked regions of the input point cloud.

### Strengths
The paper proposes an alternative to point coordinates prediction on a mask auto-encoder setup. Sampling point coordinates can be difficult for decoder architectures as the ones used by previous works. However, by fixing the point coordinate in the decoder these problems disappear and the task becomes to predict shape properties around the queried point.

### Weaknesses
I like the main idea of the paper, it is well presented and presents a significant improvement over previous works for most of the task. However, my main concern is not only related to this work in particular but to this line of works where they focus on tasks related to single objects. I have been playing around with these datasets for many years already, and I can say that datasets such as classification on ModelNet40, and segmentation on ShapeNet are relatively "easy", there is a lot of noise in the annotations, and I believe the improvements presented by current methods is simply overfitting to this specific data set. In other subfields of computer vision, a pre-training paper that is only evaluated on MNIST or CIFAR10 would not be accepted, but for some reason, they do for point clouds. So, I don't find these works convincing since the reported results and architectures usually do not translate to more challenging tasks such as semantic segmentation or instance segmentation on real 3D scans. That being said, this work presents results on the task of object detection of ScanNet and SUN-RGBD, which I believe is the right direction. However, I think more results reported on other tasks such as semantic or instance segmentation should be necessary to determine the quality of the pre-training strategy. Therefore, I will rate this paper marginally below the acceptance but I will be happy to see additional results during the rebuttal phase.

### Questions
I would encourage the authors to include more challenging tasks such as semantic and instance segmentation of 3D scans.

### Soundness
2 fair

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
This paper proposes a self-supervised learning method from point cloud. Typically, this paper addresses the importance of using surface normal and surface variance instead of using point location as proposed by the previous studies. The idea is straightforward and easy-to-understand. The experiments demonstrate that the efficacy of the proposed method. Moreover, the ablation study consistently proves the addressed issue by the authors.

### Strengths
The authors address the importance of the geometric measurements for the usage of pre-training the network. Typically, using surface normal as surface variation are meaningful in point cloud based understanding. Typically, the authors provide the various experiments such as backbone architectures, loss designs, and downstream task evaluations. I really enjoyed reading this paper.

### Weaknesses
W-1. Analysis of 2D/3D masked autoencoders.

In the manuscript, the authors commented that __"These designs make an intrinsic difference from 2D MSMs, where there is no need to recover masked pixel locations."__

It is true. I understand the analysis by the authors. When we think of the vanilla MAE, it also takes a masked image as an input and predicts the color information, not its pixel location. However, when we think of the nature of the point cloud, it is sparse, irregular, and unordered. Even, I would say _raw point cloud_ naturally does not involve color information. Accordingly, it is not feasible to extend the concept of the MAE for the 2D image into the MAE for the 3D points. In my opinion, the authors should have written such a clear understanding of MAE for 3D points. 

W-2. Details in computing surface normal and surface variance on scene-level experiments.
While the various object-level datasets, such as shapenet, are synthetically created, the real-world points are captured by the sensors. Due to such difference, raw point cloud from the real world naturally involves lots of noise, which could be an issue when computing surface normal using PCA. So I wonder how the authors solve this issue when conducting experiments on Sec. 4-4 in the manuscripts.

W-3. Insightful analysis
I truly agree that the proposed experiments demonstrate that the surface normal and surface variance are important measurements for self-supervising learning using 3D points. Technically, I also agree with such an observation. However, I wonder why such an approach brings performance improvement. Is there any geometric analysis? Based on the manuscript, this approach can be viewed as a naive extension of the Point-MAE that additionally uses other geometric measurements. 

I want to know the author's own analysis of such problem setup and insights.

### Questions
Alongside with the addressed weakness, I have one minor question.

Q-1. __Is there any reason that authors did not conduct experiments on the S3DIS dataset using 3D semantic segmentation?
If there are some reasonable and meaningful results, I can convince the efficacy of this work. Otherwise, this work could be understood as naive extension.__

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a point cloud pre-training method to improve the downstream tasks’ performances. More specifically, instead of predicting point positions by a masked autoencoder, the authors propose to recover high-order features at masked points including surface normals and surface variations through a novel attention-based decoder. To verify the effectiveness of the method, various point cloud analysis tasks have been tested, and promising results have been achieved.

### Strengths
1. The idea is interesting, and the results are promising.
2. Extensive experiments are conducted with SOTA performances.
3. The paper is clearly written and well-organized.

### Weaknesses
It seems that the ablation study shown in Table 4 failed to support the idea that it is essential to disregard point position recovery, since at the same time to predict point positions using PointMAE, the decoder architecture is also changed when using MaskFeat3D architecture. To make a fairer comparison, the same decoder architecture from MaskFeat3D should be used to predict point position as well.

### Questions
Since the authors claim that it is essential to disregard point position recovery. Hence, how to understand that predicting point positions actually enhances the performances when using PointMAE in Table 4?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors apply the self-supervised pretraining paradigm of masked signal modeling to point cloud pretraining. They propose a novel approach called MaskFeat3D, which focuses on recovering high-order features of masked points rather than their locations. Additionally, they propose an encoder-agnostic attention-based decoder. The effectiveness of the proposed method is evaluated through experiments conducted on the ScanObjectNN dataset for shape classification and the ShapeNetPart dataset for shape part segmentation.

### Strengths
- The authors present evidence that the recovery of high-order point features yields more effective results compared to the recovery of point positions for 3D masked signal modeling.
- A novel encoder-agnostic attention-based decoder is proposed by the authors to accurately regress the high-order features of masked points.
- The paper is well-written and provides clear explanations, making it easy to follow.

### Weaknesses
 - It appears that this is not the first work in 3D masked signal modeling that focuses on recovering high-order features of masked points. For example, MaskSurfel (Zhang et al.) specifically aims to recover surface normals of points. This similarity with previous work may diminish the novelty of the paper.
- The results on the ScanObjectNN dataset indicate that Point-MA2E outperforms MaskFeat3D significantly; however, this comparison is not included in the paper.
- To assess the effectiveness of the decoder, it is recommended to include results obtained by combining the block features and masked queries, and feeding them into self-attention blocks of the same depth, similar to the MAE approach, with points used as the positional embeddings.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
