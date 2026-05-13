# CO-MOT: Boosting End-to-end Transformer-based Multi-Object Tracking via Coopetition Label Assignment and Shadow Sets

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Existing end-to-end Multi-Object Tracking (e2e-MOT) methods have not surpassed non-end-to-end tracking-by-detection methods. One potential reason is its label assignment strategy during training that consistently binds the tracked objects with tracking queries and then assigns the few newborns to detection queries. With one-to-one bipartite matching, such an assignment will yield an unbalanced training, \textit{i.e.}, scarce positive samples for detection queries, especially for an enclosed scene, as the majority of the newborns come on stage at the beginning of videos. Thus, e2e-MOT will be easier to yield a tracking terminal without renewal or re-initialization, compared to other tracking-by-detection methods. To alleviate this problem, we present Co-MOT, a simple and effective method to facilitate e2e-MOT by a novel coopetition label assignment with a shadow concept. Specifically, we add tracked objects to the matching targets for detection queries when performing the label assignment for training the intermediate decoders. For query initialization, we expand each query by a set of shadow counterparts with limited disturbance to itself. With extensive ablations, Co-MOT achieves superior performance without extra costs, \textit{e.g.}, 69.4\% HOTA on DanceTrack and 52.8\% TETA on BDD100K. Impressively, Co-MOT only requires 38\% FLOPs of MOTRv2 to attain a similar performance, resulting in the 1.4$\times$ faster inference speed. Codes are attached for re-implementation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper tackles end-to-end Transformer-based multiple-object tracking. Previous methods, such as TrackFormer and MOTR, face issues with imbalanced distribution in detection and tracking label assignments, where most objects are assigned to track queries, leaving only a few “newborns” for detection queries. This joint training approach results in weaker detection performance compared to tracking-by-detection methods. To resolve this, the paper proposes a coopetition label assignment strategy to re-balance assignments between track and detection queries. Additionally, it introduces a shadow set that changes the original one-to-one mapping in DETR to a one-to-set mapping, further enhancing tracking performance. Results on various benchmarks demonstrate the effectiveness of this method.​

### Strengths
1. The paper is well-written, with a clear and logical structure that makes it very easy to follow.

2. The observation on the disproportional assignment of track and detection queries is insightful, highlighting an important yet often overlooked issue in transformer-based MOT. This analysis provides valuable context for the community.

3. The proposed coopetition label assignment strategy is simple and effective. The paper also demonstrates its effectiveness on multiple Transformer-based MOT frameworks, including TrackFormer and MOTR.

4. The experiments are thorough, covering multiple benchmarks, including more large-scale autonomous driving scenes such as BDD100K, and demonstrating the method’s robustness and practical impact.

### Weaknesses
1. To solve the issue of disproportional assignment of track and detection queries, there are also other simpler alternatives. A straightforward option would be to train detection queries jointly on image detection datasets alongside video tracking datasets. For example, detection queries could be trained exclusively on image datasets, treating every object as a new object. An ablation study comparing proposed methods to this simple joint training alternative is appreciated.

2. The paper uses the first 5 decoders to train with all queries, while the last one trains separately on detection and tracking queries. An ablation study could clarify whether a different arrangement, such as using the first decoder for track queries and the last five for all queries, would impact performance. An ablation study regarding this would be helpful for readers to understand the optimal configuration.

3. The applicability of the coopetition label assignment strategy is mostly limited to cases where there is more video data than image data for training, leading to an imbalance in track and detection query assignments. However, in many practical settings, the opposite is true—large-scale [1] and open-vocabulary MOT tasks [2] often have substantially more image detection data than video tracking data. In these cases, common practice in MOT is to use joint training with both image and tracking data, which provides sufficient supervision for detection queries. This is contrary to the paper’s analysis, and it would be beneficial for the authors to also at least discuss these more common scenarios.

### Questions
The main experiments are still concentrated on small-scale pedestrian tracking datasets. As mentioned on weakness, for other scenarios, we may face different difficulties. Are there any plans to test the model also on large-scale MOT datasets such as TAO [3]?

[3] Dave, Achal, et al. "Tao: A large-scale benchmark for tracking any object." Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part V 16. Springer International Publishing, 2020.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the limitations of existing e2e-MOT methods, particularly the unbalanced training issue caused by the label assignment strategy. And it introduces a Coopetition Label Assignment (COLA) strategy and a Shadow Set concept. Through extensive experiments on multiple datasets, it demonstrates superior performance compared to state-of-the-art methods while being more efficient.

### Strengths
1. The analysis about the drawbacks of exist e2e-trackers is very interesting, it reveals the negative impact of tracking queries on detection queries.

2. The proposed COLA strategy allows tracked objects to be reassigned to detection queries in decoders, resulting in a significant improvement in tracking performance.

### Weaknesses
1. From the public records of OpenReview, it can be seen that this paper was submitted to ICLR2024. The reviewers and AC pointed out many weaknesses last year, while authors have made almost no improvements in the latest version. 

2. Many SOTA trackers developed in this year have been overlooked by authors, such as DiffMOT, MambaTrack, TrackSSM, et al. These new methods have made many improvements, and it would be best for the author to provide a comparison with the latest methods.

