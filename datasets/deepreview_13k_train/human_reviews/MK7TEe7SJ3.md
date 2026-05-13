# USTAM: UNIFIED SPATIO-TEMPORAL ATTENTION MIXFORMER FOR VISUAL OBJECT TRACKING

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
In this paper, we present a unified spatio-temporal attention MixFormer framework for visual object tracking. Within the vision transformer framework, we design a cohesive network consisting of target template and search region feature extraction, cross-attention utilizing spatial and temporal information, and task-specific heads, all operating in an end-to-end manner. Incorporating spatial and temporal attention modules within the network enables simultaneous feature extraction and emphasis, allowing the model to concentrate on target-specific discriminative features despite changes in illumination, occlusion, scale, camera pose, and background clutter. Stacking multiple non-hierarchical blocks allows meaningful features to be extracted while irrelevant features are discarded from the provided target template and search region. The simultaneous spatio-temporal attention module is employed to accentuate target appearance features and alleviate variation in the object state across frame sequences. Qualitative and quantitative analysis, including ablation tests based on various tracking benchmarks, validates the robustness of the proposed tracking methodology.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a unified spatio-temporal attention mixformer framework for video object tracking (VOT). Specifically, they’re two main contributions stated by the authors: 1) a simple yet effective unified pipeline is proposed for feature extraction, target information integration, and localization estimation within the framework of a ViT network; 2) a spatio-temporal attention module is introduced to more effectively distinguish the target from the complicated background. Experimental results on several popular VOT benchmarks show the proposed approach performs favorably against SOTA trackers.

### Strengths
- The idea seems to be somewhat effective, which can observe some performance improvements on the main VOT benchmarks (e.g., LaSOT and TrackingNet).
- The paper is well organized, which is easy to follow.
- Sufficient related works are discussed in Sec. 2.

### Weaknesses
 - The statement for ‘We present a simple but effective unified VOT pipeline for feature extraction, target information integration, and localization estimation within the framework of a ViT network’ is not really true. This unified framework has already been proposed in previous one-stage trackers, e.g., OSTrack, including all the feature extraction, target interaction and localization in the same ViT framework.
- The contribution in this paper is somewhat incremental. It seems that the proposed framework is still similar to the MixFormer framework, although it uses a ViT-based architecture and considering the previous target state by using the temporal attention module.
- The usage of the temporal attention module is a bit similar to use the Cosine Window (e.g., also used in OSTrack), which also makes the tracker object moves smoothly in consecutive frames. In this paper, the authors make it in a learnable way by using the attention map in the previous frame. But one unsolved problem is about the reliability of the previous target state. If the previous prediction is noisy, the effectiveness of the proposed approach is also questionable. Specifically, if the previous frame's bounding box is inaccurate due to occlusion or fast motion, using its attention map could propagate errors and degrade performance, rather than improve it. The paper lacks a detailed analysis of how the tracker handles such scenarios.
- Missing some essential details and unfair comparison. It is not clear whether the proposed tracker use the pre-trained models. e.g., OSTrack and DropTrack. In Table 2, the authors compare with the OSTrack-384 only trained on GOT-10k training split, while the proposed approach additionally  uses more training data, which is not fair. From Table 3, it seems that the proposed USTAM-B-384 trained on GOT-10K is inferior to OSTrack-384. What’s the reason? Does the compared two approaches use the same pre-trained model?

