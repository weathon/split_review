# OVTR: End-to-End Open-Vocabulary Multiple Object Tracking with Transformer

- Decision: Accept
- Avg Score: 5.75
- Scores: 8, 6, 3, 6

## Abstract
Open-vocabulary multiple object tracking aims to generalize trackers to unseen categories during training, enabling their application across a variety of real-world scenarios. However, the existing open-vocabulary tracker, which relies on off-the-shelf open-vocabulary detector, perceives categories and locations independently in each frame, causing instability and making it vulnerable to similar appearances and irregular motion in diverse scenes. In this paper, we propose OVTR (End-to-End Open-Vocabulary Multiple Object Tracking with TRansformer), the first end-to-end open-vocabulary tracker that models motion, appearance, and category simultaneously. To achieve stable classification and continuous tracking, we designed the CIP (Category Information Propagation) strategy, which establishes multiple high-level category information priors for subsequent frames. Additionally, we introduce a dual-branch structure for generalization capability and deep multimodal interaction, and incorporate protective strategies in the decoder to enhance performance. Notably, our method does not require proposals that contain novel categories, yet still achieves strong results on the open-vocabulary MOT benchmark. Moreover, experiment transferring the model to other dataset demonstrates its effective adaptability.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes the first solution for end-to-end open-vocabulary multiple object tracking called OVTR. The model builds on close-set end-to-end multiple object tracker MOTR while extending it to open-vocabulary by adding the category Information Propagation strategy and dual-branch vision-language alignment training. The method achieves good results on open-vocabulary tracking benchmarks and also demonstrates good zero-shot transfer ability to unseen domains.

### Strengths
1. The paper presents the first end-to-end Transformer solution for open-vocabulary tracking that performs joint detection and tracking. This is known to be a hard problem for two main reasons:
   - There is a lack of sufficiently diverse video data to train end-to-end models effectively. Training on a small set of videos for tracking often hurts detection performance. The paper addresses this by augmenting static images for training, demonstrating that this approach can still yield good performance in an end-to-end setup. Although it is not new to use static images for tracking it is rare in end-to-end solutions, especially in open-vocabulary scenarios. 
   - In end-to-end multi-object tracking solutions, queries often perform multiple tasks—tracking, localization, and classification—which is really difficult to balance in open-vocabulary scenarios. The paper’s proposed category and content isolation strategies help balance these tasks, which is a sensible approach.

2. The zero-shot transfer experiments on the KITTI dataset indicate strong performance in association, particularly in terms of the IDF1 metric, showing significant improvement over previous methods like OVTrack.

### Weaknesses
1. The paper is not clearly written and lacks important details. For instance, understanding the overall framework and its training process is challenging. The paper mentions using only static images to train the framework; however, using static images implies there is no separation of new and old objects, which are typically handled differently in MOTR training. This critical aspect is not clearly explained in the paper.

2. The ablation results in Table 3 and Table 4 are confusing and show only marginal improvements over the baseline, especially in association. For example, in Table 4, adding category isolation only improves ClsA_b by 0.6 and ClsA_n by 0.1, while adding content isolation alone only improves 0.1 in AssocA performance. A more detailed explanation is needed here to clarify these results.​

3. Missing latest related works. The paper only compares OVTrack. However, In open-vocabulary tracking, there are some new advancements eg. MASA[1] at CVPR2024. Also, SLAck at ECCV2024, which is also a transformer-based end-to-end approach. Maybe SLAck can be a concurrent work but MASA seems to be fair to discuss.

### Questions
Will the code be public? Since this is the first work that performs end-to-end open-vocabulary object tracking, making the implementation details public is of great importance to the research community.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
In this paper, the authors propose OVTR (End-to-End Open-Vocabulary Multiple Object Tracking with TRansformer), the first
end-to-end open-vocabulary tracker.

Specifically, to achieve stable classification and continuous tracking, they designed the CIP (Category Information Propagation) strategy, which establishes multiple high-level category information priors for subsequent frames. 

They also introduce a dual-branch structure for generalization capability and deep multimodal interaction and incorporate protective strategies in the decoder to enhance performance.

### Strengths
+ The motivation for this work, the flow of category information, is reasonable.

+ This is the first end-to-end framework for open-vocabulary tracking.

