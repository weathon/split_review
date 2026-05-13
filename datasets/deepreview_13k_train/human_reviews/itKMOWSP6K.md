# FusionFormer: A Multi-sensory Fusion in Bird's-Eye-View and Temporal Consistent Transformer for 3D Object Detection

- Decision: Reject
- Scores: 6, 3, 6, 6

## Abstract
Multi-sensor modal fusion has demonstrated strong advantages in 3D object detection tasks. However, existing methods that fuse multi-modal features require transforming features into the bird's eye view space and may lose certain information on Z-axis, thus leading to inferior performance. To this end, we propose a novel end-to-end multi-modal fusion transformer-based framework, dubbed FusionFormer, that incorporates deformable attention and residual structures within the fusion encoding module. Specifically, by developing a uniform sampling strategy, our method can easily sample from 2D image and 3D voxel features spontaneously, thus exploiting flexible adaptability and avoiding explicit transformation to the bird's eye view space during the feature concatenation process. We further implement a residual structure in our feature encoder to ensure the model's robustness in case of missing an input modality. Through extensive experiments on a popular autonomous driving benchmark dataset, nuScenes, our method achieves state-of-the-art single model performance of $72.6\%$ mAP and $75.1\%$ NDS in the 3D object detection task without test time augmentation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose a novel sensor fusion technique that generates the fused BEV feature from LiDAR voxel features and image features without compressing the Z-axis information. Unlike prior works that generate separate point BEV features and image BEV features and then fuse them, the proposed method directly generates the fused BEV feature using queries in the BEV space and deformable attention modules to interact with point voxel features and 2D image features. For each BEV query, the authors generate multiple reference points with different heights and project them back to the voxel space or image feature space for deformable attention. Besides, a temporal fusion encoder is proposed to include temporal information. The proposed method can also be used for pure image BEV feature generation with additional depth estimation networks. Experiments show that the proposed method provides competitive performance with SOTA in 3D object detection.

### Strengths
1) The paper is well-written and well-organized.
2) The multi-modal fusion problem studied in this paper is interesting and timely in Autonomous Driving. 
3) The proposed method is simple and interesting. It can be seen as an extension of BEVFormer in the multi-modal settings.

### Weaknesses
1) The proposed method is only tested in one dataset (nuScenes) and one task (3D object detection), which may not be enough to show the generalizability of the proposed sensor fusion scheme. It would be better to include more datasets (Waymo) and tasks (e.g., segmentation)

2) Though the proposed method makes use of the z-axis information, it seems to greatly increase the model complexity. To make fair comparisons with other baselines, the authors may better include complexity analysis such as FLOPS, #of parameters, and FPS

3) From Tables 1 and 2, the proposed method only provides a marginal improvement.

### Questions
In Table 1, the authors only show the result that combines temporal information. How about the one that only uses single-frame BEV features? (i.e., FusionFormer-S in Table 2). This result is important to evaluate the sensor fusion mechanism when compared with other CL baselines.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a transformer-based framework for 3D multi-modality object detection. It mainly contains spatial fusion and temporal fusion modules to fuse cross-modality features and temporal features, respectively. Experiments prove the effectiveness of the proposed modules.

### Strengths
1. The direction of cross-modality fusion for 3D object detection is promising, which could bring potential effect to practical application.
2. The whole method is simple and easy to follow.
3. The presentation and writing is clear.

### Weaknesses
1. The core idea of utilizing BEV queries for temporal and cross-modality fusion is widely used in previous methods like BEVFormer. Although the proposed method is different in detailed design, the core application of BEV queries is unchanged. This harms the technical contribution of the proposed method. Specifically, the paper does not sufficiently articulate how its approach to BEV query interaction differs fundamentally from existing methods, making it difficult to assess the true novelty of the approach. The use of BEV queries, while effective, is becoming a standard practice, and the paper needs to demonstrate a more substantial departure from existing implementations to claim a significant contribution.
2. The runtime comparisons are missing. Because this work incorporated several attention modules in different encoders, it's essential to report the latency of each module. Without a detailed breakdown of the computational cost associated with each module, it's difficult to assess the practical feasibility of the proposed method. The paper should provide a more granular analysis of runtime, including the latency of the individual attention modules, to allow for a more comprehensive evaluation of its efficiency.
3. It's interesting that the proposed method can also support the camera-only setting in Figure 4. However, the performance in Table 3 seems not good enough compared with the clear BEV modeling like BEVDepth. Does it mean the fusion-based method in Figure 4 is not a good choice for the camera-only setting? The paper should provide more insights into why the fusion-based approach does not achieve comparable performance to methods specifically designed for camera-only settings. It is unclear if the performance gap is due to the limitations of the fusion approach itself or other factors, such as the quality of the monocular depth estimation.

