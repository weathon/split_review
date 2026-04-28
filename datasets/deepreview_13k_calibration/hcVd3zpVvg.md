# MV3D-MAE: 2D Pre-trained MAEs are Effective 3D Representation Learners

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Deep learning's success relies heavily on the availability of extensive labelled datasets. Compared to 2D data, acquiring 3D data is substantially more expensive and time-consuming. Current multi-modal self-supervised approaches often involve converting 3D data into 2D data for parallel multi-modal training, thereby ignoring the prior knowledge contained within extensively trained 2D models. Therefore, it is important to find ways to utilize 2D feature priors to facilitate the learning process of 3D models. In this paper, we propose MV3D-MAE, a masked autoencoder framework that utilizes a pre-trained 2D MAE model to enhance 3D representation learning. Initially, we convert single 3D point clouds into multi-view depth images. Building on a pre-trained 2D MAE model, we adapt the model for multi-view depth image reconstruction by integrating group attention and incorporating additional attention layers.  Then we propose a differentiable 3D reconstruction method named Mv-Swin, which maps the reconstructed results back to 3D objects without the use of camera poses, thereby learning 3D spatial representations. Thus, MV3D-MAE, through the bidirectional transformation between 2D and 3D data, mitigates the differences between modalities and enhances the network's representational performance by leveraging the prior knowledge in the pre-trained 2D MAE. Our model significantly improves performance in few-shot classification and achieves SOTA results in linear Support Vector Machine classification. It also demonstrated competitive performance in other downstream tasks of classification and segmentation in synthetic and real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduces MV3D-MAE, a novel masked autoencoder framework aimed at enhancing 3D representation learning by leveraging pre-trained 2D models. The authors address the challenge of costly 3D data acquisition by converting 3D point clouds into multi-view depth images, enabling the use of a pre-trained 2D MAE model. MV3D-MAE includes a differentiable 3D reconstruction module that reconstructs the depth images back into 3D point clouds without camera poses, thus enabling bidirectional transformation between 2D and 3D modalities.

### Strengths
1, The writing is clear, and easy to follow.
2. The experiments conducted are thorough and comprehensive.

### Weaknesses
1, The framework does not seem to make sense to me. In my view, it resembles a 2D encoder pre-training framework rather than a 3D encoder pre-training one, as its ultimate aim is to use multi-view 2D images to reconstruct 3D objects.

2, The results are incremental. Despite leveraging complex frameworks, the fine-tuning results on ScanObjectNN fall short compared to I2P-MAE, another 3D self-supervised learning method designed to utilize 2D foundation models. Additionally, ACT [1], a highly related approach, is not compared in this paper.

3, The comparison is unfair. The architecture of this method differs from the Point-MAE baseline. A fair comparison should involve Point-MAE with the same network architecture.

### Questions
How is the model fine-tuned? Which components are retained, and which are discarded during the fine-tuning process?

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
5

### Summary
This paper leverages a pre-trained 2D MAE in point cloud representation learning by for- and back-ward rendering of multi-view depth images. The proposed method achieves SoTA performances across several tasks. Some module analysis and key results are missing.

### Strengths
1.  Testing on incomplete data and cross-modality retrival is a nice trial.
2.  By using a pre-trained 2D MAE, the model significantly enhances 3D feature learning capacity, yielding SoTA performances.

### Weaknesses
1. The module to reconstruct multi-view depth images to point cloud is waird and somewhat redundant, as a simple depth projection might yield similar results; the authors should validate this experimentally by replace it with mv-depth image projection. The claim of no pose information requirement (L86) is also questionable, as poses are manually set during depth map generation.
2. Training costs of the proposed method is high, which may harm it generalizability. Please provide and compare the model parameter amount and FLOPs.
3. The simulation of real-word data is still not enough. Trend analysis between the noise-level or completeness and the final performances are needed.
4. Qualitative and quantitative results are desired, espically the failure case analysis.

