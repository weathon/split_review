# Position-Query-Based Autoencoders for View Decoupled Cross Point Cloud Reconstruction and a Self-Supervised Learning Framework

- Decision: Reject
- Scores: 5, 5, 8, 5, 8

## Abstract
Point cloud learning, especially in a self-supervised way without manual labels, has received emerging attention in both vision and learning communities, with its potential utility in wide areas. Most existing generative approaches for point cloud self-supervised learning focus on recovering masked points from visible ones within a single view. Recognizing that a two-view pre-training paradigm inherently introduces greater diversity and variance, it could thus enable more challenging and informative pre-training. Inspired by this, we explore the potential of two-view learning in this domain. In this paper, we propose Point-PQAE, a cross-reconstruction generative paradigm that first generates two decoupled point clouds/views and then reconstructs one from the other. To achieve this goal, we develop a crop mechanism for point cloud view generation for the first time and further propose a novel positional encoding to represent the 3D relative position between the two decoupled views. The cross-reconstruction significantly increases the difficulty of pre-training compared to self-reconstruction, which enables our method to achieve new state-of-the-art results and surpasses previous single-modal self-reconstruction methods in 3D self-supervised learning by a margin. Specifically, it outperforms self-reconstruction baseline (Point-MAE) 6.5\%, 7.0\%, 6.7\% in three variants of ScanObjectNN with Mlp-Linear evaluation protocol. Source code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors recognize and explore a two-view pre-training paradigm and propose PointPQAE, a cross-reconstruction generative framework. PointPQAE first generates two decoupled point clouds/views and then reconstructs one from the other. Additionally, PointPQAE achieves new state-of-the-art results, surpassing previous single-modal self-reconstruction methods in 3D self-supervised learning.

### Strengths
1. The writing is clear and easy to understand.
2. The authors conducted numerous experiments to verify the feasibility of the method.

### Weaknesses
1. In some metrics, the method performs similarly to PointM2AE, so I find the claim that it "surpasses previous single-modal self-reconstruction methods in 3D self-supervised learning by a large margin" to be overly bold.

2. After reading the introduction, I am still somewhat confused as to why this design works: (1) Why is Part 1 able to recover its own structural information through the structural information of Part 2? What if Part 1 and Part 2 do not overlap at all? (2) What is the approximate overlap ratio between Part 1 and Part 2? Could you provide statistical data on this?

3. Limited novelty: The core idea of cross-reconstruction has already been evident in numerous previous works [1][2][3], making it difficult for me to identify any particularly compelling innovation in this study.

### Questions
See the weaknesses.

### Soundness
2

### Presentation
3

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
The paper proposed a novel cross-reconstruction self-supervised pretraining method, which generate two vieww of original point cloud and train masked autoencoder to reconstruct one view by taking the inputs of another. The proposed method combine both contrastive learning and MAE learning into a single framework and demonstrate SOTA performance on few shot segmentation tasks.

### Strengths
1. This self-supervised training paradigm is quite intriguing. It combines contrastive learning with MAE-based completion to achieve better results.

2. The experiments conducted by the authors are highly convincing. The results in Table 4 demonstrate the benefits of decoupling views for representation learning, which can inspire future work.

### Weaknesses
1. In contrastive learning in image domain, the image augmentations typically preserve the main part of the image in different view, whereas in this setting,  the cropped point clouds often represent parts of an object. This will loses some contextual information. It's unclear why this limited information is sufficient to reconstruct the local part of point cloud from another view. This aspect needs further explanation.
2. There is some similar self-supervised approach has been proposed in the image domain, such as [1, 2]. Though they focus on different domain, the authors should consider discussing their difference in terms of learning framework in the related work section.
3. The core idea of cross-view reconstruction appears to have limited novelty, as the information from view2 is likely leaked into the features of view1 during the decoding process. This makes the approach not fundamentally different from single-view reconstruction methods, despite the authors' claims. The experimental results do not convincingly demonstrate the benefits of this cross-view approach over simpler alternatives.

