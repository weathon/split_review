# Event Camera Object Detection at Arbitrary Frequencies

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
\vspace{-0.1cm}
    Event cameras offer unparalleled advantages for real-time perception in dynamic environments, thanks to their microsecond-level temporal resolution and asynchronous operation. Existing event-based object detection methods, however, are limited by fixed-frequency paradigms and fail to fully exploit the high-temporal resolution and adaptability of event cameras. To address these limitations, we propose \flexevent{}, a novel event camera object detection framework that enables detection at arbitrary frequencies. Our approach consists of two key components: \textbf{FlexFuser}, an adaptive event-frame fusion module that integrates high-frequency event data with rich semantic information from RGB frames, and \textbf{FAL}, a frequency-adaptive learning mechanism that generates frequency-adjusted labels to enhance model generalization across varying operational frequencies. This combination allows our method to detect objects with high accuracy in both fast-moving and static scenarios, while adapting to dynamic environments. Extensive experiments on large-scale event camera datasets demonstrate that our approach surpasses state-of-the-art methods, achieving significant improvements in both standard and high-frequency settings. Notably, our method maintains robust performance when scaling from $20$ Hz to $90$ Hz and delivers accurate detection up to $180$ Hz, proving its effectiveness in extreme conditions. Our framework sets a new benchmark for event-based object detection and paves the way for more adaptable, real-time vision systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Summary: 

The authors present FlexEvent, a pioneering framework for event camera object detection that leverages the high temporal resolution and asynchronous operation of event cameras. By integrating an adaptive event-frame fusion module (FlexFuser) with a frequency-adaptive learning mechanism (FAL), FlexEvent overcomes limitations of existing methods that rely on fixed-frequency paradigms. This enables the model to detect objects with high accuracy across various operational frequencies, demonstrating robustness in both fast-moving and static scenarios.

### Strengths
Strengths:

1 The FlexFuser module effectively combines the rich spatial and semantic information from RGB frames with the high temporal resolution of event data. The approach to sample event data at different frequencies during training is particularly commendable, allowing the model to retain the benefits of high-frequency data during inference while maintaining efficiency.

2 The FAL module enhances the framework by generating frequency-adaptive labels for unlabeled high-frequency data. This self-training approach improves model generalization and robustness across varying operational frequencies, which is a notable advancement in the field.

### Weaknesses
Weaknesses:

1 The overall architecture in Figure 2 does not clearly illustrate the process of feature fusion at different frequencies, specifically the $(i) _ {hfuse}=(i) _ {hfuse}^a+(i) _ {hfuse}^b $ mentioned at the end of section 3.2 on Event-Frame Adaptive Fuser. The description lacks detail on how the features $^{(i)}h_{fuse}^a$ and $^{(i)}h_{fuse}^b$ are generated before being summed, and how this summation is integrated into the overall network architecture. Additionally, there seems to be an issue with the representation of Eq (2). Since $i$ represents different scales, the inputs to the network for all scales except the initial one which corresponds to $E^a$, $E^b$, $F$, should correspond to $(i-1) _ {hE}^a$, $(i-1) _ {hE}^b$, and $(i-1) _ {hF}^a$. The current notation does not clearly show the flow of information across scales, making it difficult to understand the multi-scale fusion process.

2 In section 3.3, the formula related to pre-training with low-frequency labels lacks numbering, which may confuse readers. This formula is critical as it corresponds to the FAL part of Figure 2, and its lack of explicit identification makes it harder to follow the explanation of the frequency-adaptive learning mechanism. The absence of a number also makes it difficult to reference this equation in later parts of the paper.

3 The experiments presented in section 4.2 are somewhat disorganized. The evaluation methods across the three datasets (DSEC-Det, DSEC-Detection, DSEC-MOD) differ, and it is unclear how comparisons are made consistently. For instance, in DSEC-Det, only the proposed method and DAGr are tested, while the results in DSEC-Detection compare against CAFR, necessitating a clearer presentation. The lack of a consistent set of baselines across all datasets makes it challenging to assess the true performance of the proposed method. It is also unclear why certain methods were chosen for specific datasets and not others, which raises questions about the fairness of the comparisons.

4 There is a discrepancy in the reported number of training iterations between section 4.1 and supplementary material A.3, with one stating 100,000 iterations and the other citing 200,000. This inconsistency should be rectified to ensure clarity. Such discrepancies undermine the reproducibility of the results and raise concerns about the rigor of the experimental setup.

### Questions
Could the authors clarify the rationale behind selecting specific datasets and methods for testing, and how this impacts the validity of their findings?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces FlexEvent, an innovative joint object detection framework that utilizes both events and frames to enable object detection at arbitrary frequencies, leveraging the high temporal resolution of event cameras. The proposed FlexEvent incorporates two key modules. The first FlexFuser adaptively combines high-frequency events with rich frame textures. The second FAL generates frequency-adjusted labels to enhance model performance across various operational frequencies. The results show that FlexEvent outperforms current state-of-the-art methods, achieving significant gains in high-frequency detection settings.