### Questions
See Weaknesses

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents an innovative end-to-end Multi-Object Tracking (MOT) framework that aims to enhance transformer-based MOT models. The authors introduce two key contributions: 1. Coopetition Label Assignment (COLA) revises label assignment by allowing detection queries to utilize tracked objects during training in intermediate decoders. This approach boosts feature augmentation for tracking objects with diverse appearances and alleviates the issue of tracking termination. Shadow Set Strategy aims to address training imbalance in one-to-one matching, CO-MOT introduces "shadow sets," which add slight disturbances to each query, thus allowing one-to-set matching. This enhances the discriminative training process and the model's generalization.The proposed method outperforms existing e2e-MOT models on benchmarks like DanceTrack and BDD100K with improved tracking metrics such as HOTA and TETA, demonstrating higher efficiency and inference speed.

### Strengths
The paper's strengths lie in its originality, quality, clarity, and significance. It introduces a novel coopetition-based label assignment (COLA) and shadow sets for one-to-set matching, enhancing the robustness of e2e-MOT without requiring additional detectors. The evaluation across multiple datasets, including ablation studies, demonstrates the effectiveness of CO-MOT, establishing its advantages over state-of-the-art models. The paper is well-structured, with clear explanations and helpful visualizations, although further clarification on certain technical aspects could enhance understanding. Overall, CO-MOT significantly improves the efficiency and performance of transformer-based multi-object tracking, making it a valuable contribution to the field.

### Weaknesses
While the paper presents valuable contributions, several weaknesses could be addressed to strengthen its impact and clarity:
1. The authors should provide a detailed discussion of the differences between COLA and TALA in Section 2.4, as well as their design in the loss function, to facilitate reader understanding. Specifically, the explanation should clarify how the matching cost is computed in both methods, and how the different matching strategies affect the gradient flow during training. It is crucial to understand the exact mathematical formulation of the loss function for each method, and how the coopetition aspect is implemented in the loss calculation.

2. In the experiments section, the authors need to include comparisons with more methods on the MOT20 and BDD100K datasets. The current comparisons are limited, and expanding the range of compared methods would provide a more comprehensive evaluation of the proposed approach. It is important to compare against both end-to-end and traditional tracking methods to demonstrate the advantages and disadvantages of the proposed method.

3. Since the authors analyze the impact of tracking queries on detection performance in transformer-based trackers, if this point serves as one of the motivations, they should compare whether the proposed framework shows improvement in mAP in the experiments. The paper should include a detailed analysis of how the tracking queries influence detection performance, and whether the proposed method leads to improved detection accuracy, especially in challenging scenarios with occlusions or cluttered backgrounds.

4. The authors should also analyze the effects of different values of $\lambda$ and $\Phi$ in Section 2.5 on the experimental outcomes. A sensitivity analysis of these parameters is necessary to understand their impact on the overall performance of the method. The analysis should include a discussion of how these parameters affect the trade-off between detection and tracking performance, and provide guidelines for selecting optimal values for different datasets.

### Questions
I have listed my concerns and questions in Weakness part and hope the response from authors.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces CO-MOT, a novel method aimed at improving end-to-end Transformer-based multi-object tracking (e2e-MOT) through a new coopetition label assignment strategy (COLA) and the introduction of shadow sets. The authors address the issue of unbalanced training in existing e2e-MOT methods, where detection queries often lack positive samples, particularly for newborn objects.

### Strengths
- The motivation of the paper is interesting and clearly demonstrated by the experiments.

- The introduction of COLA and shadow sets do mitigate the biased label assignment issue in e2e-MOT. This proposed approach provides a balanced training process, leading to improved performance.

- The authors conduct experiments on three datasets, demonstrating the effectiveness of CO-MOT across different scenarios. The results are robust and consistent, showing improvements over the baseline.

### Weaknesses
 - The introduction of shadow sets and the coopetition label assignment strategy may increase the computational complexity and training time. The authors should provide a detailed analysis of the computational overhead and discuss potential optimizations. Notably, Fig.4 in the manuscript only presents the Flops, which is not the actual training and inference time. Intuitively, more object queries would bring larger computation costs. Why do shadow sets not?


- Although the proposed method demonstrates strong performance on the tested datasets, it would be advantageous to evaluate CO-MOT on MOT20. The authors assert that the proposed approach enhances detection recall. Thus, the more densely populated nature of MOT20 provides a more suitable context for assessing the effectiveness of the model.


- The authors should investigate the sensitivity of the proposed method to hyperparameters, such as the number of shadow sets and the parameters of the coopetition label assignment strategy. Understanding how these hyperparameters affect performance would provide valuable insights for practical implementation.


- The writing should be improved. For instance, in Fig.3 and Fig.4, the axis titles are overlapped with the axis. The readability of Figures 3 and 4 could be improved by adjusting the axis labels to avoid overlap. This would enhance the overall presentation of the results.

### Questions
- Could the authors provide a detailed analysis of the cost brought by shadow sets?
- Could the authors provide the evaluation and discussion on MOT20.

### Soundness
2

### Presentation
1

### Contribution
2