### Questions
- The statement for ‘We present a simple but effective unified VOT pipeline for feature extraction, target information integration, and localization estimation within the framework of a ViT network’ is not really true. This unified framework has already been proposed in previous one-stage trackers, e.g., OSTrack, including all the feature extraction, target interaction and localization in the same ViT framework.
- The contribution in this paper is somewhat incremental. It seems that the proposed framework is still similar to the MixFormer framework, although it uses a ViT-based architecture and considering the previous target state by using the temporal attention module.
- The usage of the temporal attention module is a bit similar to use the Cosine Window (e.g., also used in OSTrack), which also makes the tracker object moves smoothly in consecutive frames. In this paper, the authors make it in a learnable way by using the attention map in the previous frame. But one unsolved problem is about the reliability of the previous target state. If the previous prediction is noisy, the effectiveness of the proposed approach is also questionable.
- Missing some essential details and unfair comparison. It is not clear whether the proposed tracker use the pre-trained models. e.g., OSTrack and DropTrack. In Table 2, the authors compare with the OSTrack-384 only trained on GOT-10k training split, while the proposed approach additionally  uses more training data, which is not fair. From Table 3, it seems that the proposed USTAM-B-384 trained on GOT-10K is inferior to OSTrack-384. What’s the reason? Does the compared two approaches use the same pre-trained model?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes to track the target object using spatial and temporal attention-based Transformer networks. This paper points out that existing works fail to find the appropriate balance between effective feature extraction and the incorporation of attention modules. They also lack explicit modeling of the relationship between spatial and temporal information. The experiments are conducted based on three widely SOT datasets.

the issues of this work are that:

the idea of incorporating attention mechanisms into the Transformer networks for tracking is not new;
the speed of this tracker is about 30-40+ FPS, which is not fast compared with other SOTA trackers, such as OSTrack;
Considering the limited novelties and regular tracking efficiency, I tend to reject this paper.

### Strengths
This paper proposes to track the target object using spatial and temporal attention-based Transformer networks. This paper points out that existing works fail to find the appropriate balance between effective feature extraction and the incorporation of attention modules. They also lack explicit modeling of the relationship between spatial and temporal information. The experiments are conducted based on three widely SOT datasets.

### Weaknesses
the issues of this work are that:

the idea of incorporating attention mechanisms into the Transformer networks for tracking is not new;
the speed of this tracker is about 30-40+ FPS, which is not fast compared with other SOTA trackers, such as OSTrack;
Considering the limited novelties and regular tracking efficiency, I tend to reject this paper.

### Questions
1. re-organization of the novelties proposed in this work; 
2. showing the real advantages of this work;

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a spatial-temporal attention MixFormer framework for visual object tracking, with experimental results affirming its effectiveness.

### Strengths
The USTAM approach is crafted as an end-to-end VOT network, integrating spatial and temporal attentions.

### Weaknesses
The proposed approach is an incremental improvement of MixFormer tracker. Many of the components in the paper such as MAM block,
asymmetric attention, loss function have already been proposed in MixFormer. The paper lacks a clear delineation of the novel contributions beyond the existing MixFormer architecture. The use of the MAM block as the fundamental building block is not sufficiently justified, and its specific adaptation for spatiotemporal attention is not clearly articulated. The paper does not provide a detailed analysis of how the spatial and temporal attention mechanisms interact within the proposed framework. The dimensions of G_f^i nxn are still unclear given that G_f^i represents the attention map between the search area and the mixed feature, which is a combination of both the search and target areas. The explanation of why only the search region's attention values are used is missing. Furthermore, the rationale behind subtracting a constant value in equation (6) after the softmax operation remains unclear, and its impact on the attention mechanism is not discussed.

### Questions
1. It would be beneficial to allocate a dedicated section to MAM, considering it serves as the primary building block for this approach. Distinguishing between the author's specific contributions and those stemming from MAM can be challenging otherwise.
2. Rearranging the reference section in order of the last name of the first author would enhance searchability.
3. The dimensions of G_f^i nxn don't seem to align. G_f^i represents the attention map between the search area and mixed, which is the combination of both the search and target areas.
4. Figure 1 appears too small to discern the letters effectively.
5. In equation (6), given that g_i,j is the attention map in equation (5), it follows that the sum of each row of G_f_t should be 1 after applying softmax. This operation essentially subtracts a constant value. Could you elaborate on the rationale behind this step?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
