# SparseLGS: Fast Language Gaussian Splatting from Sparse Multi-View Images

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5

## Abstract
3D semantic field learning is crucial for applications like autonomous navigation, AR/VR, and robotics, where accurate comprehension of 3D scenes from limited viewpoints is essential. Existing methods struggle under sparse view conditions, relying on inefficient per-scene multi-view optimizations, which are impractical for many real-world tasks. To address this, we propose SparseLGS, a feed-forward method for constructing 3D semantic fields from sparse viewpoints, allowing direct inference of 3DGS-based scenes. By ensuring consistent SAM segmentations through video tracking and using low-dimensional indexing for high-dimensional CLIP features, SparseLGS efficiently embeds language information in 3D space, offering a robust solution for accurate 3D scene understanding under sparse view conditions. In experiments on two-view sparse 3D object querying and segmentation in the LERF and 3D-OVS datasets, SparseLGS outperforms existing methods in chosen IoU, Localization Accuracy, and mIoU. Moreover, our model achieves scene inference in under 30 seconds and open-vocabulary querying in just 0.011 seconds per query.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a feed-forward method that uses only a few viewpoints to construct 3D semantic fields. SAM segmentations are used for consistent video tracking and CLIP features are used to embed language information in 3D space for open-vocabulary capability. Experimental performance show that the proposes method outperforms existing approaches in the LERF and 3D-OVS datasets.

### Strengths
This is a well-written and easy to follow paper with impressive experimental results.

### Weaknesses
My main concern is regarding the limited technical novelty. This paper combines different existing approaches and stitches them together to obtain good results. Feed-forward approaches, integrating language through CLIP features, using SAM segmentations, etc, are all concepts that have been explored before. The multi-view language memory bank that links semantic masks to natural language information has been explored extensively in CLIP-based segmentation networks (eg., [1]). The paper lacks a clear demonstration of how the combination of these existing techniques results in a novel contribution beyond simply applying them in a 3D context. Specifically, the method seems to rely heavily on the pre-trained capabilities of SAM and CLIP, without introducing significant modifications or innovations to these models themselves. The core idea of projecting 2D features into 3D space, while effective, does not present a fundamentally new approach. The paper would benefit from a more in-depth analysis of the limitations of existing methods and how the proposed approach overcomes these limitations in a non-trivial way. The novelty of the method should be more thoroughly justified beyond the empirical results.

### Questions
1. The authors report that 2D Query achieves a higher Chosen IOU as compared to the proposed method in table 6. Some intuition on why that is the case would be useful.

### Soundness
3

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
In 3D semantic field learning, this paper proposes SparseLGS, a feed-forward method for constructing 3D semantic fields from sparse viewpoints, allowing direct inference of 3DGS-based scenes.
The method surpasses state-of-the-art approaches in sparse-view 3D object localization and segmentation tasks with faster speed.

### Strengths
1. This method is the first feed-forward method in 3D semantic field learning. It is more convenient in practice than per-scene multi-view optimizations.
2. The performance and speed of the method are excellent.
3. The  quantitative results are good.

### Weaknesses
1. In the experiment, how many views are used to train the contrastive method? It seems that the performance of LangSplat is much lower than the results reported in the original paper.
2. This method rely on a video tracking models. It would be best if the author could verify the robustness of the method to the tracking model effect, and whether incorrect tracking would seriously affect the final performance.

### Questions
Is this method able to support more pictures as input to obtain more multi-view information ? It seems difficult to learn semantic fields with only two view.

### Soundness
3

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
4

### Summary
The paper proposed a new pipeline that can take in only two-view inputs and reconstruct 3D semantic scene (language Gaussians) with a feed-forward 3DGS pipeline (MVSplat). It also relies on "multi-view language bank" to efficiently query semantic features b linking semantic masks to language features. The authors evaluated the proposed method on sparse-view 3D object localization and segmentation to demonstrate the efficacy of the proposed pipeline.

### Strengths
1) integrated sparse-view gaussian splatting, LangSplat, SAM and video object tracking.
2) "language memory bank" improves query efficiency.
3) evaluation on 3D-OVS shows promising results.

