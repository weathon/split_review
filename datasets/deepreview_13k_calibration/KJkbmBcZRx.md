# Block-to-Scene Pre-training for Point Cloud Hybrid-Domain Masked Autoencoders

- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 5, 5, 5, 6

## Abstract
Point clouds, as a primary representation of 3D data, can be categorized into scene domain point clouds and object domain point clouds based on the modeled content. Masked autoencoders (MAE) have become the mainstream paradigm in point clouds self-supervised learning. However, existing MAE-based methods are domain-specific, limiting the model's generalization. In this paper, we propose to pre-train a general Point cloud Hybrid-Domain Masked AutoEncoder (PointHDMAE) via a block-to-scene pre-training strategy. We first propose a hybrid-domain masked autoencoder consisting of an encoder and decoder belonging to the scene domain and object domain, respectively. The object domain encoder specializes in handling object point clouds and multiple shared object encoders assist the scene domain encoder in analyzing the scene point clouds.  Furthermore, we propose a block-to-scene strategy to pre-train our hybrid-domain model. Specifically, we first randomly select point blocks within a scene and apply a set of transformations to convert each point block coordinates from the scene space to the object space. Then, we employ an object-level mask and reconstruction pipeline to recover the masked points of each block, enabling the object encoder to learn a universal object representation. Finally, we introduce a scene-level block position regression pipeline, which utilizes the blocks' features in the object space to regress these blocks' initial positions within the scene space, facilitating the learning of scene representations.  Extensive experiments across different datasets and tasks demonstrate the generalization and superiority of our hybrid-domain model.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper propose PointHDMAE, a hybrid-domain masked autoencoder pre-trained with a block-to-scene strategy. The method uses a hybrid architecture with separate encoders for scene and object data, aiming to address the generalization limitations of existing domain-specific MAE models.

The model shows promising results across various downstream tasks, demonstrating its generalization capability in handling both object and scene point cloud data without additional domain adaptation training.

### Strengths
1. The motivation is clear and valid. Developing a general model for 3D point cloud representation learning is indeed valuable.

2. The experimental results are comprehensive, covering a range of tasks such as point cloud classification, part segmentation, object detection, and completion.

### Weaknesses
1. Novelty alone is not enough. While the motivation is reasonable, the proposed "general autoencoder" is essentially a combination of separate scene-level and object-level encoders, which lacks true innovation. If that's the approach, why not simply use combined two-level pre-trained branches with a switch to create a general model?

2. Why are the '#Params (M)' values the same with and without PointHDMAE in Table 9?

3. The result for Point-M2AE is missing in Tables 2 and 3.

4. Separating Multimodal Self-Supervised Learning and Single Modal Self-Supervised Learning seems unnecessary. While some methods benefit from the added knowledge of other modalities, PointHD-MAE could also gain from additional training data. Comparisons should be made based on performance, not restricted by modality or data differences.

5. More qualitative results are needed.

6. Presentation consistency would improve readability, such as highlighting and bolding text in tables.

7. The manuscript does not discuss any limitations.

### Questions
Please kindly see the weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, a point cloud hybrid-domain masked autoencoder is proposed to improve the generalization ability. Specifically, the authors
address the challenge of inconsistent input data by using domain-specific encoders to process data from their respective domains.
A block-to-scene pretraining strategy is proposed to regress the block position and reconstruct the block point. Results on several datasets and tasks demonstrate the effectiveness of the proposed method.

### Strengths
1. This paper is well motivated.
2. The proposed method outperforms existing methods under different tasks and datasets.

### Weaknesses
1. In the pretraining stage, it's strange that only scene-level point cloud data is used. From the motivation of this paper, a more natural way is to utilize both scene-level and object-level point cloud for pretraining. For example, the block reconstruction can be also applied to object-level point cloud.
2. Some details are unclear. In section 4.1, the authors claim that "we can also leverage pre-trained object point cloud models on the ShapeNet55 (Chang et al., 2015) dataset to initialize our object-level models". But it's unclear whether this strategy is used.
3. Lack of dicussion with related works. The key component, block-to-scene strategy, is very similar with UP-DETR [1]. It seems that the proposed strategy is a simple extension of UP-DETR from image to point cloud, without carefully considering the problem faced by this task.
4. Compared with existing methods. The proposed method is much more complicated, training cost, parameter numbers, et al. should be reported for fair comparison.

[1] UP-DETR: Unsupervised Pre-training for Object Detection with Transformers. TPAMI 2022.

### Questions
Please address my concerns about the "weakness".

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
4