### Questions
Please refer to the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes a new spatial-temporal multi-modal fusion framework for 3D object detection. The proposed framework leverages 2D image features and 3D voxel features to generate BEV features and refine the features with temporal memory banks, which are then fed to the detection head to generate 3D object predictions. The method achieves leading performance on the nuScenes dataset.

### Strengths
* Overall the paper is well-written with clear technical pipeline. 
* The proposed framework can work even when missing modality inputs, showing better robustness. 
* The proposed method archives new SOTA results.

### Weaknesses
 * The motivation is not clear or sufficient. The author claims that " state-of-the-art multi-modality frameworks need explicitly compressing the voxel features into BEV space" and the proposed approach is aimed to address this issue. However, existing works like DeepInteraction maintain per-modality representations (2D perspective for camera and voxel space for LiDAR) and learn the interactions between these cross-modality interactions without the need for BEV intermediate representations.  What's the difference between the proposed approach and DeepInteraction? Please fully discuss the differences and highlight the novelty of the proposed methods with SOTA methods. 
* Lack of novelty. The proposed framework has a large overlay with both DeepInteraction and Bevformer. The BEV grid representation, temporal BEV feature fusion, and deformable attention have already been used in Bevformer and the cross-modality interaction of 2D features and 3D features have also been proposed in DeepInteractions. I would encourage the author to highlight the novelty and differences. The core contribution of this work is unclear, as it appears to combine existing techniques without a significant novel component. The use of voxel features, while a distinction from DeepInteraction's BEV representation, is not sufficiently explored in terms of its impact on the overall system performance or its interaction with other components. The argument for a unified multimodal fusion method is not strongly supported, as the method seems to be a combination of existing approaches.
* The memory banks contain all the previous BEV features, which is very time-consuming for learning the interactions of current BEV feature maps and previous ones. Why not choose a recurrent-style temporal fusion mechanism? The computational cost of storing and processing all previous BEV features needs to be justified, especially given the potential for redundancy and the availability of more efficient recurrent-style approaches. The paper should provide a detailed analysis of the computational complexity and memory requirements of the proposed method, comparing it with alternative temporal fusion techniques.
* In the abstract and introduction, the author claims one of the main contributions is the residual architecture. However, in the method section, it is rarely mentioned. The role and impact of the residual connections are not clearly articulated in the method section, and the paper does not provide sufficient evidence to support the claim that they are a key contribution. The paper should provide a detailed analysis of the impact of the residual connections on the model's performance, especially in scenarios with missing modality inputs.
* When comparing with other SOTAs, is temporal information used for all the other methods for a fair comparison?

### Questions
* The BEV visualization in Figure 6 (b) of the proposed method looks very good. Is this the result of a pure camera branch or generated from both LiDAR and camera inputs? What is the feature visualization of LiDAR BEV feature map?  How are the visual improvements after adding the camera modality?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a multi-modal fusion transformer-based framework for 3D object detection. The idea of this paper is intuitive and this paper is easy to understand. The performance on nuScenes is good.

### Strengths
1.This paper is easy to read.  
2.The performance of the model in this paper show superiority in nuScenes.  
3.The idea is intuitive.

### Weaknesses
1.Only one dataset is used in this paper. The generality of the framework should be analyized.  
2.In introduction, Fig.1(b) is not compared with their method in details.  
3.The most  baselines only consider LiDAR and camera, which are not fair to compare. Can you compare with them without temporal information? And this can also further verify the superiority of  Multi-modal fusion encoder.  
4. The two topics, i.e., multi-modal fusion and temporal consistence, are different, causing that the focus of this paper is unclear.

### Questions
Refer to the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