### Questions
Please refer to the weakness.

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
The paper introduces MV3D-MAE, a framework designed to improve 3D representation learning by leveraging pre-trained 2D models. Since acquiring 3D data is more expensive and time-consuming than 2D data, the authors propose converting 3D point clouds into multi-view depth images. They enhance a pre-trained 2D MAE model with group attention and additional layers for reconstructing these depth images. Their method, Mv-Swin, then maps these reconstructions back into 3D without using camera poses, facilitating better 3D spatial learning. This approach significantly boosts performance in few-shot classification, achieving state-of-the-art results in various tasks such as classification and segmentation across synthetic and real-world datasets.

### Strengths
1. The paper is clearly written.
2. The proposed method is effective, which leverages a pretrained 2D model for 3D learning and introduces MV-Swin for smooth 2D-to-3D transitions, resulting in superior few-shot classification performance.

### Weaknesses
1. The experiments are conducted mainly on ModelNet and ScanObjectNN, which are quite simple. How about the results on ShapeNet55-34 and ShapeNetPart? It would be interesting to see whether the proposed method is effective for the long-tail classification problem.
2. Missing comparison to the latest SOTA:
- Point-JEPA: A Joint Embedding Predictive Architecture for Self-Supervised Learning on Point Cloud. [arXiv 2404.16432]
- PointGPT: Auto-regressively Generative Pre-training from Point Clouds. [NeurIPS 2023]

### Questions
Please refer to the weaknesses.

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
5

### Summary
This paper presents MV3D-MAE, a masked autoencoder framework that utilizes pre-trained 2D MAE models to enhance 3D representation learning. First, a single 3D point cloud is converted into a multi-view depth image. Based on the pre-trained 2D MAE model, the model is adapted to multi-view depth image reconstruction by integrating group attention and adding additional attention layers. A differentiable 3D reconstruction method, Mv-Swin, is then proposed, which learns 3D spatial representations by mapping the reconstruction results back to 3D objects without the use of camera poses. As a result, MV3D-MAE mitigates the differences between modalities by bi-directional conversion between 2D and 3D data and enhances the network's representational performance by utilizing a priori knowledge from pre-trained 2D MAEs.

### Strengths
1. The introduction section of the paper is better written and clearly motivated, and the key question of the paper is formulated by analyzing the existing research. ‘Can a method leveragepre-trained 2D MAE networks, facilitating mutual transformation between 2D and 3D, to achieve self-supervised pre-training for 3D representation?’
2. Unlike previous 2D-3D or 3D-2D mappings, the group attention module and MV-Swin module proposed in this paper can make the mapping process microscopic, which facilitates the information transfer between modalities.
3. From the description of the method section, this paper mainly adds network components to the existing 2D MAE model to make it suitable for 3D MAE learning. It is simpler in content, but has greater potential in application, which is in line with the idea of MAE.

### Weaknesses
1. It is recommended that the italicized mathematical symbols A and M in Section 3.2 be changed to uppercase Roman symbols. Moverover, it is suggested that the paper add formulas to show how 3D-2D and 2D-3D microprojections are realized.
2. Although the experimental part of the thesis is similar in kind to the related methods, it is suggested that comparison methods can be added. Also, it is suggested that the proposed method be validated on three variants of ScanObjectNN.
3. In the ablation experiments, $\lambda$ is the weighting term for the 3D reconstruction loss. In general, there is chance in such parametric experiments. It is proposed to further analyze how this hyperparameter affects the experiments. For example, the effect of 3D point cloud reconstruction when $\lambda$ is transformed.

### Questions
1. Why do you only do 2D masking for depth maps? According to all I have, point clouds can be projected as RGB images, and it is recommended to refer and cite CrossNet (TMM'2023) and Inter-MAE (TMM'2023), which fuel 3D self-supervised learning by extracting color image features. Also, it is optional to add them as comparison methods.
2. In Fig. 3, why should all the results obtained be the same when the query Q matrix is repeated and then maximized?

Overall, this is a practice-oriented work, which is not fully compatible with the ICLR theme. If the authors would consider my comments and make explanations and modifications, I might improve my score further. And vice versa.

### Soundness
3

### Presentation
2

### Contribution
3
