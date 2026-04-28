# No Pose, No Problem: Surprisingly Simple 3D Gaussian Splats from Sparse Unposed Images

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8

## Abstract
We introduce NoPoSplat, a feed-forward model capable of reconstructing 3D scenes parameterized by 3D Gaussians from \textit{unposed} sparse multi-view images. Our model, trained exclusively with photometric loss, achieves real-time 3D Gaussian reconstruction during inference. To eliminate the need for accurate pose input during reconstruction, we anchor one input view's local camera coordinates as the canonical space and train the network to predict Gaussian primitives for all views within this space. This approach obviates the need to transform Gaussian primitives from local coordinates into a global coordinate system, thus avoiding errors associated with per-frame Gaussians and pose estimation. To resolve scale ambiguity, we design and compare various intrinsic embedding methods, ultimately opting to convert camera intrinsics into a token embedding and concatenate it with image tokens as input to the model, enabling accurate scene scale prediction. We utilize the reconstructed 3D Gaussians for novel view synthesis and pose estimation tasks and propose a two-stage coarse-to-fine pipeline for accurate pose estimation.
Experimental results demonstrate that our pose-free approach can achieve superior novel view synthesis quality compared to pose-required methods, particularly in scenarios with limited input image overlap. 
For pose estimation, our method, trained without ground truth depth or explicit matching loss, significantly outperforms the state-of-the-art methods with substantial improvements. 
This work makes significant advances in pose-free generalizable 3D reconstruction and demonstrates its applicability to real-world scenarios.
Code and trained models are available on our \href{https://noposplat.io/}{project page}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This submission proposes a sparse Gaussian splats prediction given very sparse unposed images. Comparing with prior works such as Master and Splatter, the method achieves good results without using supervision from depth, loss masks, or metric poses.

As this is a strong submission, the only weakness I could think of is that the paper should include quantitative comparisons on geometry reconstruction results with baselines such as Master and Splatter.

In short, my initial recommandation is **accept**, and I am willing to increase it to strong accept if the quantitative comparisons on geometry reconstruction are provided.

### Strengths
* The paper is very well written and easy to follow.
* Good reconstruction and NVS results while no need for depth, loss masks, and metric poses comparing with prior work.
* Good generalization capability on in-the-wild data.

### Weaknesses
It would be great to include quantitative results for geometry reconstruction, comparing it with Master and Splatter. Currenly only qualitative results are provided in Fig. 5.

### Questions
1. Add quantitative results for geometry reconstruction?
2. Clarifying questions (not affecting the paper rating):
    1. It seems like the main difference between this and Splatter is using / not using depth supervision and metric poses, which leads to an "impression" that using depth supervision would limit the dataset choices and hence constrain the GS prediction performance?
    2. L838-840: "Using the ground truth intrinsic during training also causes failure". I assume this is about training Splatter failed using the ground truth intrinsics?
    3. What is the training hardware and training time?
    4. The proposed method also loaded pre-trained Master weights, are they frozen or fine-tuned?
3. Related work: maybe worth adding another concurrent work: ReconX (not affecting the paper rating)

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a fast feed-forward model for sparse-view 3D reconstruction that is generalizable across scenes. Differently from recent work, the predictions (3DGS parameters) are performed in a common coordinate space directly without requiring any pose info. They perform evaluations on the RealEstate10k and ACID datasets and show improved performance over prior works. Their method also shows zero-shot generalizability to other datasets and in-the-wild scenarios. They also show relative pose estimation using a two-step approach: first with pnp and then with photometric optimization. The performance is benchmarked on similar datasets as well.

### Strengths
The proposed method is simple and easy to understand. More specifically, the highlighted advantages are:
- A simple VIT approach is competitive to pretrained ViT backbones from Dust3r, and Mast3r when overlap is minimal.
- The method does not require any ground-truth depth (explicit matching loss) during training thus allowing it to scale further. This is an important advantage since simple architectures w/ large datasets is a recipe for improving generalizability.
- Using pretrained Mast3r weights with pure photometric losses on more datasets is a good strategy to scale up training and improve model performance on nvs and relative pose estimation.

### Weaknesses
The canonical space motivation: The central argument of the paper is that predicting the scene structure in a common coordinate space improves scene geometry and multi-view cohesion compared to local prediction->global fused prediction approach. Although I agree with this statement, the paper does not exploit this advantage:
  * Given two views (which is the only input setting shown in the paper), the method still predicts per-pixel per-view 3DGS fields in a common coordinate (similar to Splatt3r). This is similar to Dust3r pointcloud variants where the pointclouds are predicted in a common coordinate space. I fail to see how this part is different from Dust3r-style prediction. Can you explain how this approach differs from those in the 2-view setting, if at all?
  * The main advantage seems to come from finetuning the Mast3r backbone on more data using photometric loss alone. By directly predicting 3DGS fields, this approach can improve overall model performance. But this orthogonal to the motivation of the method. It would be good to highlight this as one of the main features of this method

This approach is quite similar to Splatt3r although it is concurrent work. The advantage of this approach is that it does not need ground-truth depth during training which is important.

- Contribution no. 4 is not a contribution. 
- Multi-view (N>2): Are there any qualitative results for input images more than 2? What would the upper limit on this be given compute constraints? How does the cross-attention in the ViT decoder work for this case since L215 mentions "features from each view interact with those from all other views.."? Also, adding qualitative and quantiative results for N>2 and performance tradeoff cuves would strengthen this method.
- L274: "By default, we utilize the intrinsic token option". This needs to be "Global Intrinsic Embedding - Concat option".
- Table 1, Fig4: Why is Dust3R and Mast3r part of the NVS comparison since they were never trained for novel view synthesis? What was the evaluation protocol for these methods? 
- In Fig4, its possible that the Gaussian structure masks the actual geometry of the scene when comparing to pointcloud outputs of Dust3r. To show geometry, it would be better to either show 3D points or depth maps. To show NVS, it would be better to remove Dust3r output since it is not a fair comparison.
- Discrepancy in metrics:
  * Both MVSplat and pixelSplat report higher PSNR numbers for RealEstate10k and ACID datasets. Since the same train-test split was used, why is there a huge discrepancy in the 'Average' column of the metrics?
  * Table 4: why might be the Splatt3r numbers lower than those reported in the original paper?
- Mentioning the training time and compute requirements would be useful additions to the paper.

Appendix
- Tab. 6 ablation does not provide the complete picture. The NVS metrics are dependent on the accuracy of the 3DGS field. Since the 3DGS parameter head is randomly initialized irrespective of the backbone, its contribution due to backbone initialization might not be as pronounced. A more accurate ablation would be on pose estimation given pure 3D points. 
- L773, L775 typo. "experiences" -> experiments

### Questions
- Contribution no. 4 is not a contribution. 
- Multi-view (N>2): Are there any qualitative results for input images more than 2? What would the upper limit on this be given compute constraints? How does the cross-attention in the ViT decoder work for this case since L215 mentions "features from each view interact with those from all other views.."? Also, adding qualitative and quantiative results for N>2 and performance tradeoff cuves would strengthen this method.
- L274: "By default, we utilize the intrinsic token option". This needs to be "Global Intrinsic Embedding - Concat option".
- Table 1, Fig4: Why is Dust3R and Mast3r part of the NVS comparison since they were never trained for novel view synthesis? What was the evaluation protocol for these methods? 
- In Fig4, its possible that the Gaussian structure masks the actual geometry of the scene when comparing to pointcloud outputs of Dust3r. To show geometry, it would be better to either show 3D points or depth maps. To show NVS, it would be better to remove Dust3r output since it is not a fair comparison.
- Discrepancy in metrics:
  * Both MVSplat and pixelSplat report higher PSNR numbers for RealEstate10k and ACID datasets. Since the same train-test split was used, why is there a huge discrepancy in the 'Average' column of the metrics?
  * Table 4: why might be the Splatt3r numbers lower than those reported in the original paper?
- Mentioning the training time and compute requirements would be useful additions to the paper.

Appendix
- Tab. 6 ablation does not provide the complete picture. The NVS metrics are dependent on the accuracy of the 3DGS field. Since the 3DGS parameter head is randomly initialized irrespective of the backbone, its contribution due to backbone initialization might not be as pronounced. A more accurate ablation would be on pose estimation given pure 3D points. 
- L773, L775 typo. "experiences" -> experiments

### Soundness
3

### Presentation
3

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
This paper proposes a feed-forward generalizable GS method from sparse and unposed images. It encodes images (with known intrinsics) into feature tokens and use a decoder with cross-attention layers for cross-view feature fusion. Then the gaussians are predicted in a canonical space. The proposed method is evaluated on RealEstate10K/ACID and tested generalization on DTU.

### Strengths
- The paper proposes a simple and straightforward method.
- The paper is well-written and is easy to follow.
- The method shows a good performance, which is even better than previous pose-aware methods, e.g. MVSplat.

### Weaknesses
1. This paper is technically sound. However, basic literatures in this field are not discussed and the claimed novelty have already been studied in prior works. I don't understand why the authors ignore these works when the content and techniques are closely related. Please see details below.
- PF-LRM [1] and LEAP [2] are the two earliest works for pose-free reconstruction, but none of them are mentioned. Almost all claimed novelty of the submssion, e.g. canonicalization, PnP pose estimation, using cross-attention for cross-view feature fusion, have already been studied in these two works (also true for DUST3R). The only difference is whether using 3DGS or NeRF as the 3D representation (which is actually also studied in GS-LRM [3] and GRM [4], see below). However, I don't think this is a solid contribution for a publication.
- Besides, the architecture of the proposed work is almost the same with GS-LRM [3] with only two differences of design choice: (1) whether using a ViT encoder or directly tokenizing the images; (2) whether using cross-attention or using concatenation and self-attention for feature fusion. This is also true for GRM [4].

The paper is a direct combination of these previous works (pose-free feed-forward NVS from sparse-views + feed-forward 3DGS prediction).

- Moreover, methods that use latent 3D representations [5,6,7] (SRT is the first pose-free NVS method), reconstruction using sparse-view pose estimation methods [8,9,10,11] and more scene-specific/optimization-based pose-free methods [12] should be discussed.

2. Moreover, there some other weaknesses as follows.
- Inappropriate baselines. DUST3R is not designed for NVS but for reconstruction with point cloud. Evaluating NVS performance on DUST3R is misleading. This is also the same for MAST3R/Splatt3R. If you want to compare with these works, please compare the geometry quality, i.e. point cloud error, rather than NVS performance. Moreover, DUST3R and its following works don't require camera intrinsics.
- Unfair comparison. The proposed method is trained on a joint set of RealEstate10K, DL3DV and ACID, while all the baselines are trained on a different training dataset. Moreover, the model uses the weight initialization of models trained on large dataset (MAST3R/DUST3R/Croco).

3. As there are not a lot directly comparable works on scene-level, I require the authors to include additional five experiment results.
- On object-level, train the proposed model using the same data with the previously mentioned pose-free works and compare their performance. This also verifies whether MAST3R weight initialization generalize to object-level data.
- On scene-level, train with only RealEstate10K+ACID for comparing with MVSplat.
- On scene-level, train a variant of the proposed model, which is also conditioned on the camera poses of inputs (using the plucker ray representation rather than 6D pose representation). If the performance gap is small enough, the model has a strong capability of correlating the two images with the missing poses.
- On scene-level, ablate the weight initialization by training with no weight initialization (from MAST3R/DUST3R/Croco) using the current training set (ACID+RealEstate10K+DL3DV). This experiment ablates whether the pose-free inference capability comes from initialization or your model learning process. Please include results for both pose-free and pose-conditioned variants of your model.

4. Besides, the authors should notify that during training, the method still requires camera poses for rendering. 

5. Camera intrinsics are still needed during inference. The proposed way of merging camera intrinsic information is the same as LRM/PF-LRM, but no discussion.

6. The method is only tested with two views, while the author claim "sparse-view". The authors should perform experiments with more input views, e.g. up to 6-8 views, to support the claim. Otherwise, you should rename the paper as "unposed two images".

### Questions
Please first see comments above. 

**It is necessary to discuss prior works in an appropriate way.** I will give a reject first but I can raise the score to 5 if the author can differentiate their work from the missing related works and rephrase their contribution. 

**Besides, I strongly require the authors to perform experiment using the same training dataset with previous works.** For example, if you want to compare with MVSplat, you should only train on RealEstate10K+ACID. This is the correct way of doing scientific research. Otherwise, we cannot tell whether the performance gain comes from better model design or using larger and high-quality data (and also your MAST3R weight initialization should be ablated). The additionally used datasets in this paper are all from available resources and there is no need for data curation. It is different from LLM research where data collection and curation and be their contribution, and, thus, it is acceptable to directly compare LLMs trained using different data.

I can raise the score to 6 or higher scores if the authors performs the asked three experiments (weakness 3) with promising results.

### Soundness
3

### Presentation
2

### Contribution
1
