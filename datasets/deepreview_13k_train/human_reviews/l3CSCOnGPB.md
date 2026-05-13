# Learning Semantic-Enhanced Dual Temporal Adjacent Maps for Video Moment Retrieval

- Decision: Reject
- Scores: 3, 3, 6, 6

## Abstract
Retrieving a specific moment from an untrimmed video via a text description is a central problem in vision-language learning. It is a challenging task due to the sophisticated temporal dependency among moments. Existing methods fail to deal with this issue well since they establish temporal relations of moments in a way that visual content and semantics are coupled. This paper studies temporal dependence schemes that decouple content and semantic information, establishing semantic-enhanced Dual Temporal Adjacent Maps for video moment retrieval, conferred as DTAM. Specifically, DTAM designs two branches to encode visual appearance and semantic knowledge from video clips respectively, where knowledge from the appearance branch is distilled into the semantic branch to help DTAM distinguish features with the same visual content but different semantics with a well-designed semantic-aware contrastive loss. Besides, we also develop a moment-aware mechanism to assist temporal adjacent maps' learning for better video grounding. Finally, extensive experimental results and analysis demonstrate the superiority of the proposed DTAM over existing state-of-the-art approaches on three challenging video moment retrieval benchmarks, i.e., TACoS, Charades-STA, and ActivityNet Captions.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies temporal dependence schemes that decouple content and semantic information, establishing semantic-enhanced Dual Temporal Adjacent Maps for video moment retrieval, conferred as DTAM. Specifically, DTAM designs two branches to encode visual appearance and semantic knowledge from video clips respectively, where knowledge from the appearance branch is distilled into the semantic branch to help DTAM distinguish features with the same visual content but different semantics with a well-designed semantic-aware contrastive loss. Besides, a moment-aware mechanism is also developed to assist temporal adjacent maps' learning for better video grounding. Finally, extensive experimental results and analysis demonstrate the superiority of the proposed DTAM over existing state-of-the-art approaches on three challenging video moment retrieval benchmarks, i.e., TACoS, CharadesSTA, and ActivityNet Captions.

### Strengths
1. This paper tries to address the sophisticated temporal dependency among moments, which leads to an inability to encode temporal dependencies between moments that are crucial for moment retrieval. Therefore, it proposes semantic-enhanced Dual Temporal Adjacent Maps (DTAM) for effective video grounding.
2. The proposed DTAM achieves satisfactory performance on three public datasets.

### Weaknesses
0. The novelty of this paper is somewhat limited. Temporal Adjacent Map strategy was proposed in AAAI 2019 and became a popular trick for video moment retrieval. The proposed Dual Temporal Adjacent Maps method seems to incrementally modify the previous work, without any substantive theoretical analysis. Besides, the contrastive learning strategy is a normal and commonly-sued tricks.

1. Why don't the authors leverage the pre-trained semantic space provided by popular VLMs for feature alignment? Such visual and textual features from VLMs offer rich semantic knowledge and, compared to I3D/C3D and LSTM features, provide better semantic alignment. It is important for matching appropriate video clips with queries. 

2. Moreover, the paper states, "Previous video moment retrieval method ignore the flexibility and complexity of moment description, resulting in an inability to encode temporal dependencies between moments that are crucial for moment retrieval." The viewpoint needs to be supported in the experiments or with reference to other published results. Specifically, how are complex queries (e.g., those containing "again" as mentioned before) defined, and for samples containing these complex queries, what are the evaluation results of the current methods compared to the proposed DTAM?

3. What distinguishes the appearance temporal adjacent map from the semantic temporal adjacent map, and what are their respective roles? And how is temporal and semantic decoupling accomplished?

4. A previous study [1] suggests that current video moment retrieval approaches, influenced by dataset distribution, lead models to learn dataset-specific biases. What are the similarities and differences between the motivations of this work and those of the proposed DTAM? Additionally, it would be beneficial to evaluate the model's performance on Charades-CD and ActivityNet-CD.

### Questions
Please refer to the weakness part, especially the novelty issue.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper addresses the challenge of retrieving specific moments from untrimmed videos using text descriptions by proposing the semantic-enhanced Dual Temporal Adjacent Maps (DTAM) framework. DTAM consists of two branches: one for encoding visual appearance and the other for encoding semantic knowledge from video clips. The visual appearance branch distills information into the semantic branch, enabling DTAM to distinguish features with identical visual content but differing semantics through a semantic-aware contrastive loss. Furthermore, a moment-aware mechanism is introduced to improve the learning of temporal adjacent maps for enhanced video grounding. Extensive experiments demonstrate that DTAM outperforms existing state-of-the-art methods across three benchmarks: TACoS, Charades-STA, and ActivityNet Captions.

### Strengths
- This paper models temporal dependencies between moments in a decoupled appearance-semantic manner, enabling differentiation between instances that have similar appearances but different semantics.
- Experiments demonstrate its effectiveness.

### Weaknesses
 - The paper presents challenges in aligning descriptions, such as stating that "the semantic branch absorbs semantic knowledge from the appearance branch via the semantic-aware contrastive loss." However, Eqn. (7) still uses the embedding from the appearance branch; how is knowledge distillation reflected in this? Additionally, why is the appearance branch used for positive and negative sample classification instead of the semantic branch?