### Summary
This paper addresses the limitations of existing masked autoencoder (MAE) methods for point cloud self-supervised learning, which are often domain-specific and hinder generalization. The authors introduce a novel Point cloud Hybrid-Domain Masked AutoEncoder (PointHD-MAE) that employs a block-to-scene pre-training strategy. This hybrid model comprises an encoder for the object domain and a decoder for the scene domain, allowing for specialized handling of both scene and object point clouds. The pre-training process involves selecting point blocks from scenes and transforming their coordinates to the object space, using an object-level mask and reconstruction pipeline to recover masked points and learn universal object representations. Additionally, a scene-level block position regression pipeline helps learn scene representations by utilizing features from the object space. The extensive experiments conducted across various datasets and tasks demonstrate the model's generalization capabilities and overall superiority. The authors plan to release the code for their approach.

### Strengths
1. The writing is clear and easy to understand.
2. The perspective trying to be addressed is both interesting and meaningful.

### Weaknesses
1. In the related work section, only object-level self-supervised methods are summarized, and there is a lack of summary for scene-level self-supervised methods.
2. In the experimental section, comparisons are made only with object-level self-supervised methods, missing comparisons with scene-level self-supervised methods, such as "Masked Scene Contrast: A Scalable Framework for Unsupervised 3D Representation Learning" and "GroupContrast: Semantic-aware Self-supervised Representation Learning for 3D Understanding." This is important because the paper focuses on pre-training for point cloud hybrid-domain.

### Questions
1. Regarding Figure 1 (c), the description in lines 72 to 74 is unclear. It would be best to clearly explain the settings for each data point.
2. In line 208, the normalization process may cause deformations in the local structure of objects, such as height compression or expansion. Will such deformations affect semantic understanding? Since the level of deformation may vary for two chairs in different scenes, could this interfere with semantic comprehension?
3. In line 243, what the content embedding and position embedding of the queries are? My understanding is that you add the transformed point block features to a randomly initialized content embedding; so where does the position embedding come into play?
4. The paper lacks comparison with the other object-level and scene-level self-supervised methods on inference time and FLOPs.

### Soundness
2

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
4

### Summary
The paper presents PointHD-MAE, a model designed to bridge the gap between object and scene point cloud domains. The model uses a hybrid-domain structure with distinct encoders for each domain, employing a novel block-to-scene pre-training strategy to enhance generalization. This strategy involves reconstructing random point blocks in object space and regressing their positions in scene space to learn both object and scene-level features.

### Strengths
1. The paper proposes a new framework to combine scene and object-level point cloud self-supervised learning.

2. The writing is well-organized, clear, and easy to follow.

### Weaknesses
1, Although the idea of combining scene and object levels for pre-training is well-motivated, it does not introduce any novel elements.

2, The detection results on ScanNetV2 are impressive. However, the results on SUN-RGBD appear incremental, which is puzzling given that SUN-RGBD is generally easier compared to ScanNetV2. The performance on SUN-RGBD is still far from state-of-the-art, suggesting significant room for improvement.

3, I believe the paper leverages the Point-MAE baseline from RECON [1], but this is not mentioned, raising concerns. Consequently, the improvement in the classification task appears incremental.

4, The ablation study is insufficient. The paper does not adequately demonstrate the effectiveness of object-level, scene-level, and combined pre-training strategies.

5, There are no visualization results provided.

[1] Contrast with Reconstruct: Contrastive 3D Representation Learning Guided by Generative Pretraining

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces PointHDMAE, a hybrid-domain masked autoencoder designed for robust self-supervised learning on 3D point clouds across both object and scene domains. By implementing a "block-to-scene" pretraining strategy, the model uses randomly selected point blocks within scenes to train separate encoders for object and scene representation, enhancing the model's generalizability without additional domain-specific adaptation. Experimental results reveal the effectiveness of PointHDMAE in various downstream tasks, including object classification, scene detection, part segmentation, and point cloud completion​.

### Strengths
1. The hybrid-domain architecture effectively addresses the challenge of generalizing across different point cloud types, a limitation in many prior models.
2. The block-to-scene pretraining strategy is innovative, offering a structured approach to learning detailed object and scene representations concurrently.
3. Extensive experimentation demonstrates the model's robustness and improved accuracy across multiple tasks and datasets, affirming the approach’s versatility.

### Weaknesses
1. The approach relies on computationally intensive pretraining, especially with multiple encoders and the need for numerous point blocks, which could limit scalability.
2. The fixed frequency of selected point blocks might restrict adaptability to varied data densities and contexts within scenes.

### Questions
1. How sensitive is the model’s performance to the number of point blocks used during training, and could an adaptive block selection improve efficiency?
2. In real-world applications, how does PointHDMAE handle varying scene complexities and point cloud densities, particularly in less structured environments?

### Soundness
3

### Presentation
3

### Contribution
3
