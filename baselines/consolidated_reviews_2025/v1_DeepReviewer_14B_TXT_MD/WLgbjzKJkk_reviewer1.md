### Summary

This paper studies the end-to-end Transformer-based multi-object tracking. The authors propose a coopetition label assignment for training tracking and detection queries. Besides, the authors develop a one-to-set matching strategy with a novel shadow concept to ease the one-to-set optimization. The experimental results show the effectiveness of the proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper is well-written and easy to understand.
2. The motivation is reasonable and convincing.
3. The experimental results demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The authors do not provide the comparison with TrackFormer on BDD100K and MOT17 datasets.
2. The proposed coopetition label assignment and shadow sets can increase the complexity of the training process. It is better to provide the training time of the proposed method.
3. The proposed method is based on the MOTR framework. It is better to provide the comparison with other frameworks, such as TrackFormer.
4. The proposed coopetition label assignment and shadow sets are not novel.

### Suggestions

The paper introduces a coopetition label assignment strategy (COLA) and a shadow set concept to improve end-to-end Transformer-based multi-object tracking. While the motivation behind these ideas is reasonable, the paper lacks a thorough analysis of the computational overhead introduced by these components. Specifically, the authors should provide a detailed breakdown of the training time, not just the overall training time, but also the time spent on the COLA and shadow set operations. This would allow for a better understanding of the trade-offs between performance gains and computational costs. Furthermore, it would be beneficial to see a comparison of the training time with and without these proposed components, which could be included as an ablation study. This would help to quantify the exact overhead introduced by the proposed method and allow for a more informed assessment of its practicality.

Additionally, the paper's evaluation is limited by its focus on the MOTR framework. While MOTR is a relevant baseline, the absence of comparisons with other prominent frameworks, such as TrackFormer, raises concerns about the generalizability of the proposed method. The authors should consider evaluating their approach on other transformer-based MOT frameworks to demonstrate its broader applicability. This would involve adapting the proposed COLA and shadow set concepts to the architecture of TrackFormer and reporting the performance results. Such an analysis would provide a more comprehensive understanding of the method's strengths and weaknesses and its potential for integration into different tracking systems. It would also help to clarify whether the performance gains are specific to the MOTR framework or if they can be generalized to other architectures.

Finally, while the authors present the coopetition label assignment and shadow sets as a novel combination, the individual components are not entirely new. The paper would benefit from a more detailed discussion of how the proposed method differs from existing approaches that use similar concepts. For example, the authors should clearly articulate the specific differences between their shadow set concept and other similar techniques used in object detection and tracking. This would help to clarify the novelty of the proposed method and its contribution to the field. Furthermore, a more thorough literature review would be beneficial to identify any related work that may have explored similar ideas, and to highlight the unique aspects of the proposed approach.

### Questions

Please refer to the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