+ Experimental results have verified the effectiveness of the proposed method, to some extent.

### Weaknesses
 - The writing of the method part is not easy to follow.

- From the results, we can see that the performance of the proposed method is not very excellent, compared to the basic baseline method OVTrack, not to mention the most recent methods.

- The authors are suggested to present the advantages of the end-to-end Transformer methods compared to the tracking-by-OVD methods, based on the experimental, including the performance, speed, model size, etc.

- The authors claim that due to resource constraints, the ablation studies are conducted on a subset of 10,000 images. This makes the evaluation not very convincing. The overall framework can be implemented on the whole dataset. The ablation study without some components can be also conducted.

- The object category in the KITTI dataset is not various, which is not very appropriate for the OVTrack task. The comparison of OVTrack and the proposed method on KITTI using Car Category is not very convective, for the OVTrack problem.

### Questions
See the weakness.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors present the first application of the Transformer architecture in Open-Vocabulary Multiple Object Tracking. This work simultaneously considers the motion, appearance, and category features of the targets. A novel approach for constructing inter-frame category information flow is proposed, along with a Dual-Branch structure. As a result, an improvement of approximately one point is achieved on the Novel TETA metric of the TAO dataset.

### Strengths
The advantages of this work include the following:

1. It effectively leverages the strengths of the Transformer architecture and strives to apply it to the Open-Vocabulary Multiple Object Tracking (OVMOT) task.
2. The motivation throughout the paper is well-founded, as it integrates motion, appearance, and category features, utilizing category information flow to guide subsequent tracking.
3. The use of a dual-branch structure addresses the issue of increased training data arising from proposals with unknown categories during training. Instead, it employs ground truth to construct supervision, thereby reducing burdensome in training process.

### Weaknesses
Firstly, possibly due to time constraints, I feel that **this paper is not complete**. I read the article twice carefully. During the first read, I thought I had missed many details. However, upon a second, more thorough review, I found that the paper contains **only fragmented descriptions of the training process** and **lacks any explanation of how inference is conducted**.
I believe the potential issues are as follows:

### 1. Unclear Architecture Representation
Figure 2 lacks clarity in its representation. Several concerns need to be addressed:
- The distinction between Position Part and Content Part is not well-defined
- In Figure 3, it's unclear why the Position Part from the Encoder is directly fed as input - is this representing the feature blocks from Image Features or fused features?
- The nature and purpose of the Content Part input need clarification
- There's an unexplained discrepancy between Figure 2 (5 outputs) and Figure 3 (3 outputs)

### 2. Attention Mechanism Implementation
Section 3.3 presents several implementation issues:
- The matrix $I$ is described as a filter for large detection queries in self-attention, but the implementation details are unclear
- The relationship between $O_{txt}$ (final output) and its application in previous self-attention layers needs elaboration
- The specific self-attention layer where the filtering is applied is not specified
- The Content Isolation mechanism needs clarification, particularly regarding:
  - Its operation between detection and track queries
  - The implementation details
  - Whether it uses category features for query filtering

### 3. Dual-Branch Decoder Components
In Section 3.4:
- The origins of matrices $P$ and $O$ are not shown in the Dual-Branch Decoder diagram
- The purpose and utilization of $C^{(t+1)}$ obtained through propagation are not explained in the paper

### 4. Sequential Loss Computation
Section 3.5 presents logical inconsistencies:
- The sudden introduction of $P$ in the Sequential loss computation lacks context
- The relationship between this $P$ and the position part query from Section 3.3 needs clarification
- The connection between $L$ in Equation 6 and $L$ in Equation 5 is ambiguous

### 5. Inference Process
The paper lacks a comprehensive explanation of:
- The complete inference pipeline
- The feature fusion methodology for matching
- The integration of multiple features during inference

### 6. Claims of Mutual Benefits
The authors claim that "Our approach jointly models localization, appearance, and classification, enabling tracking and classification to mutually benefit from each other." However, this mutual benefit is not convincingly demonstrated:
- On the Validation Set:
  - Only ClsA shows improvement for Novel categories
  - Other metrics merely maintain similar performance levels
  - LocA actually decreases by one point