### Strengths
1) The relevant background knowledge of this paper is clearly explained.

2) The topic of object detection using events and frames at arbitrary frequencies is very interesting topic.

3) The authors conducted extensive experiments to validate the effectiveness of FlexEvent across multiple large-scale event-based object detection datasets. FlexEvent achieves significant improvements in mAP performance compared to existing SOTA methods and demonstrates the capability to detect objects at arbitrary frequencies.

### Weaknesses
1. In the contributions section, the authors claim to be the first to address arbitrary-frequency object detection using event cameras. This phrasing could be more precise, and I recommend refining it in the camera-ready version. I recognize this as an important topic for practical applications of event cameras. Some prior works have explored high-frequency inference by combining events and frames, such as CovGRU for arbitrary-frequency depth estimation [1] and asynchronous fusion modules for arbitrary-frequency object detection [2]. The claim of being the 'first' needs to be carefully qualified, as these existing methods also tackle aspects of high-frequency or varying-frequency processing, even if their primary focus differs. The novelty should be framed more accurately in light of these existing works.

2. In Table 1, the authors report a high mAP of 0.574 on the DSEC-Det dataset. Could you clarify the number of classes used for this evaluation? Is it two classes or eight? The appendix states eight classes for DSEC-Det. Please provide clarification on this point. The discrepancy between the main paper and the appendix regarding the number of classes is concerning and needs to be addressed to ensure reproducibility and accurate interpretation of the results. The specific classes used should also be explicitly stated.

3. The writing could be improved, particularly in Section 3.1, where the background and motivation would be more appropriate in the Introduction or Related Work sections. The current placement disrupts the flow of the methodology section. The background information should be presented earlier to provide context for the proposed approach.

### Questions
Please see weakness. Now, I give a preliminary score based on the initial manuscript and will consider adjustments depending on the authors' responses and feedback from other reviewers.

### Soundness
3

### Presentation
3

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
The paper introduces FlexEvent, an object detection framework for event cameras that operates across varying frequencies. It features two main components: 1. FlexFuser: An adaptive event-frame fusion module that integrates the high temporal resolution of event data with the rich semantic information from RGB frames, enhancing detection accuracy. 2. FAL (Freq-Adaptive Learning): A mechanism that generates frequency-adjusted labels, enabling the model to generalize across different frequencies and improve high-frequency detection through training.

### Strengths
The FlexEvent framework shows strong performance in handling varying frequencies, particularly in dynamic and fast-changing environments, as demonstrated in specific datasets that combine event data and RGB frames. Its advantage lies in the effective fusion of event cameras' high temporal resolution with the rich semantic information from RGB frames, which enhances detection accuracy in scenarios where both data modalities are available. The integration of frequency-adaptive learning allows the model to generalize well across different operational conditions, showing robust performance in high-frequency scenarios on multimodal datasets like DSEC-Det, DSEC-Detection, and DSEC-MOD.

### Weaknesses
One weakness of FlexEvent is that the comparison with other models may not be entirely fair, as many of the compared methods are trained on datasets that use only event data, where the data distribution, camera setups, and number of modalities differ. This discrepancy in experimental setup can lead to significant performance differences, making it harder to evaluate FlexEvent's true advantage. Since most of the other comparison methods are trained on the 1Mpx and Gen1 datasets, the authors should clearly state in the main text whether the comparison methods are retrained on DSEC-Det, DSEC-Detection, and DSEC-MOD.  The authors should ensure consistency in the training modalities of all models, comparing them either exclusively in the Event-RGB mode or using purely event-based training.

Another potential weakness is that the FAL in FlexEvent closely resembles existing methods such as EventDrop [1] and Shadow Mosaic [2]. Fundamentally, all these techniques focus on altering the event data’s density during training. By manipulating the frequency or sparsity of event data, FlexEvent's approach may not provide significant innovation beyond these existing techniques. This similarity raises the question of whether the improvement in performance comes more from an established method of adjusting event density, rather than from a novel or more advanced detection strategy. The authors could provide more ablation studies and visualization results to compare whether FAL shows significant differences from other data augmentation methods.

The authors should provide the network's latency, parameter count, and computational cost, as other event camera object detection networks do, to enable a fairer performance comparison.

### Questions
It is a well-established fact that objects generally do not move significantly within a few milliseconds. Based on this premise, is changing the frequency and adjusting the event sparsity through data augmentation essentially the same? When addressing the issue of missed detections at low frequencies, is it more the RGB information that compensates for this, rather than the method you proposed?

Unlike other papers, this article does not provide the model’s inference time, particularly how it varies across different frequencies. I am curious to know whether the inference time can be kept within the range of the input event data.

### Soundness
2

### Presentation
3

### Contribution
2