### Questions
Why does this self-supervised paradigm significantly improve classification tasks (table 2), but offer limited improvements in segmentation tasks (table 3)?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes Point-PQAE, a novel SSL framework for 3D point cloud data. Unlike traditional single-view reconstruction, Point-PQAE uses cross-reconstruction, generating two decoupled views of the same point cloud and reconstructing one from the other. This approach leverages relative positional encoding and a position-aware query module, leading to enhanced performance on 3D object classification and segmentation tasks. The framework demonstrates significant improvements over previous SSL methods.

### Strengths
1. The idea of using cross-reconstruction is nice.
2. The performance gain is meaningful.
3. Overall presentation/writing is very good.

### Weaknesses
I think this paper has no major flaws.
Please see the questions.

### Questions
1. Can this approach (i.e., cross-recon) is applicable to image or text domain? Or are there similar works in those modalities?

2. I am curious about the impact of increasing the cross-reconstruction branch. For example, can the authors test triple-recon setting by partitioning the original point cloud into three different views?

3. Line 247, missed "." after RPE.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this paper, the authors address the prevalent generative masking schemes used for pre-training 3D point cloud data by introducing a novel cross-reconstruction generative paradigm. This method significantly increases the pre-training challenge by reconstructing one cropped point cloud through another, contrasting with the simpler self-reconstruction methods. To facilitate this, a positional encoding is introduced to represent the 3D relative positions between the two point clouds.

### Strengths
1, The paper proposes a new framework to successfully bring cross-reconstruction to 3D generative field for point cloud self-supervised learning.

2. The writing is well-organized, clear, and easy to follow.

3. The experiments conducted are thorough and comprehensive.

### Weaknesses
 1, The view construction approach does not make sense to me. In my opinion, using one part to reconstruct another within a block is merely a specific case of block usage. The paper does not adequately explain why this approach is fundamentally different from standard block masking techniques, which also involve reconstructing one portion of the point cloud from another. The distinction between 'parts' and 'views' is not clearly defined, and the justification for treating them differently is weak. It seems that the proposed method simply applies a different form of masking, rather than introducing a novel view construction strategy.

2, The training framework lacks novelty. It introduces only a new relative position encoding (RPE) module and a cross-attention module in the decoder. The overall architecture is largely based on existing methods, with the main changes being the addition of these two modules. The cross-attention mechanism is a standard technique, and the RPE, while potentially useful, does not represent a significant departure from existing positional encoding methods. The paper does not demonstrate a substantial architectural innovation.

3, Relative position encoding is not a new concept [1, 2], and there is no specific adaptation for the 3D scenario in this work. The paper does not provide a detailed explanation of how the RPE is adapted for 3D point clouds. It is unclear whether the RPE is simply applied in a straightforward manner or if there are any modifications to account for the unique characteristics of 3D data. The lack of specific adaptation for 3D scenarios raises concerns about the novelty and effectiveness of this component.

4, The results are questionable. Point-DAE [3] has shown that adding augmentation is highly effective for 3D MAE tasks, achieving 88.69 on PB-T50-RS. However, in the ablation study, using only absolute position embeddings achieves just 87.7. This raises doubts about the effectiveness of the proposed 'multi-view' learning and cross-attention. What if we simply add the learned relative embedding to Point-DAE instead?

### Questions
See weakness part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The work proposed Point-PQAE, a cross-reconstruction generative framework for self-supervised learning. The input point cloud is randomly cropped to generate two views. Then, the proposed positional query block extracts relative geometric relations to help the recontruction of one view from the other view. Extensive experiments are conducted and prove that Point-PQAE achieves good performance on multiple benchmarks.

### Strengths
1. Inspiring attempt. While other works focus on single-view reconstruction, this work attempts to recontruct one view from the other view, which is more diffucult. The experiment results show that this is a good attempt, and this work may inspire more researchers.
2. Thorough experiments. Multiple downstream tasks are performed, and the work acheives satisfying results.

### Weaknesses
N/A

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3