- On the Test Set:
  - Novel category classification improvement is negligible
  - Shows significant asymmetry compared to Validation Set results
  - The claimed mutual benefits are neither stable nor consistently demonstrated

### 7. Weak Experimental Results
The experimental results raise several concerns:
- Minimal improvement of only ~1 point in TETA for Novel categories
- Base TETA results are lower than OVTrack by one point on Validation Set
- The authors' claim of using only Base proposals is questionable given:
  - No improvement in Base category performance
  - Previous methods using unlabeled proposals achieve superior results without requiring additional annotations
  - The only apparent advantage seems to be computational efficiency

### 8. Methodology Clarification Needed
- The specific methodology for generating image sequences through data augmentation requires explanation

### 9. Inconsistency in Training Description
- Section 4.3 states "All methods are trained are trained solely on novel categories"
- This appears to be a typo and should likely read "solely on base categories"
- This inconsistency needs clarification

### 10. Ablation Study Concerns
The ablation experiments only using 10,000 images show:
- Generally low performance metrics compared with the results in Table 1
- Particularly low ClsA for base categories
- Limited discriminative power across different ablation settings

### 11. Visualization Issues
The supplementary materials' visualizations are problematic:
- The pole case example lacks representativeness
- The comparison with OVTrack is unclear (the right-side detection in the first row appears superior)
- The elephant case visualization is ambiguous
- No guidance is provided to help readers interpret the differences
- The dense bounding box visualizations make quality comparison difficult

### Questions
I have included all the questions in the 'Weaknesses section', outlining approximately twelve areas of questions.

### Soundness
1

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
3

### Summary
This paper introduces an End-to-End Open-Vocabulary Multiple Object Tracking with Transformer, OVTR, a novel approach to multi-object tracking (MOT) that extends to handle unseen categories without prior training on those specific categories. The experimental results demonstrate that OVTR outperforms existing state-of-the-art methods in tracking novel categories on standard benchmarks like TAO and KITTI, showcasing its effectiveness and adaptability.

### Strengths
1. End-to-End Architecture: OVTR is the first to propose an end-to-end trainable model for open-vocabulary MOT, which integrates motion, appearance, and category information simultaneously.
2. The introduction of the CIP strategy and the dual-branch structure represent creative combinations of existing ideas in a novel application domain.
3. The technical depth and rigorous experimentation by comparing OVTR with state-of-the-art methods provide a strong empirical basis for the claims made.

### Weaknesses
1. For the experimental results, although OVTR proposed for handling open-vocabulary multi-object tracking tasks demonstrates innovation and advancement, the performance did not meet the high expectations, particularly in terms of localization accuracy. The reported localization accuracy, while showing some improvement, still lags behind what is typically seen in closed-set MOT tasks, suggesting that the model's ability to precisely delineate object boundaries in open-vocabulary scenarios needs further refinement. This is particularly concerning given the importance of accurate bounding box predictions for downstream tasks.
2. The authors should introduce more implementation details and release the source code for reproducibility. The lack of specific details regarding data augmentation techniques, loss functions, and training procedures makes it difficult for the community to replicate the results and build upon this work. This lack of transparency hinders the progress of the field. Furthermore, the absence of source code prevents a thorough evaluation of the model's architecture and its practical applicability.
3. The introduction of a dual-branch structure and multiple attention mechanisms increases the model complexity significantly. This might limit the practical deployment on resource-constrained platforms. The computational cost associated with the dual-branch architecture and the multiple attention layers could pose a significant challenge for real-time applications, especially when deployed on edge devices with limited resources. The authors need to provide a more thorough analysis of the model's computational footprint and its suitability for deployment in resource-constrained environments.

### Questions
1. The end-to-end MOT framework has been explored in MOT task, so what's the main difference with previous methods (such as TransTrack, TrackFormer, MOTR ...)
2. Could the authors provide visual evidence to support the effectiveness of OVTR?  Specifically, it would be beneficial to show comparative visualizations of the tracking process, including scenarios where the model successfully handles rapid motion changes, partial occlusions, and diverse object appearances across different environments.
2. What about the computational efficiency and real-time applicability of the OVTR model? Discussing its performance in terms of tracking speed and resource usage would greatly enhance the understanding of its practical value.

### Soundness
2

### Presentation
2

### Contribution
3