### Weaknesses
1) the technical contributions of this submission is rather limited - it basically integrated MVSplat, SAM, video object tracking and LangSplat. The only novel part is the memory bank which IMO is an incremental improvement to reduce computation complexity in query. 
2) the evaluation session did not compare to recent methods such as:
[1] OpenGaussian: Towards Point-Level 3D Gaussian-based Open Vocabulary Understanding
[2] SplatLoc: 3D Gaussian Splatting-based Visual Localization for Augmented Reality
[3] FastLGS: Speeding up Language Embedded Gaussians with Feature Grid Mapping
3) The ablation study is rather confusing - adding feed-forward model in LangSplat degraded the performance so drastically. I don't see how that is entirely from "semantic feature inconsistencies". Even if it is the case, it is straightforward  to get around it (e.g. first construct 3D then assign semantic features like LangSplat does). Adding Mask Association should address the "inconsistent semantic feature" issues by design, but the results became even worse. It is unclear how the authors conducted these experiments.

### Questions
I'd like the authors to clarify the above weaknesses especially the novelty. I'd appreciate more detailed explanations w.r.t. the ablation study results. I feel the experiments were not properly designed and the results are insufficiently discussed in the submission hence I found it unconvincing and difficult to understand.

### Soundness
3

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
5

### Summary
This manuscript proposes a method for sparse-view open-vocabulary 3D object segmentation and localization based on forward Gaussian representation. The sparse-view capability stems from MVSplat. The association between two sparse-view SAM masks is achieved through video-based tracking. Finally, by establishing a 3D ID and 512D CLIP feature, the Gaussian representation is endowed with open-vocabulary capability.

### Strengths
+ This method achieved SOTA performance under sparse-view configurations. 
+ In writing, easy to follow.

### Weaknesses
1. Method: The method is incremental and combinatorial. (1) The capability of sparse perspective is entirely derived from MVSplat, and I do not believe this is a contribution of SparseLGS. (2) Mask association employs video-based tracking methods that are widely used, such as GaussianGroup, and this approach is not optimal.

2. Fairness of comparison: You provided a YouTube external link video that compared with LangSplat. I found that from the perspective of RGB image rendering, LangSplat performs poorly in novel views, while the high-quality RGB of SparseLGS comes from MVSplat. In LangSplat, appearance and semantics are coupled, and the low-quality appearance also leads to low-quality semantics. Therefore, I believe this comparison is unfair, and your lead over LangSplat may come from MVSplat, which is not your own contribution.

3. Comprehensiveness of comparison: Only one Gaussian-based work was used for comparison, the comparison is weak. There are many open-source Gaussian-based methods that can be used for comparison, such as LEGaussians, GaussianGroup.

4. The experimental setup is unclear and lacks details: the metrics reported in the paper are inconsistent with the official metrics of the comparison methods. However, I couldn’t find any details about how the new metrics were obtained. I can only speculate that they were re-measured on two views.

5. The ablation study (Table 5) provides insufficient information. For example, the performance when using the MA and MV-LMB modules without MVSplat(Feed-forward Model).

6. Table 6, which compares the time efficiency with NeRF-based methods, is unnecessary. Your speed advantage is essentially due to the Gaussian, which has already been demonstrated in previous methods.

### Questions
1. Is the number of objects N in each scene manually set? What is the impact of the accuracy of this parameter on the results?

2. In ablation study Table 5, what is your base configuration? In the other configurations without MA and MV-LMB modules, how are the metrics calculated?

3. In Figure 7, you present an example using "chopsticks and napkins" as a text query. I am curious to know what the results would be if chopsticks or napkins were used as queries individually. Based on the video you provided, it seems that you treated these two objects as one. What is the reason for this? Is it due to the setting of N mentioned before?

4. In the Semantic Parameters Prediction module, why is it necessary to train a Res Block and MLP to obtain the three-dimensional features? Why can’t directly use the color of the RGB space divided into N equal parts as the three-dimensional features of the object?

and Weaknesses 2, 4, 5.

### Soundness
2

### Presentation
3

### Contribution
2