- In Section 3.5, the paper introduces a moment-aware mechanism aimed at enhancing the semantics of temporal adjacent maps by emphasizing the importance of each moment. However, it appears that this moment-aware mechanism is only applied to the semantic branch.
- The main contribution of this paper lies in the introduction of the contrastive loss function and the probability constraints on the start and end points in the maps. However, since contrastive loss is a common approach in cross-modal retrieval for enforcing semantic alignment, the only significant contribution appears to be the introduction of the start and end point probability values, which seems relatively weak for ICLR.
- In the experiments, specifically in the ablation study, what do the symbols APB, MAM, and SEB refer to?
- Lacking comparison with the work "SnAG: Scalable and accurate video grounding" CVPR 2024.

### Questions
- The paper presents challenges in aligning descriptions, such as stating that "the semantic branch absorbs semantic knowledge from the appearance branch via the semantic-aware contrastive loss." However, Eqn. (7) still uses the embedding from the appearance branch; how is knowledge distillation reflected in this? Additionally, why is the appearance branch used for positive and negative sample classification instead of the semantic branch?
- In Section 3.5, the paper introduces a moment-aware mechanism aimed at enhancing the semantics of temporal adjacent maps by emphasizing the importance of each moment. However, it appears that this moment-aware mechanism is only applied to the semantic branch.
- The main contribution of this paper lies in the introduction of the contrastive loss function and the probability constraints on the start and end points in the maps. However, since contrastive loss is a common approach in cross-modal retrieval for enforcing semantic alignment, the only significant contribution appears to be the introduction of the start and end point probability values, which seems relatively weak for ICLR.
- In the experiments, specifically in the ablation study, what do the symbols APB, MAM, and SEB refer to?
- Lacking comparison with the work "SnAG: Scalable and accurate video grounding" CVPR 2024.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel model for video moment retrieval, DTAM, which introduces dual temporal adjacent maps to enhance retrieval accuracy. It designs a semantic-aware contrastive loss that clusters features for the same query while distancing those for different queries, and incorporates a moment-aware mechanism to further strengthen the temporal adjacent maps. Through systematic experiments on three benchmark datasets and ablation studies, the paper thoroughly analyzes and validates the contributions of each module.

### Strengths
This article has advantages in the following ways:
1.  The paper introduces the Dual Temporal Adjacent Maps (DTAM) model, which decouples visual and semantic information for video moment retrieval. This design allows the model to effectively distinguish between moments that are visually similar but semantically different, addressing the limitations of traditional methods that couple visual and semantic features. 
2.  Innovative Structure Design: The paper introduces the Dual Temporal Adjacent Maps (DTAM) model, which decouples visual and semantic information for video moment retrieval. This design allows the model to effectively distinguish between moments that are visually similar but semantically different, addressing the limitations of traditional methods that couple visual and semantic features. 
3.  The introduction of the moment-aware mechanism allows the model to dynamically adjust the importance of video segments. This mechanism strengthens the representational power of the temporal adjacent maps in the video moment retrieval task, enabling better capture and modeling of temporal relationships in videos.

### Weaknesses
I think this is a convincing paper. The research questions are all reasonable. However, I believe that some improvements can be made.
1. The formatting of the tables and images on pages 6 and 7 of the paper is not aesthetically pleasing. Could you consider realigning and reformatting them?  For example, the interval between table 1 and table 2 should be widened.
2. The Introduction section in Chapter 1 states that "To this end, we propose a semantic-enhanced Dual Temporal Adjacent Maps (DTAM) for effective video grounding..." uses “video grounding”, but “video moment retrieval” used in subsequent articles. It is recommended to unify the entire text.  Video Moment Retrieval is recommended, as this is also the usage of most articles.
3.  It is unclear what knowledge the two branches have actually learned. The paper suggests that one branch focuses on appearance and the other on semantics, but this seems to be a subjective interpretation.  The paper lacks explicit supervisory signals to ensure that each branch focuses on either visual or semantic features, and there is no interpretability analysis or ablation studies to demonstrate that the branches have indeed learned their claimed distinct features.  I recommend that the authors address this issue in the manuscript. You can visualize the feature map and illustrate its results

### Questions
Clarification on Branch Specialization: The paper states that one branch focuses on visual appearance while the other emphasizes semantic information. However, there is no explicit supervisory signal in the model to ensure that each branch indeed specializes in its respective area. Could the authors provide clarification on how they ensure this specialization during training?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces an approach, Dual Temporal Adjacent Maps (DTAM), for enhancing video moment retrieval. DTAM separates visual appearance and semantic information, addressing issues in current methods that struggle to distinguish similar-looking moments with different meanings. DTAM uses two branches to encode visual and semantic features, with the appearance branch feeding signals to the semantic branch to improve differentiation. Additionally, a moment-aware mechanism is developed to optimize the model’s attention to relevant moments. Experiments on three video retrieval benchmarks demonstrate DTAM’s superior performance, highlighting its effectiveness in capturing complex temporal and semantic dependencies.

### Strengths
1. DTAM’s approach of separating visual appearance and semantic information addresses a key challenge in video retrieval, allowing the model to distinguish moments that look similar but have different meanings.
2. The moment-aware mechanism in DTAM enhances the model’s sensitivity to specific moments by dynamically focusing on relevant segments.
3. The paper presents extensive experiments on three challenging benchmarks, where DTAM consistently outperforms state-of-the-art methods.

### Weaknesses
While DTAM achieves impressive retrieval accuracy, its dual-branch structure and moment-aware mechanism may increase computational demands. This complexity could limit its scalability and efficiency when applied to large-scale video datasets.

### Questions
Given DTAM’s dual-branch structure and additional moment-aware mechanism, which add complexity, what specific optimizations or architectural choices contribute to its minimal increase in inference time compared to simpler models like 2D-TAN?

### Soundness
3

### Presentation
3

### Contribution
3
